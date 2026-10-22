# B1726 — PREREGISTRATION: THE TWO INGREDIENTS, REPLICATED (P-293) — on 23 940 points nobody has computed, with the choice of ingredients counted and the covariant readings only, do the six charged-fermion ratios come out specifically again?

cc (main), 2026-10-22, after B1724 and B1725. **Sealed before `verification/census.py` and `verification/compare.py`
run.** A test of a structure with two ingredients put in by hand, not a value derived. 0 of 19.

## Why

B1725 verified the web seat's sealed census on main's frame. With the Georgi–Jarlskog factor 3 on the leptons and a
fixed reading rule, the six ratios came within 1.27, and with the choice of ingredients counted the fit was specific
under the seat's own menu (0.29% of random hierarchies as good, over 20 seeds). It sat at the bar when every covariant
reading assignment was allowed (0.97%). But the ingredients were chosen with the data in view, and the census's rows
neighbour rows where they were chosen. **The question is whether the specificity replicates on rows nobody has computed,
with the menus fixed in advance.**

## The model (no data)

- **The frame,** as B1712–B1725: B1656's four-channel coupling, the section ∂R (B1700), B1667's canonical end at both
  horocycles with L read at Im τ from its Re τ = ¼ column.
- **The rows.** B1713's 266 lines of order 1–12 up to sign, at Re τ ∈ {0.05, 0.2, 0.35, 0.55, 0.7, 0.85} and
  Im τ ∈ {2.05, 2.15, …, 3.45}: **23 940 points, 47 880 rows.** No point of this grid has been computed by anyone: every
  earlier census used Re τ ∈ {0, 0.1, ¼, 0.4, ½} and Im τ on the tenths. The grid spans the strip 0 ≤ Re τ < 1, which
  suffices because the readings used are SL(2, ℤ)-covariant (B1724).
- **The readings:** S and S̃ only (B1724: S* is covariant only under Γ⁰(2)). Every sector in both, and the CKM
  (V = U_u^H U_d, ascending mass) for each (up, down) pair.
- **The ingredients, as menus fixed now.** The lepton factor c multiplies m_μ/m_τ and divides m_e/m_τ.
  - **seat:** {(S̃, S, S), (S̃, S̃, S̃)} × c ∈ {1, 3}: the four configurations the web seat compared;
  - **cov:** every (up, down, lepton) assignment of S or S̃ (8) × c ∈ {1, 3};
  - **free:** the seat's two reading rules with c continuous (only m_μm_e/m_τ² is constrained).
- **The measure and the calibration are main's:** the worst factor max∣ln(model/target)∣, minimised over the rows and the
  menu; B1695's random hierarchies and B1713's random mixings. A random target fits as well if its own best over the same
  rows and the same menu is at most the data's. **Each cell uses the mean over 20 seeds, 1726–1745,** 4 000 six-targets
  and 4 000 nine-targets each.

## Cells

