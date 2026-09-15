# B1361 — THE DECK'S TEXTURE IS B1273'S: the two C-field U(1)s born with the apexes allow exactly one E₆ cubic among the three 27s, the totally off-diagonal one, so with the Higgs in the apex 27s every tree-level charged-fermion mass matrix is complex symmetric with zero diagonal — B1273's texture from the flat classes, reached by a second route — and B1273's bound σ₁ ≤ σ₂ + σ₃ is in fact an identity, σ₁ = σ₂ + σ₃ (proved symbolically), refuted by the data in every charged sector; with a neutral Higgs there is no tree-level Yukawa at all; the diagonal source B1273 asked for is, in the design, the U(1)²-breaking sector

**Date:** 2026-09-15 · **Seat:** cc (the SM-derivation branch) · **Status:** NEGATIVE (structural, tree level) + PROVED (the selection rule by enumeration; the identity e₂(MM†) = (tr MM†/2)² for hollow symmetric 3 × 3 matrices, symbolic; the numerical saturation) · **Price: unchanged** · **Numbering:** B1361 (L213; the flavour face of the closing's design).

## 0. Seen from above

The three-apex design gives the three 27s charges (1, −2), (1, 1), (−2, 1) under the pair of U(1)s on which the deck acts as rotation
(B1356 §2). Those charge vectors form an equilateral triangle: no two are opposite and the three sum to zero. So the only cubic
27_i 27_j 27_k invariant under both U(1)s is 27₁ 27₂ 27₃ — exactly the coupling B1273 found on the flat Y₃ from its three twisted
classes (χ₁χ₂χ₃ = 1), and for exactly the same reason: three distinct characters whose only product-trivial triple is the mixed
one. B1273 drew the consequence — zero-diagonal complex symmetric mass matrices, σ₁ ≤ σ₂ + σ₃, refuted by the data — and named what
would lift it: a diagonal source that is not tree level. The apex route reproduces the texture verbatim and sharpens the bound to
an identity. In the design, the diagonal source has a name: the sector that breaks the apex U(1)s — Witten's axionic mass and the
instantons charged under them — which is also the only place the generations' distinction can be felt at low energies (L213 (i)).

## 1. The selection rule (computed)

| coupling | charges summed | invariant |
|---|---|---|
| 27₁ 27₂ 27₃ | (0, 0) | **yes** |
| every other symmetric λ_{ijk} (nine of ten) | ≠ 0 | no |
| 27_i 27_j H with a neutral Higgs | q_i + q_j ∈ {(2,−1), (−1,−1), (−1,2)} | **none** |
| the deck Z₃ alone (no U(1)s) | — | four invariant cubics (Σx_i³, the two cyclic mixed sums, x₁x₂x₃) |

With the Higgs doublets in the 10 ⊂ 27_i (B1273's placement) the mass matrices are M_{jk} = λ |ε_{ijk}| ⟨H_i⟩: complex symmetric,
zero diagonal, one entry per Higgs vev. With a neutral Higgs (a vector-like pair from the closing, B1302's kind) no tree-level Yukawa
survives the U(1)s at all. The deck alone would allow diagonal couplings; it is the U(1) pair — the very thing that tells the
generations apart — that forbids them.

## 2. The identity (proved)

For M = [[0, c, b], [c, 0, a], [b, a, 0]] with complex a, b, c and S = |a|² + |b|² + |c|²: tr(MM†) = 2S and the sum of the principal
2 × 2 minors of MM† equals S² (symbolic). Hence, with s_i = σ_i² the eigenvalues of MM†, e₁² − 4e₂ = (σ₁+σ₂+σ₃)(σ₁−σ₂−σ₃)(σ₁−σ₂+σ₃)(σ₁+σ₂−σ₃)
= 0; with σ₁ ≥ σ₂ ≥ σ₃ ≥ 0 the factors other than the second vanish only in degenerate cases that satisfy the second as well, so
**σ₁ = σ₂ + σ₃ for every hollow complex symmetric 3 × 3 matrix** (B1273's Takagi argument gave ≤; 10⁵ random matrices give
|σ₁ − σ₂ − σ₃|/σ₁ ≤ 10⁻¹⁵ and σ₂/σ₁ ≥ ½). The heaviest generation's mass is the sum of the other two, exactly, in each charged sector:

| sector | m₃/(m₂ + m₁), low scale (this arc) | at B1273's scale | the texture demands |
|---|---|---|---|
| up | 273 | 136 | 1 |
| down | 50 | 43 | 1 |
| charged leptons | 17 | 17 | 1 |

## 3. What it means

1. The closing's design carries B1273's negative unchanged: three generations distinguished by three distinct characters — flat
   classes on Y₃ or apex U(1) charges, the same combinatorics — have a hollow tree-level texture, and hollow means m₃ = m₂ + m₁.
2. The apex U(1)s are anomalous and acquire Witten's axionic mass; couplings violating them arise from the sector that breaks them
   (M2-instantons on three-cycles carrying the charges, the axion-dependent terms). That sector is the diagonal source — a
   Froggatt–Nielsen-like structure with the deck's charges (1, −2), (1, 1), (−2, 1) as the flavour charges, suppressions set by
   instanton actions. It is not computed here; it is where the design's flavour must come from (L213 (vii)).
3. The three faces: the selection rule is the A₂ charge lattice's arithmetic (the equilateral orbit, B1356); the texture is the
   geometry of three loci or apexes told apart only by a permuted label; the identity is linear algebra. The count stays 0 of 19,
   and the Yukawa items of the destination ledger are now told what their tree level cannot be.

## 4. Caveats

1. The Higgs placement (in the apex 27s, or neutral) covers the natural cases; a Higgs carrying a charge that pairs with one
   generation (q_H = −(q_i + q_j)) would allow one diagonal-free coupling per Higgs — still hollow.
2. The charges are B1356's coset representative; any triple in (1, 1, −2) + 3A₂ has the same equilateral property (no two opposite),
   so the selection rule is representative-independent.
3. The data are low-scale running masses here and GUT-scale in B1273; the verdict is scale-independent.

## 5. Registered

- **L213 (vii)** — the U(1)²-breaking sector as the diagonal source: the instanton three-cycles of the closing with the apex
  charges, their actions, and whether the deck's charges give a Froggatt–Nielsen hierarchy.

## Verification

`verification/decks_texture.py` (seconds; record `decks_texture_run.txt`): the enumeration of invariant couplings for the apex
charges and a neutral Higgs, the Z₃-invariant cubics, the symbolic identity e₂(MM†) = S², the numerical saturation, the data ratios.
Lock: `tests/test_b1361_the_decks_texture.py`.

**Sources.** B1273 §4 (the texture, the Takagi bound, the general remark on distinct characters); B1356 §2 (the charges); B1276
(the one cubic); Witten, hep-th/0108165 §3 (the anomalous U(1)s and their mass).

*(Currency 2026-09-15, B1362: §3.2's Froggatt–Nielsen hope quantified — a deck-symmetric Yukawa is a symmetric circulant with a
degenerate pair, and Weyl's inequality on the hollow tree level gives ‖E‖ ≥ (m₃ − m₂ − m₁)/3 for the U(1)²-violating part: a third of
the third-generation Yukawa, attained numerically. The breaking sector is a leading effect, not a correction.
`frontier/B1362_the_hierarchy_is_u1_breaking`.)*
