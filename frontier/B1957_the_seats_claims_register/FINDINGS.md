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
  - **Not resolved (gate 5, P-861):** with hypercharge as the Wilson line the mixing in this frame is deranged (15 of
    24 points orthogonal, 9 inside a degenerate pair, none aligned) and lift-dependent; with one Higgs mode the
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
- **Tools that check a note without running a seat's code:** `checks/custody.py` (commits named, their order, the
  scripts' literals and imports by parsing) and `checks/figures.py` (every number a note quotes, searched in the
  sealed outputs it names; every hash manifest against its file).

## When it closes

- No statement is pending.
- Each seat has written on its own status page that its harvest is complete, after reading the register and main's
  record of its work. Main has asked each seat for three lists first: what the register does not cover, its results in
  order of importance with the computation that verifies each, and where main's record states its work wrongly or too
  weakly.

## Not claimed

- That anything is verified by being registered.
- That a statement's verdict is final before its seat has seen it.
