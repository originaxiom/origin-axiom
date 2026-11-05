# Review 74 — reader's report: five arcs read in full (B1821, B1822, B1823, B1824, B1828)

Read-only. No tracked file edited. Re-runs were done on scratch copies or in memory, single-threaded, at nice 10. Nothing
was compared with measured data. Paths are relative to the repository root unless absolute.

Working-tree note: `frontier/B1823_step_a_the_tied_heavy_vacuum/FINDINGS.md` carries an uncommitted dated note
(lines 367–373, "Review 74's protocol check, S299"), which is main's own work in progress. I read it but did not rely on it.

---

## B1821 — the frame's mirror symmetry in Re τ — HOLDS WITH NOTES

The symmetry reproduces (re-run below). The scope words reach beyond the sample, and one committed file is described
wrongly.

1. **E9: "every direction and line" goes beyond the sample.**
   - Written: "CONFIRMED ON EVERY DIRECTION AND LINE" (FINDINGS.md:1); "confirms it on the census's thirteen directions
     and all its lines" (FINDINGS.md:4); "New here: the confirmation on every direction and line of the census"
     (FINDINGS.md:50); "confirmed on every direction and line" (arc_verdict.json:25).
   - Found: the menu has 266 lines (verification/rigid_census_full_menu.py:39, `assert len(MENU) == 266`).
     - The 200-configuration multiset check draws lines with `rnd.choice(M.MENU)` (re_symmetry_check_200.py:35). It
       touches 146 distinct lines, counted from re_symmetry_check_200.json "rows".
     - The row-by-row relative check (sym_check_relative.py:111–113, seed 20261030, n = 24) touches 23 lines, all of
       orders 5–12. I reproduced the job list from the seed without evaluating anything.
     - Together the two checks touch 160 of 266 lines. No line of orders 1–4 had the relative-precision check, the
       only one that sees outputs below 1e-5 (FINDINGS.md:29). The order-4 lines are where the census's degeneracies
       sit (P-542, P-521).
   - Proposed: "confirmed on all thirteen directions: row by row to 5.8e-07 in log10 at 24 random configurations (23
     lines, orders 5–12), and as five-decimal multisets at 200 random configurations (146 of the 266 lines, orders 1–12)".

2. **The earlier check file is described wrongly, and its two partial matches are not disclosed.**
   - Written: "The earlier 22 are in `re_symmetry_check.json`." (FINDINGS.md:28–29).
   - Found:
     - The file holds 20 configurations, not 22.
     - Two of them matched only 22 of 26 groups: `[4, "1/4", "1/2", 0.233, 3.274, 22, 26]` at
       re_symmetry_check.json:137–145, and `[4, "1/2", "1/4", 0.113, 2.171, 22, 26]` at :164–172.
     - No committed script writes this file. re_symmetry_check_200.py writes only the `_200` file.
     - I re-ran those two configurations with the committed `re_symmetry_check_200.check` and both gave 26/26. So the
       file came from an earlier, uncommitted version of the check, probably one without the "mixing excepted where
       undefined" rule.
   - Proposed: "An earlier exploratory check (20 configurations, re_symmetry_check.json, from an uncommitted earlier
     version of the script) matched all 26 groups at 18 configurations and 22 of 26 at the order-4 lines (1/4, 1/2) and
     (1/2, 1/4); the committed script gives 26 of 26 at both."

3. **E11 (minor): "checked against B1810's committed table to 2.6 × 10⁻⁶" has no committed output.**
   - Written: FINDINGS.md:16. The same figure is repeated at rigid_census.py:4 and docs/THE_FINAL_ATTACK_2026-10-29.md:48.
   - Found: the evaluator has a committed function that computes the comparison, `control()` at
     verification/cm_zero_line.py:84–96. It is asserted only to `worst < 1e-4` (:110), and its printed value is not
     committed anywhere. I did not run it, to keep to one re-run per arc. It is cheap: one τ, 208 rows.
   - Proposed: commit the control's one-line output, or quote the bound the code asserts (< 1e-4).

