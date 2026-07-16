"""B649 stage 2b — the 27-lift over L = Q(s, i) (prereg 34f851b1)."""
import json
import os
import random
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))

MOD = [Fr(16), Fr(0), Fr(8), Fr(0)]  # s^4 = 16 + 8 s^2


def pmulred(p, q):
    out = [Fr(0)] * 7
    for i, a in enumerate(p):
        if a == 0:
            continue
        for j, b in enumerate(q):
            out[i + j] += a * b
    for k in range(6, 3, -1):
        c = out[k]
        if c != 0:
            out[k] = Fr(0)
            for t, m in enumerate(MOD):
                out[k - 4 + t] += c * m
    return out[:4]


class L:
    __slots__ = ("re", "im")

    def __init__(self, re=None, im=None):
        self.re = re if re is not None else [Fr(0)] * 4
        self.im = im if im is not None else [Fr(0)] * 4

    def __add__(self, o):
        return L([a + b for a, b in zip(self.re, o.re)],
                 [a + b for a, b in zip(self.im, o.im)])

    def __sub__(self, o):
        return L([a - b for a, b in zip(self.re, o.re)],
                 [a - b for a, b in zip(self.im, o.im)])

    def __mul__(self, o):
        rr, ii = pmulred(self.re, o.re), pmulred(self.im, o.im)
        ri, ir = pmulred(self.re, o.im), pmulred(self.im, o.re)
        return L([a - b for a, b in zip(rr, ii)],
                 [a + b for a, b in zip(ri, ir)])

    def is_zero(self):
        return all(c == 0 for c in self.re) and all(c == 0 for c in self.im)

    def vec8(self):
        return self.re + self.im

    def inv(self):
        """solve z*w = 1 as an 8x8 rational system over {s^j i^k}."""
        cols = []
        for k in range(8):
            b = L([Fr(1) if t == k else Fr(0) for t in range(4)], None) \
                if k < 4 else \
                L(None, [Fr(1) if t == k - 4 else Fr(0) for t in range(4)])
            cols.append((self * b).vec8())
        # solve M x = e0 with M = columns
        n = 8
        A = [[cols[j][i] for j in range(n)] + [Fr(1) if i == 0 else Fr(0)]
             for i in range(n)]
        for c in range(n):
            piv = next(r for r in range(c, n) if A[r][c] != 0)
            A[c], A[piv] = A[piv], A[c]
            pv = A[c][c]
            A[c] = [x / pv for x in A[c]]
            for r in range(n):
                if r != c and A[r][c] != 0:
                    f = A[r][c]
                    A[r] = [x - f * y for x, y in zip(A[r], A[c])]
        x = [A[r][n] for r in range(n)]
        return L(x[:4], x[4:])

    def __repr__(self):
        return f"L({self.re},{self.im})"


def Lc(q):
    return L([Fr(q), Fr(0), Fr(0), Fr(0)], None)


L0, L1 = Lc(0), Lc(1)

# ---- load the rational E6 data ------------------------------------------------
pr = json.load(open(os.path.join(HERE, "e6_principal_rational.json")))
E_PR = [[Lc(Fr(x)) for x in row] for row in pr["e_pr"]]
F_PR = [[Lc(Fr(x)) for x in row] for row in pr["f_pr"]]
H_PR = [[Lc(Fr(x)) for x in row] for row in pr["h_pr"]]
CUB = {tuple(map(int, k.split(","))): Fr(v)
       for k, v in json.load(open(os.path.join(HERE,
                                                "cubic_rational.json"))).items()}

# ---- 27x27 helpers over L ------------------------------------------------------
def meye(n):
    return [[L1 if i == j else L0 for j in range(n)] for i in range(n)]


