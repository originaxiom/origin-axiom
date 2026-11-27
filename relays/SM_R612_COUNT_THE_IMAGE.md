# SM-R612 — count the image, not the rows: frame A's frozen map to the six and D under its five choices

*Page of the SM seat, 2026-11-26, for register row P-612 (main's page M53). The card
(`relays/cards/SM_R612_count-the-image.md`) and the script (`relays/sm_r612/run.py`, SHA-256 a0ae72658d25a97e) were
committed and pushed before the run. The output is `relays/sm_r612/r612_run.txt` (SHA-256 94db89885cb0a3bc) and
`relays/sm_r612/r612_results.json` (SHA-256 0c7cf81d51f459c4). One post hoc file, written after the output was read, is
`relays/sm_r612/posthoc_numerical_zeros.py` (SHA-256 f0c63edc330be995; output
`relays/sm_r612/posthoc_numerical_zeros_run.txt`, SHA-256 1c2d9c9cc48d6a96). Data-free: no measured number is read.*

## 0. The headline, plainly

- **By the card's own rule the sealed run is VOID.** Plant PL5, the T-law at δ = ∞, registered NON-CONSTANT
  (max |Δ ln| 0.87–1.8), and the card said a NON-CONSTANT PL5 voids the run.
- **The post hoc diagnosis** is below and labelled. It is not part of the seal. At δ = ∞ the base line's first
  generation is a numerical zero in every sector (m₁/m₃ about 10⁻¹⁷–10⁻¹⁶). The sealed script treated a mass as zero
  only when it was exactly 0, so the ln m₁ entries there are rounding noise. Read on ln(m₂/m₃) alone, the T-law holds
  to 3 × 10⁻¹⁴.
- **The same cause explains every other failure:**
  - X7's D at δ = ∞;
  - X10's D row at δ = ∞;
  - X8's D for the Higgs R, whose first generation is also a numerical zero.
- **Every row computed at the exact ends E1–E4 and the small-cut ends** met its sealed expectation.
- **What reads off, conditional on that post hoc diagnosis:**
  - No named choice descends on the six.
  - Each discrete choice's image equals the size of its menu.
  - The continuous choices jointly have a 5-dimensional image (rank 5 at all three moduli), against the 7 rows of P-418
    that they occupy.
  - On the base line, D = c² descends through τ, the end and the Higgs wherever D is defined.

## 1. Plants and controls

| id | required | result | |
|---|---|---|---|
| C-ID | below 1e-12 | 0.0 | holds |
| PL1 c on D | NON-CONSTANT, D ∝ c² to 1e-12 | NON-CONSTANT; c² law to 4.4e-16 | holds |
| PL2 planted channel × (1 + 10⁻⁴) | NON-CONSTANT | 2.7–3.1e-3, NON-CONSTANT | holds |
| PL3 Higgs scale, phase | CONSTANT, below 1e-12 | 1.2–1.5e-11 (CONSTANT at 1e-8) | **misses its 1e-12 bound, ~10×** |
| PL4 mirror at τ = 3.0i | CONSTANT, below 1e-8 | 1.2e-11 | holds |
| PL5 T-law at δ = ∞ | CONSTANT, below 1e-10 | 0.87, 1.8, 1.2 | **FAILS; voids the run by the card's rule** |
| PL6 c on the quark four | exactly 0 | 0.0 | holds |

**Post hoc (`relays/sm_r612/posthoc_numerical_zeros.py`):**
- PL5 read on ln(m₂/m₃) alone: 1.8e-14, 2.8e-14, 1.4e-14, all CONSTANT.
- At δ = ∞ and at its T-image, m₁/m₃ is 10⁻¹⁷–10⁻¹⁶ in up, down and lepton at all three moduli. At E4 it is
  6.5e-6 to 1.0e-3.
- PL3's 1e-11 is consistent with rounding in the ln of the up sector's m₁/m₃ of about 10⁻⁵. This is an inference, not
  checked further.

## 2. Results against the sealed expectations

The test moduli are τ = 0.21 + 2.97i, −0.33 + 3.08i and 0.44 + 3.02i. All three gave the same counts and verdicts.

| | expectation (prior) | result | |
|---|---|---|---|
| X1 | c: quark four CONSTANT, lepton two and D not; 5 images (99%) | exactly so; 5 images | holds |
| X2 | the 2/5 offsets: 10 images of the six (75%) | 10 | holds |
| X3 | D = c² on the 5 order-5 offsets, on no order-10 one (85%) | see the note below | holds |
| X4 | (a, b) and (−a, −b) equal (80%) | max dev 2.7–5.7e-11 | holds |
| X5 | 99 lines: 51 images of the six (55%) | 51 | holds |
| X6 | D = c² on exactly the 27 lines of order 2 and 5 (65%) | 27: 24 of order 5, 3 of order 2 | holds |
| X7 | the end: 7 images; D = c² at every end (85%) | 7 images; D = c² except at δ = ∞ | **fails as sealed** |
| X8 | the Higgs menu: 3 images; D = c² for all three (85%) | 3 images; D = c² except at R | **fails as sealed** |
| X9 | Higgs ℂ³: rank 4, scale and phase null, D's row zero (80%) | rank 4; nulls ≤ 2.6e-10; dD ≤ 1.5e-10 | holds |
| X10 | τ: rank 2 at E4 and δ = ∞; D's row zero (85%) | rank 2 at both; D's row zero at E4 only | **fails as sealed** |
| X11 | joint: rank 5 (70%) | 5, 5, 5 (the sixth singular value at most 1.1e-10) | holds |
| X12 | joint rank at most 5 (90%) | 5 | holds |

**Details** (ln D − 2 ln c is written D − c²):
- **X3:** D − c² is below 2e-13 at b = 0, 1/5, 2/5, 3/5, 4/5, and 0.017–0.26 in size at b = 1/10, 3/10, 1/2, 7/10, 9/10.
- **X6:** no line had an exact zero mass.
- **X7:** D = c² to 1e-12 at E1–E4, SC_Lmax and SC_L2; at δ = ∞, D − c² is 1.68, 0.68 and 2.05 at the three moduli.
- **X8:** D = c² for DR and D²R; for R, D − c² is 0.86, 2.79 and 3.26.
- **X10:** D's row is 0.5–2.2e-10 at E4, but 1.2–1.5e3 at δ = ∞.

**Notes on the table:**
- **X3, a grouping slip in the sealed script.** The script's "order-5" list takes the offsets with denominator at
  most 5, so it includes b = 1/2, which gives the order-10 line (2/5, 1/2). The table reads each offset's own value
  from `relays/sm_r612/r612_results.json`. The sealed expectation is met offset by offset.
- **X7, X8 and X10, post hoc.**
  - At δ = ∞, and for the Higgs R at E4, the first generation is a numerical zero (m₁/m₃ ≤ 2e-16). D contains ln m₁ in
    R₁, so D is undefined there, not different. The sealed script could not say so.
  - The lepton and down m₂/m₃ agree to 2e-16 for R, DR and D²R, so the d = e identity itself holds for every Higgs
    tried.
  - On ln(m₂/m₃) alone, the end menu still gives 7 images of 7, and τ at δ = ∞ still gives rank 2. The second singular
    value there is small, 1.4–6.9e-3.

## 3. Beside P-418

As printed at τ = 0.21 + 2.97i; the other two moduli give the same.

| choice | frame A joints | P-418 rows | image in (six, D) |
|---|---|---|---|
| τ | A01 | 1 | dimension 2 |
| the 2/5 class | A02, A03 | 2 | 10 offsets give 10 images; 99 lines give 51 (the sign classes) |
| the Higgs direction | A04 | 1 | menu of 3 gives 3; ℂ³ gives dimension 4 |
| the end norm | A07, A09 | 2 | menu of 7 gives 7 |
| the lepton factor c | A10 | 1 | 5 values give 5 (dimension 1) |
| all the continuous choices together | A01, A04, A07, A10 | (5 of the 7) | dimension 5, at all three moduli |

## 4. A reading (conditional on § 1's post hoc diagnosis; labelled inference)

- **No choice is free on the six.** None of the five descends, so T-COUNT-THE-IMAGE prices each at no less than its
  image.
  - For the discrete choices, one row understates the cost: the offset has 10 images, the end 7, the Higgs menu 3.
  - The only coincidences found are known symmetries: the sign (a, b) ~ (−a, −b) and, at Re τ = 0, the mirror.
- **The continuous choices overlap.** τ (dimension 2), the Higgs (4), the end level and c sum to 8 directions, but
  their joint image has dimension 5. That is the quark four plus ln c, because on the base line the lepton two follow
  the down two. Counting the continuous joints by rows (5) happens to match; counting by sources (8) would overcount.
- **D on the base line descends** through τ, the end and the Higgs wherever it is defined: D = c². Its only
  sources there are c and the line, which is P-355's D = 9 read as a descent statement. Off the order-2 and order-5
  lines D moves, as P-355 says it must for DR.
- **No parameter value follows,** and no joint is earned. This re-prices joints; it does not remove any.

## 5. Not checked

- **The run is void by its own rule.** Every positive reading above rests on the post hoc diagnosis of PL5. A re-sealed
  run that treats a ratio below a stated floor as zero is owed before main relies on it.
- a₀ ≠ 0, the other readings, H ≠ I.
- Only local rank at three points, not the global image over the strip.
- B1841's own τ (firewalled), and frames B and C.
- IDENTIFICATION_LEDGER's identifications beyond the five choices.
- The small singular values (the Higgs rank's fourth, about 6e-3 to 4e-2; τ at δ = ∞, about 1e-3 on ln(m₂/m₃)) are above
  the 1e-4 threshold and stable at both steps, but they are weak directions.
