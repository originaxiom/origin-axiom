# B588 — the sector-exchange theorem: −1 migrates across the Weyl-group boundary

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; no SM
quantities. Preregistered; locks `tests/test_b588_sector_exchange.py`.
Resolves L81(a).**
Run: `python3 sector_exchange.py` (pyenv, ~1 min).

## The theorem (computational + structural)

B584 observed the level-rank pair SU(2)₃ ↔ SU(3)₂ realizing ONE number (−1/φ)
in OPPOSITE parity sectors. B588 proves the exchange at the parity-projector
level, in three locked steps:

**1. (D_A₁) — the rank-1 decomposition, exact.** On ℂ[ℤ_{2κ′}] (the A₁ finite
Weil rep):
> Z(W; SU(2)_k) = ½ [ t₊(κ′) − t₋(κ′) ], κ′ = k+2,
verified exactly against the banked su2 values for golden/silver/bronze at
every κ′ = 3..20. For the figure-eight: **t₊ ≡ 1 identically** (conductor
det(A−I) = −1, a unit) and **t₋ = √5 at 5|κ′**, oscillating as the Legendre
symbol (κ′/5) = ±1 otherwise — the same √5-family Gauss data as the A₂
reflections (B587).

**2. The membership fact (exact integer check).** −1 = w₀ ∈ W(A₁) — the parity
element IS the Weyl reflection, so its Gauss term sits INSIDE the plain Weyl
assembly, C_stage = −w₀ = +1 is trivial, and the stage has only the even
sector. −1 ∉ W(A₂) — no A₂ Weyl element is −I — so the parity-type terms sit
in the C-coset, which IS the θ-odd channel (B587's convention, sign(w₀) = −1).

**3. The ingredient identity at the level-rank point κ = κ′ = 5.**
> A₁ (all even): ½(t₊ − t₋) = ½(1 − √5) = −1/φ
> A₂ (all odd): (1/12)[(1+5) − 6√5] = −1/φ
The same two arithmetic ingredients — the unit identity term and the
√5-family Gauss sums — assemble to the same number on both stages.

**Conclusion: sector exchange = the migration of the element −1 across the
Weyl-group boundary under level-rank.** On the rank-1 stage −1 is a symmetry
of the alcove (so the parity arithmetic is "even" content); on the rank-2
stage −1 is charge conjugation (so the same arithmetic is "odd" content).
This is B242/B243's "level-rank = conjugation" seen at the parity-projector
level, as L81(a) asked.

## Reading (firewalled)

Whether the object's √5 voice counts as symmetric or chiral is not a property
of the voice — it is a property of whether the theater's symmetry group
contains the central mirror. The same Gauss sum is gauge on one stage and
chirality on the other. (Cf. the observer-coupling thesis: the sector label
lives in the coupling, not in the object.)

## Residuals

The per-term closed forms share B587's Wave-2 residual (reciprocity proof).
Nothing else opened.

## Anchors

B584 (the observation), B587 (the A₂ machinery + convention), B204/Jeffrey
(the SU(2) Gauss framework, known/cited), B242/B243 (level-rank =
conjugation), B238 (banked values), L81(a) (resolved).
