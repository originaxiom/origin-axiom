# SM-R612b — count the image, re-sealed with a zero floor

*Card of the SM seat, 2026-11-26, for register row P-612 (main's page M53). This is the owed re-sealed run of SM-R612.
Its script, `relays/sm_r612b/run.py` (SHA-256 0d0edb642ce9dcbb), is written with this card before it runs on any point
of the test population. Data-free: frame A's outputs are compared only with themselves. No measured number is read.*

## 0. Why a second run

- **The first run was void by its own rule.** SM-R612 (`relays/SM_R612_COUNT_THE_IMAGE.md`) ran
  `relays/sm_r612/run.py` (SHA-256 a0ae72658d25a97e). Its plant PL5, the T-law at δ = ∞, registered NON-CONSTANT
  (0.87–1.8), and the card said that voids the run.
- **The post hoc diagnosis** (`relays/sm_r612/posthoc_numerical_zeros.py`) found the cause:
  - At δ = ∞, and for the Higgs R at E4, the first generation of the base line is a numerical zero: m₁/m₃ is
    10⁻¹⁸–10⁻¹⁶, against 6.5 × 10⁻⁶–10⁻³ elsewhere.
  - The sealed script treated a mass as zero only when it was exactly 0, so it took logs of rounding noise.
  - That one cause also produced the sealed failures of X7, X8 and X10.
- **Everything the void run showed is now known**, and the priors below are set with it in view. This run confirms
  under a stated rule; it adds no new evidence beyond that.

## 1. What changes, and nothing else

`relays/sm_r612b/run.py` is a copy of the sealed script with only these changes:

1. **The zero floor.**
   - A ratio m₂/m₃ or m₁/m₃ below ZERO_FLOOR = 10⁻¹² counts as a zero. The floor is fixed from the instrument's double
     precision: the noise sits at about 10⁻¹⁶ of the heaviest mass, and the smallest genuine ratio in the void run was
     6.5 × 10⁻⁶.
   - Any log that involves a zero is UNDEFINED (NaN). That covers ln(m₁/m₂) and ln(m₂/m₃), and D, which needs both
     m₂/m₃ and m₁/m₃ of down and lepton.
   - An undefined quantity is excluded from spreads and from Jacobians: a row undefined at any evaluation is dropped,
     and the dropped rows are printed.
   - Two outputs differ (deviation ∞) if one is defined and the other is not. This applies to the image counts, the
     sign pairs and the plants.
   - A block whose every entry is undefined gets the verdict UNDEFINED.
2. **The order-5 offsets** of slope 2/5 are b ∈ {0, 1/5, 2/5, 3/5, 4/5}. b = 1/2 moves to the order-10 group, which
   corrects SM-R612's grouping slip.
3. **PL3's bound** is stated realistically as 10⁻⁹. The void run gave 1.2–1.5 × 10⁻¹¹, which missed the 10⁻¹² written
   then.
4. **The outputs** go to `relays/sm_r612b/` as r612b_run.txt and r612b_results.json.

**Unchanged:**
- the instrument (B1842's frozen-row instrument, used unchanged);
- the base row: line (2/5, 4/5), end E4, Higgs DR, reading (S̃, S, S), a₀ = 0, c = 3;
- the test moduli τ = 0.21 + 2.97i, −0.33 + 3.08i and 0.44 + 3.02i, with 3.0i for the mirror;
- the menus;
- the tolerances: CONSTANT below 1e-8, NON-CONSTANT above 1e-5, clustering at 1e-5, rank threshold 1e-4, steps 1e-3
  and 5e-4.

The first card's § 0–1 describe the question and the design, which still apply
(`relays/cards/SM_R612_count-the-image.md`).

## 2. Controls and plants (priors set after the void run)

| id | must | void run showed | prior |
|---|---|---|---|
| C-ID | matrices equal B1842's to 1e-12 | 0.0 | 99% |
| PL1 | c on D: NON-CONSTANT, D ∝ c² to 1e-12 | 4.4e-16 | 99% |
| PL2 | planted channel × (1 + 10⁻⁴): NON-CONSTANT | 2.7–3.1e-3 | 99% |
| PL3 | Higgs scale and phase: below 1e-9 | 1.2–1.5e-11 | 95% |
| PL4 | mirror at τ = 3.0i: below 1e-8 | 1.2e-11 | 95% |
| PL5 | T-law at δ = ∞: defined outputs below 1e-10, same undefined pattern | 1.4–2.8e-14 on ln m₂/m₃ (post hoc) | 90% |
| PL6 | c on the quark four: exactly 0 | 0.0 | 99% |

**The run is void** if any of these happens:
- PL2 is not NON-CONSTANT;
- PL3, PL5 or PL6 exceeds its bound;
- PL5 has no defined output.

## 3. Expectations, restated before the run

| | expectation | void run (as sealed, or post hoc where marked) | prior |
|---|---|---|---|
| X1 | c: quark four CONSTANT; lepton two and D NON-CONSTANT; 5 images | held | 99% |
| X2 | the ten 2/5 offsets: 10 images of the six | held | 95% |
| X3 | D = c² (1e-8) at b = 0, 1/5, 2/5, 3/5, 4/5; not at 1/10, 3/10, 1/2, 7/10, 9/10 | held offset by offset | 95% |
| X4 | (a, b) and (−a, −b) give equal outputs (to 1e-8) | held | 95% |
| X5 | 99 lines: 51 images of the six | held | 85% |
| X6 | 99 lines: D = c² on exactly the 27 lines of order 2 and 5 | held under the exact-zero rule | 70% |
| X7 | the end: 7 images; D = c² at E1–E4, SC_Lmax, SC_L2; UNDEFINED at δ = ∞ | noise at δ = ∞ (post hoc) | 90% |
| X8 | the Higgs menu: 3 images; D = c² for DR and D²R; D UNDEFINED for R | D at R was noise (post hoc) | 90% |
| X9 | Higgs ℂ³: rank 4 (scale and phase null); D's row zero | held | 90% |
| X10 | τ: rank 2 at E4, D's row zero; rank 2 at δ = ∞ on defined rows | held at E4; 2 at δ = ∞ (post hoc) | 85% |
| X11 | joint (10 continuous parameters): rank 5 | 5 at all three moduli | 95% |
| X12 | joint rank at most 5 | held | 95% |

**Notes:**
- **X6:** the floor may make some order-2 or other lines' D undefined where the void run took noise for a mass. If so,
  this count falls, and the run prints the undefined lines.
- **X10 at δ = ∞:** the rows ln(m₁/m₂) of all three sectors and D are expected to be dropped as undefined.

## 4. What it would mean

- **The reading.** If the plants hold and X1–X12 hold, SM-R612's reading stands on a sealed run instead of a post hoc
  one. Each discrete choice has an image the size of its menu (offset 10, ends 7, Higgs 3, c 5), and the continuous
  choices' joint image has dimension 5. D = c² descends through τ, the end and the Higgs on the base line wherever it is
  defined. These are re-pricings of joints; none is earned, and no parameter value follows.
- **If an expectation fails** under the floor, it is reported plainly, with no further post hoc repair in this card's
  run.

## 5. Not checked

As in SM-R612:
- a₀ ≠ 0, the other readings, H ≠ I;
- only local rank at three moduli;
- B1841's own τ;
- frames B and C;
- IDENTIFICATION_LEDGER's identifications.

## 6. Disclosed

- The script was smoke-tested only at τ = 0.1 + 2.6i, line (1/3, 1/7), outside the test population, with no output
  printed.
- The new NaN logic was unit-checked on synthetic vectors.
- The run will be `python3 -B run.py MAIN_CHECKOUT > r612b_run.txt` in `relays/sm_r612b/`.
