# B1725 — THE TWO INGREDIENTS ON MAIN (P-293): THE WEB SEAT'S CENSUS REPRODUCED WITH MAIN'S CODE; WITH THE CHOICE OF INGREDIENTS COUNTED, THE SIX CHARGED-FERMION RATIOS STAY SPECIFIC UNDER EVERY MENU, THE NINE DO NOT

**Verdict: PROVED** (a verification arc: a seat's sealed result reproduced and recalibrated on main). cc (main),
2026-10-22. **0 of 19:** the result rests on two ingredients put in by hand.

## 0. What the web seat did

The web seat sealed `TWO_INGREDIENTS_RULE.md` (`9387ed764`, on its branch) before its census ran. It used main's frame
unchanged: B1720's instrument (B1656's coupling, the section ∂R, B1667's canonical end at both horocycles). The census
covered B1713's 266 lines at Re τ ∈ {0.1, 0.4}, Im τ 2.0–3.5 (8 512 points). Two ingredients were added by hand:
- **I1, the lepton factor:** m_μ/m_τ × 3 and m_e/m_τ ÷ 3 (the Georgi–Jarlskog Clebsch);
- **I2, one reading:** S̃ = εS*εᵀ for every sector, the CKM from the up and down couplings both read with S̃.

All four sealed cells held: the six ratios within 1.513 (0.725% of 4 000 random hierarchies as good, seed 1720) and the
nine (with ∣V_us∣, ∣V_cb∣, ∣V_ub∣) within 2.087 (0.475%), at τ = 0.4 + 2.7i on order-10 lines at the second horocycle.
The ingredients were chosen after a post hoc reading of main's committed rows, disclosed in the seal.

## 1. The census reproduced (`verification/reproduce.py`)

48 points drawn at random (seed 1724) were recomputed with main's frame functions in this arc's own loop: every sector in
every reading at both horocycles, and the CKM for every (up, down) pair, 36 keys per point. **Every value agrees to
6.9 × 10⁻¹⁰ in log, and J to 4.4 × 10⁻¹⁵.** That is the frame's own numerical agreement level (its covariance checks run
from 10⁻¹⁰ to 10⁻⁷, B1724), just inside this arc's bar of 10⁻⁹. The census is main's frame, correctly computed.

## 2. Recalibrated with the choice counted (`verification/recalibrate.py`)

