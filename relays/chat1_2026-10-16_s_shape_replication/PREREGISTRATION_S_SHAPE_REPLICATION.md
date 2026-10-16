# THE S-SHAPE REPLICATION ON FRESH THREADS: preregistration (chat1, 2026-10-16)

- **Committed together before the run:**
  - this file;
  - `s_shape_seal.py`;
  - `classes.py` with its run;
  - `enumerate_fresh.py` with its run, and `fresh_configurations.json`;
  - `symmetry_check_on_tlow.py` with its run;
  - `validation/dry_run.py` with its run.
- **Used unchanged from the low-thread seal** (`chat1_2026-10-15_route/twisted_units/`, sealed at 0d83e6981): the
  instrument `tlow2.py`, `null_draws.json`, the received HZ2021 masses and `forms.pkl` (sha256 64a40c03…). The output
  records their sha256 and this file's.
- **One run.** The script runs once, and its output is committed before anyone reads it.
- **The owner's ruling.** At 08:49 on 2026-10-16 the owner accepted chat1's recommendations ("do as u recomend on
  all"), including this replication.
- **Pre-seal review.** A read-only pre-seal review found one blocker and five fixes, all taken (§9).

0 of 19.

## 1. Why, and what this run can and cannot show

- **What it follows.** The low-thread seal (0d83e6981, read at fc15550e0) earned nothing.
  - One read-out, S-shape per-field pooled, had nominal p = 0.03. The SM had 84 passes of 450 configuration-cells,
    against a null mean of 46.6. That is not earned at the sealed 0.05/8.
  - All of the excess was at N = 11.
- **Three exact symmetries make that run's samples smaller than they looked:**
  - the 90 configurations form 26 classes under word reversal with the L ↔ R mirror;
  - the nulls pair up under q → −q, so 199 of them are 111 distinct;
  - in the per-field reading an order's masses obey masses(k·q, line) = masses(q, k·line) for every unit k mod N,
    and each order's closing set is closed under scaling the line. So an assignment's count at order N is constant
    on its orbit q → k·q mod N.

  The evidence is in §4.
- **What this run asks.** Does the SM's pooled excess persist on configurations that seal never saw, with the
  duplicates removed?
- **What it cannot show.**
  - The SM and the nulls are the first run's own, and the claim was chosen from the SM's first-run result.
  - The first run's counts persist across configurations: null counts correlate at r = 0.82 between T-low's two
    N = 11 class orbits, with the SM high in both.
  - So a pass here is not independent of the first run's p = 0.036 (on distinct nulls). However many configurations
    are added, the evidence that the SM is special among eligible assignments is capped by the null's size: 1/113
    pooled.

## 2. The question

Does the per-field thread frame reproduce the Standard Model's ratio-of-log-ratios more often than distinct null
assignments do, on fresh closing configurations?
- The quantity is ρ_s = ln(m₁/m₃) / ln(m₂/m₃) for each sector s.
- The test is W66's predicate as W88 used it.

## 3. Premises

Unchanged from 0d83e6981 unless stated:
- **H-thread, the per-field reading** (main's construction, S134). W92's dressing applies to every unit and Higgs mode;
  R is neutral.
- **The units:** W72's units from `forms.pkl`.
- **The cells:** five, under P4′: C1, C2/E4, C2/ORTH, C3/E4, C3/ORTH.
- **Closure:** c(q_L² + q_R² − q_H²) ≡ 0 mod N. The configuration set uses N² | Q, which closes for every charge.
- **Data:** HZ2021's running masses at M_Z, the received copy unchanged.
- **Changed:**
  - (i) the configurations;
  - (ii) the null, deduplicated;
  - (iii) per-field only and S-shape only;
  - (iv) the 53-bit coefficient check is dropped. It was report-only and read zero.

## 4. What is computed

- **The configurations** (`enumerate_fresh.py`). Lyndon words of length 13 and 14 at height ≤ 3. Lines of exact order
  N ∈ {9, 11, 12}, fixed up to sign, with N² | Q (T-low's rule).
  - That gives 204 + 220 + 112 = 536 configurations, in 51 + 55 + 30 = 136 classes under word reversal with the
    L ↔ R mirror (`classes.py`).
  - One representative per class: the least member in (word, line) order.
  - T-low used length ≤ 12, so no configuration is shared.
- **The null.** null_draws.json has 224 eligible draws (|q| ≤ 18, seed 20261015, eligible on the SM's terms at N = 9,
  11 and 12). Keeping one per pair under q → −q, the first in the fixed order, leaves 112 assignments.
  - They are distinct jointly over the three orders.
  - Per order they fall into 15, 39 and 49 unit orbits. No null shares the SM's orbit at any order: the null file
    excludes every k·SM.
- **The symmetry evidence** (`symmetry_check_on_tlow.py`, on T-low's sealed output, all bitwise):
  - (a) the predicted classes equal T-low's partition by identical masses (26 = 26);
  - (b) all 88 sign pairs are identical;
  - (c) at N = 9, 11 and 12 every unit orbit's members have identical per-field mass multisets over the order's
    configurations.
- **Per class:** the integrals at Npts = 30·P and 37.5·P, with P the period; r_calc is the largest |Δ ln s| between
  the two.
- **Cost.** The dry run took about 32 s per configuration for 113 assignments. With 136 classes, 9 class controls and
  3 sign controls (148 jobs) on two processes, that is about 40 minutes.

## 5. The scoring

- **S-shape**, for each class-cell and assignment:
  - each sector has ρ = ln(s₁/s₃) / ln(s₂/s₃) and z_ρ = ln(ρ/ρ_data) / √(r_calc² + r_ρ² + a²), with a = 0.10;
  - r_ρ = hypot(r_R1/ln R1, r_R2/ln R2) from HZ2021's σ, as in the first seal. It ignores the shared m₃, which moves
    it by at most 5% here;
  - the cell passes iff Σ_s z_ρ² ≤ 7.815.
- **Acceptance**, as in the first seal: three nonzero, distinct singular values in every sector, closure ≤ 10⁻²⁰ and
  r_calc ≤ 10⁻⁶. A failure counts as no pass.
- **Each class-cell counts once.**

## 6. The claim

- **PRIMARY, the only claim: S-shape, per-field, pooled over N = 9, 11 and 12.** The SM's passes over 136 × 5 = 680
  class-cells.
  - p = (1 + #{nulls with passes ≥ the SM's}) / 113.
  - Earned iff the SM passes at least once and p ≤ 0.025.
  - That bar is stricter than 0.05 because the SM and the nulls are the first run's. It needs at most one null at or
    above the SM; T-low had three of the distinct nulls there.
- **Report only:**
  - each order on its own, at the level of assignments and of unit orbits, with p over orbits = (1 + #{orbits ≥
    SM}) / (orbits + 1), and each orbit's spread of counts (must be 0 by the symmetry);
  - the null distribution;
  - the SM's z_ρ per class-cell;
  - a calibration of the pooled claim: each null in turn as "the SM", against the nulls sharing none of its orbits,
    as no null shares the SM's. On T-low, 2.7% of nulls reached p ≤ 0.025 this way.
- **Controls.** If one fails, the run stops and nothing is scored.
  - The first seal's excluded-order controls (closure, r_calc, rotation invariance, the uncarried line's failure) at
    N = 10 and 8, per-field. These run before any N = 9, 11 or 12 integral.
  - **The class control**, after the integrals: for each order, the first class with four members. Each of its other
    three members (the mirror, the reversal, and both) must reproduce the representative's singular values, for
    every assignment and cell, to 10⁻³⁰ of the cell's largest singular value (on 40-digit values).
  - **The sign control:** on that representative, the negatives of the first three nulls must reproduce their values
    to the same tolerance.
- **Errors.** A configuration that errors counts as no pass for anyone.

## 7. Priors (chat1's, stated before the run)

- **PRIMARY earned: 3%.**
  - The first run's excess sat at one order.
  - It needs at most one distinct null at or above the SM; T-low had three.
  - Counted by configuration class, the first run's excess was 9 of 26 (p = 0.305).
- **The excess persists at the first run's level, p ≤ 0.05 but not earned: 35%.**

## 8. What the outcomes would mean

- **PRIMARY earned.** On fresh words of length 13 and 14, the SM's S-shape excess persists, and at most one distinct
  null matches it.
  - That makes it a candidate for the shape of the hierarchy, not for the masses: S-mass failed everywhere in the
    first run.
  - It is not independent evidence that the SM is special. The SM and the nulls are those of the first run (§1).
  - It goes to main as a candidate. The SM seat's blind check comes first.
- **Not earned.** The excess does not reach the bar on fresh words. The first run's nominal p = 0.03 is reported as
  "not replicated on fresh words", and is not carried further.
  - If the pooled p is at or below 0.05 anyway, that is reported as persistence below the bar, not as evidence.
  - Nothing wider is excluded.
- **The per-order read-outs** describe where any excess sits. They carry no claim.

## 9. Seen before this seal (disclosed)

- **The first run's full output**, including S-shape for the SM and every null on T-low. That is why this replication
  exists.
- **A cost test at N = 10:** masses on one length-14 configuration, no score.
- **The dry run** (`validation/dry_run.py`, its run filed), at N = 8 and 10. It ran:
  - the controls;
  - two classes per order;
  - the class control on all three other members of a four-member class;
  - a sign control;
  - the symmetry checks;
  - the scorer, on excluded-order masses relabelled N = 9 and 11. Its numbers mean nothing and are not used.
- **The dry run's first pass failed its class control, and the control was corrected before the seal.**
  - At N = 8 and 10 some nulls have a field ≡ 0 mod N, which gives exact zeros.
  - Those zeros are noise at about 10⁻⁴⁰ of the cell's largest value. Compared relatively, they differed by 0.2% and
    11%.
  - The nonzero values agreed to 1.5 × 10⁻³⁸ (N = 10, diagnosed).
  - The tolerance is now scale-aware: 10⁻³⁰ of the cell's largest value.
  - At N = 9, 11 and 12 no eligible assignment has such a field.
- **The pre-seal review's findings, all taken:**
  - (1) the unit-orbit symmetry, which left an N = 11 claim with 39 distinct outcomes and reachable only through
    duplicates. It was dropped to report-only, with orbit-level p's and the 15/39/49 counts stated;
  - (2) §1 and §8 rewritten for the shared SM and nulls, and for the persistence of counts across configurations;
  - (3) the class control extended from one member to all three, with the scale-aware tolerance;
  - (4) a hard-coded path removed from `classes.py`;
  - (5) the unit-orbit check added to `symmetry_check_on_tlow.py`;
  - (6) the dry run rerun on the final code.
- **Not seen:** any N = 9, 11 or 12 mass on a word of length 13 or 14.

## 10. After the run

1. The output is committed before the read-out: compressed if over 90 MB, with its sha256 recorded.
2. It is scored as sealed, recomputed by an independent referee from this text, and refereed read-only.
3. It is relayed to the SM seat, whose blind check comes before it reads the output, and to main.

chat1. 0 of 19.
