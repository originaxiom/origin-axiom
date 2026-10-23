# THE NEXT ATTACK (chat1, 2026-10-23): the frame's mixing in closed form, what a Higgs would have to supply, and the reading test

> **For main, under B1740's pledge (HARVEST_LEDGER rows 1338–1342):** §1 is data-free and names no F₋₂ property; it can
> be read now. **§0's TWO_HIGGS line, all of §2 and §3** compare models with the data on grids whose menus include F₋₂
> (record_pairs evaluates F₋₂ in the Standard Model's orientation on ten lines; the optimiser starts from F₋₂) or quote
> TWO_HIGGS's results; read them after B1740's outputs are committed.

chat1 (the web seat), at the owner's word: "fetch other seats and lets prepare for another serious attack … where the
progress can move on, another huge step". **Kinds, as tagged:** §1 is data-free mathematics, each statement computed
(scripts named; `exploration/` was run before its commit and is labelled so in `exploration/README.md`); §2 is a post hoc
reconnaissance on a grid already compared with the data, labelled, not a test, each script committed before its run and
each output before its read; §3 is a plan: no test in it is sealed. By PRECISION_BAR nothing here is described as
reaching the values. Two read-only referee passes ran on drafts of this file (12 major and 16 minor points, then 1
blocker, 5 major and 10 minor points); every point was applied, with the checks they asked for in `revision_checks.py`,
`revision_checks2.py`, `lepton_channels.py` and `sm_reading_branches.py`. **0 of 19.**

## 0. The board, all seats (main at a74c9cd6f)

- **The six matched at value level three ways, all on the line (2/5, 1/10)** (in B1726's census frame):
  - main's B1735 (post hoc, labelled; reproduced by the SM seat's W142): χ²_six 3.09 with τ fitted (0.35 + 3.05i),
    L_max, the Standard Model's reading (up S̃, down and leptons S) with DR, c = 3; 0.03% of random targets as good;
  - main's B1741 (sealed, landed during this work): χ²_six 14.93 with τ at a thread's apex (0.4 + 2.993i), the line
    chosen from 266, the same reading; P2 0.60% specific, not passed under THE_BAR's look correction (1.2–3.6%);
  - [after B1740] chat1's TWO_HIGGS (sealed, H5): χ²_six 1.19 with H_u = F₆, H_d = F₂₂ read S at 0.5625 + 2.6i, L₂.
- **The nine are reached in no sealed or banked result:** B1726's census minimum 109 (B1735, at P-344's row; B1735's own
  six-best row has its CKM 4–24 times the data), B1741's 204 (P3) and 1 410 under the Standard Model's reading (P4,
  |V_ud| 0.12), [after B1740] TWO_HIGGS 154.
- **Main's B1739:** at the hierarchy band ∂R is nearly null; each sector's lightest state sits on h̄ (reading S) or h
  (reading S̃); with ∂R in its stored orientation the Standard Model's reading puts the light up and down states nearly
  orthogonal. **B1740** (the non-null F₋₂ under that reading) is sealed; its census was paused at 3 608 points while B1741
  ran. Nothing below duplicates it.
- **The SM seat:** E₆'s 27s give D ≡ 1 (W139; B1738); only five-ality lines keep m_e = m_d inside E₆ (W140); its third
  opinions confirm B1726, B1734, B1735 (W138, W141, W142).

## 1. The frame's mixing in closed form (COMPUTED, data-free; all of it on the ten (2/5, k/10) lines of the store)

**Notation.** One sector: channel weights (w; u) = (u₁; u_i, u_j, u_k) and a pure Higgs direction h (B1736's scalar part
zero, as in every census since B1700); reading S (S̃ replaces h by h̄). B1736: **Y = u hᵀ + h uᵀ − (u·h)1 + w[h]_×**
(dot = the complex bilinear form). ρ(T)'s eigenlines give an orthonormal frame **f₃ = n = (0, 1, i)/√2, f₂ = e₁ =
(1, 0, 0), f₁ = n̄**, with f₁·f₃ = 1, f₂·f₂ = 1 and every other product 0. A Higgs led by n is h = f₃ + δf₂ + εf₁ with
complex δ (its e₁, θ₂-type part) and ε (its part along the other null line); write u = a₃f₃ + a₂f₂ + a₁f₁.

