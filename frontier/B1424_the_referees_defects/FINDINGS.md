# B1424 — THE REFEREE'S DEFECTS, EVERY ONE VERIFIED: the shipped package could not pass on a clean checkout, and the paper's census drift was measured on the wrong population

cc, 2026-09-17. An outside referee re-derived about fifty of the paper's quantitative claims on a clean machine,
**using no code or data from this repository**, and found everything checkable correct — and five defects.
Each is verified here independently before action. **Verdict: PROVED (the audit); all five confirmed; four fixed,
one corrected in the paper.**

## 1. THE SHIPPED PACKAGE COULD NOT PASS ON A CLEAN CHECKOUT — confirmed, and it is the worst of the five
`tests/test_b1419_arithmetic_fillings.py` reads `arithmetic_census_closed.jsonl` row by row. That file was **excluded
by `.gitignore`'s blanket `*.jsonl` rule**, so it is present on this bench and absent from every fresh clone: all four
of its locks fail for anyone who runs the package we ship. They are the locks for **the one row of this paper that had
to be withdrawn and corrected**. Verified with `git check-ignore`, which names the rule and line. Fixed by a negation
rule and the file is now tracked. A scan of every lock for data files that are present but untracked found **exactly
one other**, and it is correctly guarded (skips when absent, marked slow).

## 2. THE PAPER'S CENSUS DRIFT WAS MEASURED ON THE WRONG POPULATION — confirmed, recomputed two ways
The paper quoted `34.25 % → 29.38 % → 21.12 %` at census depths 0, 20 000, 80 000 inside a paragraph whose other
rates are **one-cusped**. The sweep behind those figures runs `snappy.OrientableCuspedCensus` with **no one-cusp
filter** (`b1400_census_bias_stratified.py:61`). Recomputed here on both populations, by brute force over images of
the generators in SL(2,3) and independently by GAP `GQuotients`, both with m004 as a live control:

| population | depth 0 | depth 20 000 | depth 80 000 |
|---|---|---|---|
| full orientable cusped (212 641) | 34.25 % | 29.38 % | 21.12 % |
| **one-cusped (203 123)** | **33.00 %** | **33.88 %** (GAP: 33.92, one manifold skipped) | **31.38 %** |

So the steep decline is real on the full census and **absent on the one-cusped census**, which is the population the
sentence is about. The paper is corrected to carry both triples and to say which is which. **The consequence favours
the paper**: the 2T door is *not* an artefact of the census's small end where the object sits — it stays near one in
three eighty thousand manifolds deep — so the genericity argued for in that section is stronger, not weaker.
B1400 keeps its finding, with the population named in an addendum; L211 annotated.

## 3. THE PACKAGE'S OWN REPORT WAS STALE — confirmed
`anc/REPORT.md` shipped certifying **54 claims / 75 records** against a manifest carrying **67 / 95**, dated two days
earlier, at a superseded commit. Regenerated. And a second defect found while fixing it: the report said `FAIL`
**without naming which lock failed**, so a reader could not act on it. The runner now prints pytest's short summary
and the five slowest locks, with the colour codes stripped (the first version of that patch matched nothing because
pytest colours the marker).

## 4. THE MANIFEST'S COMMIT DID NOT CONTAIN WHAT IT LISTED — confirmed
`MANIFEST.json` recorded `git_head 2c06d7a9` while listing B14's lock, which first exists in its successor
`f52c4f56`: the manifest was rebuilt during a session **before** that session's commit. The rule is now written into
the submission recipe: **commit, then rebuild the manifest and report, then amend** — the same shape as the
views-generated rule the repository already follows.

## 5. TWO NUMBERS AND ONE DROPPED HYPOTHESIS — confirmed
`sin²θ_W` misses by **0.822 %**, not the `0.9 %` the paper stated in three places (checked: (0.2312 − 0.2293)/0.2312);
corrected to 0.8 % in the prose, the chain-table title and the crossing paragraph. And the paper stated
Menal-Ferrer–Porti's hypotheses as complete, non-elementary, topologically finite while **dropping the source's
`n ≥ 2`**: the symmetric power must be non-trivial. Now stated, with the note that the theorem says nothing about the
untwisted case and we do not use it there. (The referee's sixth item, Figure 1's "fifty-two" against 53, was fixed
the same day in the typesetting pass, before their report arrived.)

## What the package now does on this bench
Seals **21/21**. Locks, after the fixes: the failure the referee could not name turns out to be **two** —
`test_b1306_the_older_debt` firing correctly on **six genuinely unrowed audit-seat documents** (six pre-execution
proof candidates the seat pushed after its pin), now rowed as received-and-not-read with their own fences, since a red
test with no name is worse than a named debt and nothing in the paper cites them; and one subprocess lock whose failure this arc attributed to load.
**That attribution is WRONG and is corrected in `ADDENDUM_2026-09-18_THE_DIAGNOSIS_WAS_WRONG.md`:** the lock is hash-order dependent (E83), not load-sensitive, and raising its timeout fixed nothing.

## What the referee verified that we should not forget
About fifty claims re-derived from the manuscript's prose alone: the census counts cell by cell including the tie
list, 66 of 87 covers chiral by two orientation-aware tests, the volume as an L-value to **60** decimal places where
the paper claims 32, the content census to two contents and four rays, the square-root uniqueness with twelve
controls, Koide at 0.89σ, and Menal-Ferrer–Porti read at source with the paper's account of its hypotheses judged
exactly right. They also caught themselves reproducing this project's own **E82** error class — a cusped criterion
applied to a filled manifold — and corrected it in their own report.

## Locks
`tests/test_b1424_referee_defects.py`: the drift on both populations with its control, the census file tracked, the
gitignore negation present, and the corrected percentage in the paper.
