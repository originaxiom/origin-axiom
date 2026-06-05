# B77 (Phase 1a) — the degree=rank mechanism: a sign refinement, and the A↔D unification refuted

**Date:** 2026-06-05. **Status:** high-precision-numerical (robust across reps/seeds). Standalone
low-dim topology; **no Origin-core claim**; proven core P1–P16 untouched. Script: `probe.py`. Test:
`tests/test_b77_degree_rank_mechanism.py`.

## Two questions

degree=rank (B73/V54, B75/V57): on the SL(n) figure-eight bundle's **principal** Dehn-filling component
`{tr A=tr A⁻¹=1}`, the longitude is the meridian's `n`-th power, `Mⁿ=L`. This probe asked:
1. **What is the precise relation** — is there a hidden scalar?
2. **The A↔D unification hypothesis (CONJECTURED):** is degree=rank the geometric shadow of the Dickson
   tower's top factor `char(Mⁿ)` — i.e. are the meridian/longitude eigenvalues the roots of `char(Mⁿ)`?

## Findings (with the genuine meridian `μ=A⁻¹t`, V46; `μ` commutes with `[A,B]`)

### 1. A sign refinement of degree=rank
The relation is the **scalar-matrix identity**
```
   [A,B] = c · μⁿ ,    c = (−1)ⁿ⁻¹
```
robust across reps/seeds: **`c=+1` at n=3, `c=−1` at n=4** (scalar-deviation ~1e-10 … 1e-14). The
scalar `c` is forced to be an `n`-th root of unity (`cⁿ = det[A,B]/det(μ)ⁿ = 1/1 = 1`); the **observed**
branch is `(−1)ⁿ⁻¹`. So degree=rank is precisely the **signed** scalar-matrix law
`[A,B] = (−1)ⁿ⁻¹ μⁿ`. **Prediction for n=5: `c=+1`** (a sharp, falsifiable target for B78).

### 2. The A↔D unification is REFUTED
The meridian eigenvalues `eig(μ) = eig(t)` (confirmed equal, ~1e-11) are **generic** and **vary
continuously across the component** — `|eig|` spreads ~0.3–0.4 over reps. They are **not** roots of
unity, **not** metallic, and **not** the fixed Dickson `char(Mⁿ)` roots. Therefore:

> **degree=rank (a peripheral scalar-matrix identity) and the Dickson tower (the trace-map *Jacobian*
> spectrum) are genuinely different objects.** The "why n" mechanism lives in the **bundle / peripheral**
> structure (the cusp), not the trace ring.

This kills the tempting unification of the two prizes (A and D) with a decisive computation, rather than
letting it harden into a claim. The sign `(−1)ⁿ⁻¹` does **echo** the Dickson tower's `(−1)^k` parity
(B64) — a structural resonance worth noting — but it is **not** an eigenvalue match; the connection is
at the level of the `±` grading, not the spectrum.

## Honest reading

- A genuine **sharpening** of the central result: degree=rank is the signed identity
  `[A,B] = (−1)ⁿ⁻¹ μⁿ`, with `c` an `n`-th root of unity forced by determinants. The mechanism is now a
  cleaner target: *why is the longitude exactly the `n`-th power (up to the sign) of the meridian?*
- A clean **negative**: the two prizes do **not** unify through the eigenvalue spectrum. The mechanism
  is peripheral/topological, which is where the search should go (e.g. the relation of the fiber
  boundary `[a,b]` to the bundle monodromy on the once-punctured-torus bundle), not the trace ring.

## Disposition

Phase 1a complete. Sets up **B78 (n=5)**: the test is now sharper — does `n=5` give `[A,B]=(+1)μ⁵`
(exponent 5 *and* scalar `c=+1`)? Proven core untouched.

## Reproduce

```bash
python frontier/B77_degree_rank_mechanism/probe.py
python -m pytest tests/test_b77_degree_rank_mechanism.py -q
```
