#!/usr/bin/env python3
"""THE SLOPE LAW, verified.

M a level of a signed word state, G = F x| <t> its group, mu = t, lam = [x, y].  For a character chi of G that is
trivial on mu and non-trivial on the fibre, H^1(G; chi) is a line and its classes do not vanish on lam.  Let u_chi be
the class with u_chi(lam) = 1 and
                                s(chi) = u_chi(mu),
the SLOPE of chi (the cusp shape of the affine representation g -> [[chi(g), u_chi(g)], [0, 1]]).

FIRING LAW.   For the non-split module V(l, alpha) (sub alpha, quotient beta = alpha / l; l, alpha, beta non-trivial):
                  n(V) = [s(alpha) = s(l)],   V* = V(l, 1/beta),   I = [s(alpha) = s(l)] - [s(1/beta) = s(l)].
COUPLING LAW. For two firing sectors A, B of a background and the spin-0 character eta they couple to, with every
              class normalised on the longitude:      Y(A, B) = s(l) - s(eta)      (eta trivial: Y = -1).

This script computes s exactly over Q(zeta_N) from the definition (no census), and checks
  (1) the firing law on EVERY candidate module of the level, against main's index code (B1427, three primes);
  (2) the vanishing of Y against the sealed run of B1435 (its couplings_*.json);
  (3) the value law at the first prime on every background of both signs, pair by pair.
"""
import sys, json, itertools, collections, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
B1435 = HERE.parents[1] / "B1435_the_interaction_census" / "verification"
sys.path.insert(0, str(B1435))
import interaction_census as ic
from relcup import Bundle, Cocycle, relative_lift, X, Y
import sympy
cc, ac = ic.cc, ic.ac

class Cyc:
    """Q(zeta_N): polynomials modulo the cyclotomic polynomial, rational coefficients"""
    def __init__(self, N):
        z = sympy.Symbol("z"); self.N = N
        self.phi = [Fr(int(c)) for c in reversed(sympy.Poly(sympy.cyclotomic_poly(N, z), z).all_coeffs())]
        self.deg = len(self.phi) - 1
    def red(self, c):
        c = list(c)
        while len(c) > self.deg:
            t = c.pop()
            if t:
                off = len(c) - self.deg
                for i in range(self.deg): c[off + i] -= t * self.phi[i]
        return tuple(c + [Fr(0)] * (self.deg - len(c)))
    def el(self, c): return El(self, self.red(c))
    def zeta(self, e): return self.el([Fr(0)] * (e % self.N) + [Fr(1)])
    def const(self, q): return self.el([Fr(q)])
class El:
    __slots__ = ("F", "c")
    def __init__(self, F, c): self.F, self.c = F, c
    def _co(self, o): return o if isinstance(o, El) else self.F.const(o)
    def __add__(s, o): o = s._co(o); return El(s.F, tuple(a + b for a, b in zip(s.c, o.c)))
    def __neg__(s): return El(s.F, tuple(-a for a in s.c))
    def __sub__(s, o): return s + (-s._co(o))
    def __mul__(s, o):
        o = s._co(o); d = s.F.deg; out = [Fr(0)] * (2 * d - 1)
        for i, a in enumerate(s.c):
            if a:
                for j, b in enumerate(o.c):
                    if b: out[i + j] += a * b
        return s.F.el(out)
    def iszero(s): return not any(s.c)
    def __eq__(s, o): return s.c == s._co(o).c
    def __hash__(s): return hash(s.c)
    def inv(s):
        d = s.F.deg; cols = [(s * s.F.el([Fr(0)] * j + [Fr(1)])).c for j in range(d)]
        M = [[cols[j][i] for j in range(d)] + [Fr(int(i == 0))] for i in range(d)]
        for c in range(d):
            k = next(i for i in range(c, d) if M[i][c]); M[c], M[k] = M[k], M[c]
            iv = 1 / M[c][c]; M[c] = [v * iv for v in M[c]]
            for i in range(d):
                if i != c and M[i][c]:
                    f = M[i][c]; M[i] = [v - f * w for v, w in zip(M[i], M[c])]
        return El(s.F, tuple(M[i][d] for i in range(d)))
    def show(s):
        return str(s.c[0]) if not any(s.c[1:]) else "[" + ",".join(str(x) for x in s.c) + "]"

