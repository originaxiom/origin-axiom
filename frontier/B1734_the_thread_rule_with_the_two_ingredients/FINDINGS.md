# B1734 — THE THREAD RULE WITH THE TWO INGREDIENTS (P-312): PROVED AS SEALED FOR ITS QUESTION — WITH τ AND THE LINE TAKEN FROM THE THREAD ITSELF (ITS APEX AND ITS OWN ORDER-5 AND ORDER-10 LINES, THE BIT COUNTED), THE SIX CHARGED-FERMION RATIOS COME OUT SPECIFICALLY (0.16%); THE NINE DO NOT, AND THE BEST ROW'S DOUBLE RATIO IS GEORGI–JARLSKOG'S EXCLUDED 9

**Verdict: PROVED as sealed for its question (R1–R4 hold, R5–R7 fail, C1 holds)** — and, after the read (§3), carried by one thread pair on an order-5 line (D = 9, excluded) and at the bar once the order restriction is lifted. cc (main), 2026-10-23. Sealed
`afc60475c` (sha256 fc095718) before its instruments ran. The outputs were committed unread at `d9f1b02dc` and read
once. A structure with two ingredients put in by hand and a selection rule, graded a READING, not a value derived.
**0 of 19.**

## 1. The result

B1720's 49 thread classes whose own fixed lines (B1733) include lines of order 5 or 10: 190 points (98 order-5, 92
order-10), each at the thread's apex, both horocycles, 380 rows. Both members of every order-5 pair {v, 2v} are rows,
so the bit is counted. B1726's frame, readings and menus; main's measure and calibration; 20 fresh seeds (1734–1753).
No continuous number is scanned: τ and the line come from the thread.

| cell | prediction | prior | result |
|---|---|---|---|
| **R1** | seat's menu: six within a factor 2 | 45% | **HOLDS**: **1.614** |
| **R2, specific** | seat's menu: ≤ 1% of random hierarchies as good | 25% | **HOLDS**: **0.16%** (every seed ≤ 0.30%) |
| **R3, specific** | covariant menu: ≤ 1% | 15% | **HOLDS**: **0.53%** (every seed ≤ 0.75%) |
| **R4, specific** | factor free: ≤ 1% | 20% | **HOLDS**: **0.69%** (every seed ≤ 1.00%) |
| **R5, specific** | the nine, seat's menu: ≤ 1% | 10% | **FAILS**: 6.5% (best nine 4.58) |
| **R6, unfitted** | ∣J∣ at the best nine-row within a factor 3 of 3.08 × 10⁻⁵ | 8% | **FAILS**: 1.4 × 10⁻¹⁵ |
| **R7, unfitted** | D at the best six-row within 3σ of 10.58 ± 0.11 | 3% | **FAILS**: D = 9.00 exactly (an order-5 line; 14σ) |
| **C1, control** | B1720's stored rows reproduced to 10⁻⁹; B1726's census control | 95% | **HOLDS**: 0.0; 3.9 × 10⁻¹², 1.8 × 10⁻¹¹ |

- **The best six-row** (all three menus): the thread L⁵R² at its apex, on its own order-5 line (2/5, 3/5), L_max, up S̃
  with down and leptons S, c = 3. Model over measured: m_c/m_t 1.17, m_u/m_t 1.53, m_s/m_b 1.61, m_d/m_b 1.07,
  m_μ/m_τ 1.54, m_e/m_τ 1.20. With c free (2.65) the leptons fit within 1.36.
- **The best nine-rows:** seat's menu 4.58 (L⁵R⁴ on its order-10 line (2/5, 1/10), L₂, S̃ throughout, c = 1);
  covariant menu 2.535 (L⁶RLR on (1/10, 3/5)).
- **Not a sealed cell:** the nine under the covariant menu are at 0.43% (every seed ≤ 0.60%).

## 2. What it means (the reading written before the run, applied)

- **R2 holds.** The thread rule with the two ingredients is specific with no continuous number scanned: τ and the
  line come from the thread, up to the bit (counted). The frame's selection reduces to "which thread", plus the two
  ingredients (P-294, P-295). This is the first sealed specific contact in which a rule, not a grid, places τ and the
  line.
