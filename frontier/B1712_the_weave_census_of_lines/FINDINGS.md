# B1712 — THE WEAVE CENSUS OF LINES (P-260): NEGATIVE AS SEALED — EVERY FLAT LINE OF ORDER 8–12 TESTED TOGETHER, THE BEST POINT IS A FACTOR 2.37 OFF, BUT 22% OF RANDOM HIERARCHIES FIT AS WELL WITH THE SAME 51 408 ROWS: THE LINE IS NOT WHERE THIS FRAME'S MISSING NUMBER LIVES

**Verdict: NEGATIVE as sealed (H1 holds; H2 and H3 fail).** cc (main), 2026-10-22, at the owner's choice of 2026-10-22
("Weave census of lines"). Sealed `a35ab5642` (sha256 c4856e37) before its instruments ran; the outputs committed unread
at `ba2fea64d` and read once. A test of a structure, not a value derived. 0 of 19.

## 1. The model and the result

**The model (no data).**
- **Lines.** Every flat line w = ατ + b of exact order 8 ≤ N ≤ 12, up to sign: 204 lines. By B1703, each splits all three
  charged sectors, and nothing on record selects among them.
- **The frame.** The end-data Higgs ∂R; B1667's canonical end; B1656's four-channel coupling.
- **The grid.** Re τ ∈ {0, ½}, Im τ = 1.5–3.5, both horocycles, three up readings: one continuous number and 2 448
  discrete choices.
- **The calibration** fits each of 4 000 random hierarchical target sets with the same 51 408 rows, so the look-elsewhere
  count is inside H2.

**Against the data** (Huang–Zhou 2021 at M_Z):

| cell | prediction (prior) | result |
|---|---|---|
| **H1** | some point puts all six ratios within a factor of 3 (55%) | **HOLDS** — best worst factor **2.37** |
| **H2, specific** | at most 1% of random hierarchies fit as well (3%) | **FAILS** — **22.45%** fit as well (median 3.23; the best 1% reach 1.47) |
| **H3** | minimum χ² below 16.75 (3%) | **FAILS** — 108.5 |

- **The best point.** The order-8 line (3/8, 0) at Re τ = 0, Im τ = 3.1 (inside the grid), L_max, up reading S̃.
  - Model over measured: m_c/m_t 0.88 and m_u/m_t 2.04; m_s/m_b 2.37 and m_d/m_b 1.17; m_μ/m_τ 0.65 and m_e/m_τ 0.57.
  - d and e are split there: m₂/m₃ is 0.044 for the down quarks and 0.038 for the leptons, against the measured 0.019
    and 0.059. The order-8 line does not reproduce the data's d–e pattern; the down quarks' m₂/m₃ is the worst ratio.
- **Best per order.**
  - 8: 2.37.
  - 9: 4.17, the line (2/9, 2/9) at Im τ = 3.5, the grid's edge (B1711's point).
  - 10: 2.42, the line (2/5, 1/2) at Im τ = 3.1.
  - 11: 3.59.
  - 12: 5 × 10⁹ (see §2).
- **The spread.** 10 of the 204 lines reach a factor 3 somewhere on the grid. The median line's best is 14.1.

## 2. A read-out after the run: the electron is exactly massless on every order-12 line

**The census.** In the stored output, the leptons' m₁/m₃ never exceeds 5.5 × 10⁻¹⁴ on any of the 48 order-12 lines, at
any grid point, on either horocycle. On every line of order 8–11 the leptons' first generation is lifted, and so are the
up and down quarks' on every line.

