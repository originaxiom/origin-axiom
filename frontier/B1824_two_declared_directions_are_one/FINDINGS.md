# B1824 — TWO OF B1810'S THIRTEEN DECLARED HIGGS DIRECTIONS ARE ONE: a₀ = η⁴F₋₂/6 IDENTICALLY. B1697'S a₀ = D²R − E₄R/48 IS η⁴ TIMES B1730'S ZERO-FREE F₋₂, SO B1691'S "UNIDENTIFIED ZERO AT t = −1/48" IS IDENTIFIED AND THE DECLARED MENU HAS TWELVE DISTINCT DIRECTIONS (data-free)

**Verdict: PROVED** (an identity, with an elementary proof and two independent checks). Data-free; no measured value is
read. cc (main), 2026-10-30.

- **Found** as a side finding of Step A v2's draft (B1823).
- **Confirmed** by main componentwise at three values of τ.
- **Proved** by hand by B1823's hostile referee, and checked exactly in B1691's q-series machinery to q²⁵.
- **Re-derived** by main in its own code: the proof in sympy, and 40-digit numerics by direct differentiation at four
  values of τ.

**0 of 19.**

## 1. The identity

- **R** = (−θ₂², −θ₄², iθ₃²)/(θ₂θ₃θ₄): weight −½, multiplier ρ_R (B1645, B1691; B1730 § 1).
- **a₀** = D²R − E₄R/48 (B1697), weight 7/2. Here D² = D_{3/2}D_{−1/2}, with the Serre derivative D_k = q d/dq − (k/12)E₂.
- **F₋₂** = η⁵(θ₂⁻², θ₄⁻², iθ₃⁻²): B1730's F_a at a = −2 (ε = i⁰ = 1), with η the Dedekind eta.
- **The identity.** With η³ = θ₂θ₃θ₄/2:

  a₀ = (1/48)(θ₂θ₃³θ₄³, θ₂³θ₃³θ₄, iθ₂³θ₃θ₄³) = (1/48)(θ₂θ₃θ₄)³(θ₂⁻², θ₄⁻², iθ₃⁻²) = (η⁹/6)(θ₂⁻², θ₄⁻², iθ₃⁻²)
  = **η⁴F₋₂/6**.
- **Componentwise,** with A = θ₂⁴, B = θ₃⁴ and C = θ₄⁴: a₀ = R ∘ (−BC, −AB, AC)/48.
- **Its norm.** B1730 has N(F_a) = i2^aη⁹, so N(a₀) = a₀,₁a₀,₂a₀,₃ = iη²¹/864. It has no zero on the upper half plane.

## 2. The proof (the referee's, re-derived by main in sympy: `verification/a0_identity_main.py`, part 1)

- **The inputs,** each checked numerically at 40 digits (§ 3):
  - the theta log-derivatives, with D = q d/dq:
    - D log θ₂ = (E₂ + θ₃⁴ + θ₄⁴)/24;
    - D log θ₃ = (E₂ + θ₂⁴ − θ₄⁴)/24;
    - D log θ₄ = (E₂ − θ₂⁴ − θ₃⁴)/24;
  - Jacobi's identity, B = A + C;
  - E₄ = (A² + B² + C²)/2;
  - η³ = θ₂θ₃θ₄/2.
- **The first derivative.** D_{−1/2}R_k/R_k is free of E₂: (A + 2C)/12, −(2A + C)/12 and (A − C)/12.
- **The second.** D_{3/2}D_{−1/2}R_k − E₄R_k/48 = R_k × (−C(A + C), −A(A + C), AC)/48. Since B = A + C, that is
  R_k × (−BC, −AB, AC)/48, the monomials of § 1.
