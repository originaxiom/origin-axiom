# The selection map: what a selection can decide in the record's two working frames, and the law ingredient the data point to

chat1 (the web seat), 2026-10-22, at the owner's word: "find the One missing ingredient, a selection principle, which
decides most of the things towards 19s". GENESIS FK9 names selection as the missing ingredient and assigns its study to
this seat (2026-10-14). A READING with computed lemmas, one failed sealed prediction, two sealed tests and post hoc
analyses, each labelled. Refereed read-only before it left; the referee's corrections are applied. 0 of 19.

**Sources.** Main to 3412bf09d (B1698, B1703, B1712, B1713, B1716, B1718, B1720, the point register) and dc758224d
(B1722); the SM seat's frame at c9f001d9d (W113, W114); chat1's zero-free reading and lepton test
(`relays/chat1_2026-10-21_zero_free/`); a literature sweep (about 90 records opened at source, §3).

**Labels.**
- **[COMPUTED]** pure mathematics, no data, run from committed instruments.
- **[SEALED]** a prediction or test committed before its data were read.
- **[POST HOC]** computed after the relevant data or rows were seen.
- **[LIT]** literature, read at source.
- **[READING]** interpretation.

## 0. In brief

1. **No selection of the state alone decides the masses in either working frame.**
   - **The SM seat's theta frame** [COMPUTED, §1]. Near the cusp, ω and i, the weave's triplet gives at most one
     parametrically light generation in a typical member. The PF1-W-tuned T⊗T sector at the cusp is the one exception,
     with a pattern the data do not have. Its hierarchies live in tuned coefficients, so near those points no choice
     of τ makes it predictive.
   - **Main's fibre frame** [POST HOC regularity, §4]. In main's census runs of this frame (B1712, B1713, B1720), no
     point does better than a factor 1.80. Where its down and lepton ratios fit within a factor 2, its leptons' second
     generation copies the down quarks' (R2 = 0.93–1.40 against the data's 3.14). That costs at least √(3.14/R2): 1.77
     at R2 = 1, 1.50–1.84 over the range. The first generation is not pinned (R1 = 1.0–10.8 against 3.37).
   - **Why** [COMPUTED: the mod-N reading; READING: what follows, §7]. The frame reads each field's hypercharge only
     modulo the line's order. That is why d = e exactly on lines of order dividing 4 or 5 (B1698, B1703), and why it
     cannot give an exact, τ-independent integer Clebsch.