**1.1 The canonical matrix (exact; linear in δ and ε).** F†YF in the order (f₁, f₂, f₃) for rows and columns:

    | δ(iw − a₂)          δa₁ + ε(a₂ − iw)     2εa₁              |
    | a₂ − iw + δa₃       δa₂ − εa₃ − a₁       δa₁ + ε(a₂ + iw)  |
    | 2a₃                 a₂ + iw + δa₃        −δ(a₂ + iw)       |

(`g7_canonical.py`: 4 × 10⁻¹⁵ on 200 random draws.) The first row (the left light state f₁ = n̄) and the last column
(the right light state f₃ = n) are made only of the Higgs's departures from its leading null line; the heavy block is
the channels'.

**1.2 The determinant (B1659's J1 in this form).** det Y = (h·h)(u·h)(u·u + w²) (`g1_det.py`, sympy). With
Δ = u·u + w², m₁m₂m₃ = |h·h||u·h||Δ| exactly; at the null limit m₂m₃ = |Δ|, so m₁ ≈ |h·h||u·h| when the departures are
small, with h·h = 2ε + δ² and u·h = a₁ + a₂δ + a₃ε.

**1.3 The light state's tilt (first order in the departures).** The left light state is f₁ + βf₂ + γf₃ with
**β = conj(δ + 2εa₃(a₂ − iw)/Δ)** and **γ = −conj(ε(a₂ − iw)²/Δ)** (`g2_light.py`, random O(1) channels: relative error
3 × 10⁻⁴ at departures 10⁻⁴–10⁻³, growing linearly). With both sectors led by the same null line,
**|V_us| ≈ |β_u − β_d|**, and with β read from the SVD this holds to 0.05–2.3% for five aligned pairs of record forms
(`revision_checks2.py`, S2). **Scope:** at the band the expansion parameter is the departure times m₃/m₂, so the
first-order β is a statement of which term carries what, not a calculator: on the stored channels it errs (R1, medians
by Im τ band 2.0–2.5 / 2.5–3 / 3–3.5) by 28 / 15 / 8% for F₆ in the up sector, 48 / 31 / 19% for DR in the up sector,
40 / 9 / 2% for DR in the down sector, 58 / 67 / 60% for F₂₂ in the down sector and up to 146% for F₂₂ in the up sector;
|V_us| from the first-order β errs by up to 190% (S2); m₂m₃ ≈ |Δ| errs by 27 / 15 / 8% (F₆) and 58 / 38 / 22% (DR) in
the up sector. Band values come from the SVD, which the channel store (§2.1) makes cheap.

**1.4 V_cb is the channels' at leading order.** Each sector's 2-3 tilt at the null limit is
**κ_s = [(a₂ − iw)·conj(2a₃) − a₁·conj(a₂ + iw)] / (4|a₃|² + |a₂ + iw|²)**, and under the null Higgs n
**|V_cb| = |κ_u − κ_d|**: median relative error 0.35%, largest 1.8%, over all 2 560 stored rows (R2). How far the Higgs
moves V_cb and the down quarks' m₂/m₃: over the eight null-led record forms on the store (S1) the max/min ratio has
median 1.34 and 1.93 at Im τ 2.0–2.5 (90th percentiles 2.49 and 3.82), 1.09 and 1.17 at 2.5–3 (1.32 and 1.64), 1.02 and
1.03 at 3–3.5 (1.08 and 1.11); on the zero-free census's hierarchical rows V_cb's ratio has median 1.18 at 2.5–3 with a
90th percentile of 3.34 (`e7_vcb_spread.py`). So V_cb and the down quarks' m₂/m₃ belong to the channels at Im τ ≳ 3,
not below. On the five order-10 lines the up channel has a₂ = 0 exactly (w ≠ 0) and |κ_u| ≈ |w/2a₃|
(`g5_vcb_formula.py`); on the five order-5 lines it has w = 0 exactly (a₂ ≠ 0) (R5) — B1728's step 1 explains the
split (below, 1.6). **The horocycle scales V_cb:** under n the ratio L_max/L₂ has median 2.69–2.79 at every Im τ from 2.0
to 3.5 (range 2.58–3.39; R3).

**1.5 The light tilt and the record's Higgs forms.** With δ = 0, β ∝ ε exactly at first order, while
m₁ ≈ |2ε||a₁ + a₃ε| is linear in ε only where |a₃ε| ≪ |a₁|: in the down sector, not in the up sector at the band, where
|a₁|/|u| is 0.002–0.016 (R5) and ε is 10⁻³–10⁻². (Reading this as Froggatt–Nielsen with flavon |q|^¼ = r^½ per unit
of ρ(T)-charge, q = e^{2πiτ}, r = e^{−π Im τ}, is an interpretation, not computed; B1691 has the cusp exponents of the
covariant sections, m₂/m₃ ~ |q|^½ and m₁/m₃ ~ Im τ·|q|.) **The record's forms at the cusp** (`g4_departures.py`, at
Re τ 0.3, constant to four digits from Im τ 2.5 to 4): **R = F₂: δ = 2√2 r^½, ε = 4r** (exactly null, |δ²| = |2ε|);
**DR: δ = 4√2 r^½, ε = 20r** (|δ²/2ε| = 0.8); **F_a for a > 2: ε = 2a·r and δ vanishing faster** (for a = 6,
δ = 32√2 r^{3/2} ≈ 45.3 r^{3/2}); B1700's h₂ and h₃ are led by e₁. DR is R's Serre derivative (B1691's definition; R of
weight −½), and B1691's exact identities give R·R = 0 and R·∂R = 0; `g6_maass.py` confirms DR = qR′ + E₂R/24 to
2 × 10⁻¹¹. Every member of the pencil DR + λR therefore has the invariant DR·DR; at the cusp
δ = 2√2·|(1/6 + λ)/(1/12 − λ)|·r^½ and ε = 4·|(5/12 + λ)/(1/12 − λ)|·r (λ = 0.02 checked numerically: 8.34, 27.6), so
|δ²/2ε| is 0.8 at λ = 0 and diverges at λ = 1/12 (the leading null part cancels, δ diverges) and at λ = −5/12 (ε cancels;
δ = √2 r^½). (|V_us| ≈ √(m_d/m_s) holds for the pinned central values to 0.40%, with √(m_d/m_s) uncertain by 5.6%; S3.)

