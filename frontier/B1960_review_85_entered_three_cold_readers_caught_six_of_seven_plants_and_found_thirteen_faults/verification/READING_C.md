# Review 85, reader C: the window's checks of 2026-11-19

### F-R85-C1
**File:** frontier/B1811_the_symmetry_selection_values_against_the_six/FINDINGS.md, line 103
**Verbatim quotation:** `a₀ against F₆: relative 2.532 at (i, 0), in up's m₁/m₃ at L_max`
**What is wrong:** The digits are transposed. decode_run.txt prints 2.352 (D3, up|L_max|St, entry 1), and the test asserts "largest relative difference 2.352". FINDINGS line 94 says 2.35, and P-517 says 2.352.
**How checked:** decode_run.txt D3 line for (i, 0); tests/test_b1811_the_symmetry_selection_values_against_the_six.py line 28; FINDINGS line 94; POINT_REGISTER row P-517. I also re-ran decode.py and its output equals decode_run.txt.
**Confidence:** high

### F-R85-C2
**File:** frontier/B933_spinor_hejhal_design/DESIGN.md, line 137
**Verbatim quotation:** `**(a) Exact spectral symmetry — proven, not assumed.** J = σ₂ ∘ conj`
**What is wrong:** § 5a still states the J argument as proven, but J commutes with D (tests/test_b933_j_commutes_with_d.py, S274). The 2026-11-19 notes (B933 FINDINGS line 62, B940 FINDINGS line 63) say the symmetry now rests on U = σ₂∘Φ*, not on J. Neither note, nor any other, was added to DESIGN § 5. That includes the "by §5 the set is exactly symmetric" sentence at § 2. The test docstring calls § 5a "corrected" and POINT_REGISTER P-540 says "dated notes on B940 and B933 § 5a". The note is in FINDINGS only, and DESIGN § 5a is uncorrected.
**How checked:** grep of DESIGN.md for S274, P-540 and 2026-1 returns nothing. Read DESIGN lines 137–145 and tests/test_b933_j_commutes_with_d.py.
**Confidence:** medium

### F-R85-C3
**File:** frontier/B933_spinor_hejhal_design/FINDINGS.md, line 62
**Verbatim quotation:** `spec(D) = −spec(D) holds after all, as a theorem from a different operator than J`
**What is wrong:** "As a theorem" says more than was checked. The B940 note and pairing_source.py say the script checks identities E1–E5. They say the closing operator-theoretic step (U maps automorphic spinors to automorphic spinors, is unitary on L², and UDU⁻¹ = −D) is "main's derivation", not checked. Domain and unitarity are not checked, and E5 checks the cocycle relation only on random samples. The step from "the lifted group is normalised" to "U preserves the ρ₁ automorphy" is also not run as a test.
**How checked:** pairing_source.py docstring, last paragraph: "the script checks each identity, not the operator-theoretic closing step". Compared with the B933 note's wording.
**Confidence:** medium

### F-R85-C4
**File:** frontier/B940_dirac_sealed/FINDINGS.md, line 63
**Verbatim quotation:** `(symbolic; with σ₁ in place of σ₂`
**What is wrong:** The full sentence reads "(symbolic; with σ₁ in place of σ₂ it does too)". It contradicts the script, which records `control_sigma1_fails: True`. The test asserts it, and the docstring says the wrong matrix in U fails. By hand, Φ⁻¹ flips y, so M must commute with σ₂ and anticommute with σ₁ and σ₃. Only σ₂ qualifies, and σ₁ does not anticommute.
**How checked:** pairing_source_run.txt line E2: `'control_sigma1_fails': True`. pairing_source.py e2(). tests/test_b940_the_pairing_source.py asserts `'control_sigma1_fails': True`. I derived the sign pattern by hand.
**Confidence:** high

### F-R85-C5
**File:** frontier/B1667_the_canonical_cusp/FINDINGS.md, line 84
**Verbatim quotation:** `at most 6.7 × 10⁻⁴ in L_max and 4.4 × 10⁻⁴ in L_2`
**What is wrong:** The L_2 bound is 4.4 × 10⁻³. radius_midpoints_run.txt gives a largest |error| of 4.40e-03 for L_2 (the 1.125 row, −4.40e-03). The same note says L_2 is "about four times" P-542's 1e-3. The lock test asserts the string "4.4 × 10⁻³ in L_2" in this FINDINGS file, and it does not occur there, so that assertion would fail. The POINT_REGISTER row P-542 says 4.4e-3.
**How checked:** radius_midpoints_run.txt last lines; tests/test_b1667_the_canonical_cusp.py line 68 (assertion string); grep "4.4 × 10⁻" in the FINDINGS returns only line 84, with ⁻⁴.
**Confidence:** high

### F-R85-C6
**File:** frontier/B1957_the_seats_claims_register/FINDINGS.md, line 715
**Verbatim quotation:** `1,248 statements, 7 verified from main's record and 1,210 conditional by a stated rule`
**What is wrong:** 7 + 1,210 = 1,217, not 1,248. The remaining 31 statements have no stated verdict in the bullet. The other counts in the bullet add up (512 = 94+3+271+144; 1,417 = 139+18+863+397; the register total 35,165).
**How checked:** Arithmetic on the line. The rest of the file has no other account of row 1968, and I did not find the row's source in the copy.
**Confidence:** low