INF = "inf"
def exact_slopes(eps, word, k):
    """s(chi) for every character (i, j, 0) fixed by the monodromy; the trivial character has slope INF"""
    ng, rels, mu, lam, tau, A, tors = ac.level(eps, word, k); N = max(1, ac.torsion_exponent(A)); F = Cyc(N)
    Phi = ic.Phi_of(eps, word, k)
    ex = lambda w: (sum((g == 1) - (g == -1) for g in w), sum((g == 2) - (g == -2) for g in w))
    px, py = ex(Phi[1]), ex(Phi[2]); out = {(0, 0, 0): INF}
    for i, j in itertools.product(range(N), repeat=2):
        if (i, j) == (0, 0) or (px[0] * i + px[1] * j - i) % N or (py[0] * i + py[1] * j - j) % N: continue
        val = {1: F.zeta(i), 2: F.zeta(j), -1: F.zeta(-i), -2: F.zeta(-j)}
        u = {1: F.const(0), 2: (val[1] - 1).inv()} if i % N else {1: (F.const(1) - val[2]).inv(), 2: F.const(0)}
        def ev(w):
            tot = F.const(0); pre = F.const(1)
            for g in w:
                if g > 0: tot = tot + pre * u[g]; pre = pre * val[g]
                else: pre = pre * val[g]; tot = tot - pre * u[-g]
            return tot
        assert ev((1, 2, -1, -2)) == 1, "the longitude normalisation"
        g = 1 if i % N else 2
        s = (u[g] - ev(Phi[g])) * (val[g] - 1).inv()
        g2 = 3 - g
        if not (val[g2] - 1).iszero(): assert (u[g2] - ev(Phi[g2])) * (val[g2] - 1).inv() == s, "one slope for both generators"
        out[(i, j, 0)] = s
    return N, F, out

