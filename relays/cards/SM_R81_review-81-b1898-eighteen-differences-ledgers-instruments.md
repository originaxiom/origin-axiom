# SM-R81 — Review 81: B1898 in full, eighteen arcs as a difference, the governing pages and ledgers, main's instruments

*Card proposed by main on docs/seats/sm.md (M12, 2026-11-13); committed with main's scope, and approved by that
commit. Main at 204ee91ed when M12 was read. The rules are § 13 of the protocol (docs/seats/README.md on main).*

## 1. The package and the question

Do main's changes in Review 81's window, c40446392 to 0e637ea9e, say only what their own outputs support? Everything is
read at 7d7ab1dfa (the branch review-81/read), as git diff c40446392 7d7ab1dfa -- PATH, and never as that commit by
itself or against 0e637ea9e. That commit holds faults that main planted; their list is sealed. Read:
- **in full,** the one arc added in the window: B1898, Review 80's entry;
- **as a difference,** eighteen older arcs: B1836, B1858, B1861, B1867, B1873, B1877, B1878, B1880, B1881, B1883 (its
  builder script), B1885, B1890, B1891, B1892, B1893, B1895, B1896 and B1897;
- **as a difference,** the governing pages and ledgers M12 lists, CHANGELOG.md and PROGRESS_LOG.md among them;
- **as a difference,** main's instruments M12 lists, with the paper's verification manifest;
- **looked at hard:**
  - B1898's account that 80 findings were checked in full and every one held: is each "held" supported by a file
    in its verification/checks/ folder, or by a sentence that a file supports?
  - the six register rows moved on 2026-11-13 (P-239, P-262, P-263, P-268, P-670, P-694) in the landing 78edf8694:
    is each next action real, the draft landed where the row says, and the declined one replaced as it says?

## 2. What will be delivered, and what done means

- **One file,** relays/REVIEW_81_SM.md: one entry per finding, in the form of § 13 (the arc or page, the file, the
  sentence or line quoted exactly, what is wrong, and how it is known).
- **For each item of § 1,** what was read, and what could not be checked and why. An item with no finding gets one
  line saying what was done to look.
- **Committed first,** under relays/sm_r81/: every recomputation, and the machine check of every quotation.
- **Done means** every item of § 1 is reported, and the file is pushed.

## 3. How it could come out wrong (written before any reading)

- **A quotation not in its file** at 7d7ab1dfa. Every quotation is checked by machine, with a control altered by one
  character.
- **A finding resting on a misreading.** Readers within this session may take parts. Every finding they return is
  checked again here before entry, against the file and, where it is a number, by this seat's own code.
- **A plant missed** because a difference was skimmed. Every changed hunk of each listed path is read, and the count
  of hunks read is given per item.
- **Judging this seat's own work.** In B1898 the rows of this seat's Review 80 findings are left, and the file says
  which. Any change whose dated note or commit subject names a finding of this seat's is left and listed.
- **Reading what is not to be read:** 7d7ab1dfa by itself, or against 0e637ea9e; the other reader's file before this
  one is pushed.

## 4. What it rests on, and what it must not touch

- **It rests on** main's commits c40446392 and 7d7ab1dfa, read as git objects, and this seat's own code.
- **It must not touch:**
  - **any held-out target or measured value.** § 9's firewall holds in full, with the files M6 names as not to be
    opened. No script of an arc that compares with a measurement is run;
  - **any file with agy_ in its path;**
  - **GENESIS and CLAIMS,** which are read, and never edited;
  - **main's hand-over folders under docs/handoffs/,** which M12 puts outside this review.
- **No session is credited** in a statement of the mathematics, and the owner is not quoted.

## 5. One control that must fail if the work is broken

- **The quotation check** is run once on a quotation altered by one character, and must report it missing.
- **Any recomputation** is run once with a planted error, and must disagree with the stated value.

## 6. What is needed from main or another seat

Nothing to start. An item that cannot be located goes under needs in the status file.
