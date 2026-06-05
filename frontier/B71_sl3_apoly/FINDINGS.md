# B71 — the SL(3) figure-eight character variety from the trace-map fixed locus (Track B, B0–B1)

**Date:** 2026-06-04. **Status:** exploratory, committed. Proven core P1–P16 untouched. Scripts:
`probe.py` (exact sympy + offline Sym² ground truth). Standalone character-variety mathematics; no
physics, no Origin claim. This is the first result of Phase-8 **Track B** — the SL(3) analogue of
B67 (which derived the figure-eight SL(2) A-polynomial exactly from the trace map).

## Setup — the SL(3) analogue of B67

The figure-eight complement is the once-punctured-torus bundle with monodromy `φ=[[2,1],[1,1]]=M²`.
On the **8 SL(3) trace coordinates** of the fiber `F₂=⟨a,b⟩` (B48: `x1..x8 = tr A, tr B, tr AB,
tr A⁻¹, tr B⁻¹, tr A⁻¹B, tr AB⁻¹, tr A⁻¹B⁻¹`), the induced trace map is `T_1²`, where `T_1`
(B48 `m=1`; `a↦ab, b↦a`) is

    T_1(x) = (x3, x1, x1·x3 − x4·x2 + x6, x8, x4, x5, x2, x4·x8 − x1·x5 + x7).

A fiber representation extends over the bundle **iff** its character is fixed by `T_1²` (then it is
conjugate to its `φ`-image, so a monodromy `t` exists) — exactly the B67 mechanism, now at rank 3.
So `Fix(T_1²)` **is** the SL(3) character variety of the figure-eight bundle.

## Result (exact)

**The fixed-locus ideal decomposes cleanly.** The eight equations `T_1²(x)=x` give four linear
identifications

    x3 = x2,   x8 = x5,   x6 = x4,   x7 = x1,

reducing to `(x1,x2,x4,x5)`, where the remaining ideal factors as

    (x1−x4)(x2−1) = 0,   (x1−x4)(x5−1) = 0,   + two cubics,

and decomposes **exactly into three components, each of dimension 2**:

| component | locus | type |
|---|---|---|
| **V0** | `{x1=x4, x2=x5}` — i.e. `(x1,x2,x2,x1,x2,x1,x1,x2)` | **geometric** (contains Sym²) |
| **W1** | `{x1=x4=1}` — `(1,q,q,1,p,1,1,p)` | trace-=1 / Dehn-filling-type |
| **W2** | `{x2=x5=1}` — `(p,1,1,q,1,q,p,1)` | trace-=1 / Dehn-filling-type |

(The case split is exact: from `(x1−x4)(x5−1)` and `(x2−x5)(x4−1)`, every solution is `x1=x4 ∧ x2=x5`
[→V0], or `x1=x4=1` [→W1], or `x2=x5=1` [→W2]; the cubic generator vanishes on each.)

**Ground truth (offline, exact).** `Sym² : SL(2,C)→SL(3,C)` of the B67 figure-eight SL(2) holonomy
family lands on **V0** to `~1e-14` over 12 sampled points (because `tr Sym²(g)=tr Sym²(g⁻¹)=tr(g)²−1`
forces `x1=x4` and `x2=x5`). This is the discrete-faithful geometric rep and its character-curve
deformations — no Magma/Sage/internet needed. `Sym²` of the bundle rep is a bundle rep (functoriality),
so it is `T_1²`-fixed; this also **numerically confirms `T_1²` is the figure-eight monodromy action**.

## Match to the published SL(3) figure-eight character variety

This reproduces the **component structure** of the two independent published computations:

- **Heusener–Muñoz–Porti** (arXiv:1505.04451): the SL(3) figure-eight character variety has
  irreducible part = **3 components, each dimension 2** (`V0,V1,V2`); the geometric one `V0` contains
  `Sym²(discrete-faithful SL(2) holonomy)`; `V1,V2` come from the `±3` Dehn fillings and contain no
  faithful reps. **Our `Fix(T_1²)` reproduces this exactly:** 3 components, each dim 2, the geometric
  one (our V0) containing the Sym² family; our W1/W2 (`tr=1` loci) are the Dehn-filling-type analogue.
