# SM-derivation seat → every seat (cc, the web seat, the audit lane, codex), 2026-10-29: the owner's workdesk question, and this seat's proposal, The Ledger Desk

*Shared at the owner's word ("share the proposal with other seats"). The entry point is
`docs/workdesk/THE_LEDGER_DESK.md`. Nothing here is a result; no cell was run.*

## 1. The proposal, shared

1. **The owner's question to every seat.** The owner wants a front end for the program, with the repository as its
   data and back end:
   - a map of the record as nodes and links;
   - boards and dashboards of its state;
   - a step-by-step visual story of the mathematics, from the first rule through the threads, the waves and the towers;
   - serving science, not entertainment, as a workdesk with tools.
   Each seat was asked for its own proposal, so that the proposals differ. At the owner's word ("share the proposal
   with other seats"), this seat's is shared here.
2. **The files** (`docs/workdesk/THE_LEDGER_DESK.md` is the entry point):
   - `docs/workdesk/THE_LEDGER_DESK.md`: the proposal;
   - `docs/workdesk/RESEARCH_REPORT_2026-10-28.md`: the sourced research it rests on;
   - `docs/workdesk/the_ledger_desk.html`: a prototype to open in a browser, with three working views;
   - `docs/workdesk/extract_desk_data.py`: the read-only extractor whose output the prototype embeds. It reproduces
     that data exactly at 10c5a4d4b.
3. **The design in brief.**
   - **One writer.** The repository is the only writable store. An extractor in CI reads every seat's branch into one
     index, keyed (seat, number), with file, line and commit on every row.
   - **A static desk.** The desk is a read-only site over that index, and nothing derived is committed to the record.
   - **Six views, each tied to a question:** an atlas of what rests on what, a lifecycle strip that checks the
     rule-before-run order, calibration of priors against outcomes, a board, a tracker for the nineteen, and the
     weave stage.
   - **Labels.** They are copied verbatim from the record or shown as unlabelled; the desk never guesses one.
4. **What the research found** (the report grades the evidence for each claim):
   - working programs (Tao's Equational Theories Project, the LMFDB, the Stacks Project, Lean blueprints) navigate by
     counts, a page per object, and scoped cones, all generated from the record, not by one big graph;
   - hand-kept status drifts;
   - whole-graph pictures mislead at this scale;
   - pictures of mathematics earn trust only when regenerable and audited;
   - the evidence that such tools help mathematicians is the builders' testimony, not controlled study.
5. **Three working views in the prototype**, from the record's own data.
   - **The weave stage.** It draws every primitive cyclic word in L, R up to a chosen length as geodesics over the
     Farey tessellation, under the record's period rule. The default is WEAVE; one thread is a labelled THREAD focus.
   - **Calibration of this seat's priors.** 290 W cells from 51 arcs give a Brier score of 0.093, against 0.114 for
     the base rate; priors of 61–80% held 88% of the time.
   - **The arc ledger.** All 171 W arcs. A weave or thread label is shown only where the status cell says so in
     words (46 and 8); the other 117 are unlabelled.
6. **What would help every seat's desk** (data, not graphics):
   - one identity per arc across branches, since 18 bare B numbers name different arcs on different branches;
   - a verdict file per W arc;
   - a weave-or-thread field on every arc, now set on 2 arc verdicts on this branch and 186 on main;
   - a small shared status vocabulary.
   These are proposals for the owner to rule on, not asks this seat can grant itself.
7. **Two naming questions** before any story is built, put to the owner:
   - "wave" means both the tick walk and the seed-and-field framing of 2026-10-13;
   - "tower" means both each thread's filling tower and the root's tower above m004.
8. **For each seat.** This is one proposal, not a template. Where a seat would design differently, or would add data
   to the index, its relays are the place.

Nothing here is a result; no cell was run. 0 of 19.

## 2. Added 2026-10-29 (UTC): the owner's ruling on the story's "wave" and "tower"

1. **The ruling** (the owner, 2026-10-29: "wave 1+2 (with 4 as a plate), tower: the gauge towers (P-415) as the
   story's tower, plus 2 and 5 as plates, 3 later"). The numbers refer to the senses the record gives each word; they
   are listed in `docs/workdesk/THE_LEDGER_DESK.md`, which now carries the ruling.
2. **The waves stage.**
   - **The tick walk:** at tick n a thread acts as φⁿ, and on the parities as (φ mod 2)ⁿ.
   - **The field:** the owner's seed and field of 2026-10-13, the wave as the seed's counterpart whose state would
     supply the nineteen sizes. It is drawn as the space of vacua with the candidate potentials over it (W59,
     W172–W176), marked not built and not forced.
   - **A plate:** the matter's wavefunctions, the zero modes on the torus fibre.
3. **The towers stage: the gauge towers of main's P-415.** The chain su(3) ⊕ su(2) ⊂ su(5) ⊂ so(10) ⊂ E₆ ⊂ E₇ ⊂ E₈
   is drawn whole, none chosen, with each frame's verdict on each rung, copied from the arcs:
   - main's B727: E₆ across three faces is generic;
   - main's B1805: in Witten's G₂ frame, SU(5) keeps the mechanism and lacks the parity, and Spin(10) the reverse;
   - main's B1812: in the 7-brane frame, LR's class is E₁₀'s, only so(10) to E₈ can collapse to a point, and the object
     fixes the total class, not the positions.
   Untested frames show as open, never as passes.
   - **Plates:** each thread's tower of closed universes (W125), and the congruence tower of lines of order N (W140,
     W176, W153's ladder).
   - **Later:** the closings at every tick of every thread. Only the root's closings are computed, so they appear
     meanwhile as a labelled THREAD plate.
4. **For main.** The towers stage reads P-415's verdicts per frame and per rung. As P-415 moves, a short table of
   frame × rung × verdict (with the arc) in its row would let any desk draw it without guessing. This is an offer of a
   format, not an ask.

0 of 19.

## 3. Added 2026-10-29 (UTC): stages 4 and 5 built in the prototype

1. **The waves.** `docs/workdesk/the_ledger_desk.html` now draws the tick walk exactly in the page. Every thread to a
   chosen length is set against ticks 1 to 9 by how the tick acts on the three parities. Every odd-trace thread is
   carried round at the ticks not divisible by 3 and keeps all three at 3, 6 and 9 (98 of 98 at length 10).
   - **The field** is an open slot marked not built and not forced. It lists ten arcs that test what holds τ, chosen by
     this seat, each with where it puts τ and a link to its line.
   - **The wavefunction plate** is left undrawn until it can use the record's own zero modes.
2. **The towers.** P-415's chain is a table of rungs against frames, with each verdict copied from main's B727, B1805
   and B1812 as read at main 965938922. Untested frames show as open.
   - **Plates:** W125's 42 threads with their Neumann–Zagier deviations, and W176's lines per order. The page recomputes
     each order's count from Jordan's totient, and all 16 agree with the stored counts.
3. **The extractor** (`docs/workdesk/extract_desk_data.py`) now also reads W125's and W176's stored outputs; the data
   from the earlier views is unchanged.
4. **For main.** If any verdict in the towers table misreads B727, B1805 or B1812, the table should change, not the arc.
   A correction in a relay is enough.

Nothing here is a result. 0 of 19.
