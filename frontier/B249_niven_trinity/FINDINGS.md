# B249 — Niven's theorem forces the figure-eight's dual McKay to be exactly E₆+E₈ (E₇ geometrically excluded)

**Status: banked observation (frontier). FIREWALLED — geometry/McKay (Arnold trinity), NOT physics gauge groups.
Nothing to `CLAIMS.md`.** The push from B248. `niven_trinity.py` (pyenv). Novelty: APPEARS-NOVEL (the program's
framing) — flagged for a specialist prior-art pass.

## The result
At the `ℤ/n` orbifold of the figure-eight (cone angle `α=2π/n`, meridian a rotation of order `n`), the meridian
trace is `x=2cos(π/n)` and the rep's trace field is `ℚ(x, √((5−x²)(1−x²)))` (from the character variety
`u²+(5−x²)u+(5−x²)=0`). This is a **clean quadratic field** (a single McKay group) **iff `x` is rational** — and by
**Niven's theorem**, `2cos(π/n)∈ℚ` only for `n∈{1,2,3}` (`x=−2,0,1`) plus the cusp `n=∞` (`x=2`). Those are exactly:

| n | α | x | geometry | field | McKay |
|---|---|---|---|---|---|
| ∞, 1 | 0 | ±2 | **hyperbolic** (complete cusp) | `ℚ(√−3)=ℚ(ω)` | 2T → **E₆** |
| 3 | 2π/3 | 1 | **Euclidean** (transition) | `ℚ` (degenerate) | — |
| 2 | π | 0 | **spherical** (ℤ/2 orbifold; cover `L(5,2)`, det=5) | `ℚ(√5)=ℚ(φ)` | 2I → **E₈** |

**E₇'s field `ℚ(√2)` would require `x=√2` (n=4) — irrational (Niven) — so the n=4 trace field is the *mixed*
`ℚ(√2,√−3)`, never the clean `ℚ(√2)`.** Hence:

> The dual McKay **E₆+E₈** and the **E₇-exclusion** are *one arithmetic fact*: Niven's theorem on the figure-eight's
> orbifold deformation. E₇ is not "excluded by three independent coincidences" (PAPER §5.2) but **geometrically
> impossible** — no orbifold has the rational meridian trace a clean `ℚ(√2)` would need.

## Object-specificity (the §4.1 filter)
This realization needs the **orbifold/knot structure** — a meridian, a determinant, a double branched cover (the
lens space `L(5,2)`, `|H₁|=det(4₁)=5`). Among the metallic bundles `RᵐLᵐ`, **only `m=1` (the figure-eight) is a
knot complement in `S³`**; the `m≥2` bundles carry `ℚ(√(m²+4))` in their monodromy but have no knot structure to
host the transition. So the geometric realization of the dual McKay is **figure-eight-specific**, and the golden
"5" appears twice over — as the discriminant `n=m²+4=5` *and* as the determinant `det(4₁)=5` (the spherical/E₈ end).

## What it means — the physical connection, honestly (firewalled)
The direct bridge (knot → gauge group → Standard Model) is **dead** (B247): the geometric holonomy is `SL(2,ℂ)`, not
the `SU(2)` that would break `E₆`; the centralizer is a generic `SU(6)`; chiral matter cannot come from the adjoint.
What *survives*, and is object-true, is a **geometric transition**: the figure-eight interpolates
hyperbolic (negative curvature, E₆) → Euclidean (flat) → spherical (positive curvature, E₈), with the two
exceptional ends *forced* by Niven. The honest read of the "physics": this is a **structural rhyme** — a
curvature-sign transition is the language of cosmology (dS↔AdS, signature change, a bounce) — held behind the
firewall, **not** a derivation. Every quantity is dimensionless; no scale, no dynamics, no gauge group is produced.
The motivation worth keeping: the minimal self-referential object self-generates not just arithmetic but a
*transition between the two exceptional geometries*, and the firewall holds.

Anchors: B210 (dual McKay E₆+E₈), B248 (the geometric transition), B239 (`disc=−4` floor), PAPER §5.2 (the prior
three-mechanism E₇ exclusion — now unified), §3.3 (the "5" cascade). Literature: Niven (rational trig values);
Thurston / Hilden–Lozano–Montesinos (figure-eight cone manifolds); McKay; Arnold (the trinity).