- **Why −1/48.** For D²R + tE₄R, with E₄ = A² + AC + C², the brackets are (A², C², B²)/48 + t·E₄.
  - They are products of theta powers at exactly two values: t = 0, where D²R = R ∘ (θ₂⁸, θ₄⁸, θ₃⁸)/48, and
    t = −1/48.
  - Only at t = −1/48 do the q^{−1/8} terms of components 2 and 3 cancel. That cancellation is B1697's holomorphy at the
    cusp. At t = 0 components 2 and 3 start at q^{−1/8}.
  - **Main's correction to the referee's remark** "Only t = −1/48 collapses the bracket to a monomial": it misses t = 0.
    The remark is not load-bearing (sympy, main's check).
  - **The referee agrees** (its confirmation, to 1.6 × 10⁻⁴⁰): −1/48 is the unique t at which the brackets are both
    monomial and holomorphic at the cusp.
- **The constant 1/6** follows from the leading terms: a₀,₁ starts at q^{1/8}/24, and η⁴F₋₂,₁ at q^{1/8}/4.
- **A second route** (the draft's). η⁴F₋₂ has a₀'s weight 7/2 and trivial character, so each component ratio is
  holomorphic, since F₋₂ is zero-free (B1730). The monomial ρ_R permutes the ratios, so each is a Γ(2)-invariant function.
  Each is bounded at the cusps, hence constant. The referee notes that the bound at the cusps is the crux: it is the
  cancellation above.

## 3. The checks

**Main's** (`verification/a0_identity_main.py` → `.json`, `_run.txt`):
- **Part 1, the algebra** (§ 2).
- **Part 2, the numerics,** independent of part 1's formulas.
  - a₀ is computed by numerical differentiation of R at 40 digits, and compared with η⁴F₋₂/6, η taken from its product.
  - They agree to ≤ 2.2 × 10⁻⁴⁰ at τ = 0.17 + 1.23i, 1.7 + 0.9i, −2.3 + 1.6i and 0.31 + 0.62i.
- **Part 3, the inputs.** The log-derivatives hold to ≤ 3 × 10⁻⁴², Jacobi to 2 × 10⁻⁴¹, and E₄'s theta form to
  1.3 × 10⁻⁴¹.
- **Disclosed.** Main's first numerical run took θ₂ from mpmath's jtheta(2, 0, q). Its principal q^{1/4} is the wrong
  branch for ∣Re τ∣ > 1, a defect already known to the record (B1634, B1674). At Re τ = 1.7 and −2.3 the ratio came out
  off by a unit phase. Summing θ₂ in τ corrected it, and every value above is from the corrected run.

**The referee's** (`verification/referee/t_a0.py` → `t_a0.json`, `t_a0_run.txt`):
- **Exactly,** in a copy of B1691's own q-series machinery: all three components agree to x²⁰⁰ = q²⁵. The leading terms
  are q^{1/8}/24, q^{3/8}/6 and iq^{3/8}/6.
- **Numerically,** to ≤ 10⁻³⁰ at five values of τ.
- **It also offers two conventions that would produce a τ-dependent scalar like main's earlier mismatch.** Which of
  them, or the jtheta branch defect disclosed above, caused it is not shown:
  - B1810's direction function (θ₂⁻², θ₄⁻², iθ₃⁻²), without η⁵, gives the scalar η⁹/6;
  - a |η|⁵ convention gives (|η|⁴/6)e^{9i arg η}.

**On B1810's committed table** (`verification/b1810_a0_vs_Fm2.py` → `.json`; main's):
- The 64 pairs of a₀ and F₋₂ rows (same configuration, radius and reading) agree in every mass ratio to 1.6 × 10⁻¹⁶.
- Where V is defined (32 pairs), |V| agrees to 10⁻¹⁵ and J to 7 × 10⁻³³.
- Where B1810 marks V undefined (32 pairs, degenerate sectors), the |V| cells differ by up to 0.021, as an undefined V
  may.

**The lock** (`tests/test_b1824_two_declared_directions_are_one.py`):
- the identity and N(a₀) = iη²¹/864 at two values of τ (one with Re τ = 1.6), at 30 digits;
- **a control that must fail:** B1810's direction t = −5/288 is not proportional to F₋₂;
- the committed checks read back.

## 4. What it means

- **B1810's thirteen declared directions are twelve distinct ones.**
  - They are DR, a₀ ≡ F₋₂, R = F₂, t = −5/288, F₋₁₀, F₋₆, F₆, F₁₀, F₁₄, F₁₈, F₂₂ and F₂₆.
  - At every τ, a₀ and F₋₂ span one line in ℂ³. The frame's outputs are scale-free, so they coincide, as B1810's own
    table shows (§ 3).
  - The record saw the coincidence at τ = i only:
    - B1809's Table T, "equal to F₋₂ at i";
    - B1810 § 2.3, "a₀ has κ = 2^{−1/2} (= F₋₂)".
- **B1811 (NEGATIVE as sealed) is unchanged.** Its 52 rows held one direction twice, in the arc and in the null alike: the
  null chose among the same rows.
- **For Step B:**
  - the declared menu has twelve directions, so its price drops by log₂(13/12) = 0.115 bits;
  - the refined census computes both;
  - its a₀ and F₋₂ rows must agree. That is checked at the census's certification, by a committed aggregate-only script,
    before the seal.
- **B1691's "unidentified zero at t = −1/48" is identified** (B1697 § 1): it is η⁴ times B1730's zero-free F₋₂.
  B1697's uniqueness (the weight-7/2 ρ_R section without end data is one line) therefore names that line.

## 5. Scope

- An identity of vector-valued forms on the whole upper half plane.
- The coincidence of the frame's outputs follows for any computation that reads the direction only through its line,
  the census among them. On the census's own rows it is to be confirmed (§ 4).

## Seen first

- `VERDICT topic-sweep /a₀|\ba0\b|F₋₂|F_-2|F_\{-2\}|t = −1/48|-1/48|−1/48|eta\^4 F|η⁴/ (full text): 60 of 1568 arcs on main match (NEGATIVE 12, OPEN 2, PROVED 46); 18 register rows match (DONE 10, OWNER 1, QUEUED 7); 13 other lanes match`
- **Read:**
  - B1697: a₀'s holomorphy at the cusp, and "unidentified 'zero at t = −1/48'";
  - B1730: F_a and N(F_a);
  - B1810 § 2.3, the κ coincidence at i;
  - B1811's sealed menu;
  - P-245, P-306 and P-316.
- **The identity is stated nowhere on main.** A grep for its forms (a₀ = η…, η⁴F₋₂, θ₂θ₃³θ₄³ and their ASCII spellings)
  finds nothing in the frontier or docs. It also finds nothing on the SM seat's, the web seat's or the agy lane's
  branches.
- **The literature.** The theta identities used are classical: Jacobi's θ₃⁴ = θ₂⁴ + θ₄⁴, the theta log-derivatives,
  E₄'s theta form and η³ = θ₂θ₃θ₄/2. The identity itself is a statement about the record's objects, and no novelty is
  claimed beyond the record.
