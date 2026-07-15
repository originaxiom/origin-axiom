# B615-R — the target-uncertainty re-analysis of the Branch-3 comparison (cc2 advisory cell)

**Seat: cc2 (assistant/advisor; no repo writes; deliverable = packet to cc).
Opened 2026-07-15. Prereg tier: cell (sealed before running; hash in SEAL.txt).
Scope: a STATISTICAL RE-ANALYSIS of the recorded B615 comparison — the same
217 pairs, the same object-side inventory (copied verbatim from the in-repo
`b615_comparison.py`, design hash 9a189f49… acknowledged), the same
Poisson-binomial/Šidák machinery, the same verdict thresholds. No new object
quantities are computed or compared (the sealed B614 design's "further tests
need new held-out quantities" clause is not triggered — nothing here is a new
test of the object; it is the disclosure's own flagged gap, run: "a
target-uncertainty-aware re-analysis" (B615 FINDINGS, Disclosure item 2).**

## The question

B615 returned AMBIGUOUS (Šidák-corrected best-grid p = 0.0775 at tier 1e-2),
driven by three G2 matches against PMNS point targets recorded at PDG-2024
central values. The disclosure itself notes the PMNS targets carry
percent-level uncertainties and predicts uncertainty-awareness "can only
WEAKEN the observed significance." The Branch-3 record also reports (post
literature round) that the suggestion "dissolves under the NuFIT central
values." Neither statement has been a computation. This cell computes it.

## The two corrections (and their decomposition)

Targets change from points t to (t, σ) with current global-fit values
(fetched with sources; pasted verbatim in §Inputs before sealing):

- **(i) Central update:** t_old (PDG-2024 as recorded) → t_new (current
  NuFIT/PDG). PMNS θ₂₃: both octant minima evaluated; the headline uses the
  fit's global best, the other minimum reported alongside.
- **(ii) Width correction:** match at tier d becomes |v − t| ≤ d·t + 2σ_t
  (the window inflated by the target's 2σ; σ_t = max(σ₊, σ₋)); the per-pair
  null probability inflates identically: p = min(1, 2(d·t + 2σ_t)) on the
  unit-range grids; on the log grids the half-width gains the target's 2σ in
  log10 space. This keeps observed matches and the null expectation on the
  same footing — the correction cannot be gamed in either direction.

Three variants are computed so the two effects separate cleanly:
(a) old centrals + width correction; (b) new centrals, point windows
(the "literature round" claim, now computed); **(c) new centrals + width
correction — the headline.** Everything else is byte-equivalent to the B615
machinery (tiers 1e-2/1e-3; exact Poisson-binomial tails; Šidák over grids;
G4's log window 0.5/range 25; G3's log-uniform null on [1e-10, 1e15]).

## The locked outcome table (verdict from variant (c)'s p_final)

- **A — p_final ≥ 0.1:** the AMBIGUOUS dissolves under proper statistics.
  Branch 3's SM-silent closure is HARDENED (now resting on
  uncertainty-correct inputs); recommendation to cc: bank as the closure's
  statistical completion; no re-probe warranted.
- **B — 0.01 ≤ p_final < 0.1:** AMBIGUOUS is uncertainty-robust; the verdict
  stands exactly as banked (suggestive-only, no escalation); the record
  gains the corrected inputs.
- **C — p_final < 0.01:** the significance STRENGTHENS under correct
  treatment — the premature-closure scenario. Recommendation to cc: reopen
  per the original design's escalation lane, with the surviving rows named.

Guards: MB8 (the null recomputed per variant, never reused); MB12 (if window
inflation drives any grid's expected count ≥ observed for trivial reasons —
e.g. windows swallowing the unit interval — that grid is reported saturated,
not significant-by-collapse); the M_GUT/M_Z row is a convention, not a
measurement — carried as in B615 but flagged in-output; asymmetric σ taken
conservatively (max); lepton-ratio σ are negligible and set exactly.

## Correction (iii), added pre-seal: scheme/scale consistency (the Level-1 defect)

