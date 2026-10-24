# B1743 — THE NINE'S TARGET AND THE PRINCIPLED PENCILS (P-352; POST HOC EXPLORATION, LABELLED): ONE FREE HIGGS READ S IN EVERY SECTOR REACHES χ²_nine 17.26 (REPRODUCED ON MAIN), AT A NEARLY NULL DIRECTION WITH A FIXED INVARIANT ∣h·h∣ ≈ 0.017 AND AN e₁ ADMIXTURE ∣δ∣ ≈ 0.3; NO PENCIL OF TWO RECORD FORMS (ONE COMPLEX NUMBER FREE) GOES BELOW 41.9 ON THIS GRID

**Verdict: NEGATIVE for its question** — does a principled pencil (the span of two forms on record, one complex number
λ free) reach the nine's bar (χ²_nine < 21.67) on B1742's grid? No: the best is 41.9. With the target stated on main and
the web seat's R5 verified. **POST HOC, not a test:** nothing was sealed; every number is a minimum over a grid and a
free parameter, and no claim of specificity is made. cc (main), 2026-10-23. **0 of 19.**

## 1. The target (`verification/target.py` → `target.json`, `target_run.txt`)

The web seat's INVERSE HIGGS (row 1346; post hoc): one free direction h ∈ ℂP² for every sector, read S, c = 3, on
TWO_HIGGS's grid (the ten (2/5, k/10) lines; B1742). Main reproduces its minima exactly on its own instrument (B1740's,
via B1742's `repro.py`) and records the full complex direction, in ρ(T)'s eigenbasis: e₁ (non-null), h₀ = (0, 1, i)/√2
and h̄₀ (null); δ = e₁'s coefficient over the leading null one, ε = the other null's over the leading.

| row (line, τ, horocycle) | χ²_nine | δ | ε | ∣h·h∣/∣h∣² | nearest record form (Fubini–Study) |
|---|---|---|---|---|---|
| (2/5, 3/5), 0.4375 + 2.1i, L₂ | 17.257 | 0.074 + 0.308i | 0.048 − 0.032i | 0.0177 | ∂R̄, 0.281 |
| (2/5, 3/5), 0.3125 + 2.0i, L₂ | 18.279 | 0.120 + 0.311i | 0.040 − 0.047i | 0.0172 | F₆, 0.323 |
| (2/5, 3/5), 0.4375 + 2.2i, L₂ | 20.846 | 0.052 + 0.285i | 0.042 − 0.024i | 0.0181 | ∂R̄, 0.247 |
| (2/5, 3/5), 0.5625 + 2.3i, L₂ | 21.518 | 0.016 + 0.278i | 0.043 − 0.013i | 0.0185 | ∂R̄, 0.192 |
| (2/5, 3/5), 0.8125 + 3.2i, L_max | 26.92 | −0.035 + 0.205i | 0.026 + 0.001i | 0.0150 | ∂R̄, 0.170 |

