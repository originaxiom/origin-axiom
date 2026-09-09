# B1237 — THE PHYSICS-SEAT HARVEST, SECOND RING: R31–R38 + the W-D synthesis (2026-09-02)

**Verdict: PROVED (a harvest cell: every correction below recomputed on this bench before it was
banked; the seat's framing quarantined, its mathematics integrated). Gate 5 untouched — no physical
value anywhere in this cell. No identification declared.**

**Source.** The physics-seat evaluation branch (`…/physics-seat-evaluation-8dkbrl`), nine commits past
the B1235 harvest point: `2ebdff8d` → `d415423a` (R31–R38 under
`reports/fresh_physics_seat_2026-09-01/recompute/`, the Phase-B `W-D_SYNTHESIS.md`). Read in full via
`git show`; **nothing merged** (integrate-don't-merge). Reproduction: `verification/reproduce.sh`
(SnapPy + PARI through `snappy.pari` + mpmath; no Sage). Every number quoted below is from
`verification/*.txt`, not from the seat's report.

## THE PRIZE FIRST

The seat's synthesis names one structural fact about the record that matters more than any
single correction: **a later arc corrects an earlier one in the log, and the earlier arc's verdict
file is never touched** (their tally at draft: `SUPERSEDED_UNMARKED` 48, `RETRACTION_NOT_PROPAGATED`
25, `LOG_DRIFT` 24, of 605 arcs digested). That is **E53** (surface non-propagation) measured at
verdict-file grain — the class this bench minted on 2026-08-30 and then instanced itself the same
day. This cell verifies the four named instances on-bench and propagates each into the arc's own
`arc_verdict.json` + an addendum, so a stranger who reads verdict files (what every instrument reads)
sees the correction where the claim lives.

## What was recomputed here, and what changed (nine arcs)

| # | arc | the seat's finding | recomputed here | verdict effect |
|---|---|---|---|---|
| 1 | **B1062** (bridge cell, V2 control) | "silver non-arithmetic" is wrong: the *invariant* trace field of m136 is ℚ(i) | `silver_arithmetic.py`: 350 distinct tr(g²) over words ≤ 6 in the polished holonomy — **every one a Gaussian integer**; Vol(m136) = 4G = **12 · covol(PSL₂ℤ[i])** to 50 digits (covol = |D|^{3/2} ζ_K(2)/4π², D = −4, ζ_{ℚ(i)}(2) = ζ(2)·G). B1062's own table row already recorded x² = 2+2i. | PROVED stands; **V2 CORRECTED**: the arithmeticity axis separates **{golden, silver} from {bronze}**, not {golden} from {silver, bronze}. The *degree* statement ("golden alone at degree 2 in every tower") survives untouched — it is a trace-field statement, and the trace field of silver is degree 8 (B258's number, `test_b258` pins it). Bronze non-arithmetic is unchanged (not recomputed here; the seat's R33/R35 concur with the bank). |
| 2 | **B258** (two-ended unification) | same error at its source: "silver → 8 (non-arithmetic)" | same computation | PROVED stands (H27's trace-field/discriminant-field split is a degree fact); the parenthetical **inference** is wrong for m = 2 — `superseded_by` unchanged, note + addendum. B125/B147/B137/B850/B337 were already correct ({golden, silver} arithmetic) — the bank contradicted itself and no instrument saw it. |
| 3 | **B919** (the 3/8 traces, C42) | `traces.py` cannot run from the repo: `RUN = os.environ["HANDOFF6_RUN"]` and `cw.py` never committed; `test_b919_traces.py` compares stored strings | `git log --all --diff-filter=A --name-only`: **`cw.py` absent from all history**. `traces_from_b1236.py`: from B1236's committed `content_internal(F(−1,3),F(1,2),F(0))` (the SM-shaped 27 as a multiset of (colour, weak, Y) irreps, T₃ ∈ {±½} on doublets): **Tr(T₃²) = 3, Tr(Y²) = 5, Tr(T₃·Y) = 0 ⟹ 3/8**. | PROVED stands, **witness relocated**: C42's numbers are now derivable from committed code; THEOREM_LEDGER C42 gains the pointer; B919's lock stays as the historical string lock and the note says so. (This is NOT a second-prime tier — it is a different derivation of the same three integers from the multiplet content; the prime-tower derivation remains unreproducible from the repo.) |
| 4 | **B361** (seam local law) | PROVED, `superseded_by: None`, but **refuted by B367 at pair (3,4)** | `frontier/B367_value_map/FINDINGS.md:45–54` read: (3,4) contains no doubly-elliptic seed and is bright (aggregate 1/192, two independent computations); the minimal repair dies on (1,3) dark with the identical covering pattern. B361's own 8-pair table is correct — the LAW it induced fails on the twelfth pair. | `superseded_by: "B367"` + a SUPERSEDED prefix on the claim. Not RETRACTED: the arc's computation holds at its scope (B818's rule — RETRACTED withdraws *its own* headline; B361's headline was the 8-pair fact; the induced law is B367's kill). |
| 5 | **B259** (five-wall map) | wall #5 (k=3 → GΛ = 2π, "122 orders") RETRACTED by B980, B259's files silent | `frontier/B980_k3_conflation/arc_verdict.json`: PROVED, "WITHDRAWN … Smolin's relation is 3+1-dimensional, λ = ħGΛ, B259 dropped the ħ; GΛ dimensionless in d = 4 only; the object's level comes from a 3-manifold". | PROVED stands for the theorem (Mostow metric solves 3d vacuum Einstein at Λ = −1) and walls #1–#4; **wall #5's 122-order number is withdrawn in B259's own record** (note + addendum). B5 (L196) already cited this family. |
| 6 | **B892** (second measurement, C25) | "z = 14 = su(3)+su(2)+u(1)³" is the SM algebra? B950: the SM gauge algebra has dimension **12**; B951: the landing is the A₂+A₁ Levi | B950 `FINDINGS.md:36–41` read; B1236 (banked yesterday) is the exact multiplet-grade content on that stratum with **one** extra u(1) exhibited. | PROVED stands (the mathematics: dim 14, derived 11, centre 3, exact); the **sentence** "takes E₆ to the SM algebra" overstates by two abelian factors — note + addendum say so, with the pointer to B950/B951/B1236. C25's ledger row unchanged (it states the algebra, not the identification). |
| 7 | **B850** (length-spectrum type) | the multiplicity maxima (4/3/4/8/2; "m009 double m004") are word-count artefacts | `b850_multiplicities.py` (`length_spectrum(4.0, full_rigor=True)`): max geometric multiplicities **m004 12, m003 12, m136 11, m009 11, m015 6** (means 4.58/4.02/3.92/3.89/2.35). | NEGATIVE unchanged (DENSE for all; nothing object-specific — the correction makes the negative *stronger*: m004's spectrum is not distinguished by multiplicity either). Numbers corrected in an addendum. |
| 8 | **B333** (compositum seam) | "14 of 123 fundamental discriminants have h = 2" — the filter has a sign bug | `b333_fundamental_discriminants.py` (PARI `isfundamental`, `qfbclassno`): **122** fundamental discriminants in [−399, −3], **16** with h = 2: −15, −20, −24, −35, −40, −51, −52, −88, −91, −115, −123, −148, −187, −232, −235, −267. Bug: `compositum_seam.py:63` tests `(-m) % 4 in (2,3)` where the fundamental-discriminant condition needs `m % 4`. | NEGATIVE unchanged (h(−15) = 2 is generic — *more* generic than banked). Script left as-is (a NEGATIVE's artefact; the addendum carries the correction and the fixed count). |
| 9 | **B213** (Higgs-side periods) | four misquotes + the curve is not 40a1 | `b213_40a1.py`: 40a1 = `[0,0,0,−7,−6]`, j = 148176/25; torsion **ℤ/2 × ℤ/2** (bank: ℤ/4); c₂ = c₅ = 2, **∏c_p = 4** (bank: 8); **L(E,1) = 0.742206236711193** (bank: 0.74228); ω₁ = 1.48441247342239, L/ω₁ = **1/2**; Mahler m(Φ) = **0.742264063232416** (bank: 0.74175, "≈ L(E,1)" — the two differ at the 4th digit; not equal). `b213_isogeny_class.py`: Φ's curve has j = **55296/5** = the 40a member `[−32, 64]` ≅ B509/B510's `Y² = X³ − 2X + 1` (u = 2) — **in the 40a class, 2-isogenous to 40a1, not 40a1**; L(E,1) is isogeny-invariant (all four members 0.742206…). | NEGATIVE unchanged (O(1), BSD-generic — every corrected number is still O(1) and generic). The curve-level identification corrected to what B509/B510 already banked. |

**Reported MATCH by the seat (NOT recomputed here — a MATCH changes nothing on main, so nothing was banked on the seat's word; listed so the coverage is visible):** R31 B208 radicand divisibility
(0 failures to 300 000), R33 trace fields (B142/B146/B210/B235/B781/B803/B840/B850; bronze degree 8
resolves B840), R34 E₆ 27 complex / 78 real, R35 nine-of-ten census rows, R36 seven census rows,
R37 B790/B777/B894 (spectra, V₄ table, disc 6237), R38 B854 u(1)⁴ and B866 support reproduce.

## What the silver correction does — and does not — touch (the owner's question, 2026-09-02)

**The chain to the SM: untouched.** m = 1 enters the E₆ chain through the **McKay door**, not through
arithmeticity: π₁(m004) ↠ 2T → E₆. The siblings have no such door — **B237** (silver's π₁ has no 2O
quotient, only S₄; ℚ(√2) is a field-only coincidence), **B1019** (the silver/bronze grammars have NO
McKay door at all, so no m ≥ 2 cascade can begin), **B997** (the golden is the UNIQUE metallic grammar
whose own-conductor shadow is a McKay group — proved over the infinite family). None of the three
mentions arithmeticity; every link downstream of E₆ (cascade, hypercharge, the 3/8, B1236's landing)
is indifferent to whether m136 is arithmetic. Reid's theorem (the figure-eight is the unique
arithmetic *knot complement*) also stands — and since B125 computed m136 arithmetic, m136 is not a
knot complement in S³; Reid never separated golden from silver *inside the bundle family*.

**L161's P0-0 control: weakened, not lost.** P0-0 demanded a handle the golden passes and **both**
siblings fail. B1062 exhibited arithmeticity as that handle and wrote "the gate OPENS — control
exists (arithmetic golden vs non-arithmetic siblings)". Arithmeticity separates golden from **bronze
only**. The silver half of the control now rests on the two other candidate handles L161 itself
named: **B997's own-conductor McKay uniqueness** (golden-specific, proved, and — unlike the tones —
not a transfer-matrix ghost) and B641's ear-independence law. The gate stays open on B997; the
2026-08-13 addendum's "ARITHMETICITY leads" route is downgraded to "arithmeticity separates bronze;
the door separates silver". Stamped into L161 (addendum 2026-09-02) and B1062's note.

**Read under THE LENS:** the correction sharpens what the atom *is*. What singles out m = 1 is not
"arithmetic" (a commensurability-class property m136 shares) but **an arithmetic manifold whose
invariant field carries the 2T door** — ℚ(√−3) with the quotient, versus ℚ(i) without one. Silver is
now a genuine control of the right type: same arithmetic status, different atom, no door. That is a
discriminating fact the record did not have while silver was mis-typed.

## The error class, named

Items 1–2 are one error at two sites: **arithmeticity inferred from the degree of the trace field
instead of the invariant trace field.** For a Kleinian group Γ, kΓ = ℚ(tr Γ⁽²⁾) is the commensurability
invariant (Maclachlan–Reid); ℚ(tr Γ) can be strictly larger (silver: degree 8 vs 2). B1062's table
even recorded the invariant datum (x² = 2 + 2i) beside the wrong inference. Registered in the
ERROR_LEDGER as **E55** with both instances; the check is one line
(`silver_arithmetic.py`: traces of squares, then the Bianchi covolume ratio).

Items 4–6 are **E53** at verdict-file grain (instances #13–#15): the correcting arc exists, the log
knows, the verdict file of the corrected arc does not. The seat's tallies (48/25/24) say this is the
record's dominant drift; a `superseded_by`-sweep instrument is queued as **L197** rather than run
here (it is a judgment sweep over 48 pairs, the B1216 lesson says do not fan it out).

## What the seat got wrong (quarantined)

- **"No observable content" in all nine cells.** Correct as a Gate-5 fact and irrelevant as a
  criticism: the cells are typed as structure by design (WORKING_RULES, the freedom ledger). Read
  under THE LENS, these walls are specifications of the listener map u, not obituaries.
- The **"REPRODUCES"-string lock family** (29 test files, B1147–B1185) and **OA_SLOW gating** (~a
  third of the belt non-recomputing in default CI): both **true as described** (`tests/test_b1160_hypercharge_forced.py:51–53`
  is the shape). Not fixed here — a belt redesign is its own cell (**L197**, second half), and the
  seat's implied reading "the belt is decorative" is wrong: the string locks pin *outputs* against
  drift; what they do not do is *re-run* the derivation. Both facts belong in the reviewer view.
- The seat's paper-count tool caught nothing in the paper: its own regex counts "dimensionful unit"
  as a non-continuous row (7 vs the prose's six). The prose is right; the tool is fixed and locked
  in this cell (`scripts/checks/paper_ledger_counts.py`, `tests/test_paper_ledger_counts.py`).

## Locks

`tests/test_b1237_physics_seat_harvest.py` — the C42 witness recomputes from B1236's committed
script (3, 5, 0); the silver output text carries the arithmetic verdict; B361 carries
`superseded_by: "B367"`; the four propagated notes exist; B333's corrected count (122, 16) is in the
addendum; B213's addendum states 40a-class/2-isogenous; the kill graph carries the two new rows.

## Cost

One seat-day read; six recomputations (SnapPy/PARI/mpmath, each < 2 min); nothing merged; no new
theorem; two flagship-adjacent corrections (B1062's control claim, C42's witness location).
