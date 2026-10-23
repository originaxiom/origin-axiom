# B1732 — THE TWO INGREDIENTS WITH THE HIGGS PF1-W FIXES (P-307): NEGATIVE AS SEALED — WITH F₆ IN PLACE OF ∂R THE SIX CHARGED-FERMION RATIOS STILL FIT (1.62) BUT NOT SPECIFICALLY (7.1% OF RANDOM HIERARCHIES AS GOOD); THE SPECIFICITY WAS ∂R'S

**Verdict: NEGATIVE as sealed for its question** (R1 holds; R2–R5 fail; R6 holds at a non-specific row; R7 fails; C1
holds). cc (main), 2026-10-23. Sealed `65e6abfce` (sha256 edfa5675) before its instruments ran. The outputs were
committed unread at `5f5db8108` and read once. The web seat's zero-free census was not read before that commit.
**0 of 19.**

## 1. The result

B1726's design exactly: its 23 940 points, both horocycles, the covariant readings, the seat, covariant and free menus,
main's measure and calibration, 20 fresh seeds (1732–1751). The one change is the Higgs: F₆ = η⁻³(θ₂⁶, θ₄⁶, iθ₃⁶)
(B1731), the one zero-free Higgs whose invariant has no zero, in place of ∂R.

| cell | prediction | prior | result |
|---|---|---|---|
| **R1** | seat's menu: six within a factor 2 | 35% | **HOLDS**: 1.622 |
| **R2, specific** | seat's menu: ≤ 1% of random hierarchies as good | 20% | **FAILS**: 7.06% (every seed above 1%) |
| **R3, specific** | covariant menu: ≤ 1% | 12% | **FAILS**: 2.08% (every seed above 1%) |
| **R4, specific** | factor free: ≤ 1% | 15% | **FAILS**: 17.6% |
| **R5, specific** | the nine, seat's menu: ≤ 1% | 8% | **FAILS**: 35.8% |
| **R6, unfitted** | ∣J∣ at the best nine-row within a factor 3 of 3.08 × 10⁻⁵ | 5% | **HOLDS**: 1.26 × 10⁻⁵ (a factor 2.4), at a row that fits the nine only within 4.23 |
| **R7, unfitted** | D at the best six-row within 3σ of 10.58 ± 0.11 | 2% | **FAILS**: 9.00 |
| **C1, control** | ∂R path reproduces B1725 to 10⁻⁹; T-covariance with F₆ to 10⁻⁶; F₆'s invariant to 10⁻¹⁰ | 95% | **HOLDS**: 3.9 × 10⁻¹², 8.8 × 10⁻¹², 7.1 × 10⁻³⁹ |

- **Best six rows.**
  - Seat's menu: 1.622 at 0.55 + 3.05i, S̃ throughout, L_max, c = 3. Model over measured: m_c/m_t 1.62, m_u/m_t 1.52,
    m_s/m_b 0.67, m_d/m_b 1.02, m_μ/m_τ 0.64, m_e/m_τ 1.14.
  - Covariant menu: 1.304 at 0.85 + 2.75i on the order-10 line (2/5, 1/2), with up S and down quarks and leptons S̃.
- **Best nine row** (seat's menu): 4.226 at 0.7 + 2.95i, S̃ throughout, L₂.

## 2. What it means (the reading written before the run, applied)

- **R1 holds, R2 fails: F₆ fits but not specifically; the specificity was ∂R's.** On the same 23 940 points, with
  everything else fixed, the Higgs fixed by PF1-W read on both the field and the determinant (B1730, B1731) loses what
  the hand-chosen ∂R had:
  - the seat's menu goes from 0.12% to 7.1% of random hierarchies as good;
  - the covariant menu from 0.41% to 2.1%;
  - the nine from 0.58% to 35.8%.
- **So in B1656's frame, PF1-W read both ways and the two-ingredient fit are incompatible.** The fit needs ∂R. ∂R
  passes the determinant reading on its Higgs factor (∂R·∂R = η⁶/4, P-308) and fails only the field reading (B1730).
  This bears directly on the owner's question P-303. The reading that keeps the frame's one specific contact with the
  masses is the determinant reading alone.
- **R6 is not evidence.** The post hoc base rate below shows J falls within a factor 3 on 18% of all rows, and on half
  of those that fit the nine within 4.5.

## 3. After the read (labelled; `verification/posthoc.py`, not covered by the seal)

- **R6's base rate.** Over every row and both seat-menu CKM pairs, ∣J∣ lies within a factor 3 of PDG's on 17.9% of
  rows, and on 50% of the 20 rows whose nine fit within 4.5. R6 holding at a non-specific row is about a coin flip.
- **Where F₆ fits.** The six (seat's menu) come within 2 at 40 points, all on lines of order 8. ∂R's good rows lie on
  order 5 and 10 (B1726). D at the best rows is about 9.0.
- **Side by side with B1726 at the same rows.**
  - Best six: 1.622 against 1.202 (seat's menu), 1.304 against 1.202 (covariant), 1.622 against 1.202 (factor free).
  - Fractions as good: 7.1% against 0.12%, 2.1% against 0.41%, 17.6% against 0.92%. The nine: 35.8% against 0.58%.

## Seen first

From the preregistration: `VERDICT topic-sweep /F_?6|F₆|theta.?6|θ₂⁶|zero-free Higgs|PF1-W|invariant has no zero|Higgs PF1|fixed Higgs|two.ingredient/ (full text): 56 of 1503 arcs on main match (NEGATIVE 8, OPEN 2, PROVED 46)`;
bearing on it are B1726, B1730, B1731, B1724, B1700, B1727, B1695 and B1713. **Literature:** as the preregistration.

## Disclosed

- Everything in the preregistration's Disclosed.
- The census took 1 h 27 min on 8 workers (the machine was free), the calibration 30 minutes (shared with five
  read-only readers re-evaluating leads L229 and L233–L237 at the owner's ruling).
- `census.jsonl` is tracked through a one-file `.gitignore` exception.
- §3 was written after the read.

## Files

- `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt`.
- `verification/census.py` → `census.jsonl`, `control.json`, `census_run.txt`.
- `verification/compare.py` → `comparison.json`, `compare_run.txt`.
- `verification/posthoc.py` (labelled, after the read) → `posthoc.json`, `posthoc_run.txt`.
- The lock: `tests/test_b1732_the_two_ingredients_with_the_fixed_higgs.py`.