| cell | prediction | prior |
|---|---|---|
| **R1** | under the seat's menu, the best row puts all six ratios within a factor 2 | 80% |
| **R2, specific** | under the seat's menu, the mean fraction of random hierarchies as good is at most 1% | 50% |
| **R3, specific** | under the covariant menu, the same, at most 1% | 30% |
| **R4, specific** | with the lepton factor free, the same, at most 1% | 40% |
| **R5, specific** | the nine (six and ∣V_us∣, ∣V_cb∣, ∣V_ub∣) under the seat's menu: the mean fraction of random nine-target sets as good is at most 1% | 25% |
| **R6, unfitted** | at the best nine-row (seat's menu), ∣J∣ within a factor 3 of PDG's 3.08 × 10⁻⁵ | 10% |
| **R7, unfitted** | at the best six-row (seat's menu), P-094's double ratio (m_μm_d)/(m_s m_e) within 3σ of 10.58 ± 0.11 | 3% |
| **C1, control** | (i) the instrument reproduces B1725's verified census at its best point (0.4 + 2.7i, line (2/5, 1/10)) on every shared key to 10⁻⁹ in log; (ii) both readings T-covariant at 0.35 + 2.75i on two lines, to 10⁻⁶ | 97% |

Read-outs: the best six and nine rows under each menu (line, τ, horocycle, readings, factor, D, J); the per-seed
fractions.

**The reading, written before the run.**
- **R2 and R3 hold:** the six's specificity replicates on fresh rows and does not depend on the reading choice. The
  two-ingredient result stands as the frame's first replicated specific contact with the charged-fermion hierarchy: a
  structure with two ingredients put in by hand, graded a READING with its tags (Λ, the unit, H-cov, the canonical end,
  the factor 3, the reading). Deriving the factor (P-294) and the reading (P-295) become the first priority.
- **R2 holds, R3 fails:** it replicates only under the seat's reading rules, as B1725 found on the seat's rows. The
  result then stands or falls with a derived reading rule (P-295).
- **R2 fails:** the specificity does not replicate on fresh rows. The earlier fractions owed to the rows, and the
  candidate drops to "near the bar", like B1720's threads.
- **R5:** if it holds, masses and mixing meet specifically for the first time.
- **R6, R7:** unfitted observables. If either holds it is the strongest evidence on record; both are expected to fail
  (the seat's census: J 16–40 times too small, D 8.7–15.5).
- **C1 failing** stops the reading: the cells are then not read as a replication.

## Seen first

`VERDICT topic-sweep /two.ingredient|georgi.jarlskog|replicat|lepton factor|reading rule/ (full text): 40 of 1497 arcs on main match (NEGATIVE 11, OPEN 3, PROVED 26)`.
Most matches use "replicate" in other senses (gauge-group replication, reader-panel replication). Bearing on it:
- B1725 (the web seat's sealed census verified on main; the menus' fractions; the region this grid avoids);
- B1724 (the readings' covariance: S and S̃ covariant, S* only under Γ⁰(2); why S* is excluded here);
- B1712, B1713, B1720, B1723 (the frame's earlier censuses, their grids, and the calibrations this one reuses);
- B1695 (the random-hierarchy prior and the 1% bar); B1698 (the order-5 lines, where down = leptons, P-296);
- B1667 (the canonical end, the L column read here).

None tests the two-ingredient result on points outside the seat's rows, or with the menus counted in advance.
**Literature:** Georgi and Jarlskog (1979), the factor 3 on the leptons from a 45 of SU(5); Antusch, Hinze and Saad
(P-094's double ratio, scale-independent at one loop); out-of-sample replication with the selection counted is standard.

## Disclosed

- **Known before the seal:** B1725 in full (the census reproduced; the menus' fractions over 21 seeds; the best region
  Re τ 0.4–½, Im τ ≈ 2.7, order-10 lines, the second horocycle); the web seat's selection map and its read-outs (J, D);
  B1724 (the readings' covariance; S* excluded here).
- **The grid** was chosen to avoid every computed Re τ and Im τ and to span the strip; it was not chosen by any result.
- **Expected directions, stated before the run:** R1 likely; R2 about even; R3 below even (B1725: at the bar); R5, R6 and
  R7 likely to fail.
- **J's target** is PDG's CKM review value, an external constant written here; the record pins no J.
- **The trial count.** This is the twenty-second sealed test of this frame against data (the SM seat's ledger counts
  B1720 and B1722 as the nineteenth and twentieth, B1723 the twenty-first). Its cells are averaged over 20 seeds to
  remove seed luck; the program's history of choices is not counted, and cannot be.
- **The run's size:** about two hours on 8 workers for the census, checkpointed; the calibration about 20 minutes.
- The instruments were import-tested before the seal; importing them computes nothing.

## Instruments

- `verification/census.py` (no data) → `census.jsonl`, `control.json`.
- `verification/compare.py` → `comparison.json`.
- The hashes are in `ARTIFACT_HASHES.txt`: the two instruments, and the six files they read in place (B1723's
  `b1656_funcs.py`, B1691's `the_exponents.py`, B1667's column, B1725's received census, the masses and the CKM data).
