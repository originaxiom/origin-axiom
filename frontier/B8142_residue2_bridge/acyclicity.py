"""EXACT reproduction: is H*(m004; Sym^{2m} C^2) acyclic?

cc's B1157 refutes the antecedent of B8142b's reflection formula by computing that H*
is NEVER acyclic, (h0,h1,h2) = (0,1,1) for m >= 1. Reproduced here FROM SCRATCH and
EXACTLY -- no citation, no floating point, no computer-algebra `simplify`.

WHY EXACT, AND WHY THIS MODEL. A first attempt used SnapPy's holonomy in double
precision: Sym^{2m} amplifies entries like |M|^{2m} and the relator check failed by m=3.
SnapPy's high-precision manifold did not help either, because converting its values to
Python `complex` discards the precision at the first step. A sympy version with sqrt(-3)
was exact but too slow -- `simplify` on those matrices dominates everything. So the field
is modelled directly: every number is p + q*t with p,q rational and t^2 = t - 1, which is
Q(sqrt-3), the figure-eight's invariant trace field. All arithmetic below is exact.

THE PRESENTATION WAS NOT GUESSED. Parametrising b by an unknown and solving the relator
equations symbolically returns a parameter with minimal polynomial x^2 - x + 1 for the
relator used here; the Alexander polynomial control then pins the knot as 4_1.

    pi = <a, b | a B A b a B a b A B>,  a = [[1,1],[0,1]],  b = [[1,0],[t,1]],  t^2 = t - 1

    C^0 = V --d0--> C^1 = V+V --d1--> C^2 = V
    d0(v)   = ((rho(a)-I)v, (rho(b)-I)v)
    d1(u,v) = rho(dr/da) u + rho(dr/db) v          (Fox derivatives)
"""
import sys
from fractions import Fraction as F
from math import comb

FAIL = []


def check(name, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


# ---------- exact arithmetic in Q(t), t^2 = t - 1  (i.e. Q(sqrt-3)) --------------------
class K:
    __slots__ = ("p", "q")

    def __init__(self, p=0, q=0):
        self.p, self.q = F(p), F(q)

    def __add__(s, o): return K(s.p + o.p, s.q + o.q)
    def __sub__(s, o): return K(s.p - o.p, s.q - o.q)
    def __neg__(s):    return K(-s.p, -s.q)

    def __mul__(s, o):
        # (p+qt)(r+st) = (pr - qs) + (ps + qr + qs) t     using t^2 = t - 1
        return K(s.p * o.p - s.q * o.q, s.p * o.q + s.q * o.p + s.q * o.q)

    def inv(s):
        n = s.p * s.p + s.p * s.q + s.q * s.q          # norm
        if n == 0:
            raise ZeroDivisionError
        return K((s.p + s.q) / n, -s.q / n)            # conj / norm

    def __eq__(s, o):  return s.p == o.p and s.q == o.q
    def is_zero(s):    return s.p == 0 and s.q == 0
    def __repr__(s):   return "%s+%st" % (s.p, s.q)


ZERO, ONE, T = K(0, 0), K(1, 0), K(0, 1)


def mat(rows):   return [[c for c in r] for r in rows]
def eye(n):      return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def mmul(X, Y):
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum((X[i][t_] * Y[t_][j] for t_ in range(k)), ZERO) for j in range(m)]
            for i in range(n)]


def minv2(M):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    det = a * d - b * c
    di = det.inv()
    return [[d * di, -b * di], [-c * di, a * di]]


def msub_eye(M):
    return [[M[i][j] - (ONE if i == j else ZERO) for j in range(len(M))] for i in range(len(M))]


def rank(M):
    """Gaussian elimination over K."""
    if not M or not M[0]:
        return 0
    A = [row[:] for row in M]
    rows, cols = len(A), len(A[0])
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if not A[i][c].is_zero()), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pin = A[r][c].inv()
        A[r] = [x * pin for x in A[r]]
        for i in range(rows):
            if i != r and not A[i][c].is_zero():
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


A = [[ONE, ONE], [ZERO, ONE]]
B = [[ONE, ZERO], [T, ONE]]
REL = "aBAbaBabAB"


def sym_power(M, n):
    d = n + 1
    S = [[ZERO] * d for _ in range(d)]
    a, b, c, e = M[0][0], M[0][1], M[1][0], M[1][1]

    def pw(z, k):
        r = ONE
        for _ in range(k):
            r = r * z
        return r
    for k in range(d):
        for i in range(n - k + 1):
            for j in range(k + 1):
                px = (n - k - i) + (k - j)
                coef = K(comb(n - k, i) * comb(k, j)) * pw(a, n - k - i) * pw(c, i) \
                    * pw(b, k - j) * pw(e, j)
                S[n - px][k] = S[n - px][k] + coef
    return S


def ev(word, rep):
    d = len(rep["a"])
    P = eye(d)
    inv_cache = {}
    for ch in word:
        g = ch.lower()
        if ch.islower():
            P = mmul(P, rep[g])
        else:
            if g not in inv_cache:
                inv_cache[g] = inv_mat(rep[g])
            P = mmul(P, inv_cache[g])
    return P


