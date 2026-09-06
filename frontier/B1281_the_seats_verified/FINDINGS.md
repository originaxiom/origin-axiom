# B1281 — THE SEATS VERIFIED: what main and the physics seat solved on chirality since this branch forked, re-run on this bench and re-derived with this branch's own code; the reconciliation with B1268, the B1277 addendum, B1279 and B1280; and the three refinements that flow back

**Date:** 2026-09-07 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (a verification arc: every other-seat script re-run here with its own selftest, every load-bearing statement re-derived independently in `verification/seats_verified.py`) · **Price: unchanged** · **Numbering:** B1281 is the first free number of this branch's reserved range B1278–B1283 (`docs/SM_SEAT_ALIAS_TABLE.md`, banked on main and copied here verbatim).

## 0. Why, and what was fetched

The owner asked for the other seats' branches fetched for what is already solved, and verified. Fetched 2026-09-07:
**origin/main @ 506c591f** (twelve arcs beyond this branch's fork: main's own B1267 and B1272–B1277, then B1290–B1294),
**origin/claude/physics-seat-evaluation @ 659487bb** (the fresh physics seat fc, reports R56–R72; 165 commits beyond main),
**origin/codex/seat-r001 @ f7a49536** (R010–R040; main's B1293 records codex as fully harvested at B1238/B1239). Detached
worktrees of each were made and their scripts run on this bench.

## 1. Every relevant script of the other seats, re-run here

| seat, arc/report | claim | script | here |
|---|---|---|---|
| main B1267 the_deciding_computation | B1260's deciding computation run: h¹(V) = h¹(V\*) = 0 at 25 generic points of W1 and of W2, V0 attains 1; "W1/W2 rigid" | `deciding.py` | `SELFTEST: PASS`, min d₁ singular values 0.032 / 0.020 |
| main B1290 the_index_formula | net chirality = −χ(∂⁺M); annular ∂⁺M gives 0 identically | `index_formula.py` | `SELFTEST: PASS` |
| main B1291 the_parity_of_the_cusp | \|Fix on the cusp\| = \|det(A − I)\| is even with one cusp; 3 excluded on one-cusped manifolds; ≥ 2 cusps escape | lock `test_b1291_parity_of_the_cusp.py` (census 1200 one-cusped) | passed |
| main B1292 the_hatch_is_satisfiable | m202 (2 cusps, hexagonal, vol 4 v_tet, 96 surjections onto 2T, Sym = D₆ with four isometries of \|Fix\| = 3 on both cusps) satisfies the hatch; χ(∂M) = 0 at any cusp count | `m202.py` (SnapPy) | `SELFTEST: PASS` |
| main B1294 the_chirality_bit | L(g) = 1 − s_μ ∈ {0, 2}; the order-4 elements fix two interior points; T-CLOSED-CLOSING-COUNTS-TWO-OR-NOTHING; this branch's B1277-addendum, B1278, B1279 scripts re-run on main's bench (Y₉ numbers reproduced to the number) | `harvest_chirality_bit.py` | `SELFTEST: PASS` |
| main locks for B1267, B1290, B1291, B1292 | | pytest | 29 passed |
| fc R69 | Fix(θ) as a singular charge locus: χ(M ∖ arcs) = −2, net ±2 or 0; every filling closes the arcs (1 + [p even] loops, χ = 0) | `r69_arcs_cut_corners.py` | rc 0 |
| fc R71 | the eight cusp maps match this branch's two tables entry by entry; \|Fix\| = [0,0,0,0,0,0,4,4]; the θ-odd region-swap theorem (χ(∂⁺) = χ(∂⁻) = 0 on 480² grids for every allowed field); the corners on every allowed field's zero set (10⁻¹⁴) | `r71_seats_on_the_cusp.py` | `SELFTEST: PASS` |
| fc R71 | the θ-even count is vector-like or SU(3)-anomalous on all 928 directions tested; S(u) = 2·⊕(27_q ⊕ 27_q∘θ) holds for all | `r71_theta_even_pairing.py` | `SELFTEST: PASS` |
| fc R72 | the inner lift Ad(exp πiρ^∨): 32 fixed roots, A₅ ⊕ A₁ (dim 38); the order-3 lift: 18, A₂³ (dim 24); under the inner lift m004's arcs give 2·(16 ⊕ 10 ⊕ 1) | `r72_inner_lift.py` | `SELFTEST: PASS` |
| fc R72b | m202's 180 automorphisms → 12 isometries; all 96 axes of the order-3 lifts, 115 of order 6, 117 of order 2 run from cusp 0 to cusp 1 | `r72b_m202_lines.py` | `SELFTEST: PASS` |
| fc R72 / R72d | m202 = otet04_00000; 72 multi-cusped tetrahedral manifolds ≤ 12 tetrahedra, fixed-line counts {1: 6, 2: 14, 3: 7, 4: 48, 6: 13, 8: 3, 10: 1}; 7 with an isometry fixing exactly three lines | `r72_m202_snappy.py`, `r72d_census_menu.py` | `SELFTEST: PASS` both |
| codex R040 | closed free orientation-reversing involution ⟹ CS = 0; all 1260 cusped orientation covers CS-zero numerically | `free_deck_cs.py` | PASS (harvested on main at B1238/B1239) |

## 2. Re-derived with this branch's code (`verification/seats_verified.py`, `SELFTEST: PASS`)

- **A (B1291).** For the eight affine cusp maps of B1279's table, \|det(A − I)\| = \|(s_μ − 1)(s_λ − 1)\| = [0,0,4,4,0,0,0,0]: only the two inversions have fixed points on the cusp, four each — B1279's and the addendum's four corners. Over the finite-order classes of GL(2, ℤ), \|det(A − I)\| ∈ {0,1,2,3,4} with 3 only from (det 1, tr −1), the order-3 rotation; with one cusp every fixed geodesic line has both ends there, so the count is even: **three is excluded on m004's cusp by parity.**
- **B (B1294).** H₁(m004) = ℤ⟨μ⟩ and H₂ = 0, so L(g) = 1 − s_μ = [0,0,2,2,2,2,0,0] over the eight: the inversions' two arcs (χ = 2, the corners their ends) and the order-4 elements' two interior points are the L = 2 cases. On a closed rational-homology-sphere closing L(g) = 1 − deg g: the fixed-locus 2 needs an orientation-reversing isometry, i.e. an amphicheiral closing.
- **C (fc R72).** On E₆ the inner lift Ad(exp πiρ^∨) acts on the root α by (−1)^{ht α}: 32 of 72 roots fixed, fixed algebra of dimension 38 with Dynkin components (5, 1) = A₅ ⊕ A₁; the order-3 inner lift (e^{2πi ht/3}) fixes 18 roots, dimension 24, components (2, 2, 2) = A₂³; the outer lift θ_D fixes 24 roots and one combination of each of the 12 σ-pairs plus 4 of the Cartan: f₄, dimension 52. **B1280 adds the resolution on the geometric germ:** ι\*ρ ≅ θρ for every deformation of the geometric holonomy, so an inner lift (which would need ι\*ρ ≅ ρ) exists only on the F₄-stable locus; off it the lift of the inversion to E₆ is the outer one, forced.
- **D (fc R71, the region-swap theorem).** For g∘σ = −g with σ = −1 on the torus and transverse zeros, σ maps {g > 0} onto {g < 0}, so χ(∂⁺) = χ(∂⁻), and χ(∂⁺) + χ(∂⁻) = χ(T²) − χ(zero set) = 0: both vanish. Checked on six random θ-odd trigonometric fields with a cubical Euler characteristic (all (0, 0)); the control, an even field whose positive region is a disc, returns 1; the whole torus 0. **This makes the B1277 addendum's θ-odd "no" exact and voids its c₍±2,0₎ caveat**: the caveat's product mode has a non-transverse zero set, on which χ(∂⁺M) is undefined rather than nonzero, and any allowed perturbation returns 0.
- **E (B1292, R72; SnapPy).** m004: one cusp, vol = 2 v_tet, cusp shape 2√3 i (rectangular), \|Sym\| = 8, amphicheiral. m202: two cusps, vol = 4 v_tet, both cusp shapes e^{iπ/3} (hexagonal), \|Sym\| = 12, **chiral**.

## 3. Reconciliation with this branch

**(a) Main's B1267 and this branch's B1280 (W1/W2).** Same answer, N = 0; main sampled 25 generic points per component, B1280 proved it for every point, twist and cusped cover. **One refinement flows back:** "W1 and W2 are rigid — h¹ = 0, no modes" is true at generic points and false on the curve K = {μ has an eigenvalue in μ₃}: there h¹(M; V) = 1 (and 2 at the repeated-eigenvalue points on even covers) — K is exactly the "special locus" main's B1267 addendum says a revival must construct rather than sample for, and B1280 shows N = 0 on it because V ≅ τ\*V\* (the two sheets of the trace coordinates coincide there). B1260's route is closed by theorem, not by absence.

**(b) Main's B1290, fc's R71 and the B1277 addendum (∂⁺M).** Three benches, one statement: for a smooth θ-odd Higgs field ∂⁺M is annular and χ = 0. R71's region-swap theorem is the exact form; the addendum's leading-mode argument and its caveat are superseded by it (recorded in the addendum). **Main's door D4 (compute c₍±2,0₎) is therefore moot for the smooth θ-odd field**; what remains of D4 is its closed-manifold census half.

**(c) Main's B1291/B1292/B1294, fc's R69–R72 and this branch's B1279/B1280 (the fixed loci).** The parity theorem's four fixed points on m004's cusp are B1279's corners; B1294's L(g) ∈ {0, 2} is the same D₄ table read through Lefschetz. fc's ±2 is a **different quantity** from this branch's N: N(V) = h¹(V) − h¹(V\*) of a flat local system (zero by theorem on every system this branch supplies), fc's count is Pantev–Wijnholt's index for a *singular θ-even abelian Higgs configuration* charged on the fixed arcs — a modelling choice main names as its assumption 1. Under the outer lift of the inversion that count is vector-like or SU(3)-anomalous on every direction tested (R71); under the inner lift it is 2·(16 ⊕ 10 ⊕ 1) (R72). B1280 fixes the lift where it can: on the germ of the geometric E₆ holonomy the lift is outer, so the inner-lift count does not live there; it lives on backgrounds where the E₆ holonomy is abelian on the Higgs direction, about which B1280 is silent. **No contradiction anywhere; the seats computed different things and each is right about its object** — fc's R71 §0 says the same.

**(d) B1294's theorem and B1279's mirror pairing.** "On a closed closing you may have the fixed-locus 2 or the c-breaking, not both" is the same wall B1279 met from Y₉ (every SM vacuum mirror-paired). B1294 re-ran this branch's `arcs_and_corners.py`, `symmetries_on_the_lines.py` and `six_fold_closing.py` on main's bench and reproduced Y₉'s 5776 / 147 / 145 / 737 568 / 706 464 / 568 656 / 19 624 to the number; this arc verifies main's and fc's in return. Two-way verification is complete for everything either side has on chirality.

## 4. What is new for this branch, with the seats' own fences

1. **The parity theorem (B1291):** the generation count 3 can never come from a one-cusped manifold's fixed loci — not absent, excluded; ≥ 2 cusps is the escape, and m202 realises \|Fix\| = 3 on both cusps (B1292).
2. **The two-cusped sibling m202 (B1292, R72):** tetrahedral (4 regular ideal tetrahedra, vol = 2 vol(m004)), cusped arithmetic over ℚ(√−3) hence commensurable with m004, 96 surjections onto 2T, Sym = D₆, chiral, a ℤ/6 whose order-3 element fixes three geodesic lines, each running from cusp 0 to cusp 1. "Leave the knot, keep the field": E₆ comes through ℚ(√−3) and 2T, which m202 keeps.
3. **fc's frontier count (R72, not banked, fenced by fc):** for an order-3 symmetry only the inner lift exists (Out(E₆) = ℤ/2 has no ℤ/3), it centralises A₂³, every Cartan direction is even, and Pantev–Wijnholt's count on the three fixed lines with equal charges is ±3 for every charged component: **3·(16 ⊕ 10 ⊕ 1) on the SO(10) direction, anomaly-free**, or 3·(10 ⊕ 5̄) on 170 anomaly-free SU(5) directions, or one quark family Q ⊕ uᶜ ⊕ dᶜ on 84 SU(3)×SU(2) directions. fc's fences, carried: the configuration is a θ-equivariant abelian Higgs locus (assumed, not derived); the equal-sign assignment is a choice ("three is in the menu {0, ±1, ±2, ±3, ±4, ±6}, not selected by it"); PW's formula is cited, not derived; a generation would be a charged component under u, not a 27; I-26 is unpaid.
4. **Main's masterplan v3 doors:** D1 (B1296, drop θ-equivariance; expected count 2), D4 (B1295, the c₍±2,0₎ computation and the closed-closing census), D2 (B1297+, PW §3.1 spectral covers via the 3-fold cyclic cover). Of these, D4's first half is moot by R71 (above); D1's expected 2 is fc's inner-lift count; D2 is the T-brane route the chirality map's O4 also names.
5. **Numbering:** main resolved the B1267+ collision with an alias table and a reserved range; this branch's arcs are cited on main as sB1267…sB1276 (and this branch's B1277, pushed after the table, collides with main's B1277 as B1294 records); B1278–B1283 are this branch's; this arc is B1281.

## 5. What it changes here

- `docs/CHIRALITY_MAP_2026-09-06.md`: two walls added (parity; Lefschetz two-or-nothing), the addendum's caveat retired, and a new open item O6 — the two-cusped sibling — with fc's count and fences.
- L204's caveat is closed by the region-swap theorem; **L208 registered:** m202 as the two-cusped carrier — verify fc's count independently (the lines, the charges, the lift), and ask B1280's question there (which local systems of π₁(m202) are isometry-paired with their duals).
- The chirality bit's possible carriers are now three: the singular G₂ closing, the observer, and a two-cusped commensurable sibling with an order-3 isometry. Values: 0 of 19; no identification moves; price unchanged.

## Controls (MB12)

- Every other-seat script was run from a detached worktree of its own branch, unmodified, and judged by its own selftest; nothing was accepted from a claim line alone.
- Every load-bearing number was re-derived with independent code here (§2): the eight-map parity vector, the Lefschetz numbers, the three lift algebras with their Dynkin types, the region-swap theorem with a failing control, m202's invariants from SnapPy.
- The reconciliation names what each seat computed; where the quantities differ (N versus the singular-locus count) it says so rather than reading one as the other.

## Verification

`verification/seats_verified.py` (~10 s; `SELFTEST: PASS`; run record `verification/seats_verified_run.txt`; SnapPy part optional). Lock: `tests/test_b1281_the_seats_verified.py`. The other seats' run records are theirs (`frontier/B1290…B1294/verification` on main; `reports/fresh_physics_seat_2026-09-01/computations/*_run.txt` on the physics-seat branch); this bench's re-runs are recorded in §1. Feeds on: B1280, B1279, B1278, B1277 (and its addendum), B1268, B1260, B71; main's B1267, B1290–B1294; fc's R56, R61, R62, R69–R72; codex R040. Registers no identification change.
