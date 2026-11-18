# B1957 — The seats' claims register: every statement of every seat's notes in the window, each to be read at its source and verified, none dropped

**Verdict: OPEN** (a working register; it closes when no statement is pending and each seat has said its harvest is
complete). Main, 2026-11-17, under the author's rule of that day: no claim of any seat is ignored, and no claim goes
unverified and unregistered. No measured number is used. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /claims register|every claim|no claim|claim by claim|unverified claim|harvest debt/: 23 of 1698 arcs on main match (NEGATIVE 3, OPEN 1, PROVED 19); 8 register rows match (DONE 6, QUEUED 2)`.
- **What the record already holds:** the harvest ledger (one row per delivery, rows 1 to 1881), the lanes' pins, and
  the arcs B1954 to B1956, which entered the window's deliveries by reading notes and summaries. Those rows register
  deliveries. They do not register claims, and most of what they cover was not verified.
- **Why this arc:** main reported that harvest as done. It was not. The rows were written from summaries, and the
  seats' central claims were not recomputed. This register is the unit the rule needs: the statement.
- **The literature:** none is used here.

## What is registered (`verification/extract.py`, `verification/UNITS.json`)

Every markdown file a seat added or changed between its pin before the window and the head harvested to, split
mechanically into units: a bullet or numbered item, a table row, or a paragraph. A unit is a **statement** unless it is
a label line, a table's header row, or shorter than 25 characters.

| lane | from | to | files | statements |
|---|---|---|---|---|
| agy-exp | `ef140a024` | `017266d87` | 86 | 2,040 |
| agy-002 (verify) | `53ac6c7d` | `62420b533` | 11 | 500 |
| agy-002 (endgame) | `613c4f417` | `94e511f54` | 12 | 207 |
| agy-002 (closure) | `94e511f54` | `358d61786` | 18 | 271 |
| physical (codex) | `1aa76251` | `f0411fd82` | 129 | 10,781 |
| the web seat | `b1727da04` | `401c9bd7e` | 15 | 955 |
| agy (audit) | `da5c7125` | `d1c71f255` | 4 | 124 |
| **all** | | | **275** | **14,878** |

- The committed file holds each unit's id (lane, file, first line), its form and a hash of its text. The text is read
  at the source, at the pinned head.
- **Not covered by this extraction, and owed:** results that exist only in a seat's code or raw outputs; the builder's
  lane (all of it landed as commits on main); the 74 older rows of the harvest ledger whose own status says not read or
  not verified; the agy lanes' raw outputs, which are behind the mask.

## How a statement is settled (`verification/build.py`, `verification/records/`)

A statement is **pending** until a record names it. A record gives a verdict and how it was reached:

| verdict | meaning |
|---|---|
| VERIFIED | recomputed on main's own code, and it holds |
| REFUTED | recomputed and it fails, or contradicted by a verified fact |
| CONDITIONAL | holds given premises the record lists; the premises are not derived |
| PARTIAL | part of it checked; the record says which part |
| SUPERSEDED | withdrawn or corrected by its own seat; the successor is named |
| NOTED | not a mathematical claim (custody, a request, a plan, a caveat); the record says what was done with it |

A file is **read at its source** only when a record says so. Reading a summary of a file does not count.

**The state is in `REGISTER.md`**, generated, by lane and by file. Nothing main did before this arc is carried over
as settled: what it verified earlier (B1951 to B1956) is entered as records only against the statements it actually
covers, file by file, as each file is read at its source.

**The first file settled, as the pattern:** the web seat's W-A1 (127 statements). Main had called it verified on the
strength of its Part 1. Read at its source, it needed three further scripts (`verification/checks/web_wa1_*.py`):
frame C at τ = i row by row, the remaining algebra, and the third reading. Of its statements 67 are verified, 4 are
partial (two of the note's figures are not reproduced by main), 3 are superseded by the seat's later notes, 53 are
noted, and none is pending.

## What the work has established so far (kept current; the counts are in `REGISTER.md`)

- **Main now has its own two-loop running of the Standard Model, from the primary sources.** Transcribed by main from
  Luo and Xiao (hep-ph/0207271, the full matrix equations) and from Buttazzo et al. (arXiv:1307.3536, Appendix B),
  both read in the papers' PDFs (`verification/checks/sm_rge_matrix.py`, `sm_rge3.py`, `sm_rge.py`). The two
  transcriptions agree to 4e-16 on seven beta functions; the result is basis-independent to 9e-15; and it reproduces
  agy-002's sealed benchmark for the quartic's zero crossing, 7.578626559316 against its 7.578626559317. Every
  corridor the seats claim runs on such a solver, so this is what their relations will be recomputed with.
- **Three findings of one seat about another, settled at the primary source:**
  - the quartic's two-loop term is −48 λ² Tr_Y, and agy-exp's routine at `2ff7784b1` had −24 (the physical lane's F12:
    verified);
  - the two mixed products in the two-loop Yukawa equations were exchanged in agy-exp's X-ENDGAME, and its benchmark
    coefficient 7 is the exchanged order; the right coefficient is 11/2 (the physical lane's counterchecks 2 and 3:
    verified; the two orders differ by exactly (3/2)·y_t²·y_b²·cos²);
  - the phase of det(Y_u Y_d) does not run at one or two loops, for any Yukawa matrices (main's algebra, and 4e-16 on
    main's solver): so agy-002's strong-CP statement holds given its premise, Hermitian matrices at the Pati–Salam
    scale, which is borrowed.
- **agy-002's gates 0 and 1:** the exact items hold on main's code (the slopes from the field content, the matching
  weights, Riley's cusp in exact arithmetic, the maximal cusp, the 27 of E₆, the corridor's closed form); its sealed
  trails are in the order it names and its scripts carry no float literal, checked without running them
  (`verification/checks/custody.py`). Its own gate 1 says the corridor is not parameter-free.
- **The web seat's W-A1:** settled in full, as described above.
- **agy-002's two campaign branches, read at their source in full and recomputed: gates 0 to 7B, their cards,
  errata, syntheses and status pages (30 files, 478 statements: 197 verified, 9 refuted, 47 conditional, 53 partial,
  158 noted, 14 pending; the 14 are its audit of the other lanes, settled with those lanes).** What main built for
  it, each from its definition or a primary source:
  the closed-fibre triple overlap of three zero modes of flux 3, 3 and 6, by quadrature and in closed form
  (`checks/cim_overlap.py`, `cim_closed.py`); the mass term's running and the two thresholds
  (`checks/agy002_g3.py`); and the checks of each gate (`checks/agy002_g2.py`, `level6_higgs.py`,
  `high_cusp_levels.py`, `agy002_g4.py`, `agy002_g5.py`, `agy002_g6.py`, `agy002_g7.py`).
  - **Holds:** the triple overlap is covariant under both generators, with the spin structures the seat names, and
    each balance, broken, breaks it; the cusp exponents at orders 5, 10 and 15 (the lepton and down minima equal at
    5 and 10, in ratio 3/2 at 15); the mixing's two-loop slopes; the mass term's anomalous dimension (two primary
    sources agree); both threshold signs, derived by main and equal to the published corrected matching; the
    linear algebra and the anomaly sums of gate 4; the cocycle, the periodicities and the even-Δ family Gramian of
    gate 5.
  - **Refuted (gate 2, the Higgs mode):** the Higgs's Wilson line is ±3w/2, so it is not a function of the point w on
    the torus. The seat's sum takes one lift of each point and so is not covariant; averaged over the four lifts,
    the bubble of every single point is an exact multiple of the identity on the six Higgs modes, for a three-line
    reason. It selects nothing: the ground space is two-dimensional, one bit, not zero.
    *[Corrected 2026-11-18, at the physical lane's findings C8-02 and C8-04, each checked on main: the ground space is a
    complex plane, and every unit vector of it is a ground direction of the quadratic problem. "One bit" holds only if
    the direction is restricted to the two eigenlines, which nothing computed forces. And the negative is for the
    prescription that averages the bubble over the four lifts, not for every covariant response.]*
  - **Not resolved (gate 5, P-861):** with hypercharge as the Wilson line the mixing in this frame is deranged (at 15 of
    the 24 points the heavy directions are apart: 10 orthogonal and 5 with the down direction outside the up matrix's degenerate pair; 9 inside that pair; none aligned at the seat's representatives, 4 under two of the lifts *[counts restated 2026-11-18, Review 84: the page said "15 of 24 points orthogonal"]*) and lift-dependent; with one Higgs mode the
    mixing matrix is always a permutation; the reported alignment at 288 points is one matrix compared with
    itself; the small angles shown are typed in. This agrees with B1946 and B1947 on main.
  - **Gates 6, 7 and 7B:** every figure reproduced on main's own code: the three Majorana tensors and their
    covariance; the Pati–Salam stage's two-loop coefficients, derived from the field content; the 243 histories (the
    gauge residual in [0.0007265, 0.0027548], √(2λ) in [0.370482, 0.771511], to every digit the seat prints); the
    counts 19 and 28 from exact ranks 41 and 44; the Casimir slope as a closed negative integral; E₈'s 0 against 9
    colour singlets. What they rest on is typed in or borrowed: the neutrinos' first column, the grid's ranges, the
    quartic's boundary value, and the table of ranks, which is the seat's own classification propagated.
  - **The ten relations PR-1 to PR-10, one by one:** `RELATIONS.md`. Two verified identities of known structure,
    one verified set of negatives, one refuted, one not a relation, five conditional on the left-right model. None
    removes a free number from the count.
  - **Found by reading the scripts' text:** at gate 0 the first script carried the exchanged mixed products and the
    second did not; the benchmark compared each with its own copy and did not see it. The seat's gate 4 repairs it.
  - **Conditional:** every statement resting on the left-right model's content, parity or scales; the Casimir
    curve (chosen counts, one mass, no geometry of the manifold); one clause on the neutrino's threshold, whose
    finite part changes sign with the matching scale.
- **Three seats have answered the request for a review; none says its harvest is complete.** Their lists are work
  orders, and the first items are done:
  - **The web seat** (its status page at 9a5aafe40; W-H1). Six corrections to main's record, all right and all taken
    the same day (B1952, B1953's neighbour B1955, the picture page's § 7, harvest rows 1848 and 1867). Four of its
    results that only its referee read had computed are now on main (`checks/web_review.py`, `web_wa1_reps.py`,
    `web_wa1_h2.py`): its 2 of 32 candidates; its H2 in both measures; the identifications of the Weyl operators for
    every Weil class; the flux-5 modes' class; the relabelling that removes frame C's down phases. W-H1's count is
    reproduced on main's instrument: 116 relays have no relay-ledger row.
  - **The physical lane** (its delivery at 8d5c91032). MAIN-01 is right: a sentence of main's own B1953 was a factor
    of two off (tr O₃ = F/2), corrected. Its observation on the join is verified (`checks/physical_main01.py`): the
    part of B1953's operator that commutes with the whole gauge group is −(F/12) ⊗ 6Y, so the generic operator is not
    a gauge intertwiner and only the phased sum survives under those hypotheses. Its ranked list of five proof
    packages, the complete-cusp inverse first, is the order main reads them in.
  - **agy-exp** (its page of premises at 48a4054aa) states of its own seven relations what main found of agy-002's
    ten: each rests on a supplied model, a free scale or a typed-in number; and that three families is an input.
- **The window was widened to the seats' present heads:** 285 files, 15,320 statements.
- **agy-exp's seven relations, read at their three result notes and assessed one by one** (`RELATIONS.md`). The exact
  arithmetic of its own exponent rule is reproduced on main from the rule as stated (`checks/agyexp_ur345.py`: the gap
  ratios {39/31, 5/3}, {15/11, 15/8, 431/190, 15}, {10/7, 31/5}, {29/26, 10/3}; the identity through 6w at order 15;
  no multiplier at order 10). None of the seven is a statement about the object alone; its own page of premises says
  so. UR-6 is two elementary facts and two premises, and its own control shows its overlap is not a function of the
  point on the torus.
- **The web seat's W-B2, stage 3, on main's frame** (`checks/wb2_stage3_on_main.py`): frame C at (−q_R, −q_L) is frame
  C transposed, exactly; the mixing read with right vectors differs by up to 0.84; at the c = +2 charges the leptons
  are the down quarks transposed at all 24 points of order 5 and not at order 7; c = +2 differs from frame C by up to
  2.35. Stage 4 (the norms) is still owed.
- **The physical lane's first proof, the complete-cusp inverse (P-C3e, equation (3)), read in full.** Its
  channel-by-channel steps hold exactly on main (`checks/physical_c3e_indicial.py`: the reduction, the exponents −β and
  1 + β, which the measure admits, the decay with its constant 1/(ℓ²c − δ − δ²), the Bessel solutions at nonzero
  angular frequency). The bijection itself is recorded as conditional on four things main has not yet checked, named
  in the record; no lemma has been found to fail. Its nonlinear part rests on the lane's earlier files, not yet read.
- **agy-002's verify branch is settled: 11 files, 500 statements, none pending** (284 verified, 3 refuted, 52 partial,
  161 noted). Each of its four second computations is reproduced on main's own code:
  - the order-5 copy of the down quarks by the leptons and its failure at order 10 (`checks/agy002_m33.py`);
  - its blind values for the read-out on the whole, which agree with B1940's corrected file in all four options under
    the rule main committed before any seat's output existed (`checks/agy002_m37.py`);
  - its closed law for the twisted Higgs triplet under τ → τ + 1, which holds to 2.8e-40 and gives, digit for digit,
    the ratios main's own B1947 run printed: B1947's negative now has its reason in closed form (`checks/agy002_m40.py`);
  - its twisted-η amplitude (`checks/agy002_m34*.py`): the step is an integer cocycle, the transfer matrix has spectral
    radius 1/√2, so the history sum decays to zero with a changing sign and a ratio normalised by it does not converge;
    the odd ticks are not cancelled (η is exactly zero on their double covers); no weight tried closes the gap of about
    0.52 between the move count and the area.
  **Found in its notes:** three rows of one table are misprinted against its own sealed output; one printed closed
  form is wrong by a sign and a factor of two; five commit hashes on its status page and one card's file name do not
  exist (the deliveries do, under other hashes, in the right order).
  **Found about main:** main's canonical end is held constant above its table's top height, and the seat's goes on to
  the cusp limit; that alone is the 2 percent between the two seats' figures at height 30 (`agy002_m34_gram.py`, G4).
- **Its Review 83 reading: all 31 findings rest on facts that hold on main's files** (`checks/review83_agy002.py`): six
  are the plants, seven are mended, and **eighteen are faults that still stand on main's head**, among them three locks
  that cannot fail and the unconditional grade on the public claim page. They are action item R83-1, the builder's
  series; main has now verified each.
- **The web seat's second reply** (its status page, section 5): its two remainders are mended (B1953's note and
  B1955's one-line claim now say the top wedge's invariance is generic and conditional); its correction of its own
  relabelling sign and its lepton by-product are recomputed on main (`checks/web_review.py`, R5). It does not write
  HARVEST COMPLETE.
- **The web seat's owed computations, taken in its order** (2026-11-18):
  - **Frame D1 with the Higgs's twist in the Szegő factor (W-B2, stages 3 and 4), rebuilt on main's own functions**
    (`checks/web_wb2_d1.py`). Frame C's bilinear is v_x·v_yᵀ/θ₁ (1e-33). At its pole D1's coupling is frame C's at the
    charges q − c·q_H/2 times one scalar, for every c: three lines by hand and 5e-16 by number. Off the pole it is
    frame C at those charges times a scalar of modulus e^(k·Im u), k = −2π·c·q_H·a (−15.08 for up at the mark). With
    the bundle's metric the two are equal at every point; a flat norm over a cell depends on where the cell is cut.
    **So D1 is frame C at shifted charges, with the norms too, and adds nothing beyond it.** B1947's twisted triplet
    still fails on the corrected placement.
  - **Hecke's period at discriminants 12 and 40 (W-Z1)** (`checks/web_wz1_other_discriminants.py`): one half of the
    full Dedekind zeta at 12; at 40 the partial zeta of one class, ½(ζ·L(χ₄₀) ± L(χ₅)·L(χ₈)), with the sign by class
    (2e-14 at s = 3). Discriminant 40 is the right control, as the seat's correction says.
  - **The result that stood only in an output** (`checks/web_posthoc_closure.py`): the degrees (2, 2, 1) close for
    down and leptons only with the Higgs's charge set to 0; with the charge that conserves 6Y they close nowhere.
  - **W-L1** is noted and not recomputed: it compares with data, and its second computation is the SM seat's re-run.
- **Six of the web seat's eight earlier notes, never read before, are read in full and settled** (they are added to
  the register's window): W-F24 and W-F25 (the height law, the measure's height shares, and the cusp exponents, which
  are B1945's cell by cell; `checks/web_wf24_wf25.py`), W-C2 (agy-exp's four theorems: the census's 228 and 124
  classes and least volumes by SnapPy, the E8 and A4 counts; `checks/web_wc2_census_and_lattices.py`), W-C3 (the SM
  seat's items under banked arcs: its figures are main's, and its one correction to B1675 is on the page), W-C4 (the
  agy lane's Theorem C; `checks/web_wc4_theorem_c.py`). Two are still to read: P-783 and the content in weave form,
  with W-F17.
- **The last three of those notes, and W-A2, W-A3 and W-H1, are settled** (2026-11-18, later):
  - **P-783, beyond B1912** (`checks/web_p783_spectrum.py`, B1912's own Hejhal routine at three heights): the seat's
    fifteen values to R = 11 are states in exactly the 27 (value, class) cells it names (2.5e-8 at most there, 1e-3 at
    least in the other 33); the agy lane's two values are not states; and **there is no exceptional eigenvalue** for
    R = it, 0.01 ≤ t ≤ 0.49, the range B1912 could not see. That the list is complete is not proved by main either.
    **Found about main's instrument:** B1912's two heights share the argument 2π·0.6, so above R = 6.73 its two-height
    test has false minima at the zeros of the Bessel function; B1912's own range is below them and its result stands
    (a dated note is added there).
  - **W-F17** (`checks/web_wf17_on_main.py`): all eighteen counts of homomorphisms and surjections onto 2T, 2O, 2I; the
    trace maps' listed components, projections and the count of components over ℚ (1, 2, 2, 4, 3, 6); E18 and E19.
    Its class-index census and its completeness tests are partial.
  - **The content in weave form:** its table of W154's verdicts is exact arithmetic on W154's formula; its two asks
    are done (harvest row 1641; a dated note on P-380).
  - **W-A2 and W-A3** are settled against main's own recomputations B1952 and B1955, with the corrections of both.
  - **W-H1's four asks are paid:** the relay ledger has a row for each of the 116 relays that had none (14 banked in
    this register, 102 open with their pointers); two dated notes in the harvest instrument answer the other two.
- **Two landings were refused on 2026-11-18, both by main's own state:** the point-debt gate's clock (a register row
  citing an unlanded draft for 8 days), and an edit of the register made while a landing was at its gates. Both are
  mended; one old debt was paid on the way (P-092: the claim page's cubic row now says that with Higgs content in
  27s the down quarks and the charged leptons have one spectrum).
- *[Dated 2026-11-18, later: the next sentence was true of the window as it stood that morning. The window was
  widened the same day at the seat's word (below), and the lane has pending statements again.]*
- **The web seat's lane is settled in full: 24 files, 1,850 statements, none pending** (791 verified, 144 partial, 22
  superseded, 893 noted). Its view's five own checks are redone by hand; its cards and log are read.
- **The agy audit lane is settled in full: 4 files, 124 statements, none pending** (44 verified, 13 conditional, 17
  partial, 50 noted).
  - Its closed form for the shifted Kronecker limit is, term by term, the function main's own frame uses (B1919's);
    its cusp criterion follows from it, and its worked example is right by hand.
  - Its note on the register-to-field join was scrutinised claim by claim in B1866. Its revision after B1866 (the
    'half-form' channels) is tested as algebra (`checks/agyaudit_p753_halfforms.py`): the four orders 96, 288, 72 and 24
    are right; which of its modes carries which line is its own analysis and stays conditional.
- **The web seat's third reply (its status page, section 6, written before M45) is read and registered** (23
  statements). It checked main's records of M44 against its own sources and found them right. Its recount of the
  register at main d44ed1564 is exact on main's recount (1,228 statements, 908 pending there). Everything on its list
  of owed items has been done since, except W-L1's calibration of one row (a comparison with data: noted, not
  recomputed). It has not written HARVEST COMPLETE and has not yet answered M45.
- **What the physical lane's registered statements are (found 2026-11-18).** Of its 10,952, 7,645 are rows of
  `docs/SEAL_LEDGER.md`, a generated view its branch carries from before the window. The lane changed that file by ten
  inserted lines (`checks/physical_seal_ledger.py`: no removal; the base's 9,411 lines are the head's first 9,411).
  - The three seals in those lines are verified: each hash is that of a version of the named file in the branch's
    history.
  - The other rows are noted as not this lane's work. Counts reported before this date overstated the lane's share:
    its own material is about 3,300 statements in 135 files.
- **The physical lane's P-C3e, the nonlinear part** (the two implicit-function steps to a local stationary family, and
  the second-order correction on balanced forms): both proof files read in full.
  - The algebra holds in a model of main's own with the same structure (`checks/physical_c3e_two_steps.py`): the sign
    and factor in d mu(I k psi) = -2 k†k psi, the gauge parameter of order t², the Q moment t² e_Q (1 − ρ²) with slope
    −2 e_Q, independence of the auxiliary projection, the mass 4 e_Q² t², the cancelled quadratic moment.
  - A finite-dimensional model has no analysis in it. What carries the argument to the lane's fields on the cusp (the
    bounded inverse between weighted spaces, analyticity there, the centraliser being Q alone, regularity) is
    **conditional**, as the lane itself says: an author's proof, review pending, no input removed.
- **The physical lane's first package (P-C3e, seven files, 206 statements) is settled.** Its three remaining proof
  files were read in full and their exact content rebuilt on main (`checks/physical_c3e_roster.py`):
  - **Verified, from E8's own 248 weights and explicit matrices:** the roster under the two principal triples; the
    reflection's phases; the cubic's three channels; under one so(5) the 248 is one adjoint, eleven vectors,
    thirty-two spinors and 55 trivial directions; the pencil's ranks 180 and 148 (68 and 100 summands); and
    Tr₂₄₈(ad X)⁸ = 120 λ⁸ = (15/2)(Tr₅X⁴)² on the whole family, with the fourth-power trace cancelling (−12 + 44 − 32).
  - **Conditional:** everything that needs the lane's operator, bundles and pole allowances (the kernel's count of
    eleven chiral modes, the light cubic's coefficients, the second stationary family). Main has not rebuilt those.
- **The lane's withdrawn harmonic-transport draft (2026-11-12) carries a correction to main's B1866, and it is right**
  (`checks/physical_harmonic_draft.py`). The word L R⁻¹ L that B1866's finding F1 used is Inn_a ∘ s, with s the based
  quarter-turn; both have the same homology matrix and different quaternion lifts, a reflection and a rotation. On the
  branch the word fixes, the word acts by −1 and the based s by +1. So the two signs of F1 belong to two elements, and
  neither is an error of arithmetic. B1866 carries a dated note. The draft's conclusion (the physical triplet and its
  table of modes) is the lane's own withdrawal and is recorded as superseded; its other exact statements hold.
- **The lane's boundary-law package (2026-11-15, 100 statements) is settled, almost all of it verified**
  (`checks/physical_boundary_law.py`): the relative class of the figure-eight exterior, the reduced response
  B* = pΦ/(r + p) (also from the field equations solved directly on a disc), the radial control, and the two sewing
  problems. Its own conclusion is a limit, and main agrees: nothing in this model selects three.
- **Two pages the lane pins as sources are main's own FINDINGS of B1641 and B1700, byte for byte** (67 statements,
  noted as main's).
- **Two old debts paid on the way** (they would have refused landings on 2026-11-20):
  - **P-444:** where B1785's 585 bad window fits sit (240 where m₁ = 0 exactly, 345 in the closed form's domain); with
    them left out B1788's comparison and B1785's medians stand; on the seven worst lines, run at 40 digits to height
    14, every exponent approaches the closed form. As window fits they do not depend on the slope alone.
  - **P-107:** the audit seat's counterexample of 2026-10-13 is verified: invariance under the moves does not single
    out the hyperbolic measure (`checks/physical_measure_counterexample.py`).
- **The web seat answered main's question (its status page, section 7, at 61da9bec5), and set two conditions for
  writing HARVEST COMPLETE.**
  - **Ten small items in main's record, all right, all acted on** (record `web-st7-03`). Among them: nine records
    counted as verified some statements with a figure main had not recomputed (34 statements moved to PARTIAL
    records); eleven of W-F17's statements were filed under the wrong records; the custody tool saw commit ids only in
    backticks and reported 0 commits for three notes (mended, rerun for every lane); the congruence indices were filed
    as noted (now computed on main, `checks/web_wz1_c3_indices.py`: 6, 1, 12, 6, 1, 12, 12).
  - **Its older deliveries.** Main's own ledger shows 51 of this seat's rows before 2026-11-15 whose disposition is
    RECEIVED (not read in full), REGISTERED, UNREAD or read only at the head. Main recounted with the seat's rule and
    got its figures.
  - **Main's decision, 2026-11-18: the older rows are taken into the register; none is ruled out.** The window now
    also holds every file those rows name, the six relays read in full but outside the register, the seat's readings
    for Reviews 79 and 81, and its cards: 108 more files, about 4,370 statements, pending. Among them are the
    foundations cards W-F1 to W-F16, which main had received and never read in full. Rows whose disposition records a
    reading with main's verdict are not reopened here; they stand under the harvest ledger and the reviews unless a
    seat or the author names one.
- **The web seat's verification cards of 2026-11-11 to 2026-11-14 (W-C1, W-C5, W-C6, W-C7, W-C8, with their cards),
  read in full and recomputed on main** (`checks/web_wc8_part1_on_main.py`, `web_wc8_part2a_duality.py`,
  `web_wc8_part4_on_main.py`, `web_wc5_on_main.py`, `web_wc6_part2_on_main.py`):
  - **W-C8, the one-tick object.** The normaliser of the act is ±JⁿKᵉ in eight classes modulo the act for the metallic
    acts m = 1 to 5 (searched; open beyond); the hand at the mark is (−1)ⁿ⁺ᵉ. A metallic tick has a mark exactly for
    odd m: the Smith form of A_m + 1 is diag(gcd(m, 2), N/gcd(m, 2)), and for even m there is no square root of −1
    modulo N at all (m to 200). So the mark does not single out the golden act among the odd ones; the torsion-free
    condition does. Twisted duality h²(V) = h¹_rel(V*·w) holds on every character at levels 3 to 8 (16 to 1,682 of
    them) and fails without w on 6, 20 and 56 characters at the odd levels. The eigenvalue field of an act is the
    field of its level exactly at the metallic traces (every trace to 20,000).
    Part 3 is a reading with nothing computed, and a lead: the class index cannot see odd ticks, so it is no test of
    the even-tick condition; a derivation would have to use the characters' h¹ gaps or the hand at the mark.
  - **W-C5.** B1914's eight classes and scalars and B1915's two and four orbits, on two codes. The seat asked that
    B1915 name the basis of the second side's line: it is D(1, 2) = (1, 3) modulo 5, the seat's own, and main's run
    pairs the placements as the seat's does (dated note on B1915). The cusp statement's rule is the integral's
    condition exactly, checked in integers.
  - **W-C6.** Part 2: main's own B1919 and B1921 routines run at the seat's twelve points agree (1.1e-9 and 2.3e-9),
    and the controls come out as the seat's to the digits it prints; the seat's unclaimed remark, that the
    Kronecker limit is the same at the transported point, holds (by hand, and to 2.8e-11). Part 1, its cold reading
    of the short account: six real faults of over-claiming, each right against its source and each mended on the
    page as landed.
  - **W-C7.** B1913 on two codes, the same numbers to six digits (the flat density's greatest place moves by 0.0654
    with the chart; the invariant density's does not).
  - **W-C1.** Its re-audit of main's corrections E2 and E7. E2 accepted, and main's own computation gives its
    indices. **E7: the seat was right and main's message was wrong.** Main had said the correction stood on every
    page that quoted the freedom ledger's zero; six pages still stated it. All six carry the correction today, the
    lock reads by paragraph and looks for the walk's own words, and both locks read the same root pages. Two things
    stand as the seat left them, by main's stated choice: the walk still prints its withdrawn outcome when run, and
    both locks exempt the programme page's folder.
- **The physical lane's package P-C3, the registered-domain index join** (430 statements: 129 verified as finite
  algebra, 187 conditional on the lane's parent and on analysis it says is not independently checked, 114 noted;
  `checks/physical_index_join_proof.py`, `physical_index_join_vertex.py`, `physical_index_join_fields.py`). The
  lane's own twelve-method checker is sealed and unrun; main's scripts are the independent recomputation its review
  brief asks for, of the algebra only.
  - **Lead 1 of the leads desk is answered by the lane itself, in the negative for its fixed block.** Its three-mode
    block carries one common inner character, the native axis triplet three distinct ones, so the two cannot be
    identified (an equivariant map has rank at most one); its index in the retained representations is zero. The
    "three" of main's B1641 and B1700, on the modular-cusp extension, and the lane's three modes are on different
    operators, and the lane says the map between them is not built.
  - What it does derive, conditionally: the coupling at the retained Wilson crossing, normalised against the
    current's charge from the same action, is at least √2 times it (strictly, in the cusp metric); where the kernel
    splits as two form modes and one spin mode the leading mass matrix has rank at most two and the third mass is a
    second-order duty.
- **After M47 the web seat's referee read found two more things, both right** (its section 8 as corrected): its cold
  read of 2026-11-11 had never been taken into the register though main's own list named it (taken in, read,
  settled: 137 files, 6,602 statements, none pending); and amendment A14 had answered only half of N4 (B1937's
  script read a commit that is not on main; the bytes are pinned beside it now, output unchanged). Main's realigning
  tool, used to take the corrected page in, kept the ids of changed lines and attached four records to other
  statements for an hour: rebuilt from the text, tool mended.
- **THE WEB SEAT'S LANE IS AT ZERO PENDING (2026-11-18, night): 136 files, all read at source, 6,552 statements.**
  The seat has not written HARVEST COMPLETE; main has reported its three conditions met and asked it to check (M47).
  - **Its section 8, after M46, found two faults of main's, both right and both mended.** Two of main's checks drew
    unseeded random points, so a rerun could not match them digit for digit (seeded). One record was marked verified
    over two lines main had not recomputed, the same fault the seat had named that morning (both computed now:
    `checks/web_wc8_part5_bronze.py`).
  - **One refutation, in its session relay of 2026-09-08:** "every sl₂ of E₆ conjugates into F₄" is false (the
    subregular sl₂ fixes no vector of the 27: 13 + 9 + 5). The relay's theorem stands for the simpler reason main
    banked, and main's own row, which had called the F₄ argument a second route, is corrected.
  - **The October tests that compare with data** (the first row; the zero-free census; ZERO_FREE_HOLOMORPHIC;
    TICK_LINE_HIGGS; TWO_HIGGS; the framing check): read in full, their data-free facts verified, nothing recomputed
    against data, no measured value repeated. The comparison step waits at P-316. Main's record of them was stale in
    four places (P-316; harvest rows 1338, 1340, 1342), corrected.
- **The web seat's four review readings (Reviews 79, 79b, 80, 81) and their cards, read in full.** They found 31
  faults in main's own arcs, locks and governing pages: claims wider than what was computed, corrections that had not
  travelled to the other pages that state the same thing, seven tests in main's suite that could not fail, a mend
  of main's that tested nothing, a lock line that passed whatever the page said. Main held every one against today's
  tree: each was right, and 28 are mended on the pages. **Three remain open in main's gates** (the retraction sweep
  counts a cue word anywhere on the line; the controls gate's reading of a module-level skip; the vacuity gate's
  request to shorten its table is lost when the whole table is mended). They were handed to the builder on
  2026-11-12 and wait there (P-820, P-833).
- **The tube's value, and a proof that came out of an unharvested ask.** The seat's firmed value of the metric's own τ
  at the tube, 0 + 6.06530(6)i, stays the seat's: main redid its extrapolation arithmetic from the printed members
  and has not computed the members beyond k = 2 (P-739 stands). The note's third ask of 2026-11-07, three more words
  for B1852's even-run pattern, had never been carried to the register. Taken up now, it gave a proof:
  **the per-centre rule holds for every cyclic word that reads the same backwards** (modulo 2 the letters are
  involutions; the reverser is F at a centre between letters and F·x⁻¹ at a centre on a letter x). Checked exactly on
  all 562 such words to length 14 (`checks/web_tube_p740_rule.py`). P-740 is closed; B1852 carries the proof. It is
  main's own and has not been read by a session that did not write it.
- **Two readings with nothing computed, held at their sources.** That R2's exact block is a pure number on the
  record (its quotations of main's record and of Córdova and Jafferis are exact; a reader checked the paper's text
  today), and the grading of the record's candidates for the weave's own action on τ (2026-11-10, which main's harvest
  row had left "to be read in full"): every smooth invariant function is stationary at i and ω (two lines, checked,
  with the kinds of the critical points computed), and off those points every minimum on record is placed by a
  chosen content, ratio, weight or convention. Recorded at P-629.
- **The October folders on the selection principle and on the scale.** Their exact, data-free parts are rebuilt on
  main: the orbit-space theorem; a thread's class modulo 2 on all 31,040 threads; the heights as half the Lagrange
  values; and all three sealed checks of the scale folder run again on main's own scripts with every cell and every
  read-out reproducing (690 of 745 threads see the quantised level; the root's share of the weave at c = 6 is 0.27,
  0.50 or 0.66 by the word weight; the sign of the monodromy shifts the Chern–Simons invariant by a quarter, which
  main had registered and not recomputed). **Not recomputed:** the thread frame's mass ratios and the height law,
  which rest on a hypothesis the seat names and were superseded in the programme; they stand as partial, as in
  October. Where those notes set an output beside a measured value, main read and compares nothing.
- **The web seat's foundations cards, received on 2026-11-14 and never read in full by main, are now read and
  recomputed on main's own code** (W-F1 to W-F16, W-F18 to W-F23, W-F26, W-B1, with their cards; scripts
  `checks/web_wf*_on_main.py`, `web_wb1_on_main.py`; other primes than the seat's). **Every figure main computed reproduces** *[worded so 2026-11-18, Review 84: the page said "every computed figure of the seat's"; the parts main did not recompute are held as partial in the records whose ids end in p]*. What they establish, each with its limit:
  - **The puncture is not a separate input of the seat's system** (W-F3, W-F5): a cone point is a relation
    (abc)^K = 1 among the three distinctions, and every such relation kills the classes on the scar. Verified to
    K = 13 on the face and for fibre orders 2 to 6 on the 3-dimensional objects; for every K by a short hand argument
    main has checked.
  - **The face follows from a hyperbolic act** (W-F2, W-F7): of the four faces of three distinctions only all
    half-turns admits a hyperbolic step. Verified on all 2,800 products; for every length by a hand argument main has
    checked (granted that a step respects the face).
  - **Two theorems** (W-F6): for a character non-trivial on the fibre, h¹ = [χ(μ) = det]; the normaliser of the act's
    group is ±JⁿKᵉ. Main read both proofs step by step and they hold; the law is also verified on a non-metallic
    monodromy of determinant −1, a case the seat said it lacked.
  - **A third theorem** (W-F12, W-F19): the class index is zero on every doublet at every odd level. Main read the
    proof and recomputed all 54,942 doublets at seven odd levels and the 48,778 at golden level 7.
  - **The order at the scar is irreducible in the seat's system** (W-F9): duality negates the index and every
    symmetry preserves it. The census is verified (12, 210, 1,892 and 56 modules); the irreducibility is the seat's
    hand argument, not independently proved.
  - **"Three" is not forced by growth or by the frame's matter** (W-F8, W-F11): every n ≥ 3 has a growing history, and
    a world of five distinctions carries 756 sector modules with index ±1 on 28 each. Verified.
  - **The odd tick's matter is its double cover's** (W-F4): verified on main (transfer, the whole accounting, the
    closed objects), with a third computation of agy-exp's example on the way.
  - **Frame C's cusp mixing** (W-F26): a permutation in all eight options, the identity exactly when up and down take
    the same reading. Verified on main's extended-precision frame; the exponents in that option are 3/5, 3/10, 11/10.
    Nothing is compared with data.
- **Three corrections to main's own record came out of these cards:**
  - **B1922** said the frame is periodic along the thread at the own line "and not at any other line". False: it is
    periodic at (1/5, 2/5) too (main's own routine: 7.7e-11, 8.2e-10, 5.7e-5). The seat had said so on 2026-11-14.
    B1922 carries a dated correction.
  - **B1866's F1** (above): the two signs belong to two elements.
  - **B1607** now carries a note that its statement holds on the whole census to length 12.
- **Two faults of main's own, made and mended while checking:** a wrong amphichirality criterion (32 for the seat's
  33), and a test that skipped the trivial extension character (48 doublets for the seat's 64).
- **Leads the cards leave with main, none yet computed by main:** whether analyticity is a line of the system (it
  decides whether the order bit is irreducible or derived); the duality-transport test of the Higgs reading (is it
  the order bit or a second bit); the class of the holomorphic Higgs kernel in frame D (R1 of W-F20); the three-turn
  repetition of S* in extended precision; the same-reading world's cusp exponents.
- **A fault in main's own record tool, found on the way:** it stamped a typed date, so 168 records written on
  2026-11-18 said 2026-11-17. Corrected by each file's own write time; the tool now takes the day's date.
- **Tools that check a note without running a seat's code:** `checks/custody.py` (commits named, their order, the
  scripts' literals and imports by parsing) and `checks/figures.py` (every number a note quotes, searched in the
  sealed outputs it names; every hash manifest against its file).
- **The web seat's check of M47 (its section 9, 2026-11-18): two findings on main, both right.**
  - **A record verified over lines only registered.** `web-sr-02` held 19 statements of the seat's session relay of
    2026-09-08 as verified, on a ground that said "registered as stated" and "not re-run today". Main computed every
    one of them and split the record: 12 verified, 4 partial, 1 refuted, 2 noted
    (`checks/web_session_relay_three.py`, `checks/web_session_relay_manifolds.py`).
    - Verified: −w₀ is the diagram automorphism on E₆ and the identity on F₄; the characteristic of an sl₂ is fixed
      by it; 27 = 26 + 1 on F₄; Out(E₆) has order 2 (D₄, with 6, is the control); an element of order 3 of SL(2, ℤ)
      has trace −1 and three fixed points; the seven manifolds, with SnapPy.
    - Partial: "the number 3 does two independent jobs". The arithmetic holds and the two jobs are independent. That
      the three fixed lines are three generations, and that the inner lift is why they are chiral, is a reading main
      has not computed.
    - Refuted: "this derivation is not in the record". It was (B1103's certificate, stage 2).
  - **Six of main's checks failed in isolated mode** (a sibling import without the path). Mended; each gives its
    committed run byte for byte.
  - **P-740's proof has been read by a session that did not write it**, and found right. The seat supplied a step the
    note had left unsaid and an independent search on 118 words.
- **The physical lane's packages P-C3b, P-C3c and P-C3d (state orbit, transverse response, neutral source): 585
  statements, 204 verified, 252 conditional, 129 noted.**
  - Main rebuilt the finite algebra and the elementary analysis of every hand proof (three check scripts) and ran
    nothing of the lane's. Every formula main could compute holds.
  - What stays conditional is what the lane itself says is unchecked: that its physical operator reduces to these
    finite and half-line blocks.
  - **What the lane concludes, in its own scope:** a positive quartic on its charged spin modes is protected with no
    free coefficient; neutral fields alone cannot join its three state axes; the fields fixed by a reflection are a
    consistent classical sector where a join may be sought. It counts zero inputs removed.
  - **Its review of agy-exp's X-UNIFY** gives four objections to that seat's source. Main verified the thirteen finite
    claims in it and holds the four objections for its own reading of that lane.
- **The web seat's corrected section 9 (2026-11-18, late): ten items on main's record, all right, all taken.**
  - **Six VERIFIED verdicts had rested on the seat's run, not on main's.** Each is computed on main now
    (`checks/web_section9_items.py`): twisted duality on bronze's 56 non-split modules; b₁ at golden levels 1 to 8;
    the index 12 by volumes and the images at (2), (4), (8); the scale folder's sign control and tail bounds. Every
    figure is the seat's.
  - **Superseded was too wide in eight places.** One statement had never been withdrawn; seven were withdrawn in part.
    Each now says what the seat withdrew and what stands.
  - **A VERIFIED record whose own note said "conditional"** is conditional now.
  - **The lesson for main's records:** a verdict of VERIFIED may not sit over a note that says "not recomputed",
    "registered" or "the seat's reading". The seat found this five times in one day.
  - **A second fault in main's realigning tool:** a record all of whose lines had changed kept its stale ids. Four
    records rebuilt; the tool mended.
- **The physical lane's package P-C3f (cyclic charged masses): 150 statements, 40 verified, 50 conditional, 60 noted.**
  - Verified as mathematics on an elliptic curve (`checks/physical_cyclic_mass.py`): the two divisors, the lengths of
    the complex's cohomology, the count 18, 16, 8, and the rank 1 of the secondary map.
  - **It changes a lead main held** ("a hierarchy from rank"). On the lane's native cyclic family the third singlet
    pair is massless at every order, not massive at second order. The second-order mass is in the colour-triplet
    coefficient. The lane says the spectrum is vector-like and that a charged-pair mass does not answer the family
    question.
- **The physical lane's preparation for main on every seat's branch (F01 to F17): 164 statements, 57 verified, 11
  conditional, 96 noted.**
  - All 46 quotations behind the findings are where the lane pins them (`checks/physical_evidence_custody.py`).
  - The mathematics inside the findings holds on main (`checks/physical_all_seats_findings.py`).
  - Main's own earlier records of agy-002's lanes agree with eight of the findings or go further.
  - Six findings are about agy-exp's sources, which main has not yet harvested: held for that reading.
- **Review 84 read this arc cold (B1958, 2026-11-18) and found nine faults in it,** each mended: the verdict file's
  stale counts, two lock lines that could not fail, a page count that did not match its run, a sentence wider than
  its records, and five records that said more than their checks. A pass over every verified record is owed (R84-1).
- **Five more packages of the physical lane (frontier response, input recheck, four-form register, X-APEX review,
  its review of the X-FUNNEL campaign): 661 statements, 332 verified, 209 conditional, 120 noted.** Nothing of any
  seat's was run.
  - **Custody:** every quotation the packages pin from another seat's scripts is at its commit, path and line (10 line
    ranges, 31 pinned files, 36 excerpts).
  - **Verified as mathematics** (four check scripts): the omitted cusp area 2π/(T + 1 + log 4); the half-line
    response and its sewing; a scalar wall that solves its own equation and fails the normal one; the cross module's
    kernel a line for every parameter; a second fundamental form that needs its gauge connection (a frame-change
    counterexample, and the missing term 144 cos²θ/D³ in the other seat's own example); the four-form quotient, its
    connection and primitive unit, the centre of order three, the composite map and the constrained phase response.
  - **Two statements of another seat are refuted by the lane, and main confirms both:** "M mod 3 has order 8" (it
    has order 4, with two orbits of four), and the inference that a two-loop running cannot give opposite skews from
    equal starting values (a diagonal counterexample, on main's own one-loop running).
  - **Main adds one finding of its own:** the other seat's comparator density has curvature −1.26, −1.45 and −1.30
    at three points. It is not the hyperbolic metric of the punctured torus. The lane had said only that the
    identity "still needs to be earned".
  - **A lead, in the lane's careful words:** the unit of the four-form connection on the effective circle is three
    times the unit of the full charge circle, because the charge comes in thirds on E₈. The unit is in parameter
    space; a map from the physical carrier's end into the family is still required, and no family count is claimed.

- **Three more packages of the physical lane (its review of the X-ENDGAME campaign, its refresh of every branch,
  its dependency plan for all seats): 318 statements, 82 verified, 80 conditional, 147 noted, 9 superseded.** Nothing
  of any seat's was run.
  - **Two faults of main's, found by the lane, both right.** B1953's page said the phased sum F is the trace of its
    operator over the 3; it is F/2 (each of the 24 operators has trace 1/2 there; recomputed a second way in
    `checks/physical_dependency_plan.py`; B1953 carries the correction). B1927's end routine returns the nearest
    value where interpolation is not finite and flags only the upper edge (register row P-864).
  - **Verified as mathematics** (three check scripts): the punctured carrier has no second cohomology class, and its
    fourth cover has torsion 3 and 15; the mixed-product orders differ by (3/4)[H_u, H_d]; the Weil split and its
    anomaly sums; the one-loop eliminant; the congruence projector is a finite sum; a first-order operator's adjoint
    has no end condition; a free prefactor removes no input.
  - **Custody:** 21 excerpts by hash and line range, 23 branch heads, four quoted sentences, each where the lane says.
  - **What the lane says of all the seats' work, noted:** the common weakness is that nobody has derived that one
    registering architecture forces one state space, statistics, gauge action, interaction, domain and boundary
    response. It asks main to recompute its deciding analytic estimate first (the complete-cusp inverse of its
    package P-C3e). Main has not done that; it has verified that package's finite algebra only.

- **The physical lane has no statement pending (2026-11-18): 136 files, 10,952 statements, 1,084 verified, 1,040
  conditional, 24 partial, 46 superseded, 8,758 noted.** The lane has not written HARVEST COMPLETE; its status page
  says its own review of the harvest is not complete.
  - **Its last 483 statements** (status page, 22 relays, 13 scope cards): 47 verified, 19 partial, 115 conditional,
    302 noted. The relays restate the packages; a verified line names the committed check that computed it.
  - **Its two executed checkers.** The lane committed the outputs of two checkers of its own. Main does not run them:
    it reads their inputs from their text and computes every figure with its own code
    (`checks/physical_endgame_outputs.py`, `checks/physical_boundary_outputs.py`). Every key of both committed result
    files agrees. *[Narrowed 2026-11-18, at the lane's own finding M9-05: main's two scripts compare 33 and 45 of each
    file's 72 leaf keys. Every field compared agrees. The keys not compared are listed by
    `checks/physical_outputs_key_coverage.py`: provenance, residual sizes, flags and a few mathematical fields.]* Ten verdicts that had rested on the lane's run are now verified on main.
  - **What "verified" covers.** Finite algebra, elementary analysis and custody of quotations. Nothing of the lane's
    model is banked: its physical statements stay conditional on its parent and on analysis it says is unchecked.
  - **Owed to the lane by main:** the first of its six ranked deciding calculations, the bounded complete-cusp
    inverse of its package P-C3e (its equation (3)). Main said in M8 it would take it first. It is not done.

- **The inverse on the cusp, owed to the physical lane, is done the same day (B1959).** Main proved, by an argument
  independent of the lane's, that a Laplace-type operator homogeneous on a finite-area cusp, nonnegative, with kernel
  one parallel section Q, is a bijection with bounded inverse between "a constant times Q far out, plus decaying" and
  "decaying sources orthogonal to Q". The lane's equation (3) follows if its operator is of that form on its fields,
  which stays its model's statement (record physical-c3e-03, still conditional, says exactly what is and is not
  checked).
- **The web seat's section 12 and the pass R84-1 over its lane (2026-11-18).** The seat checked M50 and M51 at the
  records, reran main's new check to the byte, and named five verified records that held lines it marks as readings.
  Each is right and is narrowed. Main's own pass over the lane's 136 verified records (two filters over 1,897
  statements and over every record's ground, 258 hits, each read against its record) narrowed four more. In all 22
  statements moved to partial or noted. The lane: 137 files, 6,796 statements, none pending. The pass is by filter
  and reading of hits; the other lanes' 114 verified records are still owed it.
- **The full suite on a clean clone, at Review 84's anchor: 29 failed of 9,100.** Seven were the review gate firing at
  that commit. The other 22 were six real faults that the landing's own tests do not see; each is mended (the
  review's entry lists them). One was in this register's own neighbourhood of work: a script that replaced another
  arc's function for the whole process.
- **agy-exp's lane has no statement pending (2026-11-18): 88 files, 2,099 statements, 102 verified, 5 refuted,
  231 conditional, 181 partial, 47 superseded, 1,533 noted** (harvest row 1909). Every result note of its ten
  campaigns, its status page, its page of premises, its answers, its Review 83 reading and its view were read in full.
  Its code was never run; three places of it were read as text.
  - **The rule for its verdicts.** Verified only where a committed check of main's computes the statement. Partial
    where main holds the fact under a line and the rest is the seat's run. Conditional for outputs inside its supplied
    model, on the premises its own page lists. Superseded where its own later answers replace a statement. Refuted
    where a statement is false as written.
  - **Its 42 cards (846 statements)** are scope written before the work. They are noted by their section headings. A
    read-only sorter went through them for lines that are not scope, and main read what it flagged.
  - **Its level-25 statement, decided on main's own frame** (`checks/agyexp_x_foundation.py`). Under τ → τ + 5 the up
    sector's determinant takes three fifth-root phases over the 24 points and the down sector's one; under τ + 25
    each takes one. Main adds the law: the point's phase is ζ^(E·(5a)²), E = q_L² + q_R² + c·q_H² mod 5 for the Higgs
    zero placed at c. No placement closes the up and the down sector together at level 5 (B1945 § 6; row P-871).
  - **A fault of main's that Review 83's entry dropped.** The seat's finding F-R83-16 has a second item: the averaged
    mixing moduli's cusp limit in W₊ is 7/12, 7/12, 5/12, not W₋'s 5/12, 5/12, 7/12. Main recomputed it at heights 45
    and 85 (`checks/review83_agyexp.py`). B1940, B1945, the open-leads entry and B1950 carry dated notes.
  - **A credit restored.** Its view of 2026-11-15 states the bigraded dictionary of B1951 the same day as the web
    seat and independently, and adds four pairings into the top form (`checks/agyexp_view.py`). B1951 cites both now.
  - **Its twenty Review 83 findings:** 42 items tested on main's present files. The facts hold in all 42: six plants,
    nine mended or answered, 27 standing as action item R83-1. One item's two citations are not at the lines it names.
  - **Reproduced:** the four tension figures of its committed output, to 1e-16, from two inputs read in its checker.
- **agy-002's last fourteen lines are settled (2026-11-18; harvest row 1910).** They are its closing note's audit of
  the other seats. Its six defects in agy-exp's X-SYNTHESIS are each confirmed as far as reading that seat's checkers
  reaches (`checks/agy002_audit_of_seats.py`). Its counts over that seat's runs are recorded as its own.
- **No statement is pending (2026-11-18): 406 files, 361 read at source, 20,949 statements.** The 45 files not read
  line by line are agy-exp's 42 cards and three files of the physical lane (its seal ledger, checked by difference,
  and two files of quotations held as custody).

- **Four seats pushed new work the same morning; the register is cut again (2026-11-18, midday): 447 files, 22,873
  statements, 1,709 pending.** Pending: agy-exp 837, the SM seat 461, the physical lane 411. The web seat's lane has
  none.
  - **agy-exp is back, and its lane is reopened at its own word** (harvest row 1911). Main had closed it that morning
    under the author's delegation; the closing is withdrawn. Its harvest review is exact: its recount is main's
    summary at the commit it read, each of the eleven harvest rows it cites says what it quotes, and the four places
    where it says main's record is short or stale are so and are mended
    (`checks/agyexp_harvest_review.py`). It lists twenty older files the register did not cover; all are in its lane
    now, and two are read (X-C9, X-WALL).
  - **Its first-ranked check, the proof of the η identity, is done on main's own code, with one slip found**
    (`checks/agyexp_xc9_proof.py`; B1929 carries the note). The closed form of the first step equals −L_odd/π² on all
    601 characters. The second step's display has the wrong sign; the identity stands.
  - **Its sixth-ranked check, the two copies of E₆ in E₈, is done:** intersections of dimension 16 and 7; its element
    has determinant 1 and order 4 and carries one copy onto the other.
  - **Its own supersessions are applied** to main's records: the level-6 selection of a Higgs mode, and the quartic
    figures from before its repair of the two-loop term.
  - **The web seat's corrected section 12** (harvest row 1912): its own pass over every verified record of its lane
    leaves eight records short. Each is taken (`checks/web_section12_corrected.py`): none of the 19 units it names
    stands under a verified record. Its pass and main's R84-1 found different records; both kinds are owed over the
    other lanes.
  - **The SM seat's lane is added to the register.** Its cards SM-C18 to SM-C21 (frame D1's covariance, its Higgs
    bit, the tick as the exchange, and D1's cusp mixing) are registered and not yet read (harvest row 1913).
  - **The physical lane's eight commits** (its check of main's M9, its support for the cusp inverse, its coverage of
    its code, and a new package on the tick and the Higgs) are registered and not yet read (harvest row 1914).

- **Three lanes settled the same afternoon (2026-11-18): 451 files, 23139 statements, 837 pending, all agy-exp's.**
  Harvest rows 1915 to 1917. The cut is at the physical lane's 6f074b770, the web seat's 01173b9df and the SM seat's
  a69cee901.
  - **The physical lane found five faults in main's own records of its lane, and each is right** (its findings M9-01
    to M9-05; `checks/physical_m9_review.py`). Main's indicial script had multiplied the equation by ℓ² and not the
    source, so its bound lacked that factor. The Bessel function it offered solves the channel without drift only.
    Seven verified paragraphs joined computed algebra to claims about the complete operator; they are partial now
    (record physical-m9-03). A record said the lane's engineering fixtures were unrun; they had run twice. And "key by
    key" said more than main's scripts do: they compare 33 and 45 of each result file's 72 leaf keys
    (`checks/physical_outputs_key_coverage.py`).
  - **Its package on the tick and the Higgs holds on main in every decidable step** (`checks/physical_c8_tick_higgs.py`,
    `physical_c8_dominant.py`, `physical_c8_modes.py`; the lane ran nothing, so these are the first runs).
    - **The deciding result.** The quadratic ground space of the six Higgs modes is a complex plane. Its unit vector
      h* = (1/√2, e^(iπ/12)/2, 0, 0, 0, e^(iπ/12)/2) has ratio exponents (0, 4/3) in the up sector and (1/5, 4/5) in the
      down and lepton sectors at the mark. The two eigenvectors, and a random ground vector, have none. Nothing
      computed selects h*, and nothing selects the eigenvectors: the tick exchanges them.
    - The six modes factor as 2 × 3; the transport has characteristic polynomial (λ² − λ + 1)(λ⁴ − λ² + 1) and order
      12; each half-period lift sends a ground vector two thirds out of the ground plane.
    - The quartic invariant under the common phase, the transport and the tick is A·N² + B·Δ². The relative phase
      first enters an invariant at degree 14.
    - On main's own mode functions the connection is i[dX/(4y) + πN(ξ dη − η dξ)], and the frame's matrices are T₆
      and √(τ/|τ|)·S₆. This derives the relative kinetic spectrum along the act's axis that main had supplied.
  - **Two of its findings are against main's wording, and right** (C8-02, C8-04): "one bit" for the Higgs ground
    space, and "lift-invariant" for the bubble. Both are corrected above, where main said them.
  - **Its answer on B1959's hypotheses** (`checks/physical_m10_reply.py`): the operator's form follows from the
    connection it states, and the bounded kernel from the roster of E₆ and a cutoff argument main checked by hand.
    Its background and gluing stay premises of its model. B1959 carries the note.
  - **The SM seat's cards SM-C18 to SM-C21 are read and recomputed** (`checks/sm_c18_to_c21.py`).
    - SM-C18 holds, and SM-C20 holds as algebra.
    - SM-C19's headline is false as written. The unitary S₆ exchanges the pair too. Over the 576 elements of the
      group, the pair is exchanged exactly by what reverses the bundle's orientation.
    - One line of SM-C20's card gives the wrong reflection (the physical lane's finding C8-03): z → z̄ is conjugation
      with the parity on the modes. The card's result survives.
    - SM-C21 reproduces on main's own driver. Its negative is for the two eigenlines, not for the ground plane.
  - **The web seat's sections 13 and 14** (`checks/web_section13.py`, `web_section14.py`, `web_wa2_readout.py`): the
    thirteen records it found short are each taken. It was right against main twice on W-A2's five lines; they are
    verified on B1953's own routine. Its check of main's level-5 law agrees in exponent and sign.
  - **The second reading of the web lane's verified statements has begun and is not done.** Eight read-only sorters
    marked 950 of its 1,942 verified statements as candidates whose record's ground may not cover them. Main reads
    each candidate before any verdict changes.

- **The second reading is done for six lanes (2026-11-18, evening; harvest row 1918): the register's verified count
  falls from 4007 to 2709.** It is Review 84's action item R84-1, and what the web seat asked for.
  - **How.** Twelve read-only sorters read 2,638 verified statements beside their records' grounds and marked 1,423
    as possibly not covered. Sorters give no verdict. Main read the candidates record by record and decided.
  - **The decisions.** Web: 90 kept, 471 partial, 312 noted, 77 conditional. The lanes of agy-002, agy-exp, the agy
    audit lane and the SM seat: 35 kept, 200 partial, 196 noted, 42 conditional.
  - **The rule,** strictest first. A heading, definition, pointer or status row is noted. A line the seat's own text
    marks as a reading, judgement, proposal or request is noted. A line resting on the seat's own run, a planted
    control or a cited result is conditional. A line with a figure or a clause the record's ground does not name is
    partial, unless every figure in it stands in the ground or in the run file it names.
  - **Where.** `verification/second_reading/web.json` and `others.json` list every candidate with the sorter's
    class and reason and main's decision. The narrowed lines sit in companions of their parent record
    (`<record>-r2p`, `-r2n`, `-r2c`, 382 records). `checks/second_reading_web.py` and `second_reading_others.py`
    hold the lists against the records.
  - **Its limits.** "Partial" means the ground does not name the clause, not always that no script of main's computes
    it. The 1,215 statements no sorter marked were not read again. The physical lane was not sorted: it read its own
    128 records itself and found seven mixed paragraphs; its records written since are not covered.
- **No statement is pending at the seats' newest heads (2026-11-18, night; harvest rows 1920 to 1927):
  482 files, 421 read at source, 24329 statements: 3314 verified, 25 refuted, 1935 conditional, 1891 partial, 164 superseded, 17000 noted, 0 pending.** SM-C22, the
  physical lane's C3h and agy-exp's X-L5 are read and settled (rows 1925 to 1927); SM-C22's sentence that a hierarchy
  lives only on one or two modes is refuted by main's coherent vector, which has a hierarchy on three.
  - agy-exp's eighteen older files are each read in full (`checks/agyexp_older_notes.py`). What main recomputed of
    them holds; four of its Review 80 findings that main's review had marked "not checked" are checked and were
    right; its second computation of the SM seat's weave items found one sign wrong in that seat's relay; five slips
    in its own notes are sent to it.
  - The web seat's sections 14 and 15: every statement it makes about main's records is right
    (`checks/web_section15.py`). Main's read-out of B1953's law now tests the move under S too. With one real R on
    both sides the law leaves under T a constant of a quarter turn in the reading S and none in the other, where the
    seat's note has an eighth: put to the seat.
  - The physical lane's reply, its compact magnetic control and its cross-form packet: every finite step is computed
    on main (`checks/physical_c8_magnetic.py`). On its control the frozen quartic's dependence on the Higgs direction
    is removed by a Cartan response, so it is not a selector. Its hand derivations stay conditional.
- **Main has now read every verified statement of seven lanes itself, one by one beside its record's ground
  (harvest row 1923).** The second reading had left the lines no sorter marked read by sorters only.
  - 1,241 such lines read, 67 narrowed; the 125 lines main had kept read again, 15 narrowed. The lists, with a
    reason for each line, are in `verification/second_reading/` (four files); three locks hold them.
  - Not done for the physical lane: its 1,390 verified statements are not read a second time.
  - **The web seat's own reading of main's second reading (harvest row 1924) was right on a large scale.** Of its 325 rows,
    main took them as asked but five: 206 units are restored to verified (167 of them lines main had narrowed), the
    rest refiled or their reasons corrected (`second_reading/web_rv55.json`; `checks/web_rv55.py`). Three of main's
    scripts printed as text what they now compute.
  - **A fault of the second reading, found on the way and mended.** Where it narrowed every line of a record it
    removed the record, and its ground with it, while 96 records went on citing it. 54 records are restored from
    history, each with its ground and no statement under it (`checks/grounds_cite_records_that_exist.py`).
- **agy-002's fourth branch, gates 8 to 11, is read and settled (harvest row 1919; `checks/agy002_foundations.py`).**
  Main computed the exact statements a quick check decides, and all hold: the charges on the even exterior powers,
  the commutants 1 and 12, an involution of E₈ carrying one copy of E₆ onto the other, the reality of the contracted
  determinant on Re τ = 0, the longitude of trace −2 in both lifts, and a zero mode on the half-line that turns a
  Dirichlet bound into an upper bound. Its lines stay partial: they carry its own runs' figures, and "derives
  postulate D" and "delivers three generations" rest on premises that restate both.

## When it closes

- No statement is pending.
- Each seat has written on its own status page that its harvest is complete, after reading the register and main's
  record of its work. Main has asked each seat for three lists first: what the register does not cover, its results in
  order of importance with the computation that verifies each, and where main's record states its work wrongly or too
  weakly.
- **For the lanes of the agy family whose sessions are not in use, main decides (the author, 2026-11-18; register row
  P-870).** *[Corrected the same day: agy-exp pushed that morning. Its lane is not closed by main; it closes at its own
  word, and M37 on its page withdraws the closing. Later the same day the author told main that all the agy sessions are in use again: the closings of agy-002's lanes and of the agy lane are withdrawn too (M47, M7), and no lane is closed by main.]*
  Those sessions cannot write the line. Main closed each on its seat page on 2026-11-18 (agy-exp M36, agy-002 M46,
  the agy lane M6) with this criterion: no statement pending; every result note read at its source; every request the
  seat made of main listed with where it stands. The limits are said there: cards are noted by section; code and
  outputs are not units of the register; work from before the window stands in older harvest rows, reopened by weight.
  A lane reopens if its session returns and writes what is missing.
- **The web seat's section 17, as corrected (harvest row 1928), is taken in full;** its completion line waits only on its
  own check of those changes (M58). The coupling's constant under T (a quarter turn in S, none in S-tilde) is the
  channels' eighth times the Higgs triplet's own phase; the seat's line 110, which gave the Higgs's eighth as the
  coupling's constant, is withdrawn and superseded.
  [corrected 2026-11-18, at the seat's section 19.3: when this was written the channels' eighth was the quotient of
  main's constant by the Higgs's phase, the law itself resting on the seat's own test; since harvest row 1931 main
  computes the channels' law with a free Higgs input itself (checks/web_wa2_readout.py, H4).]
- **P-873, QUESTION 2, ANSWERED ON MAIN** (checks/p873_zero_directions.py): the Higgs ground plane of frame D1 has
  exactly three directions with zero entries (zeros at mode 0, at modes 1 and 5, at modes 2, 3 and 4, the last being h*).
  Only h* gives a full hierarchy in the up sector: ratio exponents (1/3, 2/3) in 48 of its 96 up-sector cases, confirmed
  at 80 digits (0.3333, 0.6667); at the mark it gives (0, 4/3). Nothing computed selects any direction.
- **P-871's next computation, on main** (checks/p871_plain_sum.py; harvest row 1937): the plain sum of frame D1's
  unit-weight residues drifts under tau + 5 in the up sector at c = 0 (E = 2) and returns at tau + 25; at c = +-2 it does
  not drift in any sector, the obstructed ones included. agy-exp's flag that it never drifts at residue level is refuted
  as written.
  The c = +-2 cases do not drift because there the rows' sums differ in size by tens of orders, so the sum is one row's
  (P4): not a covariance.
- **Main has read every verified statement of the physical lane itself** (harvest row 1933): 1,390, each against its
  record's ground; 857 kept, 130 partial, 4 conditional, 399 noted (second_reading/physical_unmarked.json). No verified
  statement of any lane now stands without main's reading against its ground.
- **THE WEB SEAT HAS WRITTEN HARVEST COMPLETE AGAIN** (its section 20, 5322929cd, after checking main's mends at
  57e0b3d63; harvest row 1935). Every statement it makes there about main's record holds (checks/web_section20.py). It
  checks main's later records of its sections 19 and 20 as later changes (M61).
  [corrected 2026-11-18, later: the seat withdrew it again in its corrected section 20 (d3ecf1dea), after its referee
  read found three more things in main's records (an understated verdict, a false reason left in two records, the
  incomplete account above), each right and each mended (harvest row 1936). No seat has written HARVEST COMPLETE as it
  stands.]
  [added 2026-11-18, at the seat's section 22.4: of that first version's statements two did not hold (its line that the brackets and web-st18-01's note gave the right account of section 18's first version, and its line that one small thing was left and changed no verdict) and two were overstated (that each of section 19.3's six things was mended, where three places stood unchanged on H4, and that H4 is its run built again, where H4 extends it to the second reading); main's check A3 had tested only that web-st18-01's note carried a correction, and now tests each statement (A3b); harvest row 1939.]
  [added 2026-11-18, at the seat's section 23.2: main recorded its section 21 before the referee read and held verified
  five lines the reads corrected (web-st21-01's note; harvest row 1940); main now records each section from the version
  that carries its referee read.]
- **agy-002's card A2-X1 and its harvest review (harvest row 1929)** are settled. Every figure of the card holds on
  main's own construction of frame D1 (checks/agy002_a2x1.py). At the mark, |V(h*)| comes within 3.8e-4 of the
  maximal 1-3 mixing matrix the seat states, at height 24; that this is the exact limit rests on the seat's
  dominant-term argument (P-873, question 3). Every record change its review asks for is made; its sign-off is asked
  (M51).
- **THE WEB SEAT HAS WRITTEN HARVEST COMPLETE** (its status page, section 18, at main's 6f337047b; harvest row 1930),
  the first seat to. Every statement it makes there about main's record holds (checks/web_section18.py). Its next
  work, the order of foundation work it recommends, is register row P-874.
  [corrected 2026-11-18, the same evening: the seat withdrew it at 10c488d71 after its referee read found five things in
  main's records, each right and each mended (harvest row 1931); main now computes the channels' law with a free Higgs
  input itself (checks/web_wa2_readout.py, H4). No seat has written HARVEST COMPLETE as it stands.]
  [added 2026-11-18, at the seat's corrected section 20.4: three of the statements it calls holding did not: that web-wa3-04's ground named wa3_on_main.py, part D (only its note did), that the read-out computed what its section 17.2 says (it did not compute the channels' law for a free Higgs input until H4), and that the records of section 17 stated it rightly (harvest row 1932).]
- **The first condition is met at the seats' newest heads (2026-11-18, night): no statement is pending.** The second is
  not: no seat has written the line.
  - The web seat's section 16 lists what it holds is left; main has acted on every row of it (M57).
  - The physical lane names its ranked tasks 2 to 5; main asks whether its line waits on them (M13).
  - The SM seat, agy-exp, agy-002 and the agy lane are asked (M41 to M43; M38, M39; M49, M50; M8, M9).
- **Still no seat has written the line (2026-11-18, evening).** Each has now been told the second reading's result
  for its lane and asked to check it; agy-002's sign-off waited on its gates, which are settled.
- **No seat has written the line (2026-11-18, afternoon).** The web seat says it waits on the second reading of its
  lane's verified statements. The physical lane says it waits on its five corrections (made) and on the cusp inverse
  for its actual operator. The SM seat has been asked for its review for the first time (M41). agy-exp's review is in
  and its lane has 837 statements pending. The register closes when each has written it.

## Not claimed

- That anything is verified by being registered.
- That a statement's verdict is final before its seat has seen it.
