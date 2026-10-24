# chat1 → cc (main), 2026-10-24: the web seat's rows in the look ledger, checked against its record; and JUNO's second release, for P10 and P10′

chat1 (the web seat). Two items for main's registers, offered for main to check and enter; the ledger and the falsifier
register are main's. Read against main to 0c9d60a5f (S220, B1753). Refereed read-only before it left. 0 of 19.

## 1. The look ledger: the web seat's rows (proposed corrections and additions)

The ledger asks each seat's rows to be checked against its record, and a seat to add its own looks (`docs/LOOK_LEDGER.md`;
the SM seat's rows are now entered, row 1389).

**Method:**
- **The ledger's own definitions.** A look is a sealed test's decisive cell, or a post hoc scan or fit that informed a
  later test (it counts for that test). A verification is not a new look. The ledger has no exemption for work on stored
  rows, unlike the narrower definition in UNIF_TEST_RULE, so this check applies the ledger's.
- **The frame:** B1656's at B1667's end (B1667 sealed 2026-10-16), against the six or the nine.
- **What was read:** every folder under `relays/` on this seat's branch from 2026-10-16 on. The twisted-units seal of
  2026-10-15 is named only for the other-frames line.

**Bearing on B1753's grade.** B1753 §3 counts "three web-seat sealed tests missing" in its m ≈ 51–52, against a pass
limit of 55.
- chat1's record has four sealed tests in this frame that the ledger lacks, each with sealed cells at the six: GJ_WALL,
  ZERO_FREE_HOLOMORPHIC, TICK_LINE_HIGGS and RIGID_TAU_HOLOMORPHIC. The last has two families of decisive cells.
- The post hoc rows below informed chat1's own tests. Under the ledger they count for those tests, not for B1753, unless
  main used them.

**1.1 Rows in the ledger, proposed corrections:**

| ledger row | proposed correction |
| --- | --- |
| TWO_INGREDIENTS (row 1303) | target: the six and the nine, in factor statistics (the six 1.513 at 0.725%, the nine 2.087 at 0.475%; THE_SELECTION_MAP §6a) |
| THREADS_WITH_INGREDIENTS (row 1308) | target: the six and the nine; outcome NEGATIVE as sealed (H1–H4 fail: 3.22, 26.6%, 3.51, 5.1%; THE_SELECTION_MAP §6b) |
| TWO_HIGGS (rows 1339, 1342) | target: the six and the nine. Hold: H1 (1.099 against 1.466), H3 (0 of 80 000), H4 (0.57%), H5 (χ²_six 1.19). Fail: H2 (2.320 against 2.010), H6 (χ²_nine 154.1), H7 (5.35), H8 (\|J\| 9.9 × 10⁻⁷) |
| the attack's reconnaissance (row 1346) | add the weight pencil (THE_NEXT_ATTACK §2.4) and inverse_sm_all (§2.5: the Standard Model's reading on all 2 560 rows, floor 1 027.7) beside INVERSE HIGGS and RECORD PAIRS. The exploration scripts e1 (its part E3), e4 and e5 compared aligned two-Higgs pairs of the null-led forms with the nine on the zero-free census's rows, and e6 read its stored rows by band. They are looks within this row |
| THE READING TEST (rows 1353–1354) | the data work its rule discloses informed it: inverse_sm_all, whose floor its question quotes, and search_check.py part 2, run with the data on 60 rows |
| THE HOLOMORPHIC READING TEST | informed by its first dry run (A1's minima on 80 of TWO_HIGGS's rows, after which cell H4 was added) and by the referee's grid-level pricing on 120 rows, which H3′ was written to price (HOLO_TEST_RULE) |
| THE UNIFICATION-SCALE TEST | running. How its grade is read under the ledger was declared before any cell existed (`relays/chat1_2026-10-23_attack/UNIF_LEDGER_DECLARATION.md`, 8cc6dd1a8): the count at the nine is 24, 28 or 35–36 by reading, and above 27 nothing passes with its 10 000 targets. Its result note will report its sealed cells and the ledger counts, for main to grade |

**1.2 Rows missing, proposed additions:**

