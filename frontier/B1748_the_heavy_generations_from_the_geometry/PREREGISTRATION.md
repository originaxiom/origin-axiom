# B1748 — PREREGISTRATION: THE HEAVY GENERATIONS FROM THE GEOMETRY ALONE (P-362) — at the apex points of fresh thread classes, on every line, with the Higgs exactly null (no Higgs freedom) and the maximal horocycle as the stated rule, do m_c/m_t, m_s/m_b, m_μ/m_τ and ∣V_cb∣ come out at the data's values, and specifically?

cc (main), 2026-10-24, at the owner's word ("lets do them all PROPERLY") after the night's synthesis (P-362). **Sealed before
`verification/census.py` and `verification/compare.py` run on the fresh points.** A test of a structure (the split the frame's
closed form implies: the channels carry the heavy 2-3 sector, the Higgs's departure from null the first generation), with the
lepton factor by hand and the horocycle chosen by a rule informed by post hoc scans (disclosed). 0 of 19.

## Why

B1736's closed form with B1744's determinant and Lemma A: with the Higgs exactly null the first generation is massless
(det Y = 0), and the heavier masses and the CKM's 2-3 entry are the channels' (∣V_cb∣ = ∣κ_u − κ_d∣, B1745). So the heavy
observables m_c/m_t, m_s/m_b, m_μ/m_τ and ∣V_cb∣ can be read from the geometry alone — the line, τ and the horocycle — with
no Higgs parameter. Post hoc tonight (§ Disclosed) they came out at the data at B1741's apex on the maximal horocycle. **The
question:** on points nobody has computed, placed by B1720's rule, is that agreement reached, and is it specific?

## The model (no data)

- **The points:** the apex points (Im τ = Lagrange(w)/2, B1720) of every primitive thread word of length 10 or 11 with apex
  height in [2.0, 3.6] — classes B1720's census (lengths 2–9, B1741's points) never contained — merged by (Re τ mod 1, Im τ):
  98 points (Im τ 2.03–3.57); × B1713's 266 lines = 26 068 points.
- **The frame:** B1656's four-channel coupling at B1667's canonical end (B1740's instrument through B1742's channel code).
- **The Higgs:** exactly null in every sector — h = n = (0, 1, i)/√2 (ρ(T)'s null eigenline, the cusp limit of R, ∂R and every
  null-led F_a) or its conjugate n̄ (the other reading). No other Higgs and no free direction.
