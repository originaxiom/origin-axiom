# B248 — the dual McKay E₆+E₈ of the figure-eight, realized as its hyperbolic↔spherical geometric transition

**Status: banked observation (frontier). FIREWALLED — geometry + McKay (Arnold trinity), NOT physics gauge groups.
Nothing to `CLAIMS.md`; P1–P16 untouched.** The push from the B247 adjudication. `geometric_transition.py` (pyenv).

## The result
The figure-eight's dual McKay `E₆+E₈` (B210) is the two **ends of its cone-manifold geometric transition**. The
meridian holonomy is a rotation by the cone angle `α`, trace `x = 2cos(α/2)`; sweeping the character-variety curve
`φ(s,u)=−s⁴u−s⁴+s²u²+3s²u+3s²−u−1=0` in `x` sweeps `α`:

| cone angle `α` | `x=2cos(α/2)` | geometry | Riley `u` | trace field | McKay |
|---|---|---|---|---|---|
| `0` | 2 | **hyperbolic** (complete cusp) | `e^{±2iπ/3}` | `ℚ(√−3)=ℚ(ω)` | `2T=SL(2,F₃)` → **E₆** |
| `2π/3` | 1 | **Euclidean** (transition) | `−2` (rational) | `ℚ` (degenerate) | — |
| `π` | 0 | **spherical** (ℤ/2 orbifold) | `−(5∓√5)/2` | `ℚ(√5)=ℚ(φ)`, `tr(ab)=φ` | `2I=SL(2,F₅)` → **E₈** |

The spherical end is concrete: the ℤ/2 orbifold (meridian order 2) of `4₁=b(5,3)` has **double branched cover the
lens space `L(5,2)=S³/ℤ₅`** (spherical), with `|H₁| = det(4₁) = 5`. So the **"5"** of the golden/E₈ end *is the knot
determinant*, while the Eisenstein **"−3"** sits at the hyperbolic/E₆ end; the Euclidean structure (`α=2π/3`) is the
transition between them. The `x=0` rep is a genuine non-abelian **SU(2)** rep (all word-traces real in `[−2,2]`,
`tr(ab)=φ`) — i.e. a *spherical* holonomy.

## Why this is more than a re-presentation of B210
B210 read `E₆+E₈` from the geometry's trace field (`ℚ(√−3)`) and the *bundle monodromy* (`ℚ(√5)`, the `RL` matrix).
Here **both** fields arise as flat connections / geometries on `4₁` itself — two distinguished points on **one**
character-variety curve, the hyperbolic and spherical ends of the same geometric deformation (Thurston's geometric
transition; Hilden–Lozano–Montesinos for the figure-eight cone manifolds). So the dual McKay is not two unrelated
faces but the two stable geometries of a single object, separated by a Euclidean wall.

## Relation to the firewall (B247)
This is the *positive, object-true* residue of the B247 adjudication: the physics bridge (breaking E₆ by the
geometric holonomy) fails because the E₆-selecting connection (`SL(2,ℂ)`, hyperbolic) and a breaking-SU(2)
connection are different points — **but that very distinctness is this clean geometric statement**: the figure-eight
carries E₆ in its hyperbolic geometry and E₈ in its spherical geometry. The split that kills the bridge *is* the
content. Firewalled: `E₆/E₈` here are Arnold-trinity / McKay labels, not gauge groups.

Anchors: B210 (dual McKay E₆+E₈), B239 (`disc=−4` floor / `ℚ(√−3)`), B247 (the V1 adjudication), PAPER §3.2/§5.
Literature: McKay; Arnold (the trinity); Thurston, Hilden–Lozano–Montesinos, Porti (figure-eight cone manifolds);
2-bridge double covers = lens spaces.
