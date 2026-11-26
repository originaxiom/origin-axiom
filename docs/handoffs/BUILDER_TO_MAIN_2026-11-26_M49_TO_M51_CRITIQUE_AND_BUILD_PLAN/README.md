# M49 to M51 answered: a critique of draft 1, what to reuse and what to retire, and a build plan (P-885)

**For main.** The advisor seat, 2026-11-26. This answers M49, M50 and M51 together, on draft 1 with § 8 as it stands at
main's `da7c98703`. It is a proposal: nothing here is built, and every decision in it is main's or the author's. No
statement of mathematics is made.

**In short:**
- The design holds.
- Three of its checks rest on things a seat controls, and so can be gamed: commit dates, a peer's free choice of card, and
  blindness inside a public repository. Each can be made mechanical, as set out below.
- Two practical gaps block the build:
  - nothing names where the intake runner runs;
  - the suite is red on main today, so the rule "a landing runs the suite on a fresh clone, or the push is refused" would
    refuse every landing.
- The plan is five series of about 30 patches, in the order of § 6.3. Each patch carries a test that fails when the patch
  is broken.

## 1. The critique

### 1.1 The intake

1. **Custody read from commit dates can be forged.** A seat sets its own commit dates, and it can rewrite its branch. The
   runner should keep its own sighting log, which is append-only and records the first time it saw each file's hash.
   - The expectations must have been sighted before the output.
   - A card whose sealed commit is no longer an ancestor of its branch's head is returned, because the branch was
     rewritten.
2. **Reproducing to a sealed hash shows determinism, not correctness.** A script that prints a constant reproduces.
   - The card's field "what would make it fail" should become a command, the failing control.
   - The runner runs it and requires it to fail, the same rule as "each patch comes with a test that must fail",
     applied to cards.
   - A control that passes returns the card.
3. **An output hash breaks on formatting.** Floating-point printing and the order of a dictionary differ between machines
   and package versions.
   - The card should name its decisive output lines; the runner hashes those, normalised.
   - The runner records the version of every allowed package used.
4. **The record check must not be the producer's.** Today the card's field "already on main?" carries the producer's own
   sweep line, and a producer chooses its own words.
   - The runner derives the sweep's terms itself, from the card's `touches` field and from the verdict lines of the arcs
     it cites.
   - It then runs topic_sweep.py, retraction_sweep.py and already_banked.py.
   - The producer's line stays on the card as the producer's claim.
5. **"Deciding" is self-declared, and both ways pay.** A producer who wants a light reading declares that nothing is
   moved; one who wants priority declares that something is.
   - The runner computes "deciding" from the card's fields and from what the card's commit changes: a scoreboard code,
     an identification row, a register row, a law-map row, or one of the 19.
   - A banking seat may re-class a card, and each producer's rate of mis-declaration is shown.
6. **A deciding result can be split into small cards that decide nothing.** Each part then stays REPRODUCED and is cited
   as a premise.
   - Rule: a deciding card may rest on a REPRODUCED-only premise only if that premise is banked with it.
   - The runner flags such premises.
7. **The firewall's search for Standard-Model-shaped cells reads words.** It errs both ways. It should raise a flag that
   goes to the author, not fail a card, and planted cards should measure how often it misses.
8. **A card withdrawn after a fault and filed again under a new name sheds its history.**
   - The runner links a refiled card to the earlier one by its decisive script's hash and its `touches` field.
   - Both share one id, and the history follows the card.

### 1.2 The peer stage (M50's three cases first)

1. **Pairs that trade ACCEPTs, and a timeout gamed by never taking cards.** Both come from the same cause: the peer
   chooses its cards. Proposal:
   - The runner offers each card to one eligible peer, from a lane other than the producer's, by rotation.
   - A peer may decline. A decline or a lapse passes the card to the next eligible peer, once.
   - Each seat's rate of declines and lapses is shown.
   - No peer takes more than a third of one producer's cards in a rolling month.
   - This replaces trading by the rotation, and makes never taking cards visible.
2. **A peer note written without a rerun.** The peer note carries:
   - its own script's path and hash;
   - the commit at which the script was written, sighted after the offer;
   - its output hash.

   The runner reruns the script, and checks that it shares no file with the producer's and imports nothing from the
   producer's paths. A note that reruns the producer's own script is accepted only as "reran", a lower kind than
   "re-derived". Only a re-derived note moves the card up the banking queue (§ 2.3 of the draft moves every card with a
   note).
3. **Measure the timeout in days, not in landings.** Landings follow main's pace: if main stops, the timer stops with it.
   Proposal: 72 hours from the offer and one re-offer, so at most six days, then "no peer check".
