# B1645 — PREREGISTRATION: THE HALF BOUND — a Higgs in M has the coupling Y(a) = a Rᵀ + R aᵀ − (a·R)𝟙; for a real direction the two massive generations have a ratio between ½ and 1, fixed by one angle

cc (main), 2026-10-14. **Sealed before `half_bound.py` runs.** No data. 0 of 19. POINT_REGISTER P-114.

**Why it matters.** B1644 found that a Higgs in the multiplicity space M gives the first coupling on the record with
flavour structure. One generation is exactly massless, by Jacobi's identity. The ratio m = m₂/m₃ of the other two came
out numerically at least ½ for real directions and as low as 0.004 for complex ones. This arc turns the real-direction
observation into a theorem with a closed form, and reads the complex case.

**The derivation, by hand, written before the run** (from B1644's sealed table, which held exactly).
1. **The formula.** Relabel B1644's blocks by their units (i, j, k). The table is Y(a)_rr = 2a_r R_r − (a·R) and
   Y(a)_rs = a_r R_s + a_s R_r for r ≠ s. That is
   **Y(a) = a Rᵀ + R aᵀ − (a·R)𝟙.**
2. **The null vector.** Y(a) R = a(R·R) + R(a·R) − (a·R)R = a(R·R), which is 0 because Jacobi makes R isotropic
   (B1644). **The massless state is R itself, the theta triplet,** for every direction a.
3. **A real direction.** Write R = r(e₁ + i e₂), with e₁, e₂ real, orthonormal, and e₃ = e₁ × e₂ (possible because
   R·R = 0). Write a = αe₁ + βe₂ + γe₃ and z = α − iβ. Then
   Y/r = [[z, iz, γ], [iz, −z, iγ], [γ, iγ, −z̄]].
   - Its 2 × 2 minors give, by Cauchy–Binet, s₁²s₂² = 4r⁴(|z|² + γ²)², so s₁s₂ = 2r²|a|² = |R|²|a|².
   - Its entries give s₁² + s₂² = r²(4|a|² + |z|²) = 2|R|²|a|² + |a·R|².
   - With u = |z|²/|a|² = |a·R|²/(r²|a|²) ∈ [0, 1], the squared masses over r²|a|² are the roots of
     t² − (4 + u)t + 4 = 0.
4. **Hence m² = t₋/t₊, increasing from m = ½ at u = 1** (a in the plane of Re R and Im R) **to m = 1 at u = 0** (a
   perpendicular to it). For real directions m ∈ [½, 1], and the spectrum depends on the single angle that u measures.
   That is why B1644's S3c read a spectrum map of rank 1.
5. **A complex direction: m reaches 0, at the conjugate theta triplet.** Take a = R̄. Then a·R = |R|² = 2r², and in the
   basis of step 3 R̄Rᵀ + RR̄ᵀ = 2r² diag(1, 1, 0), so Y(R̄) = 2r² diag(1, 1, 0) − 2r²𝟙 = −2r² diag(0, 0, 1), of rank
   one: one massive generation and two massless. Near R̄, m grows continuously from 0, so the second-to-third hierarchy
   measures how far the Higgs's direction is from the conjugate of the theta triplet. (B1644's 0.004 was the closest of
   its random draws.)

## Seen first

`VERDICT topic-sweep /half bound|isotropic|massless generation|Higgs in M|conjugate.*triplet/: 9 of 1416 arcs on main match (NEGATIVE 1, OPEN 3, PROVED 5)` — B1644 the nearest; none derives the closed form.
Seen: B1644's sealed data and its post-seal ratio range (0.5000000 for real directions; 0.004 for complex ones), which
this arc explains.

**Literature:** Cauchy–Binet for the second elementary symmetric function of Y†Y; isotropic vectors in ℂ³.

## Disclosed

- The derivation explains numbers already seen (B1644's post-seal ratio range), so cells T1–T4 are checks of a derived
  theorem, not blind predictions.
- T5 is a read-out.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **T1** | B1644's residue coupling Y(a), computed at 6 random τ and 6 random complex a, equals a Rᵀ + R aᵀ − (a·R)𝟙 in the unit labels, to 1e-25 | 95% |
| **T2** | Y(a) R = 0 at the same points, to 1e-25 relative | 95% |
| **T3** | for 200 random real a at 6 τ: s₁s₂ = \|R\|²\|a\|² and s₁² + s₂² = 2\|R\|²\|a\|² + \|a·R\|², to 1e-20 relative | 95% |
| **T4** | m(u) = √(t₋/t₊) from t² − (4 + u)t + 4 = 0 matches every real sample to 1e-12; min over samples ≥ ½ − 1e-12; m = ½ for a in span(Re R, Im R), m = 1 for a ∥ Re R × Im R | 95% |
| **T5** | complex directions: Y(R̄) has rank one, with singular values (2r², 0, 0) up to the scale, at 6 τ to 1e-25; inf m = 0, attained at a ∝ R̄; along a = R̄ + εw for 3 random complex w, m grows linearly in ε for small ε (the log-log slope of m against ε over ε = 10⁻², 10⁻³, 10⁻⁴ is 1 within 5%) | 80% |

**The reading (the cells can only lower it).** If T1–T5 hold, a Higgs in M has a closed-form coupling:
- the theta triplet R is its massless state, for every direction;
- a real direction gives m ∈ [½, 1], fixed by one angle;
- the conjugate triplet R̄ gives one massive generation alone, and the second-to-third hierarchy is the Higgs's distance
  from R̄.

A leading-order pattern of one heavy generation, one light and one massless is then a statement about where the Higgs
points relative to the theta triplet, and τ enters only through R.

## Instruments

`verification/half_bound.py` (B1642's and B1644's sealed definitions reused); hashes in `ARTIFACT_HASHES.txt`.