4. **Scope note: the radius's mirror invariance is built into the evaluator, not tested.**
   - Found: the radii come from B1667's Re τ = 1/4 column, interpolated in Im τ only (cm_zero_line.py:4, :29, :49–51).
     So L(−x + iy) = L(x + iy) by construction.
   - B1667's own table does vary with Re τ. At Im τ = 1.0, L_max is 0.68839 at Re 0 and 0.68502 at Re 0.45
     (frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json). That is consistent with a true mirror
     symmetry, but it is not a test of one.
   - FRAMING_LEDGER FL-11 (docs/FRAMING_LEDGER.md:40) lists "the radii read off B1667's Re τ = 1/4 column" as UNSTATED.
     B1821 does not mention it.
   - Proposed, in § 3 Scope: "the radius is Re τ-independent in the evaluator (B1667's Re τ = 1/4 column), so its share of
     the symmetry is assumed, not checked (FL-11)".

5. **"A lock asserts it" (the strip guard) is satisfied in a later arc, not here.**
   - Written: "The census stays inside the strip, and a lock asserts it." (FINDINGS.md:38).
   - Found: no assertion on Re τ in B1821's evaluator or in tests/test_b1821_the_frames_mirror_symmetry_in_re_tau.py. The
     guard exists in B1825's census: frontier/B1825_step_b_the_nine_from_one_address/verification/census/rigid_census_refined.py:24
     and :56 (`assert abs(re) < 1`).
   - Proposed: "(B1825's rigid_census_refined.py asserts it)".

6. **Status (minor).**
   - Written: "Verdict: PROVED" (FINDINGS.md:3), next to "A proof sketch is owed" (:5) and "A numerical identity ... not yet
     a written proof" (:43; arc_verdict.json:23).
   - The verdict enum has no numerical grade (tests/test_arc_verdict_schema.py:28), so PROVED is the only positive token
     available. The hypotheses field is honest.
   - Proposed: "PROVED (numerically, to the stated precision; written proof owed)" in the claim line.

7. **Identifications (P-516 class).**
   - The arc reads the frame's J output as the CP-violating J ("J's sign is never predicted ... a world and its mirror
     cost the same", FINDINGS.md:35–36; arc_verdict.json:25). It also scores mass-ratio and |V| outputs.
   - That is I-33's read-out (docs/IDENTIFICATION_LEDGER.md:50), but `identifications: []` (arc_verdict.json:6).
   - Proposed: `"identifications": ["I-33 (UNEARNED): the read-out's J, mass ratios and |V|"]`.

8. **Re-run:** `re_symmetry_check_200.check` on the first three committed rows, value for value: `[8,'3/8','7/8',0.23,1.155,26,26]`,
   `[9,'1/9','0',0.446,1.528,26,26]`, `[12,'1/12','5/12',0.135,3.821,26,26]`. All three are identical to
   re_symmetry_check_200.json. The two order-4 rows of item 2, run with the same function, gave 26/26.

9. Data contact: none. Later corrections: none in docs/RETRACTIONS.md or docs/LAW_MAP.md. B1825 (FINDINGS.md:20) reuses the
   evaluator with no correction.

---

## B1822 — T-NORM on the frame's matter — HOLDS WITH NOTES

Every number traces to a committed output, and the re-run is exact. The notes are wording.

1. **A counting inconsistency in the headline and the claim line.**
   - Written: "8 REAL PARAMETERS PER FIELD (2 UNDER THE DIAGONAL SU(2) THE FRAME'S HOLONOMY LIES IN)" (FINDINGS.md:1). The
     claim line says the same (arc_verdict.json:26).
   - Found:
     - The 8 is after removing the overall scale (9 − 1; FINDINGS.md:58).
     - The 2 is the real dimension of H itself, scale included. The table header is "real dimension of H" (FINDINGS.md:48),
       and the source is referee/independent.json "algebra": "(iv) diagonal SU(2): real dim": 2.
     - Its two basis forms span I and the democratic J − I, so after the scale one parameter is left.
   - Proposed: "8 real parameters per field after the overall scale (1 under the diagonal SU(2) ...)", or "a 9-dimensional
     H (2-dimensional under the diagonal SU(2))".

2. **E9-lite: "every stored number" covers six of the 306 twist classes.**
   - Written: "The referee reproduced every stored number from a copy" (FINDINGS.md:30). The § 6 table says "every stored
     number from a copy (difference 0.0)" (:106).
   - Found: the referee's rerun covers the six classes in referee/rerun_arc.py:14–15, recorded in referee/rerun_arc.json.
   - Proposed: "every stored number of six twist classes (of 306)".