def verify_level(eps, word, k, couplings_dir=None):
    st = ("+" if eps > 0 else "-") + word
    N, F, S = exact_slopes(eps, word, k)
    o, bgs, I, chars, N2, rels, tau = ic.level_census(eps, word, k); assert N2 == N
    assert set(chars) == set(S), "the characters of the census are the monodromy-fixed characters"
    add = lambda x, y: tuple((a + b) % N for a, b in zip(x, y)); neg = lambda x: tuple((-a) % N for a in x); triv = (0, 0, 0)
    isinf = lambda a: isinstance(a, str)
    eq = lambda a, b: (isinf(a) and isinf(b)) or (not isinf(a) and not isinf(b) and a == b)
    # (1) the firing law, every candidate module
    fire = collections.Counter(); bad = 0; degenerate_nonzero = 0
    for lc in chars:
        if lc == triv: continue
        for al in chars:
            be = add(al, neg(lc)); i = I.get((lc, al), 0)
            if al == triv or be == triv:
                degenerate_nonzero += (i != 0); continue
            pred = int(eq(S[al], S[lc])) - int(eq(S[neg(be)], S[lc]))
            fire[(i, pred)] += 1; bad += (pred != i)
    # deck invariance and conjugation
    tch = lambda c: tuple(sum(e * x for e, x in zip(cc.expvec(tau[g], 3), c)) % N for g in (1, 2, 3))
    deck = all(eq(S[tch(c)], S[c]) for c in chars)
    out = dict(state=st, k=k, N=N, characters=len(chars), distinct_slopes=len({(s if isinf(s) else s.c) for s in S.values()}),
               all_rational=all(isinf(s) or not any(s.c[1:]) for s in S.values()),
               slope_histogram=dict(collections.Counter(s if isinf(s) else s.show() for s in S.values()).most_common(12)),
               firing_table={"I=%d,predicted=%d" % kv: v for kv, v in fire.items()}, firing_mismatches=bad,
               degenerate_modules_firing=degenerate_nonzero, deck_invariant=deck, backgrounds=len(bgs))
    # (2) vanishing against the sealed run
    if couplings_dir is not None:
        f = pathlib.Path(couplings_dir) / ("couplings_%s_%d.json" % (st.replace("+", "p").replace("-", "m"), k))
        if f.exists():
            lv = json.load(open(f)); tab = collections.Counter(); vals = collections.Counter()
            for bg in lv["backgrounds"]:
                lc = tuple(bg["key"][0]); al = dict(zip(ic.SECT, [tuple(x) for x in bg["key"][1:]])); sg = bg["counts"][0]
                for name, v in bg["pairs"].items():
                    A_, B_ = name.split("."); eta = add(add(al[A_], al[B_]), neg(lc)); eta = neg(eta) if sg > 0 else eta
                    pred = (eta == triv) or not eq(S[eta], S[lc]); tab[(v[3], pred)] += 1
                    if v[0]:
                        y = "-1" if eta == triv else (S[lc] - S[eta]).show(); vals[y] += 1
            out["vanishing_table"] = {"Y_nonzero=%s,predicted=%s" % kv: v for kv, v in tab.items()}
            out["vanishing_mismatches"] = sum(v for (a, b), v in tab.items() if a != b)
            out["allowed_coupling_values"] = dict(vals.most_common(16))
    # (3) the value law at the first prime, both signs
    if bgs:
        p = o["primes"][0]; zeta = pow(cc.primroot(p), (p - 1) // N, p); inv = lambda v: pow(v, p - 2, p)
        B = Bundle(ic.Phi_of(eps, word, k)); C, z, _ = B.fundamental(); plan = ic.Plan(B, C, z); lam = (B.lam, 0)
        H = {}; ok = tot = 0
        def hig(c):
            if c not in H:
                Vh = ic.char_module(B, c, N, zeta, p); h = ic.classes(Vh)[0]; H[c] = (ic.Evaluator(Vh, h, plan), h)
            return H[c]
        for key, cnt in sorted(bgs.items()):
            lc = key[0]; al = dict(zip(ic.SECT, key[1:])); sg = cnt[0]; h1, ct = cc.cocycle(lc, rels, 3, N, zeta, p)
            cco = Cocycle(ic.char_module(B, lc, N, zeta, p), [ct[0]], [ct[1]], [ct[2]]); cl = cco(lam)[0]; sl = cco.vt[0] * inv(cl) % p
            E = {}
            for s_, c_ in zip(ic.SECT, cnt):
                if c_ != sg: continue
                V = ic.my_module(B, lc, al[s_], ct, N, zeta, p, dual=(sg < 0)); a = ic.classes(V)[0]; e = relative_lift(a)
                q, sub = (1, 0) if sg > 0 else (0, 1)                       # quotient and sub coordinates of the module
                qc = add(al[s_], neg(lc)) if sg > 0 else neg(al[s_])        # the quotient character
                qx = pow(zeta, qc[0] % N, p); qy = pow(zeta, qc[1] % N, p)
                v = a.v[X][q] * inv(qx - 1) % p if (qx - 1) % p else a.v[Y][q] * inv(qy - 1) % p
                nrm = (a(lam)[sub] - (cl if sg > 0 else -cl) * v) % p
                E[s_] = (ic.Evaluator(V, a, plan), e, nrm)
            for A_, B_ in itertools.combinations_with_replacement([s_ for s_ in ic.SECT if s_ in E], 2):
                eta = add(add(al[A_], al[B_]), neg(lc)); eta = neg(eta) if sg > 0 else eta
                Eh, h = hig(eta); hl = h(lam)[0]
                Yv = ic.Yfast(plan, E[A_][0], E[B_][0], Eh, E[A_][1], p)
                if eta == triv: pred = (-E[A_][2] * E[B_][2] * h.vt[0] * inv(cl)) % p
                else: pred = E[A_][2] * E[B_][2] % p * hl % p * inv(cl) % p * ((sl - h.vt[0] * inv(hl)) % p) % p
                tot += 1; ok += (Yv == pred)
        out["value_law_pairs"] = tot; out["value_law_holds"] = ok
    return out

if __name__ == "__main__":
    if sys.argv[1] == "all":                                 # all <slice> <nslices> <couplings_dir> <outdir> [with_backgrounds_only]
        sl, ns, cdir, outdir = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], pathlib.Path(sys.argv[5])
        r = json.load(open(HERE.parents[1] / "B1434_the_architecture_census" / "verification" / "architecture_census.json"))
        pop = sorted([(o["state"], o["k"], o["candidates"]) for o in r if "candidates" in o], key=lambda t: t[2])
        for i, (st, k, nc) in enumerate(pop):
            if i % ns != sl: continue
            res = verify_level(1 if st[0] == "+" else -1, st[1:], k, cdir)
            print(json.dumps({kk: res[kk] for kk in ("state", "k", "characters", "firing_mismatches", "degenerate_modules_firing", "backgrounds") if kk in res} |
                             {kk: res.get(kk) for kk in ("vanishing_mismatches", "value_law_pairs", "value_law_holds")}), flush=True)
            json.dump(res, open(outdir / ("slope_%s_%d.json" % (st.replace("+", "p").replace("-", "m"), k)), "w"), indent=1)
    else:
        st, k = sys.argv[1], int(sys.argv[2])
        res = verify_level(1 if st[0] == "+" else -1, st[1:], k, sys.argv[3] if len(sys.argv) > 3 else None)
        print(json.dumps(res, indent=1))