**1.6 The Standard Model's reading on the store: a lemma for an idealised up channel, and two failure branches.**
B1728's step 1 makes a shift of the second characteristic slot by an even integer a phase. The up sector's two
characteristics, (α, 2b) for Q and (−4α, −8b) for u, differ by (5α, 10b): on these lines 5α = 2 and 10b = k, so they
coincide up to a phase on the order-5 lines (k even) and differ by an odd shift on the order-10 lines, which matches
R5's w = 0 on order 5 and a₂ = 0 on order 10. On both, the up channel triplet is nearly n (|u·u|/|u|² median
0.004–0.037, at most 0.18; R5).
- **Lemma (idealised up channel u = a₃n, w = 0).** From 1.1 with a₁ = a₂ = w = 0 and h = c₃f₃ + c₂f₂ + c₁f₁, unit:
  Y = a₃·[[0, 0, 0], [c₂, −c₁, 0], [2c₃, c₂, 0]] in the frame. So m₁ = 0; the up light left state is n̄ for every h; the
  2 × 2 block's determinant gives m₂m₃ = |a₃|²|2c₁c₃ + c₂²| = |a₃|²|h·h| (B1659's J2 in this case); and
  ‖Y‖²_F = |a₃|²(4|c₃|² + 2|c₂|² + |c₁|²) ≤ 4|a₃|² bounds m₃, hence **m₂/m₃ ≥ |h·h|/4** (R5: 9 × 10⁻¹⁶, 2.5 × 10⁻¹⁵,
  smallest ratio to the bound 1.02 on 2 000 random h). An up hierarchy m_c/m_t ≈ 3.7 × 10⁻³ then needs |h·h| ≲ 0.015.
