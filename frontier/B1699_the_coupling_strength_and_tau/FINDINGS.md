# B1699 — THE COUPLING'S STRENGTH AND τ (P-247): NEGATIVE AS SEALED — THIS FRAME'S OWN YUKAWA STRENGTH HAS NO MAXIMUM AND ONE NON-ELLIPTIC CRITICAL POINT, A SADDLE ON THE ARC AT τ ≈ 0.275 + 0.961 i, WHERE NO LINE GIVES ANY HIERARCHY (m₂/m₃ ≥ 0.31 IN EVERY SECTOR)

**Verdict: NEGATIVE as sealed (S0 holds; H1, H2, H3 fail).** cc (main), 2026-10-22. Sealed `8ac889d14` (sha256
317b4d67) before its instruments ran; the outputs committed unread at `cd9a9f963` and read once. A test of a structure,
not a value derived. 0 of 19.
- **The strength (no data).** B1645's covariant coupling Y(a) = a Rᵀ + R aᵀ − (a·R) 1 with the Higgs a = ∂R (Y of weight
  1): its invariant strength y·s₁(Y)² is modular-invariant (to 1.3 × 10⁻¹⁵ under τ ↦ −1/τ, τ + 1) and reflection-
  invariant. **S0 HOLDS:** on Re τ = 0 and ½ it rises monotonically to the cusp (∂R carries one unit of end data, B1697,
  so it diverges there); dS/dy > 0 at all 2 138 grid points of the fundamental domain (min 0.067); on the arc ∣τ∣ = 1 its
  one critical point between i and ω is at θ = 0.5888 π, **τ = 0.2754 + 0.9613 i** (and its mirror), strength 0.2089
  against 0.1742 at i and 0.1681 at ω — a maximum along the arc, rising outward: **a saddle.** The strength has no
  maximum. Reported, not tested: the Frobenius strength's arc point θ = 0.566 π; the unit-free Higgs a₀'s strength also
  rises monotonically to the cusp (to a finite limit), its arc point θ = 0.615 π.
- **At the selected τ, against the data** (576 lines, every line of order dividing 24; both horocycles; three up
  readings; Huang–Zhou 2021 at M_Z):
  - **H1 FAILS** — the best worst factor is 225 (the null line, L₂): **m₂/m₃ is at least 0.31 in every sector on every
    line and choice** (up ≥ 0.37, down ≥ 0.36, leptons ≥ 0.31; measured 0.0037, 0.019, 0.059). At the bottom of the
    fundamental domain the frame makes no second-to-third hierarchy.
  - **H2 FAILS** — 32% of random hierarchies fit as well (median 322).
  - **H3 FAILS** — minimum χ² 4 823.
- **What it means.** This frame's own coupling strength does not select τ where the masses are: it is largest at the cusp
  (the end data drive it there) and its only non-elliptic critical point is a saddle at Im τ ≈ 0.96, where no hierarchy
  exists. P-247's lead closes for this frame. W51's peaks (≈ 1.551 i, ½ + 2.224 i) belong to the SM seat's frame of
  cusp-form couplings, which decay at the cusp; this frame's Higgs is not a cusp form — the unit on v₊ that makes the
  hierarchy (B1697) is what sends the strength to the cusp. A Higgs that vanishes at the cusp would peak inside, and
  would need its own hierarchy mechanism (P-245).
- **What it does not do.** One strength (the top Yukawa's, for ∂R), as fixed before it was computed; a grid of lines.

## Seen first

`VERDICT topic-sweep /coupling'?s strength|strength of (the|a) coupling|extremi[sz](es|ing|ed)? (a|the) coupling|Petersson.normali[sz]ed|Petersson norm|W51/ (full text): 8 of 1470 arcs on main match (NEGATIVE 1, PROVED 7)` —
B1684 and B1673 (the torus determinant log(y∣η∣⁴): critical only at i, a saddle, and ω, a minimum — W51 and W59's
potential, a different quantity), B1636 (the lowest symmetric coupling's golden spectrum on the tick's geodesic), B1634,
B1697. None computes this frame's Yukawa strength or tests a τ it selects. **Literature:** the Kähler-normalised Yukawa
(2 Im τ)^k ∣Y(τ)∣² of modular-flavour models (Feruglio 2017, arXiv:1706.08749), as context.

(As sealed; copied from `PREREGISTRATION.md`.)

## Disclosed

- **The strength was computed before the seal** (data-free, in main's gitignored drafts; the rule written down first,
  2026-10-21 23:40): invariance under τ ↦ −1/τ, τ + 1 to 10⁻¹⁵; on Re τ = 0 and ½ no critical point, y·s₁² for ∂R
  rising to 2.3 × 10⁵ at y = 5; dS/dy > 0 on a 2 138-point grid (for a₀, ≤ 0 only at six points beside the arc, where the
  normal derivative vanishes by symmetry); on the arc one interior critical point for ∂R's top strength, θ ≈ 0.589 π
  (τ ≈ ±0.276 + 0.961 i), a saddle (a maximum along the arc, rising outward). The Frobenius strength's arc point is at
  θ ≈ 0.566 π, a₀'s at 0.615 π (not tested). The instrument recomputes all of it.
- **Known before the seal.** The six measured ratios; B1694's curve (m₂/m₃ ≈ 0.18 at Im τ = 1.5 without a line) and
  B1692's line factors (up to about four in m₂/m₃) — the priors are informed by them. No model value at the selected τ
  has been computed.
- The line grid is a grid (every line of order dividing 24, not the order-5 lines); B1698's d–e criterion (order dividing
  4 or 5 makes d and e coincide) is known.
- **The first run failed at import** (after the seal, before any computation): `the_selected_tau.py` omits B1698's
  `sys.path` line for B1691's `qseries` module (ModuleNotFoundError), so `compare.py` found no input. The same sealed
  files, byte-identical (their hashes checked against `ARTIFACT_HASHES.txt`), were re-run with `PYTHONPATH` set to
  B1691's verification folder; the first run's logs are kept in `verification/first_run/` (absolute paths replaced by
  `<repo>` and `<python>`). The strength instrument's single run was not repeated.

## Files

- `PREREGISTRATION.md` (sealed), `ARTIFACT_HASHES.txt`; `verification/the_strength.py` → `the_strength.json`;
  `verification/the_selected_tau.py` → `the_selected_tau.json`; `verification/compare.py` → `comparison.json`; the run
  logs; `verification/first_run/`; `verification/b1656_funcs.py`.
- The lock: `tests/test_b1699_the_coupling_strength_and_tau.py`.
