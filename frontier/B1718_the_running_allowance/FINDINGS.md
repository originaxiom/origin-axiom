# B1718 — THE RUNNING ALLOWANCE (P-265; no fit): in the SM at one loop the within-sector mass ratios every sealed test compares run by at most 12% in log up to 10¹⁶ GeV (13% to 10¹⁸), up-type down and down-type up, the leptons not at all; the tests' 10% allowance covers the running strictly only to 10⁸ GeV, and no sealed verdict turns on the difference

**Verdict: PROVED** (a computation with the standard one-loop SM equations, a premise audit of the sealed tests). cc
(main), 2026-10-22. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /10% allowance|ratios? run|running of the (mass )?ratio|within.sector ratio|one.loop SM|Yukawa running/ (full text): 2 of 1488 arcs on main match (PROVED 2)`. The two are B1693, where the allowance first appears, and this arc. A broader sweep of renormalisation and running matches 874 arcs, the record's value-layer runs, none on within-sector ratios. The audited premise is the 10% allowance in every sealed mass
test since B1693 (B1693–B1713), which was never derived (P-265). The SM seat's W119 gave one-loop factors 0.545–1.130,
but on double ratios that mix sectors, where QCD does not cancel. **Literature:** the standard one-loop SM
renormalisation-group equations (Machacek and Vaughn; Arason et al. 1992).

## 1. What was computed (`verification/the_running_allowance.py`)

**Why only the Yukawa term matters.** Every sealed cell compares m₂/m₃ and m₁/m₃ within one charged sector. In such a
ratio the gauge terms (QCD included) and the trace T cancel, so only the Yukawa matrix term ±(3/2)(y_u² − y_d²) is left.

**The setup.**
- Three generations of diagonal Yukawas; mixing is neglected in the running.
- The Yukawas at M_Z are y = √2 m/v, from the pinned Huang–Zhou masses (B1637's file, sha 63450365…).
- The gauge couplings at M_Z are standard quoted values.
- Each gauge coupling is moved by ±3% as a sensitivity check.

| scale (GeV) | y_t | c/t, u/t | s/b, d/b | μ/τ, e/τ | largest ∣log∣ | sensitivity |
|---|---|---|---|---|---|---|
| 10⁴ | 0.788 | 0.967 | 1.034 | 1.000 | 0.034 | 0.0005 |
| 10⁸ | 0.613 | 0.927 | 1.078 | 1.000 | 0.076 | 0.0024 |
| 10¹² | 0.514 | 0.902 | 1.109 | 1.000 | 0.103 | 0.0043 |
| 10¹⁶ | 0.445 | 0.884 | 1.131 | 1.000 | 0.123 | 0.0061 |
| 10¹⁸ | 0.418 | 0.877 | 1.140 | 1.000 | 0.131 | 0.0069 |

(Each entry is the ratio at the scale over the ratio at M_Z. The two ratios of a sector share their factor to the
printed digits, since only the third generation's coupling drives the running.)

## 2. What it means

- **The premise holds to the precision the cells need.**
  - The running is a systematic shift with a known sign, not a scatter: up-type ratios fall with the scale and
    down-type ratios rise.
  - It reaches 12% by 10¹⁶ GeV. Against the factor-3 cells (H1, K1) and the calibrations, which use the same rows, that
    is small.
  - The 10% allowance strictly covers the running only up to 10⁸ GeV.
- **The χ² cells would loosen.** Their quark terms loosen by at most (0.10/0.13)² ≈ 0.6 if the fibre's scale were near
  the Planck scale. Every sealed χ² (B1711: 321; B1712: 108.5) stays far above 16.75.
- **A post hoc illustration, not a re-test.** At 10¹⁶ GeV, B1712's best point moves from a factor 2.37 to 2.31 against
  the run-up targets.
- **Scope.**
  - The SM content only. A second Higgs or new states change the Yukawa term (in a type-II two-Higgs model at large
    tan β the down-type running grows).
  - The fibre's scale is not derived (0 of 19), so the allowance is bounded, not fixed.

## Files

- `verification/the_running_allowance.py` → `the_running_allowance.json`, `the_running_allowance_run.txt`.
- The lock: `tests/test_b1718_the_running_allowance.py`.