3. **Minor: the positive control's bound covers off-diagonals only.**
   - Written: "magnetised-torus modes orthonormal on three cells (≤ 1.3 × 10⁻¹⁵)" (FINDINGS.md:36).
   - Found: in tnorm_results.json "C+-_magnetised", the off-diagonals reach at most 1.28e-15. The normalisation,
     max |G_jj/exact − 1|, reaches 1.02e-14 (N = 5, τ = 0.5 + 2.5i, the lattice-corner cell).
   - Proposed: "off-diagonals ≤ 1.3 × 10⁻¹⁵, normalisation to 1 × 10⁻¹⁴".

4. **Numbers traced.**
   - From verification/tnorm_results.json (and tnorm_run.txt:4): 1 170 configurations, 306 classes, 9 values of τ, 26
     lines, five fields; the cover's off-diagonal maximum 2.03e-12.
   - From refine_results.json: ≤ 9.8e-16 at n = 48.
   - From referee/census_basis.json: 1.55e-14; the output moves 0.0074 decades and |V| 4.4e-4 (one-mode weight), 0.0448
     decades and |V| 0.080 (the democratic 0.1); the scale 3.7·I moves them 5e-16.
   - From referee/independent.json "algebra": the typing table 9, 3, 3, 2, 1, 3/1.
   - From referee/REPORT.json: 7e-13, 0.99985, 7.4e-5 / 0.99993, 4.4e-16.
   - The 0.287348 and sin 0.3 controls are in tnorm_results.json.
   - Only the topic-sweep count ("10 of 1568 arcs", FINDINGS.md:118) has no committed output. It is process, not result.

5. **Identifications (P-516 class).**
   - The arc reads the read-out's singular values and U as "mass ratios" and "CKM moduli" (FINDINGS.md:62–63;
     arc_verdict.json:26). That is I-33. B1822 did land the dated note on I-33 (docs/IDENTIFICATION_LEDGER.md:50).
   - The verdict's `identifications: []` (arc_verdict.json:6) does not name it.
   - Proposed: `["I-33 (UNEARNED; scoped here: H = I CHOSEN)"]`.

6. **The promised dated notes all landed:**
   - B1645's claim line (frontier/B1645_the_half_bound/arc_verdict.json, "scoped 2026-10-30 by B1822");
   - B1643's FINDINGS (FINDINGS.md:74–77, :96);
   - B1654's FINDINGS (FINDINGS.md:110);
   - the P-109, P-112, P-146, P-510 and P-531 rows;
   - the relay docs/handoffs/CC_TO_ALL_SEATS_2026-10-30_T_NORM_IS_A_CHOSEN_INPUT.md;
   - FL-11 (docs/FRAMING_LEDGER.md:40).

7. **Law harvest (WORKING_RULES § 10).** G = H·‖F_x‖² is a theorem-grade structural fact for every τ and line
   (FINDINGS.md:42–44), with `creates_law: false` and no LAW_MAP row (grep for B1822 in docs/LAW_MAP.md is empty). This is
   a candidate for the law harvest, not a defect.

8. **Re-run:** `tnorm.gram_job` from the committed tnorm.py, in memory, on four classes: `Q|zero|1j`,
   `u|ord7 2/7,3/7|(0.85+3.45j)`, `Q|ord4 0,1/4|(0.3+6j)` and `L|ord12 5/12,1/12|(0.3+6j)`.
   - Max |stored − rerun| over every cover and cell block's off-diagonal, norm and entries is 0 (exact).
   - The worst class, `Q|ord4 0,1/4|(0.3+6j)`, gives 2.0306436e-12 again. About 12 s of CPU.

9. Data contact: none. census_basis.json's "base outputs" are frame outputs. Later corrections: none. B1825 adds H = I to
   its scope from B1822 (B1825 FINDINGS.md:114).

---

## B1823 — Step A v2, the tied heavy vacuum — HOLDS WITH NOTES

The NEGATIVE and its sealed tallies reproduce byte for byte. One supporting sentence is factually wrong, and the
referee's confirmation repeats it.

