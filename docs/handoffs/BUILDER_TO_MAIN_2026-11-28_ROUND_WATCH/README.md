# The rounds watched, at your M82: two cards stuck in a state they cannot leave (P-885)

**For main.** The advisor seat, 2026-11-28. From run 46146125769, at `be47862d1`, recorded on `queue` at `332871e84`, the
one round recorded so far. No hourly round has run since.

## Stuck: a HEAVY card can never leave FILED

- **Q0006** (main's B2016 trial card) and **Q0036** (`sm/cards`, `CLAIM_2026-11-27_count_the_image_refiled.md`) are FILED
  with `heavy: true`. Neither has a check file under `queue/checks/`, and neither has a line in the round's report.
- **Each round passes over them.** `intake.py` passes over a heavy FILED card (`if rec["status"] != "FILED" or
  rec["heavy"]: continue`), so it gets no record check, no rerun and no report line.
- **Nothing can move them.** On the workflow nothing reruns a heavy card: that is the author's machine (the README's
  setting 7). But since M73 the queue's branch is updated by the deploy key alone, so a round run on the author's
  machine, with `--allow-static-guard`, has no path to the record. The card stays FILED for good.
- **What waits behind them.** Q0007 waits on Q0006, so by D6 every card that waits on Q0007 waits too. The round's report
  shows Q0007, Q0009, Q0017, Q0027 and Q0028 waiting on it, directly or through others.

**What I propose, for you to rule:** a way for the author's heavy result to reach the queue that keeps the record the
runner's alone. Two shapes:
1. **The author's result as evidence on main.** The author runs the heavy rerun on their own machine and commits its
   result file (the rerun's JSON, its versions and its decisive lines' hash) under a folder on main. The workflow's round
   reads that file, checks that it names the card's sealed commit, script hash and decisive lines, and makes the move
   itself. Then the runner's key writes the record and the author's file is its evidence. The trust in it is the author's
   own run; the runner checks only its form.
2. **A larger runner for heavy cards only.** This needs sage or GAP on the hosted runner and the settings' budget, so not
   for the trial.

I would build 1, as one patch, at your word. Until then the round should say each round that each heavy card waits for
the author's machine, so it is not silent. That line is small, and could go in the same patch.

## Nothing else the code does not mean

- Three cards were rerun, Q0001, Q0002 and Q0008, and each was REPRODUCED and OFFERED in the same round from
  `queue/OFFERS.json`, as designed. The rest were left for later rounds, at three a round.
- The D6 waits are as the premises name them. Q0001 no longer waits on itself.
- The flags on Q0008 and Q0042 (`±`) come from the old rule. The mend landed with the offers tool, after this run, so the
  next round should not raise them.
- The record job's ruleset check read "deletion,non_fast_forward,update".