(Each row has a mirror on (2/5, 0) at 1 − Re τ with the same χ², δ → −iδ̄.) At the best row the model over measured is
1.005, 1.006, 1.062, 0.945, 1.013, 1.060 (the six) and 0.773, 0.775, 1.213 (∣V_us∣, ∣V_cb∣, ∣V_ub∣); J 4.2 × 10⁻⁶ (7
times small); D = 9 (B1742's identity). **What the data want:** a Higgs nearly null with a *fixed* invariant
∣h·h∣/∣h∣² ≈ 0.015–0.019 on every good row and both horocycles, and an e₁ admixture ∣δ∣ ≈ 0.2–0.33. The four free reals
fit seven independent numbers here (four quark ratios, three moduli; the leptons are the down quarks', B1742), so this is
a target, not evidence.

## 2. The principled pencils (`verification/pencils.py` → `pencils_run.txt`)

h = A + λB (λ ∈ ℂ or ∞), read S in every sector — and the conjugate pencil (read S̃) — with A, B two forms on record at
τ: ∂R ∣ R (the covariant-derivative pencil: the weight pencil h_w = ∂R + (w/12)E₂*R lies in it), ∂R ∣ ∂²R (the Serre
tower), and the pairs that share a multiplier (W143): F₂₂ ∣ F₋₂ (r = 20), F₆ ∣ F₋₆ (r = 12), F₁₄ ∣ F₋₁₀ (r = 4). λ fitted
by least squares from thirteen starts, at every one of the grid's 1 280 points and both horocycles.

| pencil | min χ²_nine | where (line, τ, horocycle) | rows below 21.67 |
|---|---|---|---|
| ∂R ∣ R | 949.7 | (2/5, 4/5), 0.5625 + 3.00i, L₂ | 0 |
| ∂R ∣ R, conjugated | 43.2 | (2/5, 3/10), 0.6875 + 3.30i, L_max | 0 |
| ∂R ∣ ∂²R | 920.2 | (2/5, 4/5), 0.4375 + 3.00i, L₂ | 0 |
| ∂R ∣ ∂²R, conjugated | 50.3 | (2/5, 1/2), 0.4375 + 3.30i, L_max | 0 |
| F₂₂ ∣ F₋₂ | 43.1 | (2/5, 3/10), 0.4375 + 3.30i, L_max | 0 |
| F₂₂ ∣ F₋₂, conjugated | 917.3 | (2/5, 0), 0.8125 + 2.00i, L₂ | 0 |
| F₆ ∣ F₋₆ | 41.9 | (2/5, 3/10), 0.3125 + 3.30i, L_max | 0 |
| F₆ ∣ F₋₆, conjugated | 956.8 | (2/5, 4/5), 0.4375 + 3.00i, L₂ | 0 |
| F₁₄ ∣ F₋₁₀ | 42.1 | (2/5, 3/10), 0.3125 + 3.30i, L_max | 0 |
| F₁₄ ∣ F₋₁₀, conjugated | 968.0 | (2/5, 3/5), 0.1875 + 2.60i, L₂ | 0 |

No pencil has a single row below 21.67. The best four sit together, at (2/5, 3/10), Im τ 3.3, L_max, about 42 — twice
the bar, against the free direction's 17.3 (L₂) and 26.9 (L_max). One complex number inside a pencil of record forms
does not reach the target: the target direction lies off every such pencil at the τ where the frame wants it.

## 3. The web seat's R5, verified on main

In the idealised up channel (u = a₃h₀, no antisymmetric weight, h₀'s component 0) B1736's closed form gives m₁ = 0,
m₂m₃ = ∣a₃∣²∣h·h∣ and m₂/m₃ ≥ ∣h·h∣/4: on 2 000 random unit Higgs directions, m₁/m₃ ≤ 1.5 × 10⁻¹⁶, the product to
1.1 × 10⁻¹⁵, the bound's smallest ratio 1.009. On the order-5 lines (2/5, k/10), k even, the up twists are equal (5w is a
lattice point, so −4w ≡ w; B1728's five-ality), and the up channel's antisymmetric weight vanishes (the seat's R5
statistics). So in the idealisation the Higgs's non-nullity sets the up hierarchy's floor, and the target's nearly
constant ∣h·h∣ is consistent with that; the real channels depart from the idealisation (∣u·u∣/∣u∣² about 0.04, the
symmetric weight a₂ about 0.2 of ∣u∣ at the band), so this is a reading, not a derivation.

## 4. What it means

- **The nine's target is now precise on main:** a nearly null Higgs whose invariant ∣h·h∣/∣h∣² is about 0.017 (not
  exponentially small in Im τ) with an e₁ admixture about 0.3, read the same way in every sector.
- **No pencil of two record forms reaches it** (best 41.9); with the web seat's RECORD PAIRS (676 ordered pairs, best
  96.3) and WEIGHT PENCIL (best 53.0), no Higgs built from the record's forms reaches the nine on this grid. A principle
  that fixes ∣h·h∣ at the hierarchy's value and the e₁ admixture is the open route (P-352).
- **Scope:** the ten α = 2/5 lines, Im τ 2.0–3.5, one Higgs for all sectors or the pencils listed; not every principled
  Higgs, not every line.

## Seen first

`VERDICT topic-sweep /pencil|one free (Higgs )?direction|inverse.higgs|the nine'?s target|h\.h|null cone/ (full text)`: 35 of 1526 arcs on main match (NEGATIVE 7, OPEN 2, PROVED 26) [corrected 2026-10-24 at Review 70: the arc landed with the placeholder unfilled, which the seen-first gate did not catch (it now does); the sweep run at the review, its count including later arcs].
Bearing on it: B1736, B1739, B1740, B1742, B1730, B1691. **Literature:** standard (modular forms, the Serre derivative).

## Disclosed

- Post hoc throughout: the free optimum and the record's pairs were read (rows 1346) before these scripts ran; the
  pencils were chosen after seeing the target. The pencil scan was first run in the audit room (`audit/verify_p352/`;
  its first launch crashed on an exactly null direction, log 0, and was rerun with singular values floored) and moved
  here with one change (the repository root's depth); rerun here.
- `pencils.py` writes `pencils.json` (every row), not committed; `pencils_run.txt` carries its summary.

## Files

- `verification/target.py` → `target.json`, `target_run.txt`; `verification/pencils.py` → `pencils_run.txt`.
- The lock: `tests/test_b1743_the_principled_pencils_and_the_nines_target.py`.
