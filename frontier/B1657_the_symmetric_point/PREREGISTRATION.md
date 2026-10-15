# B1657 — THE SYMMETRIC POINT: two isotropic vacua, two laws: preregistration

cc (main), 2026-10-15. POINT_REGISTER P-153 (main's audit of its negatives, B1655, found the isotropic Higgs directions
never tested as vacua and the near-ω regime uncomputed). The weave's fibre frame at its puncture, untwisted (no
hypercharge line), given Λ, the record's hand, one fibre and one τ at a time: a frozen piece, and its scope says so.
No data. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /symmetric point|isotropic (vacu|eigenline|direction)|rank one at|two (isotropy )?defects|isotropy defect|order-3 (move|automorphism)/: 5 of 1427 arcs on main match (PROVED 5)`
— B1645, B1646, B1654, B1443 and B1023 (the last two in other senses). The sweep reads titles and verdict lines, so the
reviewing agent and main read further; **the precedents, each read:**
- **B1645**: rank one on the whole isotropic cone a·a = 0; Y(R̄) = −2r²·diag(0, 0, 1) in its frame; T4, m = 1 for a
  direction normal to R's plane at every τ — the (1, 1, 0) below; m grows linearly in ∣a·a∣/∣a∣² (the a-side of the
  first law, slope one).
- **B1646**: the unitary frame (R/∣R∣, R̄/∣R∣, n) fixed by τ; D3, s₁s₂ = ∣R∣²∣a·a∣.
- **B1651** U4, U5: the moves carry R by the 24 rotations, and the four real body diagonals (n is one) are the only
  covariant constant lines.
- **B1640** §2: the near-fixed-point regime named as uncomputed (the origin of P-153). **B1630**: T-TAU-ONLY-PERMUTATION.
- **B1654**: D(τ), the canonical end condition, and its §0b exploration `two_defects` (the a-side and v-side at one τ).
- **The SM seat's W87** (its branch, 37a5c5924): c_r = −2π ln((π/2)∣θ_r(0)∣²) and D(τ) = −θ₃⁴h(λ)/(4πη⁶),
  h(λ) = λ ln∣λ∣ + (1 − λ) ln∣1 − λ∣, zero exactly on ω's orbit; post hoc, the slope at ω, (π²√3/6)∣θ₃(ω)∣⁴ = 2.9491720,
  in every direction. Main checked D against B1654's stored values (1.3 × 10⁻¹⁴) and the slope against its own
  exploration.
- **Literature:** P is the standard Γ(4) ≅ S₄ triplet's order-3 element (the near-fixed-point mechanism of Novichkov,
  Penedo and Petcov, cited by B1640); isotropic vectors in ℂ³.

**What this arc adds:** R(ω) and R̄(ω) as P's isotropic eigenlines; the v-side defect with coefficient one in the
conjugate vacuum; the parallel vacuum's law (the defects' sum and product: a geometric hierarchy), which is new; the
two vacua's limits under the canonical end condition; and checks of D's covariance and W87's cone at ω. Nothing here is
claimed as new mathematics.

## 0b. Disclosed

- **Everything the cells read was seen.** Main's exploration (`audit/drafts/sym/`, beside the seal at banking):
  `symmetric_point_explore.py`, `two_defects_explore.py`, `near_omega_explore.py`, `parallel_vacuum_explore.py`. The
  instrument was run from the drafts folder before the seal: v1 twice (the first run failed on two errors of main's
  draft — the determinant's sign and a control threshold — both corrected), v2 twice (every cell held; the second run
  after one diagnostic's construction was corrected, below). **No cell here is blind**, and **the column "seen" replaces
  priors**: no prior is given, because every outcome was seen before the seal.
- **A read-only reviewing agent read v1 before the seal** and found (its scripts beside the seal, `review/`):
  - **a blocker:** the two-defect law holds only in the conjugate vacuum a ≈ R̄, v ≈ R; near a ≈ R the masses go as
    ε and ε². Main then derived and checked the parallel vacuum's law (§1), which v2 seals with cross-controls that pin
    each law to its vacuum;
  - the arc's number inconsistent in the instrument (fixed);
  - incomplete identity labels (S1(d), S2 by B1645's cone, the normalisation control): fixed below;
  - arg κ = π/4 is convention-dependent (R → e^{iχ}R shifts it by 2χ): kept as a read-out, not a cell;
  - D's covariance, D(γτ)(τ + 1) = −D(τ), which forces D(ω) = 0 and kills the holomorphic term: now S5(a);
  - a negative isotropy control (at i and t1 the slope varies with direction) and tighter thresholds: now in S5;
  - the selection of the vacuum by the Higgs's modular weight (§1, a reading); the untwisted scope; precedents.
- **A second read-only reviewing agent read v2 before the seal** (`review2/`): no blocker; it re-derived the parallel law
  by hand and in its own code (a coefficient ½ or 2 instead of ¼ fails the threshold by 7.4 × 10³ and 4.4 × 10³; ±10%
  fails), checked the canonical end condition's two limits and D's covariance to 10⁻³¹ with W87's closed form, and
  asked for the m₂ law's domain, "relative" in S4, the weight reading's frame-dependence, the ½ bound's source and the
  selection rule near ω — all taken in.
- **One diagnostic corrected in the drafts:** S4's "other points of the cone" were first built as combinations of R and
  R̄, which are not isotropic; v2 builds a(s) = R̄ + s n − (s²/2) R, genuine cone points. It is a read-out, not a cell.
- **Identities, not tests (E82; B1655's rule):** S1(c) orthogonality and P³ = −𝟙, S1(d) the eigenvectors (given S1(b)),
  S1(e) the covariance of Y; S2's spectra (B1645's cone theorem for R and R̄, B1645's T4 for n); S3(a), (b); the
  normalisation control in S3; S4(a), the exact zero (a·a = 0); S5(a), D's covariance (a check of the integrator against
  an identity, its sign a convention check). **Tests that can fail:** S1(a), (b), the generic-τ control and the graded control; S2's real-direction
  control; S3's two laws and their two cross-controls; S4(b); S5(b)–(d).

## 1. The setting, and what follows by hand

- **The coupling.** Y(a; v) = a vᵀ + v aᵀ − (a·v)𝟙, a the Higgs's direction in M, v the zero modes' residue triplet:
  v = R under equal framed data (P4′), v_r = √(2πL + c_r)·R_r under equal canonical amplitudes (P4), so v·v = D (B1654).
  R·R = 0 by Jacobi. The defects: d_a = a·a/∣a∣², d_v = v·v/∣v∣² (complex).
- **Identities.** Y(a; v) = Y(v; a); Y a = v(a·a), Y v = a(v·v); det Y = (a·v)(a·a)(v·v).
- **The order-3 move at ω.** γ(τ) = −1/(τ + 1) fixes ω; θ²(γτ) = (τ + 1)·M·θ²(τ); in R's basis M is the real signed
  permutation P = [[0, 1, 0], [0, 0, −1], [1, 0, 0]], PᵀP = 𝟙, P³ = −𝟙. Eigenlines: R(ω) (e^{−iπ/3}), R̄(ω) (e^{iπ/3}),
  n = (1, −1, −1)/√3 (−1). Y(Pa; Pv) = P Y(a; v) Pᵀ.
- **Which line the Higgs takes (a reading, not computed).** P-invariance alone selects nothing: B1646's SO(3) × U(1)
  potential is already P-invariant and keeps its continuous loci. For a Higgs that is a covariant section of weight k,
  its value at ω lies on the eigenline with eigenvalue (ω + 1)^{−k} up to its multiplier: weights 1, 3 and −1 (mod 6)
  give R, n and R̄ (the reviewing agent's check). This assignment is frame-dependent — R = θ²/θ₁′(0) carries θ₁′'s
  multiplier, so the weight given to R is a convention — and the Higgs's weight and multiplier are not computed (P-108).
- **The three symmetric spectra at ω** (B1645): a ∝ n gives (1, 1, 0) (B1645's T4: a real direction gives
  s₂/s₁ ∈ [½, 1], with 1 normal to R's plane — the bound S2's control uses); a ∝ R̄ gives Y = −∣R∣²nnᵀ (∣R∣ = 1), rank one;
  a ∝ R gives Y = 2RRᵀ, rank one. At ω the c_r are equal, so P4 gives v ∝ R and the same spectra.
- **The conjugate vacuum** (∣R∣ = 1, a = R̄ + α, v = R + β). On the light space span{R, R̄} (unitary, bilinear-dual) the
  first-order block is [[0, 2α·R̄], [2β·R, 0]]: **the light masses over the heavy are ∣d_a∣ and ∣d_v∣**, with coefficient
  one.
- **The parallel vacuum** (a = R + α, v = R + β). Y₀ = 2RRᵀ, heavy 2; the light right space {y : R·y = 0} = span{R, n}
  and the light left space span{R̄, n}; the first-order block is diag(0, −(α + β)·R), so s₂ = ∣a·v∣ to first order, and
  s₃ = ∣det Y∣/(s₁s₂) = ∣a·a∣∣v·v∣/2. Since a·v = (a·a + v·v)/2 to first order: **m₂/m₃ = ∣d_a + d_v∣/4 and
  m₁/m₃ = ∣d_a d_v∣/4**, the defects' sum and product (exactly, a·v = (a·a + v·v)/2 − (α − β)·(α − β)/2). One small
  breaking gives ε² : ε : 1, with m₁m₃/m₂² = 4∣d_a d_v∣/∣d_a + d_v∣². The m₂ law needs ∣d_a + d_v∣ ≫ ε²: at a
  cancellation it fails, where the reading as a sum means nothing.
- **Under the canonical end condition** with the Higgs exactly on the line (d_a = 0): one generation exactly massless at
  every τ, and L·s₂/s₁ → ∣D∣/(2π∣R∣²) in the conjugate vacuum, ∣D∣/(8π∣R∣²) in the parallel one. Elsewhere on the cone
  the zero stays and the limit varies.
- **D near ω.** D(γτ)(τ + 1) = −D(τ) (the reviewing agent's identity); at ω the factor is e^{2πi/3}, which forces
  D(ω) = 0 and removes the holomorphic linear term, so ∣D(ω + δ)∣ = ∣κ∣∣δ∣∣R∣² + O(δ²) with ∣κ∣ W87's slope. Under
  δ → e^{−2πi/3}δ a term δ^p δ̄^q survives only if p − q ≡ −1 (mod 3) (the second reviewing agent): δ̄ is allowed and δ
  is not, so the cone's isotropy follows from the covariance and smoothness; δ² is allowed, which is why the spread
  of ∣D∣/δ over directions falls linearly in δ, and the six directions φ = jπ/3 + π/7 cancel its e^{3iφ} in the mean.

## 2. The cells (the instrument `verification/the_symmetric_point.py`; one run; its JSON written after every cell)

| cell | prediction | seen | identity or test |
|---|---|---|---|
| **S0**, plumbing (void) | numpy theta series against mpmath jtheta at six τ < 10⁻¹²; ∣R·R∣/∣R∣² < 10⁻¹³; B1654's stored c_r at ω equal to 10⁻⁹; W87's closed-form D against B1654's stored D at i, t1, t2, t3 < 10⁻¹⁰ | held | gate |
| **S1**, the move | (a) M fitted at four generic τ, residual < 10⁻¹²; (b) M in R's basis equals P to 10⁻¹²; (c) PᵀP = 𝟙 and P³ = −𝟙 exactly; (d) R(ω), R̄(ω), n eigenvectors with e^{−iπ/3}, e^{iπ/3}, −1 to 10⁻¹², n·n = 1; (e) Y(Pa; Pv) = P Y Pᵀ at 20 pairs < 10⁻¹²; **controls:** at τ = 0.13 + 1.07i, R not a P-eigenvector (residual > 0.05); off ω, the eigen-residual of R(ω + δe^{0.7i}) falls linearly (successive ratios in (9, 11) for δ = 10⁻², 10⁻³, 10⁻⁴) | held | (a), (b), the controls tests; (c), (e) identities; (d) a check of convention (the eigenvalues' phases) |
| **S2**, the symmetric vacua | at ω with v = R: n gives (1, 1, 0), R and R̄ give (1, 0, 0), to 10⁻¹²; under P4 at L = 10, 100 the same to 10⁻⁹; **control:** 50 random real directions give s₂/s₁ ≥ ½ | held | the spectra identities (B1645); the control a test |
| **S3**, two laws | (a) symbolically det Y = (a·v)(a·a)(v·v) and Y(a; v) = Y(v; a); (b) the determinant at 100 random pairs to 10⁻¹²; at ω, i, t1 and τ* with a = 2(A₀ + ε_a α), v = 3(R/∣R∣ + ε_v β): (c) **conjugate** (A₀ = R̄/∣R∣, two seeds × 200 draws × 4 τ, ε ∈ 10^[−6, −2]): max ∣(s₂/s₁, s₃/s₁)/(sorted ∣d∣) − 1∣/max ε < 0.05; (d) **parallel** (A₀ = R/∣R∣, two seeds, ε ∈ 10^[−4, −2], above the double-precision floor): the same statistic for ∣d_a + d_v∣/4 and ∣d_a d_v∣/4 < 100 each; **cross-controls:** the conjugate law in the parallel vacuum > 100, the parallel m₂ law in the conjugate vacuum > 100; the normalisation control (unnormalised defects) min over draws > 0.5 | held (0.008; 27.5 and 13.5; cross 9.5 × 10³ and 1.2 × 10⁷; 0.75) | (a), (b), the normalisation control identities; (c), (d), the cross-controls tests |
| **S4**, the canonical end condition | a ∝ R̄(τ) and a ∝ R(τ), v_r = √(2πL + c_r)R_r with B1654's stored c_r, at ω, i, t1, t2, t3 and L ∈ {40, 160, 640, 2560}: (a) s₃/s₁ < 10⁻¹² everywhere; (b) at L = 2560, L·s₂/s₁ within 10⁻³ (relative) of ∣D∣/(2π∣R∣²) (conjugate) and ∣D∣/(8π∣R∣²) (parallel), D by W87's closed form, at i, t1, t2, t3; (c) at ω, L·s₂/s₁ < 10⁻⁸; read-out: three genuine cone points at t1 | held (1.5–1.7 × 10⁻⁴) | (a) identity; (b), (c) tests |
| **S5**, D near ω | (a) D(γτ)(τ + 1) = −D(τ) by the cutoff-free integral at three generic τ, < 10⁻¹⁰ relative; (b) at ω + δe^{iφ}, φ = jπ/3 + π/7 (j = 0…5), the relative spread of ∣D∣/(∣R∣²δ) < 2 × 10⁻³ at δ = 2.5 × 10⁻⁴ and smaller than at 10⁻³; (c) its mean within 10⁻⁵ (relative) of W87's slope; (d) **negative control:** at i and t1 the spread of ∣D(τ₀ + 10⁻³e^{iφ}) − D(τ₀)∣/10⁻³ over φ > 0.1 | held (2.2 × 10⁻¹⁴; 7.5 × 10⁻⁴; 1.6 × 10⁻⁷; 1.38 and 0.70) | (a) identity; (b)–(d) tests |

Overall: PROVED if S0 is not void and S1–S5 hold. A failed cell is reported as the failure of the statement it encodes,
with what the run found stated beside it (E89).

## 3. What it would mean

- At the weave's order-3 point, in the fibre frame, the symmetric Higgs vacua are the three axes of B1646's frame: the
  real one gives the degenerate pair, the two isotropic ones give rank one. **Two laws** say what a small departure
  does: in the conjugate vacuum the two light masses are the two isotropy defects; in the parallel vacuum they are the
  defects' sum and product, a geometric hierarchy from one breaking. Which vacuum is the Higgs's is a question about
  its weight (§1), not computed.
- Under B1654's canonical end condition, with the Higgs on the line, one generation stays massless and the next is
  ∣D(τ)∣/(2πL∣R∣²) or a quarter of it, which near ω is the cone ∣κ∣∣τ − ω∣/(2πL) or a quarter of it.

## 4. What it does not show

- **Which vacuum, which weight, how near the line** the Higgs sits: the Higgs's own defect needs its covariant section
  a(τ) or its potential (B1646's quartic picks a locus; B1655's check of the octic and one-loop terms puts minima
  between). P-153's near-ω regime is answered here for the zero-mode side only.
- **The sectors**: this arc is untwisted. With a hypercharge line R·R ≠ 0 can hold (B1653), and the sectors' twisted
  channels are B1656's.
- **The interacting weave**: one fibre, one τ, the field held fixed. **Any value**, and the Cabibbo angle: at first
  order the untwisted light states are R and R̄ (conjugate) or R and n (parallel).

## 5. Files

`verification/the_symmetric_point.py` (sealed), its JSON and run text after the one run; the exploration scripts, the
reviewing agent's scripts and v1 of this design beside the seal at banking.
