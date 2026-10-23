# B1726 — THE TWO INGREDIENTS, REPLICATED (P-293; the completion map's I0): PROVED AS SEALED FOR ITS QUESTION — ON 23 940 POINTS NOBODY HAD COMPUTED, WITH THE MENUS FIXED IN ADVANCE, THE SIX CHARGED-FERMION RATIOS COME OUT SPECIFICALLY AGAIN (R1–R5 HOLD); J AND P-094'S DOUBLE RATIO MISS, AS EXPECTED

**Verdict: PROVED as sealed for its question (R1–R5 hold, R6 and R7 fail as the preregistration expected, C1 holds).**
cc (main), 2026-10-23. Sealed `8024632e1` (sha256 f7f1c28c) before its instruments ran. The outputs were committed unread
at `f1b7eb522` and read once. A structure with two ingredients put in by hand (the lepton factor 3 and the reading rule),
not a value derived. **0 of 19.**

## 1. The result

B1656's four-channel frame at B1667's canonical end, the section ∂R (B1700), on B1713's 266 lines of order 1–12, at
Re τ ∈ {0.05, 0.2, 0.35, 0.55, 0.7, 0.85} and Im τ 2.05–3.45 in steps of 0.1: 23 940 points, 47 880 rows, none computed
before. The covariant readings S and S̃ only (B1724). Main's measure (the worst factor) and main's calibration (B1695's
random hierarchies, B1713's random mixings), each random target getting the same rows and the same menu; each cell is the
mean over 20 seeds (1726–1745), 4 000 targets each.

| cell | prediction | prior | result |
|---|---|---|---|
| **R1** | under the seat's menu, all six ratios within a factor 2 | 80% | **HOLDS**: **1.202** |
| **R2, specific** | seat's menu: mean fraction of random hierarchies as good ≤ 1% | 50% | **HOLDS**: **0.12%** (every seed ≤ 0.28%) |
| **R3, specific** | covariant menu (8 reading assignments × c ∈ {1, 3}): ≤ 1% | 30% | **HOLDS**: **0.41%** (every seed ≤ 0.73%) |
| **R4, specific** | lepton factor continuous: ≤ 1% | 40% | **HOLDS, at the bar**: 0.92% (5 of 20 seeds above 1%) |
| **R5, specific** | the nine (six and ∣V_us∣, ∣V_cb∣, ∣V_ub∣), seat's menu: ≤ 1% | 25% | **HOLDS**: **0.58%** (every seed ≤ 0.75%) |
| **R6, unfitted** | ∣J∣ at the best nine-row within a factor 3 of 3.08 × 10⁻⁵ | 10% | **FAILS**: 3.97 × 10⁻⁶, 7.8 times too small |
| **R7, unfitted** | P-094's D = (m_μ m_d)/(m_s m_e) at the best six-row within 3σ of 10.58 ± 0.11 | 3% | **FAILS**: 11.01 (3.9σ; 4% high) |
| **C1, control** | B1725's census reproduced at its best point to 10⁻⁹; T-covariance to 10⁻⁶ | 97% | **HOLDS**: 3.9 × 10⁻¹², 1.8 × 10⁻¹¹ |

**The best six-row** (seat's and covariant menus alike): τ = 0.55 + 3.05i, the order-10 line (2/5, 1/2), the horocycle
L_max, the split reading (up S̃; down quarks and leptons S), c = 3. Model over measured: m_c/m_t 1.20, m_u/m_t 0.96,
m_s/m_b 1.18, m_d/m_b 1.02, m_μ/m_τ 1.11, m_e/m_τ 0.93. With c free the same row takes c = 2.74 and the leptons fit
within 1.4%.

**The best nine-row:** τ = 0.55 + 2.55i, the order-10 line (2/5, 1/10) (the line of B1725's best point), L_2, S̃ for
every sector, c = 3; worst factor 1.90 (m_c/m_t 1.90, m_u/m_t 1.70, m_d/m_b 1.49; the rest within 17%).

Not a cell: the nine under the covariant menu, 1.66% (every seed above 1%); with c free, 1.23% (19 of 20 above 1%).

## 2. What it means (the reading written before the run, applied)

- **R2 and R3 hold.** The six's specificity replicates on fresh rows and does not depend on the reading choice
  (0.41% with every covariant assignment allowed, against B1725's 0.97% on the seat's rows). As the preregistration
  wrote: the two-ingredient result stands as the frame's first replicated specific contact with the charged-fermion
  hierarchy, a structure with two ingredients put in by hand, graded a **READING** with its tags (Λ, the unit, H-cov, the
  canonical end, the factor 3, the reading). **Deriving the factor (P-294) and the reading (P-295) become the first
  priority.**
- **R5 holds.** Under the seat's menu, masses and mixing meet specifically for the first time in a sealed test (0.58%).
  Under the covariant menu they do not (1.66%), so this part depends on the reading rule.
- **R6, R7 fail, as expected.** The CP phase does not come out (∣J∣ 7.8 times too small at the best nine-row); D at the
  best six-row is 4% high, 3.9σ.
- **Masses and mixing are best at different rows and readings.** The best six-row uses the split reading, where the
  mixing fails (§3 F); the best nine-row uses S̃ throughout, with the six at 1.90.

## 3. After the read (labelled; `verification/posthoc.py`, not covered by the seal)

Run once after the outputs commit; it changes no cell.
- **A, the rows recomputed.** The best six- and nine-rows recomputed at the census module's own precision (mpmath 40
  digits) reproduce every stored key exactly; at 15 digits they agree to 2.3 × 10⁻¹¹.
- **B, breadth: a band, not a spike.** The six (seat's menu) come within 2 at 129 points (132 rows), spread evenly over
  all six Re τ (21–24 rows each) and Im τ 2.55–3.25, **only on lines of order 5 and 10** (57 and 75 rows; 10 distinct
  lines); within 1.5 at 17 points on 4 lines; within 1.3 at 3 points (Im τ 3.05, order 10). The nine come within 2.5 at
  7 points (order 10, L_2, Im τ 2.55–2.75) and within 2 at one.
- **Why orders 5 and 10 (B1728).** On a line of order N the frame sees 6Y mod N; mod 5 it is SU(5)'s five-ality, so on
  order-5 lines Y_e = Y_dᵀ exactly and, with c = 3, the six obey the Georgi–Jarlskog relations m_μ/m_τ = 3 m_s/m_b and
  m_e/m_τ = (m_d/m_b)/3 exactly. Order 10 contains the mod-5 quotient but splits d from e. So the fit lives where the
  frame is SU(5)-like and the factor 3 breaks it as the 45 does.
- **R7's near miss is the line's order.** D scales as c², so D = 9·D_frame. On order-5 lines D_frame = 1 exactly (on
  this census's 1 080 order-5 points down = leptons to 1.6 × 10⁻⁹ with S and 1.9 × 10⁻¹¹ with S̃), so D = 9,
  Georgi–Jarlskog's own value, which P-094 excludes (14σ). On the best six-row's order-10 line D_frame = 1.22, so
  D = 11.0. Nothing was tuned toward D.
- **C, without the factor.** The seat's two readings with c = 1 only: best six 2.28, and 24% of random hierarchies fit as
  well (seed 1726). The factor 3 is what makes the six specific (B1725: 2.34, 14%).
- **D, the neighbours.** Along Im τ at the best six-row's line, Re τ, horocycle and configuration: 2.40 (2.85), 1.52
  (2.95), **1.20** (3.05), 1.65 (3.15), 2.64 (3.25). A smooth valley.
- **E, THE_BAR.** THE_BAR's gate (p < 0.01 after every look the arc made, Bonferroni; the scan's trials are counted by the
  calibration, since every random target gets the same scan): over the arc's four specificity looks, **the six under the
  seat's menu pass (0.0048)**; the six under the covariant menu (0.016), with c free (0.037) and the nine (0.023) do not.
  THE_BAR's PASSED row is written for a state chosen by a fixed rule; here what passes is the population claim (the frame
  with the two ingredients fits the six specifically over the sealed rows and menu), not any row. Not counted by the
  bar's rule, and disclosed: this is the twenty-second sealed test of the frame, and the ingredients were chosen on the
  seat's rows with the data in view (×22 would give 0.026). **Grade: a READING (two hand-put ingredients) whose six-ratio
  specificity passes THE_BAR's gate on its own looks.**
- **F, the mixing at the best six-row.** ∣V_us∣, ∣V_cb∣, ∣V_ub∣ = 0.993, 0.996, 0.060: 4.4, 24 and 16 times the data, a
  near-permutation, as the web seat's readings_blocks found for any split reading (the up and down heavy states on
  different blocks).

## 4. For the seats (a third opinion, mandatory before this positive is banked as more than a reading)

- **Re-run** `verification/compare.py` on the committed `census.jsonl` (sha256 d67432f0…), and recompute a sample of
  rows, including the two best, with your own instrument (the web seat's two_ingredients_census.py is the natural one).
- **Re-derive** R7's mechanism: D_frame = 1 on order-5 lines in both readings (B1728's transpose).
- **Look for what main missed:** any look not counted, any way a random target is treated differently from the data, any
  row whose ratios sit at rounding level.

## Seen first

From the preregistration: `VERDICT topic-sweep /two.ingredient|georgi.jarlskog|replicat|lepton factor|reading rule/ (full
text): 40 of 1497 arcs on main match (NEGATIVE 11, OPEN 3, PROVED 26)`. Bearing on it: B1725 (the census verified, the
menus), B1724 (the readings' covariance), B1712, B1713, B1720, B1723 (the earlier censuses), B1695 (the prior and the 1%
bar), B1698 and B1728 (the order-5 lines), B1667 (the column). **Literature:** Georgi and Jarlskog (1979); Antusch, Hinze
and Saad (P-094's double ratio); out-of-sample replication with the selection counted.

## Disclosed

- Everything in the preregistration's Disclosed.
- **The run's size was misjudged:** the census took 3 h 14 min on 8 workers (the preregistration said about two hours),
  sharing the machine with video work; checkpointed, never restarted.
- **compare.py's first launch did not start:** the shell's change of directory did not hold, so python3 could not open
  the script (exit 2; nothing computed, nothing read). It was relaunched unchanged with absolute paths.
- `census.jsonl` (38.8 MB) is tracked through a one-file `.gitignore` exception (compare.py reads it by name).
- §3 was written after the read; its checks were chosen after seeing which rows were best.

## Files

- `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt` (the instruments relative to this arc; the six inputs relative to the root).
- `verification/census.py` → `census.jsonl`, `control.json`, `census_run.txt`.
- `verification/compare.py` → `comparison.json`, `compare_run.txt`.
- `verification/posthoc.py` (labelled, after the read) → `posthoc.json`, `posthoc_run.txt`.
- The lock: `tests/test_b1726_the_two_ingredients_replicated.py`.
