# B808 — the 35 empty cells are sample size, not structure. My own proposal, refuted.

cc banking seat, 2026-07-29. **Prereg `68d1aef066a0f555`, sealed and committed at `aaaebf4c`
BEFORE any computation.** Repository-instrument scope; nothing to `CLAIMS.md`.

## What was tested

B807 found **163 of 198 (face, motif) cells populated, 35 empty**, and cc immediately proposed the
35 as a research programme — *"each empty cell is either unexplored or impossible."*

**That proposal was not a test.** The empty cells concentrate on the smallest faces:
`emittance-lengths` has **2 arcs** and 10 empty cells; `infinite-hecke` **4 arcs**, 9 empty;
`emittance-eigenvalues` **3 arcs**, 7 empty. A face with two arcs cannot populate eighteen motifs.
Calling that a gap would be an unregistered-null error (**E29**), so this arc registered the null
first.

## Result against the sealed thresholds

Margin-preserving permutation null, **10,000 draws**, seed fixed:

| | |
|---|---|
| ARTIFACT (`p_empty ≥ 0.10`) | **34 of 35** |
| REAL GAP (`p_empty < 0.10`) | **1** — `congruence-tower × apolynomial`, p = 0.0454 |
| **sealed verdict (VACUOUS if ≥ 30 artifact)** | **VACUOUS** |

> **cc's proposal is refuted.** The empty-cell structure is explained by the margins.

## And the single survivor is not a survivor either

The prereg did not fix a multiple-comparisons correction. Applying the obvious one:

- 35 cells tested at `p < 0.10` ⟹ **≈ 3.5 expected below threshold by chance alone**
- **observed: 1**

**The count of "real gaps" is *below* what chance produces.** So `congruence-tower × apolynomial` is
not evidence of anything, and the honest conclusion is stronger than VACUOUS:

> **There are no real gaps in the (face, motif) plane. None.**

This is recorded because it cuts against the arc's own headline: it would have been easy to keep the
one survivor as a consolation finding, and it does not survive its own arithmetic.

## §4, also negative — and also pre-registered

The prereg fixed a second measurement in advance: `being` (112 arcs) and `hearing` (50) have **zero**
empty cells — is motif-completeness surprising?

| face | arcs | empty | `p_full` under the null |
|---|---|---|---|
| being | 84 | 0 | **0.895** |
| hearing | 42 | 0 | **0.601** |
| congruence-tower | 32 | 2 | 0.451 |
| mtc-overlay | 32 | 2 | 0.462 |

**Not surprising.** The null produces `being`'s completeness 89 % of the time. The prereg named this
as *"the arc's real result if the gap side dissolves"* — it dissolved too, and that is reported
rather than quietly dropped.

## What this actually establishes

**The two authored axes are jointly saturated.** The object's work covers the WHERE × WHAT plane as
fully as the margins permit — there is no hidden unexplored region in it, and no structure in what
is missing.

That is a real result, and it points somewhere specific: **whatever is unaccounted for is not
missing from the (face, motif) plane.** Which leaves the third axis — the one B807 found is **proved
complete and recorded in no instrument at all.**

## The methodological note

Two arcs in succession now: B807's proposal survived its test, B808's did not. The difference was
not care — it was that **the null was registered before the count was looked at**. Had the 35 cells
been worked as a programme, months could have gone into a structure that is arithmetic.

`null_test.py` · `null_test.json` · lock `tests/test_b808_empty_cells.py`