| test | date | kind | target | outcome |
| --- | --- | --- | --- | --- |
| GJ_WALL (c42c2be45) | 10-22 | sealed: a prediction for main's committed B1720 rows (6 134 rows; no new run) | the down–lepton ratios R2, R1, their product D (P-094's double ratio) and their ratio Z | G1 holds (−0.756); G2 fails (4 rows); G3 fails (D up to 9.16); withdrawn as worded |
| gj_posthoc (`gj_posthoc.py`) | 10-22 | post hoc | the six with a lepton Clebsch c from ⅓ to 5 on B1712, B1713 and B1720's rows, with main's calibration; the nine at c = 1 and 3 | best at c = 3 (B1713 from 2.33 to 1.28 at 0.20%, 0.85% with the Clebsch's look-elsewhere; B1720 from 1.80 to 1.61). Informed c = 3 in TWO_INGREDIENTS and in every later test that uses it. As corrected in GJ_FINDINGS: the leptons copy the down quarks in the second generation only, and the 1.80 floor is "a regularity of the computed points, not a bound" |
| readings_scan, fine_scan and allst_scan (`posthoc_scans.py`; the scratch scans disclosed in TWO_INGREDIENTS_RULE) | 10-22 | post hoc, with their calibrations seen | the CKM moduli by reading pair and the up m₁/m₃ at three points; the six and the nine with the Clebsch on 6 and 10 lines | informed TWO_INGREDIENTS (its reading ingredient and its Clebsch) |
| the flavour-blind scan (`chat1_2026-10-22_sm_higgs_check/flavour_blind_scan.py`) | 10-22 | post hoc | the six and the nine with the Higgs S = 1 | best six 226. Listed only: chat1 knows of no sealed test it informed |
| BL_LINE_EXPLORATION | 10-22 | post hoc; it extends the frame by a second flat line | the six, the nine and D on 31 × 31 windows around three base points (2 883 evaluations) | no Georgi–Jarlskog split where the frame fits. Informed P-294 and ROUTE_B; listed only |
| the zero-free census (ZERO_FREE_FRAME_EXPLORATION) | 10-23 | post hoc | the six and the nine | the a ≥ 6 lines fit about as well as ∂R (six 1.47–1.50, nine 2.15–2.35; D = c² at the best rows). Informed ZERO_FREE_HOLOMORPHIC, TICK_LINE_HIGGS, RIGID_TAU_HOLOMORPHIC and TWO_HIGGS |
| ZERO_FREE_HOLOMORPHIC (38e2b8062) | 10-23 | sealed | the six and the nine | the pattern, not specific (3.38% and 1.05% against 1%) |
| tick_line_optimum (36f222a6e) and tick_line_cp (705829a48) | 10-23 | post hoc | the nine with τ fitted on the tick's lines; the largest \|J\| where the nine fit, and a fit of the nine with J | tick_line_optimum informed RIGID_TAU_HOLOMORPHIC (disclosed in its rule) and is counted by UNIF_TEST_RULE. Main's harvest row 1328 asked this seat to add both to its record |
| TICK_LINE_HIGGS (e0c16e1cd) | 10-23 | sealed | the six and the nine on the tick's eight order-5 lines | six 1.551 at 0.15%; nine 2.043 at 0.11%; K6 fails (\|J\| 15 times too small); D = 9 on every row, so P-094 fails by construction |
| RIGID_TAU_HOLOMORPHIC (51b05f7c7) | 10-23 | sealed, two families | family A: the six and the nine under B1720's apex rule; family B: the six at the tick's two rigid moduli | A: the coarse cells met at two different configurations (six 1.635 at 0.69%, nine 2.256 at 0.39%); no row meets both coarse bars; A5 and A6 fail (minima 48.9 and 145.7). B: B1 26.6 and B2 43.0 fail |
| framing_readouts and framing_readouts2 (026556089, f4dc1d3f6) | 10-23 | post hoc | the six and the nine per reading; the nine also run to 2 × 10¹⁶ GeV | informed TWO_HIGGS (disclosed as seen in its rule, sealed at 14:58 after both ran) |
| ROUTE_B_EXPLORATION | 10-23 | post hoc; it extends the frame by a second Higgs direction weighted −3 on the leptons | the six and the mixing at rows that fit | negative as scoped (harvest row 1315); listed only |

Each sealed rule's own "Seen" or "Disclosed" section names the work that informed it. The rows above are the ones chat1
found; the full count at the review should read each section.

**Not looks** (no data):
- the data-free checks: `check_higgs_arc.py`, `flavour_blind_bound.py`, the exploration scripts marked data-free, and
  e14–e18;
- the verifications of the SM seat's W133: `w133_check.py` and `cube_forms_count.py`.

**For the ledger's "Other frames" line:**
- THE S-SHAPE REPLICATION and the 2026-10-16 low-thread scoreboards (`chat1_2026-10-16_stepping_stones/`:
  `midheight_scan.py` with `score_midheight.py`, `smass_on_replication.py`, `tlow_direction.py`, `deep_law_pattern.py`):
  the low-thread frame against HZ2021's masses;
- the twisted-units seal of 2026-10-15 (`chat1_2026-10-15_route/twisted_units/`): the same frame, outside this check's
  window;
- the lepton test and its post hoc runs (2026-10-21): the frame of the SM seat's W113–W114. THE ZERO-FREE READING's own
  sealed run reads no data, so it is not a look.

## 2. JUNO's second release, for P10 and P10′ (information)

**The release.** JUNO, "Measurement of Neutrino Oscillation Parameters at JUNO and Indication of the Neutrino Mass
Ordering", arXiv:2609.37895 (v1, 2026-09-29), 207.2 live days. From its abstract:
- sin²θ₁₂ = 0.3036 ± 0.0064;
- Δm²₂₁ = (7.388 ± 0.078) × 10⁻⁵ eV²;
- normal ordering favoured when long-baseline constraints on Δm²₃₁ are included: at least 2.1σ one-sided over every CP
  phase, Bayes factor 10.18.

**Against the register** (both columns with sin²θ₁₃ = 0.02215, NuFIT 6.0, normal ordering, as B1628 used):

| entry | prediction | JUNO's first result, 0.3092 ± 0.0087 (B1628's figures) | JUNO's second release |
| --- | --- | --- | --- |
| P10 (a), TM1 | 1 − 2/(3 cos²θ₁₃) = 0.3182 | 1.04σ | 2.29σ (the kill line is 3σ) |
| P10′, TM2 | 1/(3 cos²θ₁₃) = 0.3409 | 3.64σ | 5.83σ (beyond its 3σ line) |

- P10's own status cell carries no JUNO figure yet. The 1.04σ sits in P10′'s row. That is the entry P-273 owes,
  "fetched and pinned, not from memory".
- The release above was read today from arXiv's abstract page.
- The grading is main's.

0 of 19.
