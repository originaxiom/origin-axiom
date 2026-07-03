# B370 (W2.5) — leg A: all six E₆ tangent directions are unobstructed at third order

**Status: COMPLETE (both legs banked, frontier). Computer-assisted (mpmath dps 100), all gates
passed; conditional by nature (higher orders untested — no "smooth, period" claim). Pre-registration:
`PREREGISTRATION.md` (PR #447, committed before any computation). Firewalled; nothing promotes here
(candidacy is the promotion audit's to adjudicate). Campaign W2.5 — with this, the Gate-B classical
germ is complete: orders 1–3 integrable + Lagrangian + universal-τ (order 1) + the depth-2 bending
data below.**

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

## Leg B — the depth-2 boundary data: the τ-defect matrix (VERDICTS, gates green)

Two earlier executions were stopped by the pre-registered first-order τ-gate (basis-bridge bugs — a
scale-only bridge twice; both recorded, neither interpreted). The fix: the root→TG bridge must compose
with B352's **antidiagonal intertwiners** (`v_TG[j] = v_chain[d−j]/τ_j`); the acceptance test then
passed exactly — **τ = −2√3·i reproduced uniformly across all six directions, spread 1.4e−63**, with
per-block off-diagonals at floor (1e−60..1e−66). With the gate green, the τ-defect
`δ(m→m′) = φ_λ(z₂) − τ·φ_µ(z₂)` is indeterminacy-invariant (the universal-τ kills the ζ-shifts), and
its readouts are legitimate invariant content (`massey_legB.py`, `massey_legB.json`, run 2402 s;
all values relative to their per-entry φ-scale — the blocks span ~50 orders):

1. **The universal-τ is strictly first-order.** δ ≢ 0: the maximal relative defect is **1.017** — at
   depth 2 the boundary germ bends off the τ-line by order one. B357's universal shape is an order-1
   identity, not an all-orders rigidity — a sharp, previously unknown boundary on that banked result.
2. **The bending is θ-graded.** Into F₄-target blocks the defect saturates (relative max 0.99–1.00);
   into escape-sector targets ({4,8}) it is suppressed ~3× (0.325/0.326). **The depth-2 germ sees the
   E₆ → F₄ fold** — the first appearance of the θ-grading in the boundary dynamics data.
3. **Mixed symmetry.** Neither symmetric nor antisymmetric (sym-dev 1.50, antisym-dev 2.00 at the
   normalization where a symmetric matrix gives 0 and 2 respectively); the maximal entries lean
   symmetric. Reported as data.

Method note for the record: the τ-gate rejected two O(1) "defect matrices" as convention artifacts
before any interpretation, then certified the third. The gate design — re-deriving a banked identity
inside the new pipeline before reading anything new — is what made these verdicts safe to state.

**Provenance.** B352 (machinery, second order), B347 (the tangent classes), B357 (boundary
conventions awaiting leg B), PREREGISTRATION.md (PR #447). Reproducers: `massey.py` (~2.9 h, leg A),
`massey_legB.py` (~40 min, leg B); locks: `tests/test_b370_massey.py` (both legs, from the banked
JSONs + gates).