2. **The data point to a law ingredient of Georgi–Jarlskog size, not to a state.**
   - The record's target P-094 is the double ratio D = (y_μ y_d)/(y_s y_e) = 10.58 ± 0.11, which is stable under
     running. It asks for a lepton–down splitting of about √D = 3.25 per generation, in opposite directions in the
     second and first generations. B1698 had already named this miss the Georgi–Jarlskog pattern (P-084, P-094).
   - Georgi–Jarlskog's exact pair (×3, ÷3) gives D = 9, which P-094 excludes. So the frame, or the ingredient, must
     supply the remaining factor 1.18.
   - Post hoc, a Clebsch 3 put by hand on main's committed rows lifts B1713's best six from 2.33 to 1.28 (0.85% of
     random hierarchies fit as well, with the Clebsch's look-elsewhere counted). Of the set ⅓ to 5, the Clebsch
     closest to the data's √D = 3.25 is 3.
3. **The mixing needs a second law fact** [POST HOC, §5]. Main's up reading S̃ conjugates the Higgs's complex flavour
   coefficients. With the up and down sectors read differently, the CKM is a near-permutation. With one reading for
   every sector it aligns.
4. **Sealed: with both ingredients put in by hand, all four cells hold on rows nobody had seen** (§6a).
   - **The nine** (the six ratios and the three CKM moduli) fit within 2.09, and 0.48% of random nine-target sets fit
     as well. This is robust: over 20 further seeds it is 0.56% ± 0.02%, every seed below the 1% bar. It is the first
     specific match of main's frame, with two by-hand ingredients, under main's own measure and calibration.
   - **The six** fit within 1.51 (0.73%). That cell holds as sealed but sits at the bar: over 20 further seeds it is
     1.17% ± 0.04%.
   - **Its limits.**
     - The new rows neighbour the rows where the ingredients were chosen, so this tests robustness more than it
       discovers.
     - The Clebsch alone makes the six specific; only both ingredients make the nine specific.
     - At P-094's precision it fails: D runs 8.7–15.5 on the good rows, none within 3σ.
     - The CKM phase is 16–40 times too small, and of the wrong sign at the best six-row.
5. **Sealed: under B1720's apex rule, the principle's threads do not select the point** (§6b). At B1720's 121 thread
   apexes with their fixed lines, the same two ingredients fit the six only within 3.22 (26.6% of random hierarchies
   as good) and the nine within 3.51 (5.1%). All four cells fail. The sealed control C2 failed as written, on
   numerical zeros, as diagnosed before the run; the control as amended before the run reproduces B1720's rows. The
   threads' apexes are not where the ingredients fit, so τ and the line still need a selection.
6. **The principle's own threads are CP-even** [COMPUTED, §2]. All 27 Christoffel classes to length 9 are
   reversal-symmetric, so a CP-symmetric law averaged on them gives J = 0.
7. **The ingredient, stated once** [READING, §7]. It is a Higgs component that reads the doublet's B − L linearly
   and enters every sector through one flavour section. Pati–Salam's (15, 2, 2) carries both facets. The size of the
   leading Clebsch is N_c = 3, forced by the SU(2)²U(1) anomaly; P-094 says the data need a little more. The record's
   own candidates for deriving it are the SM seat's: the 351′ (P-084) and a flat Wilson line along B − L (relay §66).

## 1. The theta frame: Lemma H (one level per special point)  [COMPUTED]

`hierarchy_lemma.py` → `hierarchy_lemma.json`, `_run.txt` (instrument 5c359204c, outputs 83c305364). The SM seat's
modules are imported unchanged and hash-checked. For each space, 40 random real members, and the slopes of
ln(m_i/m₃) near each point. The table gives medians. An exploration of the same computation ran in scratch first; the
committed run reproduces it.

| near | generic members (every type, k ≤ 9) | PF1-W (tuned) members |
| --- | --- | --- |
| the cusp (units of \|q\|^¼) | m₁: T⊗T 0.84–0.96, T̄⊗T̄ 2.84–2.91 (k ≥ 3; k = 1 has det ≡ 0), mixed ≈ 0. **m₂: median ≤ 0.12 in every space** (90% quantile ≤ 0.48) | T⊗T k = 5: **(m₁, m₂) = (3.95, 0.98)**; T̄⊗T̄ k = 7: (6.85, 0.05); mixed k = 4: (3.9, 0) |
| ω (powers of \|τ − ω\|) | none: all three O(1) | none |
| i (powers of \|τ − i\|) | m₁ ∝ d in the impossible class (W113: E₆ there), m₂ O(1) | none |

**Why (the residual charges).**
- **At the cusp.** T acts on the triplet with eigenphases {0, ½, ¾} (T) and {0, ¼, ½} (T̄). The two parity lines T
  swaps have charges differing by ½, so their diagonal entries carry the same charge: one level at most.
- **At ω.** ST is a 3-cycle with three distinct charges, but in every bilinear type the charge-matched entries form a
  permutation pattern, so the matrix has full rank there.
- **The tuned exception.** PF1-W's determinant c·η^{6k} vanishes at the cusp one power of q faster than a generic
  member's (w = 12). In T⊗T k = 5 that extra power splits as q^¼ into m₂.

**What follows.**
- The data's patterns are not among these. Write each sector as m₂/m₃ = x^a and m₁/m₃ = x^b: the data have
  b/a = 2.1 (up), 1.75 (down), 2.9 (leptons). T⊗T-tuned (x⁴, x, 1) has b/a = 4.
- [READING, an estimate] With θ₂² ≈ 4q^¼, that pattern would put m_u/m_t near 10⁻¹⁰ when m_c/m_t is right. So W114's
  exact fits draw their hierarchies from coefficients near the rank-deficient varieties. Penedo and Petcov
  (arXiv:2404.08032) report the same for constant-determinant modular models: the mechanism is "incompatible" with
  near-fixed-point hierarchies [LIT].
- **Near the cusp, ω and i, no choice of τ makes this frame predictive.** A selection would have to select
  coefficients. Away from them there is no small parameter, which was not computed. The SM seat's W112 (p = 0.139) is
  consistent with this.

## 2. The principle's threads and CP: Lemma CP  [COMPUTED]

`christoffel_cp.py` → `christoffel_cp_run.txt`.
- **The census.**
  - 125 primitive positive classes of length 2–9; 79 are reversal-symmetric up to conjugacy.
  - **All 27 Christoffel classes are.** These are the Sturmian words, the principle's family since GENESIS v1.49.
  - The shortest that are not: LLRLRR and LLRRLR.
  - The Christoffel part is a known theorem [LIT]: a lower Christoffel word apb (p a palindrome) has as its reverse bpa,
    the upper Christoffel word of the same class, which is a conjugate (Bugeaud and Reutenauer, "On the conjugates of
    Christoffel words", arXiv:2202.05486, §7). The census confirms it to length 9. What is new here is only its
    consequence for CP.
- **Why it matters.** A word and its reverse are CP images (B1456: M(rev w) = D·M(w)⁻¹·D⁻¹). So a reversal-symmetric
  class's geodesic is invariant under τ ↦ −τ̄.
- **What follows for a CP-symmetric law** (real coefficients, the swap in the law):
  - its average over such a thread is CP-even (J = 0);
  - at a unique apex J = 0;
  - only a mirror-pair apex carries J ≠ 0, with its sign a spontaneous choice.
- **The two threads below.** B1720's best thread, L⁵RLR², is not reversal-symmetric. L⁵R² is.
- **Where L⁵R²'s lines sit.** Its apex is at 3.5 + 2.958i. The frame is T-covariant (τ ↦ τ + n with
  (a, b) ↦ (a, b − na)), so its lines must be moved before they are compared with lines at Re τ = ½. Moved there,
  two of its eleven fixed lines have α = 2/5: (2/5, 3/10) and (2/5, 4/5), the latter B1698's order-5 line. The line
  the Clebsch fits best, (2/5, 1/2), is not among them. (An earlier draft said L⁵R² fixes it; that compared lines
  across different T-frames.)
- **In main's frame** the hypercharge line itself breaks the reflection (B1713: J ≠ 0 at Re τ ∈ {0, ½}), so this
  lemma binds the theta frame and any CP-symmetric law, not main's.

## 3. The literature: what selects τ elsewhere  [LIT]

From the sweep, every claim re-opened at its arXiv record.

**Points that are not symmetric.**
- **The only principled one:** Novichkov–Penedo–Petcov's Mexican hat around ω (arXiv:2201.02020, confirmed in
  2212.03876). It is supergravity with W ∝ H(τ)/η⁶ and H = (j − 1728)^{m/2}. Its minimum sits at
  \|u\| ≈ 0.0145/(m + 0.0625) and arg u ≈ −2π/9, off the CP lines, with spontaneous CP violation.
  - The potential is negative at the minimum at leading order (their eq. 3.1); the authors do not identify it with the
    cosmological constant.
  - H is chosen, not derived; the authors argue the choice is special rather than tuned.
