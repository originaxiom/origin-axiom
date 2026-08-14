# B900 — N7: the exact frame 1-cocycle — ALL SIX BLOCKS ARE ROOT-INDEXED; the cocycle is diagonal; B896's float perms were the twists

**Date:** 2026-08-05 · **Seat:** cc (banking) · **Status:** exact (factorization over K) + 35-digit index matching

## The question (N7, registered in masterplan v3)

B896's joint-alignment permutations were float best-fits with a puzzle: frame
1's singlet perm was a transposition and its octet perm a 3-cycle — opposite
signs, seemingly at odds with B888's order-18 fiber product (which forces
sign-EQUAL Galois pairs). What is the exact S₃ 1-cocycle on the six Π-blocks?

## Result 1 — all four label cubics have a root in K (exact)

The Π-blocks are labeled by charge pairs (c₈, c₁₆). The four label cubics
(vacuum and octet, at each charge) are irreducible over ℚ with squarefree
discriminant part 77 each, and **every one of them acquires a linear factor
over K = ℚ[ρ]/μ** — each has a root in K, so each generates K:

| cubic | polynomial | field |
|-------|-----------|-------|
| vacuum c₈ | 2197x³ − 22110326784x − 21334764552192 | ≅ K |
| octet c₈ | 2197x³ − 5527581696x + 2666845569024 | ≅ K |
| vacuum c₁₆ | 2197x³ − 6963104474726400x + 2923811689117777920000 | ≅ K |
| octet c₁₆ | 2197x³ − 1740776118681600x − 365476461139722240000 | ≅ K |

(All four lead with 2197 = 13³ — the μ-constant echo.) **Every Π-block —
vacuum and octet alike — is indexed by a root of μ** through an explicit
K-rational label. Note the scope split with B888: B888's ≇ K statement
concerns its weight-cubic pair at its normalization; the λ=0/λ→∞ *label*
cubics here are all K-rational — the charge labels see only K.

## Result 2 — the cocycle is DIAGONAL; the sorted-order twists explain B896

At 35 digits, matching each K-root's three embeddings against the sorted
roots of its cubic gives the four index maps (μ-root i, sorted → label-root,
sorted):

> vac8: **[0, 2, 1]** · oct8: **[2, 0, 1]** · vac16: [2, 1, 0] · oct16: **[0, 1, 2]** (identity)

The Galois σ acts on ALL six blocks by the SAME permutation of μ's roots —
**the exact 1-cocycle is the diagonal S₃ action** (stronger than the fiber
product's sign-equality). What B896's float fit saw were the TWISTS: in
sorted-numeric coordinates, the frame-1 alignment is exactly the pair
(vac8-twist, oct8-twist) = ((0,2,1), (2,0,1)) — **the float best-fit perms
equal the exact twist maps digit for digit** — and frame 2's alignment was
already diagonal. The "opposite signs" were never a Galois anomaly: they are
the relative signs of the two orbits' fixed coordinate twists, and the
apparent non-cyclicity of B896's representatives is fully accounted for.

## Consequences

- B896's harmonic split is exact-grade: its alignment coincided with the
  Galois-consistent one; the 0.99963 trivial fraction stands as computed.
- The banked vacuum_frame_map's shape is now derivable: the inter-orbit
  correlation is the twist composition vac8⁻¹∘oct8, a fixed 3-cycle-type
  map — frames and vacuum lines are offset by one step of the diagonal
  action, exactly the banked {0:2, 1:0, 2:1} pattern.

## Files

- `cocycle.py` → `results.json`
- Locks: `tests/test_b900_cocycle.py`

## Depends on

B866 (μ), B886 (the pencil factors), B888 (the resolvent/fiber product),
B889 (the blocks), B896 (the float alignment this explains).