The recorded G3 targets mix schemes and scales (pole m_t over MS-bar m_b(m_b);
m_b(m_b) over m_s(2 GeV)); the same physical ratios span 36–61 (m_t/m_b) and
45–54 (m_b/m_s) across conventions. G3 is therefore run in THREE stated scheme
columns — (A) the recorded convention (continuity with B615), (B) pole/pole
where defined, (C) MS-bar at a common scale (conversions per standard running;
±spread carried as σ) — with the spread itself reported. α_em is MS-bar
(127.95) as recorded, with the effective-scheme value (128.95) noted as a
flagged alternative. θ₂₃ enters as the NuFIT 6.1 global best fit (NO, 0.470);
the other-octant minimum (0.550–0.555, Δχ² < 6) is run as sensitivity variant
(c2). CKM uses direct semileptonic averages (matching the recorded framing);
global-fit values noted. PDG CL=90% quark-mass errors converted to ≈1σ (/1.645).

## Inputs (pasted verbatim from the sourced fetch, sealed)

Sources: NuFIT 6.1 (2025, nu-fit.org, data through Nov 2025); PDG RPP-2026
(1 June 2026). σ = max(σ₊, σ₋).

| target | t_old (B615) | t_new | σ | note |
|---|---|---|---|---|
| α_em(M_Z)⁻¹ MS-bar | 127.951 | 127.95 | 0.02 | effective-scheme alt: 128.95 ± 0.01 (flagged) |
| α_s(M_Z) | 0.1180 | 0.1180 | 0.0009 | unchanged |
| sin²θ_W(M_Z) MS-bar | 0.23122 | 0.23122 | 0.00006 | unchanged |
| sin²θ₁₂ | 0.307 | 0.3088 | 0.0067 | NuFIT 6.1 (NO=IO) |
| sin²θ₂₃ | 0.546 | 0.470 | 0.017 | NuFIT 6.1 NO best fit (LOWER octant; 6.0→6.1 flip); (c2): 0.550 ± 0.016 |
| sin²θ₁₃ | 0.0220 | 0.02249 | 0.00057 | NuFIT 6.1 NO |
| λ_Cabibbo | 0.22501 | 0.22517 | 0.00068 | PDG-2026 global fit |
| \|Vcb\| | 0.0408 | 0.0407 | 0.0013 | direct semileptonic avg; global fit 0.04189 noted |
| \|Vub\| | 0.00382 | 0.00389 | 0.00016 | direct semileptonic avg; global fit 0.003763 noted |
| m_μ/m_e | 206.7683 | 206.768283 | 5e-6 | exact for our purposes |
| m_τ/m_μ | 16.817 | 16.8177 | 0.0009 | m_τ = 1776.93 ± 0.09 |
| m_τ/m_e | 3477.23 | 3477.37 | 0.18 | |
| m_t/m_b (A: recorded) | 41.26 | 41.24 | 0.28 | 172.60/4.186 — the recorded mixed convention |
| m_t/m_b (B: pole/pole) | — | 36.1 | 0.5 | m_b pole ≈ 4.78 ± 0.06 |
| m_t/m_b (C: MS-bar @ m_t) | — | 60.1 | 0.7 | m_t(m_t) ≈ 163.0 ± 0.4, m_b(m_t) ≈ 2.71 ± 0.03 (derived) |
| m_b/m_s (A: recorded) | 44.75 | 45.06 | 0.35 | 4.186/0.0929; m_s 1σ ≈ 0.43 MeV (CL90/1.645) |
| m_b/m_s (C: common μ) | — | 53.6 | 0.6 | m_b(2GeV)/m_s(2GeV) ≈ 4.98/0.0929 (derived) |
| m_t/m_e (A: recorded) | 337710 | 337766 | 530 | |
| m_t/m_e (C: MS-bar) | — | 318980 | 800 | m_t(m_t)/m_e |
| M_GUT/M_Z [CONVENTION] | 2.19e14 | 2.19e14 | — | not a measurement; carried, flagged; no σ |

[SEALED — hash of this file + run_b615r.py in SEAL.txt before the run]

## Deliverable

`run_b615r.py` (self-contained; prints every pair, every variant, the
decomposition table, and the verdict letter) + outputs banked to
`outputs/` before any comparison prose is written + PACKET.md for cc.