- **Useless to both record frames:**
  - Lemma H gives no hierarchy at ω.
  - Main's frame gives m₂/m₃ = ½ there (S163).

**Non-supersymmetric dynamics:**
- One-loop Coleman–Weinberg potentials fix Im τ by dimensional transmutation from input scale ratios
  (2402.02071, 2412.18435). Re τ stays flat, so there is no CKM phase.
- A fermion condensate lands at ω (2502.12662).

**Zero-free determinants** (2505.20395, 2608.13796, 2506.23343):
- the valence formula gives η-power determinants;
- no paper derives the zero-free condition, and none fixes τ in that setup.

**Elsewhere:**
- **Closed geodesics, the Markov or Lagrange spectrum, Christoffel words:** no use in physics to select τ was found.
- **Rigid (magnetized-torus) Yukawas:** the coefficients are fixed, but the discrete fluxes, Higgs directions, Wilson
  lines and τ remain. The fits are order-of-magnitude (2209.07249).
- **The multiple-point principle** (exact Higgs-sector degeneracy) is in roughly 2–5σ tension with M_h = 125.20 GeV,
  depending on the top mass used (2401.08811).

**Net:** no published principle fixes both τ and the coefficients.

## 4. Main's fibre frame: the Georgi–Jarlskog-sized miss  [SEALED, then POST HOC]

`GJ_WALL_RULE.md` and `GJ_FINDINGS.md`, with their scripts and outputs. **Credit:** B1698 named the frame's d–e miss
the Georgi–Jarlskog pattern; B1703 found the coincidence law; P-094 is the record's target.

**The sealed prediction failed as worded and is withdrawn.**
- **What it predicted.** In (log D, log Z), with D the double ratio and Z the ratio of reduced determinants, no B1720
  row would reach the data.
- **What happened.**
  - Four rows did: D = 9.16, Z = 1.05.
  - Their hierarchies are far too weak: down m₁/m₃ is 0.045 against 9.4 × 10⁻⁴.
  - D and Z are ratios of ratios and do not see that.
- **A disclosure.** The commit subject of main's S188, which chat1 saw before the seal, carries B1720's best-row ratios
  (R2 = 1.02 follows from them). It does not bear on the cells.

**The corrected statement** (post hoc, on B1712, B1713 and B1720; recomputed for this note).
- **Where the four down and lepton ratios fit within a factor 2:**
  - R2 = (m_μ/m_τ)/(m_s/m_b) is 0.93–1.40 (B1712 0.93–1.04, B1713 0.93–1.40, B1720 1.00–1.02), against the data's 3.14;
  - R1 = (m_d/m_b)/(m_e/m_τ) is not pinned: 1.0–10.8 (B1712 2.0–2.4, B1713 2.0–10.8, B1720 1.0–2.7), against 3.37.
  - These are few distinct configurations, mostly on lines of order 7, 8 and 28; only B1720's (1/5, 1/5) rows lie on
    an exact d = e line.
  - Within a factor 2.5, R2 reaches 3.35 (B1713), on rows that miss elsewhere.
- **That costs at least √3.14 = 1.77** on any row with R2 ≈ 1: the factor 3.14 must be split between m_s/m_b and
  m_μ/m_τ. B1720's best point misses by 1.80, with its R2 at 1.02. No point of main's three census runs does better
  than 1.80. This is a regularity of the computed points, not a bound.

