# B317 — The Hitchin/Painlevé-VI lens, placed: the object is a *transcendental* Painlevé-VI solution

**Status: banked (frontier). Places the object in the Painlevé-VI solution landscape; corrects P010's stale "unrun."
Firewalled; nothing to `CLAIMS.md`.** P010 (the category root) names the **Betti (flat) vs Hitchin (dynamical)** lens
as "the one frontier where the object grows a genuine dynamics" and calls it "unrun on our objects." **That phrasing is
stale:** the lens *was* run — **B164** built the (0,4) Jimbo–Fricke cubic and its Painlevé-VI / mapping-class-group
dynamics, and **B169** ran the isomonodromy (Schlesinger) flow, computed the dynamical degree `λ_m²`, and returned the
firewall verdict (the flow's time is a *dimensionless modulus*). Both are dated 2026-06-18 and postdate P010. B317 adds
the one thing they left implicit: **where the object sits in the Painlevé-VI *solution* landscape.**

## The placement
The nonlinear monodromy of Painlevé VI is the mapping-class-group action on the (0,4)/(1,1) Fricke cubic — which *is*
the metallic trace map. **Lisovyy–Tykhyy (2008)** classify the **algebraic** Painlevé-VI solutions: they are exactly the
**finite orbits** of this nonlinear monodromy (finite-order / reducible trace-map elements). The metallic elements are
**hyperbolic** (`M_m = [[m,1],[1,0]]`, `det −1`, eigenvalues `λ_m` and `−1/λ_m`, `|λ_m| > 1` for all `m ≥ 1` →
loxodromic on the cubic, B169 C4), so their orbits are **infinite** (dense; Cantor for `κ > 2`). Therefore:

> **The metallic / figure-eight Painlevé-VI solutions are *transcendental* — not among the algebraic Lisovyy–Tykhyy
> list.** They carry positive topological entropy `h = log(λ_m²) = 2 log λ_m` (m=1: `2 log φ ≈ 0.962`; m=2: `1.763`;
> m=3: `2.390`) and dynamical degree `λ_m²` (m=1: `φ² = (3+√5)/2`; m=2: `3+2√2`; m=3: `(11+3√13)/2`, B169).

So the "dynamics" P010 sought is real and genuinely **chaotic** — the *opposite* of the special algebraic solutions.
The figure-eight is the golden (`h = 2 log φ`) transcendental Painlevé-VI solution.

## Verdict
The Hitchin/Painlevé-VI lens was **run** (B164/B169); P010's "unrun" is corrected. The object is a **transcendental,
positive-entropy** Painlevé-VI solution with dynamical degree `λ_m²`. The dynamics is **real**; its time is a
**dimensionless modulus** (B169) → the firewall **relocates**, does not dissolve — exactly the caveat P010 predicted
("the Painlevé time is a dimensionless modulus, not physical time — the same type-mismatch as P006").

## The meta-finding
This is the **third** Phase-3 lead in a row (after H14 → B234, √−7 → B235) to reduce to a **consolidation of banked
work**. The pattern is now decisive: the audit surfaced "forgotten leads," but on execution they are all consolidations
— the **documentation** had forgotten pieces (now fixed by the Phase-2 sweep), the **research** did not. The in-sandbox
research frontier is genuinely exhausted; what remains is specialist (the `T[4₁;E₆]` CRUX, multiplicity, the
non-Hermitian Damanik–Gorodetski theorem) or hard-theorem (S032-A, the full L34 bundle Weil-zeta).

## The fence
The metallic eigenvalues / dynamical degrees / entropies (sympy, exact) + the Lisovyy–Tykhyy finite-orbit ⇔ algebraic
criterion + the banked B164/B169 dynamics. The "chaotic dynamics = physical time" reading is firewalled; the time is
dimensionless (B169). Nothing to `CLAIMS.md`.

`painleve_transcendental.py` (pyenv) · `tests/test_b317_painleve_transcendental.py`. Related: **B164** (the (0,4)
Fricke cubic + Painlevé-VI/MCG dynamics), **B169** (the isomonodromy flow, dynamical degree `λ_m²`, dimensionless
time), **P010** (the Betti-vs-Hitchin lens — corrected here), **K018** (the firewall across modes, the Hitchin mode),
`K007`/`K010` (the Cantor spectrum for `κ>2`). Lit: Lisovyy–Tykhyy (2008, algebraic Painlevé-VI solutions);
Cantat–Loray (the dynamics on the cubic, the dynamical degree); Iwasaki, Boalch (Painlevé VI / isomonodromy).
