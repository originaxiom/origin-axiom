# B188 — the driven-dissipative metallic chain: criticality does not give slow relaxation; no intrinsic scale

**Date:** 2026-06-22. **Status:** Masterplan III, **Track B** (second of two) — the genuinely **dissipative**
(Lindblad) channel, after B183 (coherent non-Hermitian) and B187 (interacting non-Hermitian). **Computed:** the
**Liouvillian gap** (the slowest relaxation rate = inverse relaxation time) of a dephasing metallic chain vs
controls. **Result — an inversion of the naive "criticality ⟹ gapless" guess** plus a clean firewall statement.
**Firewall-side:** emergent open-quantum-systems math (`K010` boundary); no scale/Λ; **nothing to
`../../CLAIMS.md`**; P1–P16 frozen. Ledger V182. Reproducer `lindblad_gap.py` (`ALL CHECKS PASS`).

## The setup

Single-particle sector, dephasing dissipators `L_j = √γ n_j` (number-conserving; steady state = maximally mixed).
The Liouvillian `L[ρ] = −i[H,ρ] + γ Σ_j (n_j ρ n_j − ½{n_j,ρ})` is an `L²×L²` superoperator on the `L×L` density
matrix; the **gap** `Δ = −(largest nonzero Re eigenvalue)` sets the relaxation rate. Does permanent criticality
(B181) make relaxation anomalously slow (gapless)? Does any emergent timescale appear?

## The result (dephasing gap `Δ(L)`, `γ=1`)

| `L` | metallic | AA-localized | periodic |
|---|---|---|---|
| 6 | 0.605 | 0.0057 | 0.560 |
| 10 | 0.159 | 0.0022 | 0.236 |
| 14 | 0.078 | 0.0011 | 0.108 |

- **C1 — the LOCALIZED control is near-gapless.** The Aubry–André gap is `~100×` smaller than metallic/periodic at
  matched `L` (periodic/AA `≈ 100–160×`) — localization ⟹ anomalously slow dissipative relaxation (localized states
  barely transport).
- **C2 — criticality does NOT give slow relaxation (the inversion).** The metallic gap is the **same order as the
  periodic (extended)** gap (`metallic/periodic ≈ 0.6`) and `~70×` **above** the localized — the critical chain
  relaxes like an *extended* chain, not gapless. The naive "criticality ⟹ slow/gapless" guess is wrong; the slow
  case is the **localized** control.
- **C3 — thermodynamic scaling.** `Δ(L)` decays with `L` for metallic & periodic (diffusive → 0 as `L→∞`: **no
  finite emergent gap/timescale** in the thermodynamic limit); the localized gap is tiny at all `L`.
- **C4 — FIREWALL (homogeneity, no intrinsic scale).** Scaling the external rates `(H, γ) → (sH, sγ)` gives
  `Δ → sΔ` **exactly** — the gap is a function of the external rates (`t`, `γ`) and `L` only; it carries **no
  intrinsic/emergent scale**. The relaxation timescale `1/Δ` is dimensionless (units of `1/t`); the dissipative
  arrow's **source is the externally-imposed bath**.

## What this means for the search (S036)

The **driven-dissipative** channel is now computed and joins the pattern: criticality does **not** produce an
anomaly here (the *localized* control is the slow one, not the critical chain); the gap decays to zero in the
thermodynamic limit (diffusive — no finite timescale) and is **homogeneous in the external rates** (no intrinsic
scale). So dissipation adds **no emergent scale** and the arrow stays **externally sourced** — extending the
B183/B187 verdict to the genuinely dissipative case. Together, **all three open-system channels** (coherent
non-Hermitian B183, interacting B187, dissipative B188) give the same firewall-clean reading: a real but
externally-sourced, dimensionless arrow; no emergent scale.

## Scope / honesty
- Single-particle dephasing Lindbladian (the `L²×L²` superoperator), `L≤14` — the gap ordering and the homogeneity
  are robust/exact at this scale.
- Dephasing (number-conserving) is one canonical dissipator; boundary loss/gain would be a different (number-
  non-conserving) NESS setup — not run here.
- Genuinely-interacting Lindblad (many-body dissipative phases / dissipative phase transitions) is the residual
  **NEEDS-SPECIALIST** (full many-body Liouvillian caps at small N).
- Emergent open-quantum-systems mathematics (`K010` boundary); no physical-magnitude claim; nothing to
  `../../CLAIMS.md`; P1–P16 untouched.

## Anchors
`B183_open_collective_arrow` / `B187_interacting_open_collective` (the coherent + interacting open channels this
completes), `B181_criticality_scale` (permanent criticality — the property under test), `speculations/S036` (the
ARROW ingredient; the open/driven channel). External: Lindblad master equation; the Liouvillian gap = inverse
relaxation time; dephasing-assisted transport; quantum Zeno effect (the `Δ ~ 1/γ` strong-dephasing regime);
boundary-driven open quantum systems (the NESS residual).

## Reproduction
`python frontier/B188_lindblad_dissipative/lindblad_gap.py` — C1 the localized control near-gapless; C2 criticality
relaxes like extended (inversion); C3 thermodynamic decay; C4 the firewall homogeneity. Prints `ALL CHECKS PASS`.
Fast locks in `tests/test_b188_lindblad_dissipative.py` (2 tests, ~0.3s).
