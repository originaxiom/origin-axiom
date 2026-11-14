seat: sm
read: M24
state: SM-C8 delivered (R_leak); SM-C11 (P-333) sealed, its run next
on: M22's question answered (relays/SM_ANSWER_M22_W31.md); SM-C8 (the partner test, SM-C5's E3) proposed; literature note 1 (relays/SM_LITERATURE_NOTE_1.md), with three amendments to SM-C8 and a candidate SM-C9; scope note on the closed-join block (relays/SM_SCOPE_NOTE_CLOSED_JOINS.md); SM-C8's instrument calibrated outside the population (relays/sm_c8/calibration/); SM-C6 E1's owed steps done (level 2, the read-out, the criterion)
needs: (1) a confirmation that M24's "beside SM-C8" is SM-C8's word, as this seat reads it (SM-C8 runs after SM-C10 with the amendments); (1b) main's word on restating the closed-join block with its three hypotheses, and on a card for the non-orientable closing; (1c) main's word on the leads page's "exactly when" for the audit criterion (E1 step 4); (2) for M22's second computation of B1825: it compares with measured values, which M1 and M6 keep from this seat. Main to say which sealed card covers it and which file holds the values, or to supply them
next push: B1825 second computation, once (2) is answered; or SM-C8 on main's word

# The SM seat's status (protocol of 2026-11-11, docs/seats/README.md on main)

- **M1 read** (main @ 2f3984d27): verify the physical lane's thirty items. Batch V1 has harvest rows 1418, 1420, 1421,
  1422, 1423, 1425, 1465, 1487, 1488 and 1489. Batch V2 has rows 1517–1535 and 1537.
- **Cards committed, as main proposed them:**
  - `relays/cards/SM_C1_physical-lane-batch-V1.md`
  - `relays/cards/SM_C2_physical-lane-batch-V2.md`
- **The listener runs** as scripts/seats/listen.py --seat sm, taken from main unchanged. It is not a tracked file on
  this branch, so it runs from a copy outside the tree. It showed M1 once and nothing since.
- **This seat's earlier record** (relay §1–§355) stays in `SM_TO_CC_AND_CODEX_2026-10-07_THE_CHIRAL_TRIPLETS_COUNT.md`
  at this branch's root. New work answers through this file and the cards.
- **The firewall** of M1 and § 9 of the protocol applies to all of this work.
- **SM-C1 closed** (batch V1): ten REPRODUCED. The verdicts are in `relays/SM_C1_VERDICTS.md`, and the checks in
  relays/sm_c1/ were committed first (68bccc168).
- **SM-C2 closed** (batch V2): twenty REPRODUCED. Row 1527's comparison with a measured weak angle is CANNOT CHECK
  under the firewall, and nobody makes it. The verdicts are in `relays/SM_C2_VERDICTS.md`. The checks in relays/sm_c2/
  were committed first, together with the lane's six control packages run as found (44 tests, all OK).
- **M1 complete:** thirty items, thirty verdicts. Nothing is needed from main or the lane for it.
- **M2 read** (main @ 69f66fbf3): two rulings of the owner, both dated 2026-11-11, bind every session.
  - His messages are private (register row P-796). Nothing he says is quoted in this seat's pages, status file or
    commit messages.
  - A check is named by its method, in the words of § 12 (register row P-797). A check has a result, not a verdict.
    For the cards, one result per item.
  - Taken: both result notes now name each result by method, in a new section of each. Every own script was rerun
    on a clean checkout at 868170ce5, and all 23 outputs came back byte-identical (the REPRODUCED_RUN.txt files):
    - computed once; reproduced; expectations committed first; tested against planted errors (11 of 11 and 16 of 16
      caught);
    - the lane's controls: computed once;
    - the written reviews and the cited results: not independently checked.
  - In the two cards, "verdict" now reads "result".
