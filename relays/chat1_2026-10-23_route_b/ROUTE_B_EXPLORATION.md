# Step 1, route (b): at well-fitting rows, a −3 on a second Higgs direction moves the lepton ratios toward Georgi–Jarlskog only where the down quarks and leptons see the Higgs's own components, and there the mixing fails (exploratory; three of the four readings tested)

chat1, 2026-10-23. **EXPLORATORY, labelled.** No cell, no seal, no data in the design; the read-outs compare with the
record's targets. Route (b) of step 1 in chat1's plan (make the Clebsch a frame quantity). Refereed read-only three
times before it left; the referee's corrections are applied. 0 of 19.

## What was done

- **The Higgs space.** With GENESIS FK10's unit O(δ), the weight-3/2 sections of ρ_T form a three-dimensional space
  (main's B1700, exact). Its basis:
  - h1 = ∂R, main's Higgs: line orders (1, −1, 3), the only member holomorphic off v₊, and m₂/m₃ ~ \|q\|^{1/2};
  - h2 = E₄²(E₄∂R + E₆R/12)/Δ and h3 = E₄E₆(∂²R − E₄R/48)/Δ: line orders (−7, −1, −5), no hierarchy alone.
  - All three carry the same multiplier, so every constant combination is covariant in main's frame.
- **The model, Pati–Salam-type.** The (1, 2, 2) part lies along h1 with Clebsch 1 in every sector. The (15, 2, 2) part
  lies along a second direction s, with the B − L Clebsch: 1 for quarks, −3 for leptons.
  - S_quarks = S(h1) + κ S(s) and S_leptons = S(h1) − 3κ S(s), with S(v) = v_i Q_I + v_j Q_J + v_k Q_K as in main's
    frame. Main's coupling is linear in S.
  - κ = ρ e^{iφ} \|h1(τ)\|, with log₁₀ ρ = −4.0, −3.9, …, 1.0 and φ = 0°, 15°, …, 345°.
  - No by-hand factor acts on any output.
- **The directions s, as scanned.** These were the unit vectors û2 = h2/\|h2\| and û3 = h3/\|h3\| at τ, and four
  combinations (û2 + e^{iψ}û3)/√2, ψ = 0°, 90°, 180°, 270°.
  - The combinations are not of unit length. At the fourteen S̃ points û2 and û3 are nearly opposite (û2·û3 between
    −0.986 and −0.999), so c0 has length 0.04–0.12 and c180 about √2.
  - **So effectively two directions were sampled** (`route_b_referee_checks.py`):
    - the direction û2 ≈ −û3, shared by h2, h3, c90, c180 and c270, which at these Im τ is led by the i-line (order
      x⁻⁷ in B1700);
    - c0, whose overlap with the conjugate of h1 is 0.9965–0.9996.
- **The readings.** Main's S̃ = εS*εᵀ equals S of the conjugated components, S̃(v) = S(v̄) (`readings_identity.py`:
  exact on 1 000 random v; the selection map §5 had stated it). So a reading says, sector by sector, whether the
  coupling sees the Higgs's components h or their conjugates h̄. Both are covariant (main's B1724).
  - The scan used S̃ for every sector (the sealed census's second ingredient) and the split reading (up S̃; down quarks
    and leptons S).
  - The split reading gives the up quarks and the down quarks and leptons conjugate components, as the Standard
    Model's two Yukawa terms do. Which split is the Standard Model's depends on the hypercharge the frame gives S, and
    that is open (selection map §5).
  - A post hoc pass added S for every sector and the flipped split (up S; down quarks and leptons S̃).
- **Fourteen base points.** Ten are the distinct base points among the sealed census's ten best six-rows (S̃, by-hand
  Clebsch 3). All lie on α = 2/5 lines, at Re τ 0.1 or 0.4 and Im τ 2.5–2.8. The other four are on the tick's d = e
  line (2/5, 4/5) at ½ + i{2.9, 3.0, 3.1, 3.2}. **So the base points were chosen on the data, in the reading S̃.**
