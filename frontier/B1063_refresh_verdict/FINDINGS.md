# B1063 — THE B1027 REFRESH EXECUTES: MISS in all four variants, the decisive clause FIRES — the phase exclusion is CONFIRMED-DECISIVE and the fourth crossing closes

*cc banking seat, 2026-08-13. The pre-committed refresh (sealed inside B1027's own
prereg c58c8a88: same windows, zero freedom, fetch-at-verdict) executed against
NuFIT 6.0 (arXiv:2410.05380, v2 Oct 2025; data to Sept 2024) — Table 1 read from
the PDF ON THIS BENCH (pages 6–7), the parameter table quoted exactly. Log:
`refresh_windows.log` (the mechanical re-run). Gate 5: the measured values appear
HERE, in the physics-facing verdict arc, as B1027's own protocol provides —
nothing enters CLAIMS.*

## The trigger, and a defect found with it

**The trigger had already fired before the seal.** NuFIT 6.0 published 2024-10-07
— ten months before B1027 sealed against NuFIT 5.2. The refresh condition ("a
newer fit is fetchable") was satisfiable on sealing day; B1027's verdict-time
fetch returned the stale 5.2 (the nu-fit.org certificate failure is the live
suspect — it blocks fetches today too; the arXiv route works). **Recorded as a
fetch-currency defect (the species: a fetch that cannot reach the current source
silently adjudicates against a stale one), with the repair: verdict-time fetches
must state WHICH release they reached and check the arXiv mirror.** The refresh
itself is unaffected: its windows were sealed independent of any fit.

## The re-run (mechanical; the sealed windows against Table 1's four variants)

| variant | δ_CP bfp ±1σ | 1σ interval | vs 240° | vs 120° |
|---|---|---|---|---|
| NO, IC19 w/o SK-atm | 177° +19/−20 | [157°, 196°] | **MISS by 44°** | MISS by 37° |
| IO, IC19 w/o SK-atm (best fit) | 285° +25/−28 | [257°, 310°] | **MISS by 17°** | MISS by 137° |
| NO, IC24 with SK-atm (best fit) | 212° +26/−41 | [171°, 238°] | **MISS by 2°** | MISS by 51° |
| IO, IC24 with SK-atm | 274° +22/−25 | [249°, 296°] | **MISS by 9°** | MISS by 129° |

**Eight window-target pairs, eight misses.** No variant admits ±120° at 1σ.

## The decisive clause fires

B1027's own trigger language: *"a global fit shrinking δ_CP's upper error by ~2×
decides ±120° sharply in either direction."* The NO upper error went **+42° (5.2)
→ +19° (6.0 w/o SK-atm): a 2.21× shrink.** On that variant 240° sits 44° outside
a ±20°-scale interval. **The condition is met and the decision is AGAINST ±120°.**

## The Jarlskog cross-read (B1038's binding)

J_CP^max = 0.0333 ± 0.0007 (6.0, eq. 2.6). The ±120° label implies |J| =
J^max·(√3/2) = 0.0288. The fit's NO best is J ≈ 0.0017 (CP-conserving within 1σ);
IO's best is J ≈ −0.032 (|sin δ| ≈ 0.96 — δ near 254°/286°, not the 240° label).
**The convention-free carrier agrees with the angular verdict in both orderings.**

## What closes and what is honestly noted

- **The fourth crossing (B1027) CLOSES: the phase exclusion is CONFIRMED-DECISIVE.**
  The wait-state (R44-4 = R45-10) closes; the refresh is SPENT under its own
  pre-commitment. Any future re-pose at Hyper-K/DUNE precision (few-degree δ_CP,
  ~2028+/2030s) would be a NEW arc under a NEW seal — the record does not keep a
  standing re-armed window, by the one-shot discipline.
- **The 2° footnote, stated so it cannot grow into a story**: the NO-with-SK-atm
  variant's upper edge (238°) sits 2° from 240°. That variant is the one whose
  own Δχ²(δ_CP) the fit calls non-Gaussian ("indicative only, particularly for
  NO"); the DECIDING variant (the shrunk-error one) misses by 44°. The knife-edge
  is recorded as a fact about the fit's shape, not as encouragement.
- **The type-law postscript**: this was the one crossing aimed at a finite label
  through the coupling — the right TYPE at the right LOCATION, per everything the
  field campaign later proved. It was the best-formed crossing the programme ever
  ran, and it lost on the world's numbers. That is what an honest crossing looks
  like from the losing side, and the record is better for containing one.

## Verdict

**NEGATIVE** (the refresh's miss, all variants; the exclusion decisive; the
crossing closed). Locks: `tests/test_b1063_refresh.py`.
