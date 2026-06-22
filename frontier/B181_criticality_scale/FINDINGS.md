# B181 — the criticality scale-door: the metallic object is permanently critical (= scale-free *by* criticality)

**Date:** 2026-06-19. **Status:** the first hunt of the search specification (`../speculations/S036`) — the
**large-N / criticality** door, the single most promising route to an *emergent scale* (a phase transition gives a
diverging correlation length). **Result: an inversion.** The metallic quasicrystal is **permanently critical**
(scale-invariant *by nature*) — which **explains** its scale-freeness rather than breaking it; a genuine transition
(a finite emergent length) requires *leaving* the metallic class, and even then the length is **dimensionless**, so
the scale stays external. **Firewall-side**: emergent localization/criticality math (`K010` boundary); no scale/Λ;
**nothing to `../../CLAIMS.md`**; P1–P16 frozen. Ledger V175. Reproducer `criticality_scale.py` (`ALL CHECKS PASS`).

## The diagnostic and the result

The clean probe for criticality is the **Lyapunov exponent** `γ(E)` of the 1D transfer cocycle (localization):
`γ=0` on the spectrum = critical/extended (delocalized, localization length `ξ=1/γ→∞`); `γ>0` = localized, with a
*finite* `ξ=1/γ`. Averaged over in-spectrum energies:

| model | λ=1 (weak) | λ=3 (strong) |
|---|---|---|
| **Aubry–André** (smooth cosine) | γ = 0.0004 (extended) | γ = **0.405** (localized) — matches exact `ln(3/2)` |
| **Fibonacci** (metallic Sturmian) | γ = 0.006 (critical) | γ = **0.021** (still critical) |

- **C1 — the metallic chain is *permanently critical*.** `γ≈0` on the spectrum at weak *and* strong coupling — **no
  metal–insulator transition** (`γ_Fib(λ=3)` is ~20× smaller than the AA localized value; the small residual is
  finite-N convergence of the exactly-zero critical value, Damanik–Lenz: the Fibonacci spectrum has zero Lyapunov for
  all coupling). The metallic object sits *at* criticality without tuning.
- **C2 — a transition needs a non-metallic field.** The smooth Aubry–André operator *does* have a sharp transition at
  `λ=2`: extended (`γ=0`) below, localized (`γ=ln(λ/2)>0`) above. A finite localization length `ξ=1/γ≈2.5` appears in
  the localized phase. (Verified `γ_AA(λ=3)≈ln(3/2)=0.405`.)
- **C3 — the inversion.** Permanent criticality `⟹ ξ=1/γ→∞` (**no finite length**) `⟹` scale-**invariant** `⟹`
  scale-**free**. A finite emergent length exists *only* off the metallic class (the AA localized phase) and is
  **dimensionless** (≈2.5 *lattice units*) — so the scale is still **external**. **Criticality *explains* the metallic
  object's scale-freeness; it is not a scale source.**

## What this means for the search (S036)

The most promising scale-door — "a phase transition at large N gives a diverging length = an emergent scale" —
**leads back to the relocated wall, now explained.** The metallic quasicrystal is scale-free *because* it is
permanently critical (the very property that makes it special — most-irrational, multifractal, the Hurwitz/KAM extremal
nature, `B176`/`B179` — is its scale-invariance). To get a finite emergent length you must **break** criticality
(use a non-metallic, e.g. Aubry–André, field), and even then the length is dimensionless (lattice units → external).
So the **SCALE** ingredient of the S036 register stays **external**, and the scale-search points to the **Hitchin/Higgs**
side (`K018`/`B169`), *not* large-N criticality of this object. (A genuine new understanding, not just another "no":
criticality unifies *why metallic/critical* with *why scale-free*.)

## Scope / honesty
- This tests *one* scale-door (criticality/localization), decisively for the single metallic chain vs the AA control.
  It does **not** test every large-N collective (e.g. an *open, driven* many-body system, the metabolism register
  `B177`, remains NEEDS-SPECIALIST) — but it removes the most-cited route (criticality of the metallic operator).
- Emergent localization/criticality mathematics (`K010` boundary); no physical-magnitude claim; nothing to
  `../../CLAIMS.md`; P1–P16 untouched.

## Anchors
`../speculations/S036` (the search register this is the first hunt of), `K007`/`K010` (the metallic Schrödinger
cocycle / Cantor spectrum), `B176`/`B179` (the most-irrational/multifractal nature = the criticality), `K018`/`B169`
(the firewall verdict / the external Hitchin side the scale-search points to), `B175`/`B178` (the woven-spectrum
context). External: Damanik–Lenz / Damanik–Gorodetski (zero Lyapunov on the Fibonacci spectrum, all coupling — the
critical/multifractal nature); Aubry–André / Avila (the metal–insulator transition `γ=ln(λ/2)`, self-dual at λ=2);
criticality = scale-invariance (a diverging correlation length as the scale source).

## Reproduction
`python frontier/B181_criticality_scale/criticality_scale.py` — C2 the AA metal–insulator transition (γ jumps across
λ=2); C1 the metallic chain permanently critical (γ≈0 all coupling); C3 the inversion (criticality = scale-freeness).
Prints `ALL CHECKS PASS`.
