# STEP A v2 — a gauge-consistent, modular-invariant heavy sector on (τ, Ŝ): with tied ratios the one-loop vacuum fixes the Higgs direction from two copies on, by an eigenvector condition rather than a level per coordinate (P-518, P-519; THE FINAL ATTACK, Step A; data-free)

*Main's model-builder, 2026-10-30. A draft in the audit room, not an arc. No measured number is read or compared, and no
file is read by the scripts. 0 of 19.*

## Answer first

**Yes: with tied ratios the interaction's one-loop vacuum fixes the Higgs direction from two heavy copies on, as an
isolated minimum, with one leading free number (μ/M).** This holds in the heavy regime, where each copy's singlet masses
sit above about μ²/e at the vacuum. A copy below that adds a level condition rather than an eigenvector condition, so
more copies are needed, but the tie still compresses. The fix comes from an eigenvector condition, not from B1818's
level-per-coordinate trade.

1. **The construction is consistent** (P-518).
   - n copies of vector-like leptons (L, L̄, E, Ē), with modular-invariant masses M Y_L L L̄ and M Y_E E Ē and a
     gauge-invariant Higgs mixing λ (HᵀY₃) L Ē.
   - The frame's own ρ_R acts on (τ, Ŝ). The triplets are B1730's F_a and DR; the singlets are W150-type cusp forms; the
     exponent equals the weight.
   - One shared M, μ, m₀ and λ (P-519). V is the Coleman–Weinberg sum over the 3n heavy eigenvalues.
   - **Checks:** invariance to 2.5 × 10⁻³³, with four deliberately wrong couplings caught (0.34–2.8). S's phase drops out
     (7 × 10⁻³⁵), so there are six coordinates.
2. **n = 1:** τ is fixed, the direction is not. The vacuum is a CP¹ of directions, exactly flat, of dimension 2, in 20/20
   configurations.
3. **n = 2:** isolated in 17/20.
   - The minimum has zero mixing, Ŝ* = Y₃,₁(τ*) × Y₃,₂(τ*) exactly. λv drops out exactly, and the vacuum moves only with
     μ²/M² (m₀²/μ² at 0.5% of that speed).
   - The free-number rank is 1 on a mirror line (11/17) and 2 off one (6/17).
   - **The three exceptions** have a light copy whose mixed eigenvalue sits at its level (one level condition). They leave
     a one-dimensional valley.
4. **n = 3–8:** isolated in all 119 certified configurations (1 of 120 did not converge).
   - At finite λv the vacuum moves with μ², λv and m₀² (rank 3).
   - In the decoupling limit λv ≪ M (the physical regime) it tends to (argmin of the singlets' potential, the lowest
     eigenvector of Q), Q being the heavy threshold's mass matrix of the three Higgs copies. **So λv drops out for every
     n**, and m₀² moves the vacuum at about 1% of μ²'s speed. One leading free number remains.
5. **The mechanism.**
   - The direction enters only through \|ŜᵀY₃,ᵢ\|², so the one-loop term is a Hermitian form Ŝ†QŜ, and the vacuum
     direction is its lowest eigenvector. That condition spends no level.
   - The vacuum sits where the mass map's rank drops (rank 1–2 at n = 2, against 4 at random points).
   - The untied control reproduces B1818's trade only for τ's conditions.
6. **Where it lands.**
   - Never at i or ω: they are stationary for every parameter but never minima.
   - It lands on a reflection line, or as a mirror pair across one.
   - For some (μ², λv) the potential runs to the cusp.
7. **Which direction.**
   - Menu Z gives new directions, e.g. F₂ × F₆.
   - **Menu H's n = 2 lands exactly on R**, already on record as isotropic (m₁ ≡ 0). The reason: R·R = 0 (Jacobi) and
     R·DR = 0, so R is the zero-mixing direction of the pair (DR, F₂).
8. **The weakest point: the tie and the menu are CHOSEN.**
   - "One shared M and λ" needs a normalisation convention for the forms, which is an untied ratio in disguise.
   - The location, and for n ≥ 3 the direction, move with that convention. The cusp convention pushes the small-n vacua
     deep into the cusp.
   - Nothing on record fixes the convention or the menu (P-415).
   - Close behind: tree-level non-minimal Kähler terms allowed by the same symmetry would compete with the one-loop Q.

**A side finding for main to check:** a₀ = η⁴F₋₂/6 identically (to 10⁻²⁹), so B1810's thirteen declared directions are
twelve (§ 7).

## 0. What failed in B1818, and how each failure is met here

| B1818's blocking finding | here |
|---|---|
| **B1.** A neutral mass and a charged Higgs sat on one bilinear, which is not gauge-invariant, so S's phase became a seventh coordinate. | Vector-like leptons (L, L̄; E, Ē) per copy. The masses M Y_L L L̄ and M Y_E E Ē are diagonal; the Higgs enters only through the off-diagonal mixing λ (Hᵀ Y₃) L Ē, which is gauge-invariant (−½ − ½ + 1 = 0). The singular values of [[a, b], [0, d]] depend on \|a\|, \|b\|, \|d\| only, so S's phase drops out (§2, 7 × 10⁻³⁵). Six coordinates: τ (2) + [Ŝ] ∈ CP² (4). |
| **B2.** The forms were not modular singlets and their weights did not match. | The frame's own monomial ρ_R (W64; B1730 § A) acts on (τ, Ŝ). The triplets are B1730's F_a and DR (weight 3/2); the singlets are cusp forms η^s E₄^p E₆^r, W150's η¹²E₄ among them. The exponent equals the weight throughout. Each copy's eigenvalues are invariant to 2.5 × 10⁻³³, and four deliberately wrong couplings fail at 0.34–2.8 (§2). This is P-367's line (B), a minimised vev, not H-cov (§1). |
| **B3.** "One free ratio per pair" was a choice; the source ties its pairs. | Tied: one M, μ, m₀ and λ for all copies (P-519). The tie's normalisation convention is declared and labelled CHOSEN, and the untied construction is run as the control (§4.4). |
| **B4.** A tree-level potential is another route. | Not computed here. The scope (§6) lists W67's quartic, PF1-W, B1701 and H-cov. This construction is line (B). Its vacuum directions are mostly new; menu H's n = 2 lands on R, a declared direction (§4.6). |