def mmul(A, B):
    n = len(A)
    Bt = list(zip(*B))
    out = [[L0] * n for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        nz = [(k, Ai[k]) for k in range(n) if not Ai[k].is_zero()]
        for j in range(n):
            acc = L0
            col = Bt[j]
            for k, a in nz:
                b = col[k]
                if not b.is_zero():
                    acc = acc + a * b
            out[i][j] = acc
    return out


def mscale(c, M):
    return [[c * x for x in row] for row in M]


def madd(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mexp_nil(N):
    """exp of a nilpotent 27x27 over L."""
    out = meye(27)
    term = meye(27)
    k = 1
    while True:
        term = mmul(term, N)
        if all(x.is_zero() for row in term for x in row):
            break
        fk = Lc(Fr(1, 1))
        # divide by k!: scale by 1/k at each step instead
        term = mscale(Lc(Fr(1, k)).__mul__(L1) if False else Lc(Fr(1, k)),
                      term) if False else term
        # cleaner: accumulate term = N^k / k! iteratively
        k += 1
        out = madd(out, mscale(Lc(Fr(1, 1)), term))
        if k > 30:
            raise RuntimeError("not nilpotent?")
    return out


# the loop above is wrong for factorials; do it straightforwardly:
def mexp_nil(N):  # noqa: F811
    out = meye(27)
    term = meye(27)
    k = 1
    while True:
        term = mmul(term, N)
        term = mscale(Lc(Fr(1, k)), term)
        if all(x.is_zero() for row in term for x in row):
            break
        out = madd(out, term)
        k += 1
        if k > 40:
            raise RuntimeError("not nilpotent?")
    return out


def lift_sl2(g):
    p, q, r_, s = g[0][0], g[0][1], g[1][0], g[1][1]
    det = p * s - q * r_
    if p.is_zero():
        w27 = mmul(mmul(mexp_nil(E_PR),
                        mexp_nil(mscale(Lc(-1), F_PR))), mexp_nil(E_PR))
        return mmul(w27, lift_sl2([[L0 - r_, L0 - s], [p, q]]))
    lower = mexp_nil(mscale(r_ * p.inv(), F_PR))
    upper = mexp_nil(mscale(q * p.inv(), E_PR))
    t2 = (p * p) * det.inv()
    D = meye(27)
    t2i = t2.inv()
    for i in range(27):
        wgt = int(H_PR[i][i].re[0])
        e = wgt // 2
        val = L1
        base = t2 if e >= 0 else t2i
        for _ in range(abs(e)):
            val = val * base
        D[i][i] = val
    return mmul(mmul(lower, D), upper)


# ---- the exact silver SL2(L) letters -------------------------------------------
d = json.load(open(os.path.join(HERE, "entries_L.json")))


def gen2(nm):
    return [[L([Fr(x) for x in d[f"{nm}{i}{j}"][0]],
               [Fr(x) for x in d[f"{nm}{i}{j}"][1]])
             for j in range(2)] for i in range(2)]


def inv2(M):
    return [[M[1][1], L0 - M[0][1]], [L0 - M[1][0], M[0][0]]]


G2 = {nm: gen2(nm) for nm in "abc"}
for nm in "abc":
    G2[nm.upper()] = inv2(G2[nm])

print("lifting the six letters (27x27 over L)...", flush=True)
L27 = {}
import time
for nm in "abcABC":
    t0 = time.time()
    L27[nm] = lift_sl2(G2[nm])
    print(f"  {nm}: lifted in {time.time()-t0:.1f}s", flush=True)


def word27(w):
    m = None
    for ch in w:
        m = L27[ch] if m is None else mmul(m, L27[ch])
    return m


print("\n== S2b-G1: relators = I27 exactly ==", flush=True)
for rel in ("aBAbcc", "aaCbcB"):
    t0 = time.time()
    R = word27(rel)
    ok = all((R[i][j] - (L1 if i == j else L0)).is_zero()
             for i in range(27) for j in range(27))
    print(f"  {rel}: = I27 exactly: {ok}   ({time.time()-t0:.1f}s)",
          flush=True)

print("\n== S2b-G2: cubic preservation (25 sampled exact triples) ==",
      flush=True)


def cubic_eval(x, y, z):
    acc = L0
    for (p, q, r_), c in CUB.items():
        t = x[p] * y[q] * z[r_]
        if not t.is_zero():
            acc = acc + mscale_scalar(c, t)
    return acc


def mscale_scalar(fr, lelt):
    return Lc(fr) * lelt


def matvec(M, v):
    return [sum((M[i][k] * v[k] for k in range(27)
                 if not v[k].is_zero()), L0) for i in range(27)]


random.seed(649)
ok_all = True
for trial in range(25):
    x = [L0] * 27
    y = [L0] * 27
    z = [L0] * 27
    for v in (x, y, z):
        for _ in range(3):
            v[random.randrange(27)] = Lc(Fr(random.randint(-3, 3)))
    g = random.choice("abc")
    Mg = L27[g]
    lhs = cubic_eval(matvec(Mg, x), matvec(Mg, y), matvec(Mg, z))
    rhs = cubic_eval(x, y, z)
    if not (lhs - rhs).is_zero():
        ok_all = False
        print(f"  trial {trial} (gen {g}): VIOLATION", flush=True)
print(f"  cubic preserved on all 25 trials: {ok_all}", flush=True)

print("\n== S2b-G3: peripheral 27-traces ==", flush=True)
for w, nm in (("CCB", "mu"), ("caCA", "lam")):
    W = word27(w)
    t = L0
    for i in range(27):
        t = t + W[i][i]
    ok = (t - Lc(27)).is_zero()
    print(f"  tr27({nm}={w}) = 27 exactly: {ok}", flush=True)

# persist the lifted letters for stage 3
dump = {}
for nm in "abcABC":
    dump[nm] = [[[str(f) for f in (L27[nm][i][j].re + L27[nm][i][j].im)]
                 for j in range(27)] for i in range(27)]
json.dump(dump, open(os.path.join(HERE, "letters27_L.json"), "w"))
print("\nletters27_L.json written", flush=True)
print("B649 stage 2b DONE", flush=True)
