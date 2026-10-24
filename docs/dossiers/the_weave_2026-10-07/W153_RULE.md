# W153 — the ladder: is the prime 5 forced? The moves' finite quotients stop at level 5, whose McKay lattice E₈ is the only unimodular rung, and no forced structure on record uses level 5 (the rule, committed before the script)

The SM-derivation seat, 2026-10-24. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The owner's question** (2026-10-24), on the ledger's E₈ row: "can we derive it and make it unconditional, are we
  at the right moment to probe it once more, clarify it". The ledger's corrected row: E₈ is computed from the moves
  once the prime 5 is given (W135, K0, rebuilding B1270's icosians), and nothing on record forces the prime. B1270 took
  the 5 from the golden face, one thread.
- **The owner's ruling** on this seat's recommendation, a data-free arc that sets the question out, rule first: "I
  accept your recommendations that you just laid out."
- **The ledger's section 6** stated the hand check that motivates the arc (below, "Seen before the rule").

## The objects

- **The moves' group** Γ = PSL(2, ℤ) = ⟨S, U ∣ S², U³⟩, with the parabolic T = SU. The record's moves L and R are
  parabolics conjugate to T and T⁻¹, so the normal closure of T^N contains L^N and R^N.
- **The ladder:** Δ(2, 3, N) = Γ / ⟨⟨T^N⟩⟩ = ⟨S, U ∣ S², U³, (SU)^N⟩, for N = 2, 3, …
- **The binary groups:** 2Δ(2, 3, N) = ⟨a, b⟩ ⊂ SU(2), with a of order 4, b of order 6 and ab of order 2N. As unit
  quaternions, a = n₁ and b = cos(π/3) + sin(π/3)n₂, with unit pure quaternions n₁, n₂ and n₁·n₂ = −cos(π/N)/sin(π/3).
- **The diagrams:** T(2, 3, N), the tree with arms of 1, 2 and N − 1 nodes from one centre (N + 3 nodes), its Cartan
  matrix C, and its affine extension T̃(2, 3, N).
- **The McKay graph** of a finite G ⊂ SU(2): one vertex per irreducible representation, and A_ij = ⟨V ⊗ χ_i, χ_j⟩ for
  the natural representation V.
- **The icosian E₈** of W135 (K0): B1270's 240 roots over ℚ(√5), with the bilinear form `bil`, the unit 1 and W135's
  `frame` (the E₆ cut by an order-3 unit w: the roots orthogonal to 1 and w).

## Weave or thread

**L1 to L4 are weave-type.** They concern the moves' group and every one of its finite quotients at once, and the
lattice W135 built from the moves. No thread is used. **L5 is a census** over a stated list of the record's forced
structures (the ledger's FORCED rows, W136, W152, W28 and B1601), with none hand-picked. **R** states rules and
computes nothing.

## The cells, with predictions, priors and pre-mortems

| cell | prediction | prior |
| --- | --- | --- |
| L1 | **Klein's ladder (exact).** Coset enumeration (sympy) gives \|Δ(2, 3, N)\| = 6, 12, 24, 60 for N = 2, 3, 4, 5. These equal \|PSL(2, ℤ/N)\| (counted directly) and the rotation groups of the dihedron, tetrahedron, octahedron and icosahedron. For N = 6 and N = 7 the group is infinite: N = 6 by an affine representation (S a half turn, U a third of a turn about another point) in which S·(USU⁻¹) is a nonzero translation; N = 7 by a representation in SL(2, ℝ) satisfying the relations to 10⁻⁴⁰ with an element of trace above 2 in absolute value | 99% |
| L2 | **McKay (to 10⁻⁹, then exact integers).** For N = 2, 3, 4, 5 the binary group has order 12, 24, 48, 120, and its character table (Burnside's algorithm on the class algebra) passes both orthogonality relations. Its McKay graph is isomorphic to T̃(2, 3, N): D̃₅, Ẽ₆, Ẽ₇, Ẽ₈. The trivial representation is an extending node, and removing it leaves T(2, 3, N): D₅, E₆, E₇, E₈. The dimensions of the irreducibles are the null vector of the affine Cartan matrix, with Σd² = \|G\|. **SL(2, ℤ/N) is the binary group only at N = 3 and N = 5:** their element-order counts agree there (2T and 2I) and differ at N = 2 (orders 6 against 12) and N = 4 (seven involutions against one) | 93% |
| L3 | **The determinants and the end of the ladder (exact).** det C(T(2, 3, N)) = 6 − N for N = 2, …, 8 (4, 3, 2, 1, 0, −1, −2), and 6N(1/2 + 1/3 + 1/N − 1) = 6 − N identically (sympy). So the ladder is finite exactly while 1/2 + 1/3 + 1/N > 1, that is N < 6 = 2·3. The last finite rung is N = 5, and it is the only unimodular one. The moves' own numbers: S has order 4 and SU order 6 in SL(2, ℤ), and SL(2, ℤ)'s abelianization is ℤ/12 (sympy) | 99% |
| L4 | **The chain inside the icosian E₈ (exact over ℚ(√5)).** The roots orthogonal to 1 number 126; their ℤ-span has rank 7 and Gram determinant 2 (E₇). Conjugation by every unit icosian fixes this set, and it contains each of W135's 10 E₆ frames. Inside one E₆ frame (an order-3 unit w), each root r of each of its six classes of 27 cuts exactly 40 frame roots orthogonal to it, whose ℤ-span has rank 5 and Gram determinant 4 (D₅). The 162 roots give 27 distinct D₅ sets per frame. The frame's stabilizer under conjugation has order 6 as a permutation group, so the 27 are not one orbit: the D₅ rung is not unique up to the moves, while E₇ is unique and E₆ unique up to the moves (W135) | 85% |
| L5 | **The levels the record's forced structures use (exact, and read from the record).** Each prime below is 2 or 3; 5 occurs nowhere. The parabolic orders: ρ′(T) has order 4, W136's level-4 family group, recomputed from W134's `rho_exact` and the twist k = 21; the theta qubit's g_T (W152) has projective order 4; W28's lift e^{iπZ/4} has order 8 in SU(2) and projective order 4; the η multiplier χ_η(T) = e^{2πi/24} has order 24 = 2³·3. The common point (B1601, verified in W16) is read from W16's JSON: its ideal lies over one prime of norm 3 on odd trace and over 2 on even trace | 90% |
| R | **The rules and what each gives** (stated now; no prediction and no computation; the arc does not choose) | — |

**R, the rules, stated before the run.**
- **R1, every finite rung at once.** Take every N at which the moves' quotient by T^N is finite (L1: N = 2, 3, 4, 5).
  The McKay algebras D₅, E₆, E₇, E₈ are nested, since T(2, 3, N) is a subdiagram of T(2, 3, N + 1). So the least
  algebra holding them all is E₈. The prime 5 is then forced, as the largest N with 1/2 + 1/3 + 1/N > 1. That bound
  comes from the moves' own torsion orders, 2 and 3 (L3).
- **R2, invariance under every move.** A positive-definite even lattice whose theta series is invariant under the
  whole modular group is unimodular (classical: Serre, A Course in Arithmetic, chapter VII). On the ladder only
  det = 6 − N = 1 passes, so N = 5, E₈. This needs a lattice partition function in the joint action; none is on record.
- **R3, only the levels the record's forced structures use.** If L5 holds, they are 3 and 4, with 2. The top rung is
  then E₇ (2O, level 4), not E₈.
- **What the arc can and cannot settle.** It establishes the facts each rule rests on. It cannot say which rule is the
  principle's: that is the owner's ruling, with the seats consulted, as for the breaking sentence. Under every rule the
  step from the algebra to the loop's fields stays GENESIS FK11's.

**Pre-mortems** (how each cell could fail for a reason that is not the finding):
- **L1.**
  - sympy's coset enumeration needs a bound on its table; for orders up to 60 the default suffices.
  - The infinite cases are shown by representations, not by enumeration, which could not terminate.
  - The SL(2, ℝ) entries for N = 7 come from solving trace conditions at 50 digits; a relation missed at 10⁻⁴⁰ would
    be a construction slip, not a finding.
- **L2.**
  - The groups are generated numerically in SU(2), with keys rounded at 10⁻⁹; orders up to 120 sit far from that
    scale.
  - Burnside's algorithm needs a random combination of class matrices with distinct eigenvalues. A repeated eigenvalue
    is detected and the draw repeated (a fixed seed).
  - Graph isomorphism is networkx's, on graphs of at most 9 vertices.
  - The order-count comparison is a necessary check of the isomorphisms with 2T and 2I. They are classical (SL(2, 𝔽₃)
    ≅ 2T, SL(2, 𝔽₅) ≅ 2I) and are not rebuilt here.
- **L3.** Exact. The abelianization is computed from the presentation ⟨S, U ∣ S⁴, U⁶, S²U⁻³⟩ of SL(2, ℤ).
- **L4.**
  - B1270's module and W135's `frame` are imported, not rewritten.
  - The moves act on the frames by conjugation, as in W135. Under left multiplication the root 1 moves, so E₇'s
    uniqueness is stated for W135's action only.
  - The ℤ-spans' Gram determinants use W135's Hermite-normal-form routine on the coordinates.
  - The stabilizer's order 6 follows from W135's transitivity (60 / 10, the units acting through A₅). If the
    permutation group came out larger, the bound in the prediction would be wrong, and the orbit count is read off as
    computed.
- **L5.**
  - The list of forced structures is the ledger's, fixed here. A structure missing from it is not counted.
  - The common point's primes are read from the record, not recomputed: W16's run took 1 200 digits and PARI.
  - "Level" here means the order of the image of the parabolic. For N ≤ 5 that order fixes the congruence level,
    since Γ(N) is the normal closure of T^N there; for the η multiplier's 24 it is the character's order only.
- **R.** No computation.

## What the outcomes mean (fixed now)

- **L1 to L3 hold.** The prime 5 is not an outside input in the ladder. It is the last N at which the moves' quotient
  by a power of the parabolic is finite, and the bound is fixed by the moves' own orders, 2 and 3. E₈ is the top rung,
  and the only unimodular one. The golden thread is not needed to name it.
- **L4 holds.** The lattice W135 built from the moves carries the chain E₇ ⊃ E₆ ⊃ D₅. E₇ is unique, E₆ is unique up
  to the moves, and D₅ is not.
- **L5 holds.** No forced structure on record uses level 5. So E₈ is forced under R1 or R2, and not under R3, whose top
  rung is E₇.
- **The verdict will be a map, not a selection:** each rule with the algebra it forces. The choice among them goes to
  the owner.
- **Any cell fails:** the failure is the finding, and it is diagnosed before anything else is said.
- **This is data-free,** so it is not a trial.

## What stays out

- The step from an algebra or a lattice to the loop's fields (GENESIS FK11).
- Any dynamics that would realise a quotient by T^N.
- The heterotic and Narain constructions in which modular invariance fixes the lattice (R2 cites only the lattice
  theorem).
- E₇'s and D₅'s frames under left multiplication.

## Seen before the rule (disclosed)

- **Run in the scratchpad, by hand, before this rule:** sympy's coset enumeration of Δ(2, 3, N) for N = 2, …, 5
  (6, 12, 24, 60); |PSL(2, ℤ/N)| and the involutions of SL(2, ℤ/N) for N = 2, …, 7 (6, 12, 24, 60, 72, 168;
  involutions 3, 1, 7, 1, 7, 1); det C(T(2, 3, N)) for N = 2, …, 7 (4, 3, 2, 1, 0, −1). So L1's finite orders and L3's
  determinants are seen, and the run confirms them in committed code. It is not an independent test of them.
- **Read:** W135's K0 code and its NOTE entry, W136's L0, W152's qubit group, W28's lifts, W16's B1601 entry, B1270's
  PROGRESS_LOG line ("the golden face's own McKay lattice"), and W31's "the record's order-5 structures are properties
  of the modulus or of threads".
- **By hand:** the quaternion construction of the binary groups; the D₅ count from E₆ ⊃ D₅ × U(1), with the 27 the
  orbit of a minuscule weight and |W(E₆)|/|W(D₅)| = 51 840 / 1 920 = 27; the stabilizer bound 60 / 10 = 6.
- **Not run:** no script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
