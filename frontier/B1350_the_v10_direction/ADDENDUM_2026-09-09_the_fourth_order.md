# B1350 addendum (2026-09-09) — the fourth order: the V₁₀ deformation leaves the self-dual world and the fixed-vector locus together

Two facts established in B1352 (`frontier/B1352_the_fixed_vector_locus_along_v10`) sharpen this arc's record.

1. **The trace defects obey a t⁴ law.** A second genuine point along class 1 at step 0.04/|Y| (same script, `V10_STEP=0.04`;
   relator residual 2.2·10⁻⁶⁷; 2000-bit re-read h¹(27) = h¹(27̄) = 0, h⁰(∂M) = 0, N = 0 — B1352 `verification/step04/`) has
   self-duality defects 3.69·10⁻¹¹, 3.69·10⁻¹¹, 3.03·10⁻⁹, 8.31·10⁻⁷, ~0, 8.31·10⁻⁷ against this arc's 2.18·10⁻¹², 2.18·10⁻¹²,
   1.79·10⁻¹⁰, 4.92·10⁻⁸, ~0, 4.92·10⁻⁸ at step 0.02: **all five ratios equal 16.884** = (t₂/t₁)⁴ with t₂/t₁ = 2.027. Stage (3)'s
   first-order trace-flatness is the first of three vanishing orders: the V₁₀ curve is self-dual through third order and not at
   fourth. This is the quantitative form of "θ-odd but trace-flat" of §1.
2. **The cusp-fixed vectors are lost at the same order.** Exactly (B1352 stages C, D): the V₁₀ of the 42 keeps all three cusp-fixed
   vectors of ρ₀ to first order — the only θ-odd direction that does (V₄: F F T, V₈: F T T, V₁₆: F F F) — and on every formal V₁₀
   branch of `obstruction_higher.py` (greedy, or randomised within the five first-order-keeping classes) they are lost at order 4
   (Smith exponents of [μ(t) − I; λ(t) − I] over F_p[t], p = 67108819 and 67108837, kd(m) = 3, 6, 9, 12, 12, …); on generic
   branches at order 2. Numerically the largest of the three small cusp-fixed singular values scales as (t₂/t₁)^{4.00} between the
   two genuine points; the two smaller ones do not scale cleanly (exponents 4.39, 5.64 on the 0.02 → 0.04 interval, 3.59, 7.56 on the 0.01 → 0.02 interval: not asymptotic at these steps); a third genuine point at step 0.01/|Y| (B1352 `step01/`: relator 2.0·10⁻⁶⁵, N = 0 at 2000 bits) gives defect ratios 12.737 on all five words and the leading singular value's exponent 4.000 again.
   The three values are real: polishing this arc's class-1 point at 2000 bits (residual 6.0·10⁻⁶⁸ → 2.7·10⁻⁸²) moves ρ(a) by 4.2·10⁻⁶⁰ relative and changes them by less than 10⁻⁴² relative (B1352 `polish_and_svals_run.txt`) — §4's h⁰(∂M; 27) = 0 rests on genuine non-zero pivots, not on the residual.

The reading of this arc's §4 stands and gains its mechanism: h⁰(∂M; 27) = 0 at the genuine points is not an accident of the step but
a fourth-order loss, and the point with three cusp-fixed weights nearest to each genuine point is an Sp(8) point (self-dual, N = 0).
