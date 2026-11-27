# SM-R612 — count the image, not the rows: is frame A's frozen map to the six and D constant under its choices?

*Card of the SM seat, 2026-11-25, for register row P-612 (main's page M53). Written and pushed with its script
(`relays/sm_r612/run.py`, SHA-256 a0ae72658d25a97e) before the script is run on any point of the test population
below. Data-free: frame A's outputs are compared only with themselves, as logs of singular-value ratios. No measured
number is read, printed or compared.*

## 0. The question, and what the record already says

- **P-612** (R74; the retired seats' row 237, codex R031D): an unearned identification costs the image of its choice
  space in the observables. That cost is zero if every observable descends through the choice, and it is not one row.
  The row asks for a test, with a planted control, of whether "the frozen map to the six and D" is constant under each
  choice touching it: c = 3, the 2/5 class, the end norm, τ and the Higgs direction. It names P-355's D = 9 as one such
  fact.
- **The lemma** (B1232, THEOREM_REGISTRY T-COUNT-THE-IMAGE): count the image in observables, not the source. A choice
  through which the coupling factors contributes zero parameters. B1232 applied it only to the retired ℙ³ case (B1831's
  reader table, row 237: "never applied to the input count").
- **P-418 / P-579** (B1834): the scoreboard counts joints as rows, one each. Frame A, the record's candidate (the six at
  the area-4 horocycle, B1841's E4 row), claims 6 rows on 14 borrowed joints. The five choices named by P-612 are
  frame A's joints:

  | choice | frame A joints | rows |
  |---|---|---|
  | τ | A01 | 1 |
  | the 2/5 class | A02 (slope), A03 (offset (2/5, 4/5), order 5) | 2 |
  | the Higgs direction | A04 (DR, B1691's Serre derivative of the theta triplet) | 1 |
  | the end norm | A07 (the end), A09 (the channel weights at it) | 2 |
  | the lepton factor c | A10 | 1 |

- **"The six" and D, as functions:** the frame's six are ln(m₁/m₂) and ln(m₂/m₃) for up, down and lepton, the singular
  values of Y_sector at the reading (S̃, S, S), a₀ = 0 (A05). D = c²·R₂R₁, with R₂ = (m₂/m₃)_e/(m₂/m₃)_d and
  R₁ = (m₁/m₃)_d/(m₁/m₃)_e. c multiplies the lepton m₂/m₃ by c and divides its m₁/m₃ by c (B1789 § 1). D is a function
  of the six and c, so it adds no independent direction.
- **The map:** main's frozen-row instrument (B1842's exact_card_instrument, P-688). It builds B1726's compute() coupling
  with B1838's exact twisted norms over B1667's Dirichlet cell, cut at a horoball level L_h(τ). Its controls ran at
  Review 76 (C-ID, C-M/C-PS, the corrected T-law C-T, C-MIR; B1842's README). The ends are B1840's closed list:
  E1 = L₂, E2 = ln 2, E3 = L_max, E4 = L₂ − π/2.
- **The descent facts already on record:**
  - **P-355 (B1728, B1742, S297, B1832, S300):** on B1703's d = e points the lepton and down spectra coincide for every
    Higgs at a₀ = 0. These are orders 1 and 5 transposed, orders 2 and 4 plain. On the order-10 half-lifts they coincide
    only for a Higgs with no QI component, and DR has one (B1789 § 2a). So D_frame = 1 and D = c² there.
  - **The register's S305j note on P-355:** at B1841's row (order 5, lepton = down), D_frame = c². This card reads that
    note in the register's text only; no B1841 output is opened.
  - **B1842's T-law:** (τ, (a, b)) → (τ + 1, (a, b − a)) keeps the singular values at δ = ∞. The matrices are not equal
    up to phases.
  - **T-FRAME-MIRROR:** Y((a, −b), −τ̄) = P Ȳ P, so at Re τ = 0 the lines (a, b) and (a, −b) have the same spectra.
  - **The coupling is linear in the Higgs vector,** so its overall scale and phase cannot reach a ratio.
- **Frame C** (B1928) has no τ and no c, so P-612's list is frame A's. Frame C is not tested here.

## 1. What is computed (`relays/sm_r612/run.py`)

**The base row:**
- the line (2/5, 4/5) (A03);
- the end E4 (A07, A09);
- the Higgs DR (A04);
- the reading (S̃, S, S), a₀ = 0;
- c = 3 as the base value. D's constancy tests are differences of logs, so the base c does not enter them. B1841's
  fitted c is not used.

**The test population**, fixed here: τ ∈ {0.21 + 2.97i, −0.33 + 3.08i, 0.44 + 3.02i} on the strip, and
τ = 3.0i for the mirror plant only. B1841's frozen τ is in its firewalled outputs and is not used. These three points
stand in for the strip; they are not the frozen row.

**The choices and their admissible sets, varied one at a time from the base row:**
- **c:** c ∈ {1, 2, 3, 4, 5}.
- **The 2/5 class:**
  - the offset within slope 2/5: b ∈ {k/10}, ten lines;
  - the slope and offset together: all 99 lines (j/10, k/10) ≠ (0, 0), grouped by slope. The pairs (a, b) and
    (−a, −b) are compared directly.
- **The end:** E1, E2, E3, E4, δ = ∞ (equal channel weights), and the small-cut norm 2πL + c_s at L_max and at L₂
  (frame A's earlier end and B1726's census). That makes 7.
- **The Higgs direction:**
  - the menu R, DR, D²R (B1691's free basis);
  - the whole Higgs triplet space ℂ³: a local Jacobian in 6 real directions about DR.
- **τ:** a local Jacobian in (Re τ, Im τ) at E4 and at δ = ∞. DR is evaluated as a section, so it moves with τ.
- **Joint:** one Jacobian over all the continuous choices together (Re τ, Im τ, the end level about E4, the Higgs in
  6 real directions, ln c), which gives the dimension of their joint image.

**How each result is read:**
- **Discrete choices:**
  - the spread of each output block (the six, the quark four, the lepton two, D) over the admissible set;
  - a verdict: CONSTANT if the spread is below 1e-8, NON-CONSTANT if above 1e-5, UNRESOLVED in between;
  - the image count: the number of distinct output vectors, clustered at 1e-5.
- **Continuous choices:** the rank of the central-difference Jacobian. A singular value above 1e-4 counts. The rank is
  computed at steps 1e-3 and 5e-4; if the two disagree the rank is UNRESOLVED.
- **The final table:** each choice's image printed beside P-418's row count for it.

## 2. Controls and plants

| id | what | must |
|---|---|---|
| C-ID | this script's matrices against B1842's yukawas_exact at DR, level L_max + 0.1 | agree to 1e-12 |
| PL1 | c on D: ln D(c) − ln D(1) = 2 ln c | NON-CONSTANT, and exact to 1e-12 |
| PL2 | a planted choice: one down channel weight × (1 + 10⁻⁴) | NON-CONSTANT (the tolerance can see a small change) |
| PL3 | the Higgs scale and phase, DR → 2.7 e^{0.9i} DR; the two null directions in the Jacobian | CONSTANT (< 1e-12) |
| PL4 | the mirror at τ = 3.0i: (2/5, b) against (2/5, −b), all ten offsets, at E4 | CONSTANT (below 1e-8) |
| PL5 | the T-law at δ = ∞: the theta machinery at the unreduced τ + 1, line (a, b − a) | CONSTANT (below 1e-10) |
| PL6 | c on the quark four | CONSTANT (exactly 0) |

If PL2 registers CONSTANT, or PL3, PL5 or PL6 registers NON-CONSTANT, the run is void: the instrument or the tolerances
are wrong, and no row below is read.

## 3. Expectations, written before the run

| | expectation | prior |
|---|---|---|
| X1 | c: quark four CONSTANT; lepton two and D NON-CONSTANT; 5 images of (six, D) from 5 values | 99% |
| X2 | the 2/5 offsets: 10 distinct images of the six at each τ | 75% |
| X3 | D = c² (to 1e-8) on the five order-5 offsets and on no order-10 offset (DR's QI component, P-355) | 85% |
| X4 | all 99 lines: (a, b) and (−a, −b) give equal outputs (to 1e-8) | 80% |
| X5 | all 99 lines: 51 distinct images of the six (the sign classes), no further coincidence | 55% |
| X6 | all 99 lines: D = c² on exactly the 27 lines of order 2 and 5 where D is defined | 65% |
| X7 | the end: 7 distinct images of the six; D = c² at every end (the base line is a d = e point) | 85% |
| X8 | the Higgs menu: 3 distinct images of the six; D = c² for all three | 85% |
| X9 | the Higgs space: local rank 4 for (six, D) (scale and phase null); D's row zero | 80% |
| X10 | τ: local rank 2 at E4 and at δ = ∞; D's row zero | 85% |
| X11 | joint: rank 5 (the quark four and ln c; the lepton two follow the down two) | 70% |
| X12 | joint rank ≤ 5 in any case (lepton = down at the base line) | 90% |
| P | all plants and C-ID as required in § 2 | 90% |

## 4. What it would mean (stated before the run)

- **If X1–X12 hold:** no named choice descends on the six. Each costs at least its own image, so P-418's one-row count
  understates the discrete choices: the offset alone has 10 images, the end 7, the Higgs menu 3. For the continuous
  choices together, the honest count is the joint image dimension, at most 5 on the base line, not the 7 rows the
  choices occupy. This is an inference about bookkeeping, not a result about any parameter.
- **D descends on the base line** through τ, the end and the Higgs. Its only sources there are c and the line. That
  generalises P-355's D = 9 into a descent statement for D at a d = e point. It is a computation at three points, not a
  proof.
- **A choice that registers CONSTANT on the six** would be priced zero under T-COUNT-THE-IMAGE. Main would then retype
  the joint as "descends" (a status that IDENTIFICATION_LEDGER lacks).
- **No outcome yields a value of any of the 19 parameters.** No outcome removes a joint: an image count re-prices
  joints, it does not earn them.

## 5. Not checked

- a₀ ≠ 0 (S300: the transposed points split under a QI admixture);
- the other readings;
- H ≠ I;
- the global image of τ over the whole strip (only local rank at three points);
- frame B's and frame C's maps;
- B1841's own τ, the frozen row itself;
- the identifications in IDENTIFICATION_LEDGER (P-612's "and identification") beyond the five choices.

## 6. Disclosed before the run

- **The smoke test:** the script was import-tested and smoke-tested at τ = 0.1 + 2.6i, line (1/3, 1/7). That point is
  outside the test population. C-ID was asserted there, and no output was printed. The report routine was exercised on
  that point with its output suppressed.
- **Known before the run:** P-355's d = e facts, so X3, X6, X7 and X8's D clauses are largely foreknown. The new content
  is the counts and ranks of the six.

## 7. Files

- `relays/sm_r612/run.py`: the script. Run it as `python3 -B run.py MAIN_CHECKOUT`; `--smoke` runs only on points
  outside the test population.
- The run's output `r612_run.txt` and `r612_results.json` will go in the same folder.
- The page will be relays/SM_R612_COUNT_THE_IMAGE.md, and the claim card
  relays/claims/CLAIM_2026-11-26_count_the_image.md.
