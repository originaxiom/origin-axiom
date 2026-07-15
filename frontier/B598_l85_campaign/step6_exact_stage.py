"""Readiness step 6 — exactify the stage data used by P3.

(a) The golden hearing coefficient is ALREADY exact-symbolic (B593-V: zero in
    Q(zeta20); lock test_b593::test_v1_exact_symbolic_amplitude). Cited.
(b) THIS CELL: the E6_2 pair amplitudes upgraded from 40-digit certificates
    (B589) to SYMBOLIC cyclotomic identities: the Weyl sums collected exactly
    (Counter over rational exponents mod 1), the S-matrix normalization N^2
    computed exactly, and sympy proves
        p_j - (2/sqrt7) sin(2 pi j'/7) zeta_14^k = 0
    symbolically for all three pairs.
(c) The classical family (B599-ALG) is exact Fractions already. Cited.

Run: python3 step6_exact_stage.py (~10 min, sympy). Nothing to CLAIMS.md.
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


def root_coords(labels):
    return [sum(CINV[i][j] * Fr(labels[j]) for j in range(6)) for i in range(6)]


def ip(x, y):
    return sum(Fr(c3.C6[i][j]) * x[i] * y[j] for i in range(6) for j in range(6))


RHO = root_coords([1] * 6)
SHIFT = [[a + b for a, b in zip(root_coords(p), RHO)] for p in PRIM]

print("collecting the exact Weyl sums (51840 terms x 45 entries)...")
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
        ST[(a, b)] = ST[(b, a)] = cnt
print("collected; converting to exact sympy cyclotomics...")


def ev(cnt):
    return sum(c * sp.exp(2 * sp.pi * sp.I * sp.Rational(q.numerator, q.denominator))
               for q, c in cnt.items() if c)


Stil = sp.zeros(9, 9)
for a in range(9):
    for b in range(9):
        Stil[a, b] = ev(ST[(a, b)])

# exact normalization: N^2 = sum_j |Stil[0,j]|^2 (must be rational)
N2 = sp.simplify(sp.expand_complex(
    sum(Stil[0, j] * sp.conjugate(Stil[0, j]) for j in range(9))))
print(f"  N^2 (exact) = {N2}")
assert sp.im(N2) == 0

hs = [ip(root_coords(p), [x + 2 * r for x, r in zip(root_coords(p), RHO)]) / (2 * KH)
      for p in PRIM]
cc = Fr(2 * 78, KH)
T = sp.diag(*[sp.exp(2 * sp.pi * sp.I * sp.Rational(((h - cc / 24) % 1).numerator,
                                                    ((h - cc / 24) % 1).denominator))
              for h in hs])

# sign convention: S = s * Stil / N with s = +-1 so that S[0,0] > 0
S00 = sp.simplify(sp.expand_complex(Stil[0, 0]))
sgn = sp.sign(sp.re(S00))
rho_unnorm = T * T * (sgn * Stil) * T          # rho = T^2 S T; ONE factor of 1/N

pairs = [(1, 2, 1, 3), (3, 4, 3, -2), (7, 8, 2, -1)]      # (a, b, j', k)
print("proving the three closed forms symbolically:")
ok = True
NN = sp.sqrt(N2)
for a, b, jp, k in pairs:
    p_un = (rho_unnorm[a, a] - rho_unnorm[a, b] - rho_unnorm[b, a]
            + rho_unnorm[b, b]) / 2
    target = (2 / sp.sqrt(7)) * sp.sin(2 * sp.pi * jp / 7) \
        * sp.exp(2 * sp.pi * sp.I * sp.Rational(k, 14))
    diff = sp.simplify(sp.expand_complex(p_un / NN - target))
    good = diff == 0
    ok &= good
    print(f"  pair ({PRIM[a]},{PRIM[b]}): p - (2/sqrt7) sin({jp}*2pi/7) zeta_14^{k} = {diff}  "
          f"[{'EXACT ZERO' if good else 'NONZERO'}]")
assert ok, "symbolic certification FAILED"
print("STEP 6 (b): the E6_2 amplitudes are now SYMBOLIC IDENTITIES.  DONE")
