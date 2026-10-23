# THE READING TEST — the rule, sealed before its script is committed

chat1 (the web seat), 2026-10-23, at the owner's word ("yes please" to sealing steps 1 and 2 of THE_NEXT_ATTACK).
**SEALED.** This file is committed and pushed before `reading_test.py` is committed; a draft of that script exists and
was run only on TWO_HIGGS's already-compared rows (disclosed below). Nothing here is a result. 0 of 19.

## The question

Main identifies the reading S̃ (B1724) with the up quarks' conjugate Higgs H̃ = iσ₂H* and S with the down quarks' and
leptons' H. Under that identification the Standard Model's single doublet is one Higgs direction h, read S̃ in the up
sector (S of h̄) and S in the down and lepton sectors. B1739 (PROVED for the record's Higgs) and B1740 (sealed,
NEGATIVE) found that no Higgs on record gives both the hierarchy and an unmixed light generation under that reading;
THE_NEXT_ATTACK §2 (post hoc, labelled; local minima from declared starts) found no free direction below χ²_nine 1 028
on the ten α = 2/5 lines of TWO_HIGGS's grid. This test asks the question with the direction free, on every one of
B1713's 266 lines, on τ no census has computed:

**Is there a row on which some Higgs direction lets the Standard Model's one-Higgs reading carry the nine below the
bar?**

## What is proved before the test (Lemmas A, A′ and B; exact)

For B1736's coupling Y = u hᵀ + h uᵀ − (u·h)1 + w[h]_× (one sector, channel weights (w; u), Higgs h, bilinear dot;
B1736's scalar part zero, as in every census since B1700):

- **Lemma A.** **Y h = Yᵀh = (h·h) u** for every u, w and h (sympy; control C0); B1739's lemma (u = 0: h̄ is the left
  null vector) is the case u = 0. Hence for a unit Higgs g and the sector's left singular vectors ℓ_k with singular
  values m₁ ≤ m₂ ≤ m₃, Σ_k m_k² |⟨ḡ, ℓ_k⟩|² = |g·g|² ‖u‖², and **the light left state lies within sin θ ≤ x =
  |g·g| ‖u‖ / m₂ of ḡ.** Under the Standard Model's reading the up light state lies near h (its Higgs is h̄), the down
  light state near h̄, and |⟨h, h̄⟩| = |h·h|; the Fubini–Study triangle inequality gives, on every row and for every
  direction, **|V_ud| ≤ cos(arccos|h·h| − arcsin min(1, x_u) − arcsin min(1, x_d))** (1 when the argument is negative).
- **What the bar demands.** χ²_nine < 21.67 needs every single term below 21.67: |V_us| ≤ 0.35848 and |V_ub| ≤ 0.006024,
  so |V_ud| ≥ 0.933519; |V_cb| ≤ 0.06718, so |V_tb| ≥ 0.997723; the up quarks' m₂/m₃ ≥ 2.2729 × 10⁻³ and the down
  quarks' ≥ 1.0097 × 10⁻² (factors 1.6212 and 1.8545 below the data). A direction whose Lemma A bound is below 0.933519
  is excluded exactly: in particular the null conic itself (|V_ud| = 0 there whenever both quark sectors have m₂ > 0).
- **Lemma A′ (row-independent).** The symmetric part S = (Y + Yᵀ)/2 = u hᵀ + h uᵀ − (u·h)1 has, for unit h,
  ‖S‖_F² = 2‖u‖² + 2|⟨u, h⟩|² − |u·h|² ≥ ‖u‖², and ‖S‖_F ≤ √3 ‖S‖₂ ≤ √3 m₃; so **‖u‖ ≤ √3 m₃** for every u, w and h,
  and x ≤ √3 |h·h| / (m₂/m₃). With the bar's mass limits, **every direction with |h·h| < 1.112 × 10⁻³ (|s| < 5.56 × 10⁻⁴
  below) has χ²_nine ≥ 21.67 on every row** (identity to 10⁻¹⁵ and largest ‖u‖/m₃ 1.18 on 20 000 random draws; C0).
- **Lemma B (elementary).** For a unit x ∈ ℂ³ let α(x) = ½ arccos|x·x| ∈ [0, π/4], its Fubini–Study distance from the
  real directions (0 for a real direction, π/4 for a null one). A distance to a set is 1-Lipschitz, so
  |⟨x, y⟩| ≤ cos(α(x) − α(y)); for the heaviest up and down left states **|V_tb| ≤ cos(α_u3 − α_d3)**, and the bar needs
  |α_u3 − α_d3| ≤ 0.06750: a nearly null heaviest up state with a nearly real heaviest down state is excluded.
