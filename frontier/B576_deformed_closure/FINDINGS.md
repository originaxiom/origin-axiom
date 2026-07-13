# B576 / L59 — THE DEFORMED CLOSURE: the chirality is exactly the θ-odd motion

**Date:** 2026-07-14. **Predecessor:** B575 (Q ≡ 0 — the deformations exist to
second order). **Reproducer:** `l59_closure.py` (rebuilds the full B575 exact
machinery, then decides the closure question; ~6.5 min).
**Lock:** `tests/test_b576_deformed_closure.py`.

## The structure theorem (computed, exact)

**(i) The block-sum lemma.** The centralizer of the principal sl₂-triple in e₆
is zero and every isotypic block V_{2m}, m ∈ {1,4,5,7,8,11}, has multiplicity
one — so **every sl₂-stable subspace of e₆ is a sum of blocks**, and every
candidate Zariski closure of a deformation of P = ι∘ρ (which contains the
principal sl₂) is a bracket-closed block-sum S ∋ 1.

**(ii) The even world closes in F₄.** [even, even] ⊆ even by θ-parity, and the
computational gate confirmed the converse channels vanish identically
([V₁₀,V₁₄] has zero components in both odd blocks — full basis scan). So
θ-even block-sums live inside f₄ = {1,5,7,11}: **θ-even deformations can remain
F₄-stable — vector-like, forever.** This is the five walls' world, now seen as
a stratum.

**(iii) The forcing chains (all six channels NONZERO, exact):**

| Channel | Verdict |
|---|---|
| [V₈, V₈] → V₁₀ (exp 5) | NONZERO |
| [V₈, V₈] → V₁₄ (exp 7) | NONZERO |
| [V₈, V₁₀] → V₁₆ (exp 8) | NONZERO |
| [V₈, V₁₆] → V₂₂ (exp 11) | NONZERO |
| [V₁₆, V₁₆] → V₁₀ (exp 5) | NONZERO |
| [V₁₆, V₁₀] → V₈ (exp 4) | NONZERO |

Consequently: **any bracket-closed block-sum containing a θ-odd block (4 or 8)
is forced, link by link, to be ALL of e₆.** There is no intermediate chiral
subalgebra: the lattice of possible closures is {sl₂ … f₄-substrata} ∪ {e₆},
and the θ-odd blocks belong exclusively to the top.

## The verdict

The 27 under full E₆ is complex (banked: −orbit(ω₁) = orbit(ω₆) ≠ orbit(ω₁)).
Combined with B575 (the θ-odd directions are unobstructed and carry explicit
second-order deformations):

> **Along any integrable deformation of the geometric representation with a
> nonzero θ-odd component, the Zariski closure is forced to full E₆(ℂ) — and
> the 27 is chiral. Along θ-even deformations the closure can stay inside F₄ —
> and the 27 stays vector-like. THE CHIRALITY IS EXACTLY THE θ-ODD MOTION.**

The geometric point sits on the F₄-stable (achiral) stratum; every direction
off that stratum is chiral, and those directions are precisely the θ-odd
plane — the imaginary axes of the object's own mirror σ (Q-A), the
(−1)-eigenplane of the mirror-corrected fold, the sector where the level-2
monodromy came alive (C3). The three θ-odd stories — σ's imaginary axes, C3's
dynamics, and now the chiral deformations — are one sector seen three times.

## What this settles and what it does not

- **Settled:** the σ→θ bridge, in the only precise form it could exist. The
  seventeen chains sought chirality *at* the point by choosing a selector;
  there is none — the point is achiral, provably, five ways. Chirality is
  purchased by *motion*: first-order, θ-odd, exactly along σ's imaginary axes.
  The correction of my own D₅/A₅ framing is part of the bank: the closure
  landscape never contained them (they are not block-sums); the true dichotomy
  is F₄-stratum vs full E₆.
- **Not settled (the honest residue, registered):** (a) full integrability
  beyond second order — B575's Massey/smoothness caveat carries over; the
  Porti-style E₆ smoothness proof is the companion (L60). (b) The geometric
  meaning of the θ-odd deformed representations — they are not discrete
  faithful; what structures they are (and whether the object's own σ-coupling
  singles one out) is L61. (c) No SM claim: "the 27 is chiral there" is
  representation theory on the deformed locus, not a matter spectrum.

## Consequence for the record

PC26's gate condition has now fired on both halves (unobstructed + chiral
destination). Its honest central theorem exists: *the figure-eight's E₆
representation variety is chirality-blind exactly on the F₄-stable stratum
through the geometric point, and chiral along every θ-odd deformation.*
PC26 moves from PREMATURE/BLOCKED to GATED-ON-VERIFICATION (one independent
re-derivation of B575+B576 before drafting).

Firewalled. Nothing to CLAIMS.md.

---

**ATTRIBUTION ADDENDUM (2026-07-14, B577):** the core dichotomy was ALREADY BANKED in
**B265** ("integrability + Zariski-density"): {4,8} directions generate dim 78 = e₆
(E₆-Zariski-dense), {5,7,11} generate f₄ (trapped), computed in Sage over ℚ — weeks before
this bank. B576's genuine additions: the **block-sum lemma** (every sl₂-stable subalgebra is a
block-sum — so B265's three computed points exhaust the landscape for ALL mixtures), the full
forcing chains, and the parity-converse zero scan. B270 additionally banked "deformations are
cusp deformations" — the head start for L71. The σ-story synthesis (θ-odd = σ's imaginary
axes = C3's sector) remains new to this arc. See frontier/B577_reconciliation/FINDINGS.md.