- **M3 read** (main @ 323f92327): main has received SM-C1 and SM-C2 and needs nothing more for them. Main will
  recompute one deciding number in each batch by its own route, after the review.
  - The review comes first. Card SM-R79 is committed with main's scope:
    `relays/cards/SM_R79_review-79-seven-arcs-five-locks.md`.
  - It reads seven arcs in full and plants errors against five locks. B1889 judges this seat's own record, so it is
    named and left, as § 13 asks.
  - After it come SM-C3 (the fork lane's four exact packets, register row P-057, run again with this seat's own code)
    and a proposed card for the parameter inventory.
- **SM-R79 delivered:** `relays/REVIEW_79_SM.md`, read at main 323f92327. Its outputs in relays/sm_r79/ were committed
  first.
  - Six arcs were read in full and 43 findings entered, each with its quotation checked by machine: 63 of 63 found.
    B1889 judges this seat's record, so it is named and left.
  - Five locks were tested by planted errors. Caught: E13 4 of 9, E6 3 of 6, E10 3 of 7, E5 8 of 10 (the default
    lane), E3 7 of 12. The shapes missed are named.
  - One standing instance of E3's old form was found, in the root CHANGELOG.
- **M4 read** (main @ 0dda7b472): main's own changes to its instruments in the window, added to SM-R79. The window's
  difference for scripts/checks, scripts/seats and scripts/gates/gates.py was read, with the advisor seat's four
  patches left aside as M4 asks. Five findings are added to `relays/REVIEW_79_SM.md` (R79-SM-44 to 48):
  - the arrival gate excuses a sentence on any earlier denial word, and misses a line break inside its phrase;
  - the debt gates still pass their environment to the checkers, two of which read a variable that changes their
    input;
  - a claim that the commit's day cannot freeze;
  - the listener records a message as shown before it is seen.
- **SM-C3 started:** its card is committed with main's scope: `relays/cards/SM_C3_fork-lane-four-exact-packets.md`.
  It covers the fork lane's four exact packets (register row P-057) at 0c6570bab, run again with this seat's own code.
  The listener reached its session's time limit; main's page is checked by hand at each push.
- **SM-C3 closed:** `relays/SM_C3_RESULTS.md`. The checks in relays/sm_c3/ were committed first (458ab9623,
  9c77f2f53), and a clean-checkout rerun (4f442741b) gave every output byte-identical.
  - All four packets are REPRODUCED, claim by claim, by this seat's own exact code.
  - Two claims are CANNOT CHECK. The packets take their definitions from elsewhere: W24's E8 embedding, and the lifted
    move action from bundle_transport.
  - The lane's five verifiers reproduce as found, including the first cohomology run's documented failure.
  - One plant the card named is not a fault: Bᵀ = −B is a parity twist. It is reported, and B = I₂ was planted in its
    place and caught.
  - The reading of GENESIS GM4 is left to main. The note offers one line per packet.
- **SM-C4 proposed:** `relays/cards/SM_C4_parameter-inventory.md`, the parameter inventory as M3 asks. It gives the
  names, kinds and what each rests on, with no value on the page.
  - It covers the 19, and the neutrino sector's 7 or 9 beside them. Each row gives the parameter's definition and
    scheme, the term of the Lagrangian it sits in, and what the record on main says about it.
  - The count is computed separately from the field content, and the table must match it. Planted errors are run
    against the table's own checks.
  - It is part of WP-4.4's first step. WP-4.4's bar, null and look count stay main's and the owner's.
  - As a card of this seat's own, it waits for main's word (§ 6). It also asks whether the framing ledger and the
    scoreboard may be opened. Until main says, neither is opened.
- **M5 read** (main @ 896cae025): Review 79 is entered. This seat's 48 findings all held. The five locks caught 25 of
  44 planted errors, and main has mended them.
  - Card SM-R79b is committed with main's scope:
    `relays/cards/SM_R79b_locks-again-answers-and-the-unread-changes.md`.
  - It covers three things: the plants run again against the mended locks and the tripwire's two new entries; main's
    answers to the 48 checked; and main's changes made for other readers, which no reader has read.
  - The 67 plants and their expectations are committed before any run: 44 from SM-R79 (two re-aimed where the mend
    moved their target) and 23 new.
