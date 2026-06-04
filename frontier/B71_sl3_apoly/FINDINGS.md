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

**Banked result:** the SL(3) figure-eight character variety, presented as `Fix(T_1²)` in fiber trace
coordinates, has **exactly three 2-dimensional components, the geometric one containing the Sym² lift
of the SL(2) holonomy** — reproducing the published HMP/Falbel structure from the trace map. Labeled
**computer-assisted (exact symbolic decomposition + offline Sym² numerics)**, structural match to the
literature, not a literal coordinate-ideal identity. Proven core P1–P16 untouched.
