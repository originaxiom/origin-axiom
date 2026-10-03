# THE FOUNDATION LOCK — the plan (2026-10-02, at the owner's word)

The owner, 2026-10-02: *"id like to take our time, step back, and understand completely all the ways we could make our
foundations as robust and sophisticated as it gets, so we lock once for all our genesis work, because i believe once we
do that and inform all the mds and documentation on repo to reflect that, the progress would be smoother. we wouldnt end
up retreiving old work over and over."* And: *"should we craft a plan and execute it to the end"* — *"i agree, but just
lets make sure we dont miss any work and misclaim about it. make a rule to see the repo first and literature."*

## The problem this plan answers

The genesis is stated in several places and several forms — the matrix axioms (`docs/UNIQUENESS_THEOREM.md`), the word
chain (P019, `docs/THE_END_TO_END_CHAIN.md`), the framework's four letters (`docs/THE_FRAMEWORK.md`), the generated
state space the seats adopted on 2026-09-27 — and no one page states the genesis with one numbering (`docs/THE_CLAIM.md`, B1014, is the one page for the *claim*: its hypothesis list and what follows from it). Each seat works from its memory of
them, pieces are re-derived and re-retrieved, and the top surfaces drift (the README's state section is dated
2026-08-22). The record is larger than any seat's working memory of it: on the day this plan was written, three
statements of absence made to the owner from memory were each contradicted by arcs banked in August.

## What "lock" means here

The **statement** is locked: which inputs exist, which follow from which, which are derived, chosen or open, and what
evidence would reopen each. An **open question is not locked shut**: an input that is still a declared choice is
recorded as a choice. The lock is one canonical page that every other document cites, and a gate that fails when one
restates it differently.

## The stages, each with its end

| | stage | ends when |
|---|---|---|
| 0 | Close what is open: the harvest of the SM seat's arcs (B1453). | landed |
| 1 | **The sweep.** Every statement of the genesis in the record — main's arcs, documents and paper, the SM seat, codex's two lanes, the other lanes, the web-seat handoffs — one row each: the axiom, commitment or principle, its source, what it claims to derive and what it assumes. **The first five hundred arcs are read line by line, not by keyword** (see below); the rest by `topic_sweep.py` and read-in-full passes. | a second, independent sweep adds no row |
| 2 | **The dependency analysis.** For each input: derived from the others; independent (a sibling exhibited in which the others hold and it fails); chosen and robust; chosen and fragile; or open. The puncture from the carrier axiom first (the SM seat's sm:B1380), then the two closure axioms, the dictionary between the two routes (B1323), the residual bit (B979), orientation (B1234, sm:B1380–B1383). | every row has a status carried by a computation on this bench or a source read with its hypotheses |
| 3 | **The principle.** Stated precisely in both forms the record holds — the four-letter principle, and "no unforced collapse" with generated closure — and tested for what it forces without help. | the attempt is recorded, whichever way it comes out |
| 4 | **The canonical page and two gates.** One document: the principle, the minimal inputs with their statuses and reopening rules, the generated space (states, moves, equivalences, root), what is forced, chosen and open. Gates: other documents cite it and do not restate it; a negative on a top surface carries its scope (general, one mechanism, local to a named state or family, a premise). | both gates green |
| 5 | **Propagation.** README, THE_FRAMEWORK, THEOREM_LEDGER, THE_END_TO_END_CHAIN, UNIQUENESS_THEOREM, THE_SM_VERDICT, the paper's genesis section, TERMINOLOGY; the SM seat's "for main" items applied or declined with a reason; the headline claim of every NEGATIVE arc given its scope; the page relayed to the SM seat and codex. | the scope gate is green on every surface |
| 6 | **The state of the programme, swept.** One page of what the record holds and what it lacks on dynamics, time, scale, selection, values and the physical vacuum — every "lack" carrying the sweep that supports it. The map for the physics work. | every line cites its sweep |

**The test of the whole.** A reader with no context reads only the canonical page and the README and answers a sealed
set of questions: what is forced, what is chosen, which negatives are local to which states. Wrong answers mean the
page is not done.

## The early record is read whole, not searched (the owner, 2026-10-02)

*"there is already computed grammar in our program, do we count for it? first 500 B's has a lot of genuine work that is
crutial for later."* Swept the same hour: B1–B500 is 486 arc directories on main, 481 with a verdict (281 PROVED,
168 NEGATIVE, 26 OPEN, 6 RETRACTED). **The word "grammar" appears in none of their verdict lines** — it enters the
record at B530–B535 (the four-letter object's grammar golden at three nested levels; the interaction grammar's
four-word kernel; one Perron number and the grammar fixing the substitution). The early arcs carry the same subject
under other words: 43 on words, substitutions and monoids, 58 on the trace map and the character variety, 111 on what
is forced, unique or selected. A keyword sweep written in today's vocabulary would pass over them.

So in Stage 1 every one of the 481 verdict lines is read, and each arc is given its subject and whether it bears on
the genesis, the generated states or a later result, with the Recurrence Atlas (`scripts/atlas/query.py`) as the
cross-check. The output is an index of the early record by subject, kept with the canonical page. The 168 early
negatives are scope-tagged in Stage 5 with the rest.