4. **"A lane" is not yet a field anywhere.** The peer stage needs the lane field of § 8's identity table, so that one
   field moves forward into the peer series (§ 3 below).
5. **The measure of the peer stage needs counts.** At two banking seats and a few cards a round, comparing peer verdicts
   with banking verdicts says little for months. The record should show the count beside the rate, and draw no
   conclusion below about twenty deciding cards with notes and twenty without.

### 1.3 Banking

1. **Blindness between the two banking seats can be enforced by sealing first.**
   - Each seat writes its verdict outside the repository and commits only its hash, its seal, to the queue.
   - Once both seals are sighted, each seat commits the verdict.
   - The runner checks that each verdict matches its seal and that each seal was sighted before the other verdict.

   Neither can copy the other.
2. **Blindness to the peer note cannot be enforced in a public repository.** The peer note lives on the peer's branch.
   - The charter can forbid reading it, and the peer note can be sealed the same way and opened after both banking seals.
   - Only plants check that rule: plant a note of "reproduced" on a faulty card. If faulty cards with a planted note pass
     banking more often than faulty cards without one, the blindness leaks, and the record says so.
3. **Two seats of one family make one kind of error together.** Two ACCEPTs from one family are not two independent
   checks, and plants written by main test only the faults main thinks of. Proposal:
   - Part of the plants come from the calibration set of real faults: those found at Reviews 86 and 87 are real faults
     of known kind.
   - Part are written by the auditor.
   - The rule of § 8 for main's cards (a check from another family) is worth extending in time to every deciding card.
     It stays a measure, not a rule, until the trial shows the cost.
4. **"Shares no code with the producer" is checkable only if both sides import only the allowed packages.** The rule
   should be that a decisive script, a peer's and a banking seat's import only the standard library, mpmath, sympy,
   numpy and scipy, which the claim card already lists. Disjointness then reduces to a comparison of file hashes, which
   the runner makes.
5. **A cited arc can be left out of what the banking seat reads.** The cold reader sees only the arcs the card cites. A
   producer who leaves out the arc against it is caught only by the runner's own record check (1.1.4). That check is
   what makes cold reading safe, and it is built first for that reason.
6. **There is no landing tool on main.** No tracked file is one: landings are made by hand, and the commit message records
   what was run.
   - If two banking seats write arcs, locks and ledger rows to main directly, main has three writers. That brings arc
     numbers taken twice and CHANGELOG entries that collide.
   - Proposal: a banking seat files its verdict and a prepared landing (the arc, the lock, the ledger rows) in the queue.
   - One tool lands it:
     - it takes the arc's number at landing;
     - it writes the CHANGELOG and PROGRESS_LOG pair;
     - it runs the gates and the suite on a fresh clone;
     - it refuses otherwise.

   This tool belongs in series 3.
7. **A split on main's own card would go to main.** Splits on main's cards should go to the auditor, and to the author if
   the auditor cannot settle them.
8. **A refiled card read cold again wastes the reading.** After a RETURN, the same banking seat should get its own RETURN
   back with the refiled card. It is its own note, not context from the record.

### 1.4 Plants, the auditor, identity

1. **A plant must look like any card, but every card carries a seat id.**
   - A plant under a seat that does not exist gives itself away.
   - Plants should be filed under real producers' ids, at the author's arrangement, and listed in a plant ledger.
   - The ledger's hash is committed at the start of each round and the ledger is opened after that round's verdicts.
2. **The share of plants, and a pause rule that needs a minimum count.**
   - In the trial: B2011 to B2017 and four plants, one for each stage: a broken custody, a peer-stage fault, a wrong
     number for banking, and a firewall case.
   - After the trial: one deciding card in six is a plant.
   - A seat is paused for a reading when it misses two plants in a row, or more than three of its last ten.
3. **The calibration set leaks once it is tracked.** Seats read the repository. Its faults should be kept as hashes, each
   fault opened only after the audit it calibrates.
4. **A badge must name what it covers.** Proposal: the hash of the card, of its decisive script, and of the verdict lines
   of the arcs it cites. A gate recomputes them; a badge lapses when any of them changes, including when a cited arc is
   retracted.
5. **The neutral codes must not collide with the scoreboard's codes.** The intake's pattern reads A01 to A12, F1 to F4,
   S01 to S03, LAMBDA and I-n as scoreboard codes. A family code such as "F1" would mark every card that names its seat
   as deciding. The identity gate should check every code against that pattern.
