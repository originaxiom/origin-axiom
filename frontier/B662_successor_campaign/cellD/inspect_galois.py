"""Cell D inspection — the Galois structure of the banked silver data.

L = Q(s, i), s^4 = 8 s^2 + 16.  Basis over Q: 1, s, s^2, s^3, i, is, is^2, is^3.
Gal(L/Q(i)) = {1, sigma, tau, sigma tau}:
  sigma: s -> -s          (fixes i)
  tau:   s -> 4i/s        (fixes i)
Complex conjugation c: i -> -i, s -> s (the L.conj() of the banked class).
Exact arithmetic throughout (Fraction).
"""
import json
import os
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
B649 = os.path.join(HERE, "..", "..", "B649_silver_holonomy")

# ---- the L class (verbatim arithmetic conventions of b649_stage3a) ----
MOD = [Fr(16), Fr(0), Fr(8), Fr(0)]


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

    def conj(self):
        return L(self.re[:], [-x for x in self.im])

    def is_zero(self):
        return all(c == 0 for c in self.re) and all(c == 0 for c in self.im)

    def vec8(self):
        return self.re + self.im

    def __eq__(self, o):
        return (self - o).is_zero()

    def inv(self):
        cols = []
        for k in range(8):
            b = L([Fr(1) if t == k else Fr(0) for t in range(4)], None) \
                if k < 4 else \
                L(None, [Fr(1) if t == k - 4 else Fr(0) for t in range(4)])
            cols.append((self * b).vec8())
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


def Lc(q):
    return L([Fr(q), Fr(0), Fr(0), Fr(0)], None)


L0, L1 = Lc(0), Lc(1)


def from8(v):
    return L([Fr(x) for x in v[:4]], [Fr(x) for x in v[4:]])


# ---- the Galois maps as 8x8 rational matrices on the basis ----
# basis order: 1, s, s^2, s^3, i, is, is^2, is^3  (re4 + im4)
def gal_matrix(img_s_vec8, img_i_vec8):
    """build the 8x8 matrix of the ring map sending s -> S, i -> I."""
    S = from8(img_s_vec8)
    I = from8(img_i_vec8)
    cols = []
    for t in range(8):
        # image of basis element: S^k or I*S^k
        k = t % 4
        acc = L1
        for _ in range(k):
            acc = acc * S
        if t >= 4:
            acc = acc * I
        cols.append(acc.vec8())
    return cols  # cols[t] = image of basis t, as vec8


def apply_gal(cols, x):
    v = x.vec8()
    out = [Fr(0)] * 8
    for t in range(8):
        if v[t] != 0:
            for r in range(8):
                out[r] += v[t] * cols[t][r]
    return from8(out)


SIG = gal_matrix([0, -1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0])
# tau: s -> 4i/s = i(s^3-8s)/4  (since 1/s = (s^3-8s)/16)
TAU = gal_matrix([0, 0, 0, 0, 0, Fr(-2), 0, Fr(1, 4)],
                 [0, 0, 0, 0, 1, 0, 0, 0])
CONJ = gal_matrix([0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0, 0, 0])


def gmul(cols2, cols1):
    """composition: apply cols1 then cols2."""
    out = []
    for t in range(8):
        out.append(apply_gal(cols2, from8(cols1[t])).vec8())
    return out


def gid():
    return gal_matrix([0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0])


def geq(c1, c2):
    return all(c1[t][r] == c2[t][r] for t in range(8) for r in range(8))


print("== A. the Galois group over Q(i) ==")
# ring-hom property: multiplicative on all basis pairs (defining relations)
ok_mult = True
for name, G in (("sigma", SIG), ("tau", TAU), ("conj", CONJ)):
    for t1 in range(8):
        for t2 in range(8):
            b1, b2 = from8([1 if q == t1 else 0 for q in range(8)]), \
                     from8([1 if q == t2 else 0 for q in range(8)])
            lhs = apply_gal(G, b1 * b2)
            rhs = apply_gal(G, b1) * apply_gal(G, b2)
            if not (lhs - rhs).is_zero():
                ok_mult = False
                print(f"  MULT FAIL {name} at {t1},{t2}")
