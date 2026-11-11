# MENDS FOR THREE GATES — a patch against main at `3e25c8ec3`, with its tests

> **Superseded on 2026-11-11, the same day.** Main landed its own mends for all seven cases, and for two more, at
> `16b82acda` (its B1880), while this patch was being written. They are checked in `REAUDIT_5_2026-11-11.md` and are
> better than this patch in two places. This patch no longer applies to main and nothing in it is needed. It is kept
> as it was written, for the record of what was planted and found.

**From:** the advisor seat. **To:** cc. **Kind:** `propose:`. **This seat writes nothing to main:** the patch is for main
to read, change, apply or refuse.
**Why:** re-audits 3 and 4 accepted three of main's new gates with residuals, each shown by a planted case that passed.
The owner asked this seat to write the mends ("do all on hour proposed list", 2026-11-11).

| file | what it is |
|---|---|
| `three_mends.patch` | `git diff 3e25c8ec3` of a scratch clone: `scripts/gates/gates.py` (+93, −8) and one new file, `tests/test_three_mends_after_the_reaudits.py` (12 tests). It applies cleanly (`git apply --check`) |
| `test_three_mends_after_the_reaudits.py` | the same test file, for reading; the patch holds it identically |
| `plants_of_reaudit3_with_the_mends_out.txt`, `plants_of_reaudit4_with_the_mends_out.txt` | this seat's planted cases of the two re-audits, re-run on the scratch clone with the patch applied (the commit named in their first lines is that clone's) |

## 1. What changes, in one table

| gate | the gap (planted case) | the mend | planted again |
|---|---|---|---|
| `artifact-hashes` | **t3:** a copy with the sealed content, put where the gate looked first, was read in place of the real file | **a listed name is read one way.** A name that starts with one of the repository's top-level folders is read from the root; any other name beside its list or in the list's verification folder. A second tracked file where the name could also be read makes the entry AMBIGUOUS, and the gate refuses it | **caught** |
| `artifact-hashes` | **t4:** an entry frozen "as found" is keyed by list, name and *recorded* hash, so its file could change again | **a table of what was found:** for the 41 frozen entries whose file is tracked, the first 16 hex digits of the file's hash at `3e25c8ec3`. A further change reads CHANGED AGAIN | **caught** |
| `arrival-phrases` | **r2:** "We claim that the Standard Model is derived." passed, because "claim" contains "aim" | **the excusing words are matched from the start of a word.** A word may still run on ("aims", "goals", "wouldn't"); two may not, since the longer word asserts ("none" in "nonetheless", "never" in "nevertheless") | **caught** |
| `arrival-phrases` | **r5, r6:** a paper's source and a page below `docs/` were not read | **the reach is widened** to `docs/**/*.md` and `papers/**/*.tex`, `papers/**/*.md` | **caught** |
| `attribution` | **c3, c4:** a commit that arrives by a merge was not read | **every commit reachable from the tip** after the rule's first commit is read, not the first-parent line alone | **caught** |

## 2. Measured on main's clean tree, before and after

| | before | with the patch |
|---|---|---|
| `artifact-hashes`: entries | 1,497: 1,430 verify, 67 do not (63 distinct) | **the same.** Every entry is read as before: 339 names from the root, 1,157 beside their lists, 1 with no name; none ambiguous |
| `arrival-phrases`: files read | 151 | 548 (397 added, 42 of them `.tex`) |
| `arrival-phrases`: sentences found | 3, the frozen baseline | **3, the same three.** Nothing in the 397 added files |
| `attribution`: commits read | 699 | 699. The history has no merge, so the two readings coincide today |
| gates passing in a scratch clone | 52 of 53 | 52 of 53, once the views are regenerated (see below). The one that fails, `harvest-debt`, needs the seats' branches, which a scratch clone lacks; it fails the same way without the patch |

**After applying, regenerate the views** (`python3 scripts/views/generate.py` and `python3 scripts/views/spine.py`). One
generated page, `docs/views/THE_SPINE.md`, changes by two lines when a test file is added, and the gate
`views-generated` fails until it is rebuilt. The patch does not carry that page: it is yours to generate. Found on the
second look, after the first version of this note had said 52 of 53 without it.

## 3. The tests

| | on main as it stands | with the patch |
|---|---|---|
| the 12 new tests | 11 fail, 1 passes (the one that says the wider reach finds nothing new) | **12 pass** |
| main's own tests for the three gates, and the locks of B1874 and B1878 | pass | **pass** (41 with the new ones) |

So each mend has a test that fails without it. Each test builds a small repository or a page, plants the case and
runs the gate, in the manner of main's own.

## 4. Two things the first version of this patch got wrong, mended before it was sent

- **Whole words were too strict.** The first version matched the excusing words as whole words. Then "aims", "goals"
  and "wouldn't" would no longer have excused, and an honest sentence such as "the programme aims to show that the
  Standard Model is derived" would have been refused. Main's tree has no such sentence, so nothing showed; a list of
  twenty windows written for the purpose did. The rule is now a boundary on the left, with two named exceptions.
- **The table could not be tested.** It was read from the module only. The gate now takes it as an argument as well,
  as it takes the frozen keys.

**A side effect, intended:** a denial that opens a bracket ("(Not yet: …") now excuses, where before the word had to
follow a space.

## 5. What the patch leaves open, on purpose

| planted case | why it is left |
|---|---|
| **t7:** a list of hashed files under another name (`SEAL_SHA256.txt`) | a rule on naming is main's to choose. By a heuristic search there are about 70 such files |
| **r3:** "Nothing stands in the way now. The Standard Model is derived." | a word of denial in the 64 characters before the phrase excuses whatever it denies. Mending it means reading sentences |
| **r4:** a sentence of arrival in other words | a phrase list cannot do it, as main discloses |
| **p2:** an old form restated in other words | the same |
| **j4:** the re-audit's verdict retyped in main's own file | it needs the builder to read the seat's branch |

## 6. For main to judge

- **The list of top-level folders is fixed in the gate** (15 names). A folder added at the root later is not in it, and
  a name that starts with it would be read beside its list. A computed list could be widened by adding a folder, which
  is why it is fixed; a test asserts that every folder named exists.
- **A harmless duplicate is refused too.** Any second tracked file where a root-form name could also be read makes the
  entry ambiguous, whether or not the real file changed. Main's tree has none.
- **Reading every reachable commit refuses a merge of a branch that carries older commits with trailers.** Seats'
  branches from before the rule do. Main harvests and does not merge, so nothing changes today; if a merge is ever
  wanted, it needs a waiver by name.
- **The table of 41 hashes is one more thing to keep.** It is generated, and a test checks it against the tree.

## 7. Disclosed

- **Run in scratch clones only.** Nothing was pushed anywhere but this seat's branch.
- **The planted cases are this seat's,** and so are the tests. Main's own review may know a case these miss.
- **The full suite was not run:** only the tests named in § 3 and the 53 gates.
- **The agy lane has mended two of the same gaps on its own branch** (the decoy and the frozen entries), and two that
  this patch leaves open (t7, j4). Its work was read after this patch was written:
  `lane_b1881_read/READ_OF_THE_LANES_BRANCH.md`, § 5. The arrival and attribution mends here apply on top of the lane's
  tip as they stand, and the five cases are then caught there too.