## 1. The construction — its card (WORKING_RULES, the rule of 2026-10-29)

| item | value | label (scope; evidence) |
|---|---|---|
| modular group and action | Mp(2, ℤ), acting on (τ, Ŝ) through ρ_R, projectively by real orthogonal matrices: T: (τ + 1, L⁻¹Ŝ), S: (−1/τ, PŜ), with L⁻¹ the quarter-turn about e_i and P the i–j swap | FORCED within FR-FIB (the frame's multiplier, W64; re-derived from R in B1730 § A). Every pairing below is invariant to 2.5 × 10⁻³³ (§2). |
| the Higgs | one doublet per quaternion unit, H = (H_i, H_j, H_k) ⊗ doublet in ρ_R ⊗ χ (any character: on CP² the action is the same), vev v·Ŝ | ADMITTED (the frame's Higgs lives in ρ′; THE FINAL ATTACK § 4) |
| what is minimised | Ŝ is a free vev (line (B), P-367, kept open by the owner), not a section evaluated at τ (H-cov) | CHOSEN (the construction asked for) |
| heavy content | n copies of vector-like leptons (L, L̄: Y = ∓½; E, Ē: Y = ∓1) | CHOSEN. Nothing on record forces a heavy spectrum (P-415). |
| superpotential of copy i | M Y_L,i(τ) L L̄ + M Y_E,i(τ) E Ē + λ (Hᵀ Y₃,i(τ)) L Ē; no H_u-type L̄ E coupling (§6) | CHOSEN (the minimal gauge-invariant set). A weight and character assignment making every term invariant is exhibited for all 16 copies (`checks_extra.json` § 2). |
| canonical squared masses | a² = M²(2y)^{w_L}\|Y_L\|², d² = M²(2y)^{w_E}\|Y_E\|², b² = (λv)²(2y)^{w₃}\|ŜᵀY₃\|²; charged [[a, b], [0, d]], neutral a | FORCED given the weights (exponent = weight; the control with a wrong exponent fails, §2) |
| the potential | V = Σ over the 3n heavy eigenvalues of F(m²), with F(u) = (u + m₀²)²(log((u + m₀²)/μ²) − 3/2) − u²(log(u/μ²) − 3/2): two complex scalars of mass² u + m₀², one Dirac fermion of mass² u, a universal soft mass, no A or B terms | ADMITTED (W150's mechanism, verified on main, harvest row 1371). F″ = 2 log(1 + m₀²/u) > 0 is checked symbolically (`checks_extra.json` § 1). |
| triplet forms | menu Z: F₂, F₆, F₋₂, F₁₀, F₋₆, F₁₄, F₋₁₀, F₁₈ (B1730's one-unit lines, ordered by \|a\|, then sign); menu H: DR, then F₂, F₆, F₋₂, F₁₀, F₋₆, F₁₄, F₋₁₀ | ADMITTED (the record's sections). Their use as heavy couplings, the two lists and their order are CHOSEN, declared in PLAN.md before the runs. |
| singlet forms | copy i takes the pair (2i − 1, 2i) of: η¹²E₄ (W150's), η¹²E₆; η²⁰, η²⁴; η⁸E₆, η¹⁶E₄; η⁸E₄², η²⁰E₄; η¹⁶E₆, η¹²E₄²; η⁸E₄E₆, η²⁴E₄; η²⁰E₆, η¹⁶E₄²; η¹²E₄E₆, η⁸E₄³. These are cusp forms with s ≥ 8, weights 10–16, characters χ_η^s. | ADMITTED (W150's family and its η-twists); the list is CHOSEN (PLAN.md) |
| the tie | one M, μ, m₀ and λ for every copy | CHOSEN (P-519; the source ties its two pairs) |
| the tie's normalisation | primary: each singlet divided by its sup norm (max (2y)^w\|Y\|² = 1); F_a divided by 2^{a/3} (N(F_a) = iη⁹, the family's defining invariant); DR cusp-normalised (24·DR). Alternative run as a check: cusp normalisation for every form | CHOSEN. Without a convention "one shared M and λ" is undefined, since a form's normalisation is an untied ratio in disguise (§6). |
| the free numbers | μ²/M² ∈ {0.3, 0.5, 0.8}, m₀²/μ² ∈ {0.01, 0.1}, λv/M ∈ {0.1, 0.3, 1.0} | CHOSEN (M is the unit). How the vacuum moves with each is computed (§4). |
| the Higgs copies' tree-level masses and Kähler potential | universal (∝ I) and minimal | CHOSEN (the only invariant τ-independent choice, since ρ_R is irreducible). Non-minimal Kähler terms allowed by the same symmetry are not included (§6). |
| \|v\| | held fixed | CHOSEN (N10 of B1818's referee) |
| outputs | the vacuum's dimension and the number of free numbers that move it; no value, none of the 19 | FORCED within this construction (computed) |

## 2. Consistency checks (`step_a_v2.py` A, B, C; `checks_extra.py`)

- **A. Invariance.** Every copy's three eigenvalues (both menus, all 16 copies, three random points, 34 digits) are
  unchanged under T: (τ + 1, L⁻¹Ŝ) and S: (−1/τ, PŜ) to 2.5 × 10⁻³³ (menu Z) and 2.4 × 10⁻³³ (menu H).
  - The mirror (τ, Ŝ) → (−τ̄, D conj Ŝ), with D = diag(1, 1, −1), preserves them exactly.
  - **Positive control:** W150's η¹²E₄ with exponent 10 passes at 9 × 10⁻³⁴.
  - **Controls that must fail, and do:**
    - B1818's θ₃^{2m} singlet: 0.81;
    - a triplet with permuted components: 0.64;
    - F₆ with exponent 2 instead of 3/2: 0.34;
    - B1818's additive coupling (M Y + λ S·Y₃ on one bilinear): 2.79.
- **B. The phase.** The eigenvalues at e^{iα}Ŝ equal those at Ŝ to 7.2 × 10⁻³⁵ (three phases, four points, all 8 copies of
  menu H). The control, B1818's additive coupling, moves by 4.6%, 30% and 81% at the same phases.
  - **Why.** S → e^{iα}S is a hypercharge rotation. It multiplies b by e^{iα}, and L or Ē absorbs the phase. The singular
    values of [[a, b], [0, d]] are fixed by \|a\|² + \|b\|² + \|d\|² and \|ad\|.
- **C. The rank of d(log m²) on the six coordinates at 12 random points.** It is min(n + 2, 6) for every n = 1–8 in both
  menus.
  - Two finite-difference steps agree, and the smallest kept singular value is ≥ 2 × 10⁻⁴ (threshold 10⁻⁹).
  - The singlets give τ's two directions; each copy adds one CP² direction until there are four.
  - **Control:** one shared triplet for every copy caps the rank at 3 (n = 1, 2, 4, 8). The test can fail.
- **Extra checks:**
  - an explicit weight and character assignment (k_H = 0, χ_H trivial) makes every term of all 16 copies invariant;
  - the cross product of two triplets is covariant: (Y₁ × Y₂)(γτ) ∝ O(γ)(Y₁ × Y₂)(τ) exactly, with weight-3 norm
    invariant to 2 × 10⁻³¹;
  - u* ≡ argmin F = 0.995 μ² at m₀² = 0.01 μ², and 0.950 μ² at 0.1 μ².

## 3. The structure (derived; each step checked by the computation in § 4)

1. **The direction enters only through n numbers.** V(τ, Ŝ) = Σᵢ Φ(aᵢ², dᵢ², (λv)²βᵢ), where
   βᵢ = (2y)^{w₃}\|ŜᵀY₃,ᵢ(τ)\|² and Φ = F(a²) + F(σ₊²) + F(σ₋²).
   - Φ is smooth, since it is symmetric in σ±², the roots of x² − (a² + b² + d²)x + a²d².
2. **The leading order in λv.** V = V₀(τ) + (λv)² Ŝ†Q(τ)Ŝ + O((λv)⁴), where
   Q(τ) = Σᵢ cᵢ (2y)^{w₃} conj(Y₃,ᵢ)Y₃,ᵢᵀ and cᵢ = (G(aᵢ²) − G(dᵢ²))/(aᵢ² − dᵢ²), with G(x) = xF′(x).
   - **The reading.** Q is the heavy threshold's contribution to the 3 × 3 mass matrix of the three Higgs copies. At fixed
     τ the vacuum direction is its lowest eigenvector: the combination that stays lightest.
   - cᵢ > 0 when the copy's masses lie above about μ²/e (G′ ≈ 2m₀²(1 + log(x/μ²))).
   - It is positive for every copy at all 17 isolated n = 2 vacua. Light copies (cᵢ < 0) occur in the three n = 2
     exceptions and at 50 of the 119 n ≥ 3 vacua (§ 4.1).
3. **Zero mixing (cᵢ > 0).** The minimum over Ŝ switches off as many mixings as it can.
   - **n = 1:** {Ŝ : ŜᵀY₃,₁(τ) = 0} is a projective line CP¹, two real dimensions, exactly flat (V = V₀(τ) on it, to all
     orders).
   - **n = 2:** Ŝ* ∝ Y₃,₁(τ) × Y₃,₂(τ), one point.
     - V = V₀(τ) exactly there, so **λv drops out exactly** and τ* = argmin V₀.
     - The minimised vev reproduces a covariant holomorphic section of weight 3, the cross product. Line (B) lands on an
       H-cov-type section, at weight 3.
   - **n ≥ 3:** a common zero needs det[Y₃,₁ Y₃,₂ Y₃,₃](τ) = 0.
     - For menu Z this holds at τ = i: every F_a(i) is P-even, and (1, −1, 0)/√2 is orthogonal to all of them.
     - Elsewhere the direction is Q's lowest eigenvector.
4. **The vacuum sits where the mass map's rank drops.** At zero mixing every d(bᵢ²) vanishes, since bᵢ² ≥ 0 is at its
   minimum. On a mirror line every invariant's gradient is tangent to the line.
   - So the n = 2 vacuum has rank 1 or 2, not 6, and it is isolated through the second-order structure.
   - **This is why B1818's count does not apply.** That count ("each condition a level, each level a free number") is a
     regular-value count. Here the direction is fixed by an eigenvector condition, which spends no level.
5. **The symmetric configurations.** At (i, (1, −1, 0)/√2) and at (ω, an eigenvector of PL⁻¹), the stabiliser acts on
   the whole six-dimensional tangent space with no fixed vector.
   - Every invariant V is stationary there, for every parameter value (B990's law in this mechanism; B1818's referee,
     B4 (iv)).
   - Whether they are minima is computed (§ 4.3).
6. **The mirror.** Its fixed loci are Re τ ∈ {0, ±½} or \|τ\| = 1, with Ŝ in an RP²: three real dimensions. A unique
   minimum lies on one of them; otherwise minima come in mirror pairs (spontaneous breaking of the mirror).

## 4. Results

### 4.1 The vacua (`step_a_v2.py` D; 176 configurations, 24 seeded starts each, refined at 34 digits; `summary.txt`)

The grid has 9 primary points (μ² × λv), one m₀ check (m₀² = 0.1 μ²) and one convention check per (menu, n). Each
interior minimum is refined by Newton to a gradient ≤ 10⁻²¹, except where stated. The classes follow `summarize.py`'s
refined criteria (§ 8 explains why they refine the plan's).

| n | primary convention, both menus (20 configurations per n) | the vacuum's direction | free numbers that move it (rank of dx*/d(log μ², log m₀², log λv)) |
|---|---|---|---|
| 1 | **flat valley of dimension 2** in 20/20 | a CP¹ at zero mixing (b² ≤ 5 × 10⁻³⁰). The valley follow moves Ŝ by 0.050 and 0.197 (Fubini–Study) at \|ΔV\| ≤ 10⁻³⁴, with τ unmoved, in all 20. τ* is fixed, at the singlets' joint level point when that exists (μ² = 0.5: V = 3F(u*) to 3 × 10⁻¹⁴) | — (τ* moves with μ) |
| 2 | **isolated** in 17/20 (Hessian min/max 8.8 × 10⁻⁴ – 1.9 × 10⁻²); **flat valley of dimension 1** in 3/20 (menu Z at μ² = 0.3) | zero mixing in all 17 (b² ≤ 1.3 × 10⁻³⁰, every cᵢ > 0): Ŝ* = Y₃,₁ × Y₃,₂ at τ* (Fubini–Study 0 to the 1.5 × 10⁻⁸ floor of the arccos) | **1** on a mirror line (11 of 17), **2** off one (6). λv's speed is 10⁻¹⁶ – 3 × 10⁻¹⁴ (exactly absent); μ²'s 0.017–0.46; m₀²'s 8 × 10⁻⁵ – 2 × 10⁻³ |
| 3 | **isolated** in 19/20 (one of them lies above a runaway to the cusp, Z at μ² = 0.3, λv = 1); 1 unconverged (H at μ² = 0.3, λv = 1: Im τ = 3.6, nearly flat in Re τ, gradient 10⁻³) | Q's lowest eigenvector, corrected at order (λv)⁴ | **3** |
| 4–8 | **isolated** in 100/100 (min/max 5 × 10⁻⁵ – 0.1) | the same | **3** in 99 of 100 (one 2). Over n = 3–8 (118 vacua), per unit log: μ²'s speed 0.009–3.8; λv's median 0.5 of μ²'s (0.009–9.3); m₀²'s median 1.1% of μ²'s (0.05–11%) |

- **Where the vacua land.**
  - **n = 2:** on Re τ = ±½, with Ŝ mirror-fixed (11), or off every mirror line (6: e.g. τ* = 0.405 + 1.231i at
    μ² = 0.8), as a mirror pair.
  - **n ≥ 3:** on Re τ = ±½, Re τ = 0 or \|τ\| = 1 (about half), or off them (spontaneous mirror breaking, increasingly with
    n).
  - **Never at i or ω.**
- **The rank of the mass map at the vacuum is low, as § 3.4 predicts.** On the invariants (a², d², β̂):
  - n = 1 and n = 2: rank 1 or 2, at all 40;
  - n = 3–4: 3–5;
  - n ≥ 5: 3 or 6.

  At random points it is min(n + 2, 6). The n = 2 vacua are isolated at rank 1–2.
- **The three n = 2 exceptions are the light-copy regime.**
  - Copy 2's singlets (η²⁰, η²⁴) are far below the level at the vacuum's Im τ = 2.65, so c₂ = −0.030 < 0.
  - Its mixed eigenvalue then sits at the level, b₂²/u* = 0.998: an interior level condition, one real condition whose
    value λv sets.
  - With copy 1's zero mixing (two conditions), CP² keeps one flat direction. V is constant to 10⁻³⁶ along it.
  - This is B1818's level-set count, back for one copy. Its level comes from the shared λv, so the tie still compresses,
    but two copies no longer suffice.
- **Light copies elsewhere.** 50 of the 119 certified n ≥ 3 vacua have at least one copy with cᵢ < 0.
  - There are 82 such copies. 52 of them sit within a factor 2 of their level; the rest range from bᵢ²/u* = 0.003 to 4.6.
  - All 50 vacua are isolated: the other copies supply the missing conditions.
- **n = 2's numbers.** m₀²'s speed is a median 0.46% of μ²'s (0.43–4.8%). λv's is a median 3 × 10⁻¹⁴ of μ²'s, zero to
  precision.

### 4.2 The convention check (cusp normalisation for every form; one configuration per menu and n)

- **n = 1:** unconverged deep in the cusp (Im τ 4.12, gradient ≤ 10⁻⁸, two noise-level eigenvalues): the CP¹ again.
- **n = 2:** Z unresolved (two noise-level eigenvalues; copy 2 at its level, b₂²/u* = 1.00); H unconverged at
  Im τ = 4.12.
- **n = 3:** a runaway in both menus (their interior minima isolated); **n = 4:** a runaway in H.
- **n ≥ 4–5:** isolated.

So the convention moves the vacuum (here deep into the cusp) and changes which copies are light. That changes how many
copies are needed, not the mechanism.

### 4.3 The symmetric configurations (`step_a_v2.py` H; menu Z and H, n = 1–8, at μ² = 0.5, λv = 0.3)

- **Stationary for every n, as § 3.5 says:** the gradient is ≤ 3 × 10⁻²⁰ at (i, (1, −1, 0)/√2), and ≤ 3 × 10⁻¹⁶ at the
  three (ω, eigenvector of PL⁻¹), limited by the eigenvectors' double precision.
- **None is a minimum** (64 of 64 have a negative or zero Hessian direction).
- **None is the vacuum:** V there exceeds the global minimum by at least 6.2 × 10⁻³.
- In menu H, (i, (1, −1, 0)/√2) is DR's own direction at i, where DR's mixing is maximal and V is high.
  - DR(i) ∝ (−1, 1, 0) was computed at 30 digits. Its weight-3/2 automorphy factor makes it P-odd, while every F_a(i),
    R(i) and a₀(i) is P-even.
- **The mass map's differential vanishes there** (`analysis_points.py`; menus Z and H, n = 2, 4, 8, at all four points).
  - The smooth invariants (a², d², b²) have a raw Jacobian of rank 0: singular values ≤ 10⁻²¹ at i, and ≤ 2 × 10⁻¹⁵ at
    ω (limited by the eigenvectors' double precision). One step off the point (τ + 0.01 + 0.02i) the rank is 4–6.
  - The individual eigenvalues show a residual rank 1 at some ω points. Every such case is a copy with a² = d² at zero
    mixing, where √((a² − d²)² + b²(…)) is a cone and the eigenvalues are not differentiable.
    - Copy 2's sup-normalised η²⁰ and η²⁴ both peak at ω, with value 1.
    - Copy 4's two E₄-singlets both vanish there.
  - These points carry 1–13 massless heavy states (E₆(i) = 0, E₄(ω) = 0 kill the singlets with those factors). Since
    F(0) > F(u*), this is part of why they are not minima.
  - **An artifact disclosed:** a first version used d(log m²), which is singular at a massless state, and read rank 1–4
    there (kept as `analysis_points_logjac_superseded.json`).

### 4.4 The untied control (`step_a_v2.py` G: per-copy μᵢ, M_L,i, M_E,i, every singlet planted at its own u*ᵢ at a random τ_p)

- **n = 1 (two trials):** the vacuum is the joint level set (V − bound = 3 × 10⁻¹⁶). There are two flat directions, the
  CP¹. τ is fixed by the two singlet levels, each spending one free ratio.
  - That is B1818's one-condition-one-free-number trade, reproduced, for τ.
- **n = 2:** the joint level set again (\|V − bound\| ≤ 1.4 × 10⁻¹⁶); isolated (min/max 6 × 10⁻⁴, 2 × 10⁻³).
  - The two zero-mixing conditions fix Ŝ = Y₃,₁ × Y₃,₂ and spend no level.
  - τ's four singlet conditions are consistent only because the four levels were planted (two fix τ, two are tuned).
- **n = 3:** the joint level set is empty (V − bound = 8.4 × 10⁻⁴ and 1.2 × 10⁻³). Three triplets have no common zero at a
  generic τ, so the minimum is a compromise; isolated.
- **So in the consistent construction, the trade survives only for the conditions on τ.** The conditions that fix the
  direction are zero-mixing (eigenvector) conditions, free of levels, as long as the copies are heavy (§ 4.1's exceptions).

### 4.5 The decoupling limit and the free numbers (`step_a_v2.py` F; `analysis_leading.py`)

- **n = 1, 2: the exact vacua equal the leading-order prediction exactly** at λv = 0.1, 0.03 and 0.01, in both menus
  (distance 0). This is (τ₀* = argmin V₀, and Q's null vector Y₃,₁ × Y₃,₂).
- **n ≥ 3: the exact vacua converge to (τ₀*, Q's lowest eigenvector) as (λv)².**
  - Menu Z, n = 3: τ moves 8.0 × 10⁻⁴, 7.3 × 10⁻⁵, 8.1 × 10⁻⁶ (hyperbolic) and Ŝ 1.6 × 10⁻³ → 2.7 × 10⁻⁷ at
    λv = 0.1, 0.03, 0.01.
  - Menu Z, n = 8 converges slowly: Q has a negative eigenvalue there (a light copy).
  - **So for λv ≪ M, the physical regime, λv drops out for every n.**
- **The decoupling-limit vacuum** (`analysis_leading_{Z,H}.json`, μ² = 0.5, m₀² = 0.01 μ²).
  - Q's lowest eigenvalue is simple for every n ≥ 2: the gap ratio (e₂ − e₁)/e₃ is 0.13–0.52 in menu Z and 0.008–0.44
    in menu H. So Ŝ* is isolated.
  - n = 1 has a double zero (gap 10⁻¹⁶): the CP¹.
  - The speeds per unit log μ², n = 2–8: τ* moves 0.014–0.33 (hyperbolic) and Ŝ* 0.010–1.16 (Fubini–Study).
  - **m₀².** At leading order in m₀²/u, F ≈ 2m₀²u(log(u/μ²) − 1), so both V₀ and Q are m₀² times functions of μ² alone,
    and m₀² drops out of the decoupling-limit vacuum at that order. Its residual effect is quoted from D's exact
    derivatives (§ 4.1: 0.46% of μ²'s at n = 2, 1.1% at n ≥ 3).
  - **One search miss, disclosed.** Menu H's n = 1 τ₀* (2.362i) is a local minimum the 8-start search settled in:
    V₀ = −0.01428, against −0.01500 at menu Z's 0.4304 + 1.1782i, with identical singlets. D's 24-start grid finds the
    global one in both menus. For n = 2–8 the two menus' τ₀* agree.
- **The n = 2 vacuum along μ²** (menu Z; `analysis_leading_scan.json`, 16 values; the zero-mixing branch τ* = argmin V₀,
  Ŝ* = F₂ × F₆ at τ*). It traces a curve with one free number.

  | μ²/M² | τ* | the branch |
  |---|---|---|
  | 0.30 → 0.65 | ½ + i(1.2534 → 1.2397) | on the mirror line Re τ = ½, Ŝ* mirror-fixed, moving slowly (its components shift by about 0.01) |
  | ≈ 0.70 | 0.478 + 1.238i | a pitchfork: the line minimum gives way to a mirror pair |
  | 0.70 → 0.95 | (0.478 + 1.238i) → (0.358 + 1.220i) | off the line, a mirror pair (spontaneous breaking of the mirror) |
  | 0.20, 0.25 | (Re τ = 0, Im τ ≈ 2.8) | c₂ < 0 there: copy 2 is light, so this branch is not the vacuum (the light regime; compare D's μ² = 0.3 menu Z case) |

  - The grid's exact vacua lie on the branch: −½ + 1.2534i (μ² 0.3, menu H), −½ + 1.2440i (0.5), and 0.4053 + 1.2306i
    (0.8; scan 0.4053 + 1.2306i).

### 4.6 What the vacuum direction is (`analysis_vacua.py`; `checks_extra.py` § 4)

The vacuum direction Ŝ* is compared with each declared direction evaluated at the same τ* (DR, R = F₂, a₀ = F₋₂, F₋₁₀ …
F₂₆):
- **Menu Z:** new. 1 − \|⟨Ŷ, Ŝ*⟩\| ≥ 2.5 × 10⁻³ over every vacuum, typically 0.05–0.4. F₂ × F₆ is proportional to no
  declared direction at the three τ tested (smallest 7 × 10⁻³).
- **Menu H, n = 2: exactly R's direction, Ŝ* ∝ R(τ*)** (1 − overlap ≤ 2 × 10⁻¹⁶ at all 10). The reason:
  - R is isotropic: RᵀR = (θ₂⁴ + θ₄⁴ − θ₃⁴)/(θ₂θ₃θ₄)² = 0 by Jacobi's identity.
  - Hence R·∂R = ½ D(R·R) = 0.
  - So R is bilinearly orthogonal to both DR and F₂ ∝ R, and the zero-mixing direction of the pair (DR, F₂) is R itself.

  R is on record as an isotropic direction with m₁ ≡ 0 at every radius (B1809, Table T). This vacuum therefore lands on a
  known, degenerate direction, at a τ* set by μ/M.
- **Menu H, n ≥ 3:** new. 1 − overlap from 10⁻⁵ (n = 3, near F₂) to 0.23.

## 5. What it establishes, and what it does not

**Establishes (within this construction, data-free; labels FORCED within the construction, by the computation of § 4):**
- **A consistent construction exists** (P-518's four demands): gauge-invariant couplings, modular invariance with the
  exponent equal to the weight on the frame's own ρ_R, S's phase absent, six coordinates.
- **P-519's count, with tied ratios.**
  - The one-loop vacuum on (τ, Ŝ) is a CP¹ for one copy, and isolated from two copies on in the heavy regime (n ≥ 3 in
    the light-copy cases computed).
  - The direction is fixed by an eigenvector (zero-mixing) condition of the threshold matrix Q.
  - The free numbers that move it: μ²/M² at leading order; m₀²/μ² at about 1%; λv/M only for n ≥ 3 away from the
    decoupling limit.
  - So six coordinates are fixed by one leading number plus a discrete menu: compression, as B1818's referee anticipated
    (B3), but already at n = 2 and by a different mechanism.
- **B1818's surviving count is located.** "Each condition a level, each level a free number" holds for the conditions on
  τ (the singlets) and for light copies' level conditions. It does not hold for the zero-mixing conditions, which fix the
  direction.
- **The symmetric configurations are stationary but not the vacuum** (B990's law in this mechanism).
- **P-139's demand is met only partly.** P-139 asks for "a dynamics that lands at a computable non-symmetric point". The
  vacua off the reflection lines are such points, but they are computable only given a CHOSEN heavy menu and the value
  of μ/M.

**Does not establish:**
- **That the object, or FR-FIB, contains this heavy sector,** its menu, its copy count, its tie or its normalisation
  convention. All are CHOSEN (P-415).
- **That Ŝ* is our world's Higgs direction.** Nothing is compared. The identification of the minimised vev with the
  frame's Higgs (line (B) read as the frame's direction; singular values as masses) is UNEARNED.
- **Stability beyond one loop;** robustness to non-minimal Kähler terms; the electroweak scale; a two-Higgs (H_u, H_d)
  completion.
- **Whether line (B) is to be preferred to line (A)** (H-cov). It is not. Menu H's n = 2 vacuum shows the two can meet:
  the minimised vev lands on the covariant section R.
- **Any description length** (P-418).
- **Points not certified:** the cusp-convention n = 1 and 2 vacua (deep in the cusp, gradient 10⁻⁸–10⁻¹⁰), and one
  primary n = 3 configuration (Im τ = 3.6, gradient 10⁻³).

**For THE FINAL ATTACK.**
- Step A now has a vacuum: for each menu, a curve of rigid addresses (τ*(μ/M), Ŝ*(μ/M)), traced by one leading free
  number.
- Before it can enter Step B's card, "the Higgs from Step A's vacuum" needs:
  - the menu's pricing (which forms, how many copies, which convention);
  - the decision whether μ/M is FITTED (a continuous value set by data) or swept;
  - main's check of the light-copy regime.
- The prior THE FINAL ATTACK attached to Step A's vacuum (PASS ≤ 10%) assumed a vacuum fixed by the object. This vacuum
  is fixed by a chosen sector, and that prior should be reconsidered with it.
- **0 of 19.**

## 6. Scope, and the construction's weakest point

**The weakest point: the tie and the heavy menu are CHOSEN, and the tie is convention-laden.**
- **The tie needs a convention.** "One shared M and λ" means something only once each form's normalisation is fixed, and a
  form's normalisation is a free ratio in disguise. With the forms' own invariant norms (the singlets' sup norm, the zero-
  free family's N(F_a) = iη⁹) the direction is fixed by one leading number. With the cusp normalisation instead, the vacuum
  moves, and for some copies the regime changes (§ 4.2).
- **What does not depend on it.** The n = 2 direction, given τ*, is convention-free (the cross product). Its τ*, and every
  n ≥ 3 direction, are not.
- **Nothing on record fixes the convention, the forms, the copy count or the tie** (P-415: no object-forced heavy spectrum).
  "One free number" therefore holds modulo a discrete menu that this page does not price. P-418's generator would price it.

**Close behind: the Kähler ambiguity.**
- The direction is selected by Q, a one-loop effect of size (λ²/16π²)·m₀²·log.
- Tree-level non-minimal Kähler terms for the Higgs copies, e.g. κ (2y)^{w}|Y(τ)ᵀH|², are allowed by the same modular
  symmetry. They would add a competing τ-dependent Hermitian form.
- Minimal Kähler and universal soft masses for the copies are CHOSEN here. ρ_R is irreducible, so a universal,
  τ-independent form is the only invariant one; τ-dependent forms are not excluded.

**Not established:**
- **Higher loops,** and the two-loop stability of the eigenvector selection.
- **That the frame contains these heavy states.** It does not, on record; they are added by hand (P-415's towers are the
  candidate source).
- **The identification of Ŝ with the frame's Higgs direction.**
  - The vacuum is a minimised vev (line (B)). Reading its direction as the Higgs of FR-FIB's Yukawa, and the frame's
    singular values as masses, are identifications (UNEARNED; I-33-type, P-516's class).
  - For n = 2 the direction is a covariant section at weight 3 (Y₁ × Y₂), outside H-cov's weight-3/2 proofs.
- **The electroweak scale.**
  - \|v\| is held fixed.
  - The heavy thresholds give the Higgs copies masses of order λ²m₀²log/16π² (the eigenvalues of Q). The light Higgs as
    Q's lowest eigenvector is natural, but its lightness needs one tuning (the usual hierarchy problem), which is not
    addressed.
- **Two Higgs doublets.**
  - Only an H_d-type mixing λ H L Ē couples. In a supersymmetric completion, an H_u L̄ E coupling would make the
    determinant depend on the relative phase of the two vevs, a seventh, gauge-invariant coordinate.
  - H_u's own direction would need its own heavy couplings.
- **Other routes to the direction** are not compared here: W67's quartic (harvest row 1127), PF1-W (B1730, B1731), W63's
  line tie (B1701), H-cov's covariant sections (line (A)).
- **The rest of the τ-potential:** the light fields' one-loop terms, the supergravity terms and D-terms. As in W150's
  source, only the heavy states' Coleman–Weinberg term holds τ.
- **The description length.** Not computed. The counts are given; their pricing is P-418's.
- **0 of 19:** no output of the frame is computed at the vacuum, and nothing is compared with data.

## 7. A side finding for the record: a₀ = η⁴F₋₂/6 identically, so B1810's thirteen directions are twelve

- **The identity.** B1697's a₀ = ∂²R − E₄R/48 (weight 7/2, ρ_R untwisted) equals η⁴F₋₂/6, where B1730's F₋₂ =
  η⁵(θ₂⁻², θ₄⁻², iθ₃⁻²).
  - **Computed** (`checks_extra.json` § 5): the component ratios a₀ₖ/(η⁴F₋₂,ₖ) equal 1/6 to 1.5 × 10⁻²⁹ at six τ, with
    holomorphic η.
  - **Why.** η⁴F₋₂ has weight 2 + 3/2 = 7/2 and character χ_η^{4 + 20} = 1, the same as a₀. Each ratio is holomorphic,
    since F₋₂ is zero-free (B1730), and is permuted by the monomial ρ_R. So it is a Γ(2)-invariant function bounded at
    the cusps, hence constant.
- **The record had it only at i.** B1809 (Table T: "equal to F₋₂ at i") and B1810 (§ 2.3: "a₀ has κ = 2^{−1/2} (= F₋₂)")
  state the equality at τ = i only.
- **The consequence.** As directions, a₀ and F₋₂ are one direction at every τ.
  - B1810's DIRS lists both. Its table's a₀ and F₋₂ rows (64 each) agree in every mass ratio to 1.6 × 10⁻¹⁶. The |V|
    cells differ (up to 0.021) only in the 24 rows where B1810 itself marks V undefined (degenerate sectors).
  - So the "thirteen declared directions" of P-495's fallback are twelve distinct ones. This touches the direction
    menu's pricing and the rigid-direction census, which carries duplicate rows if it ran both. It needs main's check
    before any card uses the count.

## 8. Disclosed

- **Before the plan.** Prototypes `proto1`–`proto5` (scratchpad) preceded PLAN.md:
  - the forms' checks, during which mpmath's `jtheta(2, 0, q)` was found to take the principal branch of q^{1/4}, wrong
    for Re τ outside (−1, 1); θ₂ is now summed in τ;
  - the scale table, which set the normalisation conventions;
  - one exploratory search (menu Z, n = 1–4, one parameter point, 12 starts).
- **After the plan, before the main runs** (each change re-hashed in ARTIFACT_HASHES.txt):
  - the eigenvalue discriminant written in its manifestly non-negative form, (a² − d²)² + b²(2a² + 2d² + b²); the
    subtracted form went negative by roundoff at the degenerate n = 1 vacuum;
  - per-copy levels, for the untied control;
  - the invariant Jacobian (a², d², β̂), since individual eigenvalues are not smooth where a = d and b = 0;
  - the valley follow for flat cases;
  - the mirror check at Re τ = −½;
  - the phase test applied in mpmath (the double-precision version read 2 × 10⁻¹⁶, its own rounding).
- **The first launch of D crashed.** A BFGS line search stepped to Im τ ~ 10³, where (2y)^w overflows, and the error
  aborted the pool before any D output was written. Its log is kept: `step_a_v2_run_D_crashed_overflow.txt`.
  - **The fix:** a soft wall at Im τ > 40 after reduction, per-start error trapping, and runaways (Im τ > 6) recorded
    apart from the refined interior minimum.
  - **The relaunch** ran the whole declared grid from scratch.
- **The plan's flat/isolated criterion** (eigenvalue < 10⁻⁹ × the largest) cannot separate an exactly flat valley from a
  genuine transverse curvature suppressed by e^{−2π Im τ}. The refined classes in `summarize.py` add two tests, and both
  readings are printed:
  - the valley follow (does V stay constant while the point moves?);
  - the two-step stability of the small eigenvalue.
- **Sections F, G and H** ran through `runner_FGH.py` (the same functions) while D owned `step_a_v2.json`. `merge.py`
  merged them afterwards.
- **`analysis_leading.py` was run three times.**
  - The first run used the arccos Fubini–Study distance, which floors at about 1.5 × 10⁻⁸.
  - The second, with a stable 2 arcsin(chord/2), was too slow (20 two-dimensional starts per point).
  - The third split it into three parallel parts with 8 starts. Its n = 2 vacua agree with section D's exact ones.
  - Both partial logs are kept.
  - Its m₀² speeds are below the two-dimensional optimiser's resolution (about 10⁻⁷ in τ for a 2 × 10⁻⁴ step). The m₀²
    dependence is therefore quoted from section D's exact implicit-function derivatives (34 digits), not from it.
- **`analysis_points.py`'s first version** read the log-Jacobian at massless states (§ 4.3). Its second detected only
  fully massless copies. The third detects the general cone a² = d², b = 0, and every residual is explained.
- **The menus share their singlets,** so menus Z and H differ only in their triplets. Their n = 2 vacua coincide in τ*
  wherever both are at zero mixing.
- **The source** (arXiv:2402.02071) was not re-read on this bench. The potential's form is derived here from the
  supertrace, and its convexity is checked symbolically. It agrees with main's verification of W150 (F″ ∝ log(1 + m₀²/u)).
  The "Kähler ambiguity" of modular flavour models (§ 6) is cited from memory as a known issue and was not read here; no
  claim rests on it.

## 9. Seen first

- **The sweep.**
  `VERDICT topic-sweep /vector.like|vectorlike|heavy (lepton|copy|copies|state).{0,60}(Higgs|direction|mixing)|Higgs direction.{0,40}(fix|vacuum|minim)|minimi[sz]ed vev|Coleman.Weinberg.{0,60}(Higgs|direction|section)|cross product.{0,30}(section|F_)/: 25 of 1568 arcs on main match (NEGATIVE 3, PROVED 22); 6 register rows match (DONE 2, QUEUED 4); 13 other lanes match`.
  - The arcs it lists (B865, B895, B944, B953, B978) concern E₆ content and vector-like matter in the 27, not a heavy
    sector selecting a Higgs direction.
  - The rows: P-139 (the selection principle: "the parent needs a dynamics that lands at a computable non-symmetric
    point"), P-325, P-367 (line (B), kept separate by the owner), P-377, P-495, P-518.
- **Read:**
  - B1818's FINDINGS and its referee's REPORT.json (B1–B4, N1–N11) and code (`referee_common.py`, `referee_checks.py`:
    the level-two invariant toy E);
  - STEP_A_DESIGN.md's withdrawal note;
  - main's W150 verification REPORT (§§ 1–7);
  - B1730's FINDINGS and its script's conventions (W64's L⁻¹, P);
  - B1809's FINDINGS §§ 0–5;
  - B1810's card, § 2 and its table JSON;
  - TERMINOLOGY's H-cov;
  - THE_FINAL_ATTACK § 4;
  - register rows P-139, P-367, P-495, P-510, P-518–P-535.
- **Literature:** none searched on this bench beyond what the record's verifications read. The construction uses
  standard pieces: vector-like lepton mass matrices, and the Coleman–Weinberg supertrace with universal soft masses.

## 10. Files (this folder; gitignored, nothing tracked was changed)

- `PLAN.md` (hashed before the main runs) and `ARTIFACT_HASHES.txt` (the plan's and the code's sha256 at each change).
- **The model and the search:** `model.py` (forms, actions, spectrum, potential; numpy and mpmath) and `search.py`
  (menus, normalisations, the search).
- `step_a_v2.py`, the computation, sections A–H. Its output is `step_a_v2.json`, with logs `step_a_v2_run_D.txt`,
  `step_a_v2_run_FGH.txt` and `step_a_v2_run_D_crashed_overflow.txt`.
- **Helpers:** `runner_FGH.py` and `merge.py`.
- `checks_extra.py` → `checks_extra.json`: the convexity, the weight and character assignment, the cross product's
  covariance, F₂ × F₆ against the declared directions, and the identity a₀ = η⁴F₋₂/6.
- `analysis_leading.py Z | H | scan` → `analysis_leading_Z.json`, `_H.json`, `_scan.json`: the decoupling limit, and the
  n = 2 scan in μ². Logs `analysis_leading_run_*.txt`; the two superseded partial logs are kept.
- `analysis_points.py` → `analysis_points.json`: ranks at the symmetric configurations. The superseded
  `analysis_points_logjac_superseded.json` is kept.
- `analysis_vacua.py` → `analysis_vacua.json`: the vacuum directions against the declared ones.
- `summarize.py` → `summary.txt`: the tables of § 4.
- **Run as:** `nice -n 10 env OMP_NUM_THREADS=1 python3 -I step_a_v2.py A B C`, then `... step_a_v2.py D --workers 3`,
  `... runner_FGH.py G H F`, `merge.py`, `checks_extra.py`, `analysis_leading.py {Z,H,scan}`, `analysis_points.py`,
  `analysis_vacua.py`, `summarize.py`.
  - Environment: Python 3.12.1, numpy 2.4.0, scipy 1.16.3, mpmath 1.3.0.
  - At most four cores. The grid took 18.5 minutes on three workers; its crashed first launch ran longer.
