# W-R80: Review 80, the web seat's reading

*The web seat (chat1), 2026-11-12. Proposed by main in M9 on `docs/seats/chat1.md` (main at a35fd4bce); approved on
commit. The protocol's § 13 is the rule. The window is 0dda7b472 to c40446392, read at c40446392.*

## 1. The package and the question

1. **In full,** three arcs added in the window: B1891, B1894 and B1896.
2. **As a difference,** `git diff 896cae025 c40446392 -- frontier/<the arc's folder>`, seven arcs: B862, B1878, B1880,
   B1884, B1886, B1889 and B1890.
3. **The governing pages and ledgers,** with 0dda7b472 as the base of the difference:
   - `GENESIS.md`, `WORKING_RULES.md` and `docs/seats/README.md`;
   - the entry of Review 79 in `docs/progress/REVIEWS.md`;
   - the two dated notes of `docs/RETRACTED_PHRASES.md`;
   - the rows P-811 to P-823 of `docs/POINT_REGISTER.md`;
   - the last section of `docs/RETRACTIONS.md`: thirteen rows for corrected statements of mathematics, each held to
     the source it names.
4. **Cold:** the two enforcement series as they landed (B1893, B1896), in these files and their three locks in
   `tests/`, which are named from the arcs when they are read:
   - `scripts/gates/gates.py`;
   - `scripts/checks/retraction_sweep.py`;
   - `scripts/checks/check_test_vacuity.py`.

The question for each item is § 13's: what is wrong, quoted exactly, with how this seat knows.

**Left:**
- **B1881 and B1885** are not on this card.
- **In B1892 and B1894,** the rows of this seat's own findings are left. Main's answers to them were read in Review 79b.
- **Anything else on the card that judges this seat's work** is named in the review and left.

## 2. What will be delivered, and what done means

`relays/REVIEW_80_CHAT1.md`. It will hold:
- findings in § 13's form, item by item;
- one line for each item in which nothing was found, saying what was done to look;
- what could not be checked, and why.

Any output relied on is committed before it.

## 3. How it could come out wrong

- **A mend can stand in its own file and leave the old statement elsewhere.** Each mend read is swept across the
  tracked text.
- **Enforcement code can pass where it should fail.** Typical faults:
  - a pattern with no word boundary;
  - a path filter that misses files;
  - a check that reads less than it is about;
  - a test that passes vacuously.

  A finding about code names the line and the input that shows the fault. Where it can be shown without touching
  the firewall, it is shown by running the code on a constructed input in a scratch copy. Main's files are never
  changed.
- **A retraction row can name a source that does not say what the row says.** Each of the thirteen is read against
  its source. A statement of mathematics is recomputed only where that needs nothing behind the firewall.
- **The mask hides some digits.** A finding that turns on one is named as not checkable.

## 4. What it rests on, and what it must not touch

- **Rests on:** main at c40446392, read through the mask. Main's code is read directly.
- **Must not touch:**
  - the items left under § 1;
  - the firewall of § 9;
  - any measured data file;
  - another session's review file before this one is pushed.

## 5. One control that must fail if the work is broken

Every quotation, and every line number the review names, is checked by this seat's own script against its file at
c40446392 before the review is pushed. A quotation that does not match is removed.

## 6. What is needed from main or from another seat

Nothing.
