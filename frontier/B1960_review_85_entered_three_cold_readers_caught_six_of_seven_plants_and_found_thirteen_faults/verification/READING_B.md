# Review 85, reader B: B1959

### F-R85-B1
**File:** frontier/B1959_the_weighted_inverse_on_a_finite_area_cusp_with_the_constant_asymptote_adjoined/FINDINGS.md, line 27
**Verbatim quotation:** `The frame is the weighted theory of elliptic operators on manifolds with cylindrical ends (Lockhart and McOwen,`
**What is wrong:** The page calls this the Lockhart–McOwen frame, with the exponents -β and 1+β as indicial roots "in that sense". The cusp is not a cylindrical end: the circle has length e^(-t) and the operator carries an e^(2t) D_x² term. Only the zero-frequency part is translation-invariant. The page also says the papers were not read, so the Fredholm and index-change statements about them are unverified.
**How checked:** Read FINDINGS lines 24-30 and 37-43 (metric ℓ²(dt²+e^(-2t)dx²), operator with -e^(2t)D_x²). The page's own line 25 says "the papers themselves were not read for this arc".
**Confidence:** medium

### F-R85-B2
**File:** frontier/B1959_the_weighted_inverse_on_a_finite_area_cusp_with_the_constant_asymptote_adjoined/FINDINGS.md, line 31
**Verbatim quotation:** `**This is the first proof of the statement.**`
**What is wrong:** The page says this is "the first proof", but the next sentence says "The statement is of a known kind". Section 5 (lines 152-155) and the lane's written argument (B1957 record physical-cis-01) say the lane already argued the same equation (3), by variation of constants and the bounded inverse theorem. The literature was not read. "First proof" is an overclaim of novelty that nothing in the arc supports.
**How checked:** Compared FINDINGS lines 24-33 and 152-155 with arc_verdict.json `cites_seat` ("stated by that lane with its own argument"). Also read `frontier/B1957_the_seats_claims_register/verification/records/physical-cis-01.json` ("the lane's own written-out argument for the inverse on its cusp ... B1959 ... proves the same statement ... by another route").
**Confidence:** high

### F-R85-B3
**File:** frontier/B1959_the_weighted_inverse_on_a_finite_area_cusp_with_the_constant_asymptote_adjoined/FINDINGS.md, line 80
**Verbatim quotation:** `its quadratic form is at least (1/4 + ℓ²c_j)‖u‖².`
**What is wrong:** As stated for a channel on the cusp half-line [T₀,∞) this is false. With u = e^(t/2)v the form is ∫|v'|² + (1/4+ℓ²c)v² - v(T₀)²/2. That is below the threshold for functions that do not vanish at the cut. It holds only for functions supported inside the cusp, which is what Persson's formula needs, and the page does not say so. The arc's own numerical check K2 finds one eigenvalue (0.9031) below the threshold 1.15, which is the counterexample.
**How checked:** Integrated ∫|u'|²e^(-t) by parts. Read cusp_inverse_run.txt line 3: "eigenvalues below the threshold ... 1 and 1; the lowest 0.9031 and 0.9031" against threshold 1.1500. Read the cusp_inverse.py line 57 comment, where the boundary condition is u'=0 at the cut. The FINDINGS table (line 139) reports "1 and 1" without explaining it.
**Confidence:** medium

### F-R85-B4
**File:** frontier/B1959_the_weighted_inverse_on_a_finite_area_cusp_with_the_constant_asymptote_adjoined/FINDINGS.md, line 93
**Verbatim quotation:** `At an interior maximum of |W|,`
**What is wrong:** For zero-frequency channels with c_j>0 the estimate assumes |W| = e^(δt)|u| attains its maximum at an interior point. On [T,∞) the supremum could be approached at infinity. The nonzero-frequency step handles this with the εe^((1+β₁)t) device and a sequence tending to infinity. The zero-frequency step has no such argument, so the displayed bound sup e^(δt)|u| ≤ max(...) is not justified as written. A repair is easy, but the step as stated has a gap.
**How checked:** Read Step 4, lines 86-96 against lines 105-113.
**Confidence:** medium