- **The instrument.** Main's B1720 instrument at 3412bf09d, unchanged, imported through `two_ingredients_census.py`.
- **The order of events.**
  - `route_b_scan.py` (506579a06) was committed before its run. Its output (75ac447e9) was committed unread.
  - `route_b_readout.py` (648cc5fab) was committed before that output was read. Its run (c3eb83a18) was committed
    before it was read.
  - Post hoc scripts followed, labelled, each written after the previous output was read. Each was committed before
    its run, and each output before it was read:
    - `route_b_clebsch1_control.py` and `route_b_posthoc.py` (b603a2b9d). The control's output was written at 00:42
      and committed unread at 7ae509f40; the posthoc run followed, its output committed at bfee31b24.
    - `route_b_posthoc2.py` (1635baefe; 136613eb0);
    - `route_b_split_control.py` (46187b1b3; 775b2deb7);
    - `route_b_readings.py` (b26ee079f; 9ea4f27dd);
    - `route_b_sall.py` (22ff515b2; ccbc2bf0e);
    - `readings_blocks.py` (534fd78d4; 95d1a2d86), toward step 2;
    - `route_b_referee_checks.py` (bcba50e7c; af4a1c244) and `route_b_referee_checks2.py` (ff421d533; 97db0a153),
      at the referee's prompts.
  - `readings_identity.py` (3087e14fc) was committed together with its run, after the run.
- **Controls** [COMPUTED], in `route_b_controls.json`, at the first base point:
  - B1700's line orders are reproduced for h1, h2 and h3.
  - At κ = 0 the instrument equals the census instrument exactly (max \|Δ ln\| = 0.0).
  - s = h1 leaves every ratio unchanged (1.2 × 10⁻¹¹), as linearity in S requires.
  - The mixed Higgs (s = h2, one κ) is T-covariant: τ → τ + 1 with b → b − a changes no ratio or \|V\| by more than
    5.9 × 10⁻¹².

## What came out

All numbers are worst factors over the targets (main's measure: Huang–Zhou at M_Z and PDG's three \|V\|). "Random as
good" is the fraction of 4 000 random targets from main's generator that the same rows fit at least as well. The
sealed census's bars were six ≤ 2.0, nine ≤ 2.5, and 1% for each fraction. R2 = (m_μ/m_τ)/(m_s/m_b),
R1 = (m_d/m_b)/(m_e/m_τ) and D = R2·R1. The data give R2 ≈ 3.1 and R1 ≈ 3.4, and, at the record's precision (P-094),
D = 10.58 ± 0.11.

**Reading S̃ for every sector** (the reading in which the mixing works):

| model | rows | best six | best nine | best six where D is within 3σ of P-094 | six / nine: random as good |
| --- | --- | --- | --- | --- | --- |
| census, no Clebsch | 17 024 | 2.55 | 3.27 | 4.33 (86 rows) | 22% / 11% |
| census, by-hand Clebsch 3 (sealed) | 17 024 | 1.51 | 2.09 | 8.46 (164 rows) | 0.73% / 0.47% |
| route (a), B − L line (`BL_LINE_EXPLORATION.md`) | 3 points | 2.62–3.48 | – | 7.3–11.7 | – |
| **route (b), Clebsch −3** | 205 632 | **2.17** (2.07 with κ continuous) | **2.47** (2.23) | **2.54** (82 rows; 2.53) | 6.0% / 2.0% |
| route (b), Clebsch −3, s = h3 only | 34 272 | 2.17 | 2.54 | – | 2.9% / 0.98% |
| **control: the second direction with Clebsch 1** | 205 632 | **1.91** | **1.91** | 4.11 (24 rows) | 3.5% / 0.35% |

1. **Route (b) does not reach the by-hand result in this reading.**
   - κ → 0 is on the grid, so a gain at every base point is guaranteed. Its size: at the ten census points the best
     six falls from 2.68–5.48 to 2.17–2.82, and at the tick from 14–30 to 3.5–3.9.
   - The best six is 2.17 on the grid and 2.07 with κ continuous. The refinement was Nelder–Mead from the best rows of
     the five best distinct (base point, direction, horocycle) triples (three for the nine). The best nine is 2.47 and
     2.23. The six stays above the sealed bar of 2.0 everywhere.
   - Specificity fails the sealed bars: 6.0% (six) and 2.0% (nine) over the full menu. With the base points chosen on
     the data, these fractions favour the data, so the failures are robust.
2. **The −3 is not what improves the fit.** The control is the same scan on the same rows with the second direction's
   Clebsch set to 1 in every sector. It fits better: six 1.91 and nine 1.91. So the gain over the census is the extra
   freedom, a direction and a complex κ, and the −3 worsens the fit (2.17 against 1.91).
