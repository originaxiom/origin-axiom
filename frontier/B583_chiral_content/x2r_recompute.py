"""B583-X2R — the corrected X2 recompute (the registered Vol/CS role fix).

X2 as originally computed inverted the roles (verifier catch, banked): Vol is
the REAL growth rate, CS the phase, and CS(4_1) = 0 (amphichiral) makes the
exponential factor real and channel-independent. The interference structure
therefore lives ENTIRELY in the one-loop factors 1/sqrt(tau_m), and the banked
sign law sign(tau_m) = (-1)^m (B581) forces two rigid phase classes:

    theta-odd (chiral) blocks m in {4,8}:  tau_m > 0  =>  1/sqrt(tau_m) REAL
    theta-even (gauge) blocks {1,5,7,11}:  tau_m < 0  =>  purely IMAGINARY

THE QUADRATURE THEOREM (the corrected interference statement): for ANY real
channel weights c_m (e.g. the common real Vol-exponential at any level),
    | sum_m c_m/sqrt(tau_m) |^2 = |chiral part|^2 + |gauge part|^2
— the chiral and gauge channels DO NOT interfere linearly; the chiral sector
enters the modulus only in quadrature. (Another face of the unhearability
chain: first-order interference against the gauge channels vanishes.)

Run: python3 x2r_recompute.py (pyenv, ~1 s). Nothing to CLAIMS.md.
"""
import cmath
import json
import math
import os
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
VOL41 = 2.029883212819307        # Vol(4_1), the real growth rate (CS = 0)

d = json.load(open(os.path.join(HERE, "..", "B581_six_torsions",
                                "six_torsions_results.json")))
TAU = {}
for m in sorted(d, key=int):
    q = d[m]["quotient"]
    assert all(Fraction(c[1]) == 0 for c in q)
    coeffs = [Fraction(c[0]) for c in q]
    lead = coeffs[-1]
    coeffs = [c / lead for c in coeffs]          # the banked monic convention (B581/R17)
    tau = sum(k * coeffs[k] for k in range(len(coeffs)))     # d/dt at t=1
    TAU[int(m)] = tau

print("the six one-loop factors 1/sqrt(tau_m) (sign law => two phase classes):")
ONE_LOOP = {}
ok = True
for m, tau in sorted(TAU.items()):
    assert (tau > 0) == (m % 2 == 0), f"sign law violated at m={m}"
    f = 1 / cmath.sqrt(complex(float(tau)))
    ONE_LOOP[m] = f
    cls = "REAL (chiral)" if m in (4, 8) else "IMAGINARY (gauge)"
    ok &= (abs(f.imag) < 1e-15) if m in (4, 8) else (abs(f.real) < 1e-15)
    print(f"  m={m:>2}: tau = {float(tau):+.6e}   1/sqrt(tau) = {f:+.3e}   {cls}")
assert ok, "phase dichotomy violated"
print("PHASE DICHOTOMY: theta-odd {4,8} real; theta-even {1,5,7,11} imaginary  PASS")

print("\nthe quadrature theorem, verified with the real Vol-exponential weights:")
for kap in (5, 14, 20, 50):
    c = {m: math.exp(-kap * VOL41 / (2 * math.pi)) * (1 + 0.1 * m) for m in TAU}
    total = sum(c[m] * ONE_LOOP[m] for m in TAU)
    chir = sum(c[m] * ONE_LOOP[m] for m in (4, 8))
    gaug = sum(c[m] * ONE_LOOP[m] for m in (1, 5, 7, 11))
    lhs = abs(total) ** 2
    rhs = abs(chir) ** 2 + abs(gaug) ** 2
    assert abs(lhs - rhs) < 1e-12 * max(lhs, rhs)
    print(f"  kap={kap:3d}: |total|^2 = |chiral|^2 + |gauge|^2  exact "
          f"(rel. dev {abs(lhs-rhs)/max(lhs,1e-300):.1e})")
print("\n=> the corrected X2: CS = 0 kills the phase; the sign law is the WHOLE")
print("   interference structure, and it decrees quadrature — the chiral channels")
print("   never interfere linearly with the gauge channels.")
print("ALL GATES PASS")
