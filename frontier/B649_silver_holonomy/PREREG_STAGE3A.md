# B649 stage 3a — TRACK S WAVE 4: the silver double's dimensions (campaign a463c6aa)

**Objective: the weld solve and h¹(D_silver; 27) — the dimension gate
for the silver chord. The Y-tensor and form-level law checks are
stage 3b (they run only if h¹ ≥ 3, exactly as the fig-8's B637
sequencing).**

## Conventions block

- Side 1 letters: the exact 27-lift (letters27_L.json, stage 2b).
- Conjugation on L = ℚ(s, i): i ↦ −i, s ↦ s (s is real);
  conj(L(re, im)) = L(re, −im).
- The weld at SL₂(L): solve u·conj(ρμ) = ρμ·u AND u·conj(ρλ) = ρλ⁻¹·u
  (the fig-8 convention: μ₂ = μ₁, λ₂ = λ₁⁻¹) as a rational linear
  system (64 unknowns) over the exact SL₂(L) letters; require an
  invertible element of the solution space; U27 = the scale-invariant
  Bruhat lift (projective — valid on even Sym powers); U27⁻¹ = the
  lift of the 2×2 adjugate.
- Side 2 letters: d,e,f (↔ a,b,c primed): ρ₂(g) = U27·conj₂₇(ρ₁(g))·U27⁻¹.
- π₁(D) presentation (6 generators, 6 relators): R1 = aBAbcc,
  R2 = aaCbcB, R1′ = dEDeff, R2′ = ddFefE, Rμ = CCBeff (μ₁μ₂⁻¹),
  Rλ = caCAfdFD (λ₁λ₂).
- h¹ by amalgam-Fox: 162-dim cochains; Z¹ = nullspace of the 6×27
  relator rows (pure-L Gaussian elimination — coefficient heights ≤ 20
  digits at input, feasibility verified pre-seal); B¹ = rank of the
  coboundary block; h¹ = dim Z¹ − rank B¹; h⁰ = 27 − rank B¹.
- Also reported: the SOLO h¹(M_silver; 27) (3 generators, 2 relators,
  81-dim) — the fig-8 comparison point (its solo h¹ = 3).

## Gates (two-outcome)

- **S3a-G1:** the weld intertwiner EXISTS over L (invertible solution)
  — else bank the obstruction (the silver mirror-double's 27 local
  system does not glue by this convention; name the defect; GATE B
  re-scopes).
- **S3a-G2:** side-2 letters satisfy the primed relators = I₂₇ exactly
  (consistency of the mirror construction).
- **S3a-G3:** h⁰ and h¹ of the double, exact integers; the solo h¹
  alongside. NO prediction is sealed for the values (the fig-8 gave
  solo 3, double 5; the silver's numbers are the DISCOVERY — the
  campaign's form-level table needs them, whatever they are).

Outcome: h¹ ≥ 3 ⇒ stage 3b (the Y-tensor + the form-level laws).
h¹ < 3 ⇒ the silver chord has no cubic slot — itself a form-level
verdict for §B2 (the fig-8's cubic would be dial-class, not
object-class; that reading banks honestly and GATE B proceeds with it).
