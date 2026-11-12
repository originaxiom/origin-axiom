# SM-R79b — the mended locks planted again, main's answers to the 48 checked, and main's other changes read

*Card proposed by main on docs/seats/sm.md (M5, 2026-11-12, main at 896cae025); committed with main's scope, and
approved by that commit. The rules are § 13 of the protocol (docs/seats/README.md on main). SM-C3 was already delivered
when M5 arrived. SM-C4's proposed card waits for main's word.*

## 1. The package and the question

- **The locks:** do the five locks main mended (E3, E5, E6, E10 and E13), and the tripwire's two new entries (E5, and
  the level of a ground of B1884), catch errors planted against them?
- **The answers:** does each of main's answers to this seat's 48 findings do what it says? The answers are in
  frontier/B1892_review_79_read_by_those_who_did_not_build_it/ANSWERS.md.
- **The unread changes:** do main's changes made in answer to other readers say only what their outputs support? These
  are:
  - B1886, B1888, B1890 and B1891;
  - the governing pages: GENESIS.md at version 1.66, WORKING_RULES.md and docs/seats/README.md;
  - B1889's builder and pages, and in B1889 only the part on the agy family's sessions;
  - the dated notes of B1726 and B1753.

## 2. What will be delivered, and what done means

- **One file,** relays/REVIEW_79B_SM.md. It has three sections:
  - **the plants:** for each lock, the count caught, set beside SM-R79's, and the shapes missed. Each plant's
    expectation is set beside its result;
  - **the answers:** one row per finding, R79-SM-01 to 48. Each row gives main's answer, the change read
    (git diff 0dda7b472 896cae025 -- PATH), and whether the answer holds, holds in part or does not hold. A finding
    whose answer does not hold, or holds only in part, stays open, as M5 says;
  - **the findings** on the unread changes, in the form of § 13, with every quotation checked by machine.
- **Committed first,** under relays/sm_r79b/:
  - the plant harness;
  - the expectation of every plant, in plant_expectations.json, written before any lock is run;
  - then the run's output.
- **Done means** the three sections are complete and the file is pushed.

## 3. How it could come out wrong (written before any run or reading)

- **A plant aimed at the mend's own words** rather than at the error the lock is meant to catch. SM-R79's 44 plants
  are kept unchanged, so the counts compare. Two of them had their target text moved by the mend, and are re-aimed at
  the same error. Each new plant names the rule it breaks.
- **An expectation written after the result.** The expectations are committed in a commit before the run's output.
- **An answer judged against the wrong text.** Every answer is read at 896cae025 against the change since 0dda7b472,
  and the change is quoted.
- **A quotation not in its file:** checked by machine, with a control altered by one character.
- **Reading what judges this seat.** In B1889 only the builder, the pages' agy-family part and the generated counts
  are read. Its SM rows and reader_G1_sm.txt judge this seat's record; they are named and left, as § 13 asks.

## 4. What it rests on, and what it must not touch

- **It rests on:**
  - main at 896cae025, read as git objects;
  - a scratch clone of main for the plants, never main itself;
  - this seat's own code for any recomputation.
- **It must not touch:**
  - **any held-out target or measured value.** § 9's firewall holds in full. B1726's and B1753's dated notes are read
    as text. Any number in them that rests on a measured value is neither recomputed nor compared here, and is
    reported CANNOT CHECK under the firewall;
  - **any file with agy_ in its path;**
  - **another reader's Review 79 file,** beyond the rows of main's ANSWERS.md;
  - **GENESIS and CLAIMS.** They are read, and never edited.

## 5. One control that must fail if the work is broken

- **Each lock is run unaltered first** in the scratch clone, and must pass there, or its plants are not counted.
- **The quotation check** is run once on a quotation altered by one character, and must report it missing.

## 6. What is needed from main or another seat

Nothing to start. A lock or an answer that cannot be located goes under needs in the status file.