- **On the stored channels the bound holds only roughly:** (m₂/m₃)/(|h·h|/4) has minimum 0.48, 0.69 and 0.89 by band
  over 40 random unit h per row, below 1 for under 1% of them (S6).
- **What the CKM does (data-free counts on the store):** under the Standard Model's reading it came out a
  near-permutation in every case computed. With DR, F₆ and F₂₂ in both orientations (`sm_reading_branches.py`, medians
  by band): for h led by n̄ (∂R as stored), |V_cb| is 0.98–1.00 and |V_ud| 0.04–0.82; for h led by n, either
  |V_ud| ≈ 0.99 with |V_cb| ≈ 0.99 (F₂₂ at Im τ 2.0–3.0, DR at 2.0–2.5) or |V_ub| ≈ 1 (F₆ throughout, F₂₂ and DR at
  3.0–3.5), with DR at 2.5–3.0 between the two (medians |V_ud| 0.43, |V_cb| 0.44, |V_ub| 0.89). With 204 800 random nearly null directions (S5; |δ| ≤ 0.25, |ε| ≤ 0.03), an up hierarchy (m_c/m_t < 7.4 ×
  10⁻³, m_u/m_t < 10⁻⁴) appeared in 9 154, all with h led by n̄; of those, 1 430 had |V_ud| > 0.9 and none |V_cb| < 0.2.
  So the failure has two branches — light states near-orthogonal, or the 2-3 block exchanged — not B1739's first branch
  alone, which is its statement for ∂R in its stored orientation. **Not proved:** a bound for general h on the stored
  channels.

**1.7 The leptons as the down quarks, on these ten lines** (`lepton_channels.py`). Up to one complex factor of modulus
one, the leptons' channel weights equal the down quarks' with **w → −w on the five order-5 lines** and with
**u_i → −u_i on the five order-10 lines** (3.7 × 10⁻¹⁵). (R6 in `revision_checks.py` looked for a sign pattern without
the factor and failed, its best deviation 1.902 = 2 sin 72°, as a fifth root of unity would give; `lepton_channels.py`
was written after it.) The order-5 half is B1728's derivation (Y_e = Y_dᵀ for N ∣ 5) and W138's D_frame = 1 on order-5
rows; the order-10 half is observed on five lines, not derived (B1728's step 1 is the natural route). Consequences,
checked for the record's directions (1.4 × 10⁻¹¹): on the order-10 lines the lepton singular values are the down quarks'
with **h → Ph, P = diag(−1, 1, 1)**, i.e. δ → −δ; with c = 3 that makes D = 9 exactly on order-5 lines and D − 9 a measure
of the down Higgs's e₁ part on order-10 lines (P-315 asks why, on 12 order-10 lines, only the i-component splits d from
e; five are covered here). At leading order m_d/m_e ≈ |u_d·h| / |u_d·Ph| (median error 4.0, 1.2 and 0.13% by band for
DR in both orientations; S7), so D and V_us read the same δ.

## 2. Reconnaissance (POST HOC, labelled; TWO_HIGGS's grid, already compared with the data) — [after B1740]

