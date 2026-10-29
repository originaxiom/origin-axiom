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

## 4. Added 2026-10-29 (UTC): the build order's first step, the index, and the lifecycle strip

1. **The index.** `docs/workdesk/build_index.py` reads this seat's branch and main's through git alone and writes one
   index outside the record: SQLite, a JSON copy and a manifest. The output is never committed.
   - **Keys.** Every arc is keyed (seat, id). A B directory present on main is main's; one present only here is this
     seat's. Ten numbers name different directories on the two branches, and the keys keep them apart.
   - **Size.** 1812 arcs (1518 of main's B arcs, 123 of this seat's, 171 W arcs), 4069 edges, 290 prior cells and 200
     lifecycle steps, each row with its file, ref, commit and blob.
   - **Determinism.** Two builds, equal sha-256 for every table, or nothing is written. Built from this branch at
     f35e814d3 and main at ac2e51f87.
2. **The audit list.** 30 edges point at targets the index cannot find, and it lists them rather than guess.
   - 18 point at directories without a verdict file: B506, B511, B578, B580, B614, B659, B666, B913.
   - 11 point at ids on neither branch: B514, B792, B796, B820, B829, B844, B846 and B999 among them.
   - One names another seat's id outside the two branches read.
   - 4 of main's dependencies cross to this seat by bare number: main's B1299, B1340, B1415 and B1435 on this seat's
     B1268, B1283, B1355 and B1374.
3. **The lifecycle strip.** Each W arc's steps are read from this branch's commit subjects and placed by commit time.
   99 arcs have a named step, 46 have two or more and 20 have all four main steps. None is out of order. Commits cannot
   show that a rule was pushed before its script existed, or that an output was read once; the page says so.
4. **For main and every seat.** If any of the 30 audit edges is a typo in a verdict file, the verdict file is the
   place to fix it, not the index. A seat that wants its branch read by the index can name the ref in a relay.

Nothing here is a result. 0 of 19.

## 5. Added 2026-10-29 (UTC): the owner's ruling on the two open decisions, and the labels rule

The owner answered the proposal's two open decisions with "if u recomend ao", ruling for this seat's recommendation.

1. **The weave-or-thread field.** Main has carried `weave_or_thread` on every verdict file from B1491 on (all 198), so
   this was half settled before it was asked. The gap on the two branches the index reads is this seat's 171 W arcs.
   - They get main's field, unchanged, in one register next to NOTE: W_VERDICTS.json in the weave dossier.
   - Labels are copied where the record states them. This seat assigns a label only where the record does not, under
     `docs/workdesk/THE_LABELS_RULE_2026-10-29.md`, committed before any label.
   - Arcs from before the rule keep no label, on every seat, and the desk shows them so.
2. **Where the desk lives.** In this repository, built and published by a CI job to GitHub Pages, committing nothing.
   - **For main.** The repository has no CI today, so the workflow must land on main. This seat will put a proposed
     workflow file in `docs/workdesk/`; it does nothing until main copies it into place. Whether and when is main's
     call.
   - **For the owner.** Pages is switched on in the repository's settings. The page will be public, as the repository
     is.
3. **For every seat.** A seat whose arcs carry their label in prose can do the same, under the same rule or its own.

Nothing here is a result. 0 of 19.

## 6. Added 2026-10-29 (UTC): every W arc labelled; the page rebuilt from the record; the workflow proposed

The owner corrected the ruling's wording the same day: "if u recomend ao" should read "so". §5 and the labels rule keep
the words as first given, since the rule was pushed before any label; the meaning is unchanged.

1. **The labels.** `docs/dossiers/the_weave_2026-10-07/W_VERDICTS.json` gives all 171 W arcs main's `weave_or_thread`,
   built by `docs/workdesk/w_labels.py` under the rule committed and pushed first (3889806ad).
   - **Copied: 89.** 54 from the status row's own phrase, 24 from the arc's "Weave or thread" paragraph in NOTE, 11
     from its rule file.
   - **Assigned by this seat: 82,** each with its reason, by one mapping of the record's own words: the row's tag
     "(WEAVE …)" or "weave-type" for the whole claim gives weave; "thread-and-frame" gives thread, as main labels its
     arcs on lines chosen by a stated rule; "frame result" or "frozen piece" gives neither, as main labels its frozen
     pieces; checks of another seat's arc, readings and chosen objects give neither.
   - **A gap in the rule, disclosed.** Step 1 named only the phrases "weave result" and "thread result". The early rows'
     own tags, "(WEAVE)", were not named, so those arcs are listed as assigned with the tag as their reason.
   - **One conflict, listed, not reconciled.** W125's status row says thread result; its rule file said "A weave result
     if K1–K4 hold". The row, written after K4 failed as worded, comes first in the rule's order and stands.
   - **The totals:** weave 114, neither 43, thread 14.
   - **All three expectations stated before the script failed.** Copied came out at 89 against about 120. There is one
     conflict, where none was expected at 70%. And weave, not neither, is the most common assigned label (42 against
     35).
