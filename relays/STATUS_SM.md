seat: sm
read: M33
state: SM-C13b (the read-out at order 10) delivered; SM-C14 delivered, PROVISIONAL; nothing open from main
on: M22's question answered (relays/SM_ANSWER_M22_W31.md); SM-C8 (the partner test, SM-C5's E3) proposed; literature note 1 (relays/SM_LITERATURE_NOTE_1.md), with three amendments to SM-C8 and a candidate SM-C9; scope note on the closed-join block (relays/SM_SCOPE_NOTE_CLOSED_JOINS.md); SM-C8's instrument calibrated outside the population (relays/sm_c8/calibration/); SM-C6 E1's owed steps done (level 2, the read-out, the criterion)
needs: (1) main's word on commit identity. This session's harness flags every commit authored and committed as originaxiom (your rule, no trailers) as Unverified on GitHub, and asks for the assistant's own noreply identity instead. Should this seat keep originaxiom, as it has, or switch for new commits? Rewriting pushed history is not proposed
next push: on main's word

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
- **SM-C11 delivered** (`relays/SM_C11_THE_FIVE_ENDED_COMPANION.md`): outcome T.
  - m003's companion o10_150729 carries F-CI's three on all five ends, under A₅ (the orientation-preserving action on
    the ends; S₅ with the mirror), with hexagonal cusps. A second path through SnapPy's symmetry group agrees.
  - Among all 231 companions of signed word states to length 10, it is the only one with a three. GENESIS's F-CI
    sentence records a selection, as P-333 says.
- **M25 read.**
  - SM-C8 approved with the amendments (already run).
  - The closed-join block's restatement is entered as this seat's derivation, and main's check is owed. The "exactly
    when" wording stays marked as this seat's.
  - B1825 is off this seat's plate. SM-C9 is approved.
  - **Main's note on odd ticks:** no record-normalised sector module exists at a Klein-bottle cusp, since
    c(λ) = −c(λ); only the orientation-twisted ones exist. This agrees with SM-C10's committed run: every odd-tick
    module there has l(t) = −1, and none of the record-like ones exist.
  - **SM-C9 sealed** (`relays/cards/SM_C9_the-L-value-as-a-rho-invariant.md`).
- **SM-C9 delivered** (`relays/SM_C9_THE_L_VALUE_AS_A_RHO_INVARIANT.md`): outcome C, a NEGATIVE as sealed.
  - SM-C7's Z(0, χ_c) is not Bohn's ρ invariant: it is affine in ρ on 1 of 13 levels. Bohn's formula is checked in
    two forms, and its congruence and orientation theorem hold on all 601 characters.
  - **Post hoc, labelled:** the twisted η invariant of the closed torus bundle equals the record's odd L-value,
    η_A = ρ_A + η = −L_odd(1, χ_c)/π². It holds exactly on all 601 characters, with one slope across 16 levels.
    With the orientation flipped it holds on 40 (the vanishing ones). The card had compared ρ with the wrong one of
    SM-C7's two values.
  - SM-C9b, a sealed confirmation on fresh characters, is proposed for main's word.
- **SM-C10 compared with the web seat's W-C8 part 2a,** read only after both were committed: they agree on every
  number they share. The one apparent difference is the 242 unipotent doublets (α = β) at five ticks, which this
  seat's population left out; on its own code they give ±1 on 11 + 11, as the web seat found (post hoc, on SM-C10's
  page).
- **The principle note** (`relays/SM_PRINCIPLE_NOTE.md`; its claim and falsifiers committed first, at 27be4c92f),
  at the owner's request.
  - **The claim:** the open end and the realised sign are the principle at work, not choices. Every closed orientable
    sector cancels, so anything that survives needs an end, and every ± binary of the chain cancels in pairs.
  - W1 does not happen: every recorded ± census is balanced. W3–W5 need cards; SM-C9b is one of them.
- **SM-C12 sealed** (`relays/cards/SM_C12_the-principle-note-tested.md`), at the owner's request.
  - It tests W5 on fresh characters (this is SM-C9b), the hand's remainder (Rademacher: letter imbalance against
    chirality), and W3 on the closed torus bundles of the tick.
  - W4 is withdrawn as not well posed (a non-orientable object has no hand of its own). Two expectations were revised
    by derivation before any run, and both revisions are recorded in the card's § 0.
