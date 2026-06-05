# B68 / Path E — the smarter AJ retry (confirms V52, bounded negative)

**Date:** 2026-06-05. **Status:** numeric (well-conditioned |q|=1); confirms the V52 bounded negative
via an independent method. Standalone quantum-topology; **no Origin-core claim**; proven core untouched.
Script: `cyclotomic_numeric.py`. Test: `tests/test_b68_cyclotomic_numeric.py`.

## What Path E asked

Retry the figure-eight AJ / colored-Jones recursion **only with a genuinely smarter approach** than V52's
brute symbolic `linsolve` over `ℚ(q)` (which did not complete). Accept the negative if it stays
prohibitive.

## The smarter approach

Compute the figure-eight colored Jones exactly via **Habiro's cyclotomic formula**
`J_N = Σ_{k=0}^{N-1} q^{-kN} ∏_{j=1}^{k}(1-q^{N-j})(1-q^{N+j})` (sanity: `J_2 = q⁻²−q⁻¹+1−q+q²`, the
figure-eight Jones polynomial), then find the `q`-holonomic recursion by **per-q numeric null-space** at
`|q|=1`. Two corrections over a naive numeric attempt were essential:
1. **`|q|=1` is mandatory.** Off the unit circle `J_N` spans enormous magnitude ranges (`q^{-kN}`), so
   the SVD is catastrophically ill-conditioned (cond ~1e26) and the "null-space" is noise. On `|q|=1`,
   `J_N` is bounded and cond ~1e2.
2. **Solve per q-value.** The recursion coefficients `a_b(Q,q)` are Laurent in `q` *independent of `N`*,
   so a single set of constants cannot be shared across `q`; each generic `q` is solved separately and a
   genuine recursion shows a **consistent** null-space dimension across all of them.

## Finding

- **No homogeneous recursion of order ≤ 3 at `Q`-degree ≤ 4** exists at generic `|q|=1` — null-space
  dimension `0` consistently. This **reproduces V52's exact "no homogeneous order-2" result** by an
  independent (numeric) route.
- The **only** non-zero null-spaces appear at a single `q` near a **root of unity** (`θ≈2π/3`) — a
  colored-Jones **degeneracy artifact**, not a recursion (a real recursion is consistent across *all*
  generic `q`). The genuine figure-eight recursion is **inhomogeneous with a `Q`-dependent
  inhomogeneity** (Garoufalidis–Le), beyond clean detection at this order/degree.

## Disposition

The **V52 bounded negative stands**, now confirmed by a second method. The exact figure-eight quantum
A-polynomial recursion `|_{q=1} = A` identity remains a **literature theorem** (Garoufalidis–Le), not
re-derived in-house. No claim resurrected; no new positive. Honest negative, banked.

## Reproduce

```bash
python frontier/B68_aj_conjecture/cyclotomic_numeric.py
python -m pytest tests/test_b68_cyclotomic_numeric.py -q
```
