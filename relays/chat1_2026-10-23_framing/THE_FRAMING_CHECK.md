# The framing check: in main's frame the six reach the precision bar with one Higgs direction only when the conjugate is in one sector, with a near-permutation CKM (post hoc, the day's four stored scans), and with two holomorphic directions chosen by the data (H_u = F_6, H_d = F_22; sealed) with the mixing aligned but too small; which structure fits the coarse pattern depends on the lines scanned; the mixing's size, D, the CKM phase and τ remain open; the scale and the Higgs's reading are framing choices the record has not fixed

chat1, 2026-10-23. **A READING over sealed results and labelled post hoc read-outs; every number from committed files
or the cited literature.** At the owner's "lets sit more with this, lets verify this, and lets see whether we're
misframing the program or things within it, leading us to wrong expectations … lets understand our program, and whether
the math so far frames it right", then "lets do it properly and informed". Read-outs in `relays/chat1_2026-10-23_framing/`, each script committed
before its run and its output before it was read: `framing_readouts.py` (026556089; output 5cedca1d8),
`framing_readouts2.py` (f4dc1d3f6; 5f2743567) and, after the referee's report, `framing_readouts3.py` (ee8fcf48a;
ba5eb6425). "The day's four stored scans" are the zero-free census, ZERO_FREE_HOLOMORPHIC, TICK_LINE_HIGGS and RIGID_TAU's
family A; TWO_HIGGS's grid is a fifth. TWO_HIGGS_RULE cites this note's §4a for the scale, which is now §4b. Refereed
read-only before it left. 0 of 19.

## 0. In brief

1. **What the program computes.** Main's fibre frame (B1720's instrument at 3412bf09d) turns discrete data — a flat
   hypercharge line (α, b), a Higgs direction v (a triplet of modular forms), a reading per sector (S = S(v), or
   S̃ = εS̄εᵀ = S(v̄); the code allows one direction per sector), a horocycle — and the modulus τ into the Yukawa matrices.
   The lepton factor c is put in by hand. Given those, every mass ratio and every mixing is fixed: a modular-flavour model
   with no free coefficient.
2. **What the day settled** (four sealed tests; their result notes are committed after referee).
   - TICK_LINE_HIGGS: on the tick's lines the zero-free holomorphic menu fits the nine's coarse pattern, specifically on
     those lines (2.04, with 0.11% of random targets as good).
   - ZERO_FREE_HOLOMORPHIC: on 23 940 new points over all 266 lines the menu fits (1.67, 2.19) but is not specific (3.4%,
     1.05%), and holomorphy's reading does not win both measures (Z7). Its best line is again the tick's, by 2–4%. Four
     lines containing that line or a runner-up look specific, so the specificity on the tick's lines says only that their
     set contains the menu's best line (post hoc).
   - RIGID_TAU_HOLOMORPHIC: by its sealed reading the apex rule places τ at the pattern level (A1–A4 hold). Post hoc, the
     six's coarse bar (2.0) is met at one apex configuration (with its mirror) and the nine's (2.5) at two, all
     CP-self-conjugate, and no row meets both; the values fail (A5, A6); the tick's own moduli miss (B1, B2).
   - **TWO_HIGGS:** with H_u = F_6 and H_d = F_22, two holomorphic directions from the menu chosen by the data out of six,
     the six fit within 10% at the best row (χ²_six 1.19 against 16.75, the first sealed χ²_six cell on record to hold).
     There d = e and c = 3 make the lepton ratios the down ratios times 3 and divided by 3, so four of the six are
     independent; at the fitted best row those four quark ratios are within 1σ of their measured values (post hoc), and
     random quark targets are fitted as well 0.15% of the time in the worst factor, 0.035% in χ² at the data's errors.
     χ²_six stays below the bar on 14 rows, all at Im τ 2.6 on L_2. The nine's bar fails (154), so by PRECISION_BAR this
     is a match of the six, not of the values. Both sectors' heaviest states are the same j–k mix, but
     the mixing is too small (0.19, 0.55 and 0.39 of measured at the best row; 1.6–16 times too small over the 14 rows),
     about as small as with either direction alone at that row (P2); D = 9 and J are too small; for the nine one
     direction for both stays better (2.01 against 2.32).
