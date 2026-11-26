# The framework, draft 1 — free production, a mechanical intake, a peer stage, two banking seats, main as supervisor (P-885)

Main, 2026-11-26. **The author agreed this design on 2026-11-26** (draft 0 is in git's history at `13e2f681f`). Draft 0's six
open questions are now decided, five by the author's agreement and one left to the advisor's proposal (§ 5). A peer stage
was added at the author's question. The build order is fixed, and the listening line waits for it (§ 6).

## Why (main's reading of the last month, 2026-11-26)

- **Inflow outran main's reading.** Main registered more than it verified. Deliveries went unseen: the SM seat's fifteen
  commits, and agy-002's lane reading promised in M53.
- **The gates grew while landings skipped the full suite.** The suite went red unseen.
- **Speed lowered quality.** Real faults were found in all eight arcs read at Review 86 and in eight of ten at Review 87.
- **The direction changed often, and no decisive target was set.**
- **The author's correction of the first cure:** main issuing the cards would make main the bottleneck and the censor.

## 1. The path of a result

```
producer (any seat, free)  ->  intake (mechanical)  ->  peer stage (default, timed)  ->  banking (two seats, blind)  ->  record
                                   |                         |                               |
                                   v                         v                               v
                        fail: back to the seat     fault: back to the producer     RETURN / REFUSE / split
                                   |
                                   v
                        pass: REPRODUCED (no seat needed)
```

## 2. The roles

1. **Producers: any seat, main included.**
   - Each works on anything, on its own branch; no card from main is needed. Production is never throttled.
   - To bear on the record, a result is filed as a claim card (docs/CLAIM_CARD.md, unchanged in form).
2. **The intake: mechanical, running without any seat.** An intake runner reads every seat branch for new claim cards and
   checks each one:
   - **custody:** the script and the expectations were committed before the output;
   - **reproduction:** the decisive script reruns in a sandbox to its sealed output hash;
   - **the firewall:** no comparison with data, and Standard-Model-shaped pass/fail cells flagged;
   - **the form:** every field filled; imports named; "what would make it fail" present;
   - **the record check:** the topic sweep, the retraction sweep and the already-banked check are run by the runner, and
     their output is attached to the card.

   A card that fails goes back to its seat, with the gate's reason written to the seat's page. A card that passes is graded
   **REPRODUCED** and parked in the queue with an id and a status. No seat does this step.
3. **The peer stage: the default path, not a gate.**
   - A card that passes intake is offered to the frontier seats. A seat **from a different lane than the producer** takes it,
     reruns or re-derives it, and attaches a peer note: reproduced, a fault found, or extended. Both seats are credited.
   - A fault found by the peer sends the card back to the producer before banking.
   - If no peer takes the card within a fixed number of landings, it goes to banking anyway, marked "no peer check".
   - A card with a peer note moves up the banking queue.
   - Why not a gate: a gate would make every seat's work wait on another seat's time, which moves the bottleneck from main
     to the peers; peers in one lane share framing, so their agreement is not independent and banking must recompute cold
     anyway; pairs that always check each other drift into accepting each other.
4. **Two banking seats (V1, V2): two sessions of main's own model family, separate from main and from the producers.**
   - **Only cards that decide something go to banking:** a card that moves a register item, changes a law-map row, or bears
     on a ruling. The rest stay REPRODUCED, public, with their status.
   - **Cold context.** Each banking seat reads the card, the arcs it cites, the definitions (TERMINOLOGY.md) and the
     intake's attached record check, and nothing else of the record. It recomputes what decides with its own code, not the
     producer's.
   - **Blind.** Each files a verdict before seeing the other's, and before seeing the peer note: ACCEPT; RETURN (with the
     corrections named); or REFUSE (with the counter-computation).
   - **Two ACCEPTs bank: VERIFIED.** The banking seat writes the arc, the lock and the ledger rows through the landing tool,
     crediting the producer and the peer.
   - **A RETURN** goes back to the producer, who may refile. **A split** goes to main.
5. **Main: supervisor and integrator.**
   - Reads the banked stream and keeps the picture: the law map, the synthesis, what the line has found.
   - Arbitrates splits.
   - Proposes the direction to the author.
   - Audits the peer stage and the banking seats by planting faulty cards.
   - Produces like any seat, but its own work goes through the same path. No self-banking.