3. **Nor does the −3 reach P-094 through a Georgi–Jarlskog split.**
   - With the −3, 82 rows have D within 3σ of P-094, against 24 in the control. The best six there is 2.54 on the
     grid and 2.53 with κ continuous.
   - But at that row R2 = 1.20 and R1 = 8.60, so D is reached almost entirely through the first generation.
   - Only 19 rows have D in band with both R2 and R1 in [2, 4.5]; the best six among them is 16.8.
   - Against the census (4.33 without the Clebsch, 8.46 with it), what differs is route (b)'s free complex κ: the
     census has nothing continuous to tune D at its good rows. The like-for-like reference is the control's 4.11.
   - The best six-rows have small D: 2.02 at the grid's best row, and 1.05 with κ continuous. All five refinements
     held in band end at its lower edge, D = 10.25.
4. **At well-fitting rows the −3 does not act as Georgi–Jarlskog.** At the best six-row R2 = 1.04 and R1 = 1.94 (the
   control's: 1.03 and 1.72), so the second direction does not carry the second generation.
   - With the −3, 427 rows have both R2 and R1 in [2, 4.5] (none in the control), but the best six among them is 3.55.
   - Model over measured at the best six-row: m_c/m_t 1.98, m_u/m_t 1.77, m_s/m_b 1.39, m_d/m_b 0.50, m_μ/m_τ 0.46,
     m_e/m_τ 0.88; \|V_us\| 0.23, \|V_cb\| 1.09, \|V_ub\| 0.68.
   - J at the best nine-row is 2.0 × 10⁻⁶, about 16 times too small (measured 3.1 × 10⁻⁵).

**All four readings** (up; down quarks; leptons). Six / nine, with R2 and R1 at the best six-row where computed:

| reading | census, by-hand Clebsch 3 | census, no Clebsch | route (b), Clebsch −3 | route (b), Clebsch-1 control |
| --- | --- | --- | --- | --- |
| h̄; h̄; h̄ (S̃ for every sector) | 1.51 / 2.09 | 2.55 / 3.27 | 2.17 (1.04, 1.94) / 2.47 | 1.91 (1.03, 1.72) / 1.91 |
| h̄; h; h (split) | 1.27 / 22.1 | 2.34 / 22.1 | **1.74 (2.28, 3.26)** / 22.9 | 1.83 (1.00, 1.10) / 22.6 |
| h; h; h (S for every sector) | 2.04 / 4.01 | 3.63 / 4.46 | 2.47 (2.71, 5.10) / 4.60 † | 2.45 (2.46, 0.60) / 4.41 † |
| h; h̄; h̄ (flipped split) | 1.35 / 23.4 | 2.93 / 23.4 | not tested (53 at the S̃ points) | not tested (53 at the S̃ points) |

† At that reading's own ten best census points (`route_b_sall.py`, post hoc), not at the fourteen S̃ points, where it
fails outright (best six 23).

5. **In the split reading the −3 moves R2 and R1 toward the Georgi–Jarlskog values.**
   - The best six is 1.74 (random as good 0.83%, at data-chosen points), with R2 = 2.28 and R1 = 3.26. At that row's
     base point and horocycle the frame's own ratios (κ → 0, no Clebsch) are R2 0.98 and R1 1.32
     (`route_b_referee_checks2.py`), so the −3 raised both.
   - The control reaches 1.83 (1.08%) with R2 = 1.00 and R1 = 1.10, and has no row with both ratios in [2, 4.5].
   - Where D is within 3σ of P-094, the best six is 2.70 with the −3 (93 rows), against 16.9 in the control (19 rows).
   - Model over measured at the best six-row: m_c/m_t 1.27, m_u/m_t 0.93, m_s/m_b 1.51, m_d/m_b 0.57, m_μ/m_τ 1.10,
     m_e/m_τ 0.59. D there is 7.44.
   - **At P-094 the census does as well or better in this reading.** With the by-hand Clebsch, 179 of its rows have D
     within 3σ, and the best six among them is **1.46** (0.4 + 3.1i on (2/5, 1/10), L_max; R2 2.97, R1 3.63,
     D 10.76). Without any Clebsch it is 2.55, with R2 0.66 and R1 15.8.
6. **But the mixing fails in the split reading.**
   - At route (b)'s best six-row \|V_us\|, \|V_cb\| and \|V_ub\| are 4.4, 24 and 6.2 times the data (so \|V_us\| and
     \|V_cb\| are near 1), and the best nine is 22.9.
   - This is the reading, not route (b). The census's split reading reaches only 22.1 over all its lines. At the
     census's D-matched best row \|V_us\|, \|V_cb\| and \|V_ub\| are 4.4, 24 and 13 times the data (nine 23.8).
   - Item 10 gives the mechanism.
