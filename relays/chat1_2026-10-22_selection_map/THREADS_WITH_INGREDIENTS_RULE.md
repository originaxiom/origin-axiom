# The thread fixes the point, with the two law ingredients: B1720's census re-read under one Higgs reading and the Georgi–Jarlskog Clebsch

chat1, 2026-10-22. **Sealed before `threads_with_ingredients.py` runs, and before chat1 has read any result of the
two-ingredients census** (`TWO_INGREDIENTS_RULE.md`; its run is in progress at this commit). A test of a structure on
main's frame, with main's instrument imported unchanged. No value is derived. 0 of 19.

## Why

- **The owner's question** is a selection principle that decides most of the nineteen.
- **What the record has tried.** Main's B1720 put τ at each thread's apex, with the lines its monodromy fixes, so no
  continuous number was free. It came within a factor 1.80 on the six ratios and was not specific (1.65% of random
  hierarchies fit as well, against a 1% bar). B1722 found that the record's measures do not single out the best threads.
- **What chat1 found since** (post hoc, `GJ_FINDINGS.md`). The frame's mass ceiling is the missing Georgi–Jarlskog
  factor, and its mixing fails because the up and down sectors read the Higgs differently.
- **The question here.** With both law ingredients fixed in advance, does the thread select a point that fits?
  - The ingredients are those of `TWO_INGREDIENTS_RULE.md`: I1, the Clebsch 3 on the leptons (m_μ/m_τ × 3,
    m_e/m_τ ÷ 3, the determinant kept), and I2, the reading S̃ = εS*εᵀ for every sector.
  - The selection is B1720's own: each class's apex τ and the lines its monodromy fixes.
  - The law ingredients are put in by hand; the selection is the principle's.

## The rule (fixed now)

- **The rows.** Every (class, line) of B1720's committed census (`the_thread_census.json` at main's 3412bf09d: 121
  classes, 3 249 points), at the class's apex τ as committed there. Both horocycles: 6 498 rows.
- **The frame.** `two_ingredients_census.evaluate`, which imports B1720's instrument unchanged (the files and hashes
  of `TWO_INGREDIENTS_RULE.md`).
- **The model under test.** S̃ for every sector, the CKM from the up and down couplings both read with S̃ (B1713's
  left-vector convention), and the Clebsch 3 on the lepton outputs.
- **The targets, the measure of fit and the calibration** are exactly those of `TWO_INGREDIENTS_RULE.md`: Huang–Zhou
  2021 at M_Z and PDG 2025's three moduli from the record's pinned files; main's worst factor; main's r_masses and
  r_ckm with seed 1720, drawn as in `two_ingredients_compare.py` (4 000 six-target draws, then 4 000 nine-target
  draws, from one generator).

| cell | prediction | prior |
| --- | --- | --- |
| H1 | the best six within a factor 2.0 | 45% |
| H2, specific | at most 1% of random hierarchies fit the six as well, with the same rows | 25% |
| H3 | the best nine within a factor 2.5 | 35% |
| H4, specific | at most 1% of random nine-target sets fit as well | 20% |
| C2, control | (a) every value committed in B1720's rows (the up sector's three readings, the down and lepton sectors' S, and the three CKM moduli with the down sector read with S) is recomputed to \|Δ ln\| < 10⁻⁶; (b) under main's readings without the Clebsch the best six equals B1720's committed best (1.80372, `comparison.json`) to 10⁻⁶ in ln | 97% |

**Read-outs (not cells).**
- The winning class, its line, apex and height, and J there.
- The same rows under main's readings (up S̃, down and leptons S) with the Clebsch.
- The ten best classes by their best six-row under the sealed rule.

**The reading, written before the run.**
- **If H2 and H4 hold,** the principle's threads select, with no continuous number free, a point where the frame
  with the two law ingredients matches the six ratios and three moduli specifically.
  - That would be the first time a selection the principle supplies decides a point that fits.
  - It would still be a structure with two ingredients put in by hand, not a derivation.
  - The next question would be which thread (B1722 says the record's measures do not reach it).
- **If H1 or H3 holds and the specificity fails,** the threads with the ingredients fit no better than they fit random
  hierarchies.
- **If H1 and H3 both fail,** the threads' apexes are not where the ingredients fit, and Im τ needs another selection.

## Disclosed

- **Seen.**
  - B1720's rows under main's readings, as committed: the up sector with all three readings, the down and lepton
    sectors with S only.
  - chat1's post hoc Clebsch what-if on those rows (`gj_posthoc.*`). With the Clebsch and main's readings, the best
    was L⁵R² on (2/5, 3/5) at 1.614.
- **Not seen.**
  - The down and lepton sectors with S̃ at any thread apex. No row of this rule's model is known; its up values are
    B1720's.
  - Any result of the two-ingredients census. Its run has not finished at this commit, and none of its values has been
    read.
- **The tests before this seal** (in a scratch directory; nothing written here).
  - An import test computed one point, class 0 (LR at its apex) on its first line. Only its comparison with B1720's
    committed row was printed: max \|Δ ln\| = 1.3 × 10⁻¹¹.
  - The comparison's code path was run on stand-in rows built from B1720's committed values (the down and lepton S
    copied into every reading). It reproduced B1720's best six exactly. No value of this rule's model entered it, and
    its cell output was not printed.
- **Instrument.** `threads_with_ingredients.py`, committed with this rule before it runs. It will run after the
  two-ingredients census finishes (the machine has two cores). Its output will be committed before the comparison is
  run.
