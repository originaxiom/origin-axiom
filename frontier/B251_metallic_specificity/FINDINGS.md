# B251 — the E₆↔E₈ geometric transition is golden-specific: only m=1 is a knot complement

**Status: banked observation (frontier). FIREWALLED — topology/arithmetic. Nothing to `CLAIMS.md`.** The §4.1
specificity test of the B248/B249/B250 transition. `metallic_specificity.py` (pyenv, sympy; SnapPy cross-check).

## The test and the result
B249 claimed the hyperbolic↔spherical transition is figure-eight-specific because it needs the *knot* structure
(meridian, determinant, double branched cover). Made rigorous by sweeping the metallic family `Mₘ` = mapping torus
of `RᵐLᵐ` on the once-punctured torus, monodromy `φ = RᵐLᵐ = [[1+m²,m],[m,1]]` (trace `m²+2`):

> `H₁(Mₘ) = ℤ ⊕ coker(φ−I) = ℤ ⊕ (ℤ/m)²` — which equals `ℤ` **iff `m=1`**.

(`coker[[m²,m],[m,0]]` has Smith normal form `diag(m,m)`.) A knot complement in `S³` has `H₁=ℤ`, so **only `m=1`
(the figure-eight) is a knot complement in `S³`.** Only it has the meridian/longitude, the knot determinant, and
the double branched cover (the lens space) that the geometric transition is built from. For `m≥2` the discriminant
`m²+4` survives in the invariant trace field `ℚ(√(m²+4))`, but there is **no knot determinant and no lens-space
double cover** — no transition. (`H₁(Mₘ)=ℤ⊕(ℤ/m)²` is the same fact banked at B126/S029, here used as the filter.)

## The m=1 "5" stack (golden-specific coincidence)
At `m=1` four a-priori-different integers all collapse to **5**:

| quantity | value | why |
|---|---|---|
| discriminant `m²+4` | 5 | the metallic discriminant at `m=1` |
| `det(4₁) = |Δ(−1)|` | 5 | Alexander `a²−3a+1` at `−1` (SnapPy-confirmed) |
| 2-bridge numerator `p` | 5 | `4₁ = b(5,2)` (SnapPy: `m004 = 4_1 = K2_1`) |
| `|H₁(L(5,2))|` | 5 | double branched cover `L(5,2)=S³/ℤ₅` |

So the "5" of the spherical/E₈ end (B248/B250) is simultaneously the 2-bridge numerator, the knot determinant, and
the discriminant — **all coinciding only at `m=1`**. For `m≥2` these notions split (no knot ⇒ no determinant, no
2-bridge fraction) and only the trace-field discriminant `m²+4` remains.

## What it adds (the specificity tier)
This places the geometric transition in the **sharpest** specificity tier of PAPER §4.1:
- *universal* (all m) → demoted on sight;
- *object-specific* (lives in `{ℚ(√5),ℚ(√−3)}`) → the dual McKay;
- **golden-specific (survives only at `m=1`)** → the superconformal selection (§3.1), the coincidence `n=5`, **and
  now the E₆↔E₈ geometric transition** — the last is the strongest tier, because it fails for *every* `m≥2` by a
  homology obstruction, not a numerical near-miss.

## Physical read (firewalled)
None of this produces a scale or matter; it is a topological obstruction sharpening *which* metallic member can
even carry the firewalled curvature-sign transition (S042). The answer — exactly one, the figure-eight — is why the
whole program is about this single object.

Anchors: B248/B249/B250 (the transition), B126/S029 (`H₁(Mₘ)=ℤ⊕(ℤ/m)²`), PAPER §3.3 (the "5" cascade), §4.1 (the
filter). Literature: 2-bridge knots and their lens-space double branched covers; once-punctured-torus bundles
(Floyd–Hatcher); the figure-eight as `b(5,2)=m004`.