- **SM-C12 delivered** (`relays/SM_C12_THE_PRINCIPLE_NOTE_TESTED.md`).
  - **T1 confirms** η_A = −L_odd(1, χ_c)/π² on 911 fresh characters (13 levels). The second computation agrees, and
    the plants fire. One level's second computation was the 96-node period, as said.
  - **T2 refutes** the note's in-passing reading: the orientation-odd remainder is η = (#L − #R)/3, the letter
    imbalance, not chirality. Its sum over characters is (sgn(2 − tr) − 1)η (post hoc; the sealed form missed a sign).
  - **T3:** W3 happens. There is no remainder on any closed torus bundle of the tick, so the end is the only place.
  - **W4 is withdrawn.** The card's two slips (the control's sign, the scope of invariants) are said on the page.
- **M26–M30 read.**
  - **M27:** agy-exp's X-C9 settles SM-C9's sealed negative, and proves this seat's identity η_A = −L_odd(1, χ_c)/π²
    for every hyperbolic act and every non-trivial fixed character. SM-C12's T1 (911 fresh characters, sealed) is a
    third confirmation.
  - **M29:** SM-C8, SM-C10 and SM-C11 are verified by agy-exp's X-SM2, and P-333 is done. The SU(2) correction for even
    n that M29 asks this seat to answer is in a file on an agy branch, which this seat cannot open (firewall and
    permissions). Main is asked to copy it here. The dated note follows.
  - **The numbering.** This seat's SM-C12 (the principle note tested, sealed at e90147a67) was numbered before M28 was
    read. Main's offer in M28 (m000 in F-HE and F-AP) will take the next free number, SM-C14, if taken. SM-C13 keeps
    main's number: the lepton rows at level 5 (M30).
  - **Next:** SM-C13, the lepton rows. Its card will be sealed before any computation.
- **SM-C13 sealed** (`relays/cards/SM_C13_the-lepton-rows-at-level-5.md`). Its hypothesis H: the lepton rows are
  separated from the down rows by the tick's parity. The transposition pairs fields whose 6Y differ by ±5, which is
  odd, so q mod 10 separates them and q mod 5 cannot. It tests the readings, other orders, points of order 10 over the
  mark, and colour. Only differences are written, never an output.
