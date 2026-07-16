"""B649 stage 3b-ii — THE SILVER Y-TENSOR (prereg 5dd14ee0)."""
import heapq
import itertools as it
import json
import os
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- reuse the 3b-i pipeline up to the H1 representatives ----------------------
src = open(os.path.join(HERE, "b649_stage3b_swap.py")).read()
head = src[:src.index('# ---- sigma* ---')]
ns = {"__name__": "b649_shared2",
      "__file__": os.path.join(HERE, "b649_stage3b_swap.py")}
exec(compile(head, "b649_3bi_head.py", "exec"), ns)

L, Lc, L0, L1 = ns["L"], ns["Lc"], ns["L0"], ns["L1"]
meye, mmul, mscale, madd = ns["meye"], ns["mmul"], ns["mscale"], ns["madd"]
S1, S2 = ns["S1"], ns["S2"]
reps, cob = ns["reps"], ns["cob"]
U27 = ns["U27"]
print(f"pipeline reloaded: {len(reps)} reps", flush=True)

CUB = {tuple(map(int, k.split(","))): Fr(v)
       for k, v in json.load(open(os.path.join(HERE,
                                                "cubic_rational.json"))).items()}

# ---- free-word utilities -------------------------------------------------------
def inv(w):
    return "".join(ch.swapcase() for ch in reversed(w))


def freduce(w):
    out = []
    for ch in w:
        if out and out[-1] == ch.swapcase():
            out.pop()
        else:
            out.append(ch)
    return "".join(out)


R1, R2 = "aBAbcc", "aaCbcB"
RELS = [(R1, +1, 0), (inv(R1), -1, 0), (R2, +1, 1), (inv(R2), -1, 1)]
MU, LAM = "CCB", "caCA"

CERT_CACHE = {}


def certify(word):
    """certificate: list of (prefix_word, relator_index, sign)."""
    w0 = freduce(word)
    if w0 == "":
        return []
    if w0 in CERT_CACHE:
        return CERT_CACHE[w0]
    seen = {w0: None}
    beam = [(len(w0), w0)]
    ok = False
    for depth in range(1, 25):
        cand = {}
        for _, w in beam:
            for ins, sgn, ridx in RELS:
                for i in range(len(w) + 1):
                    nw = freduce(w[:i] + ins + w[i:])
                    if nw not in seen and nw not in cand:
                        cand[nw] = (w, i, sgn, ridx)
        seen.update(cand)
        if "" in cand:
            ok = True
            break
        beam = heapq.nsmallest(1500, ((len(nw), nw) for nw in cand))
        assert beam, f"certificate dead end: {w0}"
    assert ok, f"no certificate within depth: {w0}"
    chain = []
    node = ""
    while seen[node] is not None:
        parent, i, sgn, ridx = seen[node]
        chain.append((parent, i, sgn, ridx))
        node = parent
    chain.reverse()
    cert = []
    w = w0
    RW = {0: (R1, inv(R1)), 1: (R2, inv(R2))}
    for (parent, i, sgn, ridx) in chain:
        assert parent == w
        cert.append((w[:i], -sgn, ridx))
        w = freduce(w[:i] + (RW[ridx][0] if sgn > 0 else RW[ridx][1]) + w[i:])
    assert w == ""
    prod = ""
    for (u, e, ridx) in cert:
        prod += u + (RW[ridx][0] if e > 0 else RW[ridx][1]) + inv(u)
    assert freduce(prod) == w0, "certificate replay failed"
    CERT_CACHE[w0] = cert
    return cert


def rel_chain(REL):
    cells = []
    pre = ""
    for ch in REL:
        cells.append(("", pre, ch, +1))
        if ch.isupper():
            cells.append((pre, ch, ch.lower(), -1))
        pre = freduce(pre + ch)
    return cells


RELCHAINS = {0: rel_chain(R1), 1: rel_chain(R2)}