- **Not proved:** that the rest of CP² is excluded (Lemma B constrains the heavy states, not h directly). That is what
  the scan asks.

## What was seen before this rule (disclosed)

- THE_NEXT_ATTACK §1–§2 and its outputs, including the reconnaissance on TWO_HIGGS's grid (the ten α = 2/5 lines).
- `frame_lock.py` (step 1): K1–K7 hold (`frame_lock.json`).
- `reading_prescan.py` (data-free; 0.3 + 2.6i and 0.3 + 3.1i, every line, both horocycles): the channels' structure
  differs widely between line orders (the up channel triplet is nearly n only on some lines); at an exactly null h the
  Standard Model's reading gives |V_ud| = 0 on 2 102 of 2 128 (row, h) pairs, and the other 26 are rows of N = 4 lines
  where both quark sectors have rank one there (m₂/m₃ at most 1.6 × 10⁻¹⁴): the exception Lemma A allows.
- `reading_prescan2.py` (the coarse pattern only, no pinned value): at the same two points on all 266 lines and both
  horocycles (1 064 rows, 22 800 directions each: the tube coordinates below at a coarser resolution plus 2 000
  random), Lemma A's light-state bound was never exceeded (sin θ − x never positive) and the |V_ud| bound never by more
  than 1.3 × 10⁻¹⁵. An up hierarchy (m₂/m₃ ≤ 0.015 and m₁/m₃ ≤ 10⁻⁴) occurs on 689 rows (200 lines); with it,
  |V_ud| > 0.9 occurs on 249 rows, and on every one of them the smallest |V_cb| among those directions is 0.85 or more.
  The coarse pattern (that up hierarchy, a down hierarchy m₂/m₃ ∈ [0.005, 0.08] with m₁/m₃ ≤ 0.005, |V_ud| > 0.9,
  |V_cb| < 0.2, |V_ub| < 0.05) was reached on no row. Sampled, not refined.
- `search_check.py` (post hoc, on TWO_HIGGS's rows, compared with the data before): planted directions recovered on 12
  of 12 rows (six near the conic, six uniform; χ² 1.4 × 10⁻²⁰ or less); with the data, the search reproduced
  `inverse_sm_all.py`'s fifteen lowest minima exactly (1 027.66, 1 030.98, …) and found 1 080–2 092 (median 1 253) on 45
  further rows: nothing below the earlier floor. At the optimum the CKM is the permuted one (|V_cb| about 24 times the
  data; on 35 of the 60 rows |V_ud| < 0.5 as well). 7.6 s per row. With `n_extra = 4` (added after that run, commit
  4370b2e95) the same minima on ten of its rows at 3.0 s per row (an inline check; its log is committed with the
  dry run below).
- `exploration/e8_heavy_states.py` (data-free, the two pre-scan points): over the directions with the up hierarchy and
  |V_ud| > 0.9 (249 rows), the heaviest up state is nearly null (median |ℓ·ℓ| 0.018), the heaviest down state nearly
  real (0.93), and |V_tb| at most 0.35 — Lemma B's exclusion, seen before Lemma B was written down. On 35 of those 249
  rows the heaviest down state is nearly null too (median |ℓ·ℓ| below 0.1), where Lemma B gives nothing.
- **A dry run of the draft `reading_test.py`** on TWO_HIGGS's rows (40 of its points, 80 rows, with the mirror logic;
  post hoc rows; `exploration/dry_run_reading_test/`) ran every mode end to end: C0 held; on those rows the lowest
  minimum was 1 033, S4 and S5 held and the mirror pairs agreed on 40 of 40. Its planted control as first drafted
  (targets the model's nine without noise, success at χ² ≤ 0.1, at least 23 of 24) reached 22 of 24 with all 26 record
  starts (the call lacked `n_extra = 4`, a bug fixed since) and 21 of 24 with `n_extra = 4`: directions at |h·h| ≈
  3–4 × 10⁻⁴, inside Lemma A′'s excluded tube, stopped at 0.18–1.2 in near-degenerate alternative minima. **C2 was
  therefore changed after that dry run:** what S1 needs is power at the bar, not convergence to zero, so C2's targets
  now carry noise (a planted near-solution with χ² of order 9, as a real one below the bar would be), its near-conic
  draws stay outside Lemma A′'s tube, and it adds directions near n and n̄, where every record direction lies. On 24
  rows of the old points the noisy version met or beat the planted direction's χ² (3–21) on 24 of 24; the search's
  minimum there was 1.4–8.5 below the planted value (the slack that four free numbers absorb from the noise; 2–12 in
  the referee's own noisy runs). A read-only
  referee of this rule found the same failure and the same region; Lemma A′ and C2's new strata follow its report.
  The revised draft was dry-run again on the same 80 rows: C0 held (largest ‖u‖/m₃ 1.23); C2 as now written met 36 of
  36 (noiseless recovery 35 of 36 to χ² ≤ 0.1, 36 of 36 to ≤ 2.167); S4 and S5 held there; per row Lemma B excluded a
  median 79% of the random directions and Lemma A 0.03%, and the lowest χ² among random directions neither excludes
  was 1 827.
- No point of this test's grid is on any grid chat1 has found on record (below).

## The model

- **The frame:** main's fibre frame (B1720's instrument at 3412bf09d, unchanged, through chat1's `channel_store.py`
  wrappers): the four channel weights per sector (up, down, leptons) and horocycle (L_max, L₂); B1736's closed form,
  checked against `coupling()` (C1).
- **The reading:** up Y(u_up; h̄), down Y(u_down; h), leptons Y(u_lep; h); the lepton factor c = 3 by hand (m_μ/m_τ × 3,
  m_e/m_τ ÷ 3), as in every value test since B1726.
- **Free:** h ∈ CP² (four real numbers).
- **Objective:** PRECISION_BAR's χ²_nine (σ² = the data's relative error² + 0.1² on the natural logs of m_c/m_t, m_u/m_t,
  m_s/m_b, m_d/m_b, m_μ/m_τ, m_e/m_τ, |V_us|, |V_cb|, |V_ub|), targets the record's pinned files at 3412bf09d (sha256 as
  in `inverse_higgs.py`: Huang–Zhou 2021 at M_Z and PDG 2025's moduli; the scale is a framing choice, THE_FRAMING_CHECK
  §4a); bars 16.75 (six) and 21.67 (nine).

