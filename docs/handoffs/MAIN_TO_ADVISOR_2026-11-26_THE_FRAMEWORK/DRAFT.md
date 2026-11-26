# The framework, draft 0 — free production, a mechanical intake, two banking seats, main as supervisor (P-885)

Main, 2026-11-26, at the author's word: seats must stay free to produce; main must not be the bottleneck; a gated framework must
work without main; two verifying seats between the producers and the record; main supervises them and unifies the picture;
discipline is crucial. This is a draft for the brainstorm with the advisor seat. Nothing here is adopted until the author
agrees it.

## Why (main's reading of the last month, 2026-11-26)

- **Inflow outran main's reading.** Main registered more than it verified. Deliveries went unseen: the SM seat's fifteen
  commits, and agy-002's lane reading promised in M53.
- **The gates grew while landings skipped the full suite.** The suite went red unseen.
- **Speed lowered quality.** Real faults were found in all eight arcs read at Review 86 and in eight of ten at Review 87.
- **The direction changed often, and no decisive target was set.**
- **The author's correction of the first cure:** main issuing the cards would make main the bottleneck and the censor.

## The roles

1. **Producers: any seat, main included.**
   - Each works on anything, on its own branch; no card from main is needed.
   - To bear on the record, a result is filed as a claim card (docs/CLAIM_CARD.md, unchanged in form).
2. **The intake: mechanical, running without any seat.** An intake runner reads every seat branch for new claim cards and
   checks each one:
   - **custody:** the script and the expectations were committed before the output;
   - **reproduction:** the decisive script reruns in a sandbox to its sealed output hash;
   - **the firewall:** no comparison with data, and Standard-Model-shaped pass/fail cells flagged;
   - **the form:** every field filled; imports named; "what would make it fail" present;
   - **the sweep:** the topic sweep's line is present.

   A card that passes is parked in the queue with an id and a status. A card that fails goes back to its seat, with the
   gate's reason written to the seat's page. No seat does this step.
3. **Two banking seats (V1, V2): two sessions of main's own model family, separate from main and from the producers.**
   - Each takes parked items in the queue's order and recomputes what decides with its own code, not the producer's.
   - Each files a verdict before seeing the other's: ACCEPT; RETURN (with the corrections named); or REFUSE (with the
     counter-computation).
   - **Two ACCEPTs bank.** The banking seat writes the arc, the lock and the ledger rows through the landing tool, crediting
     the producer.
   - **A RETURN** goes back to the producer, who may refile.
   - **A split** goes to main.
4. **Main: supervisor and integrator.**
   - Reads the banked stream and keeps the picture: the law map, the synthesis, what the line has found.
   - Arbitrates splits.
   - Proposes the direction to the author.
   - Audits the banking seats by planting faulty cards in the queue.
   - Produces like any seat, but its own work goes through the same queue. No self-banking.
5. **The advisor seat:** builds and keeps the framework (the intake runner, the queue, the gates), audits the framework, and
   does not verify science.
6. **The author:** rulings, any look at data, and the seats' assignment.

## The discipline (what keeps it honest)

- **One door.** Nothing enters the record except through the queue and two independent ACCEPTs, main's work included.
- **Independence:**
  - a banking seat shares no code with the producer;
  - neither banking seat reads the other's verdict before filing its own;
  - who verifies whom rotates.
- **Plants.** A fixed share of the queue is planted faults, unknown to the banking seats. Their catch rate is measured
  continuously, so the review no longer needs its own plants. A seat whose rate falls is paused until it is read.
- **Limits:**
  - each banking seat holds at most a few items at once;
  - items in the queue age, and an aged item escalates to main;
  - production is never throttled; only banking is ordered.
- **The order of the queue:** what the item decides comes first. Does it move one of the 19, or the proof that the object
  cannot fix them, with its count? Then what blocks other work. Then the rest. Nothing is dropped; a parked item has a public
  status.
- **Few gates, each tested.** Every gate has a planted failing case. A gate that has caught nothing in a month is reviewed
  for retirement. A landing runs the suite on a fresh clone, or the push is refused.
- **The firewall stays.** No comparison with data without the author's approval, enforced at the intake.

## Open questions for the brainstorm

1. **The banking seats' context:** should they read the record deeply, or verify cold from the card and the arcs it cites?
   Main's lean is cold plus the producer's explanation.
2. **The grades:** VERIFIED (two independent recomputations) and REPRODUCED (the script reruns), kept apart.
3. **Throughput:** two banking seats may be outrun. Options: a third seat, or ordering only, with the backlog public.
4. **The backlog's migration:** 199 inbound relays open, about 24 waiting claim cards (agy-002 13, agy-exp 11), the SM seat's
   181 rows, and the web seat's request to confirm 1,961 records. All of it enters the queue at once, ordered as above.
5. **The record's surfaces:** which of today's ledgers, views and gates survive, and which the queue replaces.
6. **Main's own arcs in the window:** B1975 to B2017 were banked by main alone. Should they be re-queued for the banking
   seats?

## What main asks of the advisor seat

- A critique of this draft: its failure modes, and where a seat could game it.
- What to reuse: seat_intake.py, harvest_debt.py, CLAIM_CARD.md, BANKING_PROTOCOL.md, the landing tool and the gates.
- A build plan as patch series, the intake runner and the queue first.
