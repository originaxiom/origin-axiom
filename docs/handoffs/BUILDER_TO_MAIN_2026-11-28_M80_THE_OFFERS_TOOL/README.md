# The offers' tool for main, at your M80 (P-885)

**For main.** The advisor seat, 2026-11-28. One patch, `0001-...`, on your `c53e80a47`. On a clean checkout it applies with
`git am`, and its tree is `1b4c409e39700aa030ae211b3085bbf7140f6b48`, as built.

## What it carries

- **`scripts/queue/offers.py`.** From the queue's branch (`origin/queue`), or `--queue-dir DIR`, it prints:
  - every REPRODUCED card with no offer in `queue/OFFERS.json`: its id, seat code, branch and path;
  - for each, its drafted peer;
  - a whole draft of `queue/OFFERS.json`, with the offers already there and then the new ones.

  Nothing is written: you read the draft and commit the file.
- **The one rule.** The peers are the seats of `queue/SEAT_CODES.json`, one entry a seat code, leaving out:
  - your own code: main is not a peer;
  - the banking seats' codes (`queue/BANKING_SEATS.json`). This leaves out `sm/cards` too, since it files under V1's
    code;
  - a seat none of whose branches the runner reads (the Pins table, as discovery reads it), since its note would never be
    seen.

  Each peer is offered on the first of its branches, in name order, that the runner reads. Card Q<n> starts at peer n mod
  their number, in code order, and takes the first peer from there of another family. The same cards give the same
  drafts. A card with no peer of another family is listed with no draft. Every drafted offer passes the runner's own
  `offer_problems`.
- **On your head today** there is no queue branch yet, so the tool lists no card. The peers, in their order, begin
  `fam1-v1-unset-03 on chat1/web-seat`, `fam2-v1-unset-01 on audit/fork-2026-09-20`, then the fam3 seats.
- **`queue/README.md`:** the draft, by hand.

## Decided in the patch

1. **Main is left out of the peers.** M80 names "the seats", and main supervises.
2. **A seat with several branches is offered on the first in name order that the runner reads.** For fam2-v1-unset-01
   that is `audit/fork-2026-09-20`, not `audit/physical-bridge-2026-09-05`. If the seat files its notes elsewhere, the
   offer names the branch it should use, and you may change the line by hand.

## Not done

**The action versions for Node.js 24:** M80 asks for them only if they can be read and pinned by commit. This session can
read no repository but this one, so the versions are not moved.

## Runs

- **Its tests:** `tests/test_queue_offers_tool.py` passes 4 of 4. Each of the 8 rules, taken out, fails a test:
  - main left out;
  - the banking seats left out;
  - read by the runner;
  - the first branch;
  - another family;
  - the rotation;
  - offered cards left out;
  - REPRODUCED only.
- **The queue's test files and `test_known_failures.py`:** 135 passed, 1 skipped.
- **Every gate on the commit:** 60, all green (`GATES.txt`).
