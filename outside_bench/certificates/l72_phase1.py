"""OUTSIDE BENCH -- L72 PHASE 1: the E6-principal torsion, and what its blocks obey.

Seal: outside_bench/seals/L72_PHASE1_PREREG.md
      sha256 962d708047fb5e47f761a41bdb952dd75c0bf8189b0c109771cb1805cd7dcf7e
      committed and pushed before this file was written.

Input: B581's EXACT coefficients, frontier/B581_six_torsions/six_torsions_results.json.
Nothing is re-derived from the knot group here -- B581 owns that, and its own analytic
gate (C2) is re-run below before any of its numbers are used.

CELL 1  the order of vanishing of the product at t = 1
CELL 2  the two routes to the principal torsion
CELL 3  what the six torsions obey                       [NEW]

Run: python3 outside_bench/certificates/l72_phase1.py
"""
import json
import pathlib
from fractions import Fraction

import mpmath as mp
import sympy as sp

mp.mp.dps = 40
ROOT = pathlib.Path(__file__).resolve().parents[2]
EXPONENTS = [1, 4, 5, 7, 8, 11]
t = sp.Symbol('t')

BANKED_TAU = {          # B581's FINDINGS.md table, transcribed for the C1 comparison
    1: -3,
    4: 260736,
    5: -165110400,
    7: -3257341296168960,
    8: 100636318520821923840,
}
BANKED_FACTORS = {      # B581's stated factorizations
    4: '2^7*3*7*97',
    5: '-2^7*3^4*5^2*7^2*13',
    7: '-2^12*3^4*5*7^5*11*13*19*43',
    8: '2^14*3^3*5*7^3*11*13*31*607*49297',
}

print("=" * 78)
print("L72 PHASE 1 -- outside bench")
print("seal sha256 962d708047fb5e47f761a41bdb952dd75c0bf8189b0c109771cb1805cd7dcf7e")
print("=" * 78)

raw = json.loads((ROOT / 'frontier/B581_six_torsions/six_torsions_results.json').read_text())

# ---------------------------------------------------------------- C3: structure
print("\nC3 -- structure of the six banked polynomials")
DELTA = {}
for m in EXPONENTS:
    q = raw[str(m)]['quotient']
    assert all(b == '0' for _, b in q), f"m={m}: a coefficient has a non-zero sqrt(-3) part"
    c = [int(a) for a, _ in q]                       # highest degree first
    d = len(c) - 1
    skew = all(c[k] == -c[d - k] for k in range(d + 1))
    poly = sum(sp.Integer(c[k]) * t**(d - k) for k in range(d + 1))
    at1 = sp.expand(poly.subs(t, 1))
    print(f"  m={m:2d}  deg={d:2d}  integer coeffs=True  skew-palindromic={skew}  "
          f"Delta_m(1)={at1}")
    assert skew and at1 == 0, f"m={m}: structure gate failed"
    DELTA[m] = sp.Poly(poly, t)
assert raw['1']['exact'], "B581's m=1 block is not flagged exact"

# ---------------------------------------------------------------- C2: analytic gate
print("\nC2 -- the analytic gate B581 required of itself (m = 1)")
f = sp.factor(DELTA[1].as_expr())
print(f"  Delta_1(t) = {sp.expand(DELTA[1].as_expr())}  factors as  {f}")
assert sp.simplify(f - (t - 1) * (t**2 - 5 * t + 1)) == 0, "m=1 is not (t-1)(t^2-5t+1)"
tau1 = sp.diff(DELTA[1].as_expr(), t).subs(t, 1)
print(f"  tau_1 = Delta_1'(1) = {tau1}   (B425's banked value: -3)")
assert tau1 == -3

# ---------------------------------------------------------------- C1: the table
print("\nC1 -- B581's banked table, recomputed from its own coefficients")
TAU = {}
for m in EXPONENTS:
    TAU[m] = int(sp.diff(DELTA[m].as_expr(), t).subs(t, 1))
    fac = sp.factorint(abs(TAU[m]))
    facs = '*'.join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(fac.items()))
    sign = '-' if TAU[m] < 0 else ''
    banked = BANKED_TAU.get(m)
    ok = '' if banked is None else ('  == banked' if TAU[m] == banked else '  *** MISMATCH ***')
    print(f"  tau_{m:<2d} = {TAU[m]}")
    print(f"          = {sign}{facs}{ok}")
    if banked is not None:
        assert TAU[m] == banked, f"m={m}: {TAU[m]} != banked {banked}"
    if m in BANKED_FACTORS:
        assert f"{sign}{facs}" == BANKED_FACTORS[m], \
            f"m={m}: factorization {sign}{facs} != banked {BANKED_FACTORS[m]}"
