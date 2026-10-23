# W136 — the coupling forms: which weights carry modular forms in the three irreps a family coupling may carry (1′, ρ′ and ρ′ ⊗ sgn of the joint family group), and what the least of them are (the rule, committed before the script)

The SM-derivation seat, 2026-10-23. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **W135** found that the joint family group Γ′ allows no τ-independent cubic coupling. So every family mass must come
  from a coupling Y(τ) that is a vector-valued modular form in one of the irreps of Sym³ρ′ = 1′ ⊕ 2ρ′ ⊕ ρ′ ⊗ sgn.
- **Relay §223 named the next count:** which weights carry forms in 1′, ρ′ and ρ′ ⊗ sgn. The owner asked this seat to
  do it (2026-10-23).
- **What the count decides:** where the families' couplings can start, how many independent constants each weight
  allows, and what the least couplings are as functions of τ.

## The objects

- **The joint family bundle** (W135). ρ′ = ρ_T ⊗ χ_η²¹, with ρ_T W123's monomial representation (ρ_T(S) = ζ₈P,
  ρ_T(T) = ζ₈L⁻¹) and χ_η η's multiplier. So ρ′(S) = −P and ρ′(T) = L⁻¹, both signed permutation matrices. Γ′ is
  their image, the cube's rotations (order 24).
  - The other det-1 twists, k = 5 and 13, give Γ′ × ⟨ω⟩. Their Sym³ is the same representation, since the scalars
    cube to 1.
- **The irreps of Γ′,** pulled back to SL(2, ℤ) through ρ′:
  - 1;
  - 1′ = sgn, the sign of the underlying permutation;
  - 2, through S₃;
  - ρ′ itself;
  - ρ′ ⊗ sgn.
- **The forms.** M_w(σ) is the space of holomorphic F: ℍ → ℂ^{dim σ} with F(γτ) = (cτ + d)^w σ(γ)F(τ), holomorphic at
  the cusp, in the record's convention (W45's χ). A coupling of three families, Y(τ)·Φ³, is invariant exactly when Y
  lies in σ ⊂ Sym³ρ′.
- **The theta ring.** v = 2η³R = (−θ₂², −θ₄², iθ₃²) is W123's triplet times η³. By hand it is a weight-1 form with
  multiplier ρ_T ⊗ χ_η³ = ρ′ ⊗ χ_η⁶, and v·v = θ₂⁴ + θ₄⁴ − θ₃⁴ = 0 (Jacobi).
- **The zero-free family** (W133, the web seat's check, B1730). F_a = η^{3−a}(εθ₂^a, εθ₄^a, iθ₃^a) with
  a ≡ 2 (mod 4) and ε = i^{(a+2)/2}. F₂ = 2η⁴R.

## Weave or thread

**WEAVE-type.**
- The moves' joint representation and every irrep of the joint family group.
- Every even weight to 24, all three det-1 twists.
- Claims about every coupling at once. No line is chosen.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| L0 | the instrument. **The group:** Γ′ is 24 signed permutation matrices of determinant 1, ρ′(−I) = 1 and ρ′(T)⁴ = 1. The presentation ⟨s, t \| s², (st)³, t⁴⟩ has order 24 (coset enumeration) and \|SL(2, ℤ/4)\| = 48. So the kernel of ρ′ is ±Γ(4) and Γ′ = PSL(2, ℤ/4) = Γ₄: **the joint family group is the finite modular group of level 4.** **The ring:** v transforms by ρ_T ⊗ χ_η³ under S and T (to 10⁻⁴⁰ at five random τ, the thetas summed in τ), v·v = 0, and the monomials of degree w in v span 2w + 1 independent q-series for every w ≤ 12 (exact rank) | 95% |
| L1 | the count, three routes, for each σ in {1, 1′, 2, ρ′, ρ′ ⊗ sgn} and each even w ≤ 24. (a) Characters on ℂ[v]_w/(v·v), exact, over the 48 elements of the image of SL(2, ℤ) on (v, ρ′). (b) The record's Riemann–Roch formula (W45's χ) for w ≥ 2, and dim M₀(σ) = [σ = 1]. (c) Harmonic restriction: M_w(Γ(4)) ≅ D_w ⊗ sgn^{w/2}, with D_w the spin-w representation of SO(3) restricted to the cube's rotations, from the rotation angles. **The three routes agree for every σ and w.** M(σ) is free over ℂ[E₄, E₆] with generating weights 1: {0}; 1′: {6}; 2: {2, 4}; ρ′: {2, 4, 6}; ρ′ ⊗ sgn: {4, 6, 8}, and each sum equals 12 Σλ over σ(T)'s exponents. The table below holds to w = 12, and the Hilbert series holds to 24. No odd or half-integral weight carries a form (σ(−I) = 1) | 90% |
| L2 | the least forms (exact identities, each checked under S and T at five random τ to 10⁻³⁰). **ρ′ at weight 2:** Y₂ = (v₂v₃, v₃v₁, v₁v₂) = −4iη·F₋₂. **ρ′ ⊗ sgn at weight 4:** Y₄ = v₁v₂v₃·v = 8iη⁹R = 4iη⁵·F₂. **1′ at weight 6:** Y₆ = (v₁v₂v₃)² = −16η¹². Each spans its space (dimension 1 by L1). **So each least coupling form is a power of η times a member of the zero-free family (or 1), and none vanishes on the upper half plane** | 85% |
| L3 | the channels (exact linear algebra). The Γ′-invariant cubics in Φ, linear in a Y of type σ, have dimension 0, 1, 0, 2, 1 for σ = 1, 1′, 2, ρ′, ρ′ ⊗ sgn. A basis: 1′: Y·Φ₁Φ₂Φ₃; ρ′: (Y·Φ)(Φ·Φ) and Σ_a Y_aΦ_a³; ρ′ ⊗ sgn: Σ_a Y_aΦ_a(Φ_{a+1}² − Φ_{a+2}²), indices mod 3. The same holds for k = 5 and 13 (Sym³ρ′_k = Sym³ρ′₂₁ exactly). **The coupling count** C(w) = dim M_w(1′) + 2 dim M_w(ρ′) + dim M_w(ρ′ ⊗ sgn) is 0, 2, 3, 6, 6, 9, 10 at w = 0, 2, …, 12 | 90% |
| L4 | the read-out. The table to w = 24; C(w) to 24; the least coupling at each weight. The mass matrix of the weight-2 coupling, M(h) = g₁[(Y₂·h)𝟙 + Y₂hᵀ + hY₂ᵀ] + 3g₂ diag(Y₂,ₐhₐ), for a Higgs direction h in family space, recorded as found | — |

