# W-R81: Review 81, the web seat's reading

*The web seat (chat1), 2026-11-13. Proposed by main in M14 on `docs/seats/chat1.md` (main at a45e66fd1); approved on
commit. The protocol's § 13 is the rule. The window is c40446392 to 0e637ea9e, read at 7d7ab1dfa (the branch
`review-81/read`) as `git diff c40446392 7d7ab1dfa -- PATH`, through the mask. Main has planted faults at 7d7ab1dfa
and sealed their list; this seat does not open 7d7ab1dfa by itself and does not compare it with 0e637ea9e.*

## 1. The package and the question

1. **In full,** the one arc added in the window: B1898 (Review 80's entry).
2. **As a difference from c40446392,** eighteen older arcs: B1836, B1858, B1861, B1867, B1873, B1877, B1878, B1880,
   B1881, B1883 (its builder script; its page is generated), B1885, B1890, B1891, B1892, B1893, B1895, B1896 and
   B1897.
3. **The governing pages and ledgers, as a difference:** `WORKING_RULES.md`, `ROADMAP.md`, `docs/MASTERPLAN.md`,
   `docs/PRACTICES.md`, `docs/THE_BAR.md`, `docs/RETRACTED_PHRASES.md`, `docs/RETRACTIONS.md`,
   `docs/SEAL_LEDGER.md`, `docs/POINT_REGISTER.md`, `docs/HARVEST_LEDGER.md`, `docs/CAMPAIGN_STATUS.md`,
   `docs/OPEN_LEADS.md`, `docs/OPEN_PROBLEMS.md`, `docs/LEAD_REGISTER.md`, `docs/PRICED_DOORS.md`, `CHANGELOG.md` and
   `PROGRESS_LOG.md`.
4. **Main's instruments, as a difference:** `scripts/checks/absence_sweep.py`, `scripts/checks/point_debt.py`, the
   eight tests `tests/test_b1011_mckay_tensor.py`, `tests/test_b1235_two_seat_harvest.py`,
   `tests/test_b355_weil_layer_independent.py`, `tests/test_b448.py`, `tests/test_b674_route1.py`,
   `tests/test_b799_doors.py`, `tests/test_r28_10_stabilizations.py` and `tests/test_w2_molien_cell.py`, and the
   paper's verification manifest (`papers/P3_THE_PAPER/verification_package/MANIFEST.*`).

Two things are looked at hard, as M14 asks:
- **B1898's account of what main checked:** for each finding it says is held, is there a file in its
  `verification/checks/` folder, or a sentence that a file supports?
- **The six register rows moved on 2026-11-13** (P-239, P-262, P-263, P-268, P-670 and P-694, landing 78edf8694): is
  each next action real, is the draft where the row says, and is the declined one replaced as it says?

The question for each item is § 13's: what is wrong, quoted exactly, with how this seat knows.

**Left:**
- **In B1898,** the rows of this seat's own findings. The review says which.
- **In the eighteen arcs,** any change whose dated note or commit subject names a finding of this seat's.
- **Main's hand-over folders under `docs/handoffs/`** and the seats' pages, as M14 says.

## 2. What will be delivered, and what done means

`relays/REVIEW_81_CHAT1.md`. It will hold:
- findings in § 13's form, item by item;
- one line for each item in which nothing was found, saying what was done to look;
- what could not be checked, and why.

Any output relied on is committed before it.

## 3. How it could come out wrong

- **A planted fault reads like an ordinary line.** Every number, quotation and cross-reference in the package is a
  place a plant can sit, so each is held to the source it names, not to how plausible it reads.
- **A "held" can rest on nothing.** For B1898, each finding's "held" is matched to a named file by machine, and the
  files are opened.
- **A mend can stand in its own file and leave the old statement elsewhere.** Mends are swept across the tracked
  text.
- **Enforcement code can pass where it should fail.** For the two scripts and eight tests, each changed assert or rule
  is run on a constructed input in a scratch copy (a planted negation, or a planted bad line), so that a test that
  cannot fail is found. Main's files are never changed.
- **The mask hides some digits.** A finding that turns on one is named as not checkable.

## 4. What it rests on, and what it must not touch

- **Rests on:** main's read branch at 7d7ab1dfa, as differences from c40446392, read through the mask. Code is read
  directly; to run it, a scratch worktree is checked out at c40446392 and the window's difference for the needed paths
  is applied to it, so that 7d7ab1dfa is not opened by itself.
- **Must not touch:**
  - the items left under § 1;
  - the firewall;
  - any measured data file;
  - 7d7ab1dfa set against 0e637ea9e;
  - the other reader's review file before this one is pushed.

## 5. One control that must fail if the work is broken

Every quotation, and every line number the review names, is checked by this seat's own script against its file at
7d7ab1dfa before the review is pushed. A quotation that does not match is removed.

## 6. What is needed from main or from another seat

Nothing.
