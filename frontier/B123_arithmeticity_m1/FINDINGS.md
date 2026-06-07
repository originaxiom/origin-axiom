# B123 — m=1 arithmeticity: a third independent selection criterion for the figure-eight

The figure-eight complement (golden, m=1) has a **regular ideal triangulation** with shape `z₀ = e^{iπ/3}` — a
primitive **6th root of unity** (`z²−z+1 = Φ₆`) — so its invariant trace field is `ℚ(√−3)` and it is **arithmetic**.
By **Reid (1991)** the figure-eight is the *unique* arithmetic knot complement (and there are exactly two arithmetic
once-punctured-torus bundles), so the **m≥2** metallic manifolds are **not** arithmetic. This gives a third
independent reason m=1 is special:

> the figure-eight is the unique metallic manifold that is both **simplest** (smallest volume / systole, B92) **and
> most regular** (arithmetic / root-of-unity shape) — a selection criterion **independent of** the systole and the
> expansion threshold.

Standalone arithmetic geometry; no physics; nothing to `CLAIMS.md`; the `ρ_n`/Sym-`μ_d` proof stays the prize;
P1–P16 untouched.

## The three independent m=1 selection criteria

1. **The systole** (B92/V76; `philosophy/METALLIC_FOUNDATIONS`, S001): m=1 is the shortest closed geodesic
   `2 log λ_m` on `H/GL(2,ℤ)`.
2. **The expansion threshold** (P004/B120): `m=0` is the static `|λ|=1` swap; m=1 is the first interaction
   (`M_m=(twist)ᵐ·(swap)`) that ignites the hyperbolic tower.
3. **Arithmeticity** (this): m=1 has the cyclotomic shape `e^{iπ/3}` and trace field `ℚ(√−3)` — arithmetic; m≥2 are
   not (Reid 1991).

## Status / honest scope (do NOT overstate)

| layer | content | strength |
|---|---|---|
| **computed in-house** | the cyclotomic shape `z²−z+1=Φ₆`, root `e^{iπ/3}`; the order-6 echo at the geometric cusp | verified (this probe) |
| **cited (Reid 1991)** | the figure-eight is the *unique* arithmetic knot; m≥2 metallic manifolds are non-arithmetic | literature |
| **SnapPy/Magma-gated** | the m≥2 invariant-trace-field non-arithmeticity *computed via the arithmeticity criterion* | the named **confirmation step** (the repo has no trace-field classifier) |

**Banked `SUPPORTED`, NOT `TESTED-POSITIVE`** — the in-house shape + Reid's theorem support it; the trace-field
computation is the gated confirmation.

## The order-6 echo — an OBSERVATION, not a connection

The `(0,0,0)` non-void Jacobian spectrum (B122's `sym_tower_is_void_specific`: char poly `λ³+1` = `{−1, e^{±iπ/3}}`,
6th roots, `DT⁶=I`) sits at **κ = −2, the geometric/parabolic cusp** (B69/B109, the complete hyperbolic structure).
So the geometric cusp's Jacobian spectrum is the *same* `e^{iπ/3}` / `ℚ(√−3)` as the tetrahedron shape. Both are
`ℚ(√−3)` phenomena — consistent with the figure-eight's invariant trace field. **Whether this is a deep structural
link or two manifestations of the same field is itself open**; recorded as an observation, **not** a banked
connection (per the verify-don't-trust caveat).

## Cross-reference (not a new finding)

The **`det=−1` middle eigenvalue = −1** (vs `+1` at `det=+1`) is the proved **B121** parity (the external `det=−1`
`GL(2,ℤ)`-rep / the odd-`Sym^d` obstruction), already re-derived via fig-8 = golden² (B122). An **asset, not a
kill** — cross-reference B121/S024.

**Ledger:** V112 (`SUPPORTED`, scoped). **Reuses:** `B122.sym_tower_is_void_specific`. **Anchors:** B92/S001
(systole), P004/B120 (expansion), B69/B109 (κ=−2 cusp), B121/B122 (the det=−1 parity). External: Reid 1991
(arithmeticity of knot complements).