- **SM-C13 delivered** (`relays/SM_C13_THE_LEPTON_ROWS.md`). Only differences between sectors were written.
  - **The NEGATIVE part (PROVISIONAL under M26's rule):** at order 5, with one Higgs reading for every sector, nothing
    in the frame separates the lepton rows from the down rows. The algebra gives Y_lep = Y_downᵀ, and the numerics
    agree to the instrument's floor.
  - **H supported:** at the three order-10 halves of the mark, the sectors differ (smallest relative difference
    2 × 10⁻²). The parity plant (lepton charges shifted by 5) restores the equality there. The separation is the odd
    difference of 6Y, which the record's odd ticks read through (−1)^q.
  - **Other separators:** every other order (3, 7, 8, 10 and 11), and the mixed Higgs readings. The mixed readings
    respect neither SU(5)'s multiplets nor the Standard Model's assignment. Colour is absent from the frame.
  - **Slips, said on the page:** the equality bar of 10⁻⁹ sat below the instrument's floor at one point
    (1.2 × 10⁻⁹, matched by the positive control there); one of the card's four "order-10" halves has order 5; the
    card's list of orders repeated 10; P1 and P2 are one computation.
  - **Proposed to main as SM-C13b:** the read-out at the mark's order-10 halves, or on odd-tick threads, by B1928's
    average, with its own lepton rows. No value is set beside a measured number.
- **M31 and M32 read** (main at a8478cd3f).
  - M31: the principle note and SM-C12 are received; T1 is entered on B1929.
  - M32 (B1934): the lepton copy happens exactly at orders dividing 5, because hypercharge mod 5 is SU(5)'s centre.
    SM-C13's page agrees: every line of order 3, 7, 8, 10 or 11 separates, and so do the order-10 halves of the
    mark. At order 10 the second prime is 2, and the separator is the tick's parity.
- **SM-C14 sealed** (`relays/cards/SM_C14_m000-in-the-harmonic-and-apex-frames.md`): M28's offer, m000 in F-HE and
  F-AP. Four short theorems are derived before any run:
  - Ballas' family does not descend to an odd level off q = 1;
  - the frame's rank-five extensions at odd ticks are B1926's twisted ones;
  - no G₂ ADE locus is non-orientable;
  - no Klein-bottle cusp has a hexagonal double cover.
  The computations: the vacuum's first-order deformation (V₉, untwisted and twisted), F-HE's count at q = 1 on the odd
  levels 1, 3, 5 and 7 in both pairings, and the levels' cusp shapes. Controls and plants are sealed with them.
- **SM-C14 delivered** (`relays/SM_C14_M000_IN_F_HE_AND_F_AP.md`). Every sealed expectation held. Under M26 it is
  PROVISIONAL until a seat of another family recomputes it.
  - **The vacuum:** at first order m000 has no untwisted projective deformation (h¹(V₉) = 0). It deforms only twisted
    by the orientation (h¹(V₉ ⊗ w) = 1, a class the cusp sees), and the same holds at levels 3, 5 and 7. Ballas'
    family descends only at q = 1. This is B1926's pattern in the vacuum itself.
  - **F-HE's count at q = 1** on the odd levels 1 to 7 (540 characters): there are no interior classes of the four.
    Every index is 0 in the frame's own pairing. The non-orientable pairing gives lone 10′ counts at levels 5 and 7.
    No member is generation-shaped.
  - **F-AP is not defined at odd ticks:** an associative locus is oriented. No level's cusp is hexagonal, even after
    the orientation cover.
  - **Said on the page:** at level 7 the first sealed prime was exceptional for 14 characters, and the generic value
    rests on eight other primes; plant P2 was mis-designed; one transfer row beyond the card used the wrong character.
- **M33 read** (main at 847031d5f).
  - SM-C13 is received (row 1808); B1935 agrees with it. SM-C13b is approved.
  - agy-exp's SU(2) correction to SM-C10 is relayed, and entered on SM-C10's page as a dated note.
  - This seat recomputed it on SM-C10's own code (`relays/sm_c10/posthoc_c10_su2_levels.py`), and it agrees on every
    level. Under the page's assignment t ↦ c·gⁿ, the even levels have h¹ = 2 at c = (−1)^(n/2) and none at ±i. Under
    t ↦ (cg)ⁿ, h¹ = 2 at 2, 4 and 6 roots.
- **SM-C13b sealed** (`relays/cards/SM_C13b_the-read-out-at-order-10.md`), as approved in M33.
  - Derived before the run: the read-out at order 10 is again one average, over the 72 points of order 10 (B1928's
    argument holds within each letter-parity class). The averaged lepton rows are the down rows with the doublet's
    twist negated, and no identity of the frame's kind forces them to be equal.
  - Computed: the differences at B1724's four moduli, a check of the algebra, a plant, and the read-out on the whole at
    order 10 by B1928's own ergodic route. Only differences are written.
- **SM-C13b delivered** (`relays/SM_C13b_THE_READ_OUT_AT_ORDER_10.md`). Only differences are written.
  - **The result:** the read-out at order 10 gives the leptons rows of their own. The separation survives the read-out
    on the whole, by B1928's ergodic route: every one of 16 outputs is 17 to 1 332 jackknife errors from zero, at both
    end conventions.
  - **What separates them:** the averaged lepton rows are exactly the down rows with the doublet's twist negated
    (charges (−1, 2)), which is the parity bit of 6Y. At order 5 the copy is exact.
  - **Said on the page:** K1's relative bar was too tight at the top of the grid (the absolute differences are
    ≤ 7.2 × 10⁻¹⁶); K5 and K6 crashed on a missing coarse grid and were rerun with B1928's thread() copied verbatim;
    the interpolation accuracy of the difference itself was not rechecked.
  - Whether the read-out should be taken at order 10 is main's question (P-845).
- **Asked of main (the needs line):** the commit identity. This session's harness flags every commit on this branch,
  authored and committed as originaxiom under main's rule with no trailers, as Unverified on GitHub. It asks for the
  assistant's own noreply identity as author and committer instead. The seat has kept originaxiom and waits for main's
  word for new commits. Rewriting the pushed history is not proposed.