def Cval(u, v, w):
    acc = L0
    for (p, q, r_), c in CUB.items():
        if u[p].is_zero() or v[q].is_zero() or w[r_].is_zero():
            continue
        acc = acc + Lc(c) * u[p] * v[q] * w[r_]
    return acc


def apply27(M, v):
    return [sum((M[i][k] * v[k] for k in range(27)
                 if not v[k].is_zero()), L0) for i in range(27)]


class SideL:
    """3-generator side with the T.H evaluator over L."""

    def __init__(self, lets):
        self.lets = lets
        self._mc = {"": meye(27)}

    def mat(self, w):
        w = freduce(w)
        if w not in self._mc:
            M = meye(27)
            for ch in w:
                M = mmul(M, self.lets[ch])
            self._mc[w] = M
        return self._mc[w]

    def zval(self, z, w):
        """z = (z_a, z_b, z_c) 27-vectors."""
        idx = {"a": 0, "b": 1, "c": 2}
        val = [L0] * 27
        P = meye(27)
        for ch in freduce(w):
            if ch.islower():
                add = apply27(P, z[idx[ch]])
            else:
                add = [L0 - x for x in
                       apply27(mmul(P, self.lets[ch]), z[idx[ch.lower()]])]
            val = [a + b for a, b in zip(val, add)]
            P = mmul(P, self.lets[ch])
        return val

    def make_omega(self, za, zb, zc):
        cache = {}

        def om(x, y, z):
            x, y, z = freduce(x), freduce(y), freduce(z)
            if not x or not y or not z:
                return L0
            key = (x, y, z)
            if key not in cache:
                vx = self.zval(za, x)
                vy = apply27(self.mat(x), self.zval(zb, y))
                vz = apply27(self.mat(freduce(x + y)), self.zval(zc, z))
                cache[key] = Cval(vx, vy, vz)
            return cache[key]
        return om

    @staticmethod
    def fox_positions(w):
        out = []
        for i, ch in enumerate(w):
            pre = w[:i]
            if ch.islower():
                out.append((pre, ch, +1))
            else:
                out.append((freduce(pre + ch), ch.lower(), -1))
        return out

    def S_eval(self, om, g, h, gh):
        total = L0
        total = total + om("", g, h)
        for (u, e, ridx) in certify(g + h + inv(gh)):
            for (cw, s1, s2, sgn) in RELCHAINS[ridx]:
                coeff = e * sgn
                cell1 = freduce(u + cw)
                val = om(cell1, s1, s2)
                if coeff > 0:
                    total = total - val
                else:
                    total = total + val

        def s_of_H1(coeffword, w, outer_sign):
            nonlocal total
            for (pre, ch, sgn) in self.fox_positions(w):
                val = om(coeffword, pre, ch)
                contrib_pos = (outer_sign * (-sgn)) < 0
                if contrib_pos:
                    total = total + val
                else:
                    total = total - val
        s_of_H1(g, h, +1)
        s_of_H1("", gh, -1)
        s_of_H1("", g, +1)
        return total


side1 = SideL({"a": S1["a"], "b": S1["b"], "c": S1["c"],
               "A": S1["A"], "B": S1["B"], "C": S1["C"]})
side2 = SideL({"a": S2["a"], "b": S2["b"], "c": S2["c"],
               "A": S2["A"], "B": S2["B"], "C": S2["C"]})

print("== G1: certificates + validation ==", flush=True)
t0 = time.time()
COMM = freduce(LAM + MU + inv(freduce(MU + LAM)))
cert = certify(COMM)
print(f"  peripheral commutator |word| = {len(COMM)}; AREA = {len(cert)} "
      f"({time.time()-t0:.0f}s)", flush=True)


