# B1690 — P-229'S LAST ITEMS ON MAIN: GENESIS §5'S F-FC COLUMN AND sm:B1523 REPRODUCED IN FULL, AND B1652'S FOUR FAILS CELLS CHECKED. EVERY WORD STATE IS CLOSED IN THE FREE-CUSP FRAME, 108 OF B1186'S 112 ARE CLOSED WITH THE SAME FOUR CUSPS OPEN, EVERY WORD STATE TO LENGTH 12 IS PROJECTIVELY RIGID REL CUSP WITH 262 MIRROR-BROKEN, AND EVERY MIRROR-SYMMETRIC THREAD TO LENGTH 16 HAS CS = 0

**Verdict: PROVED (a verification arc).** cc (main), 2026-10-21. POINT_REGISTER P-229 (Review 66's verifications by
consequence), its last two items: GENESIS §5's frames-by-object table and B1652's FAILS cells. 0 of 19.
- **How.** Main's own code, written from the seats' recorded read-outs and rules at the SM seat's commit e1724317, not
  their scripts; every count below was computed on main before the seat's number was compared.
- **GENESIS §5, the F-FC column: reproduced cell for cell.**
  - **The word states (sm:B1385 T1; sm:B1368 for m004 and its levels).** All 758 word states to length 12 have one
    cusp, b₁ = 1 and peripheral rank 1, so no free cusp; so do m004's levels 1–12. The theorem is elementary and main
    re-derives it: for a once-punctured-torus bundle with monodromy φ, H₁ = ℤ ⊕ coker(φ_* − I) and
    det(φ_* − I) = 2 − tr φ ≠ 0 for hyperbolic φ, so b₁ = 1; the puncture loop is a commutator and the section maps to
    the generator, so the cusp's image has rank 1 = b₁.
  - **B1186's 112 (sm:B1369).** The free-cusp census, by main's own homology (the dual spine of the canonical
    triangulation, each cusp's vertex-link cycles), checked against b₁ and the peripheral ranks from SnapPy's
    fundamental group on every member: 35 members carry 83 free cusps; the 77 without one are the 54 one-cusped members
    with b₁ = 1 and 23 multi-cusped members of full peripheral rank; the six one-cusped members with b₁ = 2 are the
    seat's (t06828, o10_150688, o10_150713, o10_150714, o10_150716, o10_150724); m202 and s959 have ranks [2, 2] with
    b₁ = 2. **The region-swap parity**, run with the isometries' exact action on H₁ (the combinatorial automorphisms of
    the canonical triangulation, |Aut| = |Isom| on every member that needs it, the cusp permutations equal to SnapPy's):
    a free cusp c is closed when an isometry fixing c acts by −1 on its free classes, that is (g_* + I) H₁ ⊂ P_c.
    **79 of the 83 close; the four open cusps are the seat's** (o10_150688 c0, o10_150708 c0, o10_150716 c0,
    o10_150725 c1), **so 108 of 112 members are closed**; four cusps close only by orientation-reversing isometries
    (o10_150684 c0 and c1, o10_150725 c0 and c2), as the seat found. The free-cusp theorem and the region-swap lemma
    (sm:B1369 §3) were read and are correct, given the frame's harmonic representative (metric-natural, so an isometry
    carries it to the representative of the image class).
  - **The four residual cusps (sm:B1370's first fact).** Reduced moduli (5√3/2)i on o10_150688 and o10_150716 and
    ±½ + (3√3/2)i (|τ| = √7) on o10_150708 and o10_150725, each with a unique shortest vector (so a unique shortest dual
    vector: in two dimensions the dual lattice is the lattice turned a quarter and rescaled). The deciding Fourier
    coefficients are not computed, here or by the seat.
- **GENESIS §5, the F-AP column's cusp side.** m004's cusp (shape 2√3 i) is not hexagonal and m003's is; of m004's 87
  connected covers of degree 2 to 10, exactly 14 have a hexagonal cusp, all of degree 10. Whether sm:B1501's cones
  complete them (its torus-link census, row 676) is not touched; cube~3.24's cusps are not checked.
- **sm:B1523, the flexible states: reproduced in full (P2 and P5).**
  - **Rigidity.** Every one of the 536 manifolds of the 758 word states to length 12 is infinitesimally projectively
    rigid rel cusp: H¹(M; v) → H¹(∂M; v) is injective, v the nine-dimensional complement of so(3, 1) in sl(4), at the
    hyperbolic holonomy. Main's route: Fox calculus on SnapPy's presentation with its holonomy polished to 200 bits, at
    60 digits, the kernel's dimension as dim S − dim v − dim v^P (S the cocycles whose boundary values are peripheral
    coboundaries). dim H¹(M; v) = 1 and dim v^P = 1 on all 536; the ranks are separated by a gap from 3 × 10⁻²³ (the
    smallest singular value kept, relative) to 3 × 10⁻⁴⁹ (the largest dropped). m004 reproduces Heusener–Porti.
  - **The mirror.** The 758 states are 536 manifolds (isometry signatures). On 262 no isometry inverts the fibre
    boundary (the homological longitude, computed on main from π₁): 131 per sign, 220 chiral and 42 whose
    orientation-reversing symmetries keep the fibre boundary, carrying 482 states; by the shortest word's length 6–12:
    2, 2, 8, 14, 36, 62, 138. Every number is the seat's. That "dualises the family" is "inverts the fibre boundary" is
    the seat's Lemma R (with Heusener–Porti and Ballas for m004); main reads it, does not re-derive it.
