# B162 — the κ-sweep: κ=2 is the unique cancellation↔non-cancellation wall

**Date:** 2026-06-18. **Status:** the lead **L19** (the κ-sweep middle) is **promoted** from validated audit
numerics to a banked finding — the *geometric* face of the non-cancellation obstruction (`speculations/S034`,
B161). The figure-eight/golden monodromy, foliated over `κ = 2 + λ²`, has a spectrum that is **positive-measure
only at `κ=2`** (the full AC band — the trivial/cancellation vacuum) and **zero-measure everywhere else** (a real
Cantor set for `κ>2`, a thin complex set for `κ<2`). Standalone spectral / character-variety mathematics; **no
Origin-core claim, no physics crossing** (both ends are established math); P1–P16 untouched; nothing to
`../../CLAIMS.md`. Ledger V156. Reproducer `kappa_sweep.py`.

## The result (one foliated map, the spectrum across κ)

Direct finite-Fibonacci-chain diagonalization (the eigenvalues *are* the spectrum), method self-validated:
**V1** Hermitian sanity (real λ ⟹ real spectrum), **V2** bulk BC-robustness (95-pct nn(open,periodic) → 0 with
size: 0.118→0.034→0.015), **V3** size convergence of max|Im E|, **V4** open-BC chiral symmetry `E ↔ −Ē` (to eig
precision 3.5e-7).

| regime | `κ` (via λ) | spectrum | measure |
|---|---|---|---|
| **cancellation** | `κ=2` (λ=0) | full AC band `[−2,2]` | **`|σ|₁D = 4.000`** (positive — trivial vacuum) |
| non-cancellation (Hermitian) | `κ>2` (λ=0.5,1,2) | real **Cantor** dust | `1.817, 0.706, 0.097` → 0 |
| non-cancellation (non-Hermitian/PT) | `κ<2` (λ=0.5i…2i) | **thin** complex set | 2D area → 0 as ε→0 (box-dim<1) |
| figure-eight cusp | `κ=−2` (λ=2i) | (endpoint) | commutator **parabolic** (symbolic, B160) |

- **`κ=2` is the unique wall** — the *only* fiber whose spectrum carries positive measure in its ambient
  dimension. It is exactly the cancellation locus (B161): full band = "everything allowed, nothing forbidden" =
  the trivial vacuum. **[num, self-validated]** + **[exact]** at λ=0 (free Laplacian).
- **Off the wall, the spectrum is the non-cancellation residue** — zero-measure: a real Cantor set for `κ>2`
  (Sütő/Damanik–Gorodetski), a **thin** (zero-2D-area, box-dim<1) complex set for `κ<2`. **[num]**
- **Lift-off into ℂ** is clean and near-linear: `max|Im E| ≈ 0.91·μ` across `κ = 1.75 … −2` (0.914, 0.913,
  0.910, 0.907). **[num]**
- **The κ=−2 endpoint** is the figure-eight complete hyperbolic cusp: `κ=2+λ²=−2 ⟺ λ=2i`, commutator parabolic
  (trace −2, single Jordan block `(C+I)²=0`, not central −I). **[symbolic, B160]**

## Honest scope (what is NOT claimed)

- The `κ<2` set is **thin / zero-2D-area**, **not proven a true (totally-disconnected) Cantor set** — there is
  **no ground-truth theorem off the real axis** (the Damanik–Gorodetski horseshoe covers only the Hermitian
  `κ>2` regime). The `κ<2` Cantor-persistence stays **`[num]`, OPEN-as-theorem** (`docs/OPEN_LEADS.md` L19).
- Whether the `κ=−2` complex spectrum **encodes** the figure-eight hyperbolic geometry is **not tested and not
  claimed** — two true facts about one `κ` value are not an encoding. **OPEN** (L19).
- "BC-identical" is **not** claimed: the bulk is BC-robust (reciprocal H, no skin effect) but ~5
  boundary/winding modes differ (refines the cross-session "exactly identical" reading).

## Firewall

Both endpoints are **established mathematics** (Sütő spectral theory; Thurston hyperbolic geometry) — so this is
a **mathematical bridge, not a firewall crossing**. The non-Hermitian/PT language is condensed-matter
mathematics ("one particle in a fixed quasicrystal"), never fields/masses. No `Λ`, no scale; nothing to
`CLAIMS.md`.

## Anchors
B161/V155 (the cancellation-locus stratification — κ=2 non-generic + trivial), `speculations/S034` (the spine),
B160/V154 (the κ-sweep symbolic anchors; κ=−2 parabolic), B67 (figure-eight from the trace map), K007/K010/P008
(the named object). External: Sütő (1987); Damanik–Gorodetski (the KKT horseshoe, Hermitian κ>2); Thurston
(figure-eight hyperbolic structure). Ledger V156.

## Reproduction
`python frontier/B162_kappa_sweep/kappa_sweep.py` — V1–V4 self-validation; the κ≥2 band measure (positive only at
κ=2); the κ<2 thin-set area + lift-off; the κ=−2 parabolic cusp. Prints `ALL CHECKS PASS`.