**The Clebsch, by hand** (m_μ/m_τ × c, m_e/m_τ ÷ c, the determinant kept).

| | c = 1 | c = 2 | c = 3 | c = 4 | c = 5 | calibration at c = 3 (best-of-set) |
| --- | --- | --- | --- | --- | --- | --- |
| B1713 (τ on the CP-line grid) | 2.33 | 1.40 | **1.28** | 1.48 | 1.55 | 0.20% (0.85%) |
| B1720 (thread apexes) | 1.80 | 1.80 | **1.61** | 1.88 | 1.98 | 0.53% (2.25%) |

- **The best row** is the order-10 line (2/5, 1/2) at τ = ½ + 3.1i, maximal horocycle, up reading S̃. Model over
  measured: 1.13, 0.84, 1.14, 0.86, 1.08, 0.78.
- **With the Clebsch, the best rows are where d and e nearly agree:** the order-10 lines with α = 2/5, then B1698's
  order-5 lines (exact d = e), at 1.43–1.46.
- **A finer scan** (chat1's, post hoc; `posthoc_scans.py`) gives 1.20 at Im τ = 3.08 on (2/5, 1/10), and 1.23 at
  Re τ = ¼, Im τ = 3.00. The fit is sharp in Im τ: the log of the miss doubles within ±0.1.
- **The double ratio** [the record's target, P-094]. D = (y_μ y_d)/(y_s y_e) = 10.58 ± 0.11 (Antusch, Hinze and Saad,
  arXiv:2510.01312v2, eq. 4.7), which excludes Georgi–Jarlskog's 9.
  - A Clebsch c multiplies D by c². On an exact d = e line, c = 3 gives D = 9.
  - The best rows reach D ≈ 11 only because the frame itself departs from d = e there by about 1.2.
  - So the data point to a splitting of Georgi–Jarlskog size, about √D = 3.25 per generation, not to its exact
    relation. Antusch and Spinrath (arXiv:0902.4644) reach a similar verdict at the unification scale: in two of
    three minimal supersymmetry-breaking scenarios (CMSSM, mGMSB) m_μ/m_s = 3 is disfavoured, and 9/2 or 6 are often
    favoured [LIT].
- **The scale caveat.**
  - The what-if follows main's convention: frame ratios against Huang–Zhou at M_Z, compared by the worst factor.
  - D contains no third-generation Yukawa, and at one loop its running cancels. R2 and R1 separately shift in
    opposite directions through y_b's top-Yukawa correction (main's B1718 sizes the within-sector running).
  - chat1's one-loop estimate (`rg_ratios.py`, `rg_ratios_run.txt`; diagonal Yukawas, \|V_tb\| = 1) gives, from M_Z to
    2 × 10¹⁶ GeV, R2 3.14 → 2.78 and R1 3.37 → 3.81, with D unchanged at 10.58 and y_b/y_τ = 0.62 there.
  - **What that does to the fit.** √D does not run, so 3 stays the best Clebsch of the set at any scale. What grows is
    the imbalance between R2 and R1. With a frame row at R2 = R1 = 1 and the Clebsch 3, the larger of the two misses,
    split between its two ratios, is a factor 1.06 at M_Z and 1.13 at 2 × 10¹⁶ GeV. The fits found (1.20–1.28) sit
    above both.

## 5. The mixing in the fibre frame: the reading  [POST HOC]

The numbers are from chat1's exploratory scans, re-run from the committed `posthoc_scans.py` into
`posthoc_scans.json`. `posthoc_check.py` recomputes the numbers quoted here and gives the scans' calibrations. The one
exception is the heaviest-left-vector figures (0.998; the j–k mix; the middle state on i), which the referee recomputed.

- **The Higgs.** At τ = ½ + 3.08i its flavour components along (i, j, k) are 0.030, 0.468 and 0.468, with phases
  −158°, −22° and −113°. The j and k phases are about 90° apart, so h·h ≈ 0 (\|h·h\|/\|h\|² = 0.005): an isotropic
  direction.
- **At ½ + 3.1i on (2/5, 1/2), each sector's heaviest left vector:**
  - down, with S: along the i-parity block (0.998);
  - up, with S̃: an equal mix of the j and k blocks, with the middle state on the i block.
- **So the CKM.**
  - With up S̃ and down S it is a near-permutation, \|V_us\| ≈ \|V_cb\| ≈ 0.99.
  - With the same reading for up and down it aligns. S̃–S̃ gives (\|V_us\|, \|V_cb\|, \|V_ub\|) = (0.033, 0.036, 0.0012);
    S–S gives (0.097, 0.064, 0.0002). The data are (0.225, 0.042, 0.0037), so "aligned" here means small mixing,
    not the right mixing: \|V_us\| is 6.8 times too small with S̃–S̃ at this point.
- **The reason.** For the quaternion units, εQ*εᵀ = Q, so S̃ = εS*εᵀ = Σ av_k* Q_k conjugates only the Higgs's
  coefficients. An isotropic coefficient vector goes to a different direction under conjugation, which moves the
  heaviest state to another parity.