3. **Which structure fits the coarse pattern depends on the lines.** Over all lines main's ∂R read S̃ (chosen by hand,
   not holomorphic) fits the six and the nine better than the menu and is specific (0.78% and 0.29%). On the tick's lines
   and at the apexes the menu fits the nine better than ∂R in the readings read out (2.04 against 3.07; 2.26 against
   3.51). On its own best four lines, chosen after the fact, ∂R's fractions are 0.07% and 0.05%; the menu's, on the
   tick's four (which contain its best line), 0.28% and 0.14%. On TWO_HIGGS's α = 2/5 grid ∂R read S̃ has the best nine (1.94), against 2.01
   for the diagonal pairs and 2.32 for the off-diagonal ones.
4. **At the six's precision bar the reading and the directions decide** (post hoc, K1 and K4; TWO_HIGGS sealed).
   - With one Higgs direction, every row of the day's four scans that meets the six's bar has the conjugate in exactly one
     sector (main's split, up S̃, or the flipped reading, up S), and at each such reading's best row |V_cb| is about 24
     times the measured value: a near-permutation CKM. No reading with the same conjugation in every sector, of any
     direction, goes below χ²_six 22.4.
   - On ZERO_FREE_HOLOMORPHIC's grid the two one-conjugate readings read out are specific in χ² too (K4; chosen after
     their minima were seen): main's ∂R split (χ²_six 3.8: five ratios within 6%, m_u/m_t at 0.70) is matched by at most
     0.025% of random six-target sets, the menu flipped (6.1) by at most 0.075%.
   - With two holomorphic directions (TWO_HIGGS) the six's bar is met with the heaviest states aligned. By the rule's
     reading H7 fails: "the tension survives this extension", and no off-diagonal row fits the six and the mixing
     together. Post hoc, its form changes: the permutation is gone, and at those rows the mixing is too small.
