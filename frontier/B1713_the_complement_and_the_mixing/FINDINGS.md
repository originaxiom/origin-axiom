# B1713 — THE COMPLEMENT AND THE MIXING (P-261; P-129, P-164, P-258): NEGATIVE AS SEALED — THE LINES OF ORDER 1–7 DO NO BETTER THAN THE TICK'S ORDER-5 LINES (A FACTOR 2.33 WITH d = e; 14.8% OF RANDOM HIERARCHIES AS GOOD); THE FRAME'S FIRST QUARK MIXING REACHES PDG'S MODULI WITHIN 14%, BUT 59.5% OF RANDOM HIERARCHICAL MIXINGS ARE MATCHED AS WELL — CABIBBO-SIZED MIXING IS GENERIC HERE, NOT SPECIFIC; MASSES AND MIXING TOGETHER FAIL

**Verdict: NEGATIVE as sealed.** cc (main), 2026-10-22.
- **Part A:** H1 holds; H2 and H3 fail.
- **Part B:** K1 holds; K2, K3 and K4 fail.
- **The controls** C1 and C2 hold.

Sealed `cd294dccf` (sha256 1cdf28e5) before the instruments ran, and before B1712's outputs were read. The outputs were
committed unread at `084db486a` and read once. A test of a structure, not a value derived. 0 of 19.

## 1. Part A — the complement (orders 1–7, 62 lines; 15 624 rows)

| cell | prediction (prior) | result |
|---|---|---|
| **A-H1** | some point puts all six ratios within a factor 3 (80%) | **HOLDS** — **2.33** |
| **A-H2, specific** | at most 1% of random hierarchies fit as well (3%) | **FAILS** — **14.8%** (median 3.63; the best 1% reach 1.59) |
| **A-H3** | minimum χ² below 16.75 (3%) | **FAILS** — 162.2 |

- **The best point.** The order-5 line (2/5, 4/5) at Re τ = ½, Im τ = 3.1, L_max, reading S̃.
  - Model over measured: m_c/m_t 0.84, m_u/m_t 0.66, m_s/m_b 1.35, m_d/m_b 0.68, m_μ/m_τ 0.43, m_e/m_τ 2.29.
  - d = e there (B1703's order-5 coincidence), so the double ratio (y_μ y_d)/(y_s y_e) is exactly 1, against the measured
    10.58 (P-094).
  - The best point is B1698's lines and B1698's result, which were seen before the seal.
- **Best per order.** 1: 12 (w = 0); 2: 5.69; 3: 5.63; 4: a massless first generation in every sector (§3); 5: 2.33;
  6: 11.4; 7: 5.35.
- **Read as written before the run.** No line of order 1–7 gives the masses specifically. With B1712 (orders 8–12), no
  line of order ≤ 12 does.

## 2. Part B — the quark mixing on every order 1–12 (266 lines; 67 032 rows)

This is the first computation of the CKM in B1656's four-channel frame at the canonical end: B1660's blind rule.

| cell | prediction (prior) | result |
|---|---|---|
| **K1** | PDG's ∣V_us∣, ∣V_cb∣, ∣V_ub∣ all within a factor 3 at some point (30%) | **HOLDS** — **1.14** |
| **K2, specific** | at most 1% of random hierarchical mixings fit as well (5%) | **FAILS** — **59.5%** (median 1.12; the best 1% reach 1.02) |
| **K3** | all nine within a factor 3 at one point (10%) | **FAILS** — 3.59 |
| **K4, specific** | at most 1% of random nine-target sets fit as well (2%) | **FAILS** — 21.6% |
| **C1**, unitarity | max ∣VV† − 1∣ < 10⁻¹⁰ (99%) | **HOLDS** — 4.0 × 10⁻¹⁵ |
| **C2**, B1712 reproduced | the ratios on orders 8–12 to 10⁻⁹ (97%) | **HOLDS** — identical |

- **The best three-moduli point.** The order-11 line (0, 5/11) at Re τ = ½, Im τ = 2.8, L_max, reading S*.
  - ∣V_us∣ = 0.253, ∣V_cb∣ = 0.0368, ∣V_ub∣ = 0.00343, against PDG's 0.2250, 0.0418 and 0.00373.
  - **J = 2.83 × 10⁻⁵** there, a read-out; PDG's is about 3.1 × 10⁻⁵. Given the moduli, that is sin δ ≈ 0.92, and about
    26% of uniformly random phases give at least that. With K2 failing it carries no weight.
  - The right-vector convention gives 0.310, 0.0418 and 0.0043 at the same point.
- **What K2 means.** The frame's rows cover the space of hierarchical mixings so densely that a random target is
  matched within 12% half the time.
  - So the measured CKM's match within 14% is what the frame does for almost any mixing.
  - The mixing is produced, and Cabibbo-sized mixing is generic here, but it is not produced specifically.
- **What K3 means.** At one point the masses and the mixing come no closer than a factor 3.59, and a fifth of random
  nine-target sets do as well.
- **Best per order (moduli).**
  - 1: 1.75; 2: 2.04; 3: 2.67; 4: degenerate (§3); 5: 1.64; 6: 1.65.
  - 7: 1.25; 8: 1.33; 9: 1.35; 10: 1.23; 11: 1.14; 12: 1.17.
- **J (P-164).** On every line except the order-4 lines, J is non-zero somewhere on the grid; the largest ∣J∣ is 0.091.
  - On the order-4 lines J vanishes, because both quark sectors' first generation is massless there.
  - At Re τ ∈ {0, ½} CP violation is therefore generic in this frame.
  - The CP transformation's action on the frame at these τ is not derived here; this is the computed J.
- **The double ratio at the best nine:** 8.46, against 10.58 ± 0.11. A read-out, not a cell; Barger's 10.714 was seen.

## 3. The blind test of P-268's law (committed before this read, `5063a0f9d`)

**The law.** Written from B1712's order-12 zero, read after B1712's run: a sector's first generation is exactly massless
at the canonical end, for every Higgs, when its left twist has exact order 4 and its right twist order ≤ 2.

**Its prediction for this output:** every order-4 line massless in all three sectors, and no zero from this mechanism on
orders 1–3 or 5–7.

**Read here:**
- every order-4 line: up, down and leptons all have m₁/m₃ ≤ 5.4 × 10⁻¹⁴ (18 of 18 line-sectors);
- no line of order 1, 2, 3, 5, 6 or 7 has an exact zero in any sector;
- with B1712: on all 266 lines of orders 1–12, the exact first-generation zeros are exactly the law's (order-4 lines in
  every sector, order-12 lines in the leptons) and nowhere else.