## Progress (kept current at each landing)

- **2026-10-02, S37. Stage 0 landed** (B1453: the SM seat's forty-seven arcs rowed, four results re-derived, lead
  L239 for its remaining items for main).
- **Stage 1, the early record: done.** `docs/EARLY_RECORD_INDEX.md` — the 486 arc directories from B1 to B500 under
  twenty subjects, every row the arc's own verdict line, generated by `scripts/checks/early_record_index.py` and
  locked (an arc in no subject fails the test). Among them: 25 arcs on the genesis, 22 on what selects the golden
  seed, 45 on constructions with more than one object.
- **Stage 1, the genesis statements on main: swept** (`topic_sweep.py`, 81 of 1 325 arcs; read: B749, B979, B1003,
  B1014, B1123, B1234, B1266, B1323 and the four pages). **The record carries three labelings** — the uniqueness
  theorem's A1–A7 (records), P019's A0/A2/A5/A5b/A6 (description) and the ledger's C1–C18 — **and the letters
  collide**: "A6" is minimality in the first and orientability in the second. B1323 proved the dictionary between two
  of them. `docs/UNIQUENESS_THEOREM.md` has not been touched since 2026-05-29 and `docs/THE_CLAIM.md` since 08-31;
  neither carries B1234 (the walls trace to orientation) or B1323.
- **The same day the SM seat wrote `GENESIS.md` v1.0** on its branch (sm:B1516, relayed to main): one collision-free
  numbering (PF, GM, SE, T-ROOT, F-, FK, GAP), the root from four inputs each shown needed, a crosswalk of the old
  labels, a mandatory scope tag. It found the same collision independently. **Stages 3 and 4 therefore change shape:
  main does not write a second page. It verifies GENESIS v1.0 with its own code (the next arc, B1454), compares it
  with what main's record holds and it does not cite (the relay of 2026-10-02 lists eighteen arcs), and adopts it,
  amended, as the one page — or answers it.** The principle's single wording (its fork FK1) is the owner's.
- **2026-10-02, S38. Stages 3 and 4 done, Stage 5 begun (B1454).** GENESIS v1.0 verified on main by other routes and
  adopted as **`GENESIS.md` v1.1**, with 23 listed changes (the frame F-MC, the principle's mathematical form, the cost
  of the orientation choice, the early record on the swap; a misquotation and one unswept absence corrected). The two
  gates of Stage 4 exist: `genesis-cited` (cite, do not restate) and the scope tag in the verdict schema from B1454.
  Stage 2's first result is in the page: the root needs four inputs and each is needed; the puncture stays
  conditional. Propagation so far: pointers in eight pages, the uniqueness theorem's witness, the ledger's count,
  WORKING_RULES, TERMINOLOGY. **What remains is lead L240**: the scope tags of the older arcs (NEGATIVE first), the
  README and THE_CLAIM rewrites, F-MC off the root, the forks with computations behind them, Stage 6's swept page,
  the fresh-reader test — and FK1, the principle's wording, which is the owner's.
- **2026-10-02, S39 and S40.** The deciding test on the root's vacua (B1455, NEGATIVE, scoped; run a third time by the SM
  seat with the same outcome). **GENESIS is at v1.3** (B1456): the SM seat's v1.2 verified — 758 word states are 536
  manifolds, signed even powers placed — with the test's result, what a source must be (GAP3) and the observer fork
  FK12. **Stage 1's lane work is done for the two active seats:** the SM seat is read through sm:B1520 and codex's
  audit lane through R80 (B1457), which is where the record's sourced counts on objects other than the root live.
  The owner's measurer question is the standing lead L241. Remaining: L240 (propagation), L242, L243.
- **2026-10-03, S41 (B1458).** Stage 5: the README's state section rewritten from GENESIS v1.4; the SM seat's bar adopted
  on main (every positive on a generated state is graded); the own-level law refined on main's own data.
- **2026-10-03, S42 (B1459).** Stage 4, a negative-to-theorem conversion in the class-index frame: the 24 + 188 zeros
  at the complete points, held as census, derived from B1297's three lines and the fibre's involution; the audit
  lane's R58-6 answered with hypotheses; one E82 instance of the seal's own caught and repaired post-seal.
- **Still Stage 1:** codex's two lanes and the sep16 lane (harvests that age on 2026-10-09 and 10-12), the audit
  lane's same-day genesis reconciliation (unread on main), the web-seat handoffs.

## What runs alongside

- The lane harvests that age on 2026-10-09 and 2026-10-12 (the sep16 lane, codex's second lane): they are also Stage 1's
  material.
- The review governance the owner approved on 2026-10-02 (R58-1): the gate at twice the period, the third-carry rule,
  three checks in the core.

## The rule this plan runs under

WORKING_RULES, the rule of 2026-10-02: see the repo and the literature first. Every stage's output cites its sweeps; a
row with no sweep behind it is not a row.
