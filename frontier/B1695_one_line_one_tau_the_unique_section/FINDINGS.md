# B1695 — ONE LINE, ONE τ, THE UNIQUE SECTION (P-243): ALL SIX CHARGED-FERMION MASS RATIOS COME WITHIN A FACTOR OF 1.8 FROM TWO CONTINUOUS NUMBERS — BUT NOT TO THE DATA'S PRECISION, AND A CALIBRATION AFTER THE SEAL SHOWS THE MATCH IS NOT SPECIFIC: WRONG SECTOR ASSIGNMENTS FIT AS WELL, AND 6% OF RANDOM HIERARCHIES FIT AS WELL

**Verdict: PROVED as sealed for its question (G1 holds; G2's prediction failed — the cell passed).** cc (main),
2026-10-21. Sealed `fc3bf0684` (sha256 aced715b) before either instrument ran; their one run committed unread at
`cedc14c5b`. A test of a structure, not a value derived. 0 of 19.
- **The model (no data).** The weight-3/2 section ∂R (no free coefficient; B1691) at B1667's canonical end with B1656's
  four-channel coupling, one flat hypercharge line w = α τ and one τ shared by the three charged sectors: six ratios
  (m₂/m₃, m₁/m₃ for up, down, leptons) from two continuous numbers (α, Im τ) and twelve discrete choices (Re τ ∈ {0, ½};
  L_max or L₂; B1660's three readings of the up sector), on a grid of 2 009 points per choice (α = j/96, j ≤ 48;
  Im τ = 1.5–3.5).
- **Against the data** (Huang–Zhou 2021 at M_Z, B1637's pinned transcription):
  - **G1 (strict, χ² < 14.86 with σ² = the data's errors² + B1637's 10%²): FAILS, as predicted** — the grid's minimum
    χ² is 61.3.
  - **G2 (all six within a factor 3 somewhere): PASSES — the prediction (FAIL, 65%) failed.** 29 grid points; the best
    (Re τ = 0, L_max, the up sector read through the conjugate Higgs S̃, α = 37/96, Im τ = 3.15) has every ratio within
    a factor of 1.79:

    | sector | m₂/m₃ model / measured | m₁/m₃ model / measured |
    |---|---|---|
    | up | 0.00446 / 0.00368 (1.21) | 1.24 × 10⁻⁵ / 7.31 × 10⁻⁶ (1.70) |
    | down | 0.0335 / 0.0187 (1.79) | 8.26 × 10⁻⁴ / 9.40 × 10⁻⁴ (0.88) |
    | leptons | 0.0343 / 0.0589 (0.58) | 2.48 × 10⁻⁴ / 2.79 × 10⁻⁴ (0.89) |

    The first generation's down–lepton ratio is 3.3 against the measured 3.4; the second generation's is about 1 against
    3.1, the two worst misses.
- **After the seal (labelled; `verification/after_the_seal/calibration.py`, only the stored grid).**
  - **Not sector-specific.** Assigning the six measured ratios to the sectors in the five wrong orders, the grid's best
    worst-factor is 1.58, 1.64, 1.91, 2.41 and 2.89: two wrong orders fit better than the true one (1.79).
  - **Not rare.** Of 2 000 random hierarchical target sets (per sector log₁₀ m₂/m₃ uniform in [−3, −1], log₁₀ m₁/m₃ in
    [−6, −2.5], m₁ < m₂), 6.25% are fitted at least as well; the median random set reaches 3.3.
- **What it means.** In this frame one line, one τ and the unique section can produce charged-fermion hierarchies of the
  observed size — all six ratios to within a factor of two — but the grid fits roughly one random hierarchy in sixteen as
  well, and the sectors' identities do not matter to the fit. So the match measures the frame's flexibility (two
  continuous numbers and twelve discrete choices), not a prediction; it is no evidence for the frame beyond B1694's, and
  it is not a value contact to bank. The second generation's down–lepton split (3.1 measured, about 1 here) is the
  frame's clearest miss, the d–e wall again (P-084).
- **What it does not do.** A grid, not an optimiser (its minimum χ² is an upper bound); β = 0 only; one section; the
  calibration's random prior is main's choice, stated.

## Seen first

`VERDICT topic-sweep /Georgi|Jarlskog|d.e wall|down quarks? (from|and) (the )?(charged )?leptons|cross.sector|two Higgs|2HDM|H_u|second.to.third|2.3 hierarch/
(full text): 37 of 1464 arcs on main match` (B1693's sweep), and B1660 (the one-Higgs census at ω on W59's lines with a
free Higgs and a fitted L: NEGATIVE, χ² 34.4 at best), B1656 (the twisted frame), B1691–B1694. None fits the six ratios
with the unique section at the canonical end near the cusp. **Literature:** none beyond B1694's.

(As sealed; copied from `PREREGISTRATION.md`.)

## Disclosed (from the seal, and after)

- The six measured ratios and B1694's misses were known before the seal; the grid's values were not computed (one
  point timed).
- G2's prediction (FAIL) failed; the reading written before the run for that case ("a near-miss, graded a READING") is
  sharpened by the calibration done after the seal, which was not sealed and is labelled: the near-miss is not specific.

## Files

- `PREREGISTRATION.md` (sealed), `ARTIFACT_HASHES.txt`; `verification/the_grid.py` → `the_grid.json`, `the_grid_run.txt`;
  `verification/compare.py` → `comparison.json`, `compare_run.txt`; `verification/b1656_funcs.py`;
  `verification/after_the_seal/calibration.py` → `calibration.json`.
- The lock: `tests/test_b1695_one_line_one_tau_the_unique_section.py`.

> *Scope note 2026-10-21 (B1697, the scan for misses).* The section ∂R used here is unique among the covariant sections that carry **one unit of end data on v₊** (B1691's family f₀R + f₁∂R + f₂∂²R is exactly those). The Higgs without end data is unique at weight 7/2, a₀ = ∂²R − E₄R/48 (W68 G1, computed on main in B1697), and gives no second-to-third hierarchy at the cusp (m₂/m₃ → ½). So this arc's hierarchy rests on the Higgs carrying end data on v₊, a datum of FK10's kind (P-245).
