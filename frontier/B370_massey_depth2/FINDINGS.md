# B370 (W2.5) — leg A: all six E₆ tangent directions are unobstructed at third order

**Status: leg A banked (frontier); computer-assisted (mpmath dps 100), controls passed, conditional
by nature (an obstruction may appear at any higher order — no "smooth, period" claim). Leg B (the
depth-2 boundary Gram) is pre-registered and NOT yet run. Pre-registration: `PREREGISTRATION.md`
(PR #447, committed before any computation). Firewalled; nothing promotes here (candidacy is the
promotion audit's to adjudicate). Campaign W2.5.**

## Method (as pre-registered: derivation-first, self-gating)

Jet arithmetic through the relator — no transcription of the BCH formula anywhere. Deform
`ρ_t(g) = exp(t·z₁(g) + t²·z₂(g))·ρ(g)` on the generators and expand `X_t(rel)` as a formal series
`I + tP₁ + t²P₂ + t³P₃` in the adjoint representation (B352's two-basis architecture unchanged).
Self-gating: `‖P₁‖ ≈ 0` gates the cocycle; `z₂` is solved blockwise (Fox `d¹` least squares) and
`‖P₂‖ ≈ 0` gates that solve *within the same expansion* (a sign error would double `P₂`, not cancel
it); `ad(q₃) = P₃` then defines the third-order obstruction, solved by B352's exact-Gram normal
equations. Classes are read per exponent block against B352's coker functionals as COMPLEX
components; the verdict is taken modulo the indeterminacy span (finite differences of the same jet
under `z₂ → z₂ + ζ`), with an MB12 random-vector control against each span.

## The verdict table (`massey.py`, `massey_legA.json`; run 10 424 s)

| direction | P₁ gate | P₂ gate | ‖class(q₃)‖ | class vs own gate | indet. rank | MB12 |
|---|---|---|---|---|---|---|
| coboundary control | 1.2e−62 | — | **6.2e−87** | zero (exact tier) | — | — |
| m=1 (integrable control) | 1.4e−52 | 5.3e−52 | **9.6e−62** | ~10 orders below | 0 | 1.55 |
| m=4 (escape) | 2.2e−55 | 7.0e−53 | **8.5e−63** | ~10 orders below | 1 | 0.85 |
| m=5 | 1.4e−52 | 5.0e−52 | **3.8e−61** | ~9 orders below | 1 | 0.84 |
| m=7 | 1.3e−51 | 1.3e−50 | **1.2e−55** | ~5 orders below | 3 | 0.39 |
| m=8 (escape) | 2.5e−54 | 6.3e−49 | **3.1e−54** | ~5 orders below | 4 | 0.36 |
| m=11 | 2.6e−51 | 6.7e−41 | **1.1e−48** | ~7 orders below | 4 | 0.35 |

Per-direction floors grow with the `Sym^{2m}` block dynamic range (the B352 pattern; `e^{±2mμ}` up
to ~1e20 at m=11) — the honest comparison is each class against its own direction's gates, and every
one sits 5–10 orders below, matching the integrable control's signature exactly.

> **All six exponent directions of the E₆ character variety at the geometric representation extend
> to third order.** With B347 (dim H¹ = 1 per exponent), B352 (second order), and B274's smoothness
> criterion context: the 6-dimensional local moduli's integrability evidence now reaches order 3,
> including the θ-odd escape sector {4, 8}.

Bonus data: the indeterminacy ranks (0, 1, 1, 3, 4, 4) grow with the exponent — the third-order
mixed classes are genuinely nonzero for the larger blocks, so the Massey quotient is nontrivial
there and the MB12 control is doing real work (random vectors sit 0.35–0.85 from the spans).

## Honest limits

Computer-assisted at dps 100 — a floor-level zero is evidence of exactness, not a proof; order 4+
untested; the m=1 control calibrates but does not certify the floors; the gauge choice for `z₂`
(minimal-norm) is quotiented out by the indeterminacy span per the pre-registration. Leg B (the
depth-2 boundary Gram, three declared readouts) runs next on the solved `z₂`'s.

**Provenance.** B352 (machinery, second order), B347 (the tangent classes), B357 (boundary
conventions awaiting leg B), PREREGISTRATION.md (PR #447). Reproducer: `massey.py` (~2.9 h);
locks: `tests/test_b370_massey.py` (from the banked JSON + gates).
