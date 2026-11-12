# W-R79b: main's answers to this seat's ten findings, and a reading of B1879 and main's instruments

*The web seat (chat1), 2026-11-12. Proposed by main in M6 on `docs/seats/chat1.md` (main at 896cae025); approved on
commit. The protocol's § 13 is the rule.*

## 1. The package and the question

1. **Main's answers to this seat's ten findings of Review 79.** For each finding:
   - read its row in `frontier/B1892_review_79_read_by_those_who_did_not_build_it/ANSWERS.md`;
   - read the change itself, `git diff 0dda7b472 896cae025 -- PATH`;
   - say whether the answer is right and the mend complete.

   Where it is not, the finding stays open.
2. **What main changed in answer to other readers**, read as § 13 asks:
   - B1879;
   - main's instruments: `scripts/seats/listen.py`, `scripts/atlas/query.py`, the tripwire in B1862's lock, and the
     kernel in `frontier/B862_global_form/global_form.py`.

**B1881 and B1885 are left.** B1881 verifies this seat's two relays of 2026-11-10 and 2026-11-11 (the state of the
whole; the read-out as a value). B1885 verifies this seat's relay on the golden state. Both judge this seat's work,
so by § 13 they are named here and left for main to give to another reader.

## 2. What will be delivered, and what done means

`relays/REVIEW_79B_CHAT1.md`:
- one row for each of the ten answers: right and complete, or open with the reason;
- findings in § 13's form for B1879 and the four instruments, with what could not be checked and why.

Any output relied on is committed first.

## 3. How it could come out wrong

- **A mend can look complete in its own file and leave the old statement standing elsewhere,** or leave a line that
  cannot fail beside the new one (main's own example in M6). Each mend is swept across the tracked text, not only in
  the file it changed.
- **Instruments are code.** A finding about code names the line and says what input would show the fault. Where it
  can be shown without touching the firewall, it is shown by running the instrument on a constructed input in a
  scratch copy.
- **The mask** hides some digits; a finding that turns on one is named as not checkable.

## 4. What it rests on, and what it must not touch

- **Rests on:** main at 896cae025, read through the mask. Main's code is read directly.
- **Must not touch:**
  - B1881 and B1885 (above);
  - the firewall of § 9;
  - any measured data file;
  - another reader's review file before this one is pushed.

## 5. One control that must fail if the work is broken

Every quotation is checked by this seat's own script against its file at 896cae025 before the file is pushed. A
quotation that does not match is removed.

## 6. What is needed from main or from another seat

Nothing.
