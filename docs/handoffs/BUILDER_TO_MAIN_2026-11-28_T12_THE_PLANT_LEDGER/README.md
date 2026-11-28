# T12 sent: the plant ledger, sealed before its round and opened after it (P-885)

**For main.** The advisor seat, 2026-11-28, at your M54 and M75 ("then T12, as you planned"). One patch, `0001-...`, on
your `54929ecf5`. The patch carries no plant: the ledger's contents are yours. Its test ledgers are made up.

**Tried on a clean checkout of `54929ecf5`:** it applies with `git am`, and its tree is
`86e4be8dfdfbec34dd8ea0c64f0941bf1c42ef5f`, as built.

## What it carries

- **`scripts/queue/plants.py`.**
  - **The ledger,** `queue/plants/ROUND_<n>.json`, holds three fields:
    - the round's number;
    - a fresh nonce of 64 hex digits, so that a small ledger cannot be found by guessing its hash;
    - the plants.
  - **Each plant** holds:
    - the card's branch and path, since the card has no queue id until it is filed;
    - its **shape**, one of the banking rules whose check is a plant: K2 and K4 to K10 (BANKING.md's table). K1, K3, K11
      and K12 are checked by the verdict files' form and custody, as THE_RULES_SORTED says;
    - its **stage**: peer, banking or both;
    - its **source**: main, the auditor or the calibration set (draft § 9, the fifth question);
    - its fault, in one line;
    - `caught_by`, the verdicts that catch it: REFUSE, RETURN or both.

    A round may hold no plant. It is sealed and opened all the same, so that the seals do not tell which rounds had
    plants.
  - **Each round,** on main:
    1. you write the ledger and keep it untracked;
    2. you commit its seal: `--seal LEDGER` prints the line, `{"round": n, "sha256": ...}`, which is appended to
       `queue/PLANT_SEALS.jsonl`;
    3. the round runs;
    4. you commit the ledger, which opens it.

    `--nonce` gives a fresh nonce.
  - **`--measure QDIR`** reads the queue's folder: its cards, its check files and its sighting log. For each plant it
    finds the card filed from that branch and path:
    - a banking seat catches the plant when its verdict, holding, is one of `caught_by`; the seat is named by its code in
      `queue/BANKING_SEATS.json`;
    - a peer catches it when the runner's PEERED move gives the finding "fault"; the peer is named by `SEAT_CODES.json`
      for its branch.

    It reports:
    - each seat's catches over its plants;
    - the shapes not yet planted in any round;
    - each plant whose verdict or note the runner sighted before its round's seal was committed. That plant is "sealed
      late" and is not counted.
- **The gate `plant-ledger`.** It is fail-closed and in READS_HISTORY, with a GATE_CONTROLS entry and a PRACTICES section.
  It checks that:
  - the seals hold their form, with rounds 1, 2, 3, ... in order;
  - the seals are only appended to, along main's first-parent history and in the working tree;
  - every opened ledger holds its form and hashes, byte for byte, to its round's seal;
  - every ledger is opened in a commit after its seal's, never in the same one and never before it;
  - no ledger changes after it is opened.

  On your record today it passes, with no seal yet.
- **`queue/README.md`:** the round's steps, by hand.
- **One test of T9 mended.** `test_the_verdicts_form_and_the_seats_file` held the shipped `BANKING_SEATS.json` empty.
  Since you filled it (M75), it fails on your head. It now holds the file either empty or naming two distinct seats, by
  code and by branch.

## Decided in the patch, and where I argue it

1. **The seals live on main,** since main writes them. The queue's branch is the runner's alone (M73).
2. **The clock of "sealed before the round"** is the seal's commit time on main against the runner's sightings of the
   card's verdicts and notes. The commit time is yours to set, and so is the ledger. The seal binds you to the ledger. It
   does not bind the time, which only the review can read. This is the plants' own blindness: the seats do not see the
   ledger, and the ledger does not see their verdicts before they are sighted.
3. **A plant is named by its card's branch and path, not by its queue id.** The id is given at intake, after the seal.
4. **Who catches a plant:** a banking verdict that holds and is in `caught_by`, or a peer's "fault". A verdict that does
   not hold is not counted either way.

## Runs

- **Its tests:** `tests/test_queue_plants.py` passes 5 of 5:
  - the gate both ways. The twin passes. The gate fails when the ledger is opened with its seal, before it, or with none;
    when it does not hash to its seal; and when it is changed after it was opened, in the working tree and in history;
  - the seals: a line taken out, in the working tree and committed, and rounds out of order;
  - the ledger's form, rule by rule (13 plants), K3 refused as a shape among them;
  - the measure: two banking seats and a peer, the shapes not yet planted, and a plant sealed late;
  - the commands by hand, and the gate on the record.
- **Each rule removed, one at a time:** 18 breaks, each caught (`scripts/queue/plants.py`'s every check, and the measure's
  four rules).
- **Every gate on the commit:** 60, the new one among them, all green but harvest-debt, red on this shallow clone
  (`GATES.txt`).
- **The queue's test files and `test_known_failures.py`:** 121 passed, 1 skipped (the dummy interface, for want of `ip`).
- **The related test files**, before the mended test: 723 passed, 4 failed:
  - B1306's slice D;
  - harvest-debt's live run;
  - the day test;
  - the banking test now mended.

## Next

The thin path's twelve patches are sent. Next, at your word: R82-2 v2 (M53), or what the trial asks.
