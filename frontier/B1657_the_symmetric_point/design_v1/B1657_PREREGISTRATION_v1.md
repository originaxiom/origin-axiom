# B1657 — THE SYMMETRIC POINT: the isotropic vacua at τ = ω are rank one, and the two light masses are two isotropy defects: preregistration

cc (main), 2026-10-15. POINT_REGISTER P-153 (main's audit of its negatives, B1655, found the isotropic Higgs directions
never tested as vacua and the near-ω regime uncomputed). The weave's fibre frame at its puncture, given Λ, the record's
hand, one fibre and one τ at a time: a frozen piece, and its scope says so. No data. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /symmetric point|isotropic (vacu|eigenline|direction)|rank one at|two (isotropy )?defects|isotropy defect|order-3 (move|automorphism)/: 5 of 1427 arcs on main match (PROVED 5)`
— B1645 (rank one on the whole isotropic cone a·a = 0; m grows linearly in |a·a|/|a|²), B1646 (the unitary frame
(R/|R|, R̄/|R|, n) fixed by τ; the direction is the mass matrix), B1654 (D(τ), zero at ω; the canonical end condition),
B1443 and B1023 (other senses). **Read before the seal, from the SM seat's branch (37a5c5924):** W87, which proves B1654's channel norms in closed form, c_r = −2π ln((π/2)∣θ_r(0)∣²), and D(τ) = −θ₃⁴h(λ)/(4πη⁶) with h(λ) = λ ln∣λ∣ + (1 − λ) ln∣1 − λ∣, zero exactly on ω's orbit, and finds post hoc the slope at ω, (π²√3/6)∣θ₃(ω)∣⁴ = 2.9491720, in every direction (main checked both on its own code: D against B1654's stored values to 1.3 × 10⁻¹⁴ at five points, the slope against its own exploration's 2.94917); and its reading of which flat hypercharge lines split the sectors. **What this arc adds to them:** the order-3 move's matrix at ω, whose eigenlines are
exactly B1646's frame, so the symmetric Higgs vacua are its axes; the rank-one spectrum at the isotropic ones under
both end conditions; the first-order law with the zero-mode triplet also off its cone, with coefficient one and the
Higgs and the matter in symmetric roles; the isotropic vacuum under B1654's canonical end condition; and D near ω.
**Literature:** isotropic vectors in ℂ³; the near-fixed-point mechanism of modular flavour (Novichkov, Penedo, Petcov;
Feruglio et al.), whose input — distinct residual charges at a fixed point — this frame has (the three eigenvalues
e^{∓iπ/3}, −1). Nothing here is claimed as new mathematics.

## 0b. Disclosed

- **Everything the cells read was seen.** Main's exploration (`audit/drafts/sym/`, kept off the tree and beside the
  seal at banking): `symmetric_point_explore.py` (the move's matrix, its eigenlines, the three spectra),
  `two_defects_explore.py` (the first-order law at ω, i, t1 and τ*: worst 0.009 per unit perturbation),
  `near_omega_explore.py` (|D|/(|R|²δ) → 2.949 in six directions; arg D = π/4 − arg δ; D/|R|² = 0.3184(1 + i) at
  τ* = ½ + i√5/2). The instrument itself was run twice before the seal, from the drafts folder: the first run failed S3
  on two errors of main's draft — the determinant's sign (det Y = +(a·v)(a·a)(v·v), as B1644's form) and the
  normalisation control's threshold (with |a| = 2, |v| = 3 the unnormalised defects miss by factors 4 and 9, a deviation
  of 0.75–0.89, not above 1) — both corrected; the second run held every cell. **No cell here is blind.** The arc's worth
  is the certified statement and its lock, not a prediction.
- **By hand (§1)**, the first-order block; the cells check it.
- **Which cells are identities, not tests (E82, E89's rule):** S1's orthogonality, P³ = −1 and the covariance of Y;
  S2's rank-one spectra (B1645's cone, given S1); S3's symbolic determinant and a ↔ v symmetry; S4's exact zero
  (a·a = 0). The cells that can fail are S1's fit and its generic-τ control, S2's real-direction control, S3's
  first-order law and its normalisation control, S4's limit, and S5.

## 1. The setting, and what follows by hand

- **The coupling.** Y(a; v) = a vᵀ + v aᵀ − (a·v)𝟙, with a the Higgs's direction in M and v the zero modes' residue
  triplet: v = R under equal framed data (P4′), v_r = √(2πL + c_r)·R_r under equal canonical amplitudes (P4), so that
  v·v = D(τ) (B1654). R = (−θ₂², iθ₃², −θ₄²)/θ₁′(0) in channels (2, 3, 4), and R·R = 0 by Jacobi.
- **Identities.** Y(a; v) = Y(v; a). Y a = v(a·a), Y v = a(v·v), and Y acts as −(a·v) on the bilinear complement of
  {a, v}; so det Y = (a·v)(a·a)(v·v).
- **The order-3 move at ω.** γ(τ) = −1/(τ + 1) fixes ω. With θ² = (θ₂², θ₃², θ₄²), θ²(γτ) = (τ + 1)·M·θ²(τ); in R's
  basis M becomes the real signed permutation P = [[0, 1, 0], [0, 0, −1], [1, 0, 0]], orthogonal with P³ = −1. Its
  eigenlines are R(ω) (eigenvalue e^{−iπ/3}), R̄(ω) (e^{iπ/3}) and n = (1, −1, −1)/√3 (−1): two isotropic, one real.
  Since P is orthogonal, Y(Pa; Pv) = P·Y(a; v)·Pᵀ, so a P-invariant potential's symmetric vacua are the three lines.
- **The three symmetric vacua at ω.** a ∝ n: n·R = 0, so Y = nRᵀ + Rnᵀ, two equal masses and one zero: (1, 1, 0) —
  the degenerate pair the record found at ω. a ∝ R̄: Y = R̄Rᵀ + RR̄ᵀ − ∣R∣²𝟙 = −∣R∣²·nnᵀ (with ∣R∣ = 1): rank one,
  the heavy state n, both R and R̄ massless: (1, 0, 0). a ∝ R: Y = 2RRᵀ, rank one. At ω all c_r are equal, so P4 gives
  v ∝ R and the same spectra.
- **The first-order law.** Take ∣R∣ = 1, a = R̄ + α, v = R + β. Y₀ = −nnᵀ; on the light space span{R, R̄}, which is
  unitary and bilinear-dual (R·R̄ = 1, R·R = 0), the first-order block is [[0, 2α·R̄], [2β·R, 0]]. So the two light
  singular values are ∣2α·R̄∣ = ∣a·a∣ and ∣2β·R∣ = ∣v·v∣ to first order, the heavy one 1. Restoring the norms by
  homogeneity: **the light masses over the heavy are ∣a·a∣/∣a∣² and ∣v·v∣/∣v∣²**, the two isotropy defects, with
  coefficient one.
- **The isotropic vacuum under P4.** a ∝ R̄(τ) keeps a·a = 0 exactly, so one generation is exactly massless at every τ;
  the next is ∣v·v∣/∣v∣² = ∣D∣/(2πL∣R∣² + Σ c_r∣R_r∣²), so L·s₂/s₁ → ∣D(τ)∣/(2π∣R∣²). At ω, D = 0 and it vanishes too.
  (In B1654's limit formula, for a off the cone, the lift goes to the lightest generation; on the cone it goes to the
  middle one, and the lightest stays at zero.)

## 2. The cells (the instrument `verification/the_symmetric_point.py`; one run)

| cell | prediction | prior | identity or test |
|---|---|---|---|
| **S0**, plumbing (void) | numpy theta series against mpmath jtheta at the six τ < 10⁻¹²; ∣R·R∣/∣R∣² < 10⁻¹³; B1654's stored c_r at ω equal to 10⁻⁹ | 99% | gate |
| **S1**, the move | (a) the fit of M at four generic τ, residual < 10⁻¹²; (b) M in R's basis equals P to 10⁻¹²; (c) PᵀP = 𝟙 and P³ = −𝟙 exactly; (d) R(ω) an eigenvector with eigenvalue e^{−iπ/3}, R̄(ω) with e^{iπ/3}, n with −1, all to 10⁻¹²; ∣R·R∣ < 10⁻¹³∣R∣², n·n = 1; (e) Y(Pa; Pv) = P Y Pᵀ at 20 random pairs < 10⁻¹²; **control:** at τ = 0.13 + 1.07i, R is not a P-eigenvector (residual > 0.05) | 97% | (a), (b), (d) and the control test; (c), (e) identities |
| **S2**, the symmetric vacua | at ω with v = R: a ∝ n gives (1, 1, 0), a ∝ R and a ∝ R̄ give (1, 0, 0), each to 10⁻¹²; under P4 at L = 10 and 100 the same to 10⁻⁹; **control:** 50 random real directions give s₂/s₁ ≥ ½ (B1645) | 97% | the spectra identities given S1; the control a test |
| **S3**, two defects | (a) symbolically det Y − (a·v)(a·a)(v·v) = 0 and Y(a; v) = Y(v; a); (b) ∣det Y∣ = ∣a·v∣∣a·a∣∣v·v∣ at 100 random pairs to 10⁻¹²; (c) at ω, i, t1 and τ*, two seeds × 200 draws with a = 2(R̄/∣R∣ + ε_a α), v = 3(R/∣R∣ + ε_v β), ε ∈ 10^[−6, −2]: max ∣(s₂/s₁, s₃/s₁) / (sorted defects) − 1∣ / max ε < 0.05; **control:** the unnormalised ∣a·a∣, ∣v·v∣ miss by > 0.5 | 95% | (a), (b) identities; (c) and the control tests |
| **S4**, the isotropic vacuum under P4 | a ∝ R̄(τ), v_r = √(2πL + c_r)R_r with B1654's stored c_r, at ω, i, t1, t2, t3 and L ∈ {40, 160, 640, 2560}: (a) s₃/s₁ < 10⁻¹² everywhere; (b) at L = 2560, L·s₂/s₁ within 1% of ∣D∣/(2π∣R∣²) from B1654's stored D at i, t1, t2, t3; (c) at ω, L·s₂/s₁ < 10⁻⁸ | 93% | (a) identity; (b), (c) tests |
| **S5**, D near ω | by the cutoff-free integral, at ω + δe^{iφ}, φ = jπ/3 + π/7 (j = 0…5), δ ∈ {10⁻³, 2.5 × 10⁻⁴}: ∣D∣/(∣R∣²δ) has relative spread < 2 × 10⁻³ at the smaller δ and smaller than at the larger, and its mean is within 10⁻³ (relative) of the SM seat's (π²√3/6)∣θ₃(ω)∣⁴; arg(D·e^{iφ})/π has spread < 2 × 10⁻³ and mean within 2 × 10⁻³ of ¼ — that is, D(ω + δ) = κ·δ̄·∣R∣² + O(δ²), ∣κ∣ = W87's slope, arg κ = π/4 | 90% | test |

Overall: PROVED if S0 is not void and S1–S5 hold; each failure is reported as a failure of its own clause.

## 3. What each outcome would mean

- **All hold.** At the weave's order-3 point the symmetric Higgs vacua are the three axes of B1646's frame; the real one
  is the degenerate pair the record found, and the two isotropic ones are rank one — one heavy generation and two
  massless. Off them, the two light masses over the heavy are the isotropy defects of the Higgs and of the zero-mode
  triplet, at first order with coefficient one. Under B1654's canonical end condition, in the isotropic vacuum, one
  generation stays exactly massless at every τ and the next is ∣D(τ)∣/(2πL∣R∣²), which vanishes at ω like ∣τ − ω∣.
  τ = ω's retirement ("no hierarchy found at ω") is then a statement about the real vacuum only.
- **S3(c) fails.** The coefficient is not one, or the law needs a correction at the sampled sizes; the reading of the
  masses as defects would stand only in order of magnitude.
- **S4(b) fails.** The isotropic vacuum's lift is not B1654's D; recompute before any use.
- **S5 fails.** D's leading behaviour near ω is not a single antiholomorphic term; the "like ∣τ − ω∣" clause goes.

## 4. What it does not show

- **Which vacuum is chosen** — the isotropic or the real — nor why the Higgs sits near an isotropic line rather than on
  it (the Higgs's defect needs its potential: B1646's quartic picks a locus; the octic and one-loop terms of B1655's
  check put minima between).
- **τ, L, the end condition** (P4 or P4′), or the sectors: this arc is untwisted; the sectors' twisted channels are
  B1656's (the electron's zero).
- **Anything about the interacting weave**: one fibre, one τ, the field held fixed.
- **Any value.** The Cabibbo angle is not here: at first order the light states are R and R̄ in every sector.

## 5. Files

`verification/the_symmetric_point.py` (sealed), its JSON and run text after the one run; the exploration scripts and
the drafts' two runs beside the seal at banking.
