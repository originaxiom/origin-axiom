# B2009 — Listening 24: the halving derived — twisting by the order-6 character pairs the small group's representations, and the stabiliser sees the trivial character and ρ's restriction equally often in all but six; the three of those six that the neutral sector sees are the constant, S₄'s sign and one 2-dimensional representation, the identity's three left-out modes

**Verdict: PROVED (the derivation by hand, disclosed; its condition verified exactly by GAP's character tables at mod 27, 81
and 243).** Main, 2026-11-26, in the author's /loop "continue the listening line". Data-free. Register row P-882. **0 of 19.**

## Seen first

- **B2002 and B2003:** p_neutral(2x) = 2^d (x² − 9) x S(x), up the 3-tower from mod 27.
- **B2004:** the whole is ⟨C⟩ * ⟨σ⟩. W is 6 Π₀P_σΠ₀ on the neutral sector and −3 Π_qP_σΠ_q on each charged sector.
- **B2005:** ρ factors through G_k exactly where the halving holds. The stabiliser is ⟨C⟩ at mod 27 and 81, and of order 9 at
  mod 243.
- **B2006:** G_k is S₄ with a 3-adic layer.
- **Swept:** `VERDICT topic-sweep /character table|Frobenius|induced representation|Ind_S|twist by the order-6/: 8 of 1750 arcs on main match (NEGATIVE 1, PROVED 7); 1 register rows match (QUEUED 1)`.
- **The literature (standard):** induced representations and Frobenius reciprocity. Twisting irreducibles by a linear
  character is a bijection on them. Character tables (GAP).

## The derivation (by hand before the card; disclosed)

G = G_k, O = G/S, Perm(O) = Ind_S^G 1 = ⊕ m_π π with m_π = ⟨π|_S, 1⟩.

1. **On each π,** W is 6 Q₀π(σ)Q₀ on C's neutral subspace and −3 Q_qπ(σ)Q_q on its charge-q subspaces (B2004).
2. **The twist.** With ρ a character of G, π ↦ π ⊗ ρ permutes the irreducibles. (π ⊗ ρ)(σ) = −π(σ), and π ⊗ ρ's C-neutral
   subspace is π's charge-2 subspace.
3. **The charge-2 sector.** W's spectrum there is ½ × (6 Q₀π′(σ)Q₀) over the irreducibles π′, weighted by
   m_{π′⊗ρ̄} = ⟨π′|_S, ψ⟩ with ψ = ρ|_S. The neutral sector weights the same blocks by ⟨π′|_S, 1⟩.
4. **The consequence.** The charged spectrum is exactly half the neutral one, except on the irreducibles where
   ⟨π|_S, 1⟩ ≠ ⟨π|_S, ψ⟩.

## The results (`verification/characters.py` through sage, `characters_run.txt`)

| level | \|G\| | \|S\| | irreducibles | with m ≠ m′ | of those, with a C-neutral subspace | Σ (m − m′) · (C-neutral dimension) |
|---|---|---|---|---|---|---|
| mod 27 | 216 | 3 | 19 | 6 | 3 | 3 |
| mod 81 | 1,944 | 3 | 85 | 6 | 3 | 3 |
| mod 243 | 52,488 | 9 | 399 | 6 | 3 | 3 |

At all three levels the six exceptions are the same:

| degree | m = ⟨χ\|S, 1⟩ | m′ = ⟨χ\|S, ψ⟩ | C-neutral dimension | which |
|---|---|---|---|---|
| 1 | 1 | 0 | 1 | the trivial character |
| 1 | 1 | 0 | 1 | ρ³, S₄'s sign pulled back |
| 1 | 0 | 1 | 0 | ρ |
| 1 | 0 | 1 | 0 | another linear character |
| 2 | 0 | 1 | 0 | a 2-dimensional representation |
| 2 | 1 | 0 | 1 | a 2-dimensional representation |

- **D1 holds:** m = m′ for every irreducible except six, at each level.
- **D2 holds:** exactly three exceptions have a non-zero C-neutral subspace:
  - the trivial character, which is the constant mode 6;
  - S₄'s sign, which is the alternation −6;
  - one 2-dimensional representation, which is the null mode.

  Their weighted count is 3, the identity's three left-out modes, and the number of points ω's exchange fixes.
- **The identity, now derived,** has been checked exactly at mod 27 and 81 and to 10⁻⁸ at mod 243 (B2002, B2003). It holds for
  the reason above.

## What the whole does, read in its own terms

- **The halving is a consequence of three facts about the whole at its prime:**
  - the whole acts on ω's orbit as a group on the cosets of a stabiliser;
  - the modular group's order-6 character passes through that group;
  - twisting by the character pairs every representation with another, and the stabiliser sees the two sides equally.
- **The only exceptions are six small representations,** the same at every level run. The three of them the neutral sector
  sees are the constant, the alternation, and one 2-dimensional representation, exactly the modes the halving leaves out.
- **The layer's growth changes none of this:** the exceptions do not move from mod 27 to mod 243.
- **No rate is read as physical, and nothing is compared with data.**

## What is open

- **A proof that the six exceptions are the same for every 3ᵏ, k ≥ 3.** They have degree at most 2 at every level run, so they
  presumably factor through the smallest quotient that carries ρ and S₄.
- **The two 2-dimensional exceptions:** identifying them, and showing that their neutral line carries the eigenvalue 0.

## Dated note (2026-11-26, B2011)

- The premise restated above from B2005 (ρ factors exactly where the halving holds) is not a law. At mod 135 ρ factors and
  the halving fails (B2011). This arc's derivation does not use the converse: its criterion is the stabiliser's, which is
  what decides.
