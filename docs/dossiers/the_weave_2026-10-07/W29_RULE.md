# W29 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-08. Committed before the code that reads it runs. Values already seen are listed.
Nothing here is a result.

## Why this route

- **The owner's approved plan, step 3** (after W28, the foundation).
- **W25 showed what the gauge side lacks.** The weave's holonomy Q₈ has only real and quaternionic irreducibles, so
  every gauge reading of it is self-conjugate.
- **The contemplation's lead.**
  - The qubit's flux −1 is blind to orientation: −1 = (−1)⁻¹. A qutrit flux ω is not, since ω ≠ ω⁻¹.
  - Qubit ⊗ qutrit is the ℤ₆ Heisenberg group H₆. Its defining 6 is complex.
  - In E₈ ⊃ (SU(3) × SU(2) × SU(6)′)/ℤ₆, with H₆ in SU(6)′, its centraliser should be exactly SU(3) × SU(2).
- **This arc tests that lead:**
  - the centraliser;
  - the matter and its type;
  - the flux's identity;
  - the end condition at the puncture under the moves;
  - the anomalies;
  - the verdict.

## Weave or thread?

- **The object is chosen, not forced.**
  - The weave forces the qubit point (W2). A qutrit flux is not among the weave's forced objects, and whether anything
    forces it is step 4 of the plan, not computed here.
  - So every claim below is conditional: **if** the shared fibre carried the ℤ₆ flux.
- **The computations are joint.** All moves act together (the lifts of L and R; −I and P as named), the quantity is
  the joint commutant, and the claims are about the common point every move fixes.
- So this is a weave-type computation on a hand-picked structure. It is labelled so, and it cannot by itself answer a
  weave question.

## The objects

- **The pair.** ζ = e^{2πi/6}, C = diag(ζ^k) and S the cyclic shift |k⟩ ↦ |k + 1⟩ on ℂ⁶ (k = 0, …, 5). Then A = λC and
  B = λS, with λ = e^{iπ/6}, so that both have determinant 1.
- **H₆ = ⟨A, B⟩ ⊂ SU(6)′.** ABA⁻¹B⁻¹ = ζ·1, the flux at the puncture.
- **The 248's characters.** By W25's chi248 (through SU(3) × SU(2) × SU(6)′):
  248 = (8, 1, 1) + (1, 3, 1) + (1, 1, 35) + (3, 2, 6) + (3̄, 2, 6̄) + (3̄, 1, 15) + (3, 1, 15̄) + (1, 2, 20).
  - The pairing of 3 against 3̄ is fixed up to SU(3)'s outer automorphism: the diagonal ℤ₆ must act trivially.
  - So the partners of the 6 and of the 15 are conjugate. Only that relative fact is used.
