# Card W-A3: the figure-eight's dihedral cover as the source of the module, the frame's level-5 class, and the up sector's level

**From:** the web seat (chat1). **Opened:** 2026-11-17, at the author's request, relaying main's card. Data-free. Main
will recompute. This card is committed before any of its computations is run.

## The questions (the author's card, in this seat's words)

**Part 1, the flux.** Main's hypothesis is that no flux is needed: the five are the sheets of the figure-eight's
dihedral cover, which exists only at p = 5; the meridian acts on them as the parity; the cusp has three preimages, of
degrees 1, 2 and 2.
- 1.1 Does the cover supply the whole module, with the shifts as deck transformations and the clocks as twists by the
  act's fixed line?
- 1.2 Which of the two level-5 classes does the frame carry? Main reads the knot's own form as x²/5, and B1951's ρ and
  W-A2's flux-5 modes as 2x²/5.
- 1.3 If the frame's class is not the knot's own, what in the object realises the other?

**Part 2, the up sector.** Main's B1953, as relayed: the down coupling is one covariant operator, and the up sector's
phases are 25th roots. Is there a three-body coupling, of two fields of degree 2 and the Higgs of degree 1, whose phases
close at level 5? If not, what level-25 structure does the up sector need?

B1953 is not on main's branch at the time of writing, so this seat works from the card's statement of it.

## What will be computed (one sealed script, `relays/chat1_2026-11-17_wa3/wa3_checks.py`)

- **A. Dihedral representations.**
  - π₁(m004) is taken as the mapping torus ⟨a, b, t | t a t⁻¹ = aba, t b t⁻¹ = ab⟩. Its monodromy induces
    LR = [[2, 1], [1, 1]] on H₁ of the fibre.
  - Every homomorphism onto D_p, for primes 3 ≤ p ≤ 31, with t sent to a reflection.
  - Plant: the monodromy a ↦ ababa, b ↦ ab, which induces [[3, 1], [2, 1]].
- **B. The cover and the module.**
  - At p = 5: the action on the five sheets; the fibre's character u.
  - Whether u is a multiple of ω(v, ·), with v = (1, 2) the act's fixed line (B1943).
  - The peripheral subgroup: the longitude [a, b], and a meridian g⁻¹t with φ([a, b]) = g[a, b]g⁻¹. Its image, and the
    cusp degrees (its orbits).
  - Deck groups, as centralisers in S₅: over m004, and over the double cover M₂, the kernel of t ↦ −1.
  - The clocks: whether the deck group's characters, pulled back to the fibre, are the twists ζ^(b·u).
  - Whether diag(ζ^(bx)) intertwines the sheets' representation with its twist on M₂.
  - Whether ⟨X, Z⟩ acts irreducibly.
  - How t acts on the (shift, clock) plane.
  - Whether the cover's t equals ρ_a(LR), up to a scalar, in either Weil class.
- **C. Homology of the covers.** Fox calculus in the permutation representation, then the Smith normal form, for:
  - m004 (expected Z);
  - M₂ (expected Z ⊕ Z/5);
  - the 5-sheeted dihedral cover;
  - the 10-sheeted regular dihedral cover.