**2.1 The instrument.** `channel_store.py` stores the four channel weights per sector and horocycle at each point, once;
B1736's closed form then makes any Higgs direction, reading or pairing three 3 × 3 SVDs. On TWO_HIGGS's 1 280 points
(the ten (2/5, k/10) lines, Re τ 0.0625–0.9375, Im τ 2.0–3.5): its sealed-in controls ran at the first five points, all
on (2/5, 0) (C1 against `coupling()` 2.8 × 10⁻¹⁶; C2 against TWO_HIGGS's stored rows 1.2 × 10⁻⁷); extended to every
point after the referee (R7): 2.4 × 10⁻⁷ in log ratios and 5.9 × 10⁻⁸ in ln|V|. A first launch was stopped after about
15 s, before it wrote anything (disclosed in its commit). **The grid is mirror-symmetric:** (2/5, b) at Re τ and
(2/5, 3/5 − b mod 1) at 1 − Re τ give the same ratios and |V| with h → P′h̄, P′ = [[−1,0,0],[0,0,1],[0,1,0]]
(4 × 10⁻¹¹ on all 640 mirror pairs, R4), so counts below are also given as independent pairs.

**2.2 With a free Higgs direction** (`inverse_higgs.py`: least squares from declared starts — 12 per row for A2, ten of
them pairs of record forms both led by n, and 16 for A1 and SM; B1720's χ²; c = 3; the 160 rows a null-Higgs screen
ranked best, 80 mirror pairs). **The screen confounds the horocycle with Im τ:** its 40 L₂ rows lie at Im τ 2.0–2.4 and
its 120 L_max rows at 2.7–3.3, none at 2.5, 2.6, 3.4 or 3.5; six lines carry 26 rows each and four lines one each.
**The minima are local:** mirror pairs must share their minima, and 11 of 80 A2 pairs and 4 of 80 A1 pairs differ by
more than 1% (R4).

| structure | free real numbers | lowest minimum found | rows (mirror pairs) below 21.67 |
|---|---|---|---|
| A2: two directions (both optima led by the same null line, an outcome not a constraint) | 8 | 0.605 | 150 (75) |
| A1: one direction in every sector, the same reading | 4 | 17.26 | 8 (4) |
| SM: one direction, the Standard Model's reading | 4 | 1 193 | 0 |

- **A2 says only that the channels carry no obstruction.** Its 0.605 is the Georgi–Jarlskog floor exactly (0.0798 +
  0.5249 from the two lepton–down pairs at c = 3), reached on 26 rows, all on the order-5 (d = e) lines, where the model
  has seven independent outputs against eight free numbers; 70 rows on order-10 lines fall below 21.67 too (lowest
  1.73). Nothing is predicted.
- **A1's fitted minimum falls below 21.67 on four mirror pairs**, all L₂ on the pair (2/5, 0), (2/5, 3/5) at Im τ 2.0–2.3
  (lowest 17.26 at 0.4375 + 2.1i; V_us and V_cb at 0.77 of the data). Because of the screen this says nothing about L₂
  above 2.4 or L_max below 2.7.
- **Under the Standard Model's reading the optimiser found nothing below 1 193** on these 160 rows: every optimum has the
  permuted CKM of B1735 (|V_us| 4.40–4.44 and |V_cb| 23.87–23.90 times the data; χ²_nine 1 193–1 236), most with the six
  fitted — §1.6's second branch. B1741's P4 (1 410 with DR on all 266 lines) is the same picture. On all 2 560 rows
  without the screen the floor is 1 028 (§2.5).
- **What A2's optima put in the Higgs (non-unique and local, so scales only),** by the screen's two blocks (R8): on the
  120 L_max rows (Im τ 2.7–3.3) the down Higgs has median δ_d ≈ 21 r^½ (3.8 times DR's) and ε_d ≈ 230 r, the up Higgs
  9.4 r^½ and 103 r; on the 30 L₂ rows below 21.67 (Im τ 2.0–2.4) the down Higgs is DR-sized (6.5 r^½, 17 r) and the up
  Higgs smaller (3.9 r^½, 14 r). The down Higgs's |δ²/2ε| has median 0.97 over the 160 rows (0.98 on the 150 below 21.67;
  0.95 on L_max, 1.00 on L₂; S4), against DR's 0.8; these optima move V_cb from its null-Higgs value by a median 1.14 on
  L_max and 1.24 on L₂ (S4). The zero-free F_a (δ ≈ 0) are the wrong shape in both blocks.

**2.3 With the record's directions only** (`record_pairs.py`, exhaustive over its set: every ordered pair of the thirteen
stored directions, each as is or conjugated, 676 pairs): **lowest χ²_nine 96.3** (F₆ with conj DR, aligned, (2/5, 9/10),
0.6875 + 2.6i, L₂), 4.4 times the bar; no pair has a row below 60; 61 pairs have a row below the six's bar; the best 25
pairs are all aligned.

