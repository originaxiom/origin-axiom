# B186 — off-axis hyperbolicity certification: the κ<2 Cantor hypothesis, validated on DG ground truth

**Date:** 2026-06-22. **Status:** Masterplan III, **Track C** (the first frontier of the computable-frontier
program). Grounds B165's conditional theorem for the off-axis (κ<2) Cantor spectrum (L19). **Computed, not
deferred:** the hyperbolicity hypothesis B165 left *unverified* is strengthened from **one** numerical diagnostic
(B163's MST gap) to **three independent** ones, the key one being a recognized hyperbolicity signature **validated
against the Damanik–Gorodetski-proven κ>2 case** before being applied off-axis. **Firewall-side:** spectral /
dynamical-systems math (`K010` boundary); no scale/Λ; **nothing to `../../CLAIMS.md`**; P1–P16 frozen. Ledger V180.
Reproducer `trace_map_hyperbolicity.py` (`ALL CHECKS PASS`).

## The setup (C0, exact)

The Fricke trace map `T(x,y,z) = (2xy−z, x, y)` conserves `I = x²+y²+z²−2xyz−1`, and the Schrödinger seed
`((E−λ)/2, E/2, 1)` lies on the surface `I = (λ/2)²` for **all** `E` (so `κ = 2 + λ²`; `κ>2 ⟺ λ` real,
`κ<2 ⟺ λ` imaginary, `κ=2 ⟺ λ=0`). The spectrum = the set of energies `E` whose trace-map orbit is **bounded**
(the non-escaping set). B165's conditional theorem: *if `T` is uniformly hyperbolic on its non-escaping set (a
complex horseshoe), then the κ<2 spectrum is a Cantor set.* The hypothesis was the open link.

## Why B165's attempt failed, and the fix

B165 recorded that a naive Jacobian "domination" ratio **failed** — it was contaminated by **escaping** orbits (the
κ=2 non-hyperbolic control also gave large ratios), so it measured generic escape, not bounded-set hyperbolicity.
The fix here: every diagnostic is **calibrated on the κ=2 band control** and **validated on the κ>2 case where the
horseshoe is a theorem (Damanik–Gorodetski)** — only then applied off-axis.

## The diagnostics

- **C1 — escape rate `γ` (the certification, ground-truth-validated).** The survival fraction `f(K)` of a trapping
  region decays `~ e^{−γK}`; by the Bowen–Ruelle thermodynamic formalism, **exponential escape `γ>0` ⟺ the maximal
  invariant set is a hyperbolic repeller** (`γ` = the topological pressure of the unstable Jacobian). Measured:

  | regime | `λ` | `γ` | reading |
  |---|---|---|---|
  | **κ>2 (DG-PROVEN hyperbolic)** | 3 | **0.51** | exponential escape ✓ (ground truth) |
  | **κ=2 band** (calibrator) | 0 | **0.00** | no escape (positive-measure band) ✓ |
  | **κ<2 off-axis** | 2i (κ=−2) | **0.18** | exponential escape — same signature |
  | **κ<2 off-axis #2** | 1.5i | **0.33** | exponential escape — same signature |

  The diagnostic is **correct on ground truth** (γ>0 exactly where the horseshoe is proven, ≈0 on the band) and the
  off-axis case shows the **same horseshoe signature**. Robust: across trapping radius `R∈[12,60]`, sampling
  density, and every κ<2 value tested (`κ` from 1.36 down to 0.56), the band stays exactly `0.000` and the
  hyperbolic regimes stay `γ>0`.
- **C2 — box-counting dimension (2nd independent Cantor diagnostic).** The spectrum's box dimension is `<1` and
  strictly below the κ=2 band's at matched depth, for golden (`m=1`: off-axis 0.91 < band 1.10) and silver
  (`m=2`: 0.77 < 0.85) — the fractal thinning of a Cantor set, independent of B163's MST.
- **C3 — recorded NEGATIVE (verify-don't-trust).** Two *local* diagnostics do **not** cleanly separate and are
  discarded (matching B165's warning): (a) the per-point index `|λ_max(DT)|` — the κ=2 band's median is also `>1`
  (a parabolic *set* has individual points with `|DT|>1`; per-point derivative magnitude is not the invariant);
  (b) the bounded-orbit trace-map Lyapunov — in the hyperbolic regimes approximate in-spectrum seeds are
  **expelled** (that *is* hyperbolicity), so exact bounded orbits are uncomputable from finite seeds. The clean
  certificates are **global** (escape-rate + box-dim + B163's MST).

## What this means (C4) and the residual

The off-axis κ<2 Cantor hypothesis is now supported by **three independent diagnostics**, the escape-rate being a
recognized hyperbolicity signature **calibrated on the band and validated on the DG-proven κ>2 case**. The
conditional theorem ("uniformly hyperbolic ⟹ Cantor") therefore rests on a hypothesis that is *numerically certified
by a diagnostic correct on ground truth* — a substantial strengthening of B165. **The sole residual is the rigorous
off-axis uniform-hyperbolicity proof** (a non-Hermitian Damanik–Gorodetski: non-normal transfer matrices, no off-axis
ground truth) — that stays NEEDS-SPECIALIST. Honest scope: a *fully rigorous* numerical cone-field certificate also
remains harder than the escape-rate signature (C3); the escape rate is strong evidence, not a constructive cone field.

## Anchors
`B165_kappa_cantor_offaxis` (the conditional theorem this strengthens), `B163_kappa_sweep_resolved` (the MST
diagnostic + controls), `B162` (κ=2 the unique wall), `B109_trace_map_dynamics` (the void linearization / Jacobian),
`K007`/`K010` (the metallic cocycle / Cantor spectrum), `B67` (κ=−2 figure-eight), `docs/OPEN_LEADS.md` L19.
External: Damanik–Gorodetski (the Hermitian κ>2 horseshoe / Cantor theorem — the ground truth); Bowen–Ruelle
thermodynamic formalism (escape rate = topological pressure; exponential escape ⟺ hyperbolic repeller); Bedford–Smillie
(complex polynomial automorphisms / horseshoes).

## Reproduction
`python frontier/B186_hyperbolicity_certification/trace_map_hyperbolicity.py` — C0 invariant + seed; C1 the
escape-rate certification (ground-truth-validated); C2 box-counting; C3 the recorded negatives; C4 the verdict.
Prints `ALL CHECKS PASS`. Fast locks in `tests/test_b186_hyperbolicity_certification.py` (2 tests, ~2s).
