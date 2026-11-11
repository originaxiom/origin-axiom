# B1877 — Review 78: the plan of all remaining work, an outside audit taken up, and ten faults in main's own arcs

*Main, 2026-11-11 (S306p). The periodic review, due since the twentieth commit after Review 77 and run at the
thirty-third; the push gate fires at forty. The review's entry is in `docs/progress/REVIEWS.md` and is the record;
this page says what the review did that an arc can lock. Process only: no value is computed. 0 of 19.*

## 1. The answer first

- **Two readers read five of main's own arcs in full and found ten faults. All ten are right.** Main checked each at
  its source, and each is corrected where the corrected line stands (`verification/readers/reader_READ_IN_FULL.md`).
- **The gravest is that three corrections did not reach every place.** They were made in answer to an audit of
  exactly that fault. A lock now reads the whole record for each old form and fails where one stands unmarked.
- **One of main's checks could not fail, and its repair changed an answer.** "The twins come together" holds by
  linear algebra. The count that can fail shows that "one twin or both as the mark" is a real choice, not a
  convention.
- **Three of Review 77's eight items are resolved and five are carried for the first time.**
- **The window originated no science of main's own.** It built the plan, took up the audit and verified eight
  results of the seats. What those results leave standing as the open object is one thing: the weight.
- **The owner decided seven things at the review,** each put by main with its recommendation: the tick is an act;
  three sentences on the principle's wording are the owner's for main; a ground is the act itself; "the ledger must
  close" means that the whole agrees with itself; the outreach stays paused; the paper stays frozen; and a compliance
  note to the agy lane was approved, which turned out not to be needed. The first four are rulings to main (P-771,
  P-774) and are carried out under P-767, not here.

## 2. What the review changed

| what | where |
|---|---|
| the premise's two cases, carried to six places | B1853, B1855, B1857, `docs/THE_TAU_READOUT_RULE.md`, B1856's verdict line, the register's row P-738 |
| the lemma's "commuting", carried to three places | B952's verdict line and results file, `docs/GUT_REQUIREMENTS_LEDGER.md` |
| B854's scope, carried to its verdict block | B854's findings |
| a lock that fails where an old form stands unmarked, with a planted control | B1862's lock |
| the twins: an identity stated as one; the real count; the fork's answer corrected | B1872's script, findings, verdict line and lock |
| the four generators against the charge reading's word form, computed | B1872 |
| four stale counts corrected; one line of live counts that the lock compares with the builder | B1861 |
| a planted control for every refusal of the programme's builder (24 of 72 had never fired), and a test that each one fires | B1861's lock |
| the title's "seven" corrected to six | B1865 |
| a gate that compares the closure map and the closure programme with their builders | `closure-generated`, `tests/test_closure_generated.py` |
| thirteen glosses; three classes' new instances; nine practices | `TERMINOLOGY.md`, `docs/ERROR_LEDGER.md`, `docs/PRACTICES.md` |
| the read-out on the whole, registered as the first lead | P-776 |
| the owner's rulings of 2026-11-11, recorded in the owner's words | P-771, P-774, P-697, P-081, P-082, P-253; the programme's § 9 |

## 3. What the review did not do

- **It carried five of Review 77's items without working them** (the lanes' paired current pole; the physical lane's
  two packets; the agy lane's three theorems; seven process arcs; the tube at k = 3).
- **It did not read the six arcs whose sealed scripts changed after their seal** (B1874). That is the first part of
  P-772.
- **It carried out none of the owner's rulings,** the eleven of 2026-11-10 or the six of 2026-11-11. That is P-767
  and the review's first item.
- **The readers ran no test.** The fresh-clone suite did.

## Seen first

- **The repo sweep:** the review tool's gather (the loop, the branches, the seals, the provenance sweep, the sample
  drawn by the anchor's seed) was run before anything was written; its output is quoted in the review's entry.
- **The literature:** none needed.

## Disclosed

- **All five arcs read in full are main's own, of the two days before the review.** The readers are two instances of
  one model family, as main is. A differently built reader would be stronger evidence.
- **Main had re-read none of the ten faults out of its own arcs.** Each was found by a reader, by a seat's re-audit,
  or by a lock that reads the whole record.
- **The review ran thirteen commits after it fell due.**

## Reproduce

```
python3 scripts/review/review_tools.py
python3 -m pytest -q frontier/B1877_review_78_the_decadal_review/verification/
```