- **D. The classes.** A class is the square class of c in T ↦ e(c x²/5), with e(x) = e^(2πix). T²'s coefficient is also
  reported, so that the comparison does not depend on which generator is used.
  - **(K) The knot's own form:** the discriminant form q(x) = xᵀA⁻¹x/2 of A = V + Vᵀ, with V = [[−1, 1], [0, 1]] the
    figure-eight's Seifert matrix; and the bilinear linking form b(x, x) = xᵀA⁻¹x.
  - **(B)** B1951's ρ(T) = diag(e(2x²/5)), from main's code.
  - **(F)** The flux-5 modes ψ_j, from the phase of ψ_j(τ + 2)/ψ_j(τ).
  - **(C) The frame's own level-5 phases.**
    - The phase of the product of the two theta numerators of each sector's pair, from this seat's transcription of
      frame C's `thc` (W-F22).
    - Taken at τ + 1 and at τ, at the same point w = aτ + b (the record's transport), on lines a = k/5, k = 1..4.
    - Sectors (Q, u), (Q, d) and (L, e), with 6Y = 1, −4, 2, −3 and 6.
  - **The shear class of the act's unipotent part.** LR ≡ −U mod 5; U is written in a symplectic basis (v, w) and its
    shear read off, and the same for U².
- **E. Part 2.**
  - The up pair's phases (their order).
  - Two models of a field of degree d:
    - M1: its theta at modulus 2dτ (frame convention), T-phase e(−dα²), checked numerically;
    - M2: its characteristic scaled to dα.
  - Every assignment of degrees in {1, 2}³ to (Q, u, H), and to (Q, d, H) and (L, e, H), with the Higgs's 6Y in
    {+3, −3, 0}: whether Σ d_i q_i² ≡ 0 mod 5 (M1), or Σ d_i² q_i² ≡ 0 (M2).
  - Main's assignment is (Q: 2, u: 2, H: 1).
- **F. Level 25 in the object.**
  - The roots of x² − 3x + 1 mod 25.
  - The cyclic subgroups of order 25 of (ℤ/25)² that LR keeps.
  - Homomorphisms onto D₂₅.
  - Any ℤ/25, or 5-rank ≥ 2, in the torsion of C's covers.

## Expectations

- **E-A.** Dihedral representations at p = 5 only; the plant gives p = 3 only.
- **E-B.**
  - u ∝ ω(v, ·).
  - The meridian acts as a reflection with one fixed point; the cusp degrees are (1, 2, 2).
  - The deck group over m004 is trivial; over M₂ it is C₅, acting as the shifts.
  - The deck characters on the fibre are ζ^(b·u).
  - ⟨X, Z⟩ is irreducible.
  - t acts as −I on the (shift, clock) plane, so the cover's t is the parity P and not ρ_a(LR), for either class: the
    act's chirp is not supplied.
- **E-C.** H₁(M₂) = Z ⊕ Z/5. The 5-sheeted cover is Z³ and torsion-free, since a 2-bridge knot's irregular dihedral
  branched cover is S³. No expectation for the 10-sheeted cover.
- **E-D.**
  - (K): q is in the residue class and b in the non-residue class.
  - (B) and (F) are in the non-residue class.
  - (C) down and lepton: phases e(−k²(q₁² + q₂²)/25), that is e(∓k²/5), in the residue class, the knot's own.
  - The act's shear is in the residue class, and U²'s in the non-residue class.
  - So the frame carries the knot's class, and B1951 and the flux carry the other, by a factor of 2.
- **E-E.**
  - The up pair's phases are primitive 25th roots.
  - Main's assignment (2, 2, 1) closes in neither model, for any Higgs charge.
  - Under M1, the only up assignment in {1, 2}³ that closes is (Q: 1, u: 1, H: 2), with H's 6Y = ±3. Under M2 none
    closes.
- **E-F.** No root mod 25; no invariant cyclic subgroup of order 25; no D₂₅.

## What would show each part has failed

- **Part 1.1 fails** (the cover does not supply the module) if any of these holds:
  - **F1** a dihedral representation exists at a prime other than 5, or none at 5;
  - **F2** the meridian does not act as a reflection with one fixed point, or the cusp degrees are not (1, 2, 2);
  - **F3** no cover of m004 or M₂ in the computation has the shifts as deck transformations;
  - **F4** the deck characters, restricted to the fibre, are not multiples of ω(v, ·);
  - **F5** ⟨X, Z⟩ is reducible.

  If F1–F5 all fail to hold but the cover's t is not ρ_a(LR) for either class, Part 1.1 is answered "the Heisenberg
  module and the parity, but not the act's Weil action", not "the whole module".
- **Part 1.2 is undecided** (**F6**) if the frame's down and lepton phases do not close at level 5, or if they fall in
  different classes.
- **Part 2's main assignment closes** (**F7**) if (Q: 2, u: 2, H: 1) satisfies the closure condition in M1 or M2, for
  some Higgs charge. That would answer the card's question "yes".
- **The model fails** (**F8**) if M1's T-phase e(−dα²) is not confirmed numerically to 1e-10. Part 2 under M1 is then
  void.
- **The harness fails** if the plant in A does not move the dihedral prime, or if H₁(m004) ≠ Z or H₁(M₂) ≠ Z ⊕ Z/5.

0 of 19.
