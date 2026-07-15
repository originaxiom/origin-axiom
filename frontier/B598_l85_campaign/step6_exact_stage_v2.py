"""Readiness step 6 v2 — the E6_2 amplitudes as SYMBOLIC IDENTITIES via exact
cyclotomic reduction (the v1 simplify-route failed at denesting sqrt(N^2); this
route is decidable: everything lives in Q(zeta_84), so we prove the SQUARED
identity p_un^2 = target^2 * N^2 by polynomial reduction mod Phi_84 (exact
rational arithmetic), and fix the discrete sign branch by a 30-digit
evaluation (the branches differ by 2|p| >> error — a proof, not a fit).

Run: python3 step6_exact_stage_v2.py (~10 min). Nothing to CLAIMS.md.
"""
import importlib.util
import os
from collections import Counter
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "c3", os.path.join(HERE, "..", "B570_allowed_plays", "c3_e6_level2_monodromy.py"))
c3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c3)

KH = 14
PRIM = c3.PRIM
C6 = [[Fr(x) for x in row] for row in c3.C6]


def mat_inv(A):
    n = len(A)
    M = [row[:] + [Fr(1) if i == j else Fr(0) for j in range(n)]
         for i, row in enumerate(A)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
    return [row[n:] for row in M]


CINV = mat_inv(C6)
root_coords = lambda lab: [sum(CINV[i][j] * Fr(lab[j]) for j in range(6))
                           for i in range(6)]
ip = lambda x, y: sum(Fr(c3.C6[i][j]) * x[i] * y[j]
                      for i in range(6) for j in range(6))
RHO = root_coords([1] * 6)
SHIFT = [[a + b for a, b in zip(root_coords(p), RHO)] for p in PRIM]

# ---- Z[x]/(x^84 - 1) arithmetic (dict exponent -> Fraction) ----
MOD = 84


def pmul(u, v):
    out = {}
    for a, ca in u.items():
        for b, cb in v.items():
            k = (a + b) % MOD
            out[k] = out.get(k, Fr(0)) + ca * cb
    return {k: c for k, c in out.items() if c != 0}


def padd(u, v):
    out = dict(u)
    for k, c in v.items():
        out[k] = out.get(k, Fr(0)) + c
    return {k: c for k, c in out.items() if c != 0}


def pscale(c, u):
    return {k: c * v for k, v in u.items() if c * v != 0}


def pconj(u):
    return {(-k) % MOD: c for k, c in u.items()}


def zeta(q):
    """exp(2 pi i q) with q rational, denominator | 84."""
    e = q * MOD
    assert e.denominator == 1
    return {int(e) % MOD: Fr(1)}


def is_zero_in_field(u):
    """u = 0 in Q(zeta_84) iff the poly reduces to 0 mod Phi_84."""
    x = sp.Symbol('x')
    poly = sum(sp.Rational(c.numerator, c.denominator) * x ** k
               for k, c in u.items())
    if poly == 0:
        return True
    phi = sp.cyclotomic_poly(MOD, x)
    return sp.rem(sp.Poly(poly, x), sp.Poly(phi, x)).is_zero


print("collecting the exact Weyl sums...")
W, eps = c3.weyl_group()
ST = {}
for a in range(9):
    for b in range(a, 9):
        cnt = Counter()
        vb = SHIFT[b]
        Gvb = [sum(Fr(c3.C6[i][j]) * vb[j] for j in range(6)) for i in range(6)]
        va = SHIFT[a]
        for wm, e in zip(W, eps):
            wa = [sum(Fr(int(wm[i][j])) * va[j] for j in range(6)) for i in range(6)]
            q = (-sum(wa[i] * Gvb[i] for i in range(6)) / KH) % 1
            cnt[q] += int(e)
        ST[(a, b)] = ST[(b, a)] = {k: Fr(v) for k, v in
                                   Counter({q: c for q, c in cnt.items() if c}).items()}
print("collected")

Stil = [[None] * 9 for _ in range(9)]
for a in range(9):
    for b in range(9):
        ent = {}
        for q, c in ST[(a, b)].items():
            ent = padd(ent, pscale(c, zeta(q)))
        Stil[a][b] = ent

# N^2 = sum_j Stil[0,j] * conj(Stil[0,j])  (an element of Q(zeta84), real)
N2 = {}
for j in range(9):
    N2 = padd(N2, pmul(Stil[0][j], pconj(Stil[0][j])))

hs = [ip(root_coords(p), [x + 2 * r for x, r in zip(root_coords(p), RHO)]) / (2 * KH)
      for p in PRIM]
cc = Fr(2 * 78, KH)
Td = [zeta((h - cc / 24) % 1) for h in hs]

# rho_un = T^2 Stil T (matrix over the group ring)
rho_un = [[None] * 9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        rho_un[i][j] = pmul(pmul(Td[i], Td[i]), pmul(Stil[i][j], Td[j]))

# sign of S00: Stil[0][0] is a positive real (sum of positive Weyl terms at the
# vacuum? verify numerically below); assume s = +1 and let the final sign check
# absorb it.
pairs = [(1, 2, 1, 3), (3, 4, 3, -2), (7, 8, 2, -1)]
import mpmath as mp
mp.mp.dps = 40


def ev_num(u):
    tot = mp.mpc(0)
    for k, c in u.items():
        tot += mp.mpf(c.numerator) / mp.mpf(c.denominator)                * mp.e ** (2j * mp.pi * mp.mpf(k) / MOD)
    return tot


print("proving the squared identities mod Phi_84:")
allok = True
for a, b, jp, k in pairs:
    p_un = {}
    p_un = padd(p_un, rho_un[a][a])
    p_un = padd(p_un, pscale(Fr(-1), rho_un[a][b]))
    p_un = padd(p_un, pscale(Fr(-1), rho_un[b][a]))
    p_un = padd(p_un, rho_un[b][b])
    p_un = pscale(Fr(1, 2), p_un)
    # target^2 = (4/7) sin^2(2 pi jp/7) zeta_14^{2k}
    #   sin(t) = (e^{it} - e^{-it})/2i => sin^2 = (2 - z - z^-1)/4 with z = e^{2it}
    z = zeta(Fr(2 * jp, 7) % 1)
    sin2 = pscale(Fr(1, 4), padd({0: Fr(2)}, pscale(Fr(-1), padd(z, pconj(z)))))
    t2 = pscale(Fr(4, 7), pmul(sin2, zeta(Fr(2 * k, 14) % 1)))
    lhs = pmul(p_un, p_un)
    rhs = pmul(t2, N2)
    diff = padd(lhs, pscale(Fr(-1), rhs))
    zero = is_zero_in_field(diff)
    # the sign branch: p_un / (target * N) = +1 numerically
    pn = ev_num(p_un)
    N2n = ev_num(N2)
    tn = (2 / mp.sqrt(7)) * mp.sin(2 * mp.pi * jp / 7) * mp.e ** (2j * mp.pi * k / 14)
    sign_ratio = pn / (tn * mp.sqrt(N2n.real))
    sgn_ok = abs(sign_ratio - 1) < mp.mpf(10) ** -30
    allok &= zero and sgn_ok
    print(f"  pair j'={jp}, k={k}: squared identity mod Phi_84: {zero};  "
          f"sign branch = +1: {sgn_ok} (ratio dev {mp.nstr(abs(sign_ratio-1), 3)})")
assert allok, "certification failed"
print("STEP 6 (v2): the three E6_2 amplitudes are SYMBOLIC IDENTITIES")
print("(squared identity exact in Q(zeta_84); sign branch fixed at 1e-25). DONE")
