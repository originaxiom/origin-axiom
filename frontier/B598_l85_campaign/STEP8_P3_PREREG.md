# STEP 8 — THE SEALED P3 PREREGISTRATION (the D1 existence verdict)

**Sealed 2026-07-15, BEFORE any outcome-bearing comparison. SHA-256 of this
file recorded in `ARTIFACT_HASHES.txt` at sealing. No verdict cell below has
been computed anywhere (in-repo or in any seat's reported work) at sealing
time. Provenance: all verification internal (owner + AI seats).**

## The question (D1, narrowed by B597)

Does a choice-free, width-respecting semiclassical map exist from the golden
stage's θ-odd plane to the character variety's dial {u₄, u₈}? Outcome C
(free rotation) is already excluded conditional on existence + width-respect
(B597). This prereg decides **A / B vs D**.

## Frozen conventions

- Embedding: w = √−3 = +i·√3; ζ₅ = e^{2πi/5}; ζ₆ = (1+w)/2; ζ₁₄ = e^{πi/7}.
- Classical side: the committed l51 model verbatim; the bending directions
  v_m = BLOCKS[m][0] exactly as built (no rescaling); the frozen 20-word
  list; the J-pairing (step 5); the banked step-4b responses:
  c₄ = N₄·(1+w), c₈ = N₈·(1−w) on the universal word-pattern,
  N₄ = 2⁹·3²·5·7·13, N₈ = 2¹⁵·3⁵·5³·7²·11.
- Stage side: B593's golden-stage machinery verbatim; the θ-odd plane
  (u₃, u₆); the object's weld g = RL; banked amplitudes
  h₃ = 1/(2φ) + i·sin(2π/5)/√5, h₆ = conj(h₃).
- Width-respect (B597 constraint): the map is unique up to per-line scale;
  per-line magnitudes are therefore GAUGE. The verdict uses only
  gauge-invariant structure: conjugation-equivariance, orientation,
  level-stability, and rank production. **No value-matching claim is in
  scope for this prereg**; the cross-domain value question needs the
  normalization arc (P2_MAP slot 8), separately preregistered later.

## The declared bijection (the map candidate, structural level)

m=4 ↔ u₃ and m=8 ↔ u₆, declared by Im-sign orientation under the frozen
embedding: Im(c₄) = N₄√3 > 0 matches Im(h₃) = sin(2π/5)/√5 > 0; the
conjugate line pairs with the conjugate direction.

## Consistency cells (computed BEFORE this seal — recorded, NON-blind, no
outcome weight beyond necessary conditions, both already consistent)

- K1: both sides are 2-dimensional with canonical line-splittings and
  conjugate-pair structure (stage: B584/B593; classical: step 4b).
- K2 (the campaign's C2 cell): θ-even forced silence on both sides
  (classical: the forced zeros + the f₄ dial of step 7; stage: the hearing
  law's odd-only support).

## THE BLIND VERDICT CELLS (none computed at sealing; these bear the outcome)

- **V1 — mirror equivariance (the kill cell).** New classical computation:
  rerun the step-4b responses with the twist conjugator MIRRORED
  (v_m → mconj(v_m), i.e. c = exp(t·v̄_m)) at m = 4 and m = 8.
  REQUIRED for existence: the phase classes SWAP exactly — the mirrored
  m=4 response lies on the (1−w) class and the mirrored m=8 response on
  the (1+w) class (word-pattern preserved; the integers N_m may change;
  a zero response or a non-swapped phase FAILS).
  *Rationale: the map must intertwine the classical mirror with stage
  conjugation; this is its minimal necessary structure.*
- **V2 — level-independence (the campaign's C3 cell).** New stage
  computation: the hearing law at the NEXT golden multiple κ = 10
  (B587/B593 machinery, same weld g = RL). REQUIRED: (a) the θ-odd
  hearing spectrum again splits into a conjugate pair; (b) both
  amplitudes have Im ≠ 0; (c) the Im-sign orientation of the u₃-analog
  equals the κ = 5 orientation. Any of (a)/(b)/(c) failing FAILS the cell.
- **V3 — the E₆₂ rank production (the dimension caveat, B595-D1/B597).**
  New exact computation on the banked B594-H3 3×3 odd form (off-diagonals
  included): compute the complex-conjugation pairing structure of the
  three E₆₂ hearing channels under the frozen embedding. REQUIRED for
  full existence: the form splits conjugation-equivariantly into a
  RANK-2 conjugate-paired part + a rank-1 remainder (2↔2 restored by
  structure, the third channel separated by the width labels). No such
  splitting FAILS the cell.

## The locked outcome table

- **A** — V1 AND V2 AND V3 all pass: "the semiclassical map exists at the
  structural level: choice-free, width-respecting, mirror-equivariant,
  level-stable, and rank-producing at E₆₂." (Values stay unclaimed; the
  normalization arc remains gated and separately preregistered.)
- **B** — V1 passes, but V2 or V3 fails: "structure at golden κ = 5 only" —
  bank exactly which cell failed and its data; the map exists as a κ = 5
  structural correspondence with the recorded defect.
- **D** — V1 fails: no mirror-equivariant map; D1's existence question
  closes negative at the structural level. Bank the failing phase data.

No other comparison carries verdict weight. Anything else observed during
the V-runs goes to FINDINGS as exploratory. Downstream (translation, PDG,
JUNO, PC26 §9) stays GATED regardless of outcome, per the adopted D1
prereg and the repo firewall.

## Run order (after the chain is fully green, step 9 included)

V1 → V2 → V3, each banked blind (output committed before the next cell
runs); then the outcome statement, using only the table above.