## The grid

- B1713's 266 lines of order 1–12; both horocycles.
- **Re τ ∈ {0.1146, 0.6354}, Im τ ∈ {2.1146, 2.5271, 2.9396, 3.3521}:** 8 points per line, 2 128 points, **4 256 rows**.
  Off every regular grid chat1 has found on record (main's Re τ ∈ {0, 0.1, ¼, 0.4, ½} and B1726's
  {0.05, 0.2, 0.35, 0.55, 0.7, 0.85}, Im τ on multiples of 0.05; chat1's Re τ on multiples of 0.1 or 1/16, Im τ on
  tenths) and at least 0.032 from each of the 66 distinct apex points (mod 1) of B1720's thread classes used by B1734,
  B1741 and RIGID_TAU. Not symmetric under Re τ ↔ 1 − Re τ.
- **The mirror control set:** the ten α = 2/5 lines at Re τ = 0.8854 and the four Im τ (40 points, 80 rows), the
  mirror partners (R4: (2/5, b) at Re τ ↔ (2/5, 3/5 − b) at 1 − Re τ, h → P′h̄) of grid rows at 0.1146. Not in the
  cells.

## The search (declared: `sm_search.py` at 4370b2e95, committed before this rule)

- **Grid:** the null conic's tube coordinates h = h₀(t) + s h̄₀(t), h₀(t) = (2t, 1 − t², i(1 + t²)) unit, for which
  |h·h| = 2|s|/(1 + |s|²): t on a 400-point Fibonacci lattice of the Riemann sphere, |s| = 10^(−4 + k/4) (k = 0 … 16),
  arg s in 16 steps (108 800 directions), plus 4 000 random directions (seed 2610, uniform on CP²). The coordinates
  with |s| ≤ 1 cover CP² (|s| = 1 is the real locus); the finite set samples it (from a random direction to the nearest
  grid direction: median 0.071 rad, largest 0.148 on the referee's sample). The three innermost shells lie inside
  Lemma A′'s excluded tube.
- **Refinement:** least squares (scipy trf, at most 400 evaluations) from the best eight grid directions that are
  pairwise more than 0.05 rad apart (Fubini–Study) and from the four best (by χ² at the start) of the record's 26
  directions at τ (∂R, F_a for a ∈ {−10, −6, −2, 2, 6, 10, 14, 18, 22, 26}, h₂, h₃, each as stored and conjugated):
  `sm_search.search(…, n_extra = 4)`.
- **Cost:** the store about 25 minutes; the scan 2–3.5 hours on two workers.
- **Per row:** the minimum found, χ²_six and the CKM's share of χ² there (the three |V| terms, which do not depend on c
  or on the leptons), the nine's model/data ratios, the CKM moduli, |h·h|, Lemma A's x_u, x_d and |V_ud| bound, the
  heaviest states' α_u3, α_d3 and Lemma B's |V_tb| bound (from the same SVD as the reported |V|); and over the 4 000
  random directions (an unbiased sample of CP²), the fraction that Lemma A or Lemma B excludes and the lowest χ²_nine
  among the directions neither excludes. Rows where a sector's weights vanish are reported as degenerate. The search is
  a heuristic: the cells are about the minima it finds, and C2 measures its power.