- **The index on the punctured fibre** (W22's rule, extended).
  - A sector whose puncture holonomy is e^{2πiα} on all r of its channels (0 < α < 1) has, in each channel, one
    singular solution of each chirality, r^{−α} and r^{α−1}.
  - A chirality-preserving end condition is the subspace Λ₊ of channels where the holomorphic singular solution is
    allowed.
  - Riemann–Roch on the parabolic extension gives index = −rα + dim Λ₊.
  - So the 6-sector (α = 1/6) has index −1 + d₁, and the 15-sector (α = 1/3) has −5 + d₂. The 20-sector (α = ½) is
    self-conjugate under the 248's reality, so its index is 0 (CPT).

## The cells, with predictions

The script is `the_z6_twist_eater.py`, writing `.json` beside it. Groups of order at most 216; characters by numpy on
roots of unity; the lemma of Z1 exact.

- **Z1, the group.**
  - |H₆| = 216. Its centre is the scalars ⟨ζ⟩, of order 6, and the commutator is ζ·1.
  - It is irreducible (commutant 1), and the 6 has Frobenius–Schur indicator 0: it is complex.
  - Under the Chinese remainder ordering, C = Z ⊗ C₃⁻¹ and S = X ⊗ S₃ exactly. So H₆ is the weave's qubit Pauli
    group tensored with a qutrit Heisenberg pair, and A³, B³ are iZ ⊗ 1 and iX ⊗ 1.
  - **The lemma (exact).** Any pair with commutator ζ·1₆ acts irreducibly: an invariant W has ζ^{dim W} = 1. So no
    U(1) in SU(6)′ commutes with H₆.
  - **Prior 99%.**
- **Z2, the centralisers in E₈** (dimension = the mean of chi248):
  - H₆: **11**, exactly SU(3) × SU(2);
  - the weave's qubit Q₈ (ρ_Q ⊗ 1₃): 55, F₄ × SU(2) (W24);
  - the qutrit alone (1₂ ⊗ H₃): **22**, SU(3) × G₂;
  - the flux ⟨ζ·1⟩ alone: 46, SU(3) × SU(2) × SU(6)′.
  - **Prior 95%** for 11 and 90% for 22.
- **Z3, the matter, by isotypic structure under H₆.**
  - The 6 is one type, with multiplicity space (3, 2), dimension 6, by characters.
  - The 15 = Λ²6 has four types of dimension 3: one twice and three once ([(3, 2), (3, 1), (3, 1), (3, 1)]).
    - On each type, A³ and B³ act as signs s_Z and s_X.
    - The doubly occurring type has (+, +), the qubit's trivial character.
    - The three single ones carry the three non-trivial characters: the three Pauli axes, the weave's parities.
  - The 20 = Λ³6 has nine types of dimension 2: one twice and eight once. A² and B² act by cube roots of unity. The
    doubly occurring type is qutrit-blind, and the eight single ones carry the eight non-trivial qutrit labels (the four
    lines of ℙ¹(𝔽₃), in conjugate pairs).
  - The adjoint 35 is 35 distinct characters, each once.
  - **Prior 85%.**
- **Z4, the flux and the orientation.**
  - exp(2πi diag(1/6, 1/6, 1/6, 1/6, 1/6, −5/6)) = ζ·1₆ (exact). Read through E₈ ⊃ SU(5) × SU(5)′ (the 6 =
    5_{1/6} + 1_{−5/6}), the flux is e^{2πiY}, the Standard Model's ℤ₆ generator together with SU(3) × SU(2)'s centre.
    That reading is a READING.
  - The moves L, R and −I keep the commutator ζ. The swap P sends it to ζ̄ (the 6 to the 6̄), and no unitary realises P
    on the pair: the intertwiner equations have only the zero solution.
  - **Prior 99%.**
- **Z5, the moves at the puncture.**
  - The lifts of L, R and −I exist on ℂ⁶ (each solution space of dimension 1). The lift of −I is the parity |k⟩ ↦ |−k⟩
    up to scalar.
  - The lifts of L and R have commutant 2, splitting the 6 as 4 ⊕ 2 (the −I lift's eigenspaces).
  - So the 6-sector's index sets are:
    - the moves: {−1, 1, 3, 5};
    - locality (the flux is central, the puncture's symmetry is U(6)): {−1, 5}.
  - The index-0 condition that a smooth E₈ field would give (traceless weights, d₁ = 1) is not move-invariant.
  - On Λ²ℂ⁶ (the 15-sector) the lifts' isotypic structure is [(1, 1), (2, 1), (3, 1), (3, 1), (6, 1)].
  - **Prior 85%** (75% for the Λ² structure).
- **Z6, the anomalies.**
  - SU(3)³ = 2 n(3, 2) − n(3̄, 1) = 3 + 2d₁ − d₂. It vanishes exactly when n(3̄, 1) = 2 n(3, 2), the Standard Model's
    two antiquark singlets per doublet.
  - **Under the moves:** every n(3, 2) ∈ {−1, 1, 3, 5} has an SU(3)³-free completion (d₂ = 3, 7, 11, 15 are subset
    sums). Three is allowed, not forced.
  - **Under locality:** of the four (n(3, 2), n(3̄, 1)) ∈ {−1, 5} × {−5, 10}, only (5, 10) is free. That is five, not
    three.
  - The coloured sector gives 3|n(3, 2)| SU(2) doublets, an odd number for every move-invariant condition. The
    doublet sector is real (index 0), so it gives no chiral leptons.
  - **Prior 90%.**
- **Z7, the verdict.**
  - **A structural echo.** The joint centraliser of qubit and qutrit is exactly the Standard Model's SU(3) × SU(2); its
    quark doublets are complex; and its flux is e^{2πiY}.
  - **Not a derivation**, for four reasons:
    - (a) U(1)_Y is broken by the lemma: the flux uses up the hypercharge direction.
    - (b) Three is not forced: the moves allow −1, 1, 3, 5, and locality with SU(3)³ gives 5.
    - (c) There are no chiral leptons, and the coloured doublets are odd in number.
    - (d) The flux itself is not forced (step 4, open).
  - **Prior 90%.**

## What each outcome means

- **As predicted.** The ℤ₆ lead closes as an echo, not a derivation.
  - The qubit with a qutrit would give the Standard Model's non-abelian group exactly, with chiral quarks in the
    Standard Model's ratio.
  - But the flux that does it is the hypercharge's own 2π rotation, so it cannot coexist with U(1)_Y.
  - Its count is not three by any forced rule.
  - W27's statement (derived given one stated link), with W28's naturality condition, stays the record's best.
- **Z2 not 11.** The echo fails at the start. Record the centraliser.
- **Locality with SU(3)³ giving three.** That would reopen the lead at once, and step 4 (is the qutrit flux forced?)
  would come next.
- **Z5's commutant not 2.** Then the index sets change. Re-derive Z6 from the computed structure before anything is
  written.

## Seen before this was written

- **W24 and W25:** chi248, and the centraliser 55 of Q₈.
- **By hand:**
  - the branching and the ℤ₆ pairing argument;
  - the CRT factorisation;
  - the centraliser count 11 (the centre acts non-trivially on the 6, 15 and 20, and H₆ is irreducible);
  - the qutrit's 22 (SU(3) × G₂);
  - Λ²(2 ⊗ 3) = Λ²2 ⊗ S²3 + S²2 ⊗ Λ²3, and Λ³(2 ⊗ 3) = S³2 ⊗ Λ³3 + S_{21}2 ⊗ S_{21}3;
  - the existence of the lifts of L and R in SU(6) (u_{k+1}/u_k = λζ^{k+1}, whose product is 1);
  - the index formula;
  - the locality table: SU(3)³ = 3, −12, 15, 0.
- **Literature, as recalled:**
  - 't Hooft's twist-eaters;
  - Slansky's branching E₈ ⊃ SU(2) × SU(3) × SU(6);
  - −1 ∈ W(E₈), so every element of E₈ is conjugate to its inverse (stated, not used);
  - the Weil representation's even/odd split.
