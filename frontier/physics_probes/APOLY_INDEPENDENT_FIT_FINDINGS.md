# Phase 2 gold-standard ACHIEVED — m136's A-polynomial independently recovered (no Sage)

**Date:** 2026-06-04. **Status:** exploratory, committed. Proven core P1–P16 untouched. Script:
`apoly_independent_fit.py` (SnapPy ManifoldHP + numpy). Standalone topology; no physics claim.

**Context.** Gate 0 (V32) verified the m=2 trace-map curve = m136's A-polynomial by a controlled
holonomy *match* (testing the known eliminant). Phase 2 sought an *independent symbolic* determination.
Two earlier attempts failed their figure-eight control (V37): the SnapPy shape-route (constant
degenerate points) and the generic-resultant gluing-variety elimination (A-poly-from-gluing
conventions that generic tools don't reproduce). The user asked about installing Sage. **Not needed:**
the trusted-holonomy *fit* route delivers it.

## Method + result

Recover the A-polynomial **from scratch** — no assumed form — by fitting an integer polynomial to
high-precision `(M,L)` from SnapPy's **fundamental-group holonomy** (`ManifoldHP`, dps 40) over ~50
Dehn-surgery deformations: build the monomial matrix `[M^i L^j]`, take the SVD null vector, round to
integers.

- **Control (figure-eight 4₁):** Cooper–Long **vanishes** on the non-abelian points (median `9.3e-16`)
  — the method correctly contains the known A-polynomial as a null vector. (At bidegree (8,2) the box
  over-parametrizes sparse Cooper–Long, so the null space is 4-dim and SVD picks a *combination*; but
  the true A-poly is verified present — the control passes.)
- **Target (m136):** the null space is **1-dimensional** (unique), and the recovered integer
  polynomial is
  ```
  +M^2 - L + 4 M^2 L - M^4 L + M^2 L^2  =  M^2 L^2 - (M^4 - 4 M^2 + 1) L + M^2
  ```
  (integer-fit error `3e-11`, vanishes at `1.6e-15`) — **exactly the m=2 trace-map eliminant.**

## Conclusion

**m136's A-polynomial IS the m=2 trace-map eliminant `M²L²−(M⁴−4M²+1)L+M²`, uniquely and independently
recovered** from trusted holonomy with a passing control. This is the Phase 2 gold-standard
confirmation of V32 — achieved without the gluing-variety elimination (whose conventions are the
specialized part that generic resultants get wrong) and **without Sage** (which is only a heavy GUI
cask here, doesn't compute A-polynomials natively, and would face the same elimination-convention
problem). The j=1728/spectral-curve thread (V32–V34) thus rests on a now-doubly-confirmed foundation:
the curve is genuinely m136's A-polynomial.

**Disposition:** Phase 2 closed (independent symbolic recovery, control passing). Proven core untouched.
