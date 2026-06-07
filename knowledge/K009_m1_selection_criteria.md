# K009 — Why m=1 is special: three independent selection criteria

> **Explainer** (`GOVERNANCE.md`). Self-contained; cites the project's own results by `B`/`V` number (no re-proof)
> and external facts to the literature. Nothing here promotes to `../CLAIMS.md`; never a premise in a proof.

## The question

The metallic family `M_m = [[m,1],[1,0]]` (`m ≥ 1`) is a *family* — the "not-nothing" condition cuts out the family,
not a member (`../philosophy/P000`). Yet `m=1` (the golden mean / the figure-eight) keeps being singled out. Selecting
a member requires *importing extra structure* beyond "is a metallic unit." There are **three independent** such
selections — three different pieces of imported structure, each picking `m=1`.

## The three criteria

1. **The systole (a metric).** On the modular surface `H/GL(2,ℤ)`, each metallic `m` is a closed geodesic of length
   `2 log λ_m`; `m=1` is the **systole** — the shortest closed geodesic. Selecting `m=1` this way requires importing
   a *metric* (which "is a metallic unit" does not provide). Anchor: **B92** (the systole length computation, V76);
   `../philosophy/METALLIC_FOUNDATIONS.md`; the load-bearing one-liner is in `../speculations/S001` ("the systole,
   not amphichirality, selects `m=1`").

2. **The expansion threshold (the dynamics).** In the mapping-class group `M_m = (twist)^m · (swap)`, with both
   factors non-expanding (`|λ|=1`); the product is hyperbolic for `m ≥ 1`. So `m=0` (swap alone) is the static
   `|λ|=1` ground state, and `m=1` (golden) is the **threshold** where the twist–swap interaction first ignites
   expansion (the engine of the whole tower). Anchor: **B120** (the factorization); `../philosophy/P004` (the
   interpretation, "expansion is interaction-born").

3. **Arithmeticity (the number field).** The figure-eight complement has a *regular* ideal triangulation with shape
   `z₀ = e^{iπ/3}` (a primitive 6th root of unity, `z²−z+1 = Φ₆`), invariant trace field `ℚ(√−3)` — so it is
   **arithmetic**. By **Reid (1991)** the figure-eight is the *unique* arithmetic knot complement (and there are
   exactly two arithmetic once-punctured-torus bundles), so the `m ≥ 2` metallic manifolds are **not** arithmetic.
   Thus `m=1` is the unique metallic manifold that is both **simplest** (smallest volume / systole) and **most
   regular** (arithmetic / root-of-unity shape). Anchor: **B123** (the cyclotomic shape, computed); Reid 1991
   (cited). *Status:* **SUPPORTED** — the shape is computed in-house and Reid's theorem is cited; the `m ≥ 2`
   invariant-trace-field non-arithmeticity *computed via the arithmeticity criterion* is the **named confirmation
   step** (SnapPy/Magma — the repo has no trace-field classifier), so it is not yet `TESTED-POSITIVE`.

## A coincidence to note (an observation, not a connection)

The same `6th-root-of-unity / ℚ(√−3)` value appears in *two* places: the figure-eight's tetrahedron shape `e^{iπ/3}`,
**and** the non-void SL(2) trace-map Jacobian at `(0,0,0)` (char poly `λ³+1`, order 6, B122) — which sits at `κ=−2`,
the geometric/parabolic cusp (B69/B109). Both are `ℚ(√−3)` phenomena, consistent with the figure-eight's invariant
trace field. Whether this is a deep structural link or two manifestations of the same field is **open**; it is
recorded as an *observation*, not a banked connection.

## What this does not license

Three independent selections of `m=1` do not collapse the family to a member as a *theorem* — each imports extra
structure (a metric, a dynamical threshold, a number field), and `P000`'s point stands: the structure is the family,
and which member is "ours" is contingent on what one chooses to import. None of these touches the open problem (the
functorial `Sym(W)→trace-ring` construction; the `μ_d` two-sequence proof, B103/B122).

**Anchors:** B92/S001 (systole), P004/B120 (expansion threshold), **B123** (arithmeticity, V112), B69/B109 (the
`κ=±2` cusp), B121/B122 (the `det=−1` parity, the order-6 echo). External: Reid, *Arithmeticity of knot complements*
(1991).
