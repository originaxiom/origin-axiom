# K012 — The SL(n) tower is sealed in ℚ(√−3): SL(2) data in larger irreps

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). Nothing here promotes to `../CLAIMS.md`; never a premise in a proof. The
> bankable MATH of the tower-sealing arc (B129/V118).

## The question

The metallic trace-map tower (`K003`) lifts the SL(2) figure-eight Fibonacci datum into higher rank. The sharp
firewall question: does climbing to SL(3) (and beyond) produce **new content** — a genuine irreducible non-abelian
fixed point carrying **new arithmetic** — or is the tower the **single SL(2) datum re-expressed in larger irreps**?

## The principal embedding is SL(2) arithmetic in SL(3) clothing (B129, exact)

Push the figure-eight (m=1) SL(2) Fibonacci representation `A₂=[[1,1],[0,1]]`, `B₂=[[1,0],[−ω,1]]` with cusp shape
`ω = ½ + √−3/2 ∈ ℚ(√−3)` through the **principal embedding** SL(2)→SL(3) — the symmetric square `Sym²`, the embedding
the tower naturally produces (`K005`, the principal `SL(2)`). The result (verified symbolically):

- The pair is **irreducible as a representation**: the algebra it generates is all of `M₃` (dim 9), no invariant
  subspace. So "irreducible non-abelian rep" is **cleared** — and is therefore *not* the right bar for a physics
  bridge.
- **Every trace invariant lies in ℚ(√−3):** `trA = trB = 3` (unipotent), `trAB = ½ − (3√3/2)i`,
  `trA⁻¹B = 9/2 + (5√3/2)i`, `tr[A,B] = ½ + (3√3/2)i`. **No new field, no new generator, no new modulus.** The SL(3)
  trace ring is a **reparametrization** of the SL(2) Fibonacci data, not an enrichment.

## No off-sublocus fixed point escapes (B129, computer-assisted)

The SL(3) once-punctured-torus character variety is **4-dimensional** (vs SL(2)'s 2-dim). Off the SL(2)/`Sym²`
sublocus, does the metallic trace map fix a point with new arithmetic? Because the trace map is a **hyperbolic
horseshoe** (`K010`), its fixed points are **saddles** — forward iteration flees them, so one must **root-find** (not
iterate) for genuine fixed conjugacy classes via Lawton's 9 SL(3) trace coordinates (`K001`), `tcoords(A,B) =
tcoords(AB,A)` (the m=1 metallic monodromy `φ(A,B)=(AB,A)`, abelianizing to `M₁=[[1,1],[1,0]]`). A 15-seed scan of 427
converged off-sublocus fixed points has **maximum distance-to-ℚ(√−3) of 1.2e-6** — every point is in ℚ(√−3) to
numerical precision, with a clean gap to the `>1e-3` a genuine algebraic escape would require. The search lands
overwhelmingly on the reducible sublocus + degenerate trivial/central reps; the only genuine irreducible content is the
`Sym²` image. **The tower is sealed in ℚ(√−3).** (Strong computational result, m=1; not a theorem — the analytic
capstone is `../speculations/S031`.)

## The reading: the tower adds matrix size, not information

The SL(n) tower is the **single SL(2) Fibonacci datum** (field ℚ(√−3), one coupling) in successively larger irreps
`Sym^{n−1}`. It never learns a second arithmetic language — consistent with `K010`'s multichannel picture: `n`
channels, **one** coupling, no non-abelian gauge factor. This is the firewall confirmed **from inside the tower** (the
sixth direction; `../philosophy/P007`).

## The firewall statement, corrected

The metallic family produces **abelian × discrete**, never an irreducible **simple non-abelian** factor — *not* "rank
is always 1." A single bundle is one-cusped rank-1 abelian, but its finite **covers** are multi-cusped and rank-2
(silver `b++RRLL` degree-2 cover → `(cusps, free_rank)=(2,2)`); the extra cusps are **copies of one boundary torus**
permuted by the deck group, so `T[cover]` is a discrete gauging of copies of the rank-1 abelian `T[M]`, not a new
irreducible theory. Rank grows by covering, **only by replication** (this strengthens the `S029` rank-1 fence; same
lesson as the torsion `K-F`, B128).

## Method (two banked bugs — `REPRODUCIBILITY.md` SCAN)

Detecting "in ℚ(√−3)" needs care: (B1) the detector must accept **pure rationals** (`1 = 1+0·√−3`) and use a **small**
denominator bound (a large `limit_denominator` approximates any real, by Dirichlet, and would accept escapes too);
(B2) on a hyperbolic map the solver lands on **degenerate** fixed points whose slightly-off traces fake escapes — the
robust test is a **polished distance** (re-solve, then measure deviation, threshold ~1e-4). The figure-eight rep is
**unipotent** (`|eig|=1`), so eigenvalue modulus does not separate genuine content from trivial reps.

**Anchors:** B129/V118 (the result, the covers correction, the method bugs), B128 (`K-F`/`S029`, the fork this
answers), `K010` (the horseshoe/multichannel naming), `K011`, `K001`/`K005` (Lawton trace coordinates / the principal
SL(2)), `../speculations/S029` (the fence, strengthened), `S031` (the capstone), `../philosophy/P007` (the firewall,
sixth direction). External: Lawton (SL(3) trace coordinates, 2007); Damanik–Gorodetski (the horseshoe).
