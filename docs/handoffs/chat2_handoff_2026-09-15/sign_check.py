#!/usr/bin/env python3
"""
R4b sign check: one-loop β-coefficients at each stage of the D-chain
E₆ ⊃ SO(10)×U(1) ⊃ SO(8)×U(1)² ⊃ SU(4)×U(1)³ ⊃ SU(3)×U(1)⁴

Convention: dα⁻¹/d(ln Q) = b/(2π), b > 0 = asymptotically free.

FERMION CONTENT assumed at each stage:
  3 generations of 16 of SO(10) (= 3 SM families + 3 ν_R).
  Branching at each stage is APPROXIMATE — see the CAVEAT below.

HIGGS CONTENT:
  One complex 10 of SO(10) (the Higgs doublet in the 10 ⊂ 27, THEOREM
  per B978/B884/B987; the SO(10) grading 27 → 16+10+1 is EARNED at I-22).
  Scalar contribution: -(1/3) × T(R) × 2 (complex = 2 real d.o.f.)

CAVEAT (from Chat-2, stated before the computation):
  Fermion counting at SO(8) and SU(4) stages uses approximate branching:
  "~3 Dirac 8's per generation at SO(8)" and "~4 Dirac fundamentals per
  generation at SU(4)." The exact branching from the CMT data (B911) may
  differ by O(1) per generation. The margins (20.67, 9.33, 6.00) are large
  enough that O(1) corrections do not flip signs — but CC should recompute
  with exact branching rules from B911 before banking.

Result: ALL POSITIVE. R4b survives the sign check.
Recompute with exact content before gating R4b on this.
"""

# === THE COMPUTATION ===

# Stage 4: SO(10) × U(1)
# C₂(SO(10)) = 8
# Matter: 3 Dirac 16 (T(16) = 2 each) + 1 complex scalar 10 (T(10) = 1)
b_gauge_SO10 = (11/3) * 8  # = 29.33
b_ferm_SO10 = -(2/3) * 3 * 2 * 2  # 3 gen, Dirac (×2), T(16)=2: = -8.00
b_higgs_SO10 = -(1/3) * 1 * 2  # 1 complex 10, T(10)=1: = -0.67
b_SO10 = b_gauge_SO10 + b_ferm_SO10 + b_higgs_SO10
print("SO(10):  gauge=%.2f  ferm=%.2f  higgs=%.2f  TOTAL=%.2f  AF=%s" %
      (b_gauge_SO10, b_ferm_SO10, b_higgs_SO10, b_SO10, "YES" if b_SO10 > 0 else "NO"))

# Stage 3: SO(8) × U(1)²
# C₂(SO(8)) = 6
# Matter: from 16 → 8_s + 8_c under SO(8), each gen contributes ~3 Dirac 8-dim reps
#   T(8_v) = T(8_s) = T(8_c) = 1 for SO(8)
# APPROXIMATE: 3 gen × 3 Dirac reps × T=1 = 18 fermion units
b_gauge_SO8 = (11/3) * 6  # = 22.00
b_ferm_SO8 = -(2/3) * 3 * 3 * 1 * 2  # 3 gen, ~3 reps, Dirac, T=1: = -12.00
b_higgs_SO8 = -(1/3) * 1 * 2  # 10 → 8_v + 1 + 1, the 8_v piece: = -0.67
b_SO8 = b_gauge_SO8 + b_ferm_SO8 + b_higgs_SO8
print("SO(8):   gauge=%.2f  ferm=%.2f  higgs=%.2f  TOTAL=%.2f  AF=%s" %
      (b_gauge_SO8, b_ferm_SO8, b_higgs_SO8, b_SO8, "YES" if b_SO8 > 0 else "NO"))

# Stage 2: SU(4) ≅ SO(6) × U(1)³
# C₂(SU(4)) = 4
# Matter: each gen contributes ~4 Dirac fund (T(4)=1/2) from 8_s → 4+4̄ etc.
# APPROXIMATE: 3 gen × 4 Dirac fund × T=1/2 = 12 fermion units
b_gauge_SU4 = (11/3) * 4  # = 14.67
b_ferm_SU4 = -(2/3) * 3 * 4 * (1/2) * 2  # 3 gen, ~4 reps, Dirac, T=1/2: = -8.00
b_higgs_SU4 = -(1/3) * 1 * 2  # complex 6 of SU(4), T(6)=1: = -0.67
b_SU4 = b_gauge_SU4 + b_ferm_SU4 + b_higgs_SU4
print("SU(4):   gauge=%.2f  ferm=%.2f  higgs=%.2f  TOTAL=%.2f  AF=%s" %
      (b_gauge_SU4, b_ferm_SU4, b_higgs_SU4, b_SU4, "YES" if b_SU4 > 0 else "NO"))

# Stage 1: SM (for reference)
# b₃ = 11 - (4/3)×3 = 7, with Higgs: 7 - 0 = 7 (Higgs is SU(3) singlet)
print("SM(SU3): b = 7.00  (standard)")

print()
print("RESULT: b = (%.2f, %.2f, %.2f) at (SO(10), SO(8), SU(4))" % (b_SO10, b_SO8, b_SU4))
print("ALL POSITIVE — R4b survives the sign check.")
print("SMALLEST MARGIN: %.2f at SU(4). An O(1) error in fermion counting" % b_SU4)
print("would change this by ~1.3 (= 2/3 × T × 2), not enough to flip.")
