# B310 — The cascade realization question, exhausted: standard E₆ chain + the banked ω; πi/3 spacing refuted

**Status: banked (frontier). The decisive multi-seat cross-check, settled computationally; the cascade math is
exhausted in-sandbox. Nothing to `CLAIMS.md`.** Both web-Opus seats independently flagged the load-bearing
distinction (the parallel-derivation catch), and asked CC the deciding question: does the "verified-three-ways"
cascade verify the **subgroup chain** (standard) or the **deformation realization** on the figure-eight's character
variety (the genuinely-new claim)? Answer: the chain (standard); the realization-at-πi/3 is refuted.

## The split
- **(1) Generic.** The cascade is the centralizer of `exp((2πi/N)·h)` in E₆ (`h` = the principal element) — pure
  Borel–de Siebenthal / Slansky (1981) Lie theory, **with no figure-eight input**. The chain
  `E₆ → SU(6)×SU(2) → SU(3)³ → SU(2)³` is the **standard E₆ GUT chain**. (B305/B306 already tiered it generic; the
  seats' "verified three ways" verified the *chain*, not a figure-eight realization.)
- **(2) The "equally-spaced πi/3" claim is refuted.** The cascade `u`-values `u_N = 2πi/N` (N=2,3,4,5,6) have gaps (in
  units of `πi`) **`1/3, 1/6, 1/10, 1/15` — not equal.** Only the single `N=3 → N=6` gap is `πi/3`. Equal-πi/3 spacing
  is false arithmetic.
- **(3) The "spacing = cusp shape πi/3" conflation is refuted.** m004's cusp shape is **`2√3·i ≈ 3.46i`** (B290);
  `πi/3 ≈ 1.047i`; the tetrahedral *saddle* is `z = e^{iπ/3}` (a shape, not a `u`-spacing). The claim conflates the
  saddle `u`-value (`iπ/3`, where the `N=6` step breaks) with the cusp modulus (`2√3·i`) — different objects.
- **(4) The one genuine object connection is already banked.** The `N=3` trinification grading **eigenvalue is
  `ω = e^{2πi/3}`** = the figure-eight's Eisenstein Riley root (B285) in `ℚ(√−3)` — so the trinification *step* sits at
  the genuine geometric Eisenstein value (B305). But that is the *eigenvalue* `ω`, not a "deformation spacing," and it
  is one step, already in B305.

## The verdict
The cascade is the **standard E₆ GUT chain (generic)** + the **Eisenstein-ω connection at trinification (banked,
B305)**. The **πi/3 spacing / cusp-shape realization is refuted.** Whether the chain is realized as *physical gauge
dynamics* on `T[4₁;E₆]` (the DGG 3d-3d correspondence for type E₆) is the **CRUX** — specialist-gated (no exceptional
state integral in-sandbox). **The cascade math is exhausted: no new object-specific content beyond the already-banked
`ω`; the remaining question is the CRUX.**

## The insight (the honest one)
This is the "exhaust the math before the specialist" result the owner asked for, and the insight is sobering and
clean: the **cascade — the thing all three seats got excited about as "the new result" — is the standard E₆ GUT chain**
(known since Slansky 1981). The only object-specific content in it is the Eisenstein `ω` at the trinification step,
which is B305 (banked). The "deformation realization at πi/3 spacing" that would have made it *new* is **not verified
and is partly refutable.** So the cascade arc does not add new object-specific physics — it confirms, once more, the
structural theorem: the object forces the *symmetry/structure* (E₆ and its standard breaking, the `ω`); the
*realization as physical dynamics* is the CRUX (specialist). The multi-seat excitement-deflation cycle, caught by the
parallel derivation, lands exactly where the discipline predicted.

## What this leaves
The cascade is **closed in-sandbox.** The genuine remaining gate is the **CRUX** (`T[4₁;E₆]` DGG realization) — now
cleanly isolated as the single specialist question, not buried under a "new cascade" that was standard all along.
The accurate open frontier (from B309) — Face IV (the TQFT quantization) ↔ the SM content — is the other in-sandbox
direction; the cascade is not it.

## Refinement (B311, 2026-06-30)
Chat-2 proposed the last in-sandbox step this verdict skipped: are the cascade grading points actual *special points* on
the figure-eight's A-polynomial? **B311 ran it and refines this card.** The points `M=i` (N=2) and `M=e^{iπ/3}` (N=3)
*are* branch points of the figure-eight A-poly discriminant `(x−1)²(x+1)²(x²−3x+1)(x²+x+1)`, `x=M²` (the two arithmetic
ends — Eisenstein `x²+x+1`, golden `x²−3x+1` — in one discriminant). So "no new object-specific content" was slightly
too strong: the **trinification (N=3)** sits at a genuine *irreducible* branch point (`L=−1`), upgrading B305 from
arithmetic-eigenvalue to character-variety relevance. **But the realization still does not close:** N=2 (M=i) is
*reducible* (`L=1`, abelian) and N≥4 are not branch points at all — the points are isolated, the first reducible, so the
chain is not realized as a connected breaking. The object-specific core remains the **one trinification step**; the full
physical realization remains the CRUX. See `B311`.

## The fence
Pure arithmetic (the spacing refutation) + the generic/object split + the tie to the banked `ω` (B305). The "physical
gauge dynamics" reading is the CRUX, firewalled. Nothing to `CLAIMS.md`.

`cascade_realization_exhausted.py` (pyenv) · `tests/test_b310_cascade_realization_exhausted.py`. Related: `B305`/`B306`
(the cascade — generic, the ω connection), `B290` (the cusp shape `2√3·i`), `B285` (the Eisenstein `ω` Riley root),
`B281` (the CRUX), `B309` (the κ-unification; the Face IV ↔ content frontier). Lit: Slansky (1981, the E₆ GUT chain);
Dimofte–Gaiotto–Gukov (the 3d-3d / `T[4₁;E₆]` — the specialist gate).