- **B1652's FAILS cells.**
  - **W76 (F2 D7): reproduced.** Every Lyndon word of length 2 to 16 in L < R (8 798 threads, b++W, every solution
    geometric): 248 mirror-symmetric (12 by rotation, 210 by reversal, 26 both), and **every one has CS = 0, none π²/2**
    (largest |CS| 6 × 10⁻¹⁴). To length 12: 745 threads, 55 mirror-symmetric, as W75 read.
  - **W83 (F3 D3 and D4): reproduced.** In E₈ the roots orthogonal to an A₂ (colour) number 72 (E₆), and those
    orthogonal also to a root of that E₆ (SU(2)_w) number 30, of type A₅: the commutant is su(6), dimension 35. On
    6 = T ⊗ 2_q with Q₈ on 2_q by ρ_Q and the moves on T as the weave's lifts (B1610's module; the group they generate on
    T has order 96 and acts irreducibly), the trace-free Y commuting with both has dimension **0**; with the moves
    through S₃ (the permutation triplet) **1**; with a trivial action **8**. So the dichotomy holds as stated, in the
    lane's frame and given its dictionary (the lane's scope note, B1652).
  - **W81 (F3 D4, the branching): reproduced.** The 248 under the continuous SU(2)_q ⊂ SU(6)′ with 6 = 2 ⊗ 3, by weights
    from E₈ ⊃ SU(3) × SU(2) × SU(6): **55 + 52 × 2 + 27 × 3 + 2 × 4**. On Q₈ it restricts to the trivial character 55
    times, each non-trivial character 27 times and ρ_Q 56 times (B1689's D3): "2 ⊗ 56" holds for Q₈ only. The
    condensate's placement in the doublets and B3's sign convention are not checked.
  - **W74 (F2 D7): partly verified.** V1 exactly (sympy): C L C = L⁻¹ and C P C = P (L the quarter-turn about e_i, P
    the i–j swap, C = diag(1, 1, −1)); the S-phase condition holds at k = −½, 3/2, 7/2 and for ρ′ at 5/2, and fails at
    ½ and 1; C conj B[l] = B[l] on e_i, v₊, v₋. Main re-derived the T and S laws of f*(τ) = C conj f(−τ̄). V2–V3 from the
    seat's stored W72 output, read: |Im Y| ≤ 1.5 × 10⁻¹³ of |Y|, det Y = 1.23 × 10¹⁰, eigenvalues −76 597, +2 788,
    −57.4, arg det(YY) = 0 to 10⁻¹³, h's imaginary parts ≤ 3 × 10⁻³⁴. **The step "each one-unit space is
    one-dimensional, so f* = f" is W64's K5 (registered, row 1124), not verified on main**: W74's conclusion, real
    Yukawas and J = 0 in the surface frame, is verified given it.
- **What it means.** No status changes. GENESIS §5's F-FC column, its F-AP cusp count, sm:B1523's census behind §5 and
  FK9, and three of B1652's four FAILS cells now rest on computations on main; W74 rests on main's identities and W64's
  dimension count. The §5 cells this arc does not reach (sm:B1386–B1388, B1501's cones, B1503, B1515's indices, B1522's
  M₇–M₁₂, B1532, B1534, B1536, B1546, and the audit lane's R40 and F01) keep GENESIS v1.51's tag.

## 0. Seen first

`VERDICT topic-sweep /free cusp|peripheral rank|B1369|B1385|projectively rigid|rigid rel cusp|mirror-broken|longitude-inverting|B1523|W74|W76|W81|W83|mirror-symmetric thread/
(full text): 6 of 1457 arcs on main match (PROVED 6)` — B1453 and B1462 (the harvests that rowed sm:B1368–B1385 and
sm:B1523), B1465 (the mirror-broken states at their complete points), B1652 (the tribunal that relies on W74–W83),
B1334 and B1460. None re-derives the free-cusp census, the parity, the rigidity census, W76's census or W83's commutant.
**Literature:** Heusener–Porti, infinitesimal projective rigidity under Dehn filling (Geom. Topol. 2011); Ballas,
Danciger and Lee (Geom. Topol. 2018) and Ballas (arXiv:1805.09274) for the family; Epstein–Penner's canonical
decomposition, whose combinatorial automorphisms are the isometries; the standard branchings E₈ ⊃ SU(3) × E₆ and
E₆ ⊃ SU(2) × SU(6) (Slansky 1981).

## 1. Disclosed

- **A void first route.** Main's first rigidity census ran in double precision with a singular-value tolerance relative to
  the largest value; it reported 280 of 536 manifolds non-rigid with dim H¹(M; v) up to 20. Before that output was taken
  as a result, main traced it on b++LLLLLR: a genuine singular value at 1.5 × 10⁻⁸ of the largest fell under the
  tolerance, and on longer presentations double precision showed no gap at all. The census was rerun at 60 digits from
  the polished holonomy (above); the float route's code and output are not kept in this arc.
- **SnapPy's homological longitude needs Sage;** main computes the fibre boundary from π₁ directly (the primitive
  peripheral class killed by the generator of H¹(M; ℚ)).
- **No failing control for rigidity.** Main knows no census manifold that is certainly not rigid rel cusp, so the
  instrument's controls are reproductions (m004, Heusener–Porti; m003; L²R² and R²L) and the gap itself.
- **The parity instrument's controls.** m004 and m003 (b₁ = 1, rank 1), the Whitehead link complement (b₁ = 2, ranks
  [1, 1]) and the Borromean rings complement (b₁ = 3, ranks [1, 1, 1]) with |Aut| = |Isom| = 8 and 48; the identity
  never closes a free cusp (it acts by +1).
- **W74's V3 consequence** ("with one coupling the CKM matrix is 1") is true by construction; main records it, it tests
  nothing.

## 2. Files

- `verification/main_ffc.py` → `main_ffc_words.json`, `main_ffc_family.json` (the F-FC column and sm:B1369);
  `verification/main_s5_extra.py` → `main_s5_extra.json` (m004's levels, the hexagonal cusps);
  `verification/main_b1523.py` → `main_b1523_mirror.json`; `verification/rigidity_mp.py` → `main_b1523_rigidity.json`;
  `verification/main_w76.py` → `main_w76.json`; `verification/main_w81_w83.py` → `main_w81_w83.json`;
  `verification/main_w74.py` → `main_w74.json`.
- The lock: `tests/test_b1690_free_cusps_rigidity_and_the_tribunal_cells.py`.

## Dated note (2026-10-29, Review 72)

- W64's K5, "each one-unit space is one-dimensional" (§ above: "not verified on main"), is computed on main by B1796 (its `verification/w123_check_run.txt`: d(1,0,0), d(0,1,0), d(0,0,1) = 1 1 1).
- W74's conclusion here now rests on main for K5. K4 (weight −½) is P-430.
