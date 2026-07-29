# B808 — PREREGISTRATION: are the 35 empty cells real gaps, or sample size?

**Sealed before any computation.** cc banking seat, 2026-07-29. Repository-instrument scope —
no physics, nothing to `CLAIMS.md`.

## 1. The confound, spotted before the test rather than after

B807 declared the object's description a triple `(face, motif, closing)` and found **163 of 198
(face, motif) cells populated, 35 empty**. cc then proposed the 35 as a research programme:
*each empty cell is either unexplored or impossible.*

**That proposal is not yet a test, and may be vacuous.** The empty cells concentrate on the
**smallest faces**:

| face | arcs | empty cells |
|---|---|---|
| emittance-lengths | **2** | 10 |
| infinite-hecke | **4** | 9 |
| emittance-eigenvalues | **3** | 7 |
| coupled-double | 16 | 4 |
| congruence-tower | 34 | 2 |
| mtc-overlay | 40 | 2 |
| sln-tower | 32 | 1 |
| **being (112), hearing (50), children (20), meeting (17)** | | **0** |

A face with 2 arcs cannot populate 18 motifs. **Most of the 35 may be arithmetic, not structure.**
Treating them as gaps without a null would be an unregistered-null error (E29), and this arc exists
to avoid committing it.

## 2. The null, fixed now

**Null model:** permutation preserving both margins. Hold each arc's *number* of faces and *number*
of motifs fixed; reshuffle which faces and which motifs, drawn according to the observed marginal
frequencies; recount empty cells. **10,000 permutations.**

For each cell, `p_empty` = fraction of permutations in which that cell is empty.

**Cell classification, thresholds fixed here:**
- **ARTIFACT** — `p_empty ≥ 0.10`: the null produces this emptiness at least 10 % of the time.
- **REAL GAP** — `p_empty < 0.10`: emptier than chance; a genuine absence.

**Arc-level verdict, fixed here:**
- **VACUOUS** if **≥ 30 of 35** cells are ARTIFACT — the "empty cell programme" dissolves and cc's
  proposal was wrong.
- **SUBSTANTIVE** if **≥ 6** cells are REAL GAPS — a genuine, named research target list.
- **MIXED** otherwise, reported as such with the count, and *no* programme declared.

## 3. Pre-stated expectation, so the result can disappoint it

**I expect VACUOUS or MIXED**, and I expect the survivors — if any — to be the cells on the four
large faces: `congruence-tower × apolynomial`, `congruence-tower × hyperbolicity_split`,
`mtc-overlay × five_web`, `mtc-overlay × hyperbolicity_split`, `sln-tower × five_web`, and the four
`coupled-double` cells.

**I explicitly expect my own earlier proposal ("35 cells are a research programme") to be largely
refuted.** Recorded here so the refutation cannot later be softened into "we always knew the small
faces were thin."

## 4. The second measurement, also fixed now

**`being` (112 arcs) and `hearing` (50 arcs) have ZERO empty cells** — every motif appears on them.
Under the null, is *that* expected or surprising? Report `p_full` for each large face. A face that is
motif-complete beyond chance is a positive structural finding and would be the arc's real result if
the gap side dissolves.

## 5. What would make this arc a failure

- Adjusting the 0.10 threshold, the 30/6 counts, or the permutation count after seeing results.
- Reporting MIXED as whichever of VACUOUS/SUBSTANTIVE reads better.
- Declaring a research programme over cells the null explains.
- Ignoring §4 because §2 produced a tidier headline.