- **The masses want S̃ for up.** With S, the up quarks' m₁/m₃ is 570 times too large at that point. The mixing wants one
  reading for all.
- **chat1's scan** (10 lines, Re τ ∈ {0, ¼, ½}, Im τ 2.3–3.5). With S̃ for every sector and the Clebsch, all nine are
  within 1.98, at τ = ½ + 2.55i on (2/5, 1/2), second horocycle. J there is 3.2 × 10⁻⁶ against 3.1 × 10⁻⁵.
  - **The calibration** (`posthoc_check.py`). On those 1 500 rows, 0.03% of random nine-target sets fit as well, with
    either draw order. Counting the choice of reading, it is 0.20% for the best of the three one-reading models and
    0.53% for the best of all 27 reading combinations. The 0.10% quoted in `TWO_INGREDIENTS_RULE.md` came from a
    separate scratch stream; these replace it.
  - `posthoc_scans.json` reproduces every number of the scratch scans exactly. The referee compared all 105 714,
    including J. The "36 000" in commit 531d5710e counted entries, not numbers.
- **A caveat for the physics.** If main's readings carry the Higgs's hypercharge (H for the up sector, H̃ for down and
  leptons, as their twist sums require), then "one reading for all" is not gauge-consistent with one doublet. It is
  with two doublets sharing one flavour section (type II), or if the 2 × 2 index is internal to the theta components.
  If the coefficients are holomorphic in τ, a supersymmetric reading (no H̃) would give S for every sector, not S̃.
  That question is main's.
- **A flavour-blind Higgs cannot replace the section** (added after the read, COMPUTED, no data;
  `relays/chat1_2026-10-22_sm_higgs_check/flavour_blind_bound.*`). With S = 1, main's coupling is u₁·1 plus an
  antisymmetric matrix in (u_i, u_j, u_k) in every sector, and m₂/m₃ ≥ ⅓ for every choice of channel weights (a short
  argument, checked numerically; the relay `CHAT1_TO_SM_2026-10-22_THE_HIGGS_ARC_CHECKED.md` gives it). So the frame's
  hierarchy is carried by the Higgs's flavour section, and the reading problem cannot be removed by making the Higgs
  flavour-blind (the SM seat's W129 test (i), in this coupling).

## 6. The two sealed tests  [SEALED]

Both import main's B1720 instrument unchanged and use main's measure of fit (the worst factor) and main's calibration
(random targets fitted with the same rows, seed 1720, 4 000 draws). Both rules and their instruments were committed and
pushed before their runs, and each run's output was committed before its comparison was run and read.

### 6a. The two ingredients off the CP lines (`TWO_INGREDIENTS_RULE.md`, 9387ed764)

- **Rows nobody had seen.** B1713's 266 lines of order ≤ 12 at Re τ ∈ {0.1, 0.4} and Im τ = 2.0–3.5: 8 512 points,
  17 024 rows.
- **The model.** S̃ for every sector and the Clebsch 3 on the leptons.
- **The order of events.** Rule and instruments pushed at 17:23 (9387ed764); the census ran in one launch of 5 384 s;
  its output was committed unread (d79e7f864); the comparison ran, and its output was committed before it was opened
  (11b74b3f1).

| cell | prediction | prior | result |
| --- | --- | --- | --- |
| F1 | the best six within a factor 2.0 | 70% | **HOLDS**: 1.513 |
| F2, specific | at most 1% of random hierarchies fit the six as well | 40% | **HOLDS**: 0.73% |
| F3 | the best nine within a factor 2.5 | 55% | **HOLDS**: 2.087 |
| F4, specific | at most 1% of random nine-target sets fit as well | 30% | **HOLDS**: 0.48% |
| C1, control | as sealed: "`two_ingredients_census.point` reproduces chat1's scan value at (τ = ½ + 3.08i, line (2/5, 1/10)) to 10⁻⁹". The code compares with main's own `ratios_at` there; chat1's scan value is bit-identical to it | 99% | **HOLDS**: 0.0 under either wording |

- **The best rows** (`two_ingredients_after.*`, read-outs committed before they were read).
  - Six: the order-10 line (2/5, 1/10) at τ = 0.4 + 2.7i, second horocycle. Model over measured: 1.36, 0.66, 0.72,
    0.73, 0.71, 0.84.
  - Nine: (2/5, 1/2) at the same τ. Model over measured: 1.17, 1.48, 0.79, 0.91, 0.78, 0.61 for the six;
    0.60, 0.48, 0.86 for \|V_us\|, \|V_cb\|, \|V_ub\|. \|V_cb\| sets the 2.09.
  - The ten best six-rows are all on order-10 lines with α = 2/5, at Im τ = 2.5–2.8. The best one's miss runs
    2.38, 1.79, **1.51**, 1.98, 2.90 at Im τ = 2.5 to 2.9: sharp in Im τ.
  - Among the 100 best six-rows the line orders are 10 (40), 8 (33) and 5 (27).
  - J at the best rows is −7.7 × 10⁻⁷ (the wrong sign) and 1.9 × 10⁻⁶, against 3.1 × 10⁻⁵.
- **The sampling of the specificity cells** (`seed_robustness.*`, post hoc, labelled; the referee found it first). The
  same calibration with seeds 100–119 gives the six 1.17% ± 0.04% (range 0.90–1.50%; 5 of 20 seeds at or below 1%) and
  the nine 0.56% ± 0.02% (range 0.40–0.73%; all 20 below 1%). F2 holds as sealed, with the sealed seed, but it sits at
  the bar. F4 is robust, and the specificity claim rests on it.
- **Each ingredient alone** (read-outs from the same rows, the same calibration):

  | model | best six (random as good) | best nine (random as good) |
  | --- | --- | --- |
  | main's readings, no Clebsch | 2.34 (14.3%) | 22.1 (32%) |
  | main's readings, with the Clebsch | 1.27 (0.13%) | 22.1 (32%) |
  | S̃ for every sector, no Clebsch | 2.55 (22.3%) | 3.27 (11.1%) |
  | **both (the sealed model)** | **1.51 (0.73%)** | **2.09 (0.48%)** |

  - The Clebsch makes the six specific.
  - The reading makes the mixing possible; only both together make the nine specific.
- **The double ratio** (`d_readout.*`, post hoc, labelled). D is 8.96 at the best six-row and 15.49 at the best
  nine-row. Among the rows fitting the six within 2 or the nine within 2.5, D runs 8.7–15.5, and none is within 3σ of
  P-094's 10.58 ± 0.11. The range straddles the target, but no row on this grid meets it.
- **The reading, as written before the run.** F2 and F4 hold: "the frame with these two law ingredients describes the
  six ratios and the three moduli specifically at points it was not tuned on. That would be the frame's first specific
  match. It stays a structure with two ingredients put in by hand, not a derivation." Three qualifications, all
  disclosed in `THREADS_C2_AMENDMENT.md` or found after the read:
  - **Continuity.** Re τ = 0.1 and 0.4 neighbour the Re τ ∈ {0, ¼, ½} where the ingredients were chosen, on the same
    α = 2/5 lines. F1 and F3 were largely predictable; F2 and F4 carry the forward information.
  - **The calibration stream.** The nine-target draws come from a different stream than main's (same seed and
    distributions).
  - **Precision.** Main's worst factor is coarse. At the precision of P-094 the structure, with the exact Clebsch 3,
    does not fit.