def validate(side, label):
    za = tuple([Lc(Fr(1, k + 2 + i)) if False else
                [Lc(Fr((i * 7 + k * 3 + j) % 5 - 2)) for j in range(27)]
                for k in range(3)] for i in [0])[0]
    # three deterministic rational cocycle-like test vectors (validation
    # only needs delta S = omega as an identity of the T.H construction —
    # it holds for ARBITRARY 1-cochains, not just cocycles)
    zb = [[Lc(Fr((i * 5 + j * 2 + 1) % 7 - 3)) for j in range(27)]
          for i in range(3)]
    zc = [[Lc(Fr((i * 3 + j * 5 + 2) % 9 - 4)) for j in range(27)]
          for i in range(3)]
    om = side.make_omega(za, zb, zc)
    S = lambda g, h, gh: side.S_eval(om, g, h, gh)
    tests = [("a", "b", "ab"), ("b", "C", "bC"), ("ca", "AC", "caAC")]
    allok = True
    for (g, h, k) in tests:
        gh, hk, ghk = freduce(g + h), freduce(h + k), freduce(g + h + k)
        lhs = (S(h, k, hk) - S(gh, k, ghk) + S(g, hk, ghk) - S(g, h, gh))
        rhs = om(g, h, k)
        ok = (lhs - rhs).is_zero()
        allok = allok and ok
        print(f"    [{label}] deltaS=omega on [{g}|{h}|{k}]: {ok}",
              flush=True)
    g, h = LAM, MU
    gh = freduce(MU + LAM)
    k = "b"
    ghk, hk = freduce(gh + k), freduce(h + k)
    lhs = (S(h, k, hk) - S(gh, k, ghk) + S(g, hk, ghk) - S(g, h, gh))
    rhs = om(g, h, k)
    ok = (lhs - rhs).is_zero()
    print(f"    [{label}] deltaS=omega on [lam|mu|b] (certificate): {ok}",
          flush=True)
    return allok and ok


ok1 = validate(side1, "side1")
ok2 = validate(side2, "side2")
print(f"  G1 machinery: {ok1 and ok2}", flush=True)

print("\n== G2: the 10-triple Y table ==", flush=True)
P1s = freduce(MU + LAM)
MU2w, LAM2w = MU, inv(LAM)
P2s = freduce(MU2w + LAM2w)


def sides_of(z):
    return ((z[0:27], z[27:54], z[54:81]),
            (z[81:108], z[108:135], z[135:162]))


def Yval(zA, zB, zC):
    (a1, a2), (b1, b2), (c1, c2) = map(sides_of, (zA, zB, zC))
    om1 = side1.make_omega(a1, b1, c1)
    om2 = side2.make_omega(a2, b2, c2)
    Sa = lambda g, h, gh: side1.S_eval(om1, g, h, gh)
    Sb = lambda g, h, gh: side2.S_eval(om2, g, h, gh)
    return (Sa(MU, LAM, P1s) - Sa(LAM, MU, P1s)) \
        - (Sb(MU2w, LAM2w, P2s) - Sb(LAM2w, MU2w, P2s))


Y = {}
for (i, j, k) in it.combinations(range(5), 3):
    t0 = time.time()
    Y[(i, j, k)] = Yval(reps[i], reps[j], reps[k])
    v = Y[(i, j, k)]
    print(f"  Y[{i}{j}{k}] = re{[str(x) for x in v.re]} "
          f"im{[str(x) for x in v.im]}  ({time.time()-t0:.0f}s)",
          flush=True)

json.dump({f"{i}{j}{k}": [str(f) for f in (v.re + v.im)]
           for (i, j, k), v in Y.items()},
          open(os.path.join(HERE, "silver_Y_L.json"), "w"))
print("silver_Y_L.json written", flush=True)

print("\n== G3: form-level checks ==", flush=True)
nz = [t for t, v in Y.items() if not v.is_zero()]
print(f"  (a) nonzero slots: {len(nz)}/10: {[''.join(map(str,t)) for t in nz]}",
      flush=True)

print("\nB649 stage 3b-ii DONE (G3 b-d analysis on the banked table next)",
      flush=True)
