# Independent audit of agy's first two relays (2026-11-02): FULL_AUDIT and ELEVATION_PLAN

What I audited: main @ 64a2a3d4e and the agy snapshot dfe4c6f90. All scripts and outputs are in this directory. I wrote my own code throughout. Main's primitives (b1656_funcs, cm_zero_line) are used as the reference for what the programme computes. None of agy's code is imported, except the run of agy's own pytest in (f).

## (a) B1825 read-out — CONFIRMED
- run.json says what agy reports: in_support false, undecided 0; least_chi2_ten 291.40969 at key ((3/8,3/8), d=0, r=1, k=6); fresh value 291.48666; nine-observable read-out 82.6048; C_ten −197.0366 = C_six (−3.0798) + bits_CKM (−193.9567), and that sum is exact; choice 30900; CKM clause false, min_chi2_six 1.358, best_chi2_4 = inf.
- Decoding the key with cm_zero_line.DIRS[0], ("L_max","L_2")[1] and census_io.reading_index 6 gives **DR, L_2, S~S~S**.
- Per the card this is a FAIL. S is false, so the pre-written reading is "NO SUPPORT" (NOT FOUND within the reach; it is not EXCLUDED). K also fails (−197 < 12.37 gate_bits). X2 had already failed before the seal.
- I recomputed the decomposition fresh with main's evaluator (cm_zero_line.rows_at) and main's data files. I get χ² = 291.48666, matching the fresh value in run.json. Per-observable z: c/t +2.04, u/t +5.81, s/b +2.87, d/b −1.80, μ/τ +3.72, e/τ −0.67 (six total 63.65), V_us −1.04, V_cb +4.07, **V_ub +12.60 (χ² 158.8), |J| −7.17 (χ² 51.4)**. Every number agy gives matches (`a_b1825_point.py`).
- Caveats:
  - agy says the nine-observable minimum sits at "(3/8,3/8), a0, L_2, S~S~S". run.json records no address for that read-out, so this claim cannot be checked from run.json.
  - agy reads best_chi2_4 = inf as "0 rows have finite ten-vectors". That is a misreading. In kten.ckm_clause, inf is the initial value when no six-window row passes the χ²_4 < 13.28 enclosure prefilter.

## (b) Theorem 1 (closed form of c_s) — closed form CONFIRMED but NOT NEW; corollaries PARTLY
- **Closed form.** I implemented the formula from the relay text (Case 1 and Case 2) myself. Against main's quadrature cA, the largest difference is **6.8e-12**, over 15 lines (including α=0, 1/3, 1/2, 1/12, 5/12, 2/11), 4 values of τ (Im τ 1.2–3.6) and 3 sectors (`b_theorem1_fast*.json`).
- **Sector independence.** cA(up), cA(down) and cA(lepton) agree to **1.0e-11**. This is quadrature precision, not the "0.00" agy reports.
  - Where cA returns None, the cause is the sector's own R_s vanishing (for example (2/5,1/10) up, channel i), not a property of c.
- **Novelty.** Not new against the SM seat. W177 (origin/claude/standard-model-derivation-0qt6ao) already has c_s = −2π ln2π − 2πγ − π[ψ(λ₊)+ψ(λ₋)] + π(S₊+S₋). It matches quadrature to 5.5e-13, gives the cusp limit and first correction, and states "ū = (q_L+q_R)w = ±3w in every sector, so one ū per line". It is new only against main, where B1788 says the "prefactors [are] not derived in closed form". B1785 had already observed the {‖3α‖, ½−‖3α‖} exponent pair.
- **Cusp vanishing locus.** D∞ = 0 on (0,½) exactly for α ∈ {1/12, 1/4, 5/12} (I scanned all denominators ≤ 60).
  - The result is stronger than claimed: from cA I get D(τ) = c_j+c_k−c_1−c_i ≈ 1e-14…5e-12 at Im τ 1.5–4.5 on (1/12,0), (1/12,1/12) and (5/12,1/4). So D vanishes identically at finite τ, not only at the cusp. The control (2/5,1/10) gives D ≈ −9.6.
  - The relay calls f = ψ(ν)+ψ(1−ν) "strictly convex". It is concave (f'' < 0). The conclusion still holds because only symmetry plus strict monotonicity in |ν−½| is needed.
  - Trivial corollary of the closed form, but a genuine and relevant observation for B1788's hypothesis (b).
