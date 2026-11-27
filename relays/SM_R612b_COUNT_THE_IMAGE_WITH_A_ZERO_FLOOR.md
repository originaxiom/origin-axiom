# SM-R612b — count the image, re-sealed with a zero floor: the run holds and confirms SM-R612's post hoc reading

*Page of the SM seat, 2026-11-26, for register row P-612 (main's page M53).*

- **Card:** `relays/cards/SM_R612b_count-the-image-with-a-zero-floor.md`, sealed and pushed before the run.
- **Script:** `relays/sm_r612b/run.py`, SHA-256 0d0edb642ce9dcbb.
- **Output:** `relays/sm_r612b/r612b_run.txt` (SHA-256 4fc024f64d7b32f4) and `relays/sm_r612b/r612b_results.json`
  (SHA-256 818985ccd5cf839e).
- **No post hoc file.** Data-free: no measured number is read.

## 0. The headline

- **The run is not void.** Every plant and control is inside its sealed bound. In particular PL5, the T-law that voided
  SM-R612, holds to 1.4–2.8 × 10⁻¹⁴ on its defined outputs, with the same pattern of undefined outputs on both sides.
- **All twelve expectations X1–X12 hold** at all three moduli (0.21 + 2.97i, −0.33 + 3.08i, 0.44 + 3.02i).
- **This confirms, under a sealed rule, the reading SM-R612 could give only post hoc.** The rule is a ratio m_i/m_3
  below 10⁻¹² counts as a zero. The void run's results were known when this card's priors were set, so this is a
  confirmation of a known reading, not independent evidence.

## 1. Plants and controls (void conditions applied)

| id | sealed bound | result | |
|---|---|---|---|
| C-ID | below 1e-12 | 0.0 | holds |
| PL1 c on D | NON-CONSTANT; D ∝ c² to 1e-12 | NON-CONSTANT; 4.4e-16 | holds |
| PL2 channel × (1 + 10⁻⁴) | NON-CONSTANT | 2.7–3.1e-3 | holds |
| PL3 Higgs scale and phase | below 1e-9 | 1.2–1.5e-11 | holds |
| PL4 mirror at τ = 3.0i | below 1e-8 | 1.2e-11 | holds |
| PL5 T-law at δ = ∞ | defined outputs below 1e-10, same undefined pattern | 1.8e-14, 2.8e-14, 1.4e-14 | holds |
| PL6 c on the quark four | exactly 0 | 0.0 | holds |

- **What PL5 compared.** Its defined outputs are the three ln(m₂/m₃). ln(m₁/m₂) in every sector and ln D are UNDEFINED
  on both sides, because the first generation is a zero at δ = ∞.
- **None of the void conditions occurred:** PL2 is non-constant; PL3, PL5 and PL6 are within their bounds; PL5 has
  defined outputs.

## 2. Results against the sealed expectations (identical at all three moduli)

| | expectation (prior) | result | |
|---|---|---|---|
| X1 | c: quark four CONSTANT; lepton two, D not; 5 images (99%) | so; 5 images | holds |
| X2 | 2/5 offsets: 10 images of the six (95%) | 10 | holds |
| X3 | D = c² at b = 0, 1/5, 2/5, 3/5, 4/5; not at the order-10 five (95%) | see the note below | holds |
| X4 | (a, b) and (−a, −b) equal to 1e-8 (95%) | max dev 2.7–5.7e-11 | holds |
| X5 | 99 lines: 51 images of the six (85%) | 51 | holds |
| X6 | D = c² on exactly the 27 lines of order 2 and 5 (70%) | 27; no line undefined | holds |
| X7 | ends: 7 images; D = c² at six ends, UNDEFINED at δ = ∞ (90%) | so | holds |
| X8 | Higgs menu: 3 images; D = c² for DR, D²R, UNDEFINED for R (90%) | so | holds |
| X9 | Higgs ℂ³: rank 4, scale and phase null, D's row zero (90%) | rank 4 | holds |
| X10 | τ: rank 2 at E4, D's row zero; rank 2 at δ = ∞ on defined rows (85%) | so | holds |
| X11 | joint: rank 5 (95%) | 5, 5, 5 | holds |
| X12 | joint rank at most 5 (95%) | 5 | holds |

**Notes on the table** (ln D − 2 ln c is written D − c²):
- **X3.** D − c² is at most 1.9e-13 in size at b = 0, 1/5, 2/5, 3/5, 4/5. At b = 1/10, 3/10, 1/2, 7/10 and 9/10 it is
  0.017–0.26 in size.
- **X7.** D − c² is at most 2.2e-13 in size at E1–E4, SC_Lmax and SC_L2, and UNDEFINED at δ = ∞. The printed
  "D NON-CONSTANT, 2 images" for the end menu is that split: c² at six ends, and undefined at one. By the card's rule, a
  value defined in some members and undefined in others counts as different.
- **X8.** D − c² is at most 1.4e-13 for DR and D²R, and UNDEFINED for R. The printed "D NON-CONSTANT, 2" is the same
  split as for the ends.
- **X9.** The four singular values above the threshold include a weak fourth (5.8e-3 to 3.6e-2). The two null directions
  are at most 2.6e-10 at step h/2, and the finite-difference check on scale and phase gives 0.5–2.2e-11. D's row is at
  most 1.5e-10.
- **X10.**
  - At E4 the singular values are 1.2–6.3 and D's row is at most 2.2e-10.
  - At δ = ∞, the rows ln u12, ln d12, ln e12 and ln D are dropped as undefined, and the rest have rank 2. The second
    singular value is weak there: 1.4–6.9e-3.
- **X11.** The sixth singular value is at most 1.1e-10.

## 3. Beside P-418

| choice | frame A joints | P-418 rows | image in (six, D) |
|---|---|---|---|
| τ | A01 | 1 | dimension 2 |
| the 2/5 class | A02, A03 | 2 | 10 offsets give 10 images; 99 lines give 51 (the sign classes) |
| the Higgs direction | A04 | 1 | menu of 3 gives 3; ℂ³ gives dimension 4 |
| the end norm | A07, A09 | 2 | menu of 7 gives 7 |
| the lepton factor c | A10 | 1 | 5 values give 5 (dimension 1) |
| the continuous choices together | A01, A04, A07, A10 | 5 of the 7 | dimension 5 |

## 4. A reading (inference, labelled)

- **No named choice descends on the six.** T-COUNT-THE-IMAGE prices each at no less than its image.
  - Each discrete menu's image is its full size. The only coincidences are the sign pair and, at Re τ = 0, the mirror.
  - One row per discrete choice therefore understates the cost.
- **The continuous choices overlap.** Their joint image has dimension 5: the quark four, plus ln c, because on the base
  line the lepton two follow the down two. That is fewer than their 8 source directions.
- **D descends on the base line.** D = c² holds through τ, every end and every Higgs at which D is defined. Its only
  sources there are c and the line. This is P-355's D = 9 read as a descent fact, computed at three moduli, not proved.
- **No parameter value follows, and no joint is earned.** This re-prices joints; it does not remove any.

## 5. Not checked

- a₀ ≠ 0, the other readings, H ≠ I;
- local rank only, at three moduli (not the global image over the strip);
- B1841's own τ;
- frames B and C;
- IDENTIFICATION_LEDGER's identifications.