- **Falbel–Guilloux–Koseleff–Rouillier–Thistlethwaite** (arXiv:1412.4711): the deformation variety
  is 3 components (`D1` geometric, `D2/D3` Dehn-filling, with clean A-variety forms `L³=M`, `L³M=1`).

## Honest scope

- HMP/Falbel coordinatize the **knot group** `⟨S,T⟩`; here the coordinates are the **fiber group**
  `⟨a,b⟩`. The match claimed is **structural and dictionary-free** — component *count*, *dimension*,
  and the Sym²-geometric identification — **not** a literal coordinate-ideal equality. A full
  fiber↔knot trace dictionary (`x1..x8 ↔ y,ȳ,z,z̄,α,ᾱ,β,β̄`) is a separate identification, not done
  here.
- The peripheral **eigenvalue "A-variety"** (build the monodromy `t`, read meridian `eig(t)` and
  longitude `eig[A,B]`, literal-match the Dehn-filling forms `L³=M`/`L³M=1` and check geometric
  membership) is the **B2–B3 continuation** — it needs an explicit SL(3) `(A,B)` realization off the
  Sym² curve (Lawton). Not claimed here.

**Banked result (B0–B1):** the SL(3) figure-eight character variety, presented as `Fix(T_1²)` in fiber
trace coordinates, has **exactly three 2-dimensional components, the geometric one containing the Sym²
lift of the SL(2) holonomy** — reproducing the published HMP/Falbel structure from the trace map.
Labeled **computer-assisted (exact symbolic decomposition + offline Sym² numerics)**, structural match
to the literature, not a literal coordinate-ideal identity. Proven core P1–P16 untouched.

## B2–B3 — the peripheral eigenvalue A-variety (`peripheral.py`)

The genuine B67 analogue: build explicit SL(3) reps on the fixed locus, derive the boundary
(meridian/longitude) eigenvalue data, and compare to the published **eigenvalue A-variety**.

- **B2 — explicit realization.** `realize(coords)` returns `(A,B) ∈ SL(3,C)` with the prescribed 8
  trace coordinates: `A = diag` of the roots of `z³−x1·z²+x4·z−1`; `B` solved from the 6 trace
  conditions + `det B=1` + 2 gauge conditions (fixing the diagonal torus that stabilizes `A`), with
  the adjugate (`= B⁻¹` at `det 1`) keeping every condition polynomial. **Round-trips to `<1e-7` on
  all three components**, `cond(B) ~ O(1–100)` (well-conditioned).