6. **The advisor seat:** builds and keeps the framework (the intake runner, the queue, the peer stage, the gates). It does
   not verify science, and it does not audit its own build; the auditor does (§ 8).
7. **The auditor seat:** audits what has passed every other seat, main included (§ 8).
8. **The author:** rulings, any look at data, and the seats' assignment. The author starts the two banking seats and the
   auditor, and may ask a new model for audits (§ 8).

## 3. The decisions (agreed by the author, 2026-11-26)

| draft 0's question | decided |
|---|---|
| 1. the banking seats' context | **cold** (§ 2.4). What cold misses, whether a claim is already on the record, contradicted or retracted, is a lookup the intake runs mechanically. The faults in main's arcs were found by readers without main's context (Review 78's ten; B1986's mislabelled mode, found by the web seat) |
| 2. the grades | **REPRODUCED** (intake: the script reruns to its sealed hash) and **VERIFIED** (two blind banking ACCEPTs), kept apart; only deciding cards go to VERIFIED |
| 3. throughput | **two banking seats, no third yet.** A third is added only if the queue of deciding cards keeps growing over several rounds, as measured by the queue, not guessed. A third seat also invites best-of-three voting, which weakens independence |
| 4. the backlog | **not at once.** Frozen as a dated list, public, labelled "unbanked": the 199 inbound relays, about 24 waiting claim cards (agy-002 13, agy-exp 11), the SM seat's 181 rows, the web seat's 1,961 records. Fed in a few per round beside new cards, by what each decides; items nobody cites stay parked with their status |
| 6. main's arcs in the window | **B2011 to B2017 re-queued as the first batch, with plants mixed in.** They were checked by main alone, and their answers are known, so the first run tests the peer stage and the banking seats (do they reproduce the census, the null control, the rate law? do they catch the plants?) before they are trusted on cards whose answer nobody knows. The mends and record work of the window are not re-queued |
| added: a peer check before banking | **the default path, timed, not a gate** (§ 2.3) |

## 4. The discipline (what keeps it honest)

- **One door.** Nothing enters the record as VERIFIED except through the queue and two independent ACCEPTs, main's work
  included.
- **Independence:**
  - a banking seat shares no code with the producer;
  - neither banking seat reads the other's verdict, or the peer note, before filing its own;
  - a peer is from a different lane than the producer.
- **Plants.** A fixed share of the queue is planted faults, in the peer stage and in banking, unknown to the seats. Catch
  rates are measured continuously, so the review no longer needs its own plants. A seat whose rate falls is paused until it
  is read.
- **The peer stage is measured.** Peer verdicts are compared with banking verdicts. If cards with a peer note are refused as
  often as cards without, the peer stage is teaching but not verifying, and the record says so.
- **Limits:**
  - each banking seat holds at most a few items at once;
  - items in the queue age, and an aged item escalates to main;
  - production is never throttled; only banking is ordered.
- **The order of the banking queue:** what the item decides comes first. Does it move one of the 19, or the proof that the
  object cannot fix them, with its count? Then what blocks other work. Then cards with a peer note. Then the rest. Nothing
  is dropped; a parked item has a public status.
- **Few gates, each tested.** Every gate has a planted failing case. A gate that has caught nothing in a month is reviewed
  for retirement. A landing runs the suite on a fresh clone, or the push is refused.
- **The firewall stays.** No comparison with data without the author's approval, enforced at the intake.

## 5. Left to the advisor's proposal

- **The record's surfaces:** which of today's ledgers, views and gates survive, and which the queue replaces (draft 0's
  question 5).
- **The timeout** of the peer stage, in landings, and the **share of plants**.
- **The queue's form:** a file per card under one directory with a status field, or one register; the advisor proposes.

## 6. The build order (agreed by the author, 2026-11-26)

1. Draft 1 to the advisor seat (this message).
2. The advisor's critique and build plan; main reads and lands them. Main also reads the advisor's R81-3 and R82-2 patches
   line by line.
3. The advisor builds, in this order: the intake runner and the queue; the peer stage; the banking verdict files; the role
   charters (§ 7); the audit ledger, the grades' badges and the seats' identity fields (§ 8). Each patch comes with a test
   that must fail when the patch is broken.