**The predicted table** (L1; dimensions of M_w(σ), with the total dim M_w(Γ(4)) = 2w + 1 and C(w)):

| w | 1 | 1′ | 2 | ρ′ | ρ′ ⊗ sgn | 2w + 1 | C(w) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| 2 | 0 | 0 | 1 | 1 | 0 | 5 | 2 |
| 4 | 1 | 0 | 1 | 1 | 1 | 9 | 3 |
| 6 | 1 | 1 | 1 | 2 | 1 | 13 | 6 |
| 8 | 1 | 0 | 2 | 2 | 2 | 17 | 6 |
| 10 | 1 | 1 | 2 | 3 | 2 | 21 | 9 |
| 12 | 2 | 1 | 2 | 3 | 3 | 25 | 10 |

## What the outcomes mean (fixed now)

- **L0 to L3 hold.** Then:
  - **The joint frame's couplings are level-4 modular forms.** W58 found that the record's triplet untwists to Γ₄ for
    two characters. Here the det-1 twists that E₈'s family slot requires (W134, W135) all give couplings through Γ₄:
    k = 21 is Γ₄ itself, and k = 5 and 13 have the same Sym³. So the group of the modular-S₄ flavour models is
    reached from the moves and E₈'s condition, with no character chosen.
  - **The least coupling is weight 2, in ρ′,** with two channels. It is η times the zero-free Higgs line F₋₂, so the
    families' least coupling and a zero-free Higgs are one function.
  - **The 1′ channel** (W135's reading: main's zero-diagonal texture d_abc 27₁27₂27₃) starts at weight 6 with η¹², is
    absent at weight 8, and is present at every even weight from 10.
  - **The ρ′ ⊗ sgn channel** starts at weight 4 with η⁹R.
  - **Nothing in this arc fixes the weight.** Each choice leaves C(w) complex constants, plus τ and the Higgs's
    direction. That is the free-number count of the joint frame's Yukawa at weight w. Two things fix the weight: the
    matter's four-dimensional modular weight and the Kähler potential, both out of scope here.
- **L1's routes disagree.** Either the ring misses forms or the formula is misapplied. That is recorded, and L2 and L3
  are read only after it is resolved post hoc.
- **L2 fails** (a least form differs from the prediction by a character or a constant). Recorded as found; the
  identities with η and F_a were by hand.
- **A form appears where the table has none** (1′ below weight 6 or at weight 8; ρ′ ⊗ sgn at weight 2). Recorded as
  found.

## What stays out

- **The coupling's weight:** the families' four-dimensional modular weight and the Kähler potential.
- **Couplings with a character of their own,** such as a supergravity multiplier on the superpotential.
- **The values:** of the constants, of τ, and the Higgs's direction (W133, B1730, B1731; the owner's P-303).
- **The doublet–triplet splitting;** per-line data; the k = 5 and 13 groups beyond their Sym³.

## Seen before the rule (disclosed)

- **Read:**
  - W58: k = 3 and 15 untwist ρ_T to Γ₄. In its sign convention for the twist, its k = 3 is ρ′ here and its k = 15
    is ρ′ ⊗ sgn.
  - NOTE's literature line (Penedo–Petcov; Novichkov–Penedo–Petcov–Titov, in abstract): the lowest-weight level-4
    forms are a doublet and a triplet.
  - W123, W133 and W135's record.
  - The web seat's W133-check relay (the family with both signs).
  - Main's B1730 and B1731 commit messages.
  - The subject lines of the web seat's commits 4542987c2 and bf1bb8713. Its cube_forms_count makes the same count on
    its own code. **Its script and output have not been opened; this arc is blind to them.** They are compared after
    this seat's output is committed, labelled post hoc.
- **By hand:**
  - the kernel ±Γ(4), through the (2, 3, 4) triangle group;
  - v's laws under S and T from the theta transformations;
  - the ring as harmonic polynomials, D_w ⊗ sgn^{w/2};
  - the branching of D_w to the cube's rotations for w ≤ 12, hence the table;
  - the generating weights and the sums 12 Σλ;
  - L2's forms and their identities with η and F_a;
  - L3's invariant cubics and C(w);
  - L4's mass matrix.
- **Not run:** nothing has been computed by a script.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