print(f"  tau_11 ~ {mp.nstr(mp.mpf(TAU[11]), 6)}   (B581 prints -6.9081...e36)")
assert str(mp.nstr(mp.mpf(TAU[11]), 5)).startswith('-6.9081'), "tau_11 magnitude differs from B581"

# ---------------------------------------------------------------- C5: the sign law
print("\nC5 -- the sign law  sign(tau_m) = (-1)^m")
hits = sum(1 for m in EXPONENTS if (TAU[m] > 0) == (m % 2 == 0))
for m in EXPONENTS:
    print(f"  m={m:2d}  sign(tau_m)={'+' if TAU[m] > 0 else '-'}  (-1)^m="
          f"{'+' if m % 2 == 0 else '-'}  theta-{'odd' if TAU[m] > 0 else 'even'}")
print(f"  sign law holds {hits}/6")
assert hits == 6

# ============================================================ CELL 1
print("\n" + "=" * 78)
print("CELL 1 -- the E6-principal polynomial")
print("=" * 78)
prod = sp.Integer(1)
for m in EXPONENTS:
    prod = prod * DELTA[m].as_expr()
DE6 = sp.Poly(sp.expand(prod), t)
deg = DE6.degree()
dims = [2 * m + 1 for m in EXPONENTS]
print(f"  deg Delta_E6 = {deg}      sum of block degrees = {sum(DELTA[m].degree() for m in EXPONENTS)}")
print(f"  the adjoint tiling: dims Sym^2m = {dims}, sum = {sum(dims)}  (dim E6 = 78)")
assert sum(dims) == 78, "the six Sym^{2m} blocks do not tile the 78"
order = 0
g = DE6.as_expr()
while sp.expand(g.subs(t, 1)) == 0:
    order += 1
    g = sp.diff(g, t)
print(f"  order of vanishing of Delta_E6 at t = 1 : {order}")
print(f"  CELL 1 OUTCOME: {'A' if order == 6 else 'B'}")

# ============================================================ CELL 2
print("\n" + "=" * 78)
print("CELL 2 -- the two routes to the principal torsion")
print("=" * 78)
route_a = sp.Integer(1)
for m in EXPONENTS:
    route_a *= TAU[m]
route_a = int(route_a)
d6 = sp.diff(DE6.as_expr(), t, 6).subs(t, 1)
route_b = sp.Rational(d6, sp.factorial(6))
print(f"  route A  Pi tau_m               = {route_a}")
print(f"  route B  Delta_E6^(6)(1) / 6!   = {route_b}")
print(f"  equal exactly as integers: {sp.Integer(route_a) == route_b}")
print(f"  CELL 2 OUTCOME: {'A' if sp.Integer(route_a) == route_b else 'B'}")
TAU_E6 = route_a
fac = sp.factorint(abs(TAU_E6))
print(f"\n  tau_E6 = {TAU_E6}")
print(f"         = {'-' if TAU_E6 < 0 else '+'}"
      + '*'.join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(fac.items())))
print(f"         ~ {mp.nstr(mp.mpf(TAU_E6), 8)}   sign = {'+' if TAU_E6 > 0 else '-'}"
      f"   (forced: (-1)^(sum of exponents) = (-1)^{sum(EXPONENTS)})")
assert (TAU_E6 > 0) == (sum(EXPONENTS) % 2 == 0)

# ============================================================ CELL 3 + C4
print("\n" + "=" * 78)
print("CELL 3 -- what the six torsions obey")
print("=" * 78)
VOL = 2 * mp.clsin(2, mp.pi / 3)
print(f"  Vol(4_1) = 2*Cl_2(pi/3) = {mp.nstr(VOL, 30)}")
print(f"  Vol/pi                  = {mp.nstr(VOL / mp.pi, 30)}")
print()
R, Rwrong = {}, {}
for m in EXPONENTS:
    L = mp.log(abs(mp.mpf(TAU[m])))
    R[m] = L - (VOL / mp.pi) * m * (m + 1)
    Rwrong[m] = L - (VOL / mp.pi) * m * m
    print(f"  m={m:2d}  log|tau_m| = {mp.nstr(L, 12):>16s}   "
          f"R_m = log|tau_m| - (Vol/pi)m(m+1) = {mp.nstr(R[m], 10):>14s}   "
          f"[wrong law: {mp.nstr(Rwrong[m], 10):>14s}]")