4. The author starts the two banking seats and the auditor, each hired against its charter.
5. The trial run: B2011 to B2017 and planted faulty cards through the whole path, intake to peer stage to banking.
6. Then the listening line resumes, through the new path.

Meanwhile the frontier seats keep producing; their cards wait on the frozen list until the intake exists. Only main's own
research line pauses.

## 7. The role charters (raised by the author, 2026-11-26)

So that a seat hired for a role knows what is expected of it, without being boxed in.

- **One page per role** under `docs/roles/`:
  - the producer;
  - the peer;
  - the banking seat;
  - the supervisor (main);
  - the builder (the advisor);
  - and the author's page, listing what only the author does.
- **Each page states:**
  - what the role receives and what it delivers;
  - its rules and its freedoms;
  - how it is measured;
  - the hiring brief, the first message a new seat in that role gets.
- **The rule against boxing seats in:** a rule on a role's page must be one the framework checks, by the intake, a gate or a
  plant. Anything nobody checks goes under "advice", which the seat may ignore.
- **The producer's page carries only the door's rules:** the claim card's form, custody, and the firewall. Nothing on what to
  work on, which methods, or which framing. The page lists the freedoms first.
- **Strictness goes where independence needs it.** The banking seat's page has the most rules (cold, blind, its own code,
  limits), because its job is to say no.
- **WORKING_RULES.md binds every seat today.** The advisor sorts each of its rules into one of three kinds:
  - a door rule, binding every role;
  - a rule for one role only;
  - advice.

  A producer keeps only the door rules.
- **Rules are reviewed like gates.** A rule that has caught nothing is reviewed for retirement.

## What main asks of the advisor seat

- **A critique of draft 1:** its failure modes, and where a seat could game it (the peer stage especially: pairs that trade
  ACCEPTs, a peer note written without a rerun, a timeout gamed by never taking cards).
- **What to reuse and what to retire:** seat_intake.py, harvest_debt.py, CLAIM_CARD.md, BANKING_PROTOCOL.md, the landing
  tool and the gates.
- **A build plan as patch series** in the order of § 6.3, with § 5's proposals.

## 8. The auditor, the AUDITED grade and the seats' identity (agreed by the author, 2026-11-26)

### The auditor seat

- **What it audits:**
  - a sample of each round's VERIFIED cards, weighted toward the deciding ones;
  - whether the process was followed: custody, blindness, the plants, the timeouts;
  - the framework itself.
- **It takes over the reviews main runs now** (the review-due gate's reviews).
- **It works cold,** like the banking seats.
- **Its findings go to a public audit ledger,** which the author reads directly. Main routes the fixes top-down. Only the
  auditor closes a finding, after re-checking the fix. Otherwise main would be filtering findings about its own work.
- **It gets planted faults from main,** and its catch rate is measured.

### The AUDITED grade

- **The grades:** REPRODUCED (intake), then VERIFIED (two blind banking ACCEPTs), then AUDITED.
- **An audit by a new model, at the author's request, gives a badge that names its scope:**
  - the model's code and its effort;
  - the commit audited and the date;
  - the checks run;
  - the model's catch rate on the calibration set.
- **Calibration first.** Before a new model's badges count, it audits a set of cards with known faults.
- **Badges add up; none replaces another.** A badge lapses when the card changes after it.

### The seats' identity

- **Each seat's page carries:** its role, its model code, its effort, who started it and when, and its branch. Every card,
  peer note, verdict and finding carries the seat's id.
- **The author records model and effort at hire.** A seat's own statement is checked against that record, since a seat may
  not know its own effort setting.
- **Tracked files carry a neutral code** (family, version, effort). The mapping to real names is kept in a local, untracked
  file under `audit/`, so the attribution gate stands.
- **The independence rules become checkable:**
  - a peer from another lane;
  - **a card produced by main needs at least one check from another model family before it is VERIFIED,** by the peer
    stage or the auditor. The banking seats share main's family, so without this rule main's cards would be checked by its
    family alone.

## 9. The advisor's critique, decided (approved by the author, 2026-11-26)

The advisor seat's answer to M49 to M51 (its branch, `docs/handoffs/BUILDER_TO_MAIN_2026-11-26_M49_TO_M51_CRITIQUE_AND_BUILD_PLAN/`,
@ `aa384d2ae`) is adopted, with the decisions below. Where this section and §§ 1 to 8 differ, this section holds.