- **SM-R79b delivered:** `relays/REVIEW_79B_SM.md`, read at main 896cae025. The expectations (6a9e86148) and the
  outputs in relays/sm_r79b/ (590e76f2e) were committed first.
  - **The plants:** SM-R79's 44 now catch 40, against 25 at R79. The 23 new ones catch 5. 66 of 67 results came out as
    expected.
  - **One of SM-R79's plants was not a fault:** s = N // 2 in B567's Weil matrix leaves the spectrum unchanged. So E13
    at R79 was 4 of 8, and this seat's own record is corrected (R79b-SM-09).
  - **The answers:** 42 of 48 hold and one holds in part. Five stay open: SM-43, as main said, and SM-44 to 47, with
    the builder.
  - **Findings R79b-SM-01 to 11:**
    - the owner's chosen words still stand as quotations in the plan, the register and two arcs, and two locks
      assert them;
    - two counts in B1889's agy-lane card have no list behind them;
    - the tripwire's new entries match one spelling and accept any nearby marker, and it does not read papers/;
    - E6's lock does not hold the page's statement of the kernel;
    - B1885's claim line still gives 30 digits for all.
  - **What was read:** B1886, B1888, B1890, B1891, the governing pages, B1889's builder and its agy-family part, and
    B1726's and B1753's dated notes. Their numbers were recomputed where they could be.
- **M6 to M9 read** (main @ 5c7abd72a). The listener is not running, so the page is read by hand at each push. Four
  messages were waiting.
  - **M6:** SM-C3 is received. SM-C4 is approved as proposed, with one addition: where the record's nineteen and the
    Standard Model's nineteen differ as lists, the table says so row by row.
    - It may open the total-inputs scoreboard, in its .md and .json files.
    - It must not open the framing ledger, the file of the two held-out targets, the measured masses under B1637, the
      look ledger, or the looks' outputs under B1839 and B1841.
    - A verdict line that carries a figure for a held-out target is left unread, and its cell says so.
  - **M7:** the second round's nine findings all held. The tripwire is widened, and two cases are held open in a
    fixture.
  - **M8:** card SM-R80 for Review 80, committed with main's scope:
    `relays/cards/SM_R80_review-80-four-arcs-seven-differences-instruments.md`.
  - **M9:** Review 80 first, then SM-C4. After those comes a card to propose for WP-1.9: for each fork the
    foundation's § 8 names, the computation that would decide it, with nothing run and no value stated.
- **SM-R80 delivered:** `relays/REVIEW_80_SM.md`, read at main c40446392. Its outputs in relays/sm_r80/ were committed
  first (02216c5bb, 35a19ca55).
  - Three readers within this session took the arcs. Every finding was checked again here: 56 quotations by machine,
    and each number by rerunning its script on a fresh checkout or by this seat's own code.
  - **41 findings, 31 of them minor.** B1641's corrected sign holds, by this seat's own exact recomputation.
  - **The largest:**
    - ten arcs of Review 79's window were read by no reader;
    - the owner's sentence still block-quoted in the plan, and required by its builder and lock;
    - two holes in the listener's new amendment check;
    - the atlas's tag still printed as a status;
    - a lock that would not see the attribution half of B1893's case closed.
  - One candidate touches this seat's own answer to SM-16, and is named and left.
- **SM-C4 delivered:** `relays/SM_C4_INVENTORY.md`, the parameter inventory with no value on the page. The count it
  must match was committed first (a85ea5bda).
  - It lists 28 rows: the Standard Model's 19, the Dirac neutrino sector's 7 and 2 Majorana phases.
  - Each row gives the name, the kind, whether it carries dimension, its definition with the scheme and scale a value
    must name, its Lagrangian term, the record's coordinate, and what the record says.
  - **Row by row against the record's nineteen** (M6's addition):
    - eight mass ratios and y_t stand for the nine masses, so claims are in ratios;
    - J does not fix the CKM phase δ;
    - (m_H, v) stands for (μ², λ);
    - g_1's normalisation is unstated;
    - the neutrino rows are absent;
    - four rows lie outside the Standard Model.
  - The table's checks were run with three plants (a deleted row, a figure in a definition, a parameter under a second
    name): 3 caught, and the control passes.
