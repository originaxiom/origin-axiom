# B101 — the Hitchin-component reframing of V0 (the SL(3,ℝ) higher-Teichmüller picture)

**Status: `computer-assisted` (+ one `dead` negative, one `open` direction).** Neutral higher-Teichmüller /
Lie theory; the Hitchin→Higgs→geometric-Langlands→N=4 chain is **cited context only** (firewalled to
`../../paths/philosophical/PHYSICS_RESONANCES.md`), never a claim. No Origin-core claim; proven core P1–P16
untouched. Script `probe.py`; test `tests/test_b101_hitchin_reframing.py`.

## The reframing
The project's geometric component **V0** (B71 — `Sym²` of the Fuchsian `SL(2,ℝ)` rep of the once-punctured
torus) **is the Fuchsian locus of the Hitchin / Fock–Goncharov positive component of the `SL(3,ℝ)` character
variety**. The principal embedding `PSL(2,ℝ)→SL(3,ℝ)` *is* the `Sym²` irrep, so `V0 = Sym²(Fuchsian)` is by
definition the Fuchsian locus, which Hitchin (1992) places in the Hitchin component. This is not analogy; it
is what the object is. Cite: **Hitchin 1992** (Teichmüller component); **Labourie** (Anosov representations);
**Fock–Goncharov** (positivity / punctured surfaces); **Choi–Goldman, Marquis** (convex projective
structures, incl. cusped). The payoff: there is *more* at `SL(3)` than V0 — the Hitchin component is
parameterized by a **quadratic + cubic differential**, and **V0 is the `{cubic = 0}` slice**.

## R1 — V0 = the Fuchsian locus (`STRUCTURAL` + `computer-assisted`)
- **Anosov hallmark** (`v0_anosov_hallmark`): on `Sym²` of the `(3,3,3)` Fuchsian rep, every non-peripheral
  word is **loxodromic** (3 distinct positive reals), the cusp `[a,b]` is **unipotent**, none complex; an
  **elliptic** generator gives a **complex** spectrum (the control — genuinely off V0).
- **`SO(2,1)` certificate** (`v0_so21_certificate`): the Ad-invariant symmetric form is **unique** (null dim
  1), signature **(2,1)** → `SO(2,1)`, invariance exact to ~1e-15. (This is the rigorous backbone of B97's
  `(2,1)` finding, now placed inside the Hitchin component.)

## R2 — the symmetric-space ladder + the spacetime-tower KILL (`dead`)
`ladder_signatures`: the principal `sl(2)` invariant form lands in **split real forms** — `Sp(k+1,ℝ)` (odd
`k`), `SO(p,p±1)` (even `k`):

```
 k=1 Sp(2,R)   k=2 SO(2,1) LORENTZIAN   k=3 Sp(4,R)   k=4 SO(3,2)   k=5 Sp(6,R)
 k=6 SO(4,3)   k=7 Sp(8,R)   k=8 SO(5,4)
```
**Lorentzian (one timelike) occurs at exactly `k=2` (`SO(2,1)`) and does NOT climb.** There is **no "tower of
spacetimes up the ranks"**: the principal `SL(2)` lands in split real forms whose maximally-balanced
signatures are structurally the *opposite* of Lorentzian. `Sp(4,ℝ)=Spin(3,2)` / `SO(3,2)` do appear (k=3,4 =
the real AdS₄ / 2+1-conformal groups) but their symmetric spaces are higher-rank (dim 6), **not** the rank-1
spacetimes a universe needs. This **kills the phase-space-dimension "3+1D at SL(3)" idea structurally**
(recorded in `docs/atlas/FAILURE_ATLAS.md`).

## R3 — the cubic-differential structure (`computer-assisted`)
`principal_sl3_branching`: under the principal `sl(2)`, the adjoint `sl(3)` decomposes as `V₂ ⊕ V₄`
(`ad(h)` weight multiset `{±4,±2,±2,0,0}` ⇒ irreps of dim **3** and **5**, highest weights 2 and 4 ⇒
holomorphic differentials of degree **2 (quadratic)** and **3 (cubic)**). **V0 is the `{cubic = 0}` slice**
— the `V₂` / quadratic directions are the Teichmüller deformations.

## R4 — the cubic-differential deformation OFF V0 (the genuinely-new computation)
- **(a) Infinitesimal split** (`tangent_space_split`, robust core): `H¹(F₂, sl(3)_Adρ₀)` at the Fuchsian rep
  is **8-dimensional**, and — because `Ad(A),Ad(B)` preserve the `V₂,V₄` blocks (the generators lie in the
  principal `SL(2,ℝ)`) — it splits **exactly** as `H¹ = 3 ⊕ 5`: the **`V₂` part (3) = Teichmüller**
  directions tangent to V0, the **`V₄` part (5) = CUBIC** directions transverse to V0. Verified at both
  Fuchsian seeds.
- **(b) Finite witness** (`cubic_deformation_witness`): the explicit real family `ρ_t(a)=exp(t·u_a)·Sym²(A0)`
  (likewise `b`), `u∈V₄`, at **2 Fuchsian seeds × 2 cubic directions**, `t=0.05`: **stays Anosov**
  (loxodromic, 3 distinct positive reals — Anosov is *open*, Labourie), **leaves V0** (`|x1−x4|≈0.1–0.27`),
  and **breaks the `SO(2,1)` form** (no invariant symmetric form survives, null dim 0). So the cubic
  directions are genuinely-`SL(3)` convex-projective deformations off the Fuchsian locus.

**Honest scope on (b):** an *unconstrained* cubic deformation also moves the **puncture holonomy off
unipotent** (`cusp_tr` drifts from 3) — fixing the boundary conjugacy class is a codimension constraint not
imposed here; the decisive, banked content is *"the cubic directions exist, stay Anosov, and leave the
Fuchsian locus."* A boundary-fixed deformation is the natural continuation (the verification chat's parallel
result; we reconcile when it lands).

## Verdict
V0 is the Fuchsian locus of the `SL(3,ℝ)` Hitchin component; the genuinely-`SL(3)` content the project never
explored is the **5-dimensional cubic-differential** directions, now exhibited both infinitesimally (`H¹`
split `3⊕5`) and as an explicit Anosov deformation off V0. The "tower of spacetimes up the ranks" is **dead**
(the ladder is Lorentzian only at `k=2`). The physics chain stays **cited and firewalled**.

```bash
python frontier/B101_hitchin_reframing/probe.py
python -m pytest tests/test_b101_hitchin_reframing.py -q
```
No physics claim; the Hitchin/Langlands/N=4 chain is cited, not claimed; proven core P1–P16 untouched;
physics chapter stays CLOSED; outreach dormant.
