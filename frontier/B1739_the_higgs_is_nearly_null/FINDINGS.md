# B1739 — THE HIGGS IS NEARLY NULL (P-344): THE FRAME'S HIGGS TRIPLET HAS h·h = η⁶/4 EXACTLY, SO ITS REALITY r = ∣h·h∣/∣h∣² FALLS LIKE e^{−π Im τ}; EACH SECTOR'S LIGHTEST STATE SITS ON h̄ (READING S) OR h (READING S̃), SO UNDER THE STANDARD MODEL'S READING (H̃ FOR UP, H FOR DOWN) THE LIGHTEST UP AND DOWN STATES ARE NEARLY ORTHOGONAL AND ∣V_ud∣ ∝ r^½ — THE HIERARCHY AND AN UNMIXED LIGHT GENERATION EXCLUDE EACH OTHER

**Verdict: PROVED** (an exact identity, an exact lemma, and a census law at log-correlation 0.996 on B1726's committed
rows; no new data contact). cc (main), 2026-10-23. **0 of 19.**

## 0. Why

P-344 (from B1735's instruments, post hoc): on B1726's grid the six's χ² minimum needs up S̃ with down S, where the CKM
is 4–24 times too large, while the nine's minimum has S̃ in every sector, where the CKM is within a factor 2 but the six
miss. B1736's closed form Y = u hᵀ + h uᵀ − (u·h)1 + u₁[h]_× suggested why: the light states follow the null line of
u₁[h]_×. This arc computes the mechanism and reads the census.

## Seen first

`VERDICT topic-sweep /null (vector|direction|triplet|Higgs)|isotropic|h·h|h\.h|Jacobi'?s (identity|quartic)|V_ud|light(est)? states? (align|orthogonal)|reality of the Higgs/ (full text): 40 of 1511 arcs on main match`.

B1731 computed F_a·F_a for the zero-free lines (F₆·F₆ = −48η⁶) as a zero-free invariant; no arc reads h·h as the
triplet's reality or ties it to the mixing.

Bearing on it: B1736 (the closed form), B1724 (S̃ conjugates the components), P-308 (∂R·∂R = η⁶/4, stated in the
register), B1726 and B1735 (the census and the precision cells). **Literature:** Jacobi's identity θ₃⁴ = θ₂⁴ + θ₄⁴;
standard.

## Disclosed

- The census read in §3 was first done in the audit room (`audit/verify_p344/`) on the same committed rows, after
  B1726's stored CKM at the six's best point was read (S̃/S 4.4, 23.8, 10.6 of the data; S/S 0.54, 1.59, 0.06; S̃/S̃ 0.17,
  0.85, 0.38). The mechanism was proposed before the census table was computed.
- A first run counted points where u₁ = 0 (B1716's residue zeros, where Y₀ = 0 and the SVD is arbitrary) in the u = 0
  lemma check; they are excluded in the recorded run.

## 1. The Higgs is nearly null (part A)

- **R = (−θ₂², −θ₄², iθ₃²)/(θ₂θ₃θ₄) is exactly null:** R·R ∝ θ₂⁴ + θ₄⁴ − θ₃⁴ = 0 (Jacobi), to 10⁻³¹.
- **The section the censuses use (B1691's components) has h·h = η⁶/4 exactly** — the ratio is 1 with phase 0 to
  10⁻¹³ at 21 points (Re τ 0.05, 0.35, 0.7; Im τ 1.0–4.0): P-308 confirmed.
- **So its reality r = ∣h·h∣/∣h∣² falls like ∣q∣ = e^{−π Im τ}**, almost independent of Re τ: 0.98 (Im τ 1.0), 0.49
  (1.5), 0.127 (2.0), 0.028 (2.5), **0.0058 (3.0)**, 0.0012 (3.5), 0.00025 (4.0). At the hierarchy band the Higgs
  triplet is null to a few parts in a thousand, and for a null h, h̄ is Hermitian-orthogonal to h.
- **Why (part D).** ρ(T) = e^{iπ/4}(1 ⊕ R₋₉₀°) has three eigenlines: e_i (phase 1/8, not null) and (0, 1, ±i) (phases −1/8
  and 3/8), **both null**. The sections on record are led at the cusp by their θ₃- and θ₄-type components, which lie on
  a null eigenline; the θ₂-type component on e_i vanishes there. **The zero-free F₆ (B1731) is nearly null too:**
  F₆·F₆ = −48η⁶ exactly, reality 0.81 (Im τ 1.0), 0.045 (2.0), 0.0093 (2.5), 0.0019 (3.0), 8 × 10⁻⁵ (4.0).

## 2. The light state follows the null line (part B)

- **Lemma (exact).** If u = 0, Y = u₁[h]_× and its left null vector is h̄: Yᴴv = −ū₁[h̄]_× v vanishes iff v ∥ h̄. Under
  the reading S̃ the Higgs is h̄ and the left null vector is h. Checked to 4 × 10⁻¹⁶ wherever u₁ ≠ 0.
- **With the channel triplet on** (24 seeded points of B1726's grid, every sector, B1736's closed form equal to the
  frame to 4 × 10⁻¹⁶): the lightest left singular vector overlaps h̄ under S with median 0.999 (10th percentile 0.54)
  and h under S̃ with median 0.999 (10th percentile 0.92).

## 3. The census law (part C, B1726's committed rows)

∣V_ud∣ = √(1 − ∣V_us∣² − ∣V_ub∣²) from the stored moduli, 47 880 rows per (up, down) reading:

| up / down | median ∣V_ud∣ | above 0.9 | median at Im τ 2.0–2.5 | 2.5–3.0 | 3.0–3.5 |
|---|---|---|---|---|---|
| S / S | 0.996 | 81% | 0.980 | 0.997 | 1.000 |
| S̃ / S̃ | 0.994 | 81% | 0.975 | 0.995 | 0.999 |
| **S̃ / S (the Standard Model's reading)** | **0.281** | 19% | 0.565 | 0.265 | **0.105** |
| S / S̃ | 0.114 | 21% | 0.467 | 0.098 | 0.022 |

Per τ, the median ∣V_ud∣ under the mixed readings follows r(τ): **log-correlation 0.996 with slope 0.52 for S̃/S**
(∣V_ud∣ ∝ r^½ ∝ e^{−π Im τ/2}) and 0.998 with slope 0.97 for S/S̃.

## 4. What it means

- **Under the Standard Model's reading the frame cannot have both a hierarchy and an unmixed light generation.** The
  hierarchy needs Im τ ≳ 2.5 (B1667, B1735: the six at Im τ ≈ 3.05); there the Higgs is null to r ≈ 0.006, the
  lightest up and down states lie near h and h̄, which are nearly orthogonal, and ∣V_ud∣ ≈ 0.1. The data's 0.974 would
  need r of order one, Im τ ≈ 1, where the frame has no hierarchy. This is why B1735's nine fail (χ² 109) and why the
  six's best row carries a CKM 4–24 times too large.
- **The same readings align the light states** (∣V_ud∣ ≈ 0.995 at the band), which is why the nine's best row has S̃
  throughout — but that reading misses the six (χ² 52.7).
- **What would lift it:** a Higgs that is not null at hierarchy τ — one led at the cusp by the non-null eigenline e_i,
  which no Higgs on record is (∂R and F₆ are both nearly null there) — or a reading rule other than the Standard Model's
  that still gives the six (P-295). Either is a test to seal with the precision cells (P-341). This bears on P-303
  (PF1-W's Higgs) and on the web seat's zero-free tests (P-316): a zero-free Higgs led by θ₃/θ₄ is nearly null too.
- **The count:** this is a structural constraint inside the frame, not a value; it removes the mass-fitting reading as
  a route to the nine with this Higgs. 0 of 19.

## Dated note (2026-10-24, S216; the web seat's e9, row 1364)

- **The obstruction holds for every scalar part.** With the Higgs quaternion's scalar part h₀ restored (S = h₀ + h·Q;
  zero in every census since B1700), det Y = N(S) N(M) ⟨S, M⟩ (B1744's formula), and at a null quaternion
  (h₀² + h·h = 0) every sector's light left state is the conjugate of the null eigenvector of [h]_× with eigenvalue h₀.
  Under the Standard Model's reading the up and down light states are then orthogonal: ∣V_ud∣ = 0. Verified on main
  (`audit/verify_split/e9_check.py`): 40 random null quaternions with h₀ ≠ 0 at B1741's apex and 40 at B1735's point give
  ∣V_ud∣ ≤ 1.8 × 10⁻¹⁴ and a light down mass zero to 1.6 × 10⁻¹⁶. § 2's law is the h₀ = 0 case.

## Files

- `verification/the_higgs_is_nearly_null.py` → `the_higgs_is_nearly_null.json`, `the_higgs_is_nearly_null_run.txt`.
- The lock: `tests/test_b1739_the_higgs_is_nearly_null.py`.

## Dated note (2026-10-29, S242; the web seat's audit, harvest row 1461, verified on main (S242): the seat's audit_checks.py parts C, D, E run against main's checkout reproduce its committed lines exactly, and b1740_floor.py likewise)

- **The power law is a property of the median, not of the distribution.** § 3's "∣V_ud∣ ∝ r^½" (slope 0.52 for S̃/S) holds
  for the median only. The quantile slopes of ln ∣V_ud∣ against ln r are 1.24, 1.14, 0.52 and 0.22 at q = 0.10, 0.25,
  0.50 and 0.75. So P-345's "∝ r^½ ≈ 0.1" is unearned as a law.
- **The 52.7 is not that reading's least.** § 4's "that reading misses the six (χ² 52.7)" is the six at the nine's best
  row. The all-S̃ reading's own least χ²_six is 22.36 (B1726's least per assignment, with B1740's compare.py).
- **Unchanged:** the exclusion on its grid (no row with both a hierarchy and ∣V_ud∣ ≥ 0.97 reaches the six: the least
  χ²_six among the 6 151 such rows is 387.4).
