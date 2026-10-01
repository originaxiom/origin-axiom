#!/usr/bin/env python3
"""The sealed run: the torsion of the bidoublet on the product of two periodic curves.

For two non-trivial characters l, eta of a level (eta not l or 1/l) and a character A1, the rank-four module
rho_l(e1) (x) rho_eta(e2) (x) a is, at e1 = e2 = 0, the sum of the characters A1, A2 = A1/l, A3 = A1/eta,
A4 = A1/(l eta).  With a_i = s(A_i) - s(l), b_i = s(A_i) - s(eta) the prediction is

    tau = e1^2 a1 a2 a3 a4 + e2^2 b1 b2 b3 b4 - e1 e2 (a1 b2 a4 b3 + b1 a3 b4 a2) + (third order).

FRAME: on the levels that carry generation-shaped backgrounds, every coupling (A, B) of up, down, lepton, neutrino
type with eta = alpha_A beta_B and A1 = alpha_A, up to PER_LEVEL distinct (l, eta, A1), spread evenly.
FREE: on levels without backgrounds, up to eight triples (l, eta, A1) spread over the characters.

usage:  mass_term.py frame <first> <last> | free <first> <last> | control
"""
import sys, json, itertools, collections, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1444_the_backgrounds_are_ends_of_periodic_curves" / "verification")); sys.path.insert(0, str(HERE))
import curve_engine as ce
from mpmath import mp, mpf, mpc, matrix, det, eye, zeros, inverse, svd_c, lu_solve, nstr, exp, pi
mp.dps = 60

FRAME = [("-LR", 3), ("+LLR", 3), ("+LRR", 3), ("-LLRLR", 1), ("-LRLRR", 1), ("-LLLRLR", 1), ("-LRLRRR", 1), ("+LLLRR", 2), ("-LLLRR", 2), ("+LLRRR", 2),
         ("-LLRRR", 2), ("+LLLLLR", 2), ("-LLLLLR", 2), ("+LRRRRR", 2), ("-LRRRRR", 2), ("+LR", 4)]
FREE = [("+LR", 2), ("-LR", 1), ("-LLR", 2), ("-LLLR", 1), ("+LLRLR", 1), ("-LLLRR", 1), ("+LLRLRR", 1), ("-LLRLRR", 1)]
CONTROL = [("+LR", 3)]
PER_LEVEL = 24
H = mpf("1e-5")
SECT = [("Q", 1, 3), ("uc", -4, 3), ("ec", 6, 3), ("dc", 2, 1), ("L", -3, 1), ("nuc", 0, -5)]
PAIRS = [("up", "Q", "uc"), ("down", "Q", "dc"), ("lepton", "ec", "L"), ("neutrino", "L", "nuc")]

def kron(A, B):
    n, m = A.rows, B.rows; K = zeros(n * m)
    for i in range(n):
        for j in range(n):
            for k in range(m):
                for l in range(m): K[i * m + k, j * m + l] = A[i, j] * B[k, l]
    return K
def torsion_n(Phi, h, T):
    """det(1 - Phi^* | H^1(F; V)) for a module of any rank given on x, y and the meridian"""
    n = T.rows
    for c in (1, 2):
        e = T * h[c] * inverse(T) - ce.wordmat(Phi[c], h)
        assert max(abs(e[a, b]) for a in range(n) for b in range(n)) < mpf(10) ** (-25), "not a module"
    xx, xy, _ = ce.fox(Phi[1], h); yx, yy, _ = ce.fox(Phi[2], h); Ti = inverse(T)
    P = zeros(2 * n); blocks = ((Ti * xx, Ti * xy), (Ti * yx, Ti * yy))
    for I in range(2):
        for J in range(2):
            for a in range(n):
                for b in range(n): P[n * I + a, n * J + b] = blocks[I][J][a, b]
    Bm = zeros(2 * n, n)
    for a in range(n):
        for b in range(n): Bm[a, b] = h[1][a, b] - (a == b); Bm[n + a, b] = h[2][a, b] - (a == b)
    U, S, Vh = svd_c(Bm, full_matrices=True)
    assert abs(S[n - 1]) > mpf(10) ** (-20), "invariants on the fibre"
    Q = zeros(n, 2 * n)
    for r in range(n):
        for c in range(2 * n): Q[r, c] = U[c, n + r].conjugate()
    QP = Q * P; Pb = QP * (Q.H * inverse(Q * Q.H))
    assert max(abs((QP - Pb * Q)[i, j]) for i in range(n) for j in range(2 * n)) < mpf(10) ** (-25), "the monodromy preserves the coboundaries"
    return det(eye(n) - Pb)

