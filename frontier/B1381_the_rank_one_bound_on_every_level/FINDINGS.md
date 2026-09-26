# B1381 — THE RANK-ONE BOUND ON EVERY LEVEL: no cyclic cover Mₙ of m004 has a rank-one character with h¹ = 2, for any n — the Fox Jacobian's t-column forces a character that kills it to be trivial on the fibre, and there the remaining block is s·I − Mⁿ, never zero because Mⁿ is never scalar; so main's B1427 observation (h¹ = 2 nowhere, n ≤ 7) is a theorem for all n, and B1377's bound |I| ≤ 2 in one doublet sector holds on every level of the cusped tower

**Date:** 2026-09-26 · **Seat:** cc (the SM-derivation branch) · **Occasion:** the harvest of main's B1427 (2026-09-18), which
solved the rank-one cohomology exactly to level seven and named the mechanism — "with 3 generators and 2 relators h¹ = 2 requires
the Fox Jacobian to vanish, which happens nowhere on it" — without a proof for every level (OPEN_LEADS sL-2 (i′)) ·
**Status:** PROVED (a five-line proof; symbolic checks to n = 8, the Fibonacci form to n = 40; an instrument control that fires) ·
**Fence:** mathematics about twisted cohomology of the cusped covers; B1374–B1378's fence unchanged (non-semisimple backgrounds, no
physics reading, no three) · **Price: unchanged, 0 of 19** · **Numbering:** B1381.

## 0. The statement

**Theorem.** Let Mₙ be the n-fold cyclic cover of m004 (n ≥ 1), and χ: π₁(Mₙ) → ℂ* any character. Then h¹(π₁(Mₙ); ℂ_χ) ≤ 1,
with equality at χ = 1 (b₁ = 1).

**Corollary.** B1377's extension bound — a firing doublet sector V is an extension of two rank-one modules, so
|I(V)| ≤ a₁(χψ) + a₁(χ⁻¹ψ) — gives **|I| ≤ 2 in one doublet sector on every level Mₙ**, not only on the levels whose character
groups were enumerated (B1377: M₂–M₆, on the torsion) or solved (main's B1427: n ≤ 7, exactly). Three generations in one doublet
sector of one background are impossible on the whole cusped tower. What remains empirical is the sharper |I| = 1 (the firing
signature (0,1,1,0)/(0,2,1,2), every level computed so far).

## 1. Proof

π₁(Mₙ) = ⟨a, b, t | t a t⁻¹ = φⁿ(a), t b t⁻¹ = φⁿ(b)⟩, the mapping torus of φⁿ where φ is m004's monodromy on the fibre group
F(a, b) (the n-fold cyclic cover unwraps the circle direction). Three generators, two relators; for χ ≠ 1,
h¹ = dim Z¹ − dim B¹ = (3 − rank J) − 1 = 2 − rank J, where J is the 2 × 3 Fox Jacobian evaluated under χ. So h¹ = 2 iff J = 0.

- **The t-column.** ∂(t g t⁻¹ w_g⁻¹)/∂t = 1 − t g t⁻¹, which χ sends to 1 − χ(g) (g = a, b; w_g = φⁿ(g) has no t). J = 0 forces
  χ(a) = χ(b) = 1: χ is trivial on the fibre.
- **The fibre block there.** With χ trivial on a, b and χ(t) = s, ∂(t g t⁻¹ w_g⁻¹)/∂h = s·[g = h] − (∂w_g/∂h)^χ, and the Fox
  derivative at the trivial character is the exponent sum: the block is s·I − (Mⁿ)ᵀ, M = φ's action on H₁ of the fibre.
- **Never zero.** s·I = (Mⁿ)ᵀ would make Mⁿ scalar; but M = [[2,1],[1,1]] has distinct eigenvalues φ², φ⁻², so Mⁿ has distinct
  eigenvalues φ^(±2n) and is never scalar (explicitly, Mⁿ = [[F(2n+1), F(2n)], [F(2n), F(2n−1)]] with F(2n) ≠ 0). ∎

The argument is basis-free (any presentation of π₁(Mₙ) gives the same h¹; any conjugate of M is non-scalar) and uses nothing
about m004 beyond "its monodromy's action on H₁ has no scalar power" — true of every pseudo-Anosov monodromy of the once-punctured
torus, so the theorem holds for the cyclic covers of every once-punctured-torus bundle with hyperbolic monodromy.

## 2. Computed (`verification/rank_one_bound.py`; record `verification/rank_one_bound_run.txt`)

| | item | result |
|---|---|---|
| S1 | the Fox Jacobian of Mₙ in (x, y, s) = (χ(a), χ(b), χ(t)), own Fox calculus, n = 1…8 (words up to 4 181 letters) | t-column exactly (1 − x, 1 − y); at x = y = 1 the block is exactly s·I − (Mⁿ)ᵀ, with the exponent-sum matrix = Mⁿ |
| S2 | Mⁿ, n = 1…40 | [[F(2n+1), F(2n)], [F(2n), F(2n−1)]], off-diagonal nonzero; eigenvalues of M 0.381966, 2.618034 |
| S3 | **instrument control that must fire**: the hyperelliptic involution a ↦ a⁻¹, b ↦ b⁻¹ (abelianization −I) | J = [[s + x, 0, 1 − x], [0, s + y, 1 − y]] vanishes at the non-trivial χ = (1, 1, −1): **h¹ = 2** — the criterion can fire, and does where the monodromy has a scalar power; m004's monodromy at the same character has rank 2 |
| S4 | h¹ by direct rank at sample characters, n = 1…6 | 1 at χ = 1; 0 or 1 elsewhere; **1 at the golden loci s = φ^(±2n), x = y = 1** — main's B1427 "two loci per level the μ_N scan cannot reach" ((3+√5)/2)^(±4) on M₄), reproduced here independently |

## 3. What this closes, and what it does not

- **Closes** sL-2 (i′) for the rank-one part: the bound B1377 proved on M₂–M₆ (torsion characters) and main's B1427 extended to
  n ≤ 7 (all characters) holds for every n.
- **Does not prove** |I| = 1 on every level (that needs the firing signature, still empirical beyond level seven), nor anything
  about the closed tower Yₙ (B1379/E72: these backgrounds do not descend), nor any physics: the fence of B1374–B1378 is unchanged.

## Verification

`verification/rank_one_bound.py` (S1–S4; the full run about four minutes, dominated by S4's symbolic ranks). Lock:
`tests/test_b1381_the_rank_one_bound_on_every_level.py` (the t-column and the fibre block to n = 4, the Fibonacci form to n = 40,
the control, the golden loci to n = 3).

**Sources.** Main's B1427 (2026-09-18; the level-seven computation and the named mechanism); this branch's B1377 (the extension
bound), B1375 (the census), B1379 (Mₙ against Yₙ), B1380 (σ² as m004's monodromy on F₂); Fox (1953), free differential calculus.