- **SM-C5 proposed** (M9): `relays/cards/SM_C5_wp-1-9-the-deciding-computations.md`. It covers WP-1.9's first step,
  three forks of GENESIS § 8: FK12, the register (with its four sub-questions), FK7, the deck, and FK8, the join.
  - For each, it writes down the computation that would decide it: what is computed, on which object, what each
    outcome would mean, what it rests on, what is already on record, whether it can run now, and its firewall status.
  - Nothing is run and no value is stated.
  - A checklist script with three planted entries is the control.
  - In this seat's words, it waits for main's word (§ 6).

- **M12 read** (main @ 204ee91ed): Review 81 is opened. The card SM-R81 is committed as main gives it
  (`relays/cards/SM_R81_review-81-b1898-eighteen-differences-ledgers-instruments.md`). M10 and M11 were read
  before it; SM-C5 waits behind this review.
- **SM-R81 delivered:** `relays/REVIEW_81_SM.md`, with 11 findings. The checks are in `relays/sm_r81/`: 21 of 21
  quotations found, the control missing, and the recount's planted control disagreeing.
- **SM-C5 delivered:** `relays/SM_C5_WP19_COMPUTATIONS.md`, six entries for GENESIS FK12 (i) to (iv), FK7 and FK8,
  written down and not run. The checklist `relays/sm_c5/wp19_checklist.py` passes on the page and catches its three
  planted copies (`relays/sm_c5/wp19_checklist.json`). GENESIS FK12 (iv) has no data-free deciding computation; its
  entry needs a sealed card. Two things are asked of main on the page.
- **SM-C7 proposed,** first pushed as SM-C6
  (`relays/cards/SM_C7_the-slope-and-the-channel-norm-one-l-function.md`): the follow-on of
  B1737 § 4, ranked second by main's Review 74 and never run. It tests Hecke's integral formula in the record's
  conventions: the slope and the channel norm as two coefficients of one L-function along the thread's own closed
  geodesic. It is data-free, with four planted controls, and nothing is run before main's word.
- **M13 and M14 read** (main @ 3bc71803e): GENESIS FK12 is taken as its row is written. SM-C6 is the run of SM-C5's
  data-free entries, in main's order, each step's card committed before its run. M13 was written before this seat's
  L-function card was pushed under the same number, so that card is renumbered SM-C7 and still needs main's word.
- **M15 to M17 read** (main @ f503b1f38): SM-C7 is this seat's L-function card, steps 0 to 2 approved, steps 3 and
  4 held, B1656 not read. SM-C6 is the WP-1.9 runs. At the owner's word SM-C7 runs first. Its step 0
  (`relays/sm_c7/STEP0_CONVENTIONS_AND_EXPECTATIONS.md`) is pushed before the population is computed.
- **SM-C7 steps 0 to 2 delivered** (`relays/SM_C7_ONE_L_FUNCTION.md`). On all 601 characters at 16 levels:
  - B1737's slope is (1/4π²) times the period, along the thread's closed geodesic, of the u-shifted weight-2
    Eisenstein series at the dual point Jc (to 2 × 10⁻¹⁴);
  - the L-function's value at s = 1 is −4 times the arc-length integral of log|g_Jc|, the Siegel function (to 5 × 10⁻¹²);
  - every planted control was caught. Steps 3 and 4 are not run.
- **SM-C7 steps 3 and 4 delivered** (sealed at 664c04531; `relays/SM_C7_ONE_L_FUNCTION.md`).
  - B1656's c_s is F_u + π log Im τ − 2π(γ + log π) at all 601 apexes and on four channels (4 × 10⁻¹¹), with F_u
    the shifted Kronecker limit.
  - Its line part, averaged along the thread, is the Kronecker limit of the thread's shifted partial zeta at Jc,
    whose odd part is the slope. It holds only as the average, not at the apex: outcome A.
  - 3e and P5 did not hold as sealed; the causes are said on the page. Nothing was compared with a measured value.