class Curve:
    """a background's curve with its points cached"""
    def __init__(self, eps, word, k, ell): self.B = ce.Background(eps, word, k, ell); self.cache = {}
    def point(self, e):
        key = nstr(e, 30)
        if key not in self.cache: self.cache[key] = self.B.point(e)
        return self.cache[key]
class Level:
    def __init__(self, name, k):
        self.name, self.k = name, k; self.eps = 1 if name[0] == "+" else -1; self.word = name[1:]
        self.Phi = ce.monodromy(self.eps, self.word, k); self.N = N = ce.exponent(self.Phi); self.chars = ce.level_characters(self.Phi, N)
        self.S = {c: ce.slope(self.Phi, c[0], c[1], N) for c in self.chars if c != (0, 0)}; self.curves = {}
    def add(self, a, b): return ((a[0] + b[0]) % self.N, (a[1] + b[1]) % self.N)
    def neg(self, a): return ((-a[0]) % self.N, (-a[1]) % self.N)
    def order2(self, c): return not ((2 * c[0]) % self.N or (2 * c[1]) % self.N)
    def curve(self, ell):
        if ell not in self.curves: self.curves[ell] = Curve(self.eps, self.word, self.k, ell)
        return self.curves[ell]
    def torsion(self, l, eta, A1, e1, e2):
        Cl, Ce = self.curve(l), self.curve(eta); z = exp(2j * pi / self.N)
        p1, g1, T1 = Cl.point(e1); p2, g2, T2 = Ce.point(e2)
        ax = z ** A1[0] / (Cl.B.v[0] * Ce.B.v[0]); ay = z ** A1[1] / (Cl.B.v[1] * Ce.B.v[1])
        return torsion_n(self.Phi, {1: ax * kron(g1[1], g2[1]), 2: ay * kron(g1[2], g2[2])}, kron(T1, T2))
    def predicted(self, l, eta, A1):
        S = self.S; A = [A1, self.add(A1, self.neg(l)), self.add(A1, self.neg(eta)), self.add(self.add(A1, self.neg(l)), self.neg(eta))]
        if any(c == (0, 0) for c in A): return None
        a = [S[c] - S[l] for c in A]; b = [S[c] - S[eta] for c in A]
        return dict(chars=A, a=a, b=b, c20=a[0] * a[1] * a[2] * a[3], c02=b[0] * b[1] * b[2] * b[3], c11=-(a[0] * b[1] * a[3] * b[2] + b[0] * a[2] * b[3] * a[1]))
    def fit(self, l, eta, A1):
        """the quadratic form at (0, 0): three points at step H and at H/10, one Richardson step"""
        out = []; r = mpf("1e-6")
        M = matrix([[1, r * r, r], [r * r, 1, r], [1, 1, 1]])              # tau / h^2 at (h, rh), (rh, h), (h, h) in terms of (c20, c02, c11)
        for h in (H, H / 10):
            t = [self.torsion(l, eta, A1, h, h * r), self.torsion(l, eta, A1, h * r, h), self.torsion(l, eta, A1, h, h)]
            c = lu_solve(M, matrix([x / h ** 2 for x in t])); out.append((c[0], c[1], c[2]))
        return tuple((10 * b - a) / 9 for a, b in zip(*out))
    def frame_cases(self):
        N, S = self.N, self.S; triv = (0, 0); eq = lambda a, b: abs(a - b) < mpf(10) ** (-20); mul = lambda a, m: ((m * a[0]) % N, (m * a[1]) % N)
        def index(l, al):
            be = self.add(al, self.neg(l))
            if al == triv or be == triv: return 0
            return int(eq(S[al], S[l])) - int(eq(S[be], S[l]))
        bgs = {}
        for th, ps, W in itertools.product(self.chars, repeat=3):
            l = self.add(mul(th, 2), self.neg(W))
            if l == triv: continue
            al = [self.add(self.add(th, mul(ps, sy)), mul(W, (sg - 1) // 2)) for _, sy, sg in SECT]; I = [index(l, a) for a in al]
            if all(i == 1 for i in I[:5]) or all(i == -1 for i in I[:5]): bgs[(l,) + tuple(al)] = (I[0], I[5])
        cases = collections.OrderedDict(); skipped = collections.Counter(); reach = collections.Counter()
        for key, (sign, inu) in sorted(bgs.items()):
            l = key[0]; al = dict(zip([s[0] for s in SECT], key[1:])); types = []
            for typ, A, B in PAIRS:
                if typ == "neutrino" and inu != sign: skipped["neutrino sector does not fire"] += 1; continue
                aA, aB = al[A], al[B]; bB = self.add(aB, self.neg(l)); eta = self.add(aA, bB)
                if eta == triv: skipped["eta trivial"] += 1; continue
                if eta == l or eta == self.neg(l): skipped["eta = l or 1/l"] += 1; continue
                if self.predicted(l, eta, aA) is None: skipped["a character of the bidoublet is trivial"] += 1; continue
                cases.setdefault((l, eta, aA), []).append((typ, sign)); types.append(typ)
            reach[tuple(sorted(types))] += 1
        return len(bgs), cases, skipped, reach
    def free_cases(self):
        smooth = [c for c in self.chars if c != (0, 0)]; out = collections.OrderedDict()
        for i, l in enumerate(smooth):
            for eta in smooth[i + 1:] + smooth[:i]:
                if eta == l or eta == self.neg(l): continue
                for A1 in self.chars:
                    if A1 != (0, 0) and self.predicted(l, eta, A1) is not None: out[(l, eta, A1)] = [("free", 0)]; break
                break
        return out

def run(name, k, mode):
    L = Level(name, k); rec = dict(state=name, k=k, mode=mode, exponent=L.N, torsion=len(L.chars), cases=[])
    if mode == "free": cases = L.free_cases()
    else:
        nb, cases, skipped, reach = L.frame_cases(); rec["backgrounds"] = nb; rec["skipped"] = dict(skipped); rec["distinct_cases"] = len(cases)
        rec["reachable_types_per_background"] = {",".join(t) or "none": c for t, c in sorted(reach.items())}
    keys = list(cases); cap = PER_LEVEL if mode != "free" else 8
    step = max(1, len(keys) // cap); keys = keys[::step][:cap]
    print("%s level %d (%s): %d cases, %d run" % (name, k, mode, len(cases), len(keys)), flush=True)
    for (l, eta, A1) in keys:
        pr = L.predicted(l, eta, A1); c = dict(l=list(l), eta=list(eta), A1=list(A1), uses=sorted(set(cases[(l, eta, A1)])), s_l=nstr(L.S[l], 15), s_eta=nstr(L.S[eta], 15),
                                              a=[nstr(x, 15) for x in pr["a"]], b=[nstr(x, 15) for x in pr["b"]], predicted=[nstr(pr[q], 15) for q in ("c20", "c02", "c11")])
        try:
            got = L.fit(l, eta, A1); c["computed"] = [nstr(x.real, 15) for x in got]; c["imag"] = nstr(max(abs(x.imag) for x in got), 3)
            c["agree"] = bool(all(abs(x - pr[q]) < mpf("1e-6") * max(1, abs(pr[q])) for x, q in zip(got, ("c20", "c02", "c11"))))
        except (AssertionError, ZeroDivisionError) as e:
            c["error"] = str(e)[:120]
        rec["cases"].append(c)
        print("   l=%s eta=%s A1=%s predicted %s computed %s %s" % (l, eta, A1, [nstr(pr[q], 8) for q in ("c20", "c02", "c11")], [nstr(x.real, 8) for x in got] if "computed" in c else [], c.get("agree", c.get("error"))), flush=True)
    return rec

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "control":
        for name, k in CONTROL: json.dump(run(name, k, "frame"), open(HERE / ("mass_control_%s_%d.json" % (name, k)), "w"), indent=1)
    else:
        pop = FRAME if mode == "frame" else FREE
        for i in range(int(sys.argv[2]), min(int(sys.argv[3]), len(pop))):
            name, k = pop[i]; json.dump(run(name, k, mode), open(HERE / ("mass_%s_%02d.json" % (mode, i)), "w"), indent=1)
