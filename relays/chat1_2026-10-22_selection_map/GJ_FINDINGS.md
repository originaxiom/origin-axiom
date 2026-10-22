# The Georgi–Jarlskog factor is what the fibre frame's mass fits are missing (sealed prediction, then post hoc)

chat1, 2026-10-22. On main's frame (B1656's four-channel coupling at B1667's canonical end), read from main's own
committed outputs; no frame value recomputed. 0 of 19.

- **Sealed prediction:** `GJ_WALL_RULE.md` (c42c2be45), committed before chat1 read B1720's rows.
- **Its read:** `gj_wall_read.py` → `gj_wall_read.json`, `gj_wall_read_run.txt` (f13a845e6).
- **Post hoc, labelled:** `gj_posthoc.py` → `gj_posthoc.json`, `gj_posthoc_run.txt`. Every number in §2–§3 was
  computed after the sealed cells were read. The Clebsch 3 was chosen knowing the data's R2 = 3.14.

## 1. The sealed cells (B1720's 6 134 rows with both sectors non-zero)

| cell | prediction | prior | result |
| --- | --- | --- | --- |
| G1 | corr(log R2, log R1) < −0.5 | 80% | **holds**: −0.756 |
| G2 | no row within 0.3 of the data in (log D, log Z) | 85% | **fails**: 4 rows; the closest has D = 9.16, Z = 1.05 |
| G3 | where Z is near the data's, D < 6.7 | 75% | **fails**: D up to 9.16 |

- R2 = (m_μ/m_τ)/(m_s/m_b), R1 = (m_d/m_b)/(m_e/m_τ), D = R2·R1 (the double ratio, P-094), Z = R2/R1. The data:
  R2 = 3.144, R1 = 3.365, D = 10.58, Z = 0.934.
- **The wall as worded is withdrawn.** The four rows that reach the pattern (the thread LLRLLRRLR and its partners,
  height 1.646, an order-29 line) are rows whose hierarchies are far too weak: down m₁/m₃ = 0.045 against 9.4 × 10⁻⁴,
  leptons m₂/m₃ = 0.20 against 0.059. D and Z are ratios of ratios and do not see that. The statistic was the wrong
  one, which the next section corrects, post hoc.

## 2. Post hoc: where the frame fits the hierarchies, it has no Georgi–Jarlskog factor

- **Rows whose four down and lepton ratios are each within a factor 2 of the data** (reading S, both horocycles):
  - B1712: 5 rows, R2 from 0.93 to 1.04;
  - B1713: 8 rows, R2 from 0.93 to 1.40;
  - B1720: 6 rows, R2 from 1.000 to 1.020.

  The data's R2 is 3.14. So where the frame fits, the leptons' second-to-third ratio equals the down quarks'
  (m_μ/m_τ ≈ m_s/m_b): the minimal-SU(5) relation.
- **That sets the frame's precision ceiling.** A row with R2 = 1 must miss m_s/m_b and m_μ/m_τ in opposite directions,
  by at least √3.14 = 1.77 on one of them. B1720's best point misses by 1.80 (m_s/m_b 1.80 high, m_μ/m_τ 0.585 low,
  so its R2 is 1.02).
- **The rows that fit best are the ones where d = e exactly or nearly.** These are B1703's order-5 lines (d = e) and
  the order-10 lines with α = 2/5. The order-5 lines are the tick's own (B1698: det(LR + I) = 5).
  - Mod 5, 6Y is constant on each SU(5) multiplet: 1 on Q, u^c and e^c; 2 on d^c and L.
  - So an order-5 hypercharge line twists like an SU(5)-symmetric element, and the frame returns SU(5)'s relation
    Y_d = Y_eᵀ there.

## 3. Post hoc: with the Georgi–Jarlskog Clebsch put on the leptons

The what-if multiplies the lepton outputs by m_μ/m_τ × c and m_e/m_τ ÷ c, keeping the lepton determinant. That is
Georgi–Jarlskog's (1979) redistribution at c = 3. It acts on the stored singular values, not on the Yukawa matrix, so
it approximates what a Clebsch in the coupling would do.

| census | c = 1 (as computed) | c = 2 | c = 3 | c = 4 | c = 5 |
| --- | --- | --- | --- | --- | --- |
| B1712 (orders 8–12, τ on the CP-line grid) | 2.369 | 1.395 | **1.277** | 1.552 | 1.715 |
| B1713 (orders 1–12, same grid) | 2.326 | 1.395 | **1.277** | 1.476 | 1.549 |
| B1720 (thread apexes, fixed lines) | 1.804 | 1.804 | **1.614** | 1.878 | 1.976 |

- **The best Clebsch is 3 in every census.** The data alone pick it: no other value of the set (⅓ to 5) does better.
- **The best row at c = 3.** It is B1713's order-10 line (2/5, 1/2) (or (2/5, 1/10)) at τ = ½ + 3.1i, the maximal
  horocycle, up reading S̃.
  - Model over measured: m_c/m_t 1.13, m_u/m_t 0.84, m_s/m_b 1.14, m_d/m_b 0.86, m_μ/m_τ 1.08, m_e/m_τ 0.78.
  - The tick's order-5 lines (2/5, ·) at τ = 3.1i come next, at 1.43–1.46.
  - The fit is sharp in Im τ: 1.39 at 3.0, 1.28 at 3.1 and 1.89 at 3.2 on the grid.
- **Main's own calibration** (B1720's prior, seed 1720, 4 000 random hierarchies):

| census | c = 1 | c = 3 fixed | best Clebsch of the set, for the data and for every target alike |
| --- | --- | --- | --- |
| B1713 | 26.6% | **0.20%** | **0.85%** |
| B1720 | 1.65% (main's figure) | 0.53% | 2.25% |

- **The mixing does not follow.** The nine (six ratios and \|V_us\|, \|V_cb\|, \|V_ub\|) go from 3.59 to 2.72 (B1713) and
  from 6.51 to 4.71 (B1720).
  - At the c = 3 mass rows, the up reading S̃ gives \|V_us\| ≈ \|V_cb\| ≈ 0.99, a near-permutation.
  - The reading S gives Cabibbo-sized mixing but worse up masses.
  - Masses and mixing still do not meet at one point.

## 4. What it shows, and what it does not

- **The frame's mass failures are mostly one thing.**
  - Where its hierarchies fit, the leptons copy the down quarks (minimal SU(5)), while the data carry the
    Georgi–Jarlskog factor.
  - With that factor supplied, B1713's τ-free census fits all six ratios within 28% and is specific at main's bar
    (0.85% with the Clebsch's look-elsewhere).
- **Post hoc, not evidence.**
  - The Clebsch was chosen knowing the data.
  - It is applied to outputs, not derived in the frame.
  - The τ is the census grid's.
  - The specificity is an argument for where to look, not a result.
- **The ingredient it names is a law ingredient, not a selection.** A coupling that is not SU(5)-uniform along B − L,
  as Georgi–Jarlskog's 45 (SU(5)) or 126 (SO(10)) does.
  - In this frame the order-5 line is SU(5)-uniform, and the line is the only source of a sector difference.
  - The record's d–e wall (W55, W56: no Higgs content in 27s splits d from e) is the same fact in E₆ language.
- **What remains a selection:** Im τ ≈ 3.1 (the magnitude), which of the tick's lines, the horocycle, and the
  mixing's alignment.
- **What would turn it into a test:**
  - a Clebsch derived in the frame (a coupling whose lepton/down ratio in the middle generation is fixed by the weave);
  - then a sealed census on rows nobody has seen (Re τ off the grid, a finer Im τ, the tick's lines), with main's
    calibration.