print(f"  sigma, tau, conj are ring homs (all 3x64 basis products): {ok_mult}")
print(f"  sigma^2 = id: {geq(gmul(SIG, SIG), gid())}")
print(f"  tau^2 = id: {geq(gmul(TAU, TAU), gid())}")
print(f"  sigma tau = tau sigma: {geq(gmul(SIG, TAU), gmul(TAU, SIG))}")
print(f"  tau != id, sigma != id: {not geq(TAU, gid())}, "
      f"{not geq(SIG, gid())}")
print(f"  conj tau = (sigma tau) conj: "
      f"{geq(gmul(CONJ, TAU), gmul(gmul(SIG, TAU), CONJ))}")
print(f"  conj sigma = sigma conj: {geq(gmul(CONJ, SIG), gmul(SIG, CONJ))}")

# fixed space of {sigma, tau}: solve (SIG - I)v = 0 and (TAU - I)v = 0
rows = []
ID = gid()
for G in (SIG, TAU):
    for r in range(8):
        rows.append([G[t][r] - ID[t][r] for t in range(8)])


def rat_nullspace(rows, ncols):
    A = [r[:] for r in rows]
    m = len(A)
    piv_cols = []
    r = 0
    for c in range(ncols):
        piv = next((k for k in range(r, m) if A[k][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for k in range(m):
            if k != r and A[k][c] != 0:
                f = A[k][c]
                A[k] = [x - f * y for x, y in zip(A[k], A[r])]
        piv_cols.append(c)
        r += 1
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [Fr(0)] * ncols
        v[fc] = Fr(1)
        for rr, pc in enumerate(piv_cols):
            v[pc] = -A[rr][fc]
        basis.append(v)
    return basis


fx = rat_nullspace(rows, 8)
print(f"  Fix(sigma,tau) dim = {len(fx)}; basis = {fx}")
print("  (expect dim 2, spanned by 1 and i => Fix = Q(i))")

# ---- B. the 2x2 letters ----
print("\n== B. the banked 2x2 letters (entries_L.json) ==")
dent = json.load(open(os.path.join(B649, "entries_L.json")))
print(f"  keys: {sorted(dent.keys())}")


def gen2(nm):
    return [[L([Fr(x) for x in dent[f"{nm}{i}{j}"][0]],
               [Fr(x) for x in dent[f"{nm}{i}{j}"][1]])
             for j in range(2)] for i in range(2)]


G2 = {nm: gen2(nm) for nm in "abc"}
for nm in "abc":
    for i in range(2):
        for j in range(2):
            x = G2[nm][i][j]
            sup = [t for t in range(8) if x.vec8()[t] != 0]
            print(f"  {nm}[{i}][{j}] support {sup} vec {x.vec8()}")


def mm2(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)]
            for i in range(2)]


def adj2(M):
    return [[M[1][1], L0 - M[0][1]], [L0 - M[1][0], M[0][0]]]


for nm in "abc":
    G2[nm.upper()] = adj2(G2[nm])


def word2(w):
    m = None
    for ch in w:
        m = G2[ch] if m is None else mm2(m, G2[ch])
    return m


def tr2(M):
    return M[0][0] + M[1][1]


print("\n  traces of sample words (vec8):")
for w in ("a", "b", "c", "ab", "ac", "bc", "abc", "aabbc", "CCB", "caCA",
          "aa", "bb", "cc", "abab"):
    t = tr2(word2(w))
    print(f"    tr({w}) = {t.vec8()}")

print("\n  dets:")
for nm in "abc":
    M = G2[nm]
    d = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    print(f"    det({nm}) = {d.vec8()}")

# apply sigma / tau entrywise: is sigma(letters) == letters? parity?
print("\n  Galois images of letters:")
for gname, G in (("sigma", SIG), ("tau", TAU)):
    for nm in "abc":
        img = [[apply_gal(G, G2[nm][i][j]) for j in range(2)]
               for i in range(2)]
        same = all((img[i][j] - G2[nm][i][j]).is_zero()
                   for i in range(2) for j in range(2))
        neg = all((img[i][j] + G2[nm][i][j]).is_zero()
                  for i in range(2) for j in range(2))
        print(f"    {gname}({nm}) == {nm}: {same};  == -{nm}: {neg}")

print("\nINSPECT DONE")
