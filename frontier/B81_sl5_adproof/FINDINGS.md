# B81 — the CRT/F_p route at SL(5): blocked by gauge-corruption at the doubly-degenerate sector

**Date:** 2026-06-05. **Status:** exact F_p; an honest negative that **precisely localizes** the
B58/B66 barrier. Standalone Lie/invariant theory; **no Origin-core claim**; proven core P1–P16
untouched. Script: `probe.py`. Test: `tests/test_b81_sl5_adproof.py`.

## The question

B80 (V62) proved the SL(4) tower from first principles by reconstructing `J(m)` over ℚ[m] from the
exact F_p ε-series pinv-limit Jacobian `DT_0`. That relied on `DT_0(4)` being **seed-canonical** (its
char poly is gauge-invariant), so m-interpolation in a fixed basis is well-defined. **Does the same
route reach SL(5)?**

## The decisive test

`char(DT_0)` is conjugation-**invariant**, so it must agree across seeds (different perturbation reps
`P,Q` and metric `S`) **iff** the pinv-limit is a well-defined Jacobian. Computing it exactly over F_p:

| rank | `char(DT_0(n,m=1))` across seeds | consequence |
|---|---|---|
| **SL(4)** | **identical** (seed 20 = 99) | pinv-limit canonical ⇒ B80's CRT route **valid** (V62) |
| **SL(5)** | **scatters** (24/25 coeffs differ, seeds 20/99/123) | pinv-limit **gauge-corrupt** ⇒ route **blocked** |

So at SL(5) the ε-series pinv-limit does **not** produce a well-defined characteristic polynomial —
m-interpolation is invalid and the CRT reconstruction cannot be applied.

## Where the corruption lives

Tagging `char(DT_0(5,m=1))` against the Dickson catalog gives
`char(M⁻¹)·char(M)²·char(M²)¹·char(M³)·char(M⁴)·char(M⁵)·char(−M²)·char(−M³)·(t−1)²·(t+1)¹` — i.e.
`char(M²)` at multiplicity **1** (should be 2) and `(t+1)` at **1** (should be 2), a **degree-3
untagged remainder**. This is exactly B66's numerical gap — now shown to be a genuine **gauge-corruption
of the char poly** (seed-dependent), not a tagging artifact.

## Net — the barrier, precisely localized

The CRT/F_p route reaches exactly the sectors where the pinv-limit is **seed-canonical**, i.e. the
**multiplicity-≤1** even-k sectors: the single `char(−M²)` at SL(4) resolves (B80). The
**multiplicity-≥2** degeneracy — `char(M²)²` at SL(5) — is the residual `e₂ = tr(Λ²A)` two-block barrier
(B58), and it manifests concretely as **char-poly seed-scatter**. SL(4) works precisely because its
even-k sector is multiplicity 1; SL(5) is the first rank with a doubly-degenerate even-k sector.

**This sharpens B80's optimistic scope note** ("opens the route to SL(5)/SL(6)"): the route opens but
is blocked at the first multiplicity-≥2 degeneracy. Closing SL(5) from first principles needs a
**degeneracy-robust pinv** (one that resolves coincident eigenvalues), not this method; the B62
opposition-involution θ-split already gives the SL(5) tower **structurally** (not from first principles).

Honest negative, precisely localized. The SL(4) result (B80/V62) stands as the rank where the route
succeeds.

## Reproduce

```bash
python frontier/B81_sl5_adproof/probe.py        # ~50s (a few SL(4)/SL(5) F_p engine calls)
python -m pytest tests/test_b81_sl5_adproof.py -q
```