The seat's calibration fits each random target with the one configuration chosen after seeing the data. Here every
random target gets the same freedom the choice had, on the same rows, and its own best over the menu is compared with
the data's best over the same menu:
- **sealed:** (S̃, S̃, S̃) with the factor 3, as the seat sealed it;
- **seat menu:** the four configurations the seat compared, {main's readings (S̃, S, S), S̃ for all} × factor {1, 3};
- **factor free:** the seat's two reading rules with the lepton factor c continuous (only m_μm_e/m_τ² is constrained);
- **all readings:** every (up, down, lepton) reading, 27, × {1, 3};
- **covariant readings:** the same over S and S̃ only, 8 × {1, 3} (B1724: S* is not SL(2, ℤ)-covariant).

| menu | six: data's best | seed 1720 | seeds 100–119 (mean ± s.e.) | seeds ≤ 1% | nine: data's best | seed 1720 | seeds 100–119 | seeds ≤ 1% |
|---|---|---|---|---|---|---|---|---|
| sealed (S̃, S̃, S̃), factor 3 | 1.513 | 0.725% | 1.17% ± 0.04% | 5 of 20 | 2.087 | 0.475% | 0.56% ± 0.02% | 20 of 20 |
| the seat's menu (4) | 1.270 | 0.25% | 0.29% ± 0.01% | 20 of 20 | 2.087 | 0.97% | 0.98% ± 0.04% | 11 of 20 |
| the factor free | 1.204 | 0.73% | 0.58% ± 0.02% | 20 of 20 | 2.087 | 2.25% | 1.95% ± 0.06% | 0 of 20 |
| the covariant readings (16) | 1.270 | 0.92% | 0.97% ± 0.03% | 14 of 20 | 2.087 | 2.93% | 3.00% ± 0.06% | 0 of 20 |
| all readings, S* included (54) | 1.204 | 0.43% | 0.50% ± 0.02% | 20 of 20 | 2.087 | 6.88% | 6.36% ± 0.08% | 0 of 20 |

## 3. What it means

- **The seal reproduces:** at seed 1720 the sealed configuration gives exactly the seat's fractions, 0.725% and 0.475%
  (29 and 19 of 4 000; the seat printed them rounded, 0.73% and 0.47%). Over seeds
  100–119 its six sit at the bar (1.17%), its nine below it (0.56%), as the seat's own robustness check found.
- **The six with the choice counted.** Under the seat's own menu the data's best improves to 1.270 (main's readings with
  the factor 3) and 0.29% of random hierarchies fit as well, every seed below the bar; with the lepton factor free (only
  m_μm_e/m_τ² constrained) 0.58%, every seed below the bar. **Under every covariant reading assignment** (S or S̃ per
  sector, 8, × the factor {1, 3}) **the six sit at the bar: 0.97%, 14 of 20 seeds.** The wider menu that includes S*
  gives 0.50%, but its best row (1.204) uses the non-covariant S* (B1724) and is set aside.
- **So the six's specificity depends on the reading rule.** With one of the seat's two rules it is clear; with the reading
  free per sector it is marginal. A derived reading rule (P-295) is therefore part of the evidence, not a side question.
- **The nine are not specific once the choice is counted beyond the seat's menu:** 0.98% with it (11 of 20 seeds), 1.95%
  with the factor free, 3.0% under every covariant reading.
- **The lepton factor is the bottleneck it was said to be.** Without it the same rows give the six only within 2.34
  (14% of random hierarchies as good, the seat's read-out); with it, 1.27.
- **What it is not.** Two ingredients are put in by hand; the rows neighbour rows where they were chosen; J is 16–40 times
  too small and P-094's double ratio D is missed (the seat's read-outs). This is a structure with two hand-put
  ingredients that reproduces the charged-fermion hierarchy's pattern within a factor 1.3 to 1.5, specifically under a
  narrow reading rule. It derives nothing.
- **Next:** B1726, main's sealed replication on rows nobody has computed, with both menus (the seat's and the covariant
  one) as cells, the covariant readings only, and J and D as cells; P-294 (the factor 3 from anomaly cancellation);
  P-295 (the reading rule).

## Seen first

`VERDICT topic-sweep /two ingredients|Georgi|Jarlskog|Clebsch|lepton factor|one reading for every sector/ (full text): 30 of 1497 arcs on main match (NEGATIVE 11, PROVED 18, no verdict file 1)`.
Bearing on it: B1340 (M_d = M_eᵀ is the SU(5) 5̄'s relation, one matrix equation for m_b/m_τ, m_s/m_μ and m_d/m_e); B1670 (Georgi–Jarlskog at M_Z graded approximate, 3.15 and 3.39); B1712, B1713, B1720 (main's frame without the ingredients); B1724 (the readings' covariance). None adds the factor or the one-reading rule to main's frame. **Literature:** Georgi and Jarlskog (1979), the 45-dimensional Higgs's Clebsch −3; the Standard Model's H̃ for the up quarks.

## Disclosed

- The census is the seat's computation, copied unchanged (`received/PROVENANCE.md`); main recomputed a random sample.
- Main's recalibration was first run in the audit room on the same census (seed 1720 and seeds 100–119, four menus),
  then re-run here with the covariant menu added. The numbers were seen before this arc was written; it seals nothing.
- The seat's census rows neighbour rows where the ingredients were chosen (Re τ ∈ {0, ¼, ½}), as the seat disclosed.

## Files

- `received/two_ingredients_census.jsonl` and `received/PROVENANCE.md`.
- `verification/reproduce.py` → `reproduce.json` (§1).
- `verification/recalibrate.py` → `recalibrate.json`, `recalibrate_run.txt` (§2).
- The lock: `tests/test_b1725_the_two_ingredients_on_main.py`.