- **The limits, in the record's own terms:**
  - The two ingredients are put in by hand. The restriction to orders 5 and 10 was informed by B1726 (disclosed).
  - **The best six-row's double ratio is exactly Georgi–Jarlskog's 9** (an order-5 line with c = 3), which P-094's
    10.58 ± 0.11 excludes at 14σ. So the best row's flavour structure is the classic SU(5) relation the data rule out.
  - The nine are not specific under the seat's menu, and J is zero to rounding at the best nine-row.

## 3. After the read (labelled; `verification/posthoc.py`, not covered by the seal)

- **A, breadth: one thread pair carries it.** Only 2 of the 380 rows come within 2 under the seat's menu: L⁵R² and its
  mirror L²R⁵, both on an order-5 line, where D = 9 exactly. On the order-10 lines the best six is only 3.76.
- **B, the restriction's cost (the honest check).** The full thread rule (every thread's own lines of every order,
  B1720's 3 249 points, 6 498 rows, through the same instrument, readings and menus; 5 seeds) has the same best row
  (1.614). But it is only at the bar under the seat's menu (1.13%, three of five seeds above 1%), and not specific
  under the covariant menu (3.7%). So the restriction to orders 5 and 10, informed by B1726, is what makes the
  covariant cell pass; with every order counted the result sits at the bar.
- **C, THE_BAR.** Bonferroni over the four specificity looks: the seat's six pass (0.0064); the covariant six (0.021),
  the free six (0.027) and the seat's nine (0.26) do not.
- **So the grade:** specific as sealed, but carried by a single thread pair on an order-5 line whose double ratio P-094
  excludes, and at the bar when the order restriction is lifted. A READING, weaker than its cells read alone. P-340
  asks whether any principled restriction keeps the specificity with D near 10.58.
- **For the seats (P-339, the third opinion):** re-run compare.py on census.json; recompute the best rows; check
  B1733's line sets; repeat B with your own instruments.

## Dated note (2026-10-23, B1735; post hoc, labelled)

- **The precision cells** (P-341): the thread rule's rows reach χ²_six 42.3 under the seat's menu (31.3 at the widest), far above
  the bar 16.75, and χ²_nine 441. With τ fitted on B1726's grid the same frame reaches 3.09: the thread's apex does not place τ
  where the values are (P-343).
- **W138's widest menu** (every covariant reading, the factor free) on this census: 2.22%, so the six are not specific under it.

## Dated note (2026-10-23, S201; W141, the SM seat's third opinion, row 1335)

- **The 190 points are 116 distinct (τ, line) points:** 74 are shared by a thread and its mirror (L⁵R² and L²R⁵ among them),
  recounted on main from census.json. A duplicated row changes no minimum and no calibrated fraction, so every cell
  stands; "190 points" overstated the census's breadth. W141 reproduces B1734 in full and, with every order counted,
  puts the seat's six at 1.15% (main's post hoc 1.13%). P-339 DONE.

## Seen first

From the preregistration: `VERDICT topic-sweep /thread rule|thread.s own (point|lines)|threads? with (the )?ingredients|own order-5|apex.*ingredient/ (full text): 2 of 1505 arcs on main match (NEGATIVE 1, PROVED 1)`;
bearing on it are B1720, B1722, B1726, B1728, B1733 and the web seat's sealed all-lines thread test (row 1308).
**Literature:** as the preregistration.

## Disclosed

- Everything in the preregistration's Disclosed.
- The census and the calibration took minutes.
- §3 was written after the read.

## Files

- `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt`.
- `verification/census.py` → `census.json`, `control.json`, `census_run.txt`.
- `verification/compare.py` → `comparison.json`, `compare_run.txt`.
- `verification/posthoc.py` (labelled, after the read) → `posthoc.json`, `allorders.json`, `posthoc_run.txt`.
- The lock: `tests/test_b1734_the_thread_rule_with_the_two_ingredients.py`.
