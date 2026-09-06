# B1291 — THE PARITY THEOREM: 3 is EXCLUDED on a one-cusped manifold, the escape is ≥2 cusps, and one of my own closures was VACUOUS

**Verdict: NEGATIVE** — the sharpest chirality statement yet, **and a specification rather than an
obituary**: the obstruction is the **cusp count**, not the arithmetic, so the way out keeps every
structure the programme has derived.

## 1. THE THEOREM

For an affine map `z ↦ Az + b` of T², the fixed-point count is **|det(A − I)|, independent of b**,
and `det(A − I) = det A − tr A + 1` identically. Finite order in GL(2,ℤ) therefore bounds it:

```
finite-order (det, tr, det(A-I)) classes: [(-1,0,0), (1,-2,4), (1,-1,3), (1,0,2), (1,1,1), (1,2,0)]
reachable |Fix| = {0, 1, 2, 3, 4}     <- 3 comes from (det 1, tr -1): the ORDER-3 ROTATION
```

So **3 is algebraically reachable.** The geometry forbids it:

> **PARITY THEOREM.** `Fix(g)` of an orientation-preserving finite-order isometry of a hyperbolic
> 3-manifold is a union of closed geodesics (no ends) and properly embedded geodesic **lines** (two
> ends each). With exactly **one** cusp, every end lands in that cusp, so
> **|Fix(g) on the cusp torus| = 2 · (#fixed geodesic lines) — EVEN.**

**Hence |Fix| = 3 is impossible for any one-cusped manifold: three ends in one cusp is odd.**

Verified on this bench over the census (`verification/parity.py`):

```
ONE-cusped, 1200 manifolds:  |Fix| sets {(0,4): 1196, (0,): 4}      ODD violations: 0
m004 itself:                 Sym = D4, order 8, |Fix| in {0, 4}
```

**m004 is one-cusped. So the generation count 3 can never come from its cusp — not absent, EXCLUDED.**

## 2. THE CONTROL FIRES — which is what makes it a specification

```
>=2 cusps:  |Fix| values {0:575, 1:4, 2:5, 3:5, 4:575}
witnesses:  m202 (2 cusps) realises BOTH 1 and 3;  m125 (2 cusps) realises 2
```

**3 is realised the moment there are two cusps.** The criterion is not vacuous, and the obstruction
is located exactly: **the cusp count.** A second control from the fan-out, in the same direction:
**s960** is one-cusped with a genuine ℤ/3 symmetry, and its order-3 elements act on the cusp as
**free translations** — precisely what parity demands.

## 3. THE ESCAPE, NAMED — leave the knot, keep the field

**E₆ does not come from the cusp count.** B727 forces it through **ℚ(√−3)**, and the **invariant
trace field is a commensurability invariant**. Therefore:

> **A multi-cusped manifold commensurable with m004 keeps ℚ(√−3), keeps 2T, keeps E₆ — and lifts the
> parity obstruction.**

That is the next computation, and it is object-intrinsic rather than a free choice.

> ### ⚠ RE-SCOPED AT B1292 (2026-09-06), SAME DAY, BY THIS SEAT — READ THIS BEFORE USING §3
>
> The computation was run. **The hatch is SATISFIABLE — m202 is a witness** (2 cusps, `vol = 4·V_tet`,
> hexagonal cusps, **96 surjections onto 2T**, four isometries with `|Fix| = 3` on both cusps; the
> mechanism is the **cusp shape**, m004's being rectangular and admitting only ±1). **But this hatch
> names the WRONG OBSTRUCTION.** `χ(M) = 0` and `χ(∂M) = 0` for **every** cusped manifold at **any**
> cusp count — every boundary component is a flat torus — verified at 1, 2 and 4 cusps. So
> `net chirality = −χ(∂⁺M) = 0` **survives the move**. **`|Fix| = 3` and `χ(∂⁺M) ≠ 0` are different
> quantities and m202 supplies only the first.** Parity was real but **not binding**; **flatness is
> binding, and it is cusp-count-independent** — as §5 of this very arc already said.
>
> **What §3 actually opens:** an **order-3 symmetry acting on the boundary inside ℚ(√−3)**, which the
> programme had nowhere. **It is not a route to net chirality. Do not read it as one.** See **B1292**.

## 4. WHAT I GOT WRONG — a vacuous criterion, by my own standing rule

An earlier draft of this arc closed the corner/cone-point case by computing **χ_orb = 0 for all 17
wallpaper quotients**. An adversarial verification lane found the fault, and it is worse than
"unjustified":

> **χ_orb(T²/G) = χ(T²)/|G| = 0 identically for every finite G. The criterion CANNOT FAIL, so it
> decides nothing.**

That is an **MB12 vacuity failure** against this repo's own written rule (*"before using a target,
check it can ever fail"*) — and my non-vacuity control was mis-aimed: I showed the *formula* returns
nonzero on hyperbolic and spherical inputs, never that the *criterion as applied* could fail on the
Euclidean inputs it was actually ranging over. **A control must vary what the argument varies.**

And the convention question I never asked has an answer: the χ that enters is the **ordinary χ of the
underlying topological space**, not χ_orb — which is **excluded on integrality alone** (for the cone
orbifold `D²(n)` the index is 1 for every n while `χ_orb = 1/n` is not an integer, so χ_orb cannot be
the index of any operator).

**The conclusion survived; the argument did not.** `verification/orbifold.py` is retained because its
computations are true, but it is **not** a closure and is labelled as the refuted step.

## 5. WHAT DOES CLOSE, and how

| closure | status |
|---|---|
| **Subsurfaces** — χ(∂⁺M) ≠ 0 **iff** the dividing set has a null-homotopic component; every canonical dividing set (slopes, meridian, longitude, geodesic cores, horospherical curves) is essential | **STANDS** (`dividing_set.py`) |
| **Symmetry** — 54 affine involutions of T², exactly three fixed-set types (whole/empty, 4 isolated points, essential circles), **never inessential** | **STANDS** (`involutions.py`); confirmed on m004 exactly: only 2 of 8 isometries have fixed points, 4 each, and **no orientation-reversing isometry has any**, so no fixed circles |
| **Corners/orbifolds** — χ_orb = 0 for all 17 quotients | **VACUOUS, withdrawn as an argument** (§4) |
| **Corners/orbifolds, properly** | closed instead by **adversarial verification**: every nonzero candidate refuted, **never on arithmetic**, on (i) **genericity, E61** — χ(T²∖4pts) = −4 holds for **3994/4000** one-cusped census manifolds and equals **−2·(#tetrahedra)**; χ(\|O\|) = #cusps for 17 of 18; and (ii) **admissibility** — puncturing is 0-dimensional, a dividing set must be a closed 1-manifold, and quotienting the boundary forces quotienting the manifold |

## 6. THE JOIN THE CORPUS ALREADY HAD AND NEVER MADE

The absence sweep found this ground is **not virgin**, and the pieces were banked and unjoined:

- **B749 fork F2** already computes the closed cone spectrum `[2,2,2,2]` with χ_orb = 0 **and the
  punctured version χ_orb = −1/2** — *the record's own escape from zero is by puncturing at a cone
  point.*
- **B365** carries the half-period table indexed by exactly **0, ½, τ/2, (1+τ)/2** — the four points.
- **B366** carries a locked **puncture lemma** (SL(2,ℤ) fixes only the origin; the other three are one
  orbit).
- The pillowcase for m004's cusp was computed on a **2026-08-25 review branch**, in prose, and that
  half was never harvested while its order-96 flat-G₂ half became **B1084**.

**Never joined, never applied to the cusp.** Recorded here so the join exists.

## 7. Fences

1. The index formula remains **CITED, not derived** (B1290's fence).
2. The parity argument was **surfaced by a verification fan-out**; every number in §1–§2 is
   **re-computed on this bench** (`parity.py`, snappy 3.3.2), not accepted from it.
3. **The affine-conjugacy hypothesis is CITED** (finite-order self-homeos of T² are conjugate to
   affine maps); §1's algebraic half is exhaustive given it.
4. **This does not pay I-26.** Fourth restatement of its price, still **UNEARNED**.
5. **No identification is asserted between any computed number and a generation count.**