- **Decay exponents.** I fitted from the closed form at Im τ 6–10 (60 digits) on 8 lines; the fits match ½‖3α‖ and ¼−½‖3α‖ to ~1e-4. Two lines cross-checked with main's cA at Im τ 3–5 agree (e.g. (2/5,1/10): 0.0999, 0.1500).
- **Against B1788 hypothesis (a).** (a) is a *lower bound*, |E00−E11|, in B1788's exp(−E·2π Im τ) convention; agy's E uses 4π. Converting:
  - (a) is in fact violated in **18 of 171** (slope, sector) cases with order ≤ 12. Examples: slope 2/5 **up**, rate 0.2 < bound 0.3; 2/7 down; 3/8 up; 3/10 down and lepton. So "(a) false as stated" is correct.
  - agy's "explanation of B1788's anomalies" mixes the two conventions (0.15 vs 0.25, 1/28 vs 3/14, 1/12 vs 1/18). On the anomalous lines B1788 named (2/5, 1/7, 4/9 down), (a) actually *holds*. The jk rate is 3× the bound on 2/5 and 4/9, which is exactly B1788's "about three times faster" note.
  - The "B1788 empirical 0.15 / ~0.04" numbers do not appear in B1788's FINDINGS.

## (c) Theorem 2 (CKM corner inversion) — identity CONFIRMED-BUT-TRIVIAL; benchmarks CONFIRMED; "no-go" REFUTED as a theorem (it is a strong tendency)
- **Yukawa identity.** Y = h mᵀ + m hᵀ − (h·m)I − m₁[h]ₓ, and Y h = Yᵀh = (h·h)m.
  - It holds for random complex S and M through main's coupling(): 2.5e-15 and 7.9e-15. At the four real points the relative error is ≤ 4e-16.
  - It is a generic bilinear identity of the coupling map; R is null in 4D to 1e-16.