## The cells, with priors

| cell | statement | prior |
| --- | --- | --- |
| S1 | no row of the 4 256 has a minimum χ²_nine below 21.67 | 92% |
| S1′ | no row has a minimum below 100 | 85% |
| S4 | at every row's optimum the CKM is in one of the two failure branches of THE_NEXT_ATTACK §1.6: \|V_ud\| < 0.5 or \|V_cb\| > 0.5 | 80% |
| S5 | at every row's optimum one of the exact bounds already excludes the bar: Lemma A's \|V_ud\| bound below 0.933519 or Lemma B's \|V_tb\| bound below 0.997723 | 60% |
| C0 | Lemma A's identity symbolically; Lemma A′'s identity and ‖u‖ ≤ √3 m₃ on 20 000 random draws (10⁻¹⁰); the search's vectorised model equal to `inverse_higgs.nine` on 1 000 directions at ten stored rows (10⁻¹⁰ in ln; no χ² against the data) | 99% |
| C1 | the store against `coupling()` at the first five points (10⁻¹²) | 95% |
| C2 | power: 36 rows of the grid (seed 1741), a planted direction each — 12 near the conic (t complex normal, \|s\| log-uniform in 5.56 × 10⁻⁴ … 10⁻¹), 12 near n or n̄ (six each: the leading null line plus δ e₁ and ε times the other null line, \|δ\| ≤ 0.25, \|ε\| ≤ 0.03, uniform in the discs, drawn again while \|h·h\| < 1.112 × 10⁻³), 12 uniform on CP² — with targets the model's nine there plus Gaussian noise of the χ²'s own σ per entry; the search's minimum is at or below the planted direction's χ² on at least 34 of 36. Read-out, not a cell: the noiseless recovery (χ² ≤ 0.1 and ≤ 2.167) on the same directions | 85% |
| C3 | the mirror pairs' minima agree within 1% on at least 72 of the 80 pairs and on every pair with a minimum below 100 | 85% |

## What the outcomes mean (fixed now)

- **S1 holds, with C2 and C3.** On every flat line of order ≤ 12, at these eight τ and both horocycles, with c = 3, the
  declared search — with the power C2 measured — found no Higgs direction that lets the Standard Model's one-doublet
  reading reach the nine's bar. Near the null conic Lemma A′ excludes it exactly; elsewhere the claim is the search's.
  If main's identification of S̃ with H̃ holds, this points to (it does not show) a flavour sector that cannot be read
  with one doublet and needs two Higgs directions with equal (holomorphic) readings, the structure of a type-II
  two-doublet model or the MSSM's — a structural pointer, not a value, no number of the 19. The next step is then
  THE_NEXT_ATTACK's step 3 (the Higgs pair from a stated rule).
- **S1 fails.** Every row below 21.67 is listed with its line. With four free numbers per row on 4 256 rows this is a
  fit; nothing is read as a selection of lines until a separate sealed calibration (random targets from main's
  generator through the same search) prices the look. Those lines become that calibration's and the next test's
  candidates.
- **S1′ fails while S1 holds.** Every row below 100 is listed with its line; nothing more.
- **S4 fails.** Some optimum sits outside both branches; reported (Lemma A's branches are not exhaustive there).
- **S5 holds.** Every row's best direction fails the bar through one of the exact bounds: descriptive — it accounts for
  the optima's failures, not for the rest of CP² (the random-direction read-out estimates how much of CP² the two bounds
  exclude). **S5 fails:** some optimum fails the bar for another reason (the masses, or a CKM entry the bounds do not
  reach); reported with its row.
- **C2 fails.** The search lacks the measured power to make S1 an exclusion; S1 is then not read as a negative (§12 of
  the standing rules: an unearned negative is as bad as numerology). **Another control fails:** nothing is read until it
  is resolved, post hoc and labelled.
- **Reach.** Everything here is conditional on the frame as main built it (B1736's scalar part zero, a pure Higgs
  direction), the eight τ, the two horocycles, c = 3, the comparison at M_Z and the identification of the readings with
  H and H̃ (P-295 records another reading). Between the sampled τ nothing is claimed.

## Discipline

- This rule is committed and pushed before `reading_test.py` is committed; `reading_test.py` is committed before its
  run on this grid; the store, the rows and the controls are committed before they are read; the cells are computed
  from the committed rows, committed, then read.
- A failed launch is disclosed with its log kept; any later check is labelled post hoc.

0 of 19.