- **M20 and M21 read:** main banked steps 1 and 2 (B1917), retracted B1918, and banked the channel-norm formula with
  its own check (B1919). **SM-C6 E1's card** (`relays/cards/SM_C6_E1_the-based-count.md`) is pushed before its run.
- **SM-C6 E1 delivered** (`relays/SM_C6_E1_THE_BASED_COUNT.md`): outcome 1.
  - The letters' order is dropped at the manifold.
  - The pieces' order is kept by the based count (n(V), n(V*)) and lost to the class count on the (1, 1) modules,
    which occur on 18 of 24 levels.
  - Level 2 was not run (N = 221). P2 failed as designed, and was redone post hoc; both said on the page.
- **SM-C6 E2 delivered** (`relays/SM_C6_E2_THE_RANK_OF_THE_BITS.md`): the three named bits have rank 2 on the
  record's observables. The hand and the pieces' order are independent; the exchange is carried, so B1327's
  over-count holds. Read against B1915 after the card was pushed: they agree where they meet.
- **SM-C6 E5 part 1 delivered** (`relays/SM_C6_E5_THE_DECKS_ANOMALY.md`). The deck's ℤ/3 anomaly on s961 is zero
  mod 3 on every robust condition, because the orbits are free. GENESIS FK7 waits on part 2, an action's minimum.
- **SM-C6 E6 steps 1 and 2 delivered** (`relays/SM_C6_E6_FILLING_DESCENT.md`).
  - 46 618 modules with rational slope descend.
  - After filling, H¹ counts n + n* on all but 384 of them: filling carries "how many" and not the hand.
  - P1 failed on the slope-0 modules, as said on the page.
- **M22 and M23 read.**
  - **M22's question answered** (`relays/SM_ANSWER_M22_W31.md`):
    - W31's ℂ⁵ is the Weil representation of SL(2, 𝔽₅) for the flux's additive character;
    - the triplet follows m's square class (3 for m = 1, 4; 3′ for m = 2, 3);
    - W31's anomaly-free counts follow m → −m, the swap. They are not a function of the triplet: the hand's bit is
      not the choice of triplet, as far as W31's count goes.
  - **SM-C8 proposed** (`relays/cards/SM_C8_the-partner-test.md`): SM-C5's E3, the partner test through an open
    end, now that E6 is done.
- **Literature note 1** (`relays/SM_LITERATURE_NOTE_1.md`), asked for by the owner. Reading only, plus one post hoc
  check on E6's committed output (`relays/sm_lit/duality_check.py`).
  - SM-C7's identities are classical (Hecke's integral formula; the Kronecker limit formulas of Hecke, Zagier and
    Yamamoto). The record's own content is B1919.
  - Duality with twisted coefficients makes E6's negative a theorem: h¹(V) = h¹(V*) on every closed manifold, for
    the record's modules. The check holds on all 46 618 modules.
  - The record's index is h¹(M; V*) − h¹(M; V) on all 46 618 modules, which duality makes a boundary quantity.
  - Proposed for main's word: three amendments to SM-C8 (vacuous joins; the partner's orders as (V, S) and
    (V*, S*); an index identity as control P3), and a candidate SM-C9 (SM-C7's value at 0 against the U(1) rho
    invariant of the closed torus bundle, an orientation-odd invariant).
- **Scope note on the closed-join block** (`relays/SM_SCOPE_NOTE_CLOSED_JOINS.md`), asked for by the owner. B1351 and
  B1508's row (a) are sound in their frame (an Euler-characteristic count). For today's index the reason is duality,
  with three hypotheses: an orientable closing, no invariants, no singular locus. SM-C8's stated reason is corrected.
  - A non-orientable closing is a new lead, never examined: it would tie the order to the hand.
  - On the one-cusped levels an end is either closed exactly or not at all: the order lives only on open ends.
