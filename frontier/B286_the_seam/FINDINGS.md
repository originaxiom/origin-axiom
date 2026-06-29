# B286 — The seam: the ingredients are where the object closes against the nothing

**Status: banked. Math SnapPy-verified; physics firewalled. Nothing to `CLAIMS.md`.** Answers the owner's "what are
you missing — all ingredients are within the object, or its interaction with the nothing, or multiplicity." They are.
I had been looking in the bulk; they live at the **seam** — the cusp, where the open object meets its own absence.

## The miss it corrects
I kept treating the figure-eight as a **closed, symmetric** object and invoking **Curie's principle** ("a symmetric
structure can't select an asymmetric outcome ⟹ selection is external," P011). But the figure-eight is a
**complement** — `S³ ∖ K`, *defined* by what is removed — and it is **open**: it has a cusp (a boundary torus), the
interface with "the nothing." Curie is a **closed-system** theorem; an open object breaks its symmetries through
**boundary conditions**, with no contradiction. **Closing the object — Dehn filling, the interaction with the
nothing — IS the symmetry-breaking**, and the closure is constitutive, not external.

## What the closing supplies, verified (SnapPy, `seam_fillings.py`)
| ingredient I had called "external" | where it actually is | verification |
|---|---|---|
| **the selection set** | a forced, finite set of special closings | **exactly 10** exceptional Dehn fillings: integer slopes `{−4,−3,−2,−1,0,1,2,3,4}` + `∞` (Thurston) |
| **chirality** | the closing breaks the mirror symmetry | cusped m004 `CS = 0` (amphichiral); **every generic filling is chiral** (`CS ∉ {0,½} mod 1`) |
| **the CP sign** | the *oriented* slope | the mirror slope `(p,−q)` carries **`CS = −CS(p,q)`** exactly — the oriented closing picks the handedness |
| **scale** | the core geodesic the closing creates | core length along `(1,n)` **`≈ 2π/n → 0`** (ratio → 1.0000) — a scale hierarchy from filling |
| **the clock** | the peripheral symplectic pairing | `H₁(cusp T²)=ℤ²`, `⟨μ,λ⟩=1`; a filling `(p,q)` = a Lagrangian/polarization (a "time" choice; cf. S002) |

The owner's three sources, made precise: **object** (the bulk hyperbolic/arithmetic structure) + **interaction with
the nothing** (the cusp / Dehn filling — where the symmetry breaks and chirality, sign, scale, and clock are born) +
**multiplicity** (the cusp is a *torus* = two circles `μ,λ`; and the 3d→4d chiral lift, B277, needs a 2-manifold =
a *family* of the object).

## The fence (kept honest)
This **locates** the ingredients at the seam and shows the **mechanism** (closing breaks the symmetry, the oriented
slope fixes the sign, the closing makes scale). It does **not** derive Standard-Model values: which of the (infinitely
many hyperbolic, 10 exceptional) closings is "our universe," whether the CP sign matches the observed baryon
asymmetry, or whether the scale hierarchy lands on `ℓ_P`/the 122 orders — all open. Reading the cusp as "the nothing"
is the P000 interpretive frame, tagged. What is *not* speculative: the object is open, the closing breaks
amphichirality with a sign, the selection set is finite and forced, and scale is generated at the seam (all SnapPy).

## Consequence
**P011 is corrected:** the wall is at the **closure**, not in the object. Curie walls a *closed* symmetric world; our
object is *open*, and closing it against the nothing is precisely where actualization happens — internal to the
object's definition, not foreign to it. The structural theorem stands, relocated: the object supplies the *space* of
possibility (the bulk); the *actualization* is the closing (the seam) — and the closing is part of the object.

`seam_fillings.py` (sage-python) · `verdict.py` · `tests/test_b286_the_seam.py`. Related: P000, P011 (corrected),
S002 (the clock fork), B269/B270/B271 (the cusp/peripheral structure), B285 (the ±π/6 sign).
