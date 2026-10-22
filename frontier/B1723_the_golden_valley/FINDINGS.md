# B1723 — THE GOLDEN VALLEY (the completion map's C3; L254, P-069): NEGATIVE AS SEALED — THE VALLEY OF THE WEAVE'S MODULAR-INVARIANT F AT ITS GOLDEN VALUE SITS TOO LOW FOR THE FRAME'S HIERARCHY; NO FUNCTIONAL WITH THIS VALLEY PRODUCES THE SIX RATIOS IN THIS FRAME

**Verdict: NEGATIVE as sealed (T1 fails, as the preregistration expected).** cc (main), 2026-10-22. Sealed `23f8a7621`
(sha256 3850a2f9) before its instruments ran. The outputs were committed unread at `8951e7afc` and read once.
**0 of 19.**

## 1. The result

49 points on the valley (the two mirror arcs from i to ±½ + (√5/2)i, where F = Σ_p ∣θ_p/η∣⁴ = 8) × 265 lines of order
2–12, both horocycles, three up readings: 77 910 mass rows.

| cell | prediction | result |
|---|---|---|
| **T1** | some row puts all six ratios within a factor 3 | **FAILS**: the best worst factor is **147** |
| **T2, specific** | at most 1% of 4 000 random hierarchies fit as well | **FAILS**: 26.6% (random median 254) |
| **T3** | the minimum χ² is below 16.75 | **FAILS**: 3 891 |
| **K1** | some row puts ∣V_us∣, ∣V_cb∣, ∣V_ub∣ within a factor 3 | **HOLDS**: 1.51 |
| **K2, specific** | at most 1% of random mixings fit as well | **FAILS**: 30.2% (random median 1.99) |
| **K3** | some row puts all nine within a factor 3 | **FAILS**: 147 |
| **K4, specific** | at most 1% of random nine-target sets fit as well | **FAILS**: 25.6% |
| **C1, control** | T at the apexes and S at i give the same ratios, bar 10⁻⁶ | **HOLDS**: 1.6 × 10⁻¹³ and 6.2 × 10⁻¹⁴ |

**The read-outs.**
- **The best mass row** is at τ = 0.094 + 1.042i (the right arc, arclength 0.381 of log φ = 0.481), on the order-11 line
  (1/11, 10/11), at L_2 with the S̃ reading. Model over measured: 134, 147, 40, 17, 11 and 71. Every ratio is too large:
  the masses are too close together.
- **The best χ²** is at the apex ½ + (√5/2)i, on the order-3 line (0, ⅓).
- **The best per line order:** 264 (order 2), 349 (3), 239 (5), 293 (6), 161 (7), 231 (8), 171 (9), 175 (10) and 147
  (11). Orders 4 and 12 carry B1716's exact first-generation zero.
- **The best mixing row** is at τ = −0.018 + 1.009i, next to i, on the order-5 line (⅖, ⅖), at L_max with the S*
  reading. Its moduli are 0.201, 0.0288 and 0.00564 (PDG: 0.225, 0.0418, 0.00373), and J = 1.30 × 10⁻⁵ (PDG: 3.08 × 10⁻⁵).
  But 30% of random mixings fit as well, so it is generic.

## 2. What it means

**Read as written before the run** (T1 fails): the valley sits too low (Im τ ≤ 1.118) for the frame's hierarchy. No
functional whose valley is the golden locus produces the six ratios in this frame, and C3 is closed in it. The golden
spectrum stays B1636's, in the older coupling.
- **The depth is the issue, not the pattern.** Over the valley's rows the median first-to-third ratio is 10⁻¹·¹ in each
  sector (the data: 10⁻⁵·¹ for the up quarks, 10⁻³·⁰ for the down quarks, 10⁻³·⁶ for the leptons). The frame's hierarchy
  grows with Im τ, and every test that came near the data sat at Im τ ≈ 2.7–3.1 (B1712, B1713, B1720).
- **No valley point is better than chance.** 26.6% of random hierarchies fit as well, so the valley does not even
  carry a weak preference.

**What it does not do.**
- Functionals with other valleys, or with F at another value. A functional whose valley crosses Im τ ≈ 3 is not
  touched.
- Other frames. B1636's older coupling, where the golden spectrum lives, is not tested here.
- A second term along the valley. None is needed: no point of the valley passes.

## 3. After the read (labelled): the lepton factor 3 does not rescue the valley

The web seat's sealed TWO_INGREDIENTS test (2026-10-22, on its branch) put the Georgi–Jarlskog factor 3 on the leptons
(m_μ/m_τ × 3, m_e/m_τ ÷ 3) in this frame. B1723's stored rows carry the down quarks and leptons in the S reading only,
so one variant is computable from them: main's readings with that factor. Its best worst factor is **138** (at
τ = −0.018 + 1.009i, line (0, 5/11)), against 147 without it. The valley's failure is the hierarchy's depth in every
sector, which no lepton factor can supply.

## Seen first

`VERDICT topic-sweep /golden valley|discriminant-5|discriminant 5 (locus|geodesic)|F ?= ?8|tau as a field|τ as a field|modular-invariant (potential|functional)|valley/ (full text): 48 of 1494 arcs on main match (NEGATIVE 4, OPEN 2, PROVED 41, RETRACTED 1)`.
Bearing on it:
- B1636 (the golden spectrum; F = 8 on the tick's geodesic);
- B1638 and B1639 (the golden identity);
- B1657 (D vanishes on ω's orbit);
- B1712, B1713 and B1720 (the frame's line census and the threads' apexes).

**Literature:** modular-invariant potentials for the modulus and their minima at or near the fixed points (the
modular-flavour vacuum-stabilisation literature); standard.

## Disclosed

- **As sealed:**
  - the expected direction (T1 to fail; B1720's LR apex, the valley's top, was 4 506 off);
  - the covariance pre-check (T ≤ 1.5 × 10⁻¹³, S ≤ 6.2 × 10⁻¹⁴), comparing only across bases;
  - the redundancies (S at i, the mirror arcs, B1713's Re τ = 0 family at i, the order-4 and order-12 zeros);
  - L read from B1667's Re τ = ¼ column.
- **After the run, before the read:** nothing removed. Both exit codes 0; the instruments' hashes matched the seal.
- **The run took 2 h 0 min** on 8 workers, against an estimate of 60–80 min.

## Files

- `PREREGISTRATION.md` (sealed) and `ARTIFACT_HASHES.txt`.
- `verification/the_golden_valley.py` → `the_golden_valley.json`, `the_golden_valley_run.txt`.
- `verification/compare.py` → `comparison.json`, `compare_run.txt`.
- `verification/b1656_funcs.py` (B1656's functions, verbatim).
- The lock: `tests/test_b1723_the_golden_valley.py`.

## Addendum 2026-10-22 (B1724): the reading S* is not SL(2, ℤ)-covariant; the mixing best was an S* row

B1724 found that of B1660's three up readings, S and S̃ are SL(2, ℤ)-covariant in this frame, and S* is covariant exactly
under Γ⁰(2) (index 3). **The mixing best (1.51, next to i) was an S* row,** one sheet's value; with the covariant readings
it is **1.851** (40.20% of random mixings as good). Every verdict stands: the mass cells fail (147 either way). The
control C1 tested S only; S̃ passes the same comparisons (B1724).
