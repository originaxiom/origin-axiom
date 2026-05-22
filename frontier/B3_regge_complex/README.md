# Probe B3 — Figure-eight triangulation and the 4D Regge question

> **Speculative frontier work.** Logged observations, not claims
> (`../../GOVERNANCE.md` §5). Nothing here is promoted to `CLAIMS.md`.

## The question

`ROADMAP.md` probe B3, from the handoff document's "Step 5A":

> Build a 4D Regge complex by stacking figure-eight slices by the monodromy `A`,
> count its simplices, and move toward Regge calculus → Einstein.

## Findings (`probe.py`)

**[1] The 3D ideal triangulation — exact, standard.**
The figure-eight knot complement admits an ideal triangulation by **2 regular
ideal tetrahedra** (Thurston): 2 tetrahedra, 2 edge classes, 4 face classes,
1 cusp. Both tetrahedra have shape parameter `z = exp(iπ/3)`.

**[2] 3D Regge / gluing-equation check — exact, satisfied.**
In 3D Regge calculus curvature concentrates on edges. A regular ideal tetrahedron
has all six dihedral angles `π/3`. Six dihedral angles meet at each of the 2
edges, summing to `2π` — so the **Regge deficit per edge is 0**. The complete
hyperbolic structure is exactly the zero-deficit (flat-in-the-Regge-sense)
solution of the gluing equations. This is exact and checkable.

**[3] The 4D Regge complex — not a defined construction.**
A genuine 4D Regge complex requires: a 4-manifold; a triangulation by
4-simplices; 2-face (triangle) hinges where 4D curvature concentrates; a deficit
rule `δ(triangle) = 2π − Σ dihedral angles`; and the Regge action
`S = Σ_triangles (area · deficit)`.

The handoff's prescription — *"stack figure-eight slices by the monodromy A"* —
supplies **none** of these. The figure-eight complement is a 3-manifold; "stacking
slices by A" names no 4-manifold and no 4-cell. (The figure-eight is *already*
the mapping torus of the punctured torus under `A`; applying `A` again is not a
canonical route to a 4-manifold.)

## Honest verdict

B3 is a **clarifying result**:

- The **3D layer is solid** — the 2-regular-ideal-tetrahedron triangulation and
  the zero-deficit Regge edge equations are exact.
- The **4D step is undefined.** The handoff's "Step 5A" is not a construction;
  it is a wish. The path 5A → 5B → 5C → Einstein has an *undefined first step* —
  there is no 4-manifold to do Regge calculus on.

This bounds the frontier precisely: probes B1, B2, B3 each found that the
well-defined content is real and exact, while the bridge to 3+1 gravity rests, in
every case, on a step that is asserted but not constructed. That is the genuine
open problem (claims O1–O3) — and it is honest to say it is not a computation
away. No claim promoted.
