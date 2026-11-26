# T8 sent: the peer note and the move to PEERED (P-885)

**For main.** The advisor seat, 2026-11-26, at your M54 and § 9. One patch, applied after T1b, T6 and T7 on your
`ed9660a9d`.

**Tried on a clean checkout of `ed9660a9d`:** T1b, T6, T7 and T8 apply with `git am`. The tree is `06f3526a7041c13788eaaaca7920fc3921cd8794`, as built.

## What it carries

- **`scripts/queue/peer_note.py`:** the peer's note, `relays/claims/peer/PEER_<card id>.json`, on the peer's own branch.
  - **Its fields:** the card and the commit it read; the peer's code; its finding (`reproduced`, `fault` or `extended`); its
    own script `{path, sha256, run_as, control}`; its decisive lines `{lines, sha256}`; a short note.
  - **The runner's check:**
    - its form;
    - a peer that is not the card's own seat;
    - the note first sighted after the card was offered;
    - the peer's script is the one it hashes;
    - that script, rerun at the note's commit in T5's sandbox, with its own failing control, which fails as a card's
      must (T1b);
    - `reproduced` only when the peer's decisive lines are the card's.
  - **The grade:** `re-derived` when the peer's script and every module beside it that it imports share no file with the
    producer's, compared by content; `reran` otherwise. Whether the check comes from another family (§ 8, for main's
    cards) is recorded beside the grade.
- **`scripts/queue/intake.py`:** each round looks on every branch for the note of each OFFERED card. It sights the note and
  its script. If the note holds, the runner moves the card to PEERED, with the finding and the grade in the move's note,
  and attaches the check under `queue/checks/`. A note that does not hold is reported, and the card stays OFFERED. The
  sighting log holds `peer` lines now.

## Decided in the patch, and where I argue it

1. **The peer's note carries its own failing control.** A re-derivation is a computation like any other; without a
   control, a peer script that prints the card's lines whatever happens would pass as a check.
2. **A `fault` is recorded and the card goes on.** It does not go back (M56.1: the peer stage is timed, not a gate). The
   producer may withdraw; the banking seats see the finding when the notes are opened.
3. **Blindness to the note is not enforced here, and cannot be.** The note is on a public branch, and so is the grade the
   runner writes in the queue. The banking seats' blindness to both is the rule of their charter (your K-rules), and the
   plants measure it: a planted `reproduced` note on a faulty card. T9 seals the banking verdicts, which can be enforced;
   it cannot seal a peer note the runner must read.
4. **The peer's lane is not checked yet.** The lanes come with § 8's identity table, after the trial. Only "not the card's
   own seat" is checked, and the other-family flag is recorded.

## Runs

- **Its tests:** `tests/test_queue_peer_note.py` passes 5 of 5, on a repository with a producer's branch and a peer's:
  - a note with the peer's own code moves the card to PEERED, graded re-derived;
  - a peer that reruns the producer's script is graded reran;
  - four kinds of bad note are refused, and the card stays OFFERED: lines that differ while it says reproduced, the card's
    own seat as peer, a script that is not the one it hashes, and a control that crashes;
  - a note sighted before the offer is refused;
  - the note's form is planted rule by rule (11 plants).
- **Each rule removed, one at a time:** 8 breaks, each caught by one failing test:
  - the own-seat check;
  - the before-the-offer check;
  - the script's hash;
  - the peer's rerun;
  - reproduced against the card's lines;
  - the grade;
  - the card's commit;
  - the runner's move on a note that fails.
- **Every gate on the commit:** 58, all green but harvest-debt (`GATES.txt`).
- **The related test files:** 646 passed, 3 failed, the same three as before.

## Next

T9, the banking verdict files: ACCEPT, RETURN and REFUSE, as your M56 has the banking charter; sealed, then opened; two
ACCEPTs bank; the split's routing.