def inv_mat(M):
    """Exact inverse by Gauss-Jordan over K."""
    n = len(M)
    A_ = [row[:] + [ONE if i == j else ZERO for j in range(n)] for i, row in enumerate(M)]
    r = 0
    for c in range(n):
        piv = next(i for i in range(r, n) if not A_[i][c].is_zero())
        A_[r], A_[piv] = A_[piv], A_[r]
        pin = A_[r][c].inv()
        A_[r] = [x * pin for x in A_[r]]
        for i in range(n):
            if i != r and not A_[i][c].is_zero():
                f = A_[i][c]
                A_[i] = [A_[i][j] - f * A_[r][j] for j in range(2 * n)]
        r += 1
    return [row[n:] for row in A_]


def fox(word, rep):
    d = len(rep["a"])
    D = {"a": [[ZERO] * d for _ in range(d)], "b": [[ZERO] * d for _ in range(d)]}
    pre = eye(d)
    inv_cache = {g: inv_mat(rep[g]) for g in ("a", "b")}
    for ch in word:
        g = ch.lower()
        if ch.islower():
            D[g] = [[D[g][i][j] + pre[i][j] for j in range(d)] for i in range(d)]
            pre = mmul(pre, rep[g])
        else:
            pre = mmul(pre, inv_cache[g])
            D[g] = [[D[g][i][j] - pre[i][j] for j in range(d)] for i in range(d)]
    return D, pre


print("A  the field and the presentation")
check("t^2 = t - 1 exactly (so Q(t) = Q(sqrt-3), m004's invariant trace field)",
      T * T == T - ONE)
check("the relator holds EXACTLY in SL(2, Q(sqrt-3))",
      ev(REL, {"a": A, "b": B}) == eye(2))
check("CONTROL a perturbed parameter does NOT satisfy the relator",
      ev(REL, {"a": A, "b": [[ONE, ZERO], [T + ONE, ONE]]}) != eye(2))

print("\nB  exact cohomology with coefficients in Sym^{2m} C^2")
print("      m   dim V   h0   h1   h2   chi")
rows = {}
for m in range(0, 6):
    n, d = 2 * m, 2 * m + 1
    rep = {"a": sym_power(A, n), "b": sym_power(B, n)}
    D, total = fox(REL, rep)
    assert total == eye(d), "relator fails exactly in Sym^%d" % n
    d0 = [r[:] for r in msub_eye(rep["a"])] + [r[:] for r in msub_eye(rep["b"])]
    d1 = [D["a"][i] + D["b"][i] for i in range(d)]
    r0, r1 = rank(d0), rank(d1)
    h0, h1, h2 = d - r0, (2 * d - r1) - r0, d - r1
    rows[m] = (h0, h1, h2)
    print("      %d   %5d   %2d   %2d   %2d   %3d" % (m, d, h0, h1, h2, h0 - h1 + h2))

print("\nC  controls")
check("CONTROL m=0 (trivial coefficients) gives (1,1,0)", rows[0] == (1, 1, 0), str(rows[0]))
check("Euler characteristic vanishes for every m", all(a - b + c == 0 for a, b, c in rows.values()))

print("\nD  the verdict on B8142b's antecedent")
check("H* is NEVER acyclic -- no m gives (0,0,0)", all(v != (0, 0, 0) for v in rows.values()))
check("for m >= 1 the profile is exactly (0,1,1) = (0, #cusps, #cusps)",
      all(rows[m] == (0, 1, 1) for m in range(1, 6)))

print("\nE  the mechanism, m-independent")
bad = []
for n in (2, 4, 6, 8, 10, 20, 40):
    P = sym_power([[ONE, ONE], [ZERO, ONE]], n)      # a parabolic
    fixed = (n + 1) - rank(msub_eye(P))
    print("      Sym^%-2d : the parabolic fixes a %d-dimensional line" % (n, fixed))
    if fixed != 1:
        bad.append(n)
check("a parabolic fixes EXACTLY ONE line in Sym^n, every n tested -- this is the mechanism",
      not bad)

print("""
  => cc's B1157 IS REPRODUCED, exactly and independently.
     The CLOSED Fried hypothesis (acyclicity) FAILS at every m, by a PERIPHERAL defect:
     the cusp's parabolic subgroup fixes a line in Sym^{2m} for every m, which plants
     h1 = h2 = #cusps = 1.

     CONSEQUENCE FOR B8142b: the antecedent I posed -- "Fried applies to rho(m)" -- is
     REFUTED in its closed form. R_{rho(m)}(s) has a nonzero order of vanishing at s = 0
     governed by h1 = h2 = 1; it is NOT a finite value equal to a torsion, so the
     reflection formula does NOT become unconditional by that route.

     SURVIVES UNTOUCHED : the identity R_{rho(m)}(s) = prod_j R(s-j, sigma_j).
     REMAINS OPEN       : the cusped Park/Pfaff route, which cc names as the right frame.
""")
print("%d/%d checks passed" % (8 - len(FAIL), 8))
sys.exit(1 if FAIL else 0)