### 6b. The principle's threads with the ingredients (`THREADS_WITH_INGREDIENTS_RULE.md`, 40079f41d)

- **The selection is the principle's.** B1720's 121 thread classes at their apexes, with the lines their monodromy
  fixes: 3 249 points, 6 498 rows, no continuous number free.
- **The model.** The same two ingredients. This rule was sealed before any result of 6a was read.
- **The control.** Before the run, chat1's referee found that the sealed control C2 would fail on numerical zeros
  (5 012 of B1720's committed values are below 10⁻⁸). C2 is kept and reported as written, and C2′ was added before the
  run (`THREADS_C2_AMENDMENT.md`, 9d3b7efc9).
- **The order of events.** The amendment was pushed at 18:56:16 and the run started at 18:56:31. The census ran in
  one launch of 2 378 s, and its output was committed unread (fcdd98c77). The comparison and C2′ ran and were
  committed before either was opened (e446c8b6d).

| cell | prediction | prior | result |
| --- | --- | --- | --- |
| H1 | the best six within a factor 2.0 | 45% | **FAILS**: 3.22 |
| H2, specific | at most 1% of random hierarchies fit the six as well | 25% | **FAILS**: 26.6% |
| H3 | the best nine within a factor 2.5 | 35% | **FAILS**: 3.51 |
| H4, specific | at most 1% of random nine-target sets fit as well | 20% | **FAILS**: 5.1% |
| C2, control, as sealed | (a) B1720's committed values recomputed to 10⁻⁶ in \|ln\|; (b) B1720's best six reproduced | 97% | **FAILS**, as diagnosed before the run: (a) 655 in \|ln\|, on a numerical zero; (b) holds, 1.8037155975 against 1.8037155975 |
| C2′, added before the run | (a) values below 10⁻⁸ to 10⁻⁹ in absolute value, the rest to 10⁻⁶ in \|ln\|; (b) as sealed | — | **HOLDS**: the 5 012 zeros agree to 4.2 × 10⁻¹², the rest to 1.4 × 10⁻⁷; (b) holds |

- **The best rows.**
  - Six: L⁴RL³R (and its mirror) at 3.0 + 2.793i on (11/26, 3/13), first horocycle. Model over measured: 3.00, 0.82,
    1.17, 0.78, 0.39, 0.31.
  - Nine: L⁵R²LR at 3.4 + 2.993i on (11/28, 27/28), second horocycle, at 3.51.
  - The ten best classes by their best six: L⁴RL³R 3.22, L⁴RLRLR 3.29, L⁵R²LR and L⁵RLR² 3.51 (each with its mirror),
    then L⁴R at 4.61.
- **Read-out: main's readings with the Clebsch** at the same apexes. The six is 1.614, at L⁵R² on (2/5, 3/5), which is
  B1698's order-5 line moved to Re τ = 3.5; that reproduces chat1's post hoc figure. The nine is 22.2.
- **The reading, as written before the run.** "If H1 and H3 both fail, the threads' apexes are not where the
  ingredients fit, and Im τ needs another selection." That is the outcome.
  - **Where the ingredients fit** (§6a, with 0 ≤ Re τ < 1): Re τ = 0.4 (and ½ in the post hoc scans), Im τ about
    2.65–2.7, the second horocycle, on the lines (2/5, 1/10) or (2/5, 1/2) specifically. The fit is sharp in Re τ and
    in the line's offset, not only in Im τ: at ½ + 2.65i on either line it is 1.50, while at Re τ = 0 on (2/5, 1/2) it
    is 9.7–21.
  - **No thread apex lands there.** Apexes do reach the order-10 α = 2/5 family near Im τ = 2.6–2.7, but only at
    Re τ = 0 on (2/5, 1/2) (L⁴RL²R and L⁴RLRLR) or at Re τ = ½ on (2/5, 3/10) (L⁵R⁴). There the sealed model misses by
    13.5–13.7. (Both bullets are post hoc, `threads_alpha25_run.txt`; the referee found the point.)
  - [POST HOC read-out, `threads_alpha25.*`] 47 of the 121 classes do have an α = 2/5 fixed line, with apexes at
    Im τ from 1.12 to 3.87. The best six among those rows is 3.58 (L⁴RLRLR at 3.0 + 2.622i on (2/5, 11/20), second
    horocycle). Those apexes and lines are not the points the ingredients favour.
  - So the principle's threads, as B1720 defines the point a thread fixes, do not supply the selection the two
    ingredients leave open. This is a sealed negative for that rule, not for every rule a thread could define.

## 7. What the ingredient must be, and how the record could derive it  [READING]

**Why the frame cannot supply it as it stands.**
- On the line w = ατ + b, a field of charge q enters main's frame through its theta characteristics (qα, 2qb).
  Shifting q by the line's order N moves them by integers (by even integers in the second slot). That changes the
  sector's coupling by an overall phase, which leaves its singular values and \|V\| unchanged. So the frame reads each
  field's 6Y only mod N.
  - [COMPUTED] `mod_n_check.py` (committed before its run) confirms it on lines of order 4, 5, 7 and 10. Charges
    shifted by multiples of N change no ratio and no \|V\| by more than 3 × 10⁻¹¹.
- This is B1698's and B1703's coincidence law, seen from the charges:
  - N | 5: 6Y ≡ 1 on Q, u, e and ≡ 2 on d, L, the SU(5) multiplets. The down and lepton ratios agree to 10⁻¹³.
  - N | 4: Q ≡ L and d ≡ e. The quark and lepton doublets differ by 6Y = 3(B − L) = 4, which mod 4 does not see,
    so this is Pati–Salam's quark–lepton symmetry. The ratios agree to 10⁻¹⁴, and the lightest state is massless.
  - Lines of order 7 and 10 do not give d = e (the ratios differ by factors up to 15 and 1.4 at the τ checked).
- **What a Georgi–Jarlskog-type Clebsch needs is the integer.** Its leading term is Y(L)/Y(Q) = −3, and equivalently
  (B − L)(L)/(B − L)(Q) = −3, since Y = (B − L)/2 on the SU(2)_L doublets. A reading mod N gives no exact,
  τ-independent integer ratio; on a line of other order it splits d from e by a τ-dependent amount (B1692, B1693).

**The size of the leading term is not a free number.**
- −3 = −N_c is forced in the Standard Model: the SU(2)²U(1) anomaly cancels only if N_c·Y(Q) + Y(L) = 0.
- So a coupling linear in the doublet leg's hypercharge (equivalently its B − L) gives the lepton and down sectors
  Clebsches in the ratio −3 : 1, with the factor fixed by the anomaly.
- In unified-theory language, such a coupling is a Higgs component along B − L:
  - SU(5)'s 45 gives (d, e) = (1, −3); its coupling to the up quarks is antisymmetric.
  - SO(10)'s 126 and Pati–Salam's (15, 2, 2) give (u, d, e) = (1, 1, −3).
  - E₆'s 351′ contains them (Babu, Bajc and Susič, arXiv:1504.00904). The SM seat had already found that only a Higgs
    outside the 27s, the 351′, can split d from e in the E₆ frame (P-084).
- **P-094 says the data need more than the pure term.** Georgi–Jarlskog's texture (the B − L term in the middle
  generation only) gives D = 9, or less with its off-diagonal entries, against 10.58 ± 0.11. The rest must come from
  the frame or from a second term.