1. **"Every computed n = 3 and n = 4 vacuum lies on a line" is false for the committed grid.**
   - Written: "for n ≥ 3 it is 3 on a mirror line ... and 6 off one (computed at n = 5, 6, 8; every computed n = 3 and
     n = 4 vacuum lies on a line)" (FINDINGS.md:47–48). The referee's CONFIRM.json repeats it in two places
     (verification/referee/confirm/CONFIRM.json, "1_findings_applied".B2(a) and "4_overclaimed_in_the_other_direction"[0]).
   - Found: in the sup/N primary grid, four converged, isolated, non-runaway vacua have `mirror_fixed: None`, both in the
     draft's verification/step_a_v2.json and in main's main/rerun_stableF/step_a_v2.json:
     - Z, n = 3, (μ², λv) = (0.5, 1.0): τ* = 0.25476 + 1.13645i (summary.txt:115);
     - Z, n = 3, (0.8, 1.0): τ* = 0.28398 + 1.19757i (summary.txt:119);
     - Z, n = 4, (0.5, 1.0): τ* = 0.21673 + 1.12685i (summary.txt:125);
     - Z, n = 4, (0.8, 1.0): τ* = 0.18679 + 1.27284i (summary.txt:129).
     - Each has gradient ≈ 1e-24 and plan class iso. A fifth, Z, n = 3, (0.3, 1.0), is the runaway (summary.txt:112).
   - The two n = 4 points are passing primary points.
   - The statement holds only for the vacua whose convention-free rank was computed:
     - the decoupling point, all on line (referee/t_dec_jacobian_run.txt, the n = 3 and n = 4 rows);
     - the referee's 35 finite-λv vacua, whose n = 3 and n = 4 rows are all at Re τ = −1/2 (referee/t_norm_jacobian.json).
   - The convention-free rank of the four off-line n = 3 and n = 4 vacua was never computed.
   - The NEGATIVE does not move. Rank 3 on a line already exceeds τ's 2, and off-line rank 6 is expected, but it is not
     computed at n = 3 and 4.
   - Proposed: "every n = 3 and n = 4 vacuum whose rank was computed lies on a line. Four converged off-line n = 3, 4
     vacua of the grid (menu Z, λv = 1.0) were not rank-computed with the convention free."

2. **"In every convention" (the robust piece) needs its condition.**
   - Written: "At n = 2 the direction is the cross product Y₃,₁ × Y₃,₂ at τ* ... in every convention" (FINDINGS.md:62–63).
     The claim line says "two copies' direction is the formula Y1 x Y2 at tau* in every convention" (arc_verdict.json:26).
   - The arc also says that in the cusp and Petersson-type conventions "the leading-order direction is then Q's simple
     lowest eigenvalue, an indefinite Q, not Y₁ × Y₂" (FINDINGS.md:50–52). The formula's own condition is that both copies
     are heavy, cᵢ > 0 (FINDINGS.md:108).
   - Proposed: "wherever both copies are heavy (c₁, c₂ > 0), the direction is Y₁ × Y₂ at τ* whatever the convention; the
     cusp and Petersson-type conventions lose that regime at the decoupling point."

3. **E11 (minor): the weak leg's medians are printed by no committed script.**
   - Written: "The third singular value ... a median 4 × 10⁻⁴ to 10⁻³ of the first. The second is a median 0.04 ... at
     λv = 0.1, and 0.16 at λv = 0.3 and 1.0" (FINDINGS.md:34–36). They appear only as prose in CONFIRM.json "3_verdict_label".
   - I recomputed them from the committed `free_numbers.svals` in step_a_v2.json, restricted to the 89 rank-3 points
     among the 90 sup/N n ≥ 4 primary points:
     - s3/s1 medians 3.65e-4 (λv 0.1), 1.08e-3 (0.3), 6.8e-4 (1.0);
     - s2/s1 medians 0.041, 0.157, 0.162.
   - The rank tally, 89 of 90 at rank 3 and one at rank 2 (H, n = 4, μ² 0.8, λv 0.3), is confirmed, and is identical in
     the rerun file. The numbers are right; only the printing script is missing.

4. **The discarded arbiter values remain, unmarked, in the committed rerun file.**
   - FINDINGS.md:316–318 says the arbiter's first version "omits the sup constants and DR's scale. Its values were
     discarded".
   - main/rerun_stableF/step_a_v2.json still carries that version's `arbiter` fields:
     - in 155 configurations, `interior_mp` differs from `interior_numpy` (for example H, N, n = 1, μ² 0.3: 0.409 against
       −0.0054);
     - 21 of the 95 sup/N n ≥ 4 configurations read `cusp_lower_mp: true`.
   - The tallies do not use them. compare_D.py reads `runaway`, and the 5 runaway flags agree with main/rerun_arbiter/.
   - The "95 of 100 ... closest 0.017" (FINDINGS.md:144–145) is right from the numpy subfields: 95 dicts, all above, the
     closest 0.01653 at (H, 5, 0.3, 0.1). But no committed script prints it.
   - Proposed: a dated note naming `rerun_stableF/step_a_v2.json`'s `arbiter.*_mp` and `cusp_lower_mp` as superseded by
     `rerun_arbiter/`.

