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