7. **Among the four readings, only S̃ for every sector brings the nine within 2.5** (the census's rows with the
   by-hand Clebsch, all lines, every τ on its grid; 3.27 without it). S for every sector reaches 4.0, and the two
   splits 22–23.
   - At the fourteen S̃ points the readings with h on the up quarks fail outright: the best six are 23 and 53. So
     route (b) in those two readings is not tested at these points; item 8 takes S for every sector at its own points.
8. **S for every sector, at its own points (post hoc).** `route_b_sall.py` took the ten distinct base points among
   the census's ten best six-rows in this reading (with the by-hand Clebsch, as the S̃ points were chosen).
   - **At the best six-row the −3 moves R1, not R2.** There R2 = 2.71 is the frame's own: at κ → 0 these order-9 lines
     give R2 2.43–2.85 (L_max) or 4.4–5.2 (L_2), with R1 0.44–0.61 (`route_b_referee_checks2.py`). The −3 takes R1
     from 0.61 to 5.10, past the data's 3.4.
   - 1 353 rows have both ratios in [2, 4.5], against none in the control. Where D is within 3σ of P-094, the best six
     is 2.53 (429 rows), against 38.9 in the control (33 rows).
   - But the six are no better than the control's (2.47 against 2.45), and the mixing is poor: the best nine is 4.60
     (4.41 in the control), and 15–17 at the rows where the −3 acts.
   - Random as good: 3.8% and 2.2% (six, nine), at data-chosen points.
   - The flipped split was not tested at its own points.
9. **The control's best row amounts to a blend of main's two readings of ∂R** (`route_b_referee_checks.py`,
   `route_b_referee_checks2.py`).
   - Its best six and nine (1.91, the same row) use c0, at 0.46% admixture. The −3's best nine-row also uses c0. The
     −3's best six (2.17) uses h3.
   - c0 is a different section, a constant combination of h2 and h3; only its value at these τ lies along the
     conjugate of h1. With c0 replaced by that projection, the coupling is ∂R read as S̃ plus 0.0046·e^{iθ} times ∂R
     read as S, and it gives six and nine 1.906, as before.
   - A blend with a fixed coefficient is not covariant: under τ → τ + 1 (b → b − a) it changes the outputs by up to
     1.49 in ln. It is covariant only if the coefficient turns by −i at each T step (residual 8.9 × 10⁻¹²), which is
     what c0's does (the c0 model: 1.1 × 10⁻¹¹). So a blend is admissible only when a section carries its coefficient.
10. **Why a split reading's mixing fails** (`readings_blocks.py`, post hoc, at the census's ten best S̃ rows and ten
    best D-matched split rows; the selection map §5 found the same at one point).
    - With h, the up and down quarks' heavy state lies on main's Q_I block (weight 0.97–1.00). With h̄, it lies off
      that block (weight at most 0.01).
    - So a reading that gives up and down different components puts their heavy states on different blocks. At all
      twenty rows, with either split, the permutation nearest \|V\| is never the identity.
    - At these twenty rows, which were chosen with the up quarks reading h̄, the up quarks' m₁/m₃ with h is 2 × 10⁻³
      to 1 × 10⁻² (data 7.3 × 10⁻⁶), and with h̄ it is 3 × 10⁻⁶ to 2 × 10⁻⁵.
    - That is by construction, not a law. At the census's own best rows with h on the up quarks, the six fit within
      2.04 (S for every sector) and 1.35 (flipped split), both with the by-hand Clebsch (`route_b_readings_run.txt`).
    - So item 10 shows why a split's mixing fails. It does not show that the up quarks need h̄.

## The reading [READING]

