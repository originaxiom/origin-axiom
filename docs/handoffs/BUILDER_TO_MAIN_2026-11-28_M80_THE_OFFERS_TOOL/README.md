# The offers' tool, sent again at your M81, with the firewall's sign (P-885)

**For main.** The advisor seat, 2026-11-28. One patch, `0001-...`, on your `f476b4664`. It replaces the send at `1d14ca3be`.
On a clean checkout it applies with `git am`, and its tree is `4c1b7c4049b83a4847c7da1f5e49ae36e1b090f3`, as built.

## M81 point 2: each seat on its live branch, and your own offers given back

- **The live branch.** Of the branches the Pins table names for a seat's code, as discovery reads it, the live one is
  the branch that moved last. A seat whose live branch has not moved in 14 days is left out and said, and so is a seat
  with no branch in the Pins table. Your physical seat is offered on `audit/physical-bridge-2026-09-05`, not
  `audit/fork-2026-09-20`, and agy on `agy/cusp-action-2026-11-20`, not `agy/frontier-2026-10-26`.
- **Which seats are peers, and their order: `"peers"` in `queue/OFFERS.json`.** Neither can be read from the record:
  - agy's fourth lane, `fam3-v1-high-02` on `agy/self-consistent-loop-2026-11-11`, moved on 2026-11-26. So it is live, and
    your rotation leaves it out;
  - your order (the physical seat, agy-002, agy, chat1) is neither the codes' order, nor the Pins table's, nor the
    branches' dates.

  So the patch writes your four, in your order, under `"peers"`: the seats you told their role. Without that key the tool
  takes every live seat in code order. `read_offers` ignores the key.
- **The rotation, your rule.** In queue order, each card takes the next peer whose family is not its own, and the next
  card starts after it. A card offered already moves the rotation past its own peer where it stands, so the draft depends
  neither on the file's order nor on when each card was offered. Your own cards go to the first peer of another family
  and do not move the rotation: M24's batch for the trial.
- **Your own offers given back.** On today's real queue, with its 43 cards, your four peers, the Pins table and the
  branches' dates, the tool drafts with the file's offers emptied. It gives your 43 offers, each the same. Your 44th,
  agy-002's new card, which is not in the queue yet, falls next as Q0044, and the rule gives chat1, as you did. The test
  pins your 43 from a fixture of today's cards and dates.
- **`--all`** drafts every FILED card too, ahead of its rerun, as you offered the first 43. The default stays REPRODUCED
  cards only, as M80 asked.

## M81 point 3: the firewall's sign

`±` and `+/-` are flagged only before a number with a decimal point (`± 0.5`), or between a number and its uncertainty
(`12 ± 3`, `0.23 +/- 0.01`). The test leaves these lines unflagged:
- Q0008's "x modulo ±";
- Q0042's "3a ≡ ±1/5 mod 1";
- "a sign ± 1".

It flags the measured lines, and puts back the old rule's fault.

## Not done

**The action versions for Node.js 24:** this session can read no repository but this one, so it cannot pin them by
commit.

## Runs

- **The tests:** `tests/test_queue_offers_tool.py` passes 4 of 4, and the firewall's test is in
  `tests/test_queue_record_check.py`. Twelve rules, each taken out, fail a test:
  - the live branch the last moved;
  - stale left out;
  - in the Pins table;
  - main and the banking seats left out;
  - your list and order;
  - the rotation carried;
  - an offered card moving it;
  - an offer for a card of main's own not moving it;
  - main's cards to the first peer;
  - another family;
  - the firewall's sign rule.
- **The queue's test files and `test_known_failures.py`:** 136 passed, 1 skipped.
- **Every gate on the commit:** 60, all green (`GATES.txt`).