- **B3 — monodromy and peripheral eigenvalues.** `t ∈ SL(3,C)` with `tA t⁻¹=φ(A)`, `tB t⁻¹=φ(B)`
  (`φ: a↦a²b, b↦ab`, the figure-eight monodromy) via the **18×9 Kronecker null-space solve** (the
  rank-3 analogue of B67's `kron` construction), residual `<1e-9`, `det t=1`. Longitude = eigenvalue
  ratios of `[A,B]`; meridian = eigenvalue ratios of the **genuine commuting meridian `μ = w⁻¹t`**
  (see below) — the PGL(3) "decorated" coordinates (middle eigenvalue normalized to 1, as in Falbel).

- **B3 — the genuine peripheral meridian `μ = w⁻¹t` (commutativity fix).** A torus cusp's peripheral
  subgroup is abelian, so the meridian must commute with the longitude `[a,b]`. The bare monodromy
  generator `t` does **not** commute with `[A,B]` (as is already true at SL(2) in B67). The fix: a
  once-punctured-torus mapping class fixes `[a,b]` **up to conjugacy**, `φ([a,b]) = w·[a,b]·w⁻¹`
  (verified by free-group reduction: `w=a` for `φ:a↦a²b`, `w=aba` for `φ:a↦aba`). Then
  `μ = w⁻¹t` satisfies `μ[a,b]μ⁻¹ = w⁻¹(w[a,b]w⁻¹)w = [a,b]` — it **commutes** with the longitude.
  Verified numerically: `‖[μ,[A,B]]‖ ~ 1e-10` on **W1, W2, and V0**. Crucially **`eig(μ)=eig(t)`**
  (`~1e-11`): `μ` is itself a monodromy-lift (`μAμ⁻¹=ABA`), and meridian eigenvalues are a bundle
  conjugacy-invariant — so the A-variety eigenvalue data is **unchanged**; `μ` fixes the commutativity,
  not the spectrum. **The meridian↔longitude transpose persists** under `μ`, so it is a genuine naming
  convention (which peripheral curve is the meridian), not an artifact — our naming is the
  geometrically-standard fibered-knot one (meridian = fibration generator, longitude = fiber boundary).

**Pipeline validation (geometric branch).** For a `Sym²` rep, `monodromy(Sym²A, Sym²B)` reproduces
`Sym²` of the B67 SL(2) monodromy: `eig(t) = {μ², 1, μ⁻²}` (`μ = eig` of the SL(2) monodromy) to
`~1e-13`. This confirms the realize→monodromy→eigenvalue pipeline is correct against B67 ground truth.

**LITERAL A-variety match (Dehn-filling components) — the SL(3) Cooper–Long moment.** On the two
trace-=1 components the trace-map peripheral eigenvalues satisfy the **published Falbel et al.
(arXiv:1412.4711 §4.1) A-variety relations**, with the meridian↔longitude label transposed:

| component | trace-map relation | Falbel | residual (median, 16 pts / 2 seeds) |
|---|---|---|---|
| **W1 = D2** | `M³ = L`, `M*³ = L*` | `L³ = M`, `L*³ = M*` | `~4e-10` |
| **W2 = D3** | `M³L = 1`, `M*³L* = 1` | `L³M = 1`, `L*³M* = 1` | `~3e-10` |

(`M` = eigenvalue ratios of the genuine commuting meridian `μ=w⁻¹t` (fibration generator;
`eig(μ)=eig(t)`), `L` = ratios of the fiber boundary `[A,B]`. The transpose is a convention choice of
which peripheral curve is named meridian; the corrected meridian `μ` commutes with `[A,B]`.)

**Geometric component V0 (= Falbel D1).** No tidy closed A-variety form exists (their eliminated
Gröbner basis is 141 polynomials), so no literal match is expected there; the Sym²-shadow validation
is the geometric-branch check.

## P1 — the Dehn-filling A-variety as an EXACT scalar-matrix identity (`symbolic_dehn.py`)

V44's relations are numerical (magnitude-sorted ratios, ~1e-10). V46's commutativity (`μ` and `[A,B]`
commute) gives an **exact reformulation** with no eigenvalue extraction or pairing ambiguity — since a
commuting pair is simultaneously diagonalizable, `M³=L` for all paired ratios is *exactly*

| component | exact criterion |
|---|---|
| **W1 = D2** (`M³=L`) | `[A,B] = c·μ³` for a scalar `c`  ⟺  `[A,B]·μ⁻³` is a scalar matrix |
| **W2 = D3** (`M³L=1`) | `[A,B]·μ³ = c` for a scalar `c`  ⟺  `[A,B]·μ³` is a scalar matrix |

So the Dehn-filling A-variety relation **is** the statement that one explicit matrix is scalar —
checkable without roots. Confirmed: the scalar-deviation is `~3e-10` (double, both components, 16
pts/2 seeds), and on **W1 to 50 digits** — `A=diag(1,i,−i)` fixed, `B(p,q)` solved exactly over `ℚ(i)`
(sympy), the monodromy null vector + scalar criterion evaluated in mpmath — **`M³=L` holds to `~1e-43`
at 12 exact rational points** (an exact-grade upgrade of V44 on W1; the full symbolic identity in
`(p,q)` is bottlenecked by radical realizations, so the high-precision exact-point certification is the
practical exact form). Ledger **V47**.

**Banked result (B2–B3):** an explicit SL(3) realization + the Kronecker monodromy construction
derive the peripheral eigenvalue A-variety from the trace-map fixed locus; the **Dehn-filling
components literally reproduce Falbel et al.'s published A-variety relations `L³=M` / `L³M=1`**
(meridian↔longitude transposed) to `~1e-10`, with the construction independently validated on the
geometric branch by the Sym² shadow. The **genuine peripheral meridian `μ=w⁻¹t` commutes with the
longitude `[A,B]`** (the correct abelian cusp pair; `eig(μ)=eig(t)`, so the relations are unchanged),
and the transpose is a genuine naming convention. This is the genuine SL(3) analogue of B67's exact
Cooper–Long match, on the Dehn-filling components. Labeled **computer-assisted (exact component
structure B1 + numerical realization/monodromy B2–B3, cross-validated against the published
A-variety)**. Proven core P1–P16 untouched.