2. **The index (schema 2)** reads the register and main's verdict files and gives every arc its label and its era.
   - **After the rule:** main's arcs from B1491, this seat's B arcs whose verdict file came after
     `docs/THE_WEAVE.md`, and every W arc.
   - **The coverage.** Every arc after the rule is labelled on both branches: main 198 of 198, this seat's B arcs 2 of
     2, its W arcs 171 of 171. Main's 1320 arcs and this seat's 121 from before the rule stay unlabelled, and the desk
     shows them so.
   - **A correction to §4.** §4 implied the index reads only through git. The B arcs and the register are read that
     way, but the W rows and the prior cells come from the extractor, which reads the checked-out NOTE, so a build is
     made from a clean checkout.
3. **The page from the record.** `docs/workdesk/build_page.py` takes the committed page and replaces its two data lines
   with a fresh extraction and the commit it came from. Panels recompute; numbers in the prose stay as of the page's
   last commit.
4. **For main: the workflow.** `docs/workdesk/PROPOSED_WORKFLOW_ledger_desk.yml` runs on main's pushes, every six hours
   and by hand.
   - **What it does.** It checks out this seat's branch with main's history beside it, checks the register, builds the
     index twice and stops unless the builds agree, rebuilds the page, and deploys it to Pages. It commits nothing.
   - **How it is adopted.** It is inert where it sits. Main adopts it by copying it into `.github/workflows/`, and the
     owner switches Pages on.

Nothing here is a result. 0 of 19.

## 7. Added 2026-10-29 (UTC): the build order's third step, the board and the atlas

The owner asked for all of this seat's recommendations ("all u reccomend"). This section covers the desk's third
step. W177, the second recommendation, follows under its own rule.

1. **The board** (view H) shows each seat's open arcs with their labels and every arc counted by verdict and label.
   - **The relays waiting:** the OPEN rows of each seat's ledger, aged to that seat's commit. The last row for a file
     wins, as in the relay-debt gate.
   - **For main: the gate's blind spot.** The gate's row pattern (`scripts/checks/relay_debt.py`, ROW_RE) matches 9 of
     main's 79 OPEN rows and 42 of this seat's 82. Most rows that miss carry text after the backticked file name in
     their first cell, so the gate can neither age nor escalate them.
   - **What the board found under it.** One row on this seat's ledger was past 21 days with no marker: cc3's four-paper
     relay of 2026-08-26, whose twin row on main was escalated on 2026-09-17 (B1420, recipient lane retired). The
     escalation is now mirrored onto this seat's row (92f6aee28). No other unmatched row on either ledger is stale and
     unescalated.
   - **An offer, not a change.** Widen only the first cell, so it allows text after the file name:
     `` ^\|\s*`?(?P<name>[A-Za-z0-9_.\-]+\.md)`?[^|]*\| ``. With the rest of ROW_RE unchanged, the pattern then
     matches all 79 of main's OPEN rows and all 82 of this seat's, checked on both ledgers at the build commits.
     Whether to change the gate, which is shared code, is main's call. A widened gate would at once see the rows
     that are stale today.
2. **The atlas** (view I) draws any arc's upstream and downstream cones over depends_on and main's rests_on_seat.
   - **The most depended-on arcs,** computed: main's B849 and B851 (654 arcs downstream each), then B261 and B5 (651).
   - **Four dependency 2-cycles:** main's B849/B851, B872/B875 and B1306/B1307, and this seat's B1530/B1532.
   - **This seat's own cycle.** B1530 and B1532 each list the other in depends_on, which reads as mutual citation
     rather than dependence. Their verdict files are banked and are left unchanged here. Main's three are main's to
     judge.
3. **The index is at schema 3.** It adds the relays table and the atlas's slice. Two builds agree, and the page
   rebuilds from the record byte for byte.

Nothing here is a result. 0 of 19.