**Checked after the read, by main, on six lines** (the instrument's own function, unsealed). On four order-12 lines at
two generic τ off both CP lines (0.37 + 2.2 i and 0.11 + 1.7 i), the leptons' m₁/m₃ stays ≤ 1.1 × 10⁻¹⁴ on both
horocycles, while every one of the four lepton channel residues is non-zero (ratios to the largest from 0.06 to 1). Two
order-9 lines at the same τ give 2 × 10⁻⁴ to 2 × 10⁻².

So the zero is not B1703's protection rule (R₁ vanishing iff N ∣ δ or N ∣ 3, δ = 5, 1, 9):
- That rule names order 9's leptons, which the canonical end lifts (B1711 and here).
- It does not name order 12, where the zero is exact although no residue vanishes.

**Where the zero comes from (computed after the read on three order-12 lines; not proved).**
- B1659's determinant law is det Y = 4 det S det M tr(εSMᵀ), so the electron is massless for every Higgs when the
  leptons' matter has det M = 0.
- With M = Σ_s u_s E_s* and u_s = √(2πL + c_s) R_s, det M = ¼ Σ u_s² = ¼ (2πL Σ R_s² + Σ c_s R_s²). The identity
  det(Σ u_s E_s*) = ¼ Σ u_s² was checked exactly on random weights.
- **The first sum vanishes for every twist.**
  - Every entry of `bil` has a simple pole at u = 0, with residue X_i(0)Y_j(0) times a factor.
  - The 2 × 2 residue matrix therefore has rank one exactly when den′(0)² = θ₁′(0)·∂_u θ₁(u + τ)∣₀, and both sides equal
    −e^{−iπτ}θ₁′(0)² by θ₁'s quasi-periodicity.
  - Checked to 10⁻¹⁶.
- **On order 12 the channels pair.** On (1/12, 0) and (5/12, 1/3), R_j = iR₁ and R_k = −iR_i, with c₁ = c_j and
  c_i = c_k. On (0, 1/12) the pairs are (1, i) and (j, k). So Σ c_s R_s² cancels exactly, at every L, to 10⁻¹⁴ of its
  scale.
- **A half-period right twist alone is not the condition.** At order 12 the right-handed electron's twist (6α, 12b) is a
  half-period. But the up quarks' right twist is also a half-period at order 8, and they are lifted there.
- **The general law and its proof are open** (P-268, beside P-262). The zero does not bear on H1–H3, since the order-12
  lines fail by the electron's zero.

## 3. What it means

**The reading written before the run** (H2 fails): no flat line of order ≤ 12 gives the masses specifically in this
frame, so the line is not where the frame's missing number lives.
- **The census is too flexible to be a test of the line.** A factor 2.37 is what one in five random hierarchies also
  reaches with the same rows, so H1's success carries no information about the data.
- **With B1698 (orders 5) and B1711 (W59's order 9), every line the record selects, and now every line of order 8–12,
  fails specifically in this frame.** The complement, orders 1–7, and the quark mixing on every order are sealed in B1713.

**What it does not do.**
- Higher orders.
- τ off the two CP lines.
- Other Higgs sections.
- β's role.
- A line that a principle selects for a reason other than its order.

## 4. Seen first

`VERDICT topic-sweep /line census|every (line )?order|orders? 8|W73|weave form|look.elsewhere/ (full text): 81 of 1483 arcs on main match (NEGATIVE 25, OPEN 2, PROVED 54)` —
B1656 (W73's per-sector lines), B1698, B1703, B1711 and the SM seat's relays §195–§196 (the weave form). None tests the
census against data. **Literature:** none beyond the cited arcs.

(As sealed; copied from `PREREGISTRATION.md`.)

## 5. Disclosed

- **As sealed:**
  - the six measured ratios and B1694–B1711's results, known before the seal;
  - the sign check's two lines at an off-grid τ;
  - B1703's census JSON, unread at three off-grid τ.
- **After the read:**
  - §2's census of the stored output;
  - main's six-line check at two generic τ. That check is unsealed; it reads model values only, and no data.

## Files

- `PREREGISTRATION.md` (sealed) and `ARTIFACT_HASHES.txt`.
- `verification/the_line_census_masses.py` → `the_line_census_masses.json`, `the_line_census_masses_run.txt`.
- `verification/compare.py` → `comparison.json`, `compare_run.txt`.
- `verification/b1656_funcs.py`.
- The lock: `tests/test_b1712_the_weave_census_of_lines.py`.

> *Dated correction 2026-10-22 (the math referee's audit, S188; RETRACTIONS row 44).* §2's "and so are the up and down
> quarks' [first generation lifted] on every line" is wrong for this arc's own stored output. On Re τ = 0, the up and down
> quarks are exactly massless on the 16 order-12 lines with 12α odd (α ∈ {1/12, 1/4, 5/12}). They are lifted at Re τ = ½.
> The leptons' order-12 zero holds at both. The verdict and every cell are unchanged: those lines already fail by the
> electron's zero. The Re τ = 0 family is open (P-292).

## Addendum 2026-10-22 (B1724): the reading S* is not SL(2, ℤ)-covariant

B1724 found that of B1660's three up readings, S and S̃ are SL(2, ℤ)-covariant in this frame, and S* is covariant exactly
under Γ⁰(2) (index 3), so S*'s rows depend on which of three sheets τ is taken on. **The verdict stands:** the best row
used S̃, and without the S* rows 20.00% of random hierarchies fit as well (22.45% as sealed; same targets). The per-line
bests marked S* in `comparison.json` are one sheet's values.
