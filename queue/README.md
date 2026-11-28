# The queue

The framework's queue of claim cards (draft 1 of `docs/handoffs/MAIN_TO_ADVISOR_2026-11-26_THE_FRAMEWORK/DRAFT.md`, § 9;
register row P-885). Each card the intake has seen is one file, `queue/cards/Q<nnnn>.json`, written by the intake runner
to the queue's own branch; main holds the schema and the gate that reads it.

- The schema and its command: `scripts/queue/queue_schema.py` (run it with `--ref <the queue's branch>` to read the cards
  there without a checkout).
- The gate: `queue-schema`, on every card in this checkout's `queue/cards/`.

A card's history is append-only. A returned card is refiled as a new card that names the old one.

## The runner (the thin path's patch T7)

- **One round, by hand:** `python3 scripts/queue/intake.py --queue-dir <the queue/ folder of the queue's branch> [--write]`.
  On a machine where the network cannot be cut by a namespace, add `--allow-static-guard`, by the author's choice only.
- **On the workflow:** `.github/workflows/intake.yml`, every hour (every three hours until 2026-11-28) and by hand (Actions, "intake", "Run workflow").
  The job that runs seat code reads only and holds no secret; a second job checks the round's queue and pushes it to the
  queue's branch, `queue`.

## A heavy card (main's M83)

A card that needs sage or GAP, or declares itself heavy, is not rerun on the workflow: each round says it waits for the
author's machine. There, main runs, from main's checkout with the queue's folder at hand:

    python3 scripts/queue/rerun.py --heavy-result Q0006 --queue-dir <the queue/ folder of the queue's branch>

It reruns the card at its sealed commit with no wrap, by the author's choice, with the caller's PATH (set it so that
`sage`, `gap` and a `python3` with python-flint are found), and writes `queue/heavy/Q0006.json`. Main commits that file
on main. The next round checks it against the card (its id, branch, path and sealed commit, the decisive script and its
hash, the decisive lines as the card states them, a control that exited 1) and moves the card to REPRODUCED, or to
RETURNED_AT_INTAKE with the reasons. A card of another seat is rerun there only with `--author-allows`, the author's word
for that card.

## The offers to peers (main's M79)

The queue's branch is the runner's alone, so main offers a card to a peer in its own file on main, `queue/OFFERS.json`:
each offer names the card by its branch and its path (its queue id is given at intake) and the peer by its seat code and
branch. Each round the runner moves a REPRODUCED card whose offer holds to OFFERED, its note naming the peer. An offer to
the card's own seat or its own family (the code's first part), or to a branch that is not the code's in
`queue/SEAT_CODES.json`, is refused and reported. A card with no offer stays REPRODUCED, and the report says so. Only the
offered peer's note is taken; another seat's note is refused.

