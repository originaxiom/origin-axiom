# B1476 — PREREGISTRATION: THE SPIN SWAP, PHASE 1c — the theorem, the ¼ class, the parent's Pin type, and what A5 chose

**Sealed before any cell runs.** cc (main), 2026-10-04. L246 Phase 1c after B1474 (the swap table) and B1475 (no
spin structure of a swap member is mirror-invariant). Three questions, each with a computation: (i) is the fix/swap
class of an amphichiral member read off its Chern–Simons invariant — swap ⟺ CS ≡ ¼ (mod ½)? (ii) is sm:B1382's fact
(m004's two spin structures are the pullbacks of the Gieseking manifold's Pin⁺ and Pin⁻ structures; the extension
route selects B1141's lift within Pin⁺ only) the same bit seen on the knot, verified on main? (iii) what is the
theorem, and what exactly did A5 choose?

## 0. Seen first

- **Repo, by sweep.** `topic_sweep.py "quarter class|1/4 class|CS = 1/4|cs ≡ ¼|Pin\+|Pin-|Pin type|free deck|orientation double cover|free orientation-reversing"`: /quarter class|1/4 class|CS = 1/4|cs ≡ ¼|Pin\+|Pin-|Pin type|free deck|orientation double cover|free orientation-reversing/: 38 of 1348 arcs on main match (NEGATIVE 4, OPEN 3, PROVED 31). Read: **B1224** (amphichirality ⟹ CS ∈ {0, ¼} mod ½; m004, m136, m206 at 0; m003, m135, m207 at ¼), **B1239** (the ¼ class is cusp-local — "the residue is the τ-invariant cusps"; closed amphichiral ⟹ ¼ excluded via APS/η; 37 of 37), **B1235/L194** (free deck ⟹ CS ≡ 0 on 40, then 200 (B1472), orientation double covers — "data, not theorem"), **B279** (the knot's mirror fixes both spin structures; "every ambient symmetry of every knot complement"; the firewall: the η/parity step unbanked), **sm:B1382/B1383** (REGISTERED, L243 (b); the referee's sweep of 2026-10-01 verified B1382's four steps exactly in ℚ(ω) — W·W̄ = +A, a lift sending a ↦ +A extends only into Pin⁺, the other only into Pin⁻), **B1141/B1118** (the spin lift as the last free discrete bit), **B1474, B1475**. **Literature:** every 3-manifold admits a Pin⁻ structure (w₂ + w₁² = 0 in dimension 3), and a Pin± structure on M/τ for a *free* orientation-reversing involution τ pulls back to a τ-invariant spin structure on M — standard (Kirby–Taylor "Pin structures on low-dimensional manifolds"), not re-read here; the η-invariant's role in CS mod ½ for amphichiral manifolds is B1239's APS route.

## 1. The cells, fixed now

- **C1 — the table completed.** Mirror-invariant spin structures for the three fix members B1475 did not run (m206,
  o10_150696, o10_150707), with B1475's instrument; so all thirteen amphichiral rank-one members carry: class
  (all / some / none of Spin(M) mirror-invariant), K, η₀, H¹(M;ℤ/2).
- **C2 — the ¼ law, and the 1/24 lattice.** SnapPy's `chern_simons()` (HP) on all thirteen, folded mod ½ into
  {0, ¼, other} as B1239 did; the table class against the CS class (**P1**). Then, on chat1's handoff of the same day
  (L248: every regular-tetrahedral census manifold has CS ∈ (1/24)ℤ, derived from Re R(e^{iπ/3}) = −π²/12 — each
  regular ideal tetrahedron contributes −π²/12 to the CS part, flattenings add multiples of π²/6, SnapPy divides by 2π²):
  CS on all 112 members of the family and on the 41 chiral rank-one members, the distance to the nearest 1/24, and the
  denominator distribution (**P6**); controls: the first 40 one-cusped census manifolds outside the family (their shape
  fields not ℚ(√−3)) — irrational or a different denominator expected; and Re R(e^{iπ/3}) = −π²/12, Im R(e^{iπ/3}) =
  Cl₂(π/3) = Vol(4₁)/2 computed on this bench to 30 digits.
- **C3 — free or not.** For each reversing isometry found in B1474 (as words τ), whether it acts freely: an isometry
  with a fixed point on a cusped hyperbolic manifold fixes a point of the universal cover — tested at matrix level:
  the antiholomorphic map z ↦ C·conj(z) (the Möbius–conjugate action on ℍ³ built from C) composed with the deck
  group has a fixed point iff some element g has C·conj(ρ(g))… — *the arc uses the simpler necessary condition the
  record already has*: a free orientation-reversing involution makes M an orientation double cover, and B1239/L194's
  census of all orientation double covers has CS ≡ 0 on 240 of 240; so a member at CS = ¼ carries no free reversing
  involution. The arc states which direction is computed (CS) and which is inferred (freeness), and checks the
  inference on m004 (the Gieseking deck is free; CS = 0) and m003 (CS = ¼; so no free reversing involution: m003 is
  not the orientation cover of any non-orientable census manifold — checked against the non-orientable census by
  SnapPy's `orientation_cover()`).
- **C4 — the parent's Pin type on main (sm:B1382 verified).** On m004 with B1474's C (C·conj ρ(g)·C⁻¹ = ρ(τg), η = 1
  for the Gieseking deck τ): C·C̄ commutes with ρ, so by Schur it is a scalar c ∈ ℝ; its sign is the Pin type of the
  extension of that lift — Pin⁺ if +1, Pin⁻ if −1 — and the other lift ρ⊗ε gives the opposite sign. Computed for
  both lifts and for the referee's W (re-run of `r14_axiom_checks.py` (4) from the review lane, pinned). **Then the
  statement for the swap members:** for s₀ there is no C with η = 1 (B1474), so no Pin type is assigned to s₀ by the
  mirror — the bit the knot's construction could not assign (B1382: it is the parent's Pin type, free) is the bit the
  swap members' mirror *moves*; same bit, two faces.
- **C5 — the theorem and A5, written.** (a) *Knot complements in S³ with an orientation-reversing symmetry have both
  spin structures mirror-invariant* (B279's argument: H¹ = ℤ/2, the S³-bounding spin structure is preserved by any
  symmetry of the pair, hence so is the other) — so A5's choice of the knot (B197's tie-break; the family's only
  H₁ = ℤ member) puts the object in the "all" class by theorem. (b) The converse fails (m206, t12839, o10_150707 are
  non-knots in the "all" class). (c) If P1 holds: *on the family's amphichiral rank-one members, swap ⟺ CS ≡ ¼*, and
  the sister m003 — the member A5 excluded — is the smallest swap member. (d) **The owner's rule of 2026-10-04 — "existence emerges from the family as object; we shouldn't tie
  ourselves to m004" — is the frame:** not "relax A5 for m004" but "A5 picked a member; the family is where existence is".
  What the record already runs on the −LR states and the siblings, read from the
  record (not re-derived): which of the record's load-bearing results already run on the −LR states (B1438's slope
  census, B1444's population include −LR levels 1–3), and which are knot-only (B425's torsion, the A-polynomial
  layer, A7's bit via the fibration — B1234/xB012). The owner's decision at this gate is taken in advance by the rule above; the arc records what it means for A5 (a selection of a member, not of the object).
- **C6 — GAP6 narrowed (GENESIS, adoption/amend.py).** My v1.9 wording "no index built on a flat bundle can tell 27 from 27̄; chirality is a statement about curvature" drops hypotheses: it is a Chern–Weil statement on a CLOSED bulk. With the object as boundary the APS index carries the boundary's η — a flat-structure quantity — and the record's own class index (B1297, firing at ±1, ±2 in B1418) is a flat-bundle quantity that tells. Narrowed to: "no characteristic-class index on a closed bulk distinguishes 27 from 27̄ over a flat frame; the boundary's spectral data (η; the H¹-index; the spin swap) are flat quantities that do, and reach discrete data, not continuous values." Credit: codex R89 (2026-10-04) and chat1's handoff (2026-10-04, L247), from opposite sides.

- **C7 — the law outside the family (the owner's "test what would happen if ¼ is true", 2026-10-04).** If swap ⟺
  CS ≡ ¼ is a theorem of amphichiral 3-manifolds and not of this family, it must hold where the arithmetic is absent.
  B1239's census: among the first 3 000 cusped census manifolds the one-cusped amphichiral ones split 9 at zero / 11 at
  ¼, the two-cusped amphichiral 5 at zero; the closed amphichiral 37 are all at zero (¼ excluded by theorem). The matrix
  route of B1474 (`spin_swap.classify`, word length ≤ 7; the K cell where η-sets are not singletons) on every one of
  them that is outside the 112-family, and on the closed 37 (SnapPy's SL2C on the filled triangulation is the closed
  holonomy; the word search is the same). `verification/census_lists.py` (the names, built before the seal — a listing,
  disclosed) and `verification/census_swap.py`.

**Instruments at the seal (sha256):** `phase_1c.py` d0b48d9611321209, `census_swap.py` d5e6c82f9631de4e, `census_lists.py` cd0ff41efe20620e, `r14_axiom_checks_referee.py` 9bec03f5b5792b3e; `adoption/amend.py` (GAP6 → v1.11) built and not applied; `census_lists.json` built before the seal (a listing of names and CS classes — B1239's counts re-derived: 25 cusped amphichiral in the first 3 000, 14 at zero / 11 at ¼, 15 outside the family; 37 closed at zero). None of the cells run on any member.

## 2. Predictions, with priors

| | prediction | prior |
|---|---|---|
| P1 | **swap ⟺ CS ≡ ¼ (mod ½)** on all thirteen: the seven swap members at ¼, the six fix members at 0 | 70% |
| P2 | m206, o10_150696, o10_150707 are in the "all" class (every spin structure mirror-invariant); the family's classes are then all = 5 (m004, m206, t12839, o10_150696, o10_150707), some = 1 (s961), none = 7 | 65% |
| P3 | m003 is not the orientation double cover of any non-orientable census manifold (no free reversing involution), m004 is (the Gieseking's) | 90% |
| P4 | on m004, C·C̄ = +c for one lift and −c for the other (one Pin type each), agreeing with the referee's r14 (4) | 85% |
| P5 | the referee's script re-runs on main and reproduces its four statements | 90% |
| P7 | **outside the family: every amphichiral cusped census manifold at CS = ¼ is a genuine SWAP, every one at CS = 0 is FIX-able** (the law is topological, not arithmetic) | 60% |
| P8 | **every closed amphichiral census manifold (37, all at CS ∈ {0, ½}) is FIX-able** — no closed amphichiral manifold swaps | 70% |
| P6 | **CS ∈ (1/24)ℤ on every one of the 112 family members** (not only the amphichiral), with denominators dividing 24; the 40 outside controls are not on that lattice except at 0 | 80% |

**What a failure would mean.** P7 false with P1 true: the ¼ law is a fact of the ℚ(√−3) family (arithmetic), not of amphichirality — stated as such. P8 false: a closed amphichiral manifold with no mirror-invariant spin structure exists at CS ∈ {0, ½}, and the law's mechanism cannot be the ¼ alone. P1 false: the ¼ class and the spin swap are different partitions of the amphichiral
members — then C2 reports both and the "formula" is withdrawn before it is spoken; the theorem of C5 still stands
on B279 and the tables. P4 false: either B1382 or B1474's η on m004 is wrong, found before any verdict.

## 3. Disclosed

Known before the seal: B1224's six CS classes (m003 ¼, m004 0, m206 0, m207 ¼; m135, m136 outside the family) — four
of the thirteen, consistent with P1, which is why P1 is at 70% and not 50%; for P6, chat1's sweep of 16 regular-tetrahedral
census manifolds (all on the 1/24 lattice; m202 1/12, s959 1/3, v3551 7/24, s958 5/12) and the sep16 lane's xB015 note that
thirteen non-arithmetic family members have 24·CS ∈ ℤ — so P6 is a verification of a stated law on the whole family, at
80% because the derivation is standard (Neumann's complex volume as a sum of Rogers dilogarithms) and the family is
defined by shape field, not by regular tetrahedra (a member need not be built from regular tetrahedra: P6 can fail); B1474/B1475's tables; the referee's
r14 (4) results as read in its sweep; B1239's census. Not computed: CS on the other nine; any Pin sign; m206,
o10_150696, o10_150707's spin tables.

## 4. Scope

Frame F-CI; object the thirteen amphichiral rank-one members; reach *class* for the tables, *general* for C5 (a)
(B279's argument), and *conjectural* for the ¼ law beyond the thirteen (stated as such if P1 holds). No physics:
Pin types and CS classes are mathematics of the family; what the bit is for the observer is Phase 2 and the owner's.