6. **An untracked file of real names lives on one machine.** Sessions here are lost when their container ends, and no
   other seat or the auditor can read such a file.
   - Proposal: a tracked table of neutral codes giving family, version and effort.
   - The mapping to real names is kept by the author outside the repository.
   - The attribution gate stands as it is.
7. **Main's cards need a check from another family, and none may be free.** Such a card should wait with a public status,
   "waiting for another family". It should not lapse to "no peer check".
8. **The audit ledger's routing runs through main.** A finding about main's work that main routes late should age, and
   escalate to the author, not to main.

### 1.5 Two gaps that block the build

1. **Where the runner runs.** The draft says the intake runs "without any seat". There is no workflow on main
   (`.github/workflows` does not exist), and seat sessions end. The choices are:
   - a scheduled workflow on the repository, which needs the repository's Actions and a writer to main that is not a seat;
   - one dedicated session that runs only the runner and holds no other role;
   - main's own session, on a schedule.

   The first is "without any seat"; the other two are not. **This is the author's decision.** The code is the same
   either way.
2. **The suite is red on main.** On `b11a892ca`, 23 tests failed. On `da7c98703`, harvest-debt is red: harvest_debt.py
   stops with `KeyError: 'head'` when a seat branch cannot be reached. Proposal:
   - a baseline of known failures, held in a file that may only shrink;
   - a landing is refused if it adds a failure or a red gate;
   - harvest_debt.py reports a branch it cannot reach and does not stop.

   These go in series 1 (the runner reads branches the same way) and series 3 (the landing tool).

## 2. What to reuse, and what to retire

| piece | reuse | retire |
|---|---|---|
| `scripts/checks/seat_intake.py` (76 lines) | the branch pins, the search for claim cards and the reading of their fields; its pattern of codes, for "deciding" | its tiers A, B and C (banking replaces them); the rule of one intake a day by main |
| `scripts/checks/harvest_debt.py` (874 lines) | the helpers that resolve and read a seat branch; the report of what each branch holds | the ledger rows per item (BACKLOG, STALE) once the unbanked list is frozen; its use by review-due, which moves to the auditor. The gate harvest-debt is reviewed after the trial |
| `docs/CLAIM_CARD.md` | the form, with four fields added: the card's id (given by the runner), the seat's code, the failing control as a command, and the decisive output lines | the section "How main takes a card" |
| `docs/BANKING_PROTOCOL.md` | Part I, A, B and D, as the landing tool's checklist | Part II (banking and the auditor replace it); Part III, to the auditor; Part IV, to main's integration. It is written again once, as the landing checklist |
| the landing tool | none: it does not exist | — |
| the 57 gates | the gates that keep the record whole: attribution, tracked-forbidden, append-only, firewall-oneway, id-collisions, the seal gates, arc-verdicts, verdict-schema, log-changelog-paired, gate-controls, test-vacuity, practices-register, public-face | candidates, to be measured first: harvest-debt, relay-debt, review-fires, review-actions, review-core, carry-age, lead-debt, point-debt, retraction-debt, seat-positive-verified, negative-second-computation. No gate is retired before a count of what each caught (series 1, patch 9) |

**The record's surfaces (§ 5).**
- **Keep:** the arcs, their verdict files and locks; the CHANGELOG and PROGRESS_LOG pair, written by the landing tool; the
  law map; the register; the scoreboard; the foundation.
- **The queue replaces:** HARVEST_LEDGER's per-item rows, RELAY_LEDGER for cards, and CAMPAIGN_STATUS's LATEST, which is
  generated from the queue.
- `relays/claims/` stays as the way cards travel.
- The views are generated from the queue.

**The queue's form (§ 5): a file per card,** `queue/cards/Q<nnnn>.json`, with:
- a status, out of: FILED, RETURNED AT INTAKE, REPRODUCED, OFFERED, PEERED, AT BANKING, VERIFIED, RETURNED, REFUSED,
  SPLIT, PARKED;
- an append-only history;
- the seals;
- the badges.

A file per card, not one register, because several writers file at once (the runner, the peers, two banking seats), and a
single register would collide on every round. A generated `queue/QUEUE.md` is the view.

## 3. The build plan (the order of § 6.3)

Each patch carries a test that fails when the patch is broken, and the gates and the suite are run as for R81-3.

**Series 1: the intake runner and the queue (10 patches).**
1. The queue's schema, `queue/cards/`, the gate queue-schema. Test: a planted malformed card.
2. Discovery: reuse seat_intake.py's reading; find cards on every seat branch; report a branch it cannot reach; give ids.
   Also mend harvest_debt.py's stop on an unreachable branch.
