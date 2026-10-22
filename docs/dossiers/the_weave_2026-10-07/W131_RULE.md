# W131 — the forced field and the chiral three: does W130's field give the three families masses? Its couplings to the fibre's zero modes, by type, parity and residue (the rule, committed before the script)

The SM-derivation seat, 2026-10-22. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **W130 found the one field GENESIS PF1 forbids from resting at zero:** the fibre's uniformizing Higgs field Φ, of
  size ½.
- **W130 left the link to masses open:** does Φ couple the chiral three? The owner asked this seat to finish what it
  named, without waiting on the other seats (2026-10-22). Main's ask in relay §217 (a) is taken here.

## The objects

- **The chiral three (W21, W22).**
  - One zero mode per parity block p = 1, 2, 3: a holomorphic section of S⁺ ⊗ ρ_Q ⊗ χ_p with the half-integer
    exponent the puncture's −1 allows (Λ₊ = ℂ²). There is no zero mode of chirality −.
  - Each block sees one of the three even spin structures (W22).
  - The scalar part of its zero mode is that spin structure's Szegő kernel,
    S_k(z) = θ_k(z)θ₁′(0)/(θ_k(0)θ₁(z)) for k = 2, 3, 4 (B1651's Szegő reading).
- **The forced field (W130).**
  - Φ ∈ H⁰(End E ⊗ K), with E = S = K^{1/2} ⊕ K^{−1/2} the spinor bundle and Φ = c·N, |c| = ½.
  - Its conjugate is Φ*, and its square root is h, a section of E ⊗ K^{1/2} = K ⊕ O.
- **A coupling of two zero modes ψ_a, ψ_b through X** (X = Φ, Φ* or h) is the invariant pairing of the three, with ε
  on ρ_Q, the spinor pairing, and the parity characters. It is either integrated over the fibre, which needs a
  (1, 1)-form, or read as its residue at the puncture, a point coupling.

## Weave or thread

**WEAVE-type.** The shared fibre at every τ, with all three parity blocks, the forced field and the coupling to all
three at once.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| J0 | the instrument (mpmath, 40 digits, at three τ): each S_k has a simple pole at 0 with residue 1 and is odd; S_k² − S_l² is constant in z; under z → z + π and z → z + πτ the signs of S₂, S₃, S₄ are (+, −), (−, −), (−, +), the three non-trivial characters of H₁ | 95% |
| J1 | type (exact): N maps S⁺ to S⁻, and Nᵀ annihilates S⁺. So Φ*ψ = 0 for every zero mode, while ⟨ψ_a, Φψ_b⟩ and ψ_a·ε(h, ψ_b) are (1, 0)-forms. No bulk integral exists, and a coupling is at most a residue at the puncture | 97% |
| J2 | parity (exact and checked): Φ, Φ* and h are blind to the parity characters (End(E ⊗ χ) = End E, and h is the canonical section of the trivial summand), so an invariant coupling pairs equal parities only. For a ≠ b, S_a·S_b carries the third parity's character (its signs under the two periods are S_c's) | 95% |
| J3 | the residue (exact and checked): for a = b the coupling is c·S_a(z)² dz (and the same through h), a single-valued meromorphic 1-form on the closed torus whose only pole is the puncture. Its residue is 0, by oddness and by the residue theorem. The contour integral of S_a², and of S_aS_b for a ≠ b, around the puncture vanishes to 10⁻³⁰. So the coupling matrix is Y ≡ 0, through Φ, Φ* and h, at every τ | 95% |
| J4 | the read-out: the matrix Y (all zero); and a READING by hand on what can couple. The index ±3 is topological, so no internal background lifts the three. A non-zero coupling needs a datum that carries parity and is of type (0, 1) at the puncture (B1651's addendum, B1654: one framed datum per parity), which the principle does not force | — |

## What the outcomes mean (fixed now)

- **J0 to J3 hold.** Then the field the principle forces is silent toward the chiral three on the fibre.
  - Its conjugate annihilates them, it couples nothing in the bulk, and its residue coupling vanishes. It is
    parity-blind, so it cannot pair different families either.
  - So W130's field cannot by itself supply the non-zero masses W128 needed. It is the shape's field, not the
    mass-giver, as W129 read.
  - The masses need a parity-carrying datum at the puncture, which is not forced, and a four-dimensional field that
    breaks the weak symmetry (W128).
- **J3 fails** (a non-zero residue). Then the forced field couples, and the coupling's rank and pattern are recorded:
  that would be the link to masses. Nothing is read beyond what is computed.
- **J0 or J2 fails.** The Szegő reading or the parity assignment is wrong. It is recorded, and J3 is read only after
  that is resolved post hoc.

## What stays out

- Couplings of a non-forced Higgs (B1651, B1653, B1654, B1716). The four-dimensional Higgs and its potential.
- The full ρ_Q doublet structure of the zero modes beyond its ε-contraction. That contraction is invariant because
  ρ_Q ⊂ SU(2), so it does not change J3's argument.

## Seen before the rule (disclosed)

- **Read:** main's B1651 (and its audit B1655), B1653, B1654 and B1716; W21, W22, W130.
- **By hand:**
  - the Szegő kernels' oddness, residues and period signs (from the theta functions' standard transformation laws,
    Whittaker–Watson §21);
  - J1's types;
  - J3's residue argument.
- **Not run:** nothing has been computed.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
