# K004 — The figure-eight knot, Dehn filling, and A-polynomials

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). Nothing here promotes to `../CLAIMS.md`; never a premise in a proof.

## The figure-eight complement as a once-punctured-torus bundle

The **figure-eight knot** `4₁` is the simplest hyperbolic knot. Its complement `S³ ∖ 4₁` fibers over the circle with
fiber a **once-punctured torus** and monodromy the mapping class
```
   φ = [[2, 1], [1, 1]]  ∈ SL(2,ℤ)        (conjugate to LR = M_1² in the metallic notation).
```
This is the bridge between the knot and the metallic family (`K002`): the figure-eight monodromy is the **square of
the golden generator** `M_1` (B122's "fig-8 = golden²"). Because the fiber is a once-punctured torus, its fundamental
group is `F₂` and the trace map (`K001`) acts on its character variety; the knot's representations are the trace
map's `φ`-fixed points.

## Dehn filling

**Dehn filling** glues a solid torus back into the cusped manifold along a slope `p/q`, producing closed manifolds
`4₁(p/q)`. By **Thurston's hyperbolic Dehn surgery theorem** all but finitely many fillings stay hyperbolic, with
volumes increasing to the cusped volume `vol(4₁) = 2.0299…` from below. The exceptional (non-hyperbolic) fillings of
the figure-eight are a classical short list. In the character-variety picture the Dehn-filling representations are
distinguished fixed points of the trace map — the project's "third fixed-point class" (B106): **partially elliptic**,
with root-of-unity neutral eigenvalues, distinct from the trivial (= tower) and geometric (= torsion) classes.

## A-polynomials

The **A-polynomial** `A(M, L)` of a knot (Cooper–Culler–Gillet–Long–Shalen 1994) records, on the boundary torus, the
relation between the eigenvalue `M` of the meridian and the eigenvalue `L` of the longitude across all
`SL(2,ℂ)` characters — it is the defining polynomial of the projection of the character variety to the
peripheral `(M, L)`-plane. For the figure-eight it is the well-known
```
   A(M,L) = −L + L M² + M⁴ + 2M⁶ + M⁸ + L M⁶ + L M¹⁰ − L² M⁶ ,   (up to normalization)
```
the textbook example. `B67` reproduces it **exactly** as the trace-map fixed-point locus.

## Degree = rank: `L = (−1)^{n−1} M^n`

Pushing to higher rank, the project's signature peripheral relation is **"degree = rank"**: at the appropriate
boundary-unipotent / Dehn-filling representation the longitude eigenvalue is the meridian eigenvalue raised to the
rank,
```
   L  =  (−1)^{n−1} M^n        (equivalently the longitude class = char(M^n), B83/B89).
```
This has two readings that the project keeps separate (P005): a **spectral law** (`char(M^n)` is always a tower
factor, `μ_n = 1` for all `n` — `K003`) and a **geometric state** (an actual irreducible Dehn-filling representation
with `L = M^n`, which exists only for `n ∈ {3,4}`; B95/B119/B153 show the principal spectrum — forced *given* the
mult-(n−2) ansatz — degenerates at `n=5`: a principal/Dehn-filling rep has the boundary element of **finite order**
⟹ semisimple ⟹ `A²=I` ⟹ reducible, so **no irreducible principal rep at n=5**, PROVEN).
`M⁴ = L` is proved symbolic-exact over `ℚ(ω)` at `SL(4)` (B89); the **rank-stratified** picture (genuine
component at n=3, slice at n=4 — n=3 also now exact over F_p, n=4 over ℚ(ω) — absent at n=5) is **B153** (V142–V145),
which also corrected an earlier numerical "n=5 0/120 no-irreducibles" claim (non-ss irreducibles *do* exist but
carry no degree=rank relation).

## How the project uses it

- `B67`/`B71` — the figure-eight A-polynomial / A-variety from the trace map (`SL(2)`, `SL(3)`).
- `B83`/`B89` — the A-polynomial **family** `L = (−1)^{n−1} M^n` and the symbolic-exact `M⁴ = L`.
- `B106` — the Dehn-filling fixed-point class (the third class), partially elliptic.
- `B123` — `4₁` is the **unique arithmetic knot complement** (Reid 1991), shape `e^{iπ/3}`, trace field `ℚ(√−3)`
  (`K009`). **Reid's uniqueness is about *knots* and does not extend to bundles:** the metallic `R^m L^m` are
  once-punctured-torus *bundles*, and B125 finds **two** of them arithmetic — `m=1` (`ℚ(√−3)`) and `m=2` silver
  (`ℚ(i)`); `m=2` is necessarily *not* a knot, confirming Reid's scope.

## What this is and is not

The figure-eight complement is a *3-manifold*; its A-polynomial and Dehn fillings are *low-dimensional topology*. The
3d-3d correspondence (`K006`) makes the character variety a SUSY moduli space, but the firewall stands: this is knot
theory, not fundamental physics.

**Anchors:** B67/B71 (A-polynomial / A-variety), B83/B89 (degree=rank, `M⁴=L`), B106 (Dehn-filling class), B123/V112
(arithmeticity). External: Cooper–Culler–Gillet–Long–Shalen (A-polynomial, 1994); Thurston (hyperbolic Dehn surgery);
Reid 1991 (the figure-eight is the unique arithmetic knot); Heusener–Muñoz–Porti (the `SL(3)` character variety,
1505.04451).
