# K009 — Why m=1 is special: the selection criteria

> **Explainer** (`GOVERNANCE.md`). Self-contained; cites the project's own results by `B`/`V` number (no re-proof)
> and external facts to the literature. Nothing here promotes to `../CLAIMS.md`; never a premise in a proof.
>
> **CORRECTED (B125/V114).** This entry previously claimed *three independent* `m=1` selections, with arithmeticity
> the third. New computational evidence (SnapPy, in-sandbox) shows **arithmeticity is a two-element selector
> `{m=1, m=2}`, not a unique `m=1` criterion** — see criterion 3. Two criteria (systole, expansion threshold) still
> uniquely select `m=1`; arithmeticity selects golden **and** silver. `m=1` is therefore the **most-selected** point,
> not the unique arithmetic one.

## The question

The metallic family `M_m = [[m,1],[1,0]]` (`m ≥ 1`) is a *family* — the "not-nothing" condition cuts out the family,
not a member (`../philosophy/P000`). Yet `m=1` (the golden mean / the figure-eight) keeps being singled out. Selecting
a member requires *importing extra structure* beyond "is a metallic unit." Below are the imported structures and what
each actually selects: **two** pick `m=1` uniquely; **one** (arithmeticity) picks `{m=1, m=2}`.

## The criteria

1. **The systole (a metric) — uniquely `m=1`.** On the modular surface `H/GL(2,ℤ)`, each metallic `m` is a closed
   geodesic of length `2 log λ_m`; `m=1` is the **systole** — the shortest closed geodesic. Selecting `m=1` this way
   requires importing a *metric* (which "is a metallic unit" does not provide). Anchor: **B92** (the systole length
   computation, V76); `../philosophy/METALLIC_FOUNDATIONS.md`; the load-bearing one-liner is in `../speculations/S001`
   ("the systole, not amphichirality, selects `m=1`").

2. **The expansion threshold (the dynamics) — uniquely `m=1`.** In the mapping-class group `M_m = (twist)^m · (swap)`,
   with both factors non-expanding (`|λ|=1`); the product is hyperbolic for `m ≥ 1`. So `m=0` (swap alone) is the
   static `|λ|=1` ground state, and `m=1` (golden) is the **threshold** where the twist–swap interaction first
   ignites expansion (the engine of the whole tower). Anchor: **B120** (the factorization); `../philosophy/P004` (the
   interpretation, "expansion is interaction-born").

3. **Arithmeticity (the number field) — a two-element selector `{m=1, m=2}`.** The orientable metallic members are
   the once-punctured-torus bundles `M_m² = R^m L^m` (B125 §1). Computing the invariant trace field `kM` directly
   (SnapPy, by the Maclachlan–Reid criterion: arithmetic ⟺ `kM` imaginary quadratic + traces integral) gives:
   **`m=1` golden is arithmetic** (`kM = ℚ(√−3)`, shape `e^{iπ/3}`, `z²−z+1 = Φ₆`) **and `m=2` silver is arithmetic**
   (`kM = ℚ(i)`, roots `1±i`); **`m ≥ 3` are non-arithmetic** (`kM` not imaginary quadratic). So arithmeticity
   selects **two** members, not one — and they sit in *different* Bianchi families (`ℚ(√−3)` vs `ℚ(i)`, not
   commensurable), the **two** arithmetic once-punctured-torus bundles. Anchor: **B125** (V114, **TESTED-POSITIVE**,
   SnapPy in-sandbox); this **corrects B123/K009**, whose `SUPPORTED` "unique `m=1` arithmetic" reading mis-applied a
   *knot* theorem (Reid 1991) to *bundles* — see the next note.

   *Reid 1991 stands (preserved).* The figure-eight is the unique arithmetic *knot* complement in `S³` — a statement
   about **knots**. The `m ≥ 2` metallic manifolds are **bundles**, generally not knot complements; `m=2` being
   arithmetic confirms Reid's scope (`m=2` is necessarily not a knot, else a second arithmetic knot), it does not
   contradict it.

## A coincidence to note (an observation, not a connection)

The same `6th-root-of-unity / ℚ(√−3)` value appears in *two* places: the figure-eight's tetrahedron shape `e^{iπ/3}`,
**and** the non-void SL(2) trace-map Jacobian at `(0,0,0)` (char poly `λ³+1`, order 6, B122) — which sits at `κ=−2`,
the geometric/parabolic cusp (B69/B109). Both are `ℚ(√−3)` phenomena, consistent with the figure-eight's invariant
trace field. Whether this is a deep structural link or two manifestations of the same field is **open**; it is
recorded as an *observation*, not a banked connection.

## What this does not license

These selections do not collapse the family to a member as a *theorem* — each imports extra structure (a metric, a
dynamical threshold, a number field), and `P000`'s point stands: the structure is the family, and which member is
"ours" is contingent on what one chooses to import. `m=1` is the **most-selected** point (two unique criteria + one
of the two arithmetic members), but "most-selected" is not "uniquely determined." None of these touches the open
problem (the functorial `Sym(W)→trace-ring` construction; the `μ_d` two-sequence proof, B103/B122).

**Anchors:** B92/S001 (systole), P004/B120 (expansion threshold), **B125** (arithmeticity corrected: the two-element
selector `{m=1,m=2}`, V114), B123/V112 (the original `SUPPORTED` claim, now corrected), B69/B109 (the `κ=±2` cusp),
B121/B122 (the `det=−1` parity, the order-6 echo). External: Maclachlan–Reid, *The Arithmetic of Hyperbolic
3-Manifolds* (the arithmeticity criterion); Bowditch–Maclachlan–Reid 1995 (**three** cyclic commensurability classes
of arithmetic once-punctured-torus bundles — so "the two arithmetic members of the `R^m L^m` family" is a
family-restricted statement, *not* the global count; the figure-eight `m004` and its sister `m003` are two bundles in
one `ℚ(√−3)` class); Reid, *Arithmeticity of knot complements*
(1991) — the unique arithmetic *knot* (preserved; knots ≠ bundles).