5. **The sentence checked.** chat1's sentence in its conversation with the owner on 2026-10-23, quoted back by the owner
   (it is not in the repository): "So the missing ingredient is no longer a selection principle. What is left is three
   magnitudes: τ, a d–e splitting that breaks SU(5), and the size of the CP phase. GAP6 already says a flat frame cannot
   fix magnitudes like these."
   - The selection on record is partial, and items 3 and 4 qualify it: at the six's precision bar the reading and the
     Higgs directions decide (K1's best rows below the bar lie on six different lines, all in a one-conjugate reading), and
     the data prefer structures the principles did not single out.
   - In the frame as scanned (lines of finite order, c by hand) only τ is continuous. There D = c² where d = e (the
     order-5 lines; on the order-10 α = 2/5 lines, H_d = F_22), and elsewhere it is an output of the line, the direction
     and τ (∂R split: 10.79 at its best six-row on TWO_HIGGS's grid). So discrete data on record already produce a d–e
     splitting, at the cost of the mixing. J is an output. A flat line off finite order is continuous and could split d
     from e (relay §66, HARVEST_LEDGER row 1100).
   - GAP6 as main states it at 3412bf09d (GENESIS v1.54: "continuous moduli"; a rigid flat point fixes continuous numbers
     exactly) bounds what a flat frame can fix without a continuous input; it does not make D or J free numbers. This
     branch's v1.11 said "continuous values", and the quoted sentence followed that wording.
6. **The deficits, measured** (§3; post hoc where not a cell): the values (the six's bar met by TWO_HIGGS's pair, not the
   nine's); the mixing's size at those rows; D = 9 at TWO_HIGGS's six-fitting rows, against 10.58 ± 0.11 (∂R split comes
   near 10.58 only with the permuted CKM); the CKM phase, which the frame breaks readily but not where the nine fits (for
   F1's four models no row of the day's scans with nine ≤ 3 has |J| above 7.05 × 10⁻⁶, and asking for the right J costs
   the nine more than chance would, F1 and K3); and τ.
7. **Two framing choices the record has not fixed** (§4).
   - **The Higgs's reading** moves verdicts (post hoc, G1: χ²_six 3.8 against above 470 at the same rows). S̃ conjugates
     the Higgs's coefficients as H̃ = iσ₂H* does a doublet's. If the frame's 2 × 2 index is SU(2)_L (a reading, not fixed by the
     frame), one doublet needs the conjugate in exactly one sector, and holomorphy in every sector needs two doublets
     whose directions can differ. If the index is internal, one reading for all is consistent with one doublet
     (THE_SELECTION_MAP §5).
   - **The scale.** The targets are M_Z values. One-loop SM running to 2 × 10¹⁶ GeV moves six of the nine targets by a
     factor 1.13 either way (0.884, 1.131), more than PRECISION_BAR's 10% allowance. It changes no precision-bar verdict
     for the four models read out (F2); TWO_HIGGS's best row stays below the bar (5.8); K1's other one-conjugate readings
     were not run against the high-scale targets.
8. **Where a value can still move** (informed, §5). A flat hypercharge holonomy at the puncture is impossible: the
   puncture's loop is a commutator, so every flat U(1) connection is trivial around it. A hypercharge flux there is
   curvature; it is not built, and it would bring a continuous number unless a principle quantizes it. A flat line off
   finite order could split d from e (relay §66).
9. **Next** (§6): what sets the mixing's size in the two-doublet structure, and what principle assigns F_6 to H_u and F_22
   to H_d (with them comes a ratio of departures from the isotropic direction of 3.66, close to 22 : 6); D (c ≈ 3.25 by
   hand, a d–e-breaking direction on the order-10 lines, a flat line off finite order, or a quantized flux); J; τ; the
   scale fixed before any further values test.

## 1. What the program computes  [READING, from the code at 3412bf09d]

- **Inputs.**
  - A line (α, b), here always of finite order N; each field is twisted by q·w, with q = 6Y and w = ατ + b.
  - The Higgs direction v ∈ ℂ³: main's ∂R, or a zero-free F_a = η^{3−a}(eθ₂^a, eθ₄^a, iθ₃^a) with its sign e.
  - A reading per sector; the modulus τ; a horocycle (L_max or L_2, B1667's canonical cuts); and c, by hand.
- **The machine.** Twisted theta kernels on the flat torus with one puncture, read at the puncture.
  - Residues R_s and regularised norms c_s give the channel weights u_s = √(2πL + c_s)·R_s.
  - The Yukawa is Y_ab = Σ (C_aᵀ ε S C_b) ∘ M. The generations are the quaternion blocks C = (QJ, QI, QK) (B1644),
    S = Σ v_k Q_k, and ε = QJ.
- **The readings.** For the quaternion units εQ̄εᵀ = Q, so S̃ = εS̄εᵀ = S(v̄): it conjugates only the Higgs's
  coefficients (THE_SELECTION_MAP §5). Two directions for the two sectors are allowed by the code: the up Yukawa takes
  one S, the down and lepton Yukawas another.
- **Outputs.** Six mass ratios, three |V| and J at each τ. The frame reads 6Y only mod N. On the tick's order-5 lines
  6Y mod 5 is constant on the 10 and on the 5̄, so Y_e = Y_dᵀ and d = e (B1698's reading). At TWO_HIGGS's six-fitting
  rows D = 9.000: on the order-5 line (2/5, 4/5) for any direction, by that reading, and on the order-10 lines because
  H_d = F_22 (`two_higgs_posthoc2.json`, Q1); other directions break it there (`two_higgs_posthoc.json`, P2).
- **Discrete and continuous.** As scanned, the line, the Higgs's class, the readings, the horocycle and c are discrete
  and τ is continuous. Given all of them nothing is fitted.

## 2. The day's sealed results

| test | holds | fails | the reading after referees |
| --- | --- | --- | --- |
| TICK_LINE_HIGGS (rule e0c16e1cd; result 524072d81) | six 1.551 at 0.15%; nine 2.043 at 0.11%; S beats S̃; α = 2/5 | J (15 times too small); P-094 by construction | specific on the tick's lines, which contain the menu's best line; the values (post hoc), D and J fail |
| ZERO_FREE_HOLOMORPHIC (rule 38e2b8062; result dfc078a79) | six 1.668; nine 2.192; α = 2/5 | specificity (3.4%, 1.05%); Z7; D; J | fits, not specifically over all lines; the tick's line is the best by 2–4% (the written prediction held, by continuity with the census); ∂R read S̃ is better and specific |
| RIGID_TAU_HOLOMORPHIC (rule 51b05f7c7; result 5c4097fa7) | six 1.635 at 0.69%; nine 2.256 at 0.39%; S beats S̃ | χ² (A5, A6); J; D; the tick's own moduli | the apex rule places τ at the pattern level, at two different CP-self-conjugate configurations, no row meeting both bars; the six is a known fit that ∂R also reaches; the nine is narrow |
| TWO_HIGGS (rule 0b192e458; result 8040bebd2) | H1 (six 1.099 against 1.466); H3 (0 of 80 000); H4 (0.57%); H5 (χ²_six 1.19) | H2 (nine 2.32 against 2.01); H6 (χ²_nine 154); H7 (nine 5.35 at the best six-row); H8 (J) | the six at the precision bar with two holomorphic directions (four independent numbers with d = e and c = 3); not the values (H6); the heaviest states aligned but the mixing too small (H7 fails); D = 9, J small |

## 3. The deficits, measured  [SEALED where a cell; otherwise POST HOC, labelled]

**The values** (post hoc, `framing_readouts.json` F2; sealed only as RIGID_TAU's A5 and A6 and TWO_HIGGS's H5 and H6).
PRECISION_BAR's χ² (σ² = the data's relative error² + 0.1²), minimum over each scan's rows, c = 3, M_Z targets
(χ²_six / χ²_nine; bars 16.75 / 21.67):

| model | zero-free census | ZERO_FREE_HOLOMORPHIC | TICK_LINE_HIGGS | RIGID_TAU family A |
| --- | --- | --- | --- | --- |
| menu, S | 35.1 / 133 | 36.5 / 113 | 39.1 / 113 | 48.9 / 146 |
| menu, S̃ | 59.1 / 507 | 55.2 / 482 | 481 / 1 180 | 138 / 588 |
| ∂R, S̃ in every sector | 40.5 / 103 | 22.4 / 101 | 126 / 243 | 111 / 263 |
| ∂R, split (up S̃) | 11.1 / 1 380 | 3.8 / 1 320 | 21.0 / 1 460 | 42.3 / 1 470 |

On TWO_HIGGS's grid (its sealed comparison; cells H5 and H6 for the off-diagonal pairs): the off-diagonal pairs 1.19 /
154, the diagonal pairs 33.8 / 125, ∂R split 6.1 / 1 198, ∂R read S̃ 32.9 / 104. Below the six's bar among single
directions (K1) are only one-conjugate readings: ∂R split on two scans, F_22 flipped on three, F_6 flipped on two, F_22
split on one, and four other zero-free directions on the census, each with |V_cb| about 24 times measured at its best
row. TWO_HIGGS's F_6 | F_22 is below it with the mixing aligned.

**The mixing's size.** At TWO_HIGGS's rows below the six's bar, |V_us| is 0.06–0.24, |V_cb| 0.49–0.61 and |V_ub|
0.30–0.52 of measured (`two_higgs_posthoc.json`, P1). At the best row the two directions nearly coincide
(|⟨F_6|F_22⟩| = 0.99996, `two_higgs_posthoc2.json`, Q5), but that is not what keeps the mixing small: with either
direction alone the same row gives |V_us| 0.27 or 0.32 and |V_cb| 0.54 or 0.55 of measured (P2). Aligned readings give
small mixing here.

**d–e.** At TWO_HIGGS's rows below the six's bar D = c² = 9 (P1). P-094 needs 10.58 ± 0.11: 14σ at Antusch, Hinze and
Saad's precision, 1.3σ with the record's own inputs (HARVEST_LEDGER row 1100). On the order-10 lines d = e depends on
the down quarks' and leptons' direction: F_22 keeps it, while at the best row F_6, F_−2 and ∂R give 9.0015, 8.51 and
12.3 or 13.8 (`two_higgs_posthoc.json`, P2). Main's ∂R split, which meets the six's bar with one direction on these same
lines, gives 10.79 at its best six-row on TWO_HIGGS's grid, near P-094, but with the permuted CKM (THE_SELECTION_MAP §4:
D ≈ 11). Meeting the six within 10% still leaves D, a product of four of the six's ratios, free by up to a factor
1.1⁴ ≈ 1.46.

**The CKM phase** (post hoc, `framing_readouts.json` F1 and `framing_readouts3.json` K2–K3; the sealed J cells are
TICK_LINE_HIGGS's K6, Z6, A8 and H8, all failing):

| model | rows with \|J\| ≥ J_PDG/3 | largest \|J\| among rows with nine ≤ 3 | best nine among rows with \|J\| within a factor 3 of J_PDG |
| --- | --- | --- | --- |
| menu, S | 44–56% | 1.4–6.5 × 10⁻⁶ (212 rows) | 4.48 (census), 5.09 (fresh grid), 5.2 (apexes), 21.4 (tick grid) |
| menu, S̃ | 45–57% | no row | 4.04, 4.02, 7.64, 38.9 |
| ∂R, S̃ | 37–55% | 3.6–7.05 × 10⁻⁶ (32 rows) | 5.19, 4.51, 8.78, 28.1 |
| ∂R, split | 71–84% | no row | 22 or worse |

- The frame breaks CP readily, but not where the nine fits. For the menu read S and ∂R read S̃ on the two all-line scans,
  the best nine among the rows with the right |J| (4.5–5.2) is far worse than among random row subsets of the same size
  (median 2.2–2.7, 95th percentile at most 3.7; K3): the cost is not a subset-size effect.
- The cut matters: with nine ≤ 5 the menu read S̃ has rows with |J| far above the measured value (up to 1.8–3.1 × 10⁻⁴),
  and the menu read S and ∂R read S̃ reach 1.26–1.27 × 10⁻⁵.
- At the 843 CP-self-conjugate apex configurations |J| ≤ 2.4 × 10⁻¹⁰ for every direction and every reading (K2).
- So in the readings that fit the nine best (menu S, ∂R S̃) the phase is not a magnitude to be supplied on its own: it is
  a tension between where the pattern fits and where CP is broken. The bound of 7.05 × 10⁻⁶ is committed for F1's four
  models; TWO_HIGGS's rows have |J| ≤ 1.23 × 10⁻⁶ where the six fit.

**τ.** The record's rigid candidates place it at no single point for both the six and the nine, nor for the values
(RIGID_TAU_HOLOMORPHIC; B1696 and B1702 for ∂R). THE_SELECTION_MAP §3's sweep of the literature found no principle that
fixes both τ and the coefficients.

## 4. Two framing choices the record has not fixed

### 4a. The Higgs's reading  [READING, and POST HOC where labelled]

- **The form.** S̃ = εS̄εᵀ conjugates the Higgs's coefficients, as H̃ = iσ₂H* does a doublet's.
  - If the frame's 2 × 2 index is SU(2)_L (a reading; the frame does not fix it), one doublet needs the conjugate in
    exactly one of the two sectors. Main's split reading (up S̃, down and leptons S) has that structure, and so has the
    flipped one (up S, down and leptons S̃); since the twist sums fix which sector carries H (THE_SELECTION_MAP §5),
    the two need opposite identifications of S with H and cannot both be one doublet. Holomorphy in every sector (W135)
    then needs two doublets, H_u and H_d, as in supersymmetry, whose directions can differ. The record's 27 contains two (B1253: "the 10 emerging as two Higgs
    doublets + colour triplets", a consistency check on its weight blocks), in one multiplet.
  - If the index is internal to the theta components, one reading for all is consistent with one doublet
    (THE_SELECTION_MAP §5), and the two-doublet structure is a choice.
- **What the one-conjugate readings do** (post hoc; `framing_readouts2.json`, G1; `framing_readouts3.json`, K1 and K4).
  On the fresh grid main's ∂R split with c = 3 has seven rows below the six's bar, all at Im τ 3.05 on L_max, on
  (2/5, 1/10) and (2/5, 1/2) (the record had a six of 1.20 at Im τ 3.08 on (2/5, 1/10), THE_SELECTION_MAP §4). The best,
  at 0.3 + 3.05i on (2/5, 1/10): χ²_six 3.8, model over measured 0.99, 0.70, 1.05, 1.01, 0.99, 0.95; |V_us| 0.99,
  |V_cb| 1.00, |V_ub| 0.029 (absolute; 4.4, 24 and 7.7 times measured). Read with S̃ or with S in every sector, the same
  rows align the mixing but lose the masses (χ²_six above 470).
- **Why, at that row** (G2, one row recomputed in main's frame; THE_SELECTION_MAP §5's account made exact): the down
  sector read S has its heaviest left state on the i block (0.995); the up sector read S̃ has its heaviest on an equal
  j–k mix (0.495, 0.500) and its middle state on the i block (0.992); read S, the up sector's heaviest is on the i block
  (0.984), aligned, but m_u/m_t is 667 times too large.
- **What two holomorphic directions do** (TWO_HIGGS, sealed, with its post hoc read-outs). With H_u = F_6 and H_d = F_22,
  both sectors' heaviest states are the same j–k mix (about 0.498 on QJ and on QK in both; |V_tb| 0.9997), and the six
  fit within 10% at the best row: 1.010, 0.910, 0.983, 0.938, 0.938, 1.052. At the same row one direction for both fails
  (F_6 for both: m_d/m_b 0.33; F_22 for both: m_u/m_t 3.51): the up quarks want F_6, the down quarks and leptons F_22.
  The two directions are close to the isotropic v0 = (0, 1, i)/√2, with nearly parallel departures in the ratio 3.66,
  close to 22/6, which follows from a at leading order (Q5; ZERO_FREE_FRAME_EXPLORATION §1).

### 4b. The scale  [POST HOC estimate]

The nine targets are Huang and Zhou's M_Z masses and PDG's moduli; the frame says nothing about the scale at which its
couplings hold. If they are boundary values at a high scale, the targets must be run up. One loop in the SM, with
`rg_ratios.py`'s equations extended (`framing_readouts.json`, F2), from M_Z to 2 × 10¹⁶ GeV:
- m_c/m_t and m_u/m_t × 0.884; m_s/m_b and m_d/m_b × 1.131; the lepton ratios × 1.000; |V_cb| and |V_ub| × 1.131;
  |V_us| unchanged; J × 1.28. Six of the nine targets move by a factor 1.13 either way, more than the bar's 10%
  allowance.
- The size agrees with the literature's for the moduli: about +13% in the full SM from m_t to 10¹⁵ GeV (Balzereit,
  Hansmann, Mannel and Plümper, hep-ph/9810350).
- For the four models read out (F2) it raises every χ²_six minimum (36.5 → 53.5 for the menu on the fresh grid; 22.4 →
  36.9 for ∂R read S̃) and most χ²_nine minima, and changes no precision-bar verdict; TWO_HIGGS's best row stays below
  the bar (1.19 → 5.8), with m_c/m_t then at 4.8σ. K1's other one-conjugate readings were not run against these targets.
- In a supersymmetric theory the cross terms of the Yukawa equations change sign (+1 against the SM's −3/2), so the
  moduli and the down ratios run the other way, and tan β enters.

PRECISION_BAR was sealed at M_Z; that is a choice, and the record's only one so far. A values test should state its scale
and its theory.

## 5. Where a value can still move  [READING, informed]

| lever | status | why |
| --- | --- | --- |
| the horocycle | discrete; scanned | L_max or L_2 (B1667's canonical cuts), both in every scan |
| c | by hand | D = c² on the d = e lines; P-094 asks c ≈ 3.25 there |
| the regularised norms c_s | fixed by the frame | B1656's norms at the puncture with B1667's cut, already sector-dependent through the twists; a further sector-dependent change needs curvature (the flux below) |
| a flat line of finite order | discrete; scanned | d = e on the order-5 lines for every direction (B1698's reading); on the order-10 lines it depends on the direction |
| a flat line off finite order | possible; two continuous numbers | relay §66 (HARVEST_LEDGER row 1100): along hypercharge or B − L it could split d from e continuously; predictive only if a principle fixes it |
| a magnetic flux on the closed torus | a different frame, not a lever | it sets the number of zero modes; its normalisation is the same for every generation (Cremades, Ibáñez and Marchesano, hep-th/0404229) |
| a flat hypercharge holonomy at the puncture | impossible | the puncture's loop is a commutator, so every flat U(1) connection is trivial around it. In a group whose commutant of the SM is abelian (SU(5), SO(10), E₆), no flat connection commuting with the SM has a hypercharge holonomy there either |
| a hypercharge flux at the puncture, net flux zero | not built; one continuous number | the analogue of F-theory's hypercharge flux at a Yukawa point, which splits d from e through the wavefunctions (Font, Ibáñez, Marchesano and Regalado, arXiv:1211.6529); in main's frame it would act through the norms c_s, sector by sector (a reading); predictive only if a principle quantizes it |
| two holomorphic directions | discrete; tested | TWO_HIGGS: the six at the precision bar with H_u = F_6, H_d = F_22, not the nine; which principle assigns them is open |
| the scale | a framing choice | §4b |
| τ | open | §3 |

## 6. Next

1. **The mixing's size in the two-doublet structure.** At TWO_HIGGS's six-fitting rows the mixing is aligned and too
   small: |V_us| 4–16, |V_cb| 1.6–2.0 and |V_ub| 1.9–3.3 times below measured (P1), about as small as with either
   direction alone at the best row (P2). What in the frame could set it (the line, the horocycle, τ within the band,
   another principled direction), asked as a sealed test before any scan of it is read.
2. **What assigns F_6 to H_u and F_22 to H_d.** The data chose this pair out of six (with it comes a ratio of departures
   from the isotropic direction of 3.66, close to 22 : 6, Q5). A principle that fixes it (both have weight 3/2; they
   differ in a and in the twist r, 12 and 20) would remove the pair's selection from the six's match; τ is still chosen
   by the fit and c set by hand.
3. **D.** At TWO_HIGGS's six-fitting rows d = e and D = 9; P-094 asks 18% more. Levers on record and built: c (about
   3.25, by hand) and a d–e-breaking direction on the order-10 lines (∂R split gives 10.79, with the permuted CKM). Not
   built: a flat line off finite order (relay §66) and a quantized flux at the puncture.
4. **J and τ.** On the scans read out J is small wherever the nine fits (F1, K3), near the self-conjugate configurations
   or not, and zero at them (K2). A principle that fixes τ must give J ≈ 3 × 10⁻⁵ where the pattern fits, which no
   scanned row does.
5. **The scale**, fixed before any further values test.

0 of 19.
