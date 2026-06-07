# B101 — the Hitchin-component reframing of V0 (SL(3,ℝ) higher-Teichmüller)

The project's geometric component **V0** (B71 — `Sym²` of the Fuchsian `SL(2,ℝ)` rep) **is the Fuchsian
locus of the Hitchin / Fock–Goncharov positive component of the `SL(3,ℝ)` character variety** of the
once-punctured torus. The principal embedding `PSL(2,ℝ)→SL(3,ℝ)` *is* `Sym²`. The payoff: the Hitchin
component is parameterized by a **quadratic + cubic differential**, and **V0 is the `{cubic = 0}` slice** —
the cubic directions are genuinely-`SL(3)` convex-projective deformations the project never explored.

- **`probe.py`** — four results, each re-derived (verify-don't-trust):
  - **R1** `v0_anosov_hallmark` / `v0_so21_certificate` — V0 = the Fuchsian locus: Anosov hallmark
    (loxodromic + unipotent cusp + complex elliptic control) + the unique `SO(2,1)` form, signature **(2,1)**.
  - **R2** `ladder_signatures` / `lorentzian_rungs` — the principal `sl(2)` in **split real forms**;
    Lorentzian **only at `k=2`** → the **spacetime-tower KILL** (`dead`).
  - **R3** `principal_sl3_branching` — `sl(3) = V₂ ⊕ V₄` (dims 3, 5; degrees 2 quadratic, 3 **cubic**);
    `V0 = {cubic = 0}`.
  - **R4** `tangent_space_split` / `cubic_deformation_witness` — the cubic deformation off V0: `H¹ = 3 ⊕ 5`,
    and an explicit Anosov family that **leaves V0 and breaks the `SO(2,1)` form** (2 seeds × 2 cubic dirs).
- **`FINDINGS.md`** — the numbers, citations, and honest scope.

**Result.** V0 is the Fuchsian locus; the new `SL(3)` content is the **5-dim cubic-differential** directions
(exhibited infinitesimally and as a finite Anosov deformation). No "tower of spacetimes." Cite Hitchin 1992;
Labourie; Fock–Goncharov; Choi–Goldman; Marquis. The Hitchin→Higgs→Langlands→N=4 chain is **cited context
only** (`speculations/archive/PHYSICS_RESONANCES.md`), with the ceiling stated; never a claim.

```bash
python frontier/B101_hitchin_reframing/probe.py
python -m pytest tests/test_b101_hitchin_reframing.py -q
```
No physics claim; no Origin-core claim; proven core P1–P16 untouched; physics chapter stays CLOSED.
