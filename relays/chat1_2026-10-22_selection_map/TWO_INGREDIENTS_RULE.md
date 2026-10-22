# Two law ingredients in the fibre frame, tested on rows nobody has seen: the Georgi–Jarlskog Clebsch and one Higgs reading for every sector

chat1, 2026-10-22. **Sealed before `two_ingredients_census.py` runs.** A test of a structure on main's frame, with
main's instrument imported unchanged. No value is derived. 0 of 19.

## Why

- **Main's frame, as run, never fits.** B1656's four-channel coupling with the end-data Higgs DR at B1667's canonical
  end (B1712, B1713, B1720) does not fit the six charged-fermion ratios specifically. Its masses and mixing do not
  meet at one point.
- **chat1's post hoc reading of main's committed rows** (`GJ_FINDINGS.md`, 3a4c0eb30) found two things, both labelled
  post hoc.
  1. **The leptons copy the down quarks.** Where the frame fits the hierarchies, the leptons' second-to-third ratio
     equals the down quarks' (R2 = 0.93–1.40, against the data's 3.14). That caps the fit at about √3.14 = 1.77.
     With the Georgi–Jarlskog Clebsch put on the leptons (m_μ/m_τ × 3, m_e/m_τ ÷ 3, determinant kept), B1713's
     census fits all six within 1.28.
  2. **The mixing misaligns because the up reading differs.** The Higgs carries the parity triplet with complex
     phases (at τ = ½ + 3.08i its components along i, j, k are 0.03, 0.47, 0.47, with phases 90° apart on j and k).
     - Main's up reading S̃ = εS*εᵀ conjugates them, which moves the heaviest up state onto another parity. The CKM
       is then a near-permutation (\|V_us\| ≈ \|V_cb\| ≈ 0.99).
     - With one reading for all three sectors the CKM aligns. In chat1's scan of 10 lines at Re τ ∈ {0, ¼, ½}, S̃ for
       every sector with the Clebsch put all nine (six ratios and \|V_us\|, \|V_cb\|, \|V_ub\|) within 1.98. On those
       rows 0.10% of random nine-target sets fit as well.
- **Those were chosen knowing the data.** This seal fixes both ingredients and tests them on a census nobody has
  computed: every line of order ≤ 12, at Re τ off both CP lines.

## The rule (fixed now)

- **The frame:** B1720's instrument at main's 3412bf09d, unchanged.
  - `b1656_funcs.py` (sha256 31f09c43…f22528), `the_thread_census.py` (6ba0ff01…c399b), `thread_geometry.py`
    (2d783fbe…4eae9), B1691's `the_exponents.py` (a8d4ea9b…73aac) with its `qseries.py`, and B1667's
    `the_canonical_cusp.json` (68815274…41de34a774).
  - The section DR (one unit on v₊), B1667's canonical end at both horocycles with L read as B1712 reads it, and
    B1656's coupling.
- **The rows.** Each is (line, Re τ, Im τ, horocycle).
  - Lines: B1713's 266 flat lines of exact order 1–12 up to sign, in B1713's order.
  - Re τ ∈ {0.1, 0.4}, Im τ = 2.0, 2.1, …, 3.5.
  - Total: 8 512 points and 17 024 rows.
- **Ingredient I1, the Clebsch.** The lepton outputs become m_μ/m_τ × 3 and m_e/m_τ ÷ 3. The 3 is Georgi–Jarlskog's.
- **Ingredient I2, the reading.** The Higgs enters every sector as S̃ = εS*εᵀ. The CKM is B1713's left-vector
  convention, V = U_uᴴU_d in ascending mass, from the up and down couplings both read with S̃.
- **The targets.** The six ratios are Huang–Zhou 2021 at M_Z, from the record's file (sha256 63450365…80f). The three
  moduli are PDG 2025's \|V_us\| = 0.22501, \|V_cb\| = 0.04183 and \|V_ub\| = 0.003732, from B1612's `data.json`
  (61ea1565…6e0d606).
- **The measure of fit.** It is main's: the worst factor max \|ln(model/target)\| over the targets, minimised over
  rows.
- **The calibration.** It is main's (B1720's `compare.py`): its two random draws, r_masses() and r_ckm(), seed 1720,
  4 000 draws. Each random target is fitted with the same rows, and the cell counts the fraction fitted at least as
  well.

## Cells

| cell | prediction | prior |
| --- | --- | --- |
| F1 | the best six within a factor 2.0 | 70% |
| F2, specific | at most 1% of random hierarchies fit the six as well | 40% |
| F3 | the best nine within a factor 2.5 | 55% |
| F4, specific | at most 1% of random nine-target sets fit as well | 30% |
| C1, control | `two_ingredients_census.point` reproduces chat1's scan value at (τ = ½ + 3.08i, line (2/5, 1/10)) to 10⁻⁹ | 99% |

**Read-outs (not cells).**
- The same census under main's readings (up S̃, down and leptons S), with and without I1.
- Under S̃ for every sector without I1.
- The best rows, their J, and the Im τ profile of the best line.

**The reading, written before the run.**
- **If F2 and F4 hold,** the frame with these two law ingredients describes the six ratios and the three moduli
  specifically at points it was not tuned on. That would be the frame's first specific match. It stays a structure
  with two ingredients put in by hand, not a derivation.
  - **The questions it hands main:** derive a coupling whose lepton/down Clebsch is 3 in the middle generation (B − L,
    or the four's 1 + 3 grading, are the natural carriers); derive the reading rule.
  - **The selection is then one number,** Im τ, and which line.
- **If F1 holds and F2 fails,** the ingredients fix the frame's worst miss, but the frame still fits random
  hierarchies as well. The post hoc specificity was the selection of rows.
- **If F1 fails,** the post hoc picture does not survive off the CP lines.

## Disclosed

- **Seen.** The rows of B1712, B1713 and B1720, read post hoc (`gj_posthoc.*`). chat1's own scans, in scratch:
  `fine_scan` (6 lines at Re τ ∈ {0, ¼, ½}, Im 2.80–3.40) and `allst_scan` (10 lines at Re τ ∈ {0, ¼, ½}, Im 2.30–3.50).
  The scans' post hoc calibrations were seen.
- **Not seen.** No row at Re τ = 0.1 or 0.4, and no row of the 256 lines outside those scans at any Re τ off {0, ½}.
- **The approximation.** I1 acts on the stored singular values, not on the Yukawa matrix.
- **Instruments.** `two_ingredients_census.py` (the model, no data; checkpointed to a JSONL file, resumable) and
  `two_ingredients_compare.py` (the cells). Both were committed before either ran. The census will be launched in
  pieces of under two hours, because of the job limit; a resume repeats no row.
- **The import test before this seal** (in a scratch directory, nothing written here): 266 lines and 8 512 points
  enumerated, and the control C1 computed at its one point (already seen in `fine_scan`). It gave max \|Δ log\| = 0.0
  against main's `ratios_at`. No census point was computed.