**One ingredient, two facets.**
- Pati–Salam's (15, 2, 2) carries both requirements at once.
  - Its 15 carries B − L, which gives the Clebsch.
  - Its bidoublet (2, 2) gives the up and down sectors' Higgs from one field, so they share one flavour section. That
    is §5's second requirement.
- So the missing ingredient, stated once, is a **law ingredient: a Higgs component that reads the doublet's B − L
  linearly and enters every sector through one flavour section.** It is not a choice of state.
- §6a tests a by-hand stand-in for this structure: the Clebsch applied to stored singular values, plus a reading rule.
  It does not test a B − L Higgs component. The stand-in is specific at main's measure, and it misses P-094.

**How the record could derive it.** These are questions for main, not claims.
- **A flat Wilson line along B − L, near zero** (the SM seat's relay §66, P-084). On a line of infinite order the
  frame reads the charges as numbers, not residues. Near w = 0 the first term of the doublet leg's theta factor is
  linear in q·w, which is a coupling linear in the charge: the jet ∂_w brings down the integer q.
- **A condensate Higgs.** If the Higgs is a bilinear of two matter fields (W70's cusp condensate), Sym²(27) = 27̄ ⊕ 351′
  contains the needed component without a new field.
  - W70's condensate class has two Y = +½ and two Y = −½ doublets. That is the field content of the second facet
    (type II, two doublets sharing one flavour section).
- **Which reading is which.** Whether B1656's 2 × 2 index is SU(2)_L or the theta components' internal index decides
  whether "one reading for all" is gauge-consistent as written (§5).

**What then remains to select.**
- τ. The fits put Im τ near 2.7 at the second horocycle and near 3.1 at the first, sharply, with Re τ off 0 (0.4 or
  ½ fit; 0 does not).
- The line: (2/5, 1/10) or (2/5, 1/2), not merely the order-10 family with α = 2/5.
- The horocycle, which is one of two.
- The CKM phase, which is 16–40 times too small at the best rows (and of the wrong sign at one). Lemma CP says where a
  phase can come from.
- **The principle's threads, under B1720's apex rule, do not decide the first three** (§6b, sealed): no thread apex
  with its fixed lines is where the ingredients fit. The selection the owner asked for is therefore still missing.
  What is now known is its target, in a frame with the two ingredients and 0 ≤ Re τ < 1: Re τ near 0.4–½, Im τ about
  2.65–2.7, the second horocycle, and the line (2/5, 1/10) or (2/5, 1/2). The fit is sharp in each of these.

## 8. What this does not do

- **It derives none of the nineteen.** 0 of 19.
- **The two ingredients are put in by hand.**
  - The Clebsch acts on the frame's stored singular values (m_μ/m_τ × 3, m_e/m_τ ÷ 3, the determinant kept). It is not
    a coupling with a B − L component built into the frame. Such a coupling would change the other entries too.
  - The reading rule is not derived, and its gauge consistency is open (§5).
- **The Higgs itself is assumed.** Main's DR is the SM seat's ∂R (W123).
  - With untwisted end data O(nδ), a weight-3/2 Higgs exists iff n ≥ 1, in a space of dimension 3n (W123 as
    corrected). A unit on v₊ alone is a chosen line, where ∂R is the only section.
  - So both sealed tests rest either on GENESIS FK10's unit O(δ) plus the choice of ∂R among its three directions, or
    on a unit on v₊ alone.
  - The SM seat's W130 forces a field of the fibre's own SL(2) to be non-zero. Whether that field is this Higgs is the
    open dictionary question (GENESIS FK11).
- **The sealed match is at main's coarse measure.** At the precision of the record's double-ratio target (P-094) it
  fails, and the CKM phase is far off.
- **Even if both ingredients were derived and a selection fixed τ, the line and the horocycle, this frame would reach
  at most ten of the nineteen:** the six mass ratios, the three CKM moduli and the CKM phase. It does not touch:
  - the three overall scales (m_t, m_b, m_τ), since the frame gives ratios;
  - the three gauge couplings, θ_QCD, and the Higgs mass and vacuum value.
- **The comparison convention is main's:** frame ratios against Huang–Zhou at M_Z, by the worst factor.
  Georgi–Jarlskog is a unification-scale relation; §4 gives the size of that difference.
- **The scope of the lemmas.**
  - Lemma H covers the SM seat's theta frame as built (its three bilinear types, weights k ≤ 9, near the cusp, ω and
    i). It does not exclude other theta-frame constructions.
  - Lemma CP is a symmetry statement. It computes no J.
- **The literature sweep was a sample** (about 90 records opened at source), not a census.
- **Only §6 is a forward test, and §6a's rows neighbour rows already seen.** Everything in §4 and §5 was chosen knowing
  the data.
- **§6b tests one thread rule** (B1720's: the apex and the monodromy-fixed lines) with one pair of ingredients. Other
  rules by which a thread could fix a point were not tested.
