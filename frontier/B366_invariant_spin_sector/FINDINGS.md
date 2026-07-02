# B366 (first installment) — the invariant spin sector lives in the seam-bearing class

**Status: banked (frontier). The gate's skeleton, EXACT (two elementary lemmas + the identification); the
numerical S-mixing verification is pre-registered, not yet passed — the seam arc REMAINS ON PROBATION.
Campaign W2.2. Firewalled; nothing to `CLAIMS.md`.**

## The two lemmas (exact)

1. **The puncture lemma.** `SL(2,ℤ)` acting on the 2-torsion of the fiber torus fixes **only the origin**;
   the three nonzero half-periods form a single orbit (`SL(2,ℤ/2) ≅ S₃`). The puncture is the unique
   MCG-invariant point.
2. **The spin lemma.** Under the classical action on theta characteristics, the odd `[½,½]` is **fixed by
   both generators**; the three even characteristics form one orbit (`T` swaps `[0,0]↔[0,½]` fixing `[½,0]`;
   `S` swaps `[0,½]↔[½,0]` fixing `[0,0]`).

## The identification and the forcing-shaped corollary

With B364/B365: `T+ = triangular = [½,0]` (its T-multiplier verified in B364 — and indeed `T` fixes `[½,0]` ✓,
an independent consistency hit); `T− = triangular×(−1)ⁿ = [½,½]` (**the odd one**); `S+ = square = [0,0]`;
`S− = [0,½]`. Hence, exactly:

> **The seam-bearing (a=½, triangular/theta-lift) class contains the unique invariant spin sector `[½,½]`;
> the canonical (a=0) class contains none.**

Combined with lemma 1, the gate's argument has its shape: an MCG-equivariant quantization of the *punctured*
fiber (the unique invariant point) that selects a single spin sector can only select the invariant one — which
lives in the seam-bearing class. B365's vanishing signature (one distinguished half-period zero for the
triangular family; the parity-central label `j=8`) is the same structure seen from the divisor side.

## Pre-registered, not yet passed (the probation condition)

The classical action predicts the S-mixing pattern of the four families: **`T− → T−`, `S+ → S+`, `T+ ↔ S−`.**
Verifying this numerically requires the correctly-normalized theta S-transformation — **three quick ansatz
attempts failed for three different reasons** (a degenerate large-`c` strip that fit anything; a mis-derived
`j`-dependent prefactor; a growth-measurement that conflates prefactor and theta growth) and are recorded as
such. The clean derivation-first computation is the named next step; until it passes, the identification of
the families with the characteristics rests on the T-side multipliers + parity algebra + vanishing signatures
(three independent consistency hits, no S-side confirmation yet).

**Provenance.** B364 (the two polarizations), B365 (the vanishing signature; the doubling), the seam arc
B358–B363 (what this would force). Reproducer: `invariant_spin.py`; test:
`tests/test_b366_invariant_spin_sector.py`.