- **In the reading where the mixing works, the lesson of route (a) repeats.** In main's frame h1 and the hypercharge
  line already make all three generations. A second direction with no hierarchy of its own (B1700: m₂/m₃ ~ \|q\|⁰
  alone) perturbs that hierarchy. It does not generate the second generation.
  - Georgi–Jarlskog needs the −3 on the term that makes m₂, with the determinant Clebsch-1, so that R2 and R1 both
    approach 3.
  - At the best S̃ rows the second direction does not dominate m₂ (R2 ≈ 1). Where D matches, it is almost only the
    first generation that moves. Georgi–Jarlskog-like rows exist, but they fit at 3.55 at best.
- **At well-fitting rows the two jobs sit in different readings, among the three tested.**
  - Where the down quarks and leptons see h, the −3 moves the lepton ratios. In the split reading it raises R2 from 0.98
    to 2.28 and R1 to 3.26, at a six of 1.74. With S for every sector it moves R1 (to 5.1, past the data); R2 there is
    the frame's own.
  - Where up and down both see h̄, the mixing works.
  - No reading tested does both. The flipped split is untested.
- **Item 10 says why a split's mixing fails.** A split puts the up and down quarks' heavy states on different blocks.
  One reading for up and down aligns them. S̃ for every sector does so with the best mixing (2.09 by hand); S for
  every sector does so with poorer mixing (4.0 by hand, 4.4–4.6 with route (b)).
- **In the split reading the by-hand factor already fits the six within 1.46 with D at P-094** (one row of 179 in band;
  post hoc, not calibrated). What fails there is the mixing.
  - In S̃ for every sector it is the other way round: the six and nine fit (1.51, 2.09), and D misses P-094.
  - Main's frame does not say which components a sector sees, or whether a sector may see a blend carried by a section
    (item 9). That is the reading question the selection map left open (its §5 and §7; GENESIS FK11). Route (b)
    sharpens it: the ingredient is not only a −3 but a rule for which sector sees h and which h̄, one that keeps the
    up and down heavy states on one block (item 10).
  - The census's split-reading fractions (0.13% and 0.10% for the two splits) are single-seed and per reading. Main's
    B1725, counting the choice among covariant reading assignments, put the census's six at the bar (0.97%, 14 of 20
    seeds).
- **So route (b), with the unit's untwisted directions, does not supply the ingredient** at these points. This is an
  exploratory negative, scoped to:
  - effectively two directions (the û2 ≈ −û3 direction, and c0 near the conjugate of h1), with κ on a grid refined
    continuously at the best rows;
  - a second direction confined to span(h2, h3). If s may carry an h1 component, s = αh1 + s′ with s′ in
    span(h2, h3), then the ratios depend only on κ/(1 + ακ) for the quarks and −3κ/(1 − 3ακ) for the leptons, and α
    and κ make these independent. So the −3 has content only through B1700's basis, which is a choice, not a principle;
  - fourteen base points chosen on the data in the reading S̃, ten more for S in every sector, none for the flipped
    split;
  - a Clebsch on a whole direction. A −3 on one line component of h1 alone was not tried, and would need a reason.
- **What it does show.**
  - In the reading S̃, D = 10.58 is reachable at a six of 2.5, but almost only through the first generation, and never
    with a fitting six.
  - A small admixture of the other reading of ∂R, carried covariantly by c0, improves the S̃ fit to 1.91 for the nine
    (random as good 0.35%, at data-chosen points). That is post hoc.
- **No sealed test follows.** The exploration offers no rule-shaped prediction to seal: κ is a free complex number,
  the best S̃ rows fail the six bar, and the −3 worsens the S̃ fit. A seal would test a model already seen to fail on
  the same rows.
- **What remains of route (b).**
  - W133's twisted zero-free lines, which main's P-294 names as the natural candidates.
    - Under T and S a twist multiplies the coupling by a phase, which no ratio, \|V\| or J sees.
    - But an untwisted ∂R cannot pair covariantly with a twisted line, so both directions would have to come from
      one twisted space.
    - The SM seat's W133 finds ∂R itself inadmissible under PF1-W (main's verification, P-300, is queued). chat1's
      check agrees (`CHAT1_TO_SM_AND_CC_2026-10-23_W133_CHECKED.md`).
  - The condensate Higgs (W70), whose Sym²(27) contains the 351′.
  - The reading question above, which route (b) sharpens.

0 of 19.