- **The horocycle:** L_max (B1667's maximal) is the stated rule; L₂ is read in comparison cells.
- **The menu:** (n or n̄) × (c = 1 or 3), the lepton factor multiplying m_μ/m_τ (the first generation is not read).
- **The measures:** the coarse worst factor over the four (max ∣log model − log target∣) and χ²_heavy with σ² = (the data's
  relative error)² + 0.10² (B1720's definition), each minimised over rows and menu; the bar for χ²_heavy is the 99th
  percentile of χ² with four degrees of freedom, 13.28.
- **The calibration:** the fraction of random targets reaching as low over the same rows and menu — B1741's generators
  exactly (random hierarchies' second-generation entries for c/t, s/b, μ/τ; random mixings' middle entry for ∣V_cb∣); 20 seeds
  1748–1767, 4 000 targets each.

## Cells

| cell | prediction | prior |
|---|---|---|
| **R1** | on L_max, the best row puts all four heavy observables within a factor 1.25 | 75% |
| **R2, specific** | on L_max, the mean fraction of random targets as good (worst factor) is at most 1% | 15% |
| **P1, precision** | on L_max, some row has χ²_heavy below 13.28 | 70% |
| **P2, precision specific** | on L_max, at most 1% of random targets reach as low a χ²_heavy | 15% |
| L1 | on L₂, no row has χ²_heavy below 13.28 | 40% |
| L2 | L_max's precision fraction is below L₂'s | 55% |
| **C1, control** | (i) the instrument reproduces at B1741's apex (3.4 + 2.993i, (2/5, 9/10), L_max, n) the values main read post hoc (m_c/m_t 0.00350, m_s/m_b 0.0206, the leptons' m₂/m₃ × 3 0.0617, ∣V_cb∣ 0.0384) to 2 × 10⁻³ (they were rounded); (ii) B1724's T-law at a fresh apex to 10⁻⁹ | 95% |

Read-outs: the best rows by each measure on each horocycle; the rows below the bar, their Im τ and lines; the per-seed
fractions.

**The reading, written before the run.**
- **P1 and P2 hold:** the heavy generations at value level and specifically, from the geometry alone at rule-placed τ with
  no Higgs freedom; the split is real, and the Higgs's job is the first generation (P-357). Before any grade: THE_BAR's
  correction for the looks (the six cells' two specificity looks, and × 2 for the horocycle's choice, made after post hoc
  scans) — PASSED only below 0.01 after it. With c = 3 by hand and, on the α = 2/5 lines, m_μ/m_τ tied to m_s/m_b
  (Georgi–Jarlskog), the independent numbers are three.
- **P1 holds, P2 fails:** the heavy sector is reachable at rule-placed τ but not specifically — the geometry spans that
  region generically; no evidence for the split as a prediction.
- **P1 fails:** the post hoc agreement at B1741's apex does not carry to fresh apices.
- **L1 and L2** read whether the horocycle rule matters.
- **A control failing** stops the reading until resolved post hoc, labelled.

## Seen first

`VERDICT topic-sweep /heavy generations?|geometry alone|null Higgs|exactly null|channels alone|horocycle rule|L_max (rule|as the rule)|V_cb from the channels/ (full text): 8 of 1520 arcs on main match (NEGATIVE 3, PROVED 5)`
— B1621, B1657, B1658, B1739, B1740, B1743, B1745, B1746. Bearing on it: B1720 (the thread rule), B1741 (τ at an apex;
P-350, the apex heights fill the window), B1736, B1744 (the determinant), B1745 (∣V_cb∣ = ∣κ_u − κ_d∣), B1728 (the leptons as
the down quarks on order-5 lines), B1726, B1735. None reads the heavy observables from a null Higgs on fresh points.
**Literature:** Georgi and Jarlskog (1979); residual modular symmetry at the cusp (standard); Antusch, Hinze and Saad (P-094).

## Disclosed

- **Known before the seal (post hoc, tonight, in the audit room):**
  - `audit/verify_synthesis/channels_only.py`: with the null Higgs on B1742's grid and three other α families, ∣V_cb∣ and
    m_s/m_b were both within 10% on 58 of 4 864 rows, the best at Im τ 2.6–2.7 on L_max on α = 2/5 lines (∣V_cb∣ 0.041–0.044,
    m_s/m_b 0.018–0.019, m_μ/m_τ 0.054–0.057, m_c/m_t 0.010–0.014).
  - `audit/verify_synthesis/horocycle_scan.py`: at B1741's apex (3.4 + 2.993i, (2/5, 9/10)) on L_max: m_c/m_t 0.00350,
    m_s/m_b 0.0206, m_μ/m_τ 0.0617, ∣V_cb∣ 0.0384 — all within 10%; at B1735's point 0.00276, 0.0185, 0.0556, 0.0356; on L₂
    every heavy ratio 2.5–4 times too small. C1 reproduces the first set.
  - At that apex, one free Higgs read S everywhere reaches χ²_nine 58.7 at best (the first generation does not come cheaply).
- **The horocycle rule is informed by those scans:** L_max is the frame's maximal horocycle (B1667), but it was chosen here
  because the post hoc scans favoured it; L₂ is kept as comparison cells, and THE_BAR's reading carries × 2 for the choice.
- **P1 is close to foreknown:** apex heights fill the band as threads lengthen (P-350), so fresh apices sample Im τ densely; the
  specificity cells (R2, P2) are the test.
- The menu (n, n̄) × (1, 3) mirrors the seat's menu (two readings, two lepton factors).
- The instruments were import-tested and run before the seal on one fresh point to time it (17.5 s with module loading) —
  its values were printed: line 152 at the lowest apex (Im τ 2.03), on L_max with n, m_c/m_t 0.044, m_s/m_b 0.038,
  ∣V_cb∣ 0.082, far from the data — and on C1's and C2's own points (8.3 × 10⁻⁴ and 8.9 × 10⁻¹³). No other fresh value was seen.
- The twenty-seventh sealed test of this frame.

## Instruments

- `verification/census.py` → `census.jsonl`, `control.json`, `census_run.txt`.
- `verification/compare.py` → `comparison.json`, `compare_run.txt`.
- Import-tested; importing computes nothing. `ARTIFACT_HASHES.txt` pins both and the files they read in place.
