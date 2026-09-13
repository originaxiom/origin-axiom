"""EXACT instrument in Q(zeta_60) = Q[z]/Phi_60. Discharges B1348/B1349's owed exactification.

All exponents land in (1/15)Z, so every entry is a Z-combination of zeta_60 powers:
  T = diag(zeta_15^{-2}, zeta_15^{2}, zeta_15^{8}, zeta_15^{2}, zeta_15^{7}, zeta_15^{8})
  S = (-i / (5 sqrt3)) * sum_w sgn(w) zeta_15^{-3 <w(l+rho), m+rho>}
with i = zeta_60^15 and sqrt3 = zeta_60^5 + zeta_60^{-5}.
"""
import itertools
import sympy as sp
from sympy import Rational as Q

z = sp.symbols('z')
PHI = sp.cyclotomic_poly(60, z)
DEG = sp.degree(PHI, z)
assert DEG == 16, DEG

def red(e):
    """reduce a polynomial in z modulo Phi_60"""
    return sp.rem(sp.expand(e), PHI, z)
def zt(k, n=60):
    """zeta_n^k as a reduced polynomial in z = zeta_60"""
    assert 60 % n == 0
    return red(z ** ((k * (60 // n)) % 60))
def conj(e):
    """complex conjugation: z -> z^-1 = z^59"""
    p = sp.Poly(red(e), z)
    return red(sum(c * z ** ((-m[0]) % 60) for m, c in zip(p.monoms(), p.coeffs())))
def mul(a, b): return red(sp.expand(a * b))

W = [(0,0),(0,1),(0,2),(1,0),(1,1),(2,0)]
KAP = 5
Lv = lambda w: (w[0] + w[1] + 2, w[1] + 1, 0)
def ip3(u, v):
    """3 * <u,v> for the su(3) trace-zero form -- an integer"""
    return 3 * sum(a * b for a, b in zip(u, v)) - sum(u) * sum(v)
perms = list(itertools.permutations(range(3)))
sgn = lambda p: (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))

# S, exactly
sqrt3 = red(zt(5) + zt(-5))                  # zeta_12 + zeta_12^-1 = 2cos(pi/6) = sqrt3
minus_i = red(-zt(15))                       # -i
inv5sqrt3 = None                             # we keep the prefactor symbolic-rational times 1/sqrt3
Sraw = [[0]*6 for _ in range(6)]
for i, wl in enumerate(W):
    Ll = Lv(wl)
    for j, wm in enumerate(W):
        Lm = Lv(wm)
        tot = 0
        for p in perms:
            e = ip3(tuple(Ll[p[t]] for t in range(3)), Lm)   # = 3*<w(l+rho), m+rho>
            # exponent -2 pi i <.,.>/5 = 2 pi i * (-3<.,.>)/15  -> zeta_15^{-e}
            tot += sgn(p) * zt(-e, 15)
        Sraw[i][j] = red(sp.expand(tot))
# S = minus_i/(5*sqrt3) * Sraw  ;  1/sqrt3 = sqrt3/3
pref = red(sp.expand(mul(minus_i, sqrt3) * Q(1, 15)))        # (-i/(5 sqrt3)) = -i*sqrt3/15
S = sp.Matrix(6, 6, lambda i, j: mul(pref, Sraw[i][j]))
TD = {(0,0): -2, (0,1): 2, (0,2): 8, (1,0): 2, (1,1): 7, (2,0): 8}
T = sp.diag(*[zt(TD[w], 15) for w in W])

def mmul(A, B):
    n, m, k2 = A.rows, B.cols, A.cols
    return sp.Matrix(n, m, lambda i, j: red(sp.expand(sum(A[i, t] * B[t, j] for t in range(k2)))))
