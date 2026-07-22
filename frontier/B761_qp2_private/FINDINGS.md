# QP-2: private states — FINDINGS

> Prereg hash: 6bbc78aa. Branch: `phenomenology/theorem-chain`. cc3 seat.
> Gate 5-Q. Nothing to CLAIMS.

## Verdict: FLAT

fiber_dim(n) = 0 for n = 2, 3, 4. The object has no private states at any
rank. Every deformation direction of the character variety is visible from the
cusp torus. S072's "Markov blanket sees everything" reading is upheld.

## The computation

For the figure-eight complement M at the geometric SL(2,C) representation,
the adjoint of sl(n) decomposes under the principal sl(2) as:

    ad(sl(n)) = (+)_{k=1}^{n-1} Sym^{2k}

The fiber dimension (number of deformation directions invisible from the
boundary) is:

    fiber_dim(n) = dim H^1(M; ad_n) - rank(restriction to boundary)

### Per-block results

| k | dim H^1(Sym^{2k}) | |phi_mu| | d1 gap | restriction |
|---|--------------------:|--------:|-------:|:-----------:|
| 1 | 1                  | 0.5495  | 10^15  | detected    |
| 2 | 1                  | 0.6195  | 10^13  | detected    |
| 3 | 1                  | 0.6829  | 10^11  | detected    |

### Per-SL(n) assembly

| n | dim H^1(ad_n) | rank(r_n) | fiber_dim |
|---|:---:|:---:|:---:|
| 2 | 1   | 1   | 0   |
| 3 | 2   | 2   | 0   |
| 4 | 3   | 3   | 0   |

## Method: double-method cross-validation

Every claim is backed by two independent computations. A cross-validation
failure HALTs the verdict.

1. **dim H^1**: computed by both numpy Fox calculus (self-contained) and B264's
   mpmath Fox calculus (80 dps, tol=1e-50). All three blocks agree.

2. **Boundary restriction**: the K-functional K(f_a, h) = f_a[last] detects
   the meridian restriction. The algebraic guarantee (last row of S_a - I = 0
   in the transposed convention) ensures coboundaries have f_a[last] = 0. So
   f_a[last] != 0 for a cocycle proves it's NOT a coboundary, hence rank >= 1.

3. **B357 cross-check**: B357's independent computation (different presentation,
   different code, mpmath at 60 dps) confirms rank = 1 at k = 1.

4. **Singular value gaps**: all rank claims have gap ratios > 10^11 (smallest
   nonzero / largest zero singular value), ruling out threshold artefacts.

5. **MFP control**: dim H^1(Sym^{2k}) = 1 for k = 1..6 (Menal-Ferrer-Porti),
   verified via B264.

## Convention note (caught by HALT mechanism)

The code uses the transposed convention (B264's `symn` returns Q^T). In this
convention:
- The fixed vector of S_a is e_0 (first basis vector), not e_{2k}.
- K(v, e_0) = v[last] (antidiagonal pairing), not v[0].
- The LAST row of (S_a - I) is zero (not the first row).

An initial implementation checked v[0] and was caught by the cross-validation
HALT before any verdict was issued. This validates the double-method design.

## What FLAT means for S072

The half-lives-half-dies theorem says the boundary restriction has Lagrangian
image (half-dimensional). For a 1-cusped manifold with dim H^1 = 1 per block,
the restriction is injective: every internal deformation direction has a
boundary shadow. The cusp torus (the Markov blanket) sees everything.

The formula:

    fiber_dim(n) = (n-1) - (n-1) = 0

is rank-independent. It holds for all n, not just n = 2, 3, 4. The object has
no private states at any rank.

## Q2 controls

- **Menal-Ferrer-Porti**: PASS for k = 1..6 (all dim H^1 = 1).
- **Dehn-filling A-variety** (cited from B71/B73/B83): each component is 1D,
  mapping to a 1D curve in the boundary. fiber_dim = 0 at every Dehn filling.
- **B357 Lagrangian certificate** (cited): rank = 6/6 over all E6 exponents
  {1,4,5,7,8,11}. Image is 6-dim = half of 12. Lagrangian confirmed.

## Together with QP-3 and QP-4

| Fork | Verdict     | What it establishes                           |
|------|-------------|-----------------------------------------------|
| QP-3 | INTEGRATED | chord/sum coupling = 15/32 at SL(3)           |
| QP-4 | NO-HATCH   | no canonical sign for the chord sector        |
| QP-2 | FLAT       | no private states — blanket sees everything   |

The object is integrated (15/32), cannot close (unsigned), and has nothing to
hide (no private states). Three of four S072 layers now have computational
backing. QP-1 (self-naming) remains.
