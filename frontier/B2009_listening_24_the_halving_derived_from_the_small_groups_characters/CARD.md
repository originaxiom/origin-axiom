# B2009 — Listening card 24: the halving derived from the small group's characters — twisting by the order-6 character turns it into a multiplicity condition, decided by GAP's character tables

Written 2026-11-26, before any run, in the author's /loop "continue the listening line". Data-free. 0 of 19.

## The derivation, by hand before this card (disclosed)

Let G = G_k be the whole's group on ω's orbit O = G/S (B2005), with S the stabiliser of (3,3,3), and ρ the order-6 character
(ρ(C) = ω, ρ(σ) = −1). ρ factors through G for k ≥ 3 (B2005). Let ψ = ρ restricted to S.

1. **The permutation representation:** Perm(O) = Ind_S^G 1 = ⊕_π m_π π, with m_π = ⟨π|_S, 1⟩.
2. **The sector forms (B2004):** W is 6 Q₀π(σ)Q₀ on C's neutral subspace of each π, and −3 Q_qπ(σ)Q_q on its charge-q
   subspaces.
3. **The twist:** π ↦ π ⊗ ρ is a bijection on irreducibles. (π ⊗ ρ)(σ) = −π(σ), and π ⊗ ρ's C-neutral subspace is π's charge-2
   subspace. Hence:
   - the spectrum of W on Perm's charge-2 sector is −3 times the spectrum of Q₀π′(σ)Q₀ over π′, but each π′ is weighted by
     m_{π′⊗ρ̄} = ⟨π′|_S, ψ⟩;
   - the neutral sector weights the same blocks by m_{π′} = ⟨π′|_S, 1⟩.
   - So, with step 2, **the charged spectrum is half the neutral one wherever ⟨π|_S, 1⟩ = ⟨π|_S, ψ⟩.**
4. **The three left-out modes** (6, −6, 0) must come from the irreducibles where the two multiplicities differ.
5. **Where ρ does not factor through G** (mod 9, the leaves mod p), the twist in step 3 does not exist.

## The checks (GAP through sage)

At mod 27, 81 and 243, for every irreducible character χ of G_k:
- its degree;
- m = ⟨χ|_S, 1⟩ and m′ = ⟨χ|_S, ψ⟩;
- the dimension of C's neutral subspace.

The irreducibles with m ≠ m′ are listed. ρ is identified among G_k's linear characters by ρ(C) = ω and ρ(σ) = −1.

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| D1 | at mod 27, 81 and 243, m = m′ for every irreducible except a few | 0.75 |
| D2 | the exceptions with a non-zero C-neutral subspace are exactly: the trivial character (giving the constant, 6), S₄'s sign pulled back (the alternation, −6), and one more irreducible (the null mode) | 0.45 |

## What it means

- **If D1 and D2 hold:** the halving is derived, not only observed. At the whole's prime, ω's orbit is a coset space of a group
  through which the order-6 character passes. Twisting by it pairs each representation with another, and the stabiliser sees
  the trivial character and ψ equally often, except at the modes the identity leaves out.
- **Nothing is compared with data.**
