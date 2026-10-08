# B1613 — TM1'S FORWARD PREDICTION: the weave's one viable mixing relation fixes θ₁₂ from θ₁₃ (sin²θ₁₂ = 0.318) and δ_CP from θ₂₃ up to its mirror — δ ≈ 262.5°, within 252.7°–292.9° over θ₂₃'s 3σ range (or the mirror 67°–107°, outside NuFIT 6.1's 3σ range) — registered as falsifier P10

**Verdict: PROVED** (F1–F3 and D1 hold as sealed). cc (main), 2026-10-08. Sealed `540e12dd0` before `tm1_forward.py` ran
and before any δ_CP value was read. A READING throughout: TM1 rests on FK11 (which sector is the leptons) and on the
residual subgroups selected (B1612). The PMNS is outside the nineteen. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /delta_CP|CP phase|Jarlskog|TM1|theta_23|DUNE|Hyper-K|forward prediction|falsifier/: 36 of 1384 arcs on main match (NEGATIVE 9, OPEN 1, PROVED 26)`
— B1612, B1611, B342, B1066, the falsifier register (P1–P9). **Literature:** the TM1 relations (cited; re-derived and
checked numerically in F1).

## 1. The computation (`tm1_forward.py`; `tm1_forward.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **F1** | the TM1 relations reproduce the column (⅔, ⅙, ⅙) | 99% | **HOLDS** — to 1.9 × 10⁻¹⁶ over 2000 random points, both branches |
| **F2** | central cos δ ≈ −0.13, δ ≈ 97° or 263°; the lower branch inside 240°–300° over θ₂₃'s 3σ range | 80% | **HOLDS** — cos δ = −0.130, δ = 97.5° or 262.5°; 1σ bands 93.2°–101.2° and 258.8°–266.8°; over θ₂₃'s 3σ range (41.27°–49.86°) 67.1°–107.3° and **252.7°–292.9°**; J = ±0.0338 |
| **F3** | TM1 can hold for every θ₂₃ in 40°–50° | 85% | **HOLDS** — no θ₂₃ in 35°–55° fails within θ₁₃'s 3σ range |
| **D1** | against NuFIT 6.1's δ_CP 3σ range (125°–365°, NO): the lower branch inside, the upper outside | 70% | **HOLDS** (that range from a secondary source, as disclosed in the seal) |

## 2. What it says, and the register

If the weave's TM1 reading is right, the leptonic CP phase is not free: with θ₁₃ and θ₂₃ measured it is fixed up to its
mirror, and the data already prefer the lower branch, **δ_CP ≈ 263° (252.7°–292.9°), J ≈ −0.034**, with
sin²θ₁₂ = 0.318. Both are registered as **falsifier P10** (`docs/FALSIFIER_REGISTER.md`): (a) a θ₁₂ measurement more than
3σ from 1 − 2/(3 cos²θ₁₃) kills the reading (S1: the reactor experiments' precision reaches it); (b) a δ_CP
measurement outside both branches kills it (S2: DUNE, Hyper-Kamiokande). A failure kills the TM1 reading, not the weave.

## 3. Disclosed

- The inputs are secondary (NuFIT 6.1 via B1066's source and the search record of 2026-10-08); the central branches
  were estimated by hand before the seal.

## 4. Files

`verification/tm1_forward.py` (sealed, unchanged), `tm1_forward.json`, `tm1_forward_run.txt`. Test:
`tests/test_b1613_tm1s_forward_prediction.py`.
