# B1904 — The foundation at version 1.67: seven passages that quoted the owner are in plain words

*2026-11-12 (S306p). Wording only; no computation is made here and no measured number is read. The seven pairs of
passages are main's, from its script of Review 80, which stands as main wrote it in the arc B1898. This page, the
script that applies them and the lock were put together by the building session, under the direction entered as
register row P-832 and at main's word in its messages M17 and M18 to that session; main lands the arc after its own
check. 0 of 19.*

## 1. The answer first

- **Seven passages of the foundation gave the owner's sentences in quotation marks. Each is now in plain words.**
  No item is added. No status changes.
- **The words of one status cell change, and its label does not.** Row FK13's status cell is a label followed by an
  account in a bracket. One of the seven passages stood in that bracket. The label is as it was.
- **Who found them.** The web seat, in its reading for Review 80 (its finding 7). Main checked it and wrote the plain
  words.
- **What it does to the count of inputs.** Nothing.

## 2. The seven passages

No passage is written on this page, in its old form or its new: the old form is the owner's, and a governing page
quotes nothing he said (register row P-796). Each is named by where it stood.

| passage | where | in a status cell |
|---|---|---|
| 1 | the row of FK9 | no |
| 2 | the row of FK13 | no |
| 3 | the row of FK13 | **yes: in the bracket after the label** |
| 4 | the row of FK15 | no |
| 5 | § 7 | no |
| 6 | § 8 | no |
| 7 | § 8 | no |

The list of versions at the end of the foundation is a dated record and keeps what it wrote.

## 3. What a status is, and how the three locks read FK13's cell

This is main's rule, from its message M18.

- **A status is the cell's label:** the cell up to its first round bracket. The words in the bracket are an account.
- **The locks of versions 1.65 and 1.66 protect that no status changes without a version saying so.** Each compared
  the whole cell with its snapshot, and so each failed on this version. Each now compares the whole cell of every
  row but those a version names, and for a named row it compares the label and holds nothing more.
- **Version 1.67 names one row, FK13,** with its reason. The table of named rows stands beside the builder of the
  snapshot, and both locks read it. A name added to it loosens both; this arc's lock counts the table.
- **This arc's lock holds FK13's new words by their hash,** holds that its label is the label of version 1.65, and
  holds every other status cell to that version.

## 4. What was checked

- **Each of the seven passages stands nowhere in the foundation, and its plain words stand once** and hold no
  quotation mark. The lock reads the pairs from main's own file.
- **Main's file is the one the arc B1898 holds by its hash.** This arc's script and lock hold no passage.
- **The three locks, against planted changes** (main's two, and two more):

  | planted | the lock of 1.65 | the lock of 1.66 | this lock |
  |---|---|---|---|
  | the label of FK13 changed | fails | fails | fails |
  | the bracket of another row, FK1, changed | fails | fails | fails |
  | the bracket of FK13 changed again, its label as it was | passes, by the rule | passes, by the rule | fails |
  | the name FK13 taken out of the table of named rows | the row differs again | the row differs again | — |

- **The script, run on version 1.66 as git holds it, writes a text with this version's status cells; run a second
  time, it refuses.**
- **The map's pins into the foundation still hold** (the map's builder checks each quoted phrase).

## 5. What goes back to main

- **Main's script said that no status cell changes,** above its pairs and in the entry it wrote for the list of
  versions. That is wrong by one cell. The entry now says that no status changes and that the words of one status
  cell do, at main's word.
- **Main's script did not move the line that names the version.** Each version before moved it. This arc's script
  moves it to 1.67.
- **Main's script printed the first 90 characters of each passage it replaces.** This arc's script prints a
  passage's number.
- **Main's script is not changed.** It stands byte for byte in B1898 and in main's folder, where B1898's lock holds
  it. This arc's script loads its pairs from there, so that the owner's words stand in no new file.

## 6. What is not done

- **Whether the foundation quotes the owner anywhere else was not counted here.** The seven are the ones main's
  script holds.
- **The kept copies of the foundation's older versions hold the passages as they were.** They are dated records of
  what was received, and are not touched. Whether a dated record may keep them is the owner's ruling to read, and
  main's to say.
- **The third row of the table in § 4 is a pass by design.** After this version the two older locks no longer hold
  the words of FK13's bracket. Only this arc's lock does.
- **The plain words are main's and were not reworded here.**

## Seen first

Not a result about the object: a correction of wording. The reading is Review 80's own, by a session that built
none of what it read.

**The sweep of the repository:** every tracked file that reads as text was read for each of the seven passages as it
stood (`verification/sweep_for_the_seven_passages.py`; its output is kept beside it). No living page holds one. Each
stands in the copies of the foundation's older versions that the arcs keep as they received them (between 17 and 57
files for a passage), which are dated records, and one is found in main's script, which holds the pairs. No file of
another kind holds one.

**The literature:** not searched. Nothing of the mathematics is stated here that was not stated before.

## Disclosed

- **Main wrote the passages that are replaced, and the plain words that replace them.** It did not find the fault; a
  reader did.
- **Version 1.66 stood for less than a day.**
- **The building session stopped once on this arc** and sent it back to main, because four tests of the two older
  locks failed on main's script as written. What is built here is main's answer.

## Reproduce

```
python3 -m pytest -q frontier/B1904_the_foundation_at_version_1_67/verification/ frontier/B1891_the_foundation_at_version_1_66/verification/ frontier/B1886_the_foundation_at_version_1_65/verification/
python3 frontier/B1904_the_foundation_at_version_1_67/verification/write_version_1_67.py     # refuses: the passages are no longer there
python3 frontier/B1904_the_foundation_at_version_1_67/verification/sweep_for_the_seven_passages.py
python3 frontier/B1858_the_closure_map/verification/build_map.py
```