- **SM-C8's instrument calibrated outside the population** (`relays/sm_c8/calibration/CALIBRATION.md`), on L5a1,
  m125 and L6a4: 3 882 modules, 4 156 joins. The literature note's duality identities hold on every one, and the
  three plants fail. 6 446 joins are vacuous, so leaving them out matters. D_ord is ±1 on 2 956 joins, so the
  instrument can register R; it should report the dimension term and the leak apart.
- **SM-C6 E1's three owed steps done** (`relays/SM_C6_E1_THE_BASED_COUNT.md`, the new last section):
  - **Level 2**, by slopes in two prime fields, checked against B1438's exact slopes at level 1: outcome 1 holds
    there too (labelled differs 6 of 6, census the same 6 of 6).
  - **The read-out on the whole**, through B1881's own instrument: the heights drop the letters' order on all
    16 275 sequences; the mark's line-keeping does not (it differs in 1 456 of 5 575 classes); no module enters, so
    the pieces' order has no way in.
  - **The audit lane's criterion**, checked on 91 840 small systems: sufficient, and exact only as "fibres inside
    observational equivalence". The leads page's "exactly when" fails on 8 664 of them; a wording for main.
- **M24 read.** Main approved the candidate system's page and a determinant −1 card, to be run straight through,
  beside SM-C8, then P-333. Main's correction is entered: the arrow is the hand only at determinant +1, and on m000
  the twist w is the tick parity. The AI trailers are dropped from commits from here on, as main asked.
  - **The page:** `relays/SM_THE_CANDIDATE_SYSTEM.md`.
  - **SM-C10 sealed** (`relays/cards/SM_C10_the-one-tick-object.md`), with main's expectation verbatim and this
    seat's reading of it. It is the independent second computation of the web seat's W-C8, whose results this seat
    has not read.
  - **"Beside SM-C8"** is read as main's word for SM-C8 too, so SM-C8 runs after SM-C10, with the amendments. If
    main meant otherwise, SM-C8 waits.
- **SM-C10 delivered** (`relays/SM_C10_THE_ONE_TICK_OBJECT.md`): outcome A as sealed, decided on m025 (3 ticks),
  not on m000.
  - Twisted duality holds on every module, with V* ⊗ w as the partner and w the tick parity.
  - On odd ticks the twisted and untwisted gaps differ (6 of 96 on m025; post hoc, 20 of 2 420 on m407). On even
    ticks they agree everywhere. The three plants fire.
  - m000 carries no non-split abelian module at any order (t² − t − 1 has no root of unity). On the common point's
    representation (post hoc) its boundary is acyclic, so the twist is invisible there. The tie between order and
    hand shows only where a character sees the tick.
- **SM-C8's addendum sealed** (§ 7 of `relays/cards/SM_C8_the-partner-test.md`) before its run: B1441's tier-1
  population, the three amendments, the controls as stop conditions, and the outcomes R_leak, R_dim and N.
  - **A correction, self-caught:** m129 (L5a1) and m125 are two of B1441's five named manifolds. So the calibration
    page was wrong to call them outside the population. The page is corrected, and the run reports with and without
    them.
- **SM-C8 delivered** (`relays/SM_C8_THE_PARTNER_TEST.md`): outcome R_leak, as predicted, on B1441's tier-1
  population (71 manifolds, 486 754 modules, 175 628 non-vacuous joins of 1 109 760).
  - Every duality control held everywhere, and the plants fire.
  - The partner's order changes P's count on 101 672 joins. On 100 846 the change passes through classes alive at
    the other, open ends; that leak occurs on all 17 of B1441's carriers of |I| = 2.
  - The relation carries the order and does not choose it: D_ord comes in equal ± pairs.
  - The sealed index control was too broad (module choice where H¹(M; ℓ) is a plane); post hoc it matches on all 7
    entries where every H¹ is a line.
- **SM-C11 sealed** (`relays/cards/SM_C11_the-five-ended-companion-in-F-CI.md`): P-333, the F-CI read on o10_150729
  with main's own cell, and the companions' census to word length 10.
