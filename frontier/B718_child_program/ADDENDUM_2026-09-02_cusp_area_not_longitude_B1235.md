# ADDENDUM (2026-09-02, B1235) — one label corrected: the Neumann–Zagier constant is π²·(cusp AREA), not π²·(cusp longitude)

**What is wrong.** `b718_probe4.py:95` prints, of the Richardson-extracted leading constant in the
volume deficit vol(4₁) − vol(4₁(p,1)) ≈ C/L²:

> `C = pi^2 * (2*sqrt3) = pi^2 * (cusp longitude)`

The **number** is right (C = π²·2√3 = 34.19, reproduced at the time and again today). The **label**
is wrong. Neumann–Zagier's asymptotic is ΔV ≈ π²·A / L(p,q)², with **A the cusp area** and L the
slope length in the same cusp metric. So C = π²·A — an area-weighted constant.

**Why it decides itself.** Under g → k²g (the B1022 weight ledger): a length has weight +1, an area
+2, a volume +3. C/L² is a volume deficit — the leading term must be weight-0 relative to the
scale-covariant volume, so C must carry weight +2: an **area**, never a length. A constant labelled
"longitude" (weight +1) divided by L² (weight +2) is not even homogeneous.

**Why the slip was invisible.** At m004's maximal cusp |meridian| = 1 exactly, so the longitude's
length and the cusp area are **the same number**, 2√3 = 3.464102 (the cusp is rectangular, shape
2√3·i). Same number, different weight. `verification/b718_cusp_area_check.py` in B1235 shows both
from SnapPy and prints the weight argument.

**What is NOT wrong.** Line 148 — `12 = (2*sqrt3)^2 = longitude^2` inside L² = 12 + p² — is correct
as written: there the longitude's *length* enters the slope-length formula |p·μ + λ|² = p²·|μ|² + |λ|²,
and |λ|² = 12. FINDINGS.md:50–51 give values only and are correct. No result, number or verdict of
B718 changes; the ℚ(√−3) flavour of the constant is unaffected (2√3 is the area, and the area is
√−3-valued).

**Source.** Found by cc3's HARVEST_MANIFEST (2026-08-09, lost with the E51 files, recovered and read
under B1235); re-derived here before writing.
