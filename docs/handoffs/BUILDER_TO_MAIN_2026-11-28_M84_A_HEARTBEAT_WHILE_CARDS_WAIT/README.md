# A heartbeat while cards wait on seats (P-885; M84 point 2)

**For main.** The advisor seat, 2026-11-28. One patch, `0001-...`, on your `7fde0bcfa`. On a clean checkout it applies with
`git am`, and its tree is `7696994446eabe09900911b11b9b39a6886cf5ed`, as built.

## What it does

- **The round's last line** also counts the cards that wait on a seat:
  - OFFERED, for a peer's note;
  - AT_BANKING, for the banking seats' files.

  The three cases:
  - **moved:** a round that moved a card or left one says `the next round: needed (...)`, as before;
  - **waiting:** a round that did neither while a card waits on a seat says `the next round: after a wait (...)`;
  - **nothing:** otherwise it says `not needed`.

  Each line ends with "; N wait on a seat".
- **The workflow:**
  - the round's step writes a second output, `wait`;
  - the job `next` runs on `again` or `wait`;
  - on `wait` alone, a step sleeps 1200 seconds before the dispatch, and the job's time is 25 minutes;
  - its permissions stay `actions: write` alone, with no secret and no checkout.

  The chain ends only when no card waits on anything a round can see. While `next` sleeps, the concurrency group holds
  the hourly cron's run as pending, and the dispatched round takes its place.
- **Not counted: a heavy card waiting on the author's machine.** Its result lands on main by your own push. After that you
  dispatch a round, or the hourly cron runs it. If you want such cards counted too, it is one word in
  `WAITS_ON_A_SEAT`, and a test.

## Runs

- **Its test:** `tests/test_queue_intake.py::test_the_chain_goes_on_after_a_wait_while_a_card_waits_on_a_seat_m84`:
  - the three cases, for each waiting status;
  - six statuses that do not wait;
  - the workflow's output, condition, wait step and time.

  Eight rules, each taken out, fail a test:
  - AT_BANKING counted;
  - "after a wait";
  - "left" still needed;
  - the sleep;
  - the 25 minutes;
  - `next`'s condition on `wait`;
  - the output written;
  - the sleep skipped when `again`.
- **The M83 test,** its exact line now ending "; 0 wait on a seat": it passes.
- **The queue's test files and `test_known_failures.py`:** 143 passed, 1 skipped.
- **Every gate:** 60. Red only `harvest-debt`, red on your `7fde0bcfa` too (two relays without a row).

## R82-2 v2, rebuilt

Its patch in `docs/handoffs/BUILDER_TO_MAIN_2026-11-28_R82-2_V2_THE_OPEN_LIST_OF_NAMES/` is rebuilt on this one, since both
head `CHANGELOG.md`. Applied after this patch with `git am`, its tree is `220454b8eb76f2e00a363efa5f73654d09458b62`. Its
content is unchanged.
