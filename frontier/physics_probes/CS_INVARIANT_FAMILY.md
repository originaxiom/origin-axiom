# CS-invariant family of the metallic mapping tori (m=1,2,3) — corrected torsion, no tidy pattern

**Date:** 2026-06-04. **Status:** exploratory, committed for honest history. Proven core P1–P16
untouched. Script: `frontier/physics_probes/cs_invariant_family.py` (sympy + mpmath).
**Standalone topology / number theory — explicitly NOT a physics crossing** (SL(2,C) Chern–Simons of
hyperbolic 3-manifolds is a TQFT; this is the Dimofte-object / cross-check, not our-universe physics).

**What this is.** The natural Tier-B math harvest after the two physics-crossing negatives (V28, V29):
the Chern–Simons semiclassical data (A-polynomial = classical action; normal Reidemeister-type torsion
`τ_m = det'(I − D(T_m²)|_normal)` = one-loop-type term) of the metallic mapping tori `φ_m²`, computed at
the **correct** complete hyperbolic structure (`κ = tr[A,B] = −2`, both peripheral elements parabolic).
This **corrects** the earlier AI-web evaluation at `κ=+2`, which sat at the *identity* rep `x=2` and
returned the abelian determinant (5 for m=1, 32 for m=2), not the geometric torsion.

## Results

| m | manifold | trace field (min poly of x) | deg | `τ_m(geom)` | A-polynomial | volume |
|---|---|---|---|---|---|---|
| 1 | figure-eight `4₁` | `u²−3u+3` = `Q(√−3)` | 2 | **−3** (clean; `|τ|=3=|disc|`) | Cooper–Long (B67, exact) | 2.0298832 |
| 2 | census `m136` | `u⁴−4u²+8` | 4 | **−16** (clean) | `M²L²−(M⁴−4M²+1)L+M²` (verified) | 3.6638623 |
| 3 | bundle `[[10,3],[3,1]]` | `u⁸−4u⁷+4u⁶−u⁵+8u⁴−11u³−4u²+3u+6` | 8 | **branch-ambiguous** (−2.64 or −52.08) | not a clean eliminant (`√(5x⁴−10x³−x²+6x+1)`) | needs SnapPy |

All values recomputed from one uniform code path (branch `y=β_m z/(1−α_m)` from `p_m=y`; z-branch from
`T_m²[0]=x`; `κ` via the Fricke relation; the discrete-faithful rep = the κ=−2 root with **real**
torsion — the others are Galois conjugates with complex τ).

## Honest findings

1. **The corrected geometric torsions are `−3, −16` for m=1,2** (not the web chat's `5, 32`). The
   `5`/`32` were evaluated at `κ=+2` — which includes the *identity* representation `x=2` — and are the
   abelian knot determinant, not the adjoint/geometric torsion. At the genuine `κ=−2` complete
   structure (`x=(3±i√3)/2` for m=1, in `Q(√−3)`), `τ₁=−3`.
2. **The family has NO tidy arithmetic pattern.** The trace-field degree grows `2 → 4 → 8`, and the
   torsion is a clean integer only for m=1,2. `m=1` is special (`|τ|=3=|disc Q(√−3)|`). By **m=3** the
   torsion at the geometric rep is already **branch-ambiguous**: the two `±√disc` fixed-locus branches
   give *different* real torsions (−2.64 vs −52.08), and pinning the actual discrete-faithful value
   would require the explicit hyperbolic structure (SnapPy) — not resolved here.
3. **The m=3 A-polynomial is not a clean eliminant:** the meridian relation `tr(t)²(x)` carries
   `√(5x⁴−10x³−x²+6x+1)` (the fixed locus is no longer a rational curve), so there is no clean
   degree-(2,4) A-polynomial analogue. (m=1,2 A-polynomials are clean and verified.)
4. **The open question stands:** whether `τ_m = det'(I − D(T_m²)|_normal)` *is* Porti's adjoint
   Reidemeister torsion (the genuine one-loop CS term) or a related-but-distinct invariant remains
   unconfirmed — it needs comparison to Porti's formula. The clean m=1 value (`−3`, in the trace
   field) is consistent with an adjoint-type torsion; the m=3 branch-ambiguity warns that the naive
   "normal torsion" is not yet a canonically-normalized invariant.

## Disposition

Real CS/number-theory data for the metallic family, banked as **topology, not a physics crossing**.
The corrected m=1,2 torsions (−3, −16) and trace fields (`Q(√−3)`, deg-4) are the clean, defensible
new content; m=3 shows the family becomes genuinely complicated (degree-8 field, branch-ambiguous
torsion, no clean A-polynomial) — there is **no simple new invariant pattern across the family**.
This is the honest object for an eventual specialist (the Porti/Dimofte comparison), not a result on
its own. Proven core untouched.