### Where the intake runner runs

- **GitHub Actions on the repository, on standard GitHub-hosted runners only.** These are free on a public repository;
  larger runners are billed and are never used. The author sets the Actions spending budget to $0, so the worst case is a
  job that does not run, never a charge.
- **Two jobs.**
  - The job that runs seat code has read-only permissions and no secrets.
  - A separate job writes the runner's results, the queue's files, to the queue's own branch.
  - Main is protected so the runner's token cannot push to it.
- **The sighting log is committed to the queue's branch.** Run logs are public but kept about 90 days, so they do not serve.
- **A manual trigger is kept beside the schedule.** The same code runs by hand on the author's machine as the fallback. If
  Actions is down, the queue waits and production does not stop.
- **Modest use:** the runner reruns the repository's own scripts, as GitHub's terms allow, with a cap of about 30 minutes
  per card. A card needing more, or needing sage, is marked **heavy** and rerun by the same code on the author's machine,
  when the author chooses; the banking seats recompute it in any case.

### The advisor's six questions

1. **Where the runner runs:** as above.
2. **The four claim-card fields** (the runner's id, the seat's code, the failing control as a command, the decisive output
   lines): **adopted.**
3. **Peers are offered cards by rotation** instead of choosing them: **adopted.** A seat may decline; its rate of declines
   is shown, not penalised. Production stays free.
4. **A split on main's own card goes to the auditor, then to the author:** **adopted.**
5. **Plants come from three sources:** the calibration set of real faults, the auditor and main. **Adopted.** The auditor's
   own plants come from main and the calibration set.
6. **A baseline of known failures that may only shrink:** **adopted.** Each entry carries a register row; a landing that
   adds a failure or a red gate is refused.

### The advisor's other proposals: adopted

- **The intake:**
  - custody from the runner's sighting log, and a rewritten branch returns the card;
  - the failing control must fail;
  - normalised decisive output lines;
  - the record check on the runner's own terms;
  - "deciding" computed by the runner;
  - a deciding card's REPRODUCED-only premises banked with it;
  - the firewall as a flag to the author;
  - a refiled card linked to its history.
- **The peer stage:**
  - the peer note graded "reran" or "re-derived", and only a re-derived note moves a card up;
  - the timeout of 72 hours and one re-offer;
  - the cap on one peer's share of one producer's cards;
  - counts shown beside every rate.
- **Banking:**
  - verdicts sealed first, then opened;
  - the peer note sealed until both banking seals are in;
  - the same banking seat gets its own RETURN back with the refiled card;
  - the landing tool, tracked, as the single writer of arcs, locks, ledger rows and the log pair.
- **Plants and identity:**
  - plants under real producers' ids, arranged by the author, in a plant ledger sealed per round;
  - the calibration set held as hashes;
  - badges covering the card's, the script's and the cited verdict lines' hashes;
  - neutral codes checked against the scoreboard's pattern;
  - a tracked code table, with the real names kept by the author outside the repository;
  - "waiting for another family" for main's cards;
  - audit findings that main routes late escalate to the author.
- **Surfaces:**
  - a file per card under `queue/cards/`, with a generated view;
  - the reuse and retire table;
  - no gate retired before a count of what it caught.

### Two changes by main

- **Allowed packages.** The trial batch B2011 to B2017 uses python-flint, and sage with GAP. The allowed list adds them at
  pinned versions, and the runner records the version of every package used.
- **A thin path first.** Before all 31 patches, the thinnest cut that carries B2011 to B2017 and the four plants from intake
  to landing. The advisor proposes the cut. Main's sketch:
  - the queue's schema; discovery; the form check; custody; the sandboxed rerun with its failing control; the workflow;
  - the peer note's schema, with offers made by hand in the trial;
  - the banking verdicts, sealed; two ACCEPTs; the known-failures baseline; the landing tool; the plant ledger;
  - the producer's and the banking seat's charters;
  - the seat code on cards.

  The trial then runs, and the rest is built after it, in the order of the advisor's plan. The advisor's stop rule applies:
  if the path costs more than it catches, it is simplified before it is trusted.
