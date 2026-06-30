# B298 — The figure-eight does not force three generations (the degree-2 obstruction)

**Status: banked (frontier). A forced negative, cross-chat convergent and verified; nothing to `CLAIMS.md`.** From
the cross-chat SM-from-axiom attempt (Chat-1 + Chat-2, 2026-06-30). The three seats *appeared* to disagree about
generations; **verified, they agree** — and the resolution is a clean, falsifiable result.

## The apparent disagreement, resolved
- **Chat-1:** "3 generations from the Z₃×Z₃ orbifold (3 fixed tori)."
- **Chat-2:** "3 is not in the object."
- **This session's computation (the bridge, B299):** the orbifold's `(θ,φ)` acts on the 27 as **9 free orbits of 3 —
  the trinification triality**; the doublet-triplet split is *external* (needs a color choice), and the orbifold
  itself is a heterotic input. Chat-1 even labeled its "3" *"natural not forced."*

→ **They agree: the object does not force three generations.** The orbifold-3 is an external input; the object's own
matter multiplicities are 1 or 2.

## The obstruction (the unifying reason)
The figure-eight's invariant trace field is **`ℚ(√−3)`, a degree-2 field with Galois group ℤ/2** (verified here:
`x²−x+1`, disc `−3`). Its natural multiplicities are therefore **1 (fixed) or 2 (conjugate pair)**. The number **3
appears everywhere as a *value*** — dimension 3, level `k=3`, trace 3, ramified prime 3, E₆-center ℤ/3 — **but never
as a matter *multiplicity***, because a multiplicity of 3 needs a **cubic** structure and `4₁` is **quadratic
everywhere** (trace field, tetrahedron shape `x²−x+1`, A-polynomial flavor, Galois ℤ/2).

## Seven routes, all 1 or 2 (never 3)
| route | multiplicity |
|---|---|
| H¹ / flat-connection components | 1 |
| ideal tetrahedra | 2 |
| **3-fold covers of m004 (SnapPy)** | **1** (`H₁ = ℤ/4 + ℤ/4 + ℤ`) |
| SU(3)_family in SU(6) (E₆⊃SU(6)×SU(2)) | 1 (one 27 = one generation + exotics, B280) |
| μ₃ / E₆-center ℤ/3 on the 27 | 1 (scalar, Schur — uniform) |
| 𝔽₃-unipotent `(x−1)³` on the 27 | 1 (scalar on irreducible); non-central → 9+9+9 *wrong size* (B299) |
| trace-map / A-polynomial fixed points | 2 (geometric + conjugate) |

They all failed *for the same reason* — they tried to extract a 3-count from a 2-structure.

## The cubic-carrier conjecture (bankable, falsifiable)
> **Three generations require a knot/manifold with a *cubic* invariant trace field; the figure-eight (degree 2) is
> structurally a one-generation object.** The three-generation carrier is a different, degree-3 object.

This converts "we can't get 3" into a *direction*: "3 lives on a cubic-trace-field knot — go find it." And it explains
why all seven routes failed at once.

## Where it lands
A forced negative that **sharpens B292** (multiplicity tripartite — this says *which* multiplicities, and why not 3)
and **B282** (the arithmetic atom — the degree-2 field is the obstruction). It corrects the "SM at the seam" frame,
which had been *mis-listing* "the generation count 3" as an open external input — it's a forced negative, and the
carrier is external *and degree-3*.

## The fence
Pure arithmetic + a SnapPy cover count; a forced negative about matter content. The cubic-carrier statement is a
**conjecture** (clearly labeled). Nothing to `CLAIMS.md`.

`generation_obstruction.py` (sage-python: the 3-fold cover count) · `verdict.py` (pyenv; degree-2 re-check + the
seven-route table) · `tests/test_b298_generation_obstruction.py`. Related: `B282` (arithmetic atom), `B292`
(multiplicity tripartite), `B299` (the trinification triality / the 9+9+9), `B280` (one 27 = one generation).
