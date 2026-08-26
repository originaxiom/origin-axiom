# THE SUPERPOSITION SPEAKS — the merged ζ_K spacings that reject single-GUE at p~10⁻⁸⁵ are fit by the 2-fold GUE superposition surmise at D = 0.024, while each factor alone rejects it: the product structure ζ·L(χ₋₃) is exactly what the spacing statistics see
## (outside bench, 2026-08-26; fifty-fifth memo; B1151's named follow-up executed on B1151's own committed data; C4's honest negative completed into a positive identification)

### The question
B1151 (cc bench, i9) ran my preregistered C4 cell at T=3000: the single-GUE
gate failed (merged D = 0.13365, p ≈ 2×10⁻⁸⁵) while each factor separately
sat at the surmise-error level (D ≈ 0.040/0.049) — the deviation lives in the
merge, the fingerprint of a 2-fold superposition. B1151 named the positive
test as the follow-up. This cell runs it, on the same committed raw zeros
(main @ 522c7caa), with the same unfolding conventions.

### THE MODEL (closed form, same approximation family as the test it replaces)
Unit-density GUE gap function from the Wigner surmise (renewal):
**E_W(s) = e^{−4s²/π} − s·erfc(2s/√π)**, E_W′(s) = −erfc(2s/√π) − (4s/π)e^{−4s²/π}.
Superposition of two independent factors with density fractions f₁+f₂ = 1:
E(s) = E_W(f₁s)·E_W(f₂s), **CDF(s) = 1 + E′(s)**. Fractions from the merged
counts: f_ζ = 0.4522, f_L = 0.5478. Model sanity verified: CDF(0) = 0,
CDF(∞) = 1 to 10⁻⁹, mean = 1.000000.

### THE FACTS (`certificates/c4b_superposition.py`; data vendored in `certificates/c4data/`; all gates preregistered as asserts, GREEN)
| test | D | p | gate |
|---|---|---|---|
| A1: ζ alone vs single-GUE | 0.0401 | 7×10⁻⁴ | anchor to B1151 ✓ |
| A1: L(χ₋₃) alone vs single-GUE | 0.0487 | 1.4×10⁻⁶ | anchor to B1151 ✓ |
| A2: merged vs single-GUE | 0.13359 | 2×10⁻⁸⁵ | anchor to B1151 ✓ |
| **S1: merged vs 2-fold superposition** | **0.02400** | 3.7×10⁻³ | **D < 0.06 and D < D_single/2 ✓** |
| C1: ζ alone vs superposition | 0.1802 | — | worse than its GUE fit ✓ |
| C1: L alone vs superposition | 0.1914 | — | worse than its GUE fit ✓ |

- **S1 (the claim, landed):** the superposition surmise absorbs the merge
  deviation from 0.134 down to **0.024 — below even the factors' own
  single-GUE residuals.** The p-value (0.0037) fails a strict 0.01, exactly
  as B1151's fence predicts at n ≈ 5459 for any surmise-level model (the
  Wigner surmise itself is detectably approximate at ~2500 samples); the
  preregistered claim was the D gate, and it passed with a 5.6× margin.
- **C1 (the discriminating control):** the superposition is *not* a
  universally better fitter — each single factor rejects it hard (D ≈ 0.18)
  while fitting single-GUE at 0.04. The model wins only where the product
  structure is real.

> **B1151's negative and this positive are two halves of one statement:
> ζ_K's nearest-neighbour statistics see exactly its factorization
> ζ·L(χ₋₃) — two independent GUE spectra laid on top of each other, no
> cross-repulsion — no more and no less. The C4 arc closes: the gate
> failure was not noise, it was structure, and the structure is the product
> formula.**

### Fences
Generic throughout: superposition-of-two-GUE is the expected class for *any*
product of two L-functions (B1142/B1151's universality fence) — nothing here
is object-specific, no firewall crossing. Global count fractions are used for
f₁, f₂ (the true fractions drift as log t; at T=3000 the drift is far below
the surmise error). The renewal (independent-spacings) construction of E_W is
the same approximation family as the single-GUE Wigner test it replaces — the
comparison is like-for-like. Data note: the committed ζ file carries 2469
zeros (B1151's prose says 2468); the anchors reproduce to 10⁻³ regardless.
The named residual follow-up (exact Gaudin per-factor + higher-order
unfolding) stands. Gate 5 untouched.

### Certificates
`certificates/c4b_superposition.py` (numpy/scipy; deterministic);
data `certificates/c4data/c4_zeros_{zeta,L}.txt` (vendored verbatim from
main @ 522c7caa, B1151's committed scan); output
`outputs/c4b_superposition_out.txt` (in-lane rerun byte-identical).

### One sentence for the ledger
The cusp voice's numerator fails the single-spectrum test precisely because
it is two voices — and when the test is asked the right question, the two
independent golden-class spectra inside ζ_K answer to within the error of the
question itself.
