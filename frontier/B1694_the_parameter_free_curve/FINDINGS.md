# B1694 — THE PARAMETER-FREE CURVE (P-242): THE ONE COVARIANT HIGGS WITH NO FREE COEFFICIENT RELATES EACH SECTOR'S FIRST GENERATION TO ITS SECOND WITHIN A FACTOR OF ABOUT EIGHT IN ALL THREE CHARGED SECTORS — THE UP QUARKS PASS EVERY CURVE, THE LEPTONS THREE OF FOUR — BUT NO CURVE PASSES ALL THREE: THE DOWN QUARKS AND THE LEPTONS MISS IN OPPOSITE DIRECTIONS

**Verdict: PROVED as sealed for its question (C1, C2, C4 hold; C0 failed as worded; C3 failed).** cc (main), 2026-10-21.
Sealed `90edb73e3` (sha256 a6d90f7e) before either instrument ran; their one run committed unread at `f9a9b2c42`. A test
of a structure, not a value derived. 0 of 19.
- **The curve (no data).** The weight-3/2 section ∂R — the unique covariant Higgs direction of its weight, no free
  coefficient — at the canonical end (B1667's horocycles) with B1656's four-channel coupling and no line gives
  (m₂/m₃, m₁/m₃) as a function of τ alone (B1691's correction). On the CP lines Re τ = 0, ½ and both horocycles, m₂/m₃
  falls monotonically from 0.44–0.62 at Im τ = 1.2 to 2.8–8.3 × 10⁻⁴ at 3.6, and m₁/m₃ falls with it, faster (local
  slope d log m₁/d log m₂ ≈ 1.3–2.1), after a flat start on the L₂ curves (a 1% rise between Im τ = 1.2 and 1.3). Eliminating τ: **m₁/m₃ = F(m₂/m₃), four curves, no free number.**
- **Against the data** (B1637's pinned Huang–Zhou 2021 at M_Z; each sector evaluated where the curve meets its own
  m₂/m₃; ρ = measured m₁/m₃ ÷ F; PASS if the 3σ band of ρ meets [⅓, 3]):

  | curve | up (m_u/m_t = 7.0e-6) | down (m_d/m_b = 9.4e-4) | leptons (m_e/m_τ = 2.8e-4) | all three |
  |---|---|---|---|---|
  | Re τ = 0, L_max | **1.72** PASS | 8.32 FAIL (band 3.46–20.0) | **0.265** PASS | no |
  | Re τ = 0, L₂ | 4.93 PASS (band 2.2–11) | 41.4 FAIL | **2.22** PASS | no |
  | Re τ = ½, L_max | **1.20** PASS | 5.51 PASS (band 2.3–13.4) | 0.169 FAIL | no |
  | Re τ = ½, L₂ | 4.80 PASS | 41.2 FAIL | **2.27** PASS | no |

- **The cells as sealed.** C0 (the shape) failed as worded: the curve starts at 0.44–0.62, not the predicted 0.2–0.3;
  it is monotone and ends below 10⁻³ as predicted. C1 (leptons pass a curve) HOLDS, three of four. C2 (up quarks pass a
  curve) HOLDS, four of four. C3 (down quarks fail every curve) FAILED: they pass one. C4 (no curve passes all three)
  HOLDS.
- **What it means.** The program's one fully parameter-free mass relation reproduces the first-to-second-generation
  relation of the up quarks on every curve and of the leptons on three of four, and on its best curve (Re τ = 0, L_max)
  puts all three charged sectors within a factor of about eight (up 1.7, leptons 0.27, down 8.3) across three orders of
  magnitude of m₁/m₃. It does not pass all three on any curve, and the misses are opposite: measured, the down quarks'
  first generation is heavier relative to its sector than the leptons', although their m₂/m₃ is smaller — a pattern no
  single monotone curve gives. The residue is the down–lepton split again (P-084; B1692, B1693), which in this frame
  needs a line or a second Higgs — each a choice.
- **What it does not do.** Each sector sits at the τ where the curve meets its own m₂/m₃ (up Im τ ≈ 3.1, down ≈ 2.5,
  leptons ≈ 2.1 on the best curve); one fibre has one τ, so the three sectors as computed here cannot share a fibre
  without a line or further Higgs fields (B1693). The test is of the curve's shape, not of one vacuum. No mixing; one
  section; the factor-3 tolerance is a stated allowance, not derived.

## Seen first

`VERDICT topic-sweep /near the cusp|near omega|near ω|q-expansion|residual (charge|symmetr)|exponents? (of|fixed by)|hierarch(y|ies) (from|as) (powers|exponents)|Froggatt|modular weight|discrete exponents/
(full text): 28 of 1462 arcs on main match` (B1691's sweep), and B1654 (the lift), B1656 (the four channels; the
electron's zero at ω), B1660 (the one-Higgs census at ω, NEGATIVE: fitted L, a free Higgs), B1667 (the canonical end),
B1691–B1693. None tests a curve with no free number. **Literature:** the Gatto–Sartori–Tonin and Georgi–Jarlskog
relations as the classical first-to-second-generation patterns (context, not tested).

(As sealed; copied from `PREREGISTRATION.md`.)

## Disclosed (from the seal)

- The curve's first points were computed while exploring and set beside recalled masses before the seal (roughly the
  leptons within a factor 2, the up quarks 5, the down quarks 50 off at L = 2.5); the priors were informed by it. The
  outcome differs from that recollection in the down quarks on L_max (5.5–8.3, not 50), the horocycle the exploration did
  not use.
- C0's wording was a guess at the curve's start; it failed as worded and is reported so.

## Files

- `PREREGISTRATION.md` (sealed), `ARTIFACT_HASHES.txt`; `verification/the_curve.py` → `the_curve.json`,
  `the_curve_run.txt`; `verification/compare.py` → `comparison.json`, `compare_run.txt`; `verification/b1656_funcs.py`.
- The lock: `tests/test_b1694_the_parameter_free_curve.py`.

> *Scope note 2026-10-21 (B1697, the scan for misses).* The section ∂R used here is unique among the covariant sections that carry **one unit of end data on v₊** (B1691's family f₀R + f₁∂R + f₂∂²R is exactly those). The Higgs without end data is unique at weight 7/2, a₀ = ∂²R − E₄R/48 (W68 G1, computed on main in B1697), and gives no second-to-third hierarchy at the cusp (m₂/m₃ → ½). So this arc's hierarchy rests on the Higgs carrying end data on v₊, a datum of FK10's kind (P-245).

> *Scope note 2026-10-22 (B1700, P-245).* ∂R's end data are FK10's tagged unit (W46's), not a second datum: given the unit, the weight-3/2 Higgs directions form a three-dimensional space (W46's three), ∂R is its only member holomorphic off v₊ — the coupling triplet R's own end condition — and the only one giving a hierarchy. So this arc holds given Λ, the unit and H-cov in R's own module.