### F-R85-B5
**File:** frontier/B1959_the_weighted_inverse_on_a_finite_area_cusp_with_the_constant_asymptote_adjoined/FINDINGS.md, line 106
**Verbatim quotation:** `K(t) ≥ m₀² e^(2t)/4, which is increasing. Take T₁ larger if needed so that K₁ = K(T₁) > δ + δ².`
**What is wrong:** The comparison function Z needs K(t) ≥ K₁ for all t ≥ T₁, where K₁ = K(T₁). The page only shows that the lower bound m₀²e^(2t)/4 is increasing, not that K is. K(T₁) may exceed the lower bound at T₁, so K(t) ≥ K(T₁) does not follow from what is written. Either K₁ should be defined as m₀²e^(2T₁)/4, or monotonicity of K beyond T₁ should be argued. It is in fact true, since each V_m = (|m|e^t ± |w|/2)² is increasing there, but the stated reason is not the reason.
**How checked:** Checked the subsolution step (lines 109-113), which uses -N''+N'+K₁N ≤ -N''+N'+KN. Checked V_m = (m e^t + w/2)² (line 49). The code's K6 (cusp_inverse.py line 79) uses the actual K[i1].
**Confidence:** medium

### F-R85-B6
**File:** frontier/B1959_the_weighted_inverse_on_a_finite_area_cusp_with_the_constant_asymptote_adjoined/FINDINGS.md, line 132
**Verbatim quotation:** `The proof's formulas, each checked, and each with the change that breaks it.`
**What is wrong:** The table shows a control only for K4 and K7. The script cusp_inverse.py has controls only for K4 and K7. The lock has controls for K1, K3 and K4, plus a K7 control that checks only the size of the non-decaying source's growth. K2 has no control, and K5 and K6 have none anywhere. K5 and K6 are not in the lock at all. So "each ... with the change that breaks it" overclaims, as does the script docstring (line 2).
**How checked:** Read the FINDINGS table lines 135-145, all of cusp_inverse.py, and the four tests in test_b1959_cusp_inverse.py (K1; K2 and K3 symbolic; K4; K7). Ran `python3 -m pytest -q test_b1959_cusp_inverse.py`: 4 passed.
**Confidence:** high

### F-R85-B7
**File:** frontier/B1959_the_weighted_inverse_on_a_finite_area_cusp_with_the_constant_asymptote_adjoined/FINDINGS.md, line 141
**Verbatim quotation:** `control: a weight δ = 0.8 beyond β = 0.527`
**What is wrong:** The number is wrong. In the run, β_c = 0.5724, which is (√4.6 - 1)/2 for ℓ²c = 0.9. 0.527 is a digit transposition.
**How checked:** cusp_inverse_run.txt line 4: "beta_c = 0.5724". Computed (sqrt(4.6)-1)/2 = 0.57238.
**Confidence:** high

### F-R85-B8
**File:** frontier/B1959_the_weighted_inverse_on_a_finite_area_cusp_with_the_constant_asymptote_adjoined/verification/test_b1959_cusp_inverse.py, line 1
**Verbatim quotation:** `"""B1959's lock: the computable steps of the proof, each recomputed here (no stored number is read), each with the change that breaks it."""`
**What is wrong:** The lock recomputes K1, K2/K3 (symbolic), K4 and K7. It does not recompute K5 (the c=0 bounds), K6 (the nonzero-frequency inequality and N ≤ Z) or the numerical K2 eigenvalue count. So the docstring's "the computable steps of the proof, each recomputed" is not true. A change to the K5 or K6 formulas would leave the lock green. The K7 control only tests that u moves by more than 1.5 over ten units, not the formula.
**How checked:** Read the file's four test functions in full, and compared them with K1-K7 in cusp_inverse.py. Ran pytest: 4 passed.
**Confidence:** high