**The draft, by one rule** (main's M80, M81): `python3 scripts/queue/offers.py [--all]` prints every REPRODUCED card on the
queue's branch with no offer yet (with `--all`, every FILED card too, offered ahead of its rerun), and a whole draft of
`queue/OFFERS.json`. The peers are the codes under `"peers"` in that file, in their order, each on its live branch: of
the Pins table's branches for its code, the one that moved last; a seat whose live branch has not moved in 14 days is
left out, and said. Each card takes the next peer of another family in a rotation carried from card to card in queue
order, a card offered already moving it where it stands; main's own cards go to the first peer of another family. Main reads the draft and commits the
file itself.

**The rounds dispatch the next** (main's M83): a round that moved a card or left one for later dispatches the next
round itself, by a job that holds only the right to dispatch; a round with nothing to do ends the chain, and the hourly
cron stays as the fallback.

## The settings the author makes (once, in the repository's settings on GitHub)

1. **Spending:** set the account's budget for Actions to $0, so a run that would cost money does not run. Standard runners
   on a public repository are free; the workflow names only `ubuntu-latest`.
2. **Workflow permissions** (Settings, Actions, General): "Read repository contents and packages permissions". No job asks
   for more: the record job pushes with the queue's deploy key (setting 4), not with the workflow's token.
3. **Main is protected from the runner's token** (Settings, Rules, Rulesets, a branch ruleset on `main`): restrict updates
   and deletions, and block force pushes, with the repository's admin role as the only bypass. The workflow's token acts as
   the Actions bot, which is not an admin, and it reads only, so it cannot push to main.
4. **The queue's branch is written by one key alone** (main's M73; a second ruleset, on `queue`):
   - block force pushes; restrict deletions; **restrict updates**, with the queue's deploy key as the **only** bypass, and
     no role, admin included. A rewritten branch would carry no trace (main's M58), and a record anyone could append to
     would carry a VERIFIED no runner made (main's M72).
   - The author's steps:
     1. make a key pair, with no passphrase (`ssh-keygen -t ed25519 -N "" -f queue_deploy_key`);
     2. add the public key (`queue_deploy_key.pub`) as a deploy key of the repository, with write access (Settings, Deploy
        keys);
     3. add the private key as the repository secret `QUEUE_DEPLOY_KEY` (Settings, Secrets and variables, Actions), then
        delete the local copy;
     4. add that deploy key to the `queue` ruleset's bypass list, and nothing else.
   - Only the record job names the secret; the round job, which runs seat code, never sees it.
   - **The record job checks the ruleset after its push.** It reads the rules GitHub applies to `queue` (the REST call
     "get rules for a branch", which the job's read-only token may make) and fails, saying so, unless updates, deletions
     and force pushes are all restricted there. It cannot read the bypass list with that token, so a bypass given to a
     role is not seen: check the list by hand once. A dry `git push` cannot test the rule: a dry run never reaches the
     server's rules.
5. **Fork pull requests:** the workflow has no pull-request trigger, so no fork's code runs in it. Keep it that way.
6. **After the first round,** check that the run's log reads "the network guard: sudo unshare -n -m -i -p, as nobody". A round
   that cannot make that sandbox runs no seat code (every rerun is HEAVY); it is never to be given `--allow-static-guard`
   on the workflow.
7. **A heavy rerun on the author's machine** runs sage, and for main's B2016 wrapper also a `python3` on the PATH that has
   python-flint (main's M65): set the PATH so first. There the author may run with `--allow-static-guard`, by choice.
8. **Switching the runner on** (ADDED 2026-11-27 by main, at landing): the workflow's `round` job runs only when the
   repository variable `INTAKE_ENABLED` is `true` (Settings, Secrets and variables, Actions, Variables). Set it once
   settings 1 to 4 are made; until then a scheduled run skips both jobs and costs nothing.

## The landing (the thin path's patch T11)

A card the queue holds VERIFIED is landed on main by `scripts/queue/land.py` alone, the single writer of its arc, its lock,
its harvest row and the log pair. It holds a lock, so that one landing runs at a time, and makes a fresh clone of main. It
takes the arc's number and the harvest row's at landing, writes them, commits, regenerates the views, and runs every gate
and the full suite with `-rfE` against `queue/KNOWN_FAILURES.json`. It never pushes: a landing that holds ends with the
command that pushes it.

    python3 scripts/queue/land.py --landing DIR        # DIR: LANDING.json, arc/, lock.py, changelog.md, progress.md

docs/CAMPAIGN_STATUS.md's LATEST line and the surfaces a reader forms a picture from (BANKING_PROTOCOL Part I C) stay
main's.

## The plant ledger (the thin path's patch T12)

Main's alone, and not read by any seat before it is opened. **Its round is a batch of cards, not one run of the runner**
(the runs above, every hour, are a different round): a ledger is opened only when every card it names has ended,
its status final, and round n's ledger is opened before round n + 1 is sealed (main's M76). Each round, main writes `queue/plants/ROUND_<n>.json` and keeps
it untracked, commits its seal (`python3 scripts/queue/plants.py --seal queue/plants/ROUND_<n>.json`, a line appended to
`queue/PLANT_SEALS.jsonl`), lets the round run, and then commits the ledger, which opens it. A fresh nonce for each ledger:
`plants.py --nonce`. The catch rates: `plants.py --measure <the queue/ folder of the queue's branch>`. The gate
`plant-ledger` checks the seals and the opened ledgers.