- **Benchmark table** (main's primitives, `c_theorem2.py`). Every entry reproduces to quoted precision.
  - B1825 best point: V_ub/(V_usV_cb) = 1.0631, V_td/(V_usV_cb) = 0.0942, V_ub/V_td = 11.280, sinδ = 0.0842, θ12u/θ12d = 14.285.
  - B1726, P-377 and B1743 also match: 4.19/1.2858/0.3236/3.973/0.1376; 42.50/1.0132/0.0691/14.661/0.0675; 27.63/0.9509/0.0559/17.021/0.0267.
- **The "no-go" is a perturbative heuristic, not a theorem.** I scanned 150 random (line, τ) points × 13 directions × 2 radii × 4 quark readings, 15 532 defined rows (`c_nogo_scan2.py`):
  - Rows with a mass hierarchy and SM-ordered CKM (0.05 < V_us < 0.5, V_ub < V_cb < V_us): **52/250 have |V_ub| < |V_td| and 17/250 also have sinδ > 0.5**. Example: (3/7,0), F_18, L_2, S~S~: V_us 0.075, V_cb 0.0094, V_ub 0.00055, V_td 0.00088, sinδ 0.9995.
  - Rows with realistic masses and V_us, V_cb (mc/mt and ms/mb within ×3, 0.1 < V_us < 0.4, 0.015 < V_cb < 0.12): 1/33 has V_ub < V_td and 0/33 flip.
  - So inversion dominates in the realistic corner, but "no point in FR-FIB could ever produce the SM CKM" is not proved. B1825's NO SUPPORT is the actual (census-limited) negative.
- **The "analytic proof" of (0.7347, 0.7347, 1.3611)** is just the minimum-norm solution of one linear constraint, x₁₃−x₁₂−x₂₃ = ln 2.522, i.e. x = (L/3)(−1,−1,1). It is trivial, and the constraint does not even hold for the cited optimizers: r13/(r12r23) = 2.02 (B1743) and 2.93 (P-377), against 2.52.

## (d) Defects 4A–4D — none changes B1825's verdict
- **4A — mis-described / design choice.**
  - Using physical=False in the six's mixture follows the card, which charges all 12 directions in A = 18.81 and says the null shares them.
  - K_ten's posterior being averaged over all choices is stated in its own comment ("every choice"). It is still a valid normalized predictive code (Kraft holds).
  - Choice 30900 (F_26) is a physical direction anyway.
  - K is not graded once X2 fails, and C_ten = −197 is ~209 bits from the gate.
- **4B — real gap, no verdict effect.**
  - physical_choice tests only F[:,6:10], which is exactly the card's preregistered definition ("|V_us|, |V_cb|, |V_ub| or J").
  - Order-12 lines do give m_e = 0: 6w is 2-torsion and 3w is 4-torsion, so B1788's degeneracy applies; there are 96 points of exact order 12, giving 48 lines.
  - agy's 7680 is arithmetic (48×10×2×8, hardcoded in stepb_audit.py), not counted from the census.
  - No effect on S: m_e = 0 rows have χ² = ∞. Effect on p2 is at most ~1/(1−0.192) = 1.24×, which cannot close the ≥8× gap to X2's gate.
  - The NaN at cells.py:127 comes from inf−inf in `dev`. It is caught by the np.isfinite → rad = inf path (conservative), so it is benign. agy quotes the wrong code line.
- **4C — true by construction (V depends only on the up and down U's), no bias.** The duplication is a uniform 2×, so the marginal is unchanged; it is a storage inefficiency.
- **4D — mischaracterized.**
  - There is no IEEE underflow. |θ2/θ3|^a is 1.3e-16 to 2.3e-28 for a = 18–26 at Im τ 3–4, not down to 1e-41 (`d_underflow.py`).
  - The term is only absorbed against O(1) entries, and its effect on h·h (~1e-56 against ~1e-4) is far below census precision.
  - The import-time execution of the_exponents.py is real (guard at line 172; mods() took 9.7 s), but it costs performance only.

## (e) Theorems 3, 4, Gate 0, FR-COV
- **Theorem 3 (det factorization) — CONFIRMED but NOT NEW.** It holds for random inputs to 6.8e-15. It is B1659's J1, det Y = 4 det S det M tr(εSMᵀ), proved by sympy for all S, M ∈ M₂(ℂ), rewritten in quaternion coordinates.
- **Theorem 4 — CONFIRMED-BUT-TRIVIAL and partly not new.**
  - With main's own DR (te.B[1]), DR·DR/η⁶ = 0.25000000000000 at 3 values of τ; main's R equals agy's R.
  - DR·DR = −R·D²R is in B1691 C1 already (R·R ≡ 0, R·DR ≡ 0, R·D²R + DR·DR ≡ 0). The η⁶ constant follows from a one-dimensional weight-3 space.
  - The FR-COV conclusions drawn from it (masses on the primary section, "zero new parameters") do not follow, because a₀ is free.
- **Gate 0 — largely tautological; literal-flag violations.** In evaluate_operator_gate("FR-COV"):
  - **Clause 1:** `extends_to_3manifold_m004=True` is a hardcoded literal.
  - **Clause 4:** `"distinguishes_colour_triplet_dc_from_singlet_L": True` is a hardcoded literal.
  - **Clause 2:** commutant dimension 1 needs the ad hoc "graded reflection" diag(1,−1,−1)P_perm. Using the deck group with the plain sheet swap gives dim 2 (I verified 2, 2 and 1). Nothing derives the sign grading.
  - **Clause 3:** a₀ = 0.20·e^{7πi/8} is hand-picked and hardcoded, together with hardcoded h and m vectors. I checked that those vectors match mine to 1e-16.
  - Arithmetic I confirmed: det(LR−I) = −1, det((LR)³−I) = −16 (15 nonzero fixed points mod 4), |Δ(ω)| = 4, 4/√3. SnapPy finds exactly one connected 3-fold cover (cyclic, H₁ = Z/4+Z/4+Z), so the "unique" claim is OK.
- **FR-COV adds free parameters — and the flip worsens the fit.** At the B1825 point, using main's coupling with S → S + a₀I:
  - a₀ = 0 gives χ² over the 8 quark observables = 277.2.
  - **agy's a₀ gives χ²₈ = 1287.** mc/mt goes 0.0046→0.038 (z +22.5), md/mb z +16.4, V_us 0.112 (z −7.0). V_ub/V_td = 0.678 and sinδ = 0.700 are reproduced. "Preserving mc/mt < ms/mb" is technically true but meaningless.
  - Scan over |a₀| ≤ 1 (≈20k points): the best χ²₈ is 257.5 (V_ub/V_td still 9.2). The best χ²₈ inside the flip region is 514.
  - a₀ is a new complex parameter (2 reals), plus a sector-dependent conjugation under the S/S~ reading. The "w_H twist ⇒ a₀ with zero parameters" argument is not implemented anywhere: the code uses a constant.
  - So FR-COV is a new frame with more freedom (look-elsewhere grows). Its "16.34 bits saved" ledger counts a menu that has not been derived.

## (f) Tests
- agy's `tests/test_elevation_operator_gate.py`, run on the snapshot in an isolated sandbox (`agy_run/`, frontier/scripts symlinked from main, `--rootdir=. -c /dev/null`, no bytecode or cache): **9 passed in 7.7 s**.
- **Not vacuous:** the closed form vs cA (1 τ, 2 lines, up only, tolerance 5e-12) and the random-input checks of the Yukawa identity and Theorem 3.
- **Vacuous / hardcoded:**
  - the Gate 0 asserts, which only echo hardcoded literals and a hand-tuned a₀;
  - the order-12 count (arithmetic);
  - the decay-exponent asserts (formula against itself);
  - the Lagrange check (algebra against itself);
  - the ledger counts (497952 → 6).
- I did not run main's 47 gates (they are not needed for the claims above).
