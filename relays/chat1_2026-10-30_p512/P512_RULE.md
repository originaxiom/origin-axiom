# P-512, THE QUARTER RELATION OF THE LINE CONSTANTS — the rule, written before the check script

chat1 (the web seat), 2026-10-30, at main's offer ("an attempt at P-512's derivation"). Data-free: no Standard Model value is
read or compared. The frame's own outputs are the only numbers used. 0 of 19.

**What P-512 asks** (POINT_REGISTER, 2026-10-30): "the frame's two non-integer cusp lepton/down constants satisfy R₂(1/8) =
4·R₂(3/8) exactly (3.4298922 against 0.8574731, ratio 4 to 10⁻⁸ in two codes) — the same 4 as the family limits (4, ¼);
neither seat stated it; an explanation from B1788's pole blocks is owed". Its next step: "derive the relation from the four
blocks; check whether every cusp constant is 4^k times a few".

Here R₂ = (m₂/m₃)_leptons / (m₂/m₃)_down on B1656's frame through B1726's `compute` (B1817's definition), m₂/m₃ = σ₂/σ₁
of the coupling Y.

## 0. What was explored before this rule (labelled; below the gate, data-free)

The derivation below was found by exploration in a scratch directory. It used main's modules unchanged, at main's
5e5e75ac4.
- **Read:** B1817's FINDINGS, and its committed rows at α = 1/8 and 3/8 only, at N_c = 3; B1788's FINDINGS and
  `blocks.py`; `b1656_funcs.py`; B1726's `compute`.
- **Computed:**
  - R₂ on 1/8 and 3/8 at b = 0, 0.137 and 0.311 (Re τ = ⅓, Im τ = 10);
  - the identities of § 1 (D3) at b = 0, at Im τ 2.5 and 6;
  - the formula of D4 at Im τ 10 for those three b;
  - x's closed form (D5) at b = 0, Im τ 8–12;
  - |det M₀|'s dependence on b_x + b_y at Im τ 10.
- **Worked by hand:** the tie census of D8 (C5's predicted set).

So the cells below are set at points the exploration did not use: random τ and b for C1; Re τ ∈ {0.1, 0.6}, b ∈
{0.05, 0.4} and Im τ = 13 for C2–C4. C6 reads B1817's committed rows on every other slope, which this seat has not read.
The exploration scripts are committed beside this rule, labelled, with their outputs rerun once for the record.

## 1. The derivation (claims D1–D8)

Notation:
- **The twists.** A sector with 6Y charges (q_L, q_R) on the line (α, b) has the characteristics x = (a_x, b_x) =
  (q_Lα, 2q_Lb) and y = (a_y, b_y) = (q_Rα, 2q_Rb) (`sector_twists`).
- **The frame's pieces:** bil(u) is B1656's 2×2 bilinear, r_ij its residues at u = 0 (the four pole blocks), R_s the
  channel residues, c_s the regularised channel norms, w_s = √(2πL + c_s), M = Σ_s w_s R_s E_s^dual (B1726).
- **The coupling:** Y(S; M)_ab = Σ_mn (C_aᵀ ε S C_b)_mn M_mn, with C_a ∈ {QJ, QI, QK} and ε = QJ (`coupling`).

**D1 (exact, every τ, u and b).** The half-shift identities, and full negation:
- bil at a_x + ½ = iε · bil at a_x;
- bil at a_y + ½ = bil at a_y · (−iε);
- bil at (−a, −b) (both chiralities) evaluated at u = −bil at (a, b) evaluated at −u.

They follow from thc(a, b, u + τ, 2τ) = e^{−iπτ/2} e^{−iπ(u+b)} thc(a + ½, b, u, 2τ), from θ₁(u + τ) = −e^{−iπτ}
e^{−2πiu} θ₁(u), and from thc(−a, −b, u, T) = thc(a, b, −u, T). Integer shifts of a are exact symmetries of thc.

**D2 (exact).** Multiplying bil by iε or −iε permutes the channel kernels up to phases (each half-shift swaps 1 ↔ j and
i ↔ k). So the c_s permute and M transforms the same way (M → iεM, M(−iε)). Full negation leaves the c_s and M unchanged.
For U, V ∈ {1, iε, −iε}, Y(S; UMV) has the singular values of Y(S′; M), with S′ = (εᵀUᵀε) S Vᵀ.

**D3 (exact).** With N_c = 3's charges (down (1, 2), leptons (−3, 6)), the four configurations at α = 1/8 and 3/8 reduce to
one a-configuration, (a_x, a_y) = (1/8, 1/4). Write M₀(b_x, b_y) for its M. Then:
- down(1/8, b) has M₀(2b, 4b);
- leptons(1/8, b) have ε M₀(−6b, 12b) ε, since their twists (5/8, 3/4) are the base plus (½, ½);
- down(3/8, b) has iε M₀(−2b, −4b), by negation and then an x half-shift;
- leptons(3/8, b) have M₀(6b, −12b) (−iε), by negation and then a y half-shift.

**D4 (leading order in Im τ).** S's entries are ordered |S₀₁| ≫ |S₀₀| ≫ |S₁₀| (B1788 § 1.3: "S₀₁ at −1/8", "S₀₀ = −S₁₁ at
1/8", "S₁₀ at 3/8"). In Y, S₀₁ multiplies m₀₀ in four entries, m₀₁ and m₁₀ in two each, and m₁₁ in one. The S₀₁² parts of
the 2×2 minors are ±det M or ±i·det M, in four minors. So on the det-M branch (B1788's e(m₂/m₃) < ½):

  σ₂/σ₁ → 2|det M| / Q₀₁(M), with Q₀₁ = 4|m₀₀|² + 2|m₀₁|² + 2|m₁₀|² + |m₁₁|².

For S̃ the large entry sits at (1, 0), and Q₁₀ = 4|m₁₁|² + 2|m₁₀|² + 2|m₀₁|² + |m₀₀|².

**D5 (leading order).** In the base a-configuration, E₀₀ = E₀₁ = −3/64 < E₁₀ = E₁₁ = 5/64 (B1788's block exponents). So
m₀₀ and m₀₁ dominate.
- Their moduli μ = |m₀₀| and ν = |m₀₁| do not depend on b.
- ν²/μ² → x = (2πL + c₁)/(2πL + (c_j + c_k)/2). This uses |r₀₁/r₀₀| → 1, c₁ − c_i → 0 and c_j − c_k → 0.
- |det M₀| depends on (b_x, b_y) only through b_x + b_y.

**D6.** b_x + b_y = 2(q_L + q_R)b, and q_L + q_R = 3 for down (1 + 2) and for leptons (−3 + 6). This is main's P-397 note:
"every sector's pair carries the total charge ±3". So at each slope the two sectors' |det M| coincide (6b on 1/8, −6b on
3/8), and the det-M factor cancels in R₂.

**D7 (the relation).** By D3 the dominant pair (μ, ν) sits at (m₀₀, m₀₁) for down(1/8), at (m₁₁, m₁₀) for leptons(1/8),
at (m₁₀, m₁₁) for down(3/8) and at (m₀₁, m₀₀) for leptons(3/8). So:
- R₂(1/8) = (4μ² + 2ν²)/(μ² + 2ν²) = (4 + 2x)/(1 + 2x);
- R₂(3/8) = (2μ² + ν²)/(2μ² + 4ν²) = (2 + x)/(2 + 4x);
- R₂(1/8)/R₂(3/8) = [2(2 + x)/(1 + 2x)] · [2(1 + 2x)/(2 + x)] = 4, identically in x.

So the relation holds for every L, both horocycles, every b and every Re τ. In S̃, R̃₂ = 1/R₂ on each slope. The 4 is
2 × 2: down(3/8)'s Q₀₁ is half of down(1/8)'s (4μ² + 2ν² against 2μ² + ν²), and leptons(1/8)'s is half of leptons(3/8)'s.

**D8 (the other cusp constants; P-512's second question).**
- **Single dominant entries.** On an equal-exponent slope where each sector's M has a single dominant entry, at the block p
  with the smallest E_ij, R₂ → [mult(p_down)/mult(p_lep)]·ρ. The multiplicities in reading S are mult = 4 at (0, 0), 2 at
  (0, 1) and (1, 0), and 1 at (1, 1); reading S̃ swaps (0, 0) and (1, 1). ρ is the ratio of the det-M and modulus
  coefficients.
- **Ties.** A non-integer limit needs a tie: two dominant entries with equal exponent. Among N_c = 3's equal-exponent
  slopes of order ≤ 30, ties occur only at 1/12, 1/8, 1/4, 3/8 and 5/12. Of these, 1/12, 1/4 and 5/12 are B1817's
  torsion-degenerate slopes.
- **So** the only non-degenerate non-integer constants are on 1/8 and 3/8, which D7 covers.

## 2. The cells (thresholds and priors fixed here)

The instrument is main's code, loaded unchanged from a checkout of main at 5e5e75ac4, with each module's sha256 asserted.
- `b1656_funcs.py`: 31f09c433c14312d9cee8cfa29a632a72ce13fc46ae838757bf9b22958f22528
- `the_exponents.py`: a8d4ea9bae79dde894b192b7c3645685c1c97890665c96123be20ea6e9073aac
- `the_canonical_cusp.json`: 688152749777970f21a85b3278a39ae33884b9ae99623d5eec541f41de34a774
- B1726's `census.py`: 185cf17d8b51c11559bf14650d5ad1dd12745eaa228fc40da0a8b9181d1986bf
- B1817's `a1_cusp_map.jsonl`: 40aa2ef74c789850a9d7c08a2c789fc42849280f11baeff094c26764a02ee4a9

L is read as B1726 reads it (B1667's column at Re τ = ¼, clamped).

| cell | what is computed | passes when | prior |
|---|---|---|---|
| **C1** exact identities | D1 at 8 random u (0.05 < \|u\| < 0.3) on 6 random points (Re τ ∈ (0, 1), Im τ ∈ [1.5, 4], b uniform in (0, 1)); D3's three reductions there: singular values of Y(S; M_config) against Y(S′; M₀) at the mapped b's, both readings, both horocycles; the c_s permutations | every relative deviation < 1e-10 for D1, < 1e-8 for D3 and the c_s | 97% |
| **C2** the leading formula | σ₂/σ₁ against 2\|det M\|/Q (Q₀₁ in S, Q₁₀ in S̃) for the four configurations at Re τ ∈ {0.1, 0.6}, b ∈ {0.05, 0.4}, Im τ = 13, both horocycles: 64 values | every \|ratio − 1\| < 1e-5 | 95% |
| **C3** the relation | R₂(1/8)/R₂(3/8) in S and in S̃; R₂·R̃₂ on each slope; at C2's 8 (Re τ, b, horocycle) points | within 1e-5 of 4, ¼ and 1 | 95% |
| **C4** the constant in closed form | x from the base configuration's own c₁, c_j, c_k and L at each of C2's points; (4 + 2x)/(1 + 2x) and (2 + x)/(2 + 4x) against the instrument's R₂(1/8) and R₂(3/8) | within 1e-5 at all 8 points | 90% |
| **C5** the ties (exact arithmetic) | for N_c = 3's equal-exponent slopes α = j/N, N ≤ 30, 0 < α < ½ (B1817's `slopes`), the slopes where either sector's min E_ij is attained more than once | the set is exactly {1/12, 1/8, 1/4, 3/8, 5/12} | 95% |
| **C6** the integer limits | for every equal-exponent slope of B1817's map (N_c = 2, 3, 4, 5; 0 < α < ½) with no tie in either sector and e(m₂/m₃) < ½ in both, the predicted limit mult(p_d)/mult(p_l), in S and in S̃, against B1817's committed R₂ at Im τ 12, L_max, both offsets | on every slope whose R₂ is a converged constant (\|R₂(12)/R₂(10) − 1\| < 1e-3 at both offsets and both readings, and \|R₂(b = 0.137)/R₂(b = 0.311) − 1\| < 1e-3 at Im τ 12), \|R₂/pred − 1\| < 0.01; the other slopes are listed and not graded | 60% |

**What would count against:**
- **C1 failing** would mean the symmetry argument is wrong, and D3–D7 fall with it.
- **C2–C4 failing** at the unseen points would scope the derivation to the explored points. It would be reported as such.
- **C6 failing** would leave the integer limits unexplained by multiplicities. The ρ factor would then carry them, and
  D8's second half would be withdrawn. C6 reads only committed frame outputs.

**After the run:**
- the script is committed before its run, and its output is committed unread;
- the result is read and written up, and the write-up goes to a read-only referee before the relay;
- any step taken after the output is read is labelled post hoc.

0 of 19.