5. **Wording (minor): "deep in the cusp".**
   - The table says H, n = 1 and 2 in the cusp convention are "unconverged deep in the cusp" (FINDINGS.md:128–129).
   - The rerun puts them at Im τ 4.1168 and 4.1166 (compare_D.json "changed"). § 4 itself says "at Im τ 4.12"
     (FINDINGS.md:199), and the rerun searched the cusp up to Im τ 16.
   - Proposed: "unconverged at Im τ 4.12".

6. **"Only in a CHOSEN normalisation convention"** (FINDINGS.md:1; arc_verdict.json:26) is literally true, since every
   convention is CHOSEN, but it should not be read as "fails in the others".
   - The cusp convention was run at a single point (μ² 0.5, λv 0.3), not on the primary grid.
   - There n = 6–8 came out isolated or weakly isolated and were not undercut (FINDINGS.md:133–135, :209). No wording
     change is needed if the reader keeps that in mind.

7. **Identifications (P-516 class).**
   - The arc names UNEARNED identifications in its own text:
     - "Using this vacuum for the frame needs H_u ≡ H_d, an UNEARNED identification" (FINDINGS.md:58–59, :233–234);
     - "Reading the minimised vev as the frame's Higgs, and the singular values as masses, is UNEARNED" (:244–245);
     - "a massless first generation" from m₁ ≡ 0 (:63–64, :257–258).
   - The verdict has `identifications: []` (arc_verdict.json:6). The ledger has no H_u ≡ H_d row: grep for "H_u" in
     docs/IDENTIFICATION_LEDGER.md is empty, and it is registered only as P-536 (docs/POINT_REGISTER.md:684).
   - This is exactly P-516's ask, "an identification a frame card labels UNEARNED appears in the verdict".
   - Proposed: `["I-33 (UNEARNED)", "H_u ≡ H_d (UNEARNED; P-536; no ledger row yet)"]`, and a ledger row.