3. The form check, with the failing control and the decisive output lines.
4. Custody from the sighting log; a rewritten branch returns the card.
5. Reproduction in a sandbox:
   - no network;
   - a time limit;
   - allowed imports, read from the script's syntax tree;
   - normalised output lines.

   Then the failing control must fail. Test: a script that prints a constant reproduces, its control does not fail, and
   the card is returned.
6. The record check, from the runner's own terms, with its output attached to the card.
7. The firewall flag, raised to the author.
8. "Deciding", computed; the order of the queue; the producer's rate of mis-declaration.
9. The frozen unbanked list, generated and dated; a gate that lets it only shrink. Also the count of what each gate has
   caught, read from git's history, for the retirement reviews.
10. The listener tells a seat what the queue says about its cards. The runner writes to the card's file, not to the
    seat's page, which is main's.

**Series 2: the peer stage (6 patches).**
1. The lane field and the identity table's first rows, moved forward from § 8.
2. The offer by rotation, the decline, and the rates of declines and lapses.
3. The peer note's schema, the rerun of the peer's own script, and the check that it shares no file with the producer's.
   Test: a note that reruns the producer's script is graded "reran".
4. The timeout of 72 hours with one re-offer, then "no peer check"; "waiting for another family" for main's cards.
5. The cap of one peer on one producer's cards.
6. The table comparing peer verdicts with banking verdicts, with its counts.

**Series 3: the banking verdict files and the landing tool (7 patches).**
1. The verdict schema: ACCEPT, RETURN (corrections named) and REFUSE (counter-computation).
2. Sealing first. Tests: a verdict with no seal is refused; a seal sighted after the other verdict is refused.
3. Two ACCEPTs bank; a split goes to main, and on main's own cards to the auditor.
4. The baseline of known failures, which may only shrink.
5. The landing tool, on BANKING_PROTOCOL Part I A, B and D. Tests: a landing that adds a failure is refused; a single
   ACCEPT is refused.
6. The plant ledger, sealed at the start of each round and opened after its verdicts.
7. BANKING_PROTOCOL.md written again as the landing checklist; CLAIM_CARD.md's fields added.

**Series 4: the role charters (3 patches).**
1. `docs/roles/`, six pages: producer, peer, banking seat, supervisor, builder, and the author's page. Each lists what the
   role receives and delivers, its freedoms first (on the producer's page), its rules, how it is measured, and its hiring
   brief.
2. The gate charter-rules-checked: every rule outside "Advice" names the check that enforces it (a gate, an intake check
   or a kind of plant), and the check exists. Test: a rule with no named check fails.
3. The sorting of WORKING_RULES.md: its 21 sections, each sorted into a door rule, a rule for one role, or advice, with
   the check named. Rules are named by section and line, not quoted.

**Series 5: the audit ledger, the badges, identity (5 patches).**
1. The audit ledger, append-only. Only the auditor's code closes a finding; a finding ages and escalates to the author.
2. The badges' schema; their hash set; the gate that marks them lapsed.
3. The calibration set, held as hashes.
4. Identity fields on every card, note, verdict and finding, in neutral codes, checked against the scoreboard's pattern.
   The attribution gate stands.
5. A VERIFIED card produced by main needs one check from another family.

**After the build:** the author starts the two banking seats and the auditor; the trial runs B2011 to B2017 and the four
plants through every stage; then the listening line resumes (§ 6.4 to 6.6). This seat proposes a stop rule for the trial:
if the path costs more than it catches, it is simplified before it is trusted.

## 4. For main and the author

1. **Where the runner runs** (1.5.1). This is the author's decision, and series 1 is built either way.
2. **The four fields added to the claim card** (§ 2). The draft keeps the form unchanged.
3. **The offer by rotation in place of a peer's free choice** (1.2.1).
4. **A split on main's own card goes to the auditor** (1.3.7).
5. **Who writes plants:** part from the calibration set of real faults, part from the auditor, not main alone (1.3.3).
6. **The baseline of known failures, which may only shrink** (1.5.2), in place of the fresh-clone suite having to be
   green before any landing can pass.
7. **The two patches already sent:** R81-3 has landed (`da7c98703`). R82-2 waits for main's reading, and series 1 does
   not depend on it.

| | the label |
|---|---|
| the critique, the plan, the proposals | the builder's; to be read and decided by main and the author |
| the facts used | read on main's `da7c98703`: the draft, CLAIM_CARD.md, BANKING_PROTOCOL.md, seat_intake.py, harvest_debt.py, WORKING_RULES.md's headings, the list of gates, the lack of a workflow and of a landing tool |
