# W61 — the rule, recorded before the code

The SM-derivation seat, 2026-10-13. Committed before the code that reads it exists. The predictions below were worked
by hand before this was written, as disclosed. Nothing here is a result.

## Why this arc

- **The owner chose "W61: the couplings"** (2026-10-13) after W60.
- **What W60 found.** W60's labelled post hoc found that the full one-loop potential puts the hypercharge line on a
  half-period, w = (½, ½) for instance. There one parity copy of the Higgs has a trivial local system, so it has a
  normalizable massless mode on the fibre. That is the Higgs C0 lacked.
- **This arc computes the Yukawa couplings at that state** (τ = ω, w a half-period, the Higgs copy p* = 3w) as
  overlaps of the zero modes.

## Weave or thread?

- **Weave-type.** The zero modes are the weave's T (W21, W49) on the shared fibre, all generations at once.
- **The tags.** Given Λ (GENESIS FK11), at the state W60 selected. The reading of the mass term is stated for each
  cell: T ⊗ T (W39, the record's) or T̄ ⊗ T (B1615's). Main has not ruled between them (relay §68).

## The objects

- **The zero modes.** In each parity block c the holomorphic zero mode is C_c F (W21's second route, W49):
  - F = (f(z), f(z + τ)) dz, with f = θ₃(z | 2τ)/√θ₁(z | τ);
  - C_c is the quaternion unit that carries ρ_Q to χ_c ⊗ ρ_Q: j, i and ij for (½, 0), (0, ½) and (½, ½), and 1 for
    the trivial block 0.
  - The antiholomorphic modes of T̄ are their conjugate partners (W49, E2).
- **The fields.** A field of charge q (in units of 6Y) and generation r sits in block r + q w (mod the lattice), since
  at a half-period L_{qw} is the parity character q w.
  - So at w = (½, ½): Q and L (odd q) of generation r sit in block r + (½, ½); u^c, d^c and e^c (even q) sit in
    block r.
- **The Higgs.**
  - In the copy p* = 3w it has a trivial local system. Its massless mode is constant: dz̄ as a (0, 1)-form for T ⊗ T,
    or the constant function for T̄ ⊗ T.
  - Its direction in the common point's adjoint is C_{p*}.
- **The coupling of blocks c₁ and c₂.**
  - T ⊗ T: ∫ (C_{c₁} f⃗)ᵀ J C_{p*} (C_{c₂} f⃗) d²z.
  - T̄ ⊗ T: ∫ (C_{c₁} f⃗)† C_{p*} (C_{c₂} f⃗) d²z.
  - Here f⃗ = (f(z), f(z + τ)) and J is the common point's ε.
  - The integrand is single-valued on the fibre exactly when χ_{c₁} χ_{c₂} χ_{p*} = 1, that is c₁ + c₂ = p*.
    Otherwise the coupling is 0 by the group.

## Worked by hand before the rule (disclosed)

- **When c₁ + c₂ = p*, the matrix C_{c₁}⁻¹ C_{p*} C_{c₂} is ±1.** Three distinct units multiply to ±1, a unit squares
  to −1, and a unit times its inverse is 1.
  - So the T ⊗ T integrand is ±f⃗ᵀ J f⃗ = ±(f(z) f(z + τ) − f(z + τ) f(z)) = 0 pointwise.
  - The T̄ ⊗ T integrand is ±|f⃗|², whose integral is half W41's norm N(ω).
- **So each sector's 3 × 3 Yukawa matrix is predicted:**
  - T ⊗ T: zero;
  - T̄ ⊗ T: a signed permutation times N(ω)/2. Each generation r of the first field pairs with exactly one generation
    of the second.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **Q1, the algebra** | Over all c₁, c₂ ∈ {0, (½, 0), (0, ½), (½, ½)} and p* ∈ the three parities, using the record's C_c matrices (W21's second route): C_{c₁}⁻¹ C_{p*} C_{c₂} = ±1 whenever c₁ + c₂ = p*, and the bilinear (1, 1)-form's equivariance fails otherwise. | 98% |
| **Q2, the sectors at w = (½, ½)** | With the generation-to-block maps above and p* = (½, ½), for up (Q u^c H), down (Q d^c H̃) and lepton (L e^c H̃): the T ⊗ T Yukawa matrices are 0. The T̄ ⊗ T ones are signed permutations times one number, so three equal singular values. Down and lepton are identical. The same holds at w = (½, 0) and (0, ½), with p* = 3w. | 95% |
| **Q3, the numbers at ω** | F's equivariance under a and b holds at τ = ω (the record's check, now at ω). At 50 sample points the T ⊗ T integrand is 0 to 10⁻¹² of \|f⃗\|². N(ω) is finite and agrees with W41's routine. | 95% |

## The reading, written before the run (predicted)

- **At the state the potential selects, the zero modes get no tree-level hierarchy.**
  - In the record's T ⊗ T reading the selected Higgs does not couple to them at all. The three alike share one
    wavefunction (W49), and a Higgs whose local system is trivial can only contract them through ε (C0, point 2).
  - In the T̄ ⊗ T reading it couples them with three equal strengths: degenerate masses, a permutation for mixing, and
    d and e identical.
- **So the hierarchy needs the multiplicity broken.** One source would be a flavour line acting on M (C0, point 4;
  allowed, not forced). Another would be a departure from the selected state (τ ≠ ω, or no half-period line). Neither
  is selected by anything computed so far.
- **The count stays all 19 of the 19 free** (18 if I-18 is earned). 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.
