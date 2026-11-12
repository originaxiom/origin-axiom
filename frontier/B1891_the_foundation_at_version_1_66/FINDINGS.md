# B1891 — The foundation at version 1.66: four corrections from Review 79

*Main, 2026-11-12 (S306p). Wording only; no computation is made here and no measured number is read. 0 of 19.*

## 1. The answer first

- **Four sentences of the foundation are corrected, and one quotation is given in plain words.** No item is added. No
  status cell changes.
- **Who found them.** Three were found by sessions that built none of what they read, in the reading for Review 79.
  The fourth follows from one of those. Main reproduced each at its source before changing a word.
- **What it does to the count of inputs.** Nothing.

## 2. The corrections

| where | it read | it reads now | why |
|---|---|---|---|
| §0, who sets a status | "Eleven entries of the record came as suppositions" | fourteen entries, which are eleven things | the advisor seat's sort, which the sentence cites, counts fourteen entries that are eleven things |
| GM5c, (a) | "every statement the record holds about the weave is unchanged except the hand" | most of what the record holds is unchanged, and what changes is the hand | B1879 says "most". The group's order changes, as its own statement says, and two negatives were not restated |
| GM5c, (a) | "the walk's measure ... stand" | the walk's law of run lengths | B1879 computed the law of the lengths of runs. The measure at every strength of the pull-back, and where the walk's point lies, are not shown unchanged (B1879 as corrected at Review 79) |
| GM5c, (a) | the tick "is the only history of at most five letters that does" | the only one among those that are not a power of a shorter one | B1879's count leaves out powers; the square of the tick is a power and fixes a curve |
| GM5c, (b) | the option the owner chose, in quotation marks | the same in plain words | his ruling of 2026-11-11 that his messages are private (register row P-796); this is a governing page |

## 3. What was checked

- **No status cell changed.** The lock compares every row that opens with an identifier, and every row of every table
  that has a column headed Status, between version 1.65 as committed and the file as it stands.
- **The map's pins into the foundation still hold** (the map's builder checks each quoted phrase).
- **The log has its entry,** above that of 1.65, which is not rewritten.

## 4. What is not done

- **The foundation still quotes the owner elsewhere.** Only the one quotation in the passage corrected here was put
  in plain words. How many others stand in the file was not counted.
- **The sentence on the unit at the cusp** needs no change: the foundation's row FK10 has said since version 1.59 that
  the unit is uniform on three lines (register row P-802, closed).

## Seen first

Not a result about the object: a correction of wording. The sweep is the review's own: the three sentences were found
by its readers, and main looked for each old form in the foundation and in the pages that quote it.

**The literature:** not searched. Nothing of the mathematics is stated here that was not stated before; the arc changes
which words the foundation uses for what the record already computed.

## Disclosed

- **Main wrote the sentences that are corrected here.** It did not find the faults; readers did.
- **Version 1.65 stood for one day.**

## Reproduce

```
python3 -m pytest -q frontier/B1891_the_foundation_at_version_1_66/verification/
python3 frontier/B1858_the_closure_map/verification/build_map.py
```