**2.4 With the covariant pencil** (`weight_pencil.py`, exhaustive over its set): DR + μE₂*R with E₂* = E₂ − 3/(π Im τ)
is covariant for every constant μ; `weight_pencil.py` labels μ = w/12 by the weight w of the η-twisted R it differentiates
(w = 0 is DR, w = −½ the Maass–Shimura derivative of R itself) and samples w ∈ {−1, −½, 0, ½, 1, 3/2, 2}. Over its 49
(w_u, w_d) pairs the **lowest χ²_nine is 53.0** at (½, 2), 2.4 times the bar; (−½, −½) gives 96.3 and (0, 0), DR, 104.

**2.5 The Standard Model's reading on every row** (`inverse_sm_all.py`, committed before its run: the same optimiser
from twelve starts, on all 2 560 rows, no screen): **the lowest minimum found is 1 027.7** (1st percentile 1 043, median
1 249); no row below 500. The lowest rows are L₂ at Im τ 3.4–3.5 on the mirror pairs (2/5, 7/10)–(2/5, 9/10) and
(2/5, 1/5)–(2/5, 2/5): there |V_us| and |V_ub| come within 10% of the data, |V_cb| is 23.8–23.9 times it (the 2-3
block exchanged, §1.6's second branch) and χ²_six is 55–66. Minimised alone, the six reach 0.10. Local minima from
declared starts, as in §2.2.

**What §2 settles and what it does not.** On the 160 screened rows of the ten α = 2/5 lines: with two free directions the
channels carry the nine (no prediction in that); the record's directions and the covariant pencil, exhaustively over
their sets, do not (4.4 and 2.4 times the bar); for the Standard Model's one-Higgs reading the optimiser found no
direction below 1 193 on the screened rows and none below 1 028 on all 2 560 rows (local minima). Nothing here reaches
beyond these ten lines.

## 3. The attack (PLAN; nothing sealed) — [after B1740]

**Step 1, data-free: bank the canonical frame.** §1.1, 1.2, 1.4's V_cb = |κ_u − κ_d|, 1.6's idealised lemma and 1.7 as
a result note with locks, each scoped to the lines computed; §1.3 and 1.5 as structure, with their band accuracy stated.
Ask: the SM seat's third opinion on 1.1, 1.4 and 1.7. Cost: an hour or two.

**Step 2, THE READING TEST: can any Higgs direction let the Standard Model's one-Higgs reading carry the nine?**
- **2a, a proof where one is within reach:** extend 1.6's lemma from the idealised up channel to the stored channels with
  explicit constants (S6 says they are of order 2–4), and bound the two branches together — "|V_ud| small or |V_cb| near
  1" — for nearly null h. That excludes a stated region of CP² on every row where the constants hold.
- **2b, a sealed global scan of the rest:** on fresh points over all 266 lines (a τ grid no census has computed and not
  symmetric under Re τ ↔ 1 − Re τ, with a separate small mirror-paired control set), the χ²_nine of the Standard Model's
  reading over a declared parametrisation of CP²: a uniform 12 × 12 × 24 × 24 grid plus an explicit dense sampling of the
  nearly null shells |h·h| ≤ 0.05 around n and n̄ (where 1.6 confines any up hierarchy, and which a uniform grid barely
  touches), vectorised at about 17 μs per direction, with local refinement from each row's best five. Controls: the
  mirror set agreeing, a planted direction recovered, the store against `coupling()`. **Cell S1:** no row below 21.67.
  Cost, for 266 lines × 8 τ points (2 128 points, 4 256 rows with both horocycles): the store about 25 minutes, the scan
  and refinement about 3–4 hours on two workers.
- **What S1 would and would not mean.** Its reach is the sampled τ, the 266 lines, c = 3 and the two horocycles. Main
  identifies S̃ with the up quarks' conjugate Higgs (H̃) and S with the down quarks' and leptons' (H); P-295 records
  another reading (the theta components' internal index). If that identification holds and S1 holds, the frame on those
  rows cannot carry the Standard Model's single doublet, which points to a second doublet with equal readings (a type-II
  two-doublet model or the MSSM's) — a structural pointer, not a number of the 19. If S1 fails on some lines, those lines
  are where the reading can fit: a selection by fit, to be calibrated against random targets before it is read as a
  rule. One Higgs in every sector (A1) is left to a separate test with its own calibration design.

**Step 3, theory then sealed: THE HIGGS PAIR.** §2.2's optima put a down Higgs of about DR's shape (|δ²/2ε| ≈ 1, DR 0.8)
with an e₁ part about four times DR's in the screen's L_max block (Im τ 2.7–3.3) and DR-sized in its L₂ block (2.0–2.4);
the horocycle and Im τ are confounded there. §1.7 adds a constraint: on order-10 lines D reads the same δ as V_us.
Candidates, each scored on the channel store before any seal, the survivor sealed on fresh points with both precision
bars, main's calibration and THE_BAR's look correction:
- (a) **after main's P-324, the Higgs's own hypercharge twist**: H_u and H_d carry 6Y = ±3 on the line, so their
  directions could differ by the line rather than by choice (chat1 waits for main's word);
- (b) **the covariant pencil with μ fixed by a stated rule** (its sampled floor is 53, so a rule would have to do better
  than any of the 49 sampled pairs);
- (c) **forms of the joint family group's level** (the SM seat's W136, PSL(2, ℤ/4)) — whether their cusp coefficients
  differ from DR's is not computed;
- (d) **the poles-allowed weight-3/2 space** (B1700's h₂, h₃) with a coefficient fixed by a stated condition.
No candidate is sealed until its rule says why that direction and not a fitted one.

**Step 4, after step 2: V_cb as the channels' test.** At Im τ ≳ 3, V_cb and the down quarks' m₂/m₃ move by 2–3% (median)
across the record's null-led forms (S1), so with m_μ/m_τ through c on order-5 lines they test the line, τ and the
horocycle; the up quarks' m₂/m₃ is excluded (a factor 3 across the null-led forms at one point, `g3_quartet.py`), and a
Higgs of A2's shape would still move V_cb by 14–24% (S4). It needs a horocycle rule first: L_max and L₂ differ by 2.7.

**What would count.** A sealed row below both bars on fresh rows with the Higgs pair from a stated rule (step 3) would be
the first value-level nine — conditional on c = 3 by hand, the reading, the line and the horocycle chosen, and τ fitted.
On order-5 lines the model has seven independent outputs for the nine numbers and gives D = 9, which P-094's
10.58 ± 0.11 excludes, so a nine that also respects D has to sit on order-10 lines, where D − 9 reads δ (1.7).

## 4. Asks

- **To main:** verify §1 (a dated note on B1736 or an arc) — readable now; §0's TWO_HIGGS line, §2 and §3 after B1740's
  outputs are committed; your word on step 3 (a).
- **To the SM seat:** a third opinion on §1.1, 1.4 and 1.7; and whether W136's level-4 forms have a direction of DR's
  shape with larger cusp coefficients at the band.

## Files (this folder)

`channel_store.py` → `channel_store_two_higgs.npz`, `_index.json`, `_controls.json`, `_run.txt`;
`inverse_higgs.py` → `inverse_higgs_two_higgs.json`, `_run.txt`; `inverse_higgs_readout.py` → `..._readout.json`;
`record_pairs.py` → `record_pairs_two_higgs.json`; `weight_pencil.py` → `weight_pencil_two_higgs.json`;
`inverse_sm_all.py` → `inverse_sm_all_two_higgs.json`; `revision_checks.py` → `revision_checks.json`;
`revision_checks2.py` → `revision_checks2.json`; `lepton_channels.py` → `lepton_channels.json`;
`sm_reading_branches.py` → `sm_reading_branches.json`; `exploration/` (run before commit, labelled; see its README).

0 of 19.