**The prediction holds.** The mechanism (the channels pair, so det M = 0) is derived and checked in B1716.

## 4. What it means

- **The line census is complete to order 12 and does not select a line.** Every line the record selects, and every line
  of order ≤ 12, fails specifically in this frame (B1698, B1711, B1712, this arc).
- **The Cabibbo question (P-129), answered in this frame.**
  - B1649's zero belonged to point couplings (rank ≤ 2, B1653).
  - At the canonical end the four-channel coupling has rank three, and mixing of every size occurs.
  - The measured mixing is reproduced within 14%, but not specifically.
  - The frame is missing a principle that selects the point, not a mixing mechanism.
- **The structure the census found is exact.** The first-generation zeros follow a law that predicted unseen lines
  (§3).

**What it does not do.**
- τ off the two CP lines.
- Orders above 12.
- Other Higgs sections.
- The PMNS (no neutrino sector).
- A selection principle.

## 5. Seen first

As sealed (`PREREGISTRATION.md`):
- `VERDICT topic-sweep /CKM|Cabibbo|Jarlskog|V_us|V_cb/ (full text): 45 of 1484 arcs on main match (NEGATIVE 13, PROVED 32)`.
- Part A: `… /CKM|Cabibbo|V_us|V_cb|Jarlskog|mixing matrix|complement/ …: 196 of 1484 arcs`.
- None computes the mixing in this frame. **Literature:** PDG 2025 §12 (pinned in B1612's `data.json`); Antusch, Hinze and
  Saad for the double ratio.

## 6. Disclosed

**As sealed:**
- B1698's order-5 lines were seen (2.33).
- B1712's outputs were unread at the seal.
- No model mixing value in this frame was seen.
- The CKM function was checked on random matrices only.

**After the read:**
- §2's read-outs (J by line; the best per order) and §1's best per order, from the stored outputs;
- §3's check of the prediction, from the stored output.

## Files

- `PREREGISTRATION.md` (sealed) and `ARTIFACT_HASHES.txt`.
- `verification/the_complement_and_mixing.py` → `the_complement_and_mixing.json`, `_run.txt`.
- `verification/compare.py` → `comparison.json`, `compare_run.txt`.
- `verification/b1656_funcs.py`.
- The lock: `tests/test_b1713_the_complement_and_the_mixing.py`.
