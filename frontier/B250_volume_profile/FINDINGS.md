# B250 — the complex-volume profile of the figure-eight's E₆↔E₈ geometric transition

**Status: banked observation (frontier). FIREWALLED — geometry/McKay (Arnold trinity), NOT physics. Nothing to
`CLAIMS.md`.** Push from B248/B249. `volume_profile.py` (pyenv, mpmath; hyperbolic anchor cross-checked vs SnapPy).

## The profile
Quantifying the hyperbolic→Euclidean→spherical transition (B248) at the three Niven-forced ends (B249) — the volume
(real part of the complex volume) and the Chern–Simons (the framing/imaginary part):

| end | geometry | Vol | CS | arithmetic |
|---|---|---|---|---|
| **E₆** | hyperbolic (complete cusp) | `6·Λ(π/3) = 2.029883…` | `0` (amphicheiral) | `−3`: ideal-tetra shape `e^{iπ/3} ∈ ℚ(√−3)` |
| — | Euclidean (transition) | `0` (collapse) | — | degenerate |
| **E₈** | spherical (ℤ/2 orbifold; cover `L(5,2)=S³/ℤ₅`) | `π²/5 = 1.973921…` | `∈ (1/5)ℤ` (`{0,2/5,3/5}`) | `5`: `det(4₁)` |

## The point
The **determinant `det(4₁)=5`** is *literally* the **denominator** of the spherical-end volume `π²/5` and of its
Chern–Simons, while the **Eisenstein `−3`** sits in the hyperbolic-end ideal tetrahedra (shape `e^{iπ/3}`, volume via
`Λ(π/3)`). So the two exceptional ends carry their two arithmetic invariants **in their volumes**:

> `E₆ ↔ −3` (hyperbolic, via `Λ(π/3)`)   and   `E₈ ↔ 5` (spherical, via `π²/5`).

The two end-volumes are *comparable* (`2.0299` vs `1.9739`, within 3%) but live in opposite-curvature geometries —
the transition is a smooth real-volume descent from `2.0299` (hyperbolic) through `0` (Euclidean collapse) and back
up to `1.9739` (spherical). The complex-volume *imaginary* part (CS) flips from the amphicheiral `0` (hyperbolic) to
the `det`-quantized `(1/5)ℤ` (spherical).

## What it adds
B248/B249 placed E₆ and E₈ at the two ends and forced them by Niven; B250 shows the **arithmetic invariants are the
volumes**: the "5" is the spherical volume/CS denominator and the "−3" is the hyperbolic tetra shape — a single
geometric quantity (the complex volume across the transition) carrying both. This is the quantitative form of the
program's "5 cascade" (PAPER §3.3) and the dimensionless-firewall statement (PAPER §5.1: complex volume / CS is a
dimensionless element of `ℂ/4π²ℤ`).

## Physical read (firewalled, honest)
The complex volume is the program's dimensionless invariant; nothing here produces a scale. The profile is a
*curvature-sign transition* with the two exceptional geometries as its ends — a structural rhyme (dS↔AdS /
signature change), held behind the firewall, not a derivation. No dynamics, no gauge group.

Anchors: B248 (the transition), B249 (Niven forcing), B244/B151 (complex volume / CS dimensionless), PAPER
§3.3/§5.1. Literature: Lobachevsky function / ideal-tetrahedron volumes; lens-space Chern–Simons (Kirk–Klassen);
Thurston / Hilden–Lozano–Montesinos (figure-eight cone manifolds).
