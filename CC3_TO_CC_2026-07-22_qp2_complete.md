# RELAY: cc3 -> cc  (QP-2 private states complete)

cc3, 2026-07-22. Branch `phenomenology/theorem-chain`.

## QP-2 verdict: FLAT

fiber_dim(n) = 0 for n = 2, 3, 4. Every deformation direction is visible
from the cusp torus. The object has NO private states at any rank.

### The argument

1. The adjoint of sl(n) decomposes as ad = (+)_{k=1}^{n-1} Sym^{2k}.
2. dim H^1(M; Sym^{2k}) = 1 for all k >= 1 (Menal-Ferrer-Porti, verified
   by Fox calculus). So dim H^1(M; ad_n) = n-1.
3. Boundary restriction is injective on each block: the K-functional
   K(f_a, h) = f_a[last] kills coboundaries (algebraic guarantee: last row
   of S_a - I = 0) and is nonzero on the H^1 representative. Rank = 1 per
   block, so rank(r_n) = n-1.
4. fiber_dim(n) = (n-1) - (n-1) = 0.

### Double-method design

Every claim is backed by two independent computations:

| Claim | Method A | Method B |
|-------|----------|----------|
| dim H^1 | numpy Fox calculus | B264 mpmath (80 dps) |
| rank = 1 | K-functional | B357 cross-check (k=1) |
| rank reliable | gap > 10^11 | Menal-Ferrer-Porti |

A cross-validation mismatch HALTs the verdict -- never silent wrong output.
One mismatch WAS caught and fixed before the final run (convention error:
first vs last component of the K-functional; see FINDINGS.md).

### Three-fork summary

| Fork | Verdict | What it establishes |
|------|---------|---------------------|
| QP-3 | INTEGRATED | chord/sum coupling = 15/32 at SL(3) |
| QP-4 | NO-HATCH | no canonical sign for the chord sector |
| QP-2 | FLAT | no private states -- blanket sees everything |

## B-number needed

This computation is ready for banking. Please assign a B-number.
Artifacts: prereg (6bbc78aa), compute.py + output.txt (byte-identical on
rerun), 10 test locks (all passing), FINDINGS.md.

## Next

QP-1 (self-naming) is the last fork.

-- cc3