8. **Numbers traced** (spot checks beyond the referee's "every number checked", CONFIRM.json "2_numbers"):
   - the § 3 table and the seven changed configurations (compare_D.json; the re-run below);
   - 11 of 176, nine in the cusp convention, recounted by me from summary.txt;
   - 4.77/1.55, 4.76/0.53 and 5.39/0.87 (main/cusp_undercuts_main.json);
   - −0.0043525 and −0.0057286 at Im τ 10.54 (main/rerun_arbiter/arbiter_run.txt);
   - 0.66 then 8.7e-17, the six values 2.88 ... 0.0233, and −4.6e-41 (main/conv_jacobian_main.json);
   - 0.26–3.41 (referee/t_controls_S_action.json);
   - 640 Hessians, 0 without a negative direction (referee/t_sympoints_run.txt:1);
   - 56/56 (L Lbar and H L Ebar at n = 8; E Ebar is 53/56, so "about 3n(n − 1)" holds; referee/t_cross_terms.json);
   - the c_min values and Q's eigenvalues (referee/confirm/c_checks.json);
   - the Menu H n = 2 vacuum on F₂ = 2η⁴R to ≤ 2.2e-16 (analysis_vacua.json; B1730 FINDINGS.md:56);
   - the PLAN quote (verification/PLAN.md:72–73);
   - the anomaly arithmetic (−3/4, −3/4, −3) checked by hand.

9. **Re-run:** main/compare_D.py, on a scratch copy with only the read root and the write target changed. The output is
   byte-identical to the committed main/compare_D.json, and the printed table matches FINDINGS.md:126–140.

10. Data contact: none. "The Standard Model's 12" doublets (FINDINGS.md:228) is a structural count, not a measured value.
    Later corrections: none in RETRACTIONS or LAW_MAP. B1830 closes P-495 on B1823 and B1825.

---

## B1824 — two declared directions are one (a₀ = η⁴F₋₂/6) — HOLDS WITH NOTES

The identity is right, and the re-run is byte-identical. The notes concern support that sits outside the arc.

1. **E11 (minor): "Confirmed by main componentwise at three values of τ" has no committed output.**
   - Written: FINDINGS.md:7.
   - Found: the committed componentwise checks are at six values of τ (the draft's, frontier/B1823_step_a_the_tied_heavy_vacuum/verification/checks_extra.json
     "a0_equals_eta4_Fm2_over_6", max 1.5e-29; checks_extra.py:92–93) and at four (main's, a0_identity_main.json "part2").
     I found none at three.
   - Proposed: "confirmed componentwise at six values of τ (B1823's checks_extra.json § 5) and four (main's
     a0_identity_main.json)".

2. **"Twelve distinct" asserts more than the arc computes.**
   - Written: "THE DECLARED MENU HAS TWELVE DISTINCT DIRECTIONS" (FINDINGS.md:1); "B1810's thirteen declared directions are
     twelve distinct ones" (:89); the same in arc_verdict.json:26.
   - Found: the arc proves one coincidence, so 13 become at most 12. No committed B1824 script checks that the remaining
     twelve are pairwise distinct.
   - My read-only check on B1810's committed table
     (frontier/B1810_the_symmetry_selection_value_table/verification/symmetry_selection_table.json) supports the claim.
     Over all 78 pairs of directions, the only coincidence is a₀/F₋₂ (1.6e-16). The next closest pair, F₂₂/F₂₆, differs by
     0.048 in some mass ratio.
   - Proposed: add "the other twelve differ pairwise on B1810's table (closest F₂₂/F₂₆, 0.048)" with a committed one-liner,
     or say "at most twelve".

3. **The pending census confirmation was done in B1825, with no back-pointer here.**
   - Written: "its a₀ and F₋₂ rows must agree. That is checked at the census's certification ... before the seal"
     (FINDINGS.md:100–102); "On the census's own rows it is to be confirmed" (:109–110); "to be confirmed equal before the
     seal" (arc_verdict.json:26).
   - Found: frontier/B1825_step_b_the_nine_from_one_address/verification/preseal/certification.json reads
     "a0_vs_F_minus2_max_log10": 0.0. preseal/a0_fm2_diagnostic.json, over 42 166 592 pairs, shows:
     - 2 184 pairs above the floor differing by up to 3.34e-5 in log10;
     - pairs below the floor (1e-12) differing by up to 62 decades;
     - 10 220 pairs with one exact zero.
   - B1824 carries no dated note recording this. The certification's 0.0 against the diagnostic's 3.3e-5 is B1825's to
     reconcile; I note it only as a cross-reference.
   - Proposed: a dated note in B1824 § 4 pointing to the two preseal files, with the residual stated.

4. **Numbers traced.**
   - From a0_identity_main.json: ≤ 2.2e-40 (max 2.18e-40); log-derivatives ≤ 2.9e-42; Jacobi 2.3e-41; E₄ 1.28e-41.
   - From b1810_a0_vs_Fm2.json: 64, 1.56e-16, 32, 9.9e-16, 7.5e-33 and 0.0215.
   - From referee/t_a0_run.txt: ≤ 9.3e-31 at five values of τ; q²⁵ (x^200) exact.
   - Checked by hand: the algebra (both the componentwise form and the 1/6, from θ₂ ~ 2q^{1/8}); N(a₀) = (η⁴/6)³·(i/4)η⁹
     = iη²¹/864; log₂(13/12) = 0.1155.
   - The prior-record quotes are verbatim: B1809 FINDINGS.md:97 "equal to F₋₂ at i"; B1810 FINDINGS.md:56 "a₀ has
     κ = 2^{−1/2} (= F₋₂)"; B1697 FINDINGS.md:15 "unidentified 'zero at t = −1/48'".

5. **Identifications:** essentially none. This is an identity of forms. The "Higgs direction" and "mass ratio" labels are
   inherited from B1810's frame (I-33). `identifications: []` is defensible here. A pointer to I-33 would cost nothing.

6. **Law harvest:** a₀ = η⁴F₋₂/6 is an exact identity with reach "general" (arc_verdict.json:23). It has
   `creates_law: false` and no LAW_MAP row, so it is a candidate under WORKING_RULES § 10.

7. **Re-run:** a0_identity_main.py on a scratch copy, 4 s. The run log is identical to a0_identity_main_run.txt and the
   JSON is byte-identical to a0_identity_main.json.

8. Data contact: none. Later corrections: none in RETRACTIONS or LAW_MAP.

---

## B1828 — GENESIS v1.60, the earned dictionary — HOLDS

1. **GENESIS.md carries the adopted text verbatim.**
   - I built v1.60 from `adoption/amend.py`'s `build()` (in memory, nothing written). The received v1.59's sha256
     a56f4b09… matches the pin at amend.py:13.
   - Three of the four CHANGES appear verbatim in the current root GENESIS.md: the GAP1 rule at GENESIS.md:316–334, the
     FK11 cell at :443 and the log entry at :708.
   - The whole diff between the v1.60 build and the current file is B1829's v1.61 edits: the version line at :3, the
     FK9 cell at :441 and the v1.61 log line at :707.

2. **The companions were changed in the landing commit 38d5ceafe:**
   - docs/IDENTIFICATION_LEDGER.md:14, the EARNED BY PREDICTION status;
   - docs/KIND_TABLE.md:127, the dated note;
   - docs/POINT_REGISTER.md:728, P-580 DONE → B1828;
   - P-577 (:725), later closed by B1829;
   - docs/FRAMING_LEDGER.md:112 and :178 (FL-20), which FINDINGS § 3 does not list.
   - "No identification changes status": the ledger has a single "EARNED BY PREDICTION" occurrence, the status legend
     at line 14.

3. **Minor: "the rule uses it unchanged" is not quite literal.**
   - Written: FINDINGS.md:44–45.
   - Found: two small departures from THE_FINAL_ACTS_BAR's V cell.
     - The v1.60 rule lets a target be "added to [the held-out list] before any look" (GENESIS.md:321), where the bar
       says "The held-out list, fixed now" (docs/THE_FINAL_ACTS_BAR_2026-10-29.md:437).
     - Its gloss of the matched null, "F's pipeline re-run over its whole CHOSEN menu" (GENESIS.md:324), drops the bar's
       fallback "Where the pipeline has no menu, it is a reference law fixed on the card" (bar:465).
   - The PASSED definition itself matches (bar:468).
   - Proposed: "uses it, with one extension (targets may be added before any look)".

4. **No lock.**
   - Every GENESIS amendment from v1.49 to v1.59 has a tests/test_bNNNN_genesis_v1_NN.py lock, for example
     tests/test_b1797_genesis_v1_59.py. None exists for B1828, nor for B1829.
   - `amend.py --check` (amend.py:64–66) returns 0 whenever the root is not at v1.60. Now that the root is v1.61, it can
     no longer detect drift in the v1.60 text.
   - Proposed: a lock in B1797's pattern that asserts the RULE text is present in GENESIS.md.

5. Re-run: none needed beyond the in-memory `build()` comparison (item 1). Identifications: none, correctly empty. Data
   contact: none ("nothing is computed", FINDINGS.md:52). Later: B1829 (v1.61) builds on the v1.60 rule
   (B1829 FINDINGS.md:24) without correcting it.

---

## What I could NOT check

- **B1821:** the 24-configuration relative check itself (sym_check_relative.py) was not re-run, being about 26 evaluations
  per configuration. Nor was cm_zero_line.py's `control()` (the 2.6e-6 figure), to keep to one re-run per arc. Whether
  B1667's true radius satisfies L(−τ̄) = L(τ) was not checked: its table has no Re τ < 0 points.
- **B1822:** whether the three one-dimensional typings are derived anywhere on the record ("none of them is derived on the
  record", FINDINGS.md:59–60). That is a negative search I did not repeat.
- **B1823:**
  - the hash table, which main has checked;
  - the referee's numbers I did not touch myself: 17 vacua with FS ≤ 1e-16, 146 vacua and 7.7e-4, the 35 Jacobians,
    0.008 and 2.8, and the sup norms beyond η²⁴;
  - whether the four off-line n = 3, 4 vacua have rank 6;
  - the extra doublets' mass estimate (FINDINGS.md:248–249), which no output computes; it reads as an estimate.
- **B1824:** whether the "not stated anywhere on the seats' branches" sweep (FINDINGS.md:121–123) holds. I did not read the
  seat branches.
- **All arcs:** the topic-sweep counts ("N of 1568 arcs"), which have no committed output by design.