tail = [m for m in EXPONENTS if m >= 4]
spread = max(R[m] for m in tail) - min(R[m] for m in tail)
spread_w = max(Rwrong[m] for m in tail) - min(Rwrong[m] for m in tail)
print(f"\n  spread of R_m over m in {tail} : {mp.nstr(spread, 10)}")
print(f"  m = 1 reported separately        : R_1 = {mp.nstr(R[1], 10)}")
print(f"\n  C4 (MB12 transversality) -- the same statistic against the WRONG law m^2:")
print(f"     spread = {mp.nstr(spread_w, 10)}   must be >= 0.05 for CELL 3 to be readable")
c4 = spread_w >= mp.mpf('0.05')
print(f"     C4 verdict: the statistic DISCRIMINATES = {c4}")
if not c4:
    print("  *** C4 FAILED -- CELL 3 may not be read (memo 164). Stopping.")
    raise SystemExit(1)
print(f"\n  CELL 3 OUTCOME: {'A' if spread < mp.mpf('0.05') else 'B'}"
      f"   (threshold 0.05, preregistered)")
if spread < mp.mpf('0.05'):
    mean = sum(R[m] for m in tail) / len(tail)
    print(f"  the constant the residual settles to: {mp.nstr(mean, 15)}")
    print(f"  for reference only, NOT a claim: "
          f"Vol/(4pi) = {mp.nstr(VOL/(4*mp.pi), 12)},  "
          f"log 2 = {mp.nstr(mp.log(2), 12)},  "
          f"Vol/pi = {mp.nstr(VOL/mp.pi, 12)}")

# ---------------------------------------------------------------- POST-HOC (not sealed)
print("\n" + "-" * 78)
print("POST-HOC DIAGNOSTIC -- NOT PREREGISTERED, reported as such")
print("-" * 78)
print("  Least-squares fit  log|tau_m| = A*m^2 + B*m + C  on the five tail points,")
print("  then each coefficient divided by Vol/pi.  The seal's m(m+1) form predicts 1 and 1.")
A = mp.matrix([[mp.mpf(m)**2, mp.mpf(m), mp.mpf(1)] for m in tail])
y = mp.matrix([mp.log(abs(mp.mpf(TAU[m]))) for m in tail])
coef = mp.lu_solve(A.T * A, A.T * y)
vp = VOL / mp.pi
print(f"     A = {mp.nstr(coef[0], 12):>15s}   A / (Vol/pi) = {mp.nstr(coef[0]/vp, 10)}")
print(f"     B = {mp.nstr(coef[1], 12):>15s}   B / (Vol/pi) = {mp.nstr(coef[1]/vp, 10)}")
print(f"     C = {mp.nstr(coef[2], 12):>15s}")
print()
print("  Menal-Ferrer--Porti / Mueller give the LEADING term for cusped hyperbolic M:")
print("     log|tor(Sym^n)| / n^2 -> Vol/(4pi).   With n = 2m that is A -> Vol/pi.")
print(f"     Vol/(4pi) = {mp.nstr(VOL/(4*mp.pi), 12)};  A/4 = {mp.nstr(coef[0]/4, 12)}")
print()
print("  Written in the block DIMENSION d_m = 2m+1, the fitted form reads")
print("     log|tau_m| ~ (Vol/4pi)*(d_m^2 - 1) + C,   since 4*m(m+1) = (2m+1)^2 - 1.")
for m in EXPONENTS:
    d = 2 * m + 1
    pred = (VOL / (4 * mp.pi)) * (d * d - 1)
    print(f"     m={m:2d}  d={d:2d}  (Vol/4pi)(d^2-1) = {mp.nstr(pred, 12):>15s}   "
          f"log|tau_m| - that = {mp.nstr(mp.log(abs(mp.mpf(TAU[m]))) - pred, 10)}")
print()
print("  THE CONSTANT IS NOT IDENTIFIED, AND NO IDENTIFICATION IS ATTEMPTED.")
print(f"     The five tail residuals agree to a spread of {mp.nstr(spread, 6)} -- about four")
print("     significant figures. Four figures cannot support an identification, and this")
print("     bench has a banked precedent for exactly that overreach (B583 X2, a PSLQ-null")
print("     overclaim). The constant is reported and left open.")

print("\n" + "=" * 78)
print("DONE -- outcomes above; interpretation lives in the memo, not here.")
print("=" * 78)
