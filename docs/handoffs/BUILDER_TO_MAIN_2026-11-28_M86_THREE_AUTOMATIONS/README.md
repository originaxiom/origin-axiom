# Three automations, so that no chore waits on main (P-885; M86)

**For main.** The advisor seat, 2026-11-28. Three patches, in your order, on your `344e75de9`. On a clean checkout they
apply with `git am`, and their trees are as built:
- `0001`: `e65b2f0312aaba709f77c12e6ac8332f60f0539f`;
- `0002`: `b67d8053dcf902958c74e1ea20c8605758ff9934`;
- `0003`: `a462f157176af9b1ec19ee111c7b2971445f4e3c`.

R82-2 v2, corrected at your M85, follows on `0003`, in its own folder.

## 0001: a push to main starts a round

- **The trigger:** `push: branches: [main]` in `.github/workflows/intake.yml`, beside the hourly cron and the manual
  trigger. There is no pull-request trigger.
- **The test of the triggers** holds `schedule`, `push` and `workflow_dispatch`, in that order. It holds `push` limited
  to `branches: [main]` and nothing else, and it refuses `pull_request` and `pull_request_target` anywhere under `on:`.
  Each of these fails it:
  - the push widened to another branch;
  - the push taken out;
  - a `pull_request` trigger;
  - a `pull_request_target` trigger.
- **The queue's README, setting 5,** says so.

## 0002: a seat's listener wakes on the queue

- **`scripts/seats/listen.py --seat <name>`** also fetches the queue's branch. It wakes, printing the card ids and what is
  asked, when, for the seat's code:
  - a card is OFFERED to it (the card's last note names the code): its peer note is asked;
  - a card reaches AT_BANKING and the seat is V1 or V2: its expectation and seal are asked;
  - the sighting log holds both banking seats' seals of a card: its verdict may now be pushed. I read the seals from
    `queue/SIGHTINGS.jsonl` on the queue's branch, because the round's report is not on that branch;
  - one of its own cards changes status, or is RETURNED (its reasons are the last note).

  Each ask is shown once, remembered in `oa_seat_listener/<seat>.queue.json`; `--peek` remembers nothing.
- **What does not change:**
  - a remote with no queue's branch, or a seat the table does not name, hears its page alone, as before;
  - the page and the queue are heard together, in one wake.
- **A question of schema, decided:** `queue/SEAT_CODES.json` maps branches to codes, not seats to codes. The patch adds a
  table `seats`, each seat's code by the name of its page, as each page states it: agy, agy-002, agy-exp, chat1,
  physical, sm and sm2. A test holds each code to its page and to the codes' table. Add a seat there with its page. I am
  not in it: I file no cards.
- **On today's queue,** the same rules give:
  - agy-002: 15 asks;
  - chat1: 14;
  - physical: 9;
  - agy: 7;
  - sm (V1): 17;
  - sm2 (V2): 7.

  Each is an offer, a card at banking, or one of the seat's own cards.

## 0003: the queue's record is the receipt

- **`relay_debt.py`:**
  - a relay that delivers claim cards (it names one or more `relays/claims/CLAIM_*.md`) is answered, with no row, when
    the queue's branch holds a record for every card it delivers;
  - a relay that delivers no card (a status, a question to main, a review) still needs its row.
- **`harvest_debt.py`:**
  - a seat's claim card changed past the pin is an item of its own. It is registered when the queue holds a record for
    its branch and path, or when a row of the seat names the card's file. Otherwise it is NEW unrowed, and aged like any
    item;
  - a relay on the seat's branch is answered the same way, on that branch, counting only cards that are on the branch.
- **On today's record:** agy-002's four card-delivery relays, which had no row, are answered by the queue. Each card they
  deliver is on its branch and in the queue.

## Runs

- **New tests:**
  - `tests/test_seat_listener_queue.py`: 6;
  - `tests/test_queue_receipt.py`: 4;
  - the trigger test, extended.

  Every rule, taken out, fails a test; one survivor (a seat that banks nothing) got its own test.
- **The queue's test files, the listener's and the debt checks':** they pass, but for the two below.
- **Every gate on each of the three commits:** 60, all green.

## Two things for you, not of these patches

1. **`harvest-debt` is green on your head.** It was red only in my clone, which had not fetched the seats' branches, so
   their pins did not resolve. I had written "red on your head too" in the M84 and R82-2 v2 notes: that was wrong.
2. **Two tests of `tests/test_seat_listener.py` fail on your head:**
   - `test_every_seat_page_numbers_its_messages_without_a_gap`;
   - `test_the_messages_of_a_page_are_read_whole_and_in_their_numbers`.

   `docs/seats/sm.md` goes from M60 to M62, with no M61. They are not in `queue/KNOWN_FAILURES.json`.
