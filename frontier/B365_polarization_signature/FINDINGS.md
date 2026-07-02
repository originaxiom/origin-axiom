# B365 — the S-side: closure fails for BOTH (the metaplectic doubling), but the vanishing signature discriminates

**Status: banked (frontier). Numerical tier (theta q-series at 1e-10–1e-21 floors); one pre-registered
prediction REFUTED by its own test — recorded as the finding. Campaign W2.1. Firewalled; nothing to
`CLAIMS.md`.**

## The refutation (my own prediction)

Predicted: the triangular family is S-closed on its own 15-dim span, the square is not. **Both closure fits
fail** (residuals ≈ 0.63 over all prefactor/shift candidates). The corrected Poisson algebra explains it: the
half-shift in the dual sum produces a `(−1)^m` sign twist — **at odd level, the S-transform forces the
level-30 sign-doubling for BOTH polarizations** (the classical metaplectic doubling). The two 15-dim lifts are
two graded slices of the level-30 theta space; **polarization selection does not happen at the S-closure
level.** (Discipline note: the second self-refuted prediction of the campaign; each has redirected the
question productively.)

## The signal that survived — the half-period vanishing signature

| family | z = 0 | z = 1/2 | z = τ/2 | z = (1+τ)/2 |
|---|---|---|---|---|
| **triangular** (theta-lift) | no zero (min `3.5e-6`, genuine value) | **EXACT ZERO** (`3.3e-21`, j = 8) | no zero (min ≈ 1) | no zero |
| **square** (canonical) | zero (`8.5e-11`, j = 7) | zero (`8.5e-11`) | zero (`1.2e-8`, j = 4) | zero (`1.2e-8`) |

**The triangular family vanishes at exactly ONE half-period; the square family at all four.** A single
distinguished vanishing point is the **odd-theta signature** — and the once-*punctured* torus fiber has
exactly one marked point. This sharpens W2.2 (the odd-spin argument) to a concrete identification: **show the
puncture's position in the fiber quantization is the `z = 1/2` point of the triangular polarization.** If it
is, the theta class is the puncture-compatible polarization — one bundle, one lift map, both slots forced —
the L57 forcing mechanism.

## Tiers and scope

Numerical (q-series, truncation-safe at K = 60; the exact zero at `3e-21` vs genuine small values at `1e-6`
cleanly separated). The doubling statement is derived (the `(−1)^m` twist) and consistent with the failed
fits; not formalized. The puncture ↔ `z = 1/2` identification is W2.2's open target — **the seam arc remains
on probation.** Nothing promotes.

**Provenance.** B364 (the two polarizations), B358–B363 (the seam arc), L57/W2.2. Reproducer: `s_side.py`;
test: `tests/test_b365_polarization_signature.py`.
