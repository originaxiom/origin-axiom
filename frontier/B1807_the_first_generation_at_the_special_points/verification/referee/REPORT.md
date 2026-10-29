# B1807 (P-431) — hostile referee report (read-only, 2026-10-29)

Saved by main from the referee's hand-back (the referee could not write report files). Its scripts are beside this file,
with relative paths only:
- refkit.py, its own evaluator: direct theta and Eisenstein sums, exact termwise q-derivatives;
- ref_cr.py, its own channel-norm quadrature, validated against B1654;
- ref_identities, ref_near_i, ref_finite_L, ref_extra, ref_cusp_omega, ref_aa, ref_rbar_branch, ref_truncation;
- topic_sweep_full.txt.

The draft's script was not rerun by the referee. Main's verification is § V.

**Verdict: BLOCK as drafted; PASS WITH CORRECTIONS once B1 and B2 are applied.** The large-L mathematics stands.

## Verified independently by the referee

- **Attack 1, the identities.** R·R = 0, R·∂R = 0, R·∂²R = −∂R·∂R, ∂R·∂R/η⁶ = ¼ and ∣Wronskian∣ = ∣η∣⁹/8 hold to
  4×10⁻⁴¹ at six points. a·R + ¼f₂η⁶ = 0 holds to 7×10⁻⁴¹ at weights −½ to 43/2.
- **New exact identities.** ∂R·∂²R = 0 and ∂²R·∂²R = −(5/144)E₄∂R·∂R. Together they give **a·a = (η⁶/4)·g**, with
  g = f₁² − 2f₀f₂ − (5/144)E₄f₂² ∈ M₄ₙ₋₄ (to 2×10⁻⁴⁰).
- **Every large-L exponent of the draft's § 3**, with the referee's own random coefficients, and the post hoc m₂ slope 2.
- **The valence orders** at i and ω, and B1691's ω column for m₁.
- **Its own c_r matches B1654:** c₂ = c₄ = −1.701563 and c₃ = −3.879149 at i; −2.945819 at ω; D(i)/∣R∣² = 1.088793. D
  vanishes linearly and isotropically at ω (∣D∣/∣R∣² ≈ 2.95∣ε∣).
- **The finite-L coupling's determinant, exact:** det Y(a, u) = (a·a)(u·u)(a·u), with u·u = D at every L. So
  s₁s₂s₃ = ∣a·a∣∣D∣∣a·u∣.
- **Attack 2, the heavy pair's degeneracy, does no harm.** The large-L formula needs s₂ ≫ O(1/L), not s₁ ≠ s₂;
  exact/formula = 1.000 at L = 2560 near i.
- **Attack 5, the truncation, does no harm.** The series agree with direct sums to 6×10⁻⁴⁹, and the two launches' slope
  cells are identical.

## BLOCKING

**B1. The exponents are those of the 1/L coefficient; at the record's canonical L they change near i.**
- **The mechanism.** Under P4, u_r = √(2πL + c_r)R_r, so a·u = √(2πL)[a·R + a·(c⊙R)/(4πL) + O(L⁻²)].
  - The second term vanishes at i only through the residual symmetry (c₂(i) = c₄(i)), and generically to first order
    only.
  - In the 3/2 class, a·u(i) = 0 at every L.
  - In the 7/2 class with f₂(i) = 0, a·(c⊙R)(i) = f₀(i)D(i) ≠ 0. The zero moves to a·a, and s₂ stays at O(1/L).
- **Computed** at L = 0.65, 2.5, 40 and 2560, for ∣τ − i∣ from 10⁻¹ to 10⁻⁴:

  | section near i | the draft (large L) | finite L (every L tested) |
  |---|---|---|
  | 43/2, f₂ = E₆³ | exponent 3 | exponent **1**; crossover at ∣τ − i∣ ≈ L^{−½} |
  | 3/2, 11/2 | m₁ ≡ 0 | exponent **1**: m₁/m₃ ≈ 0.0315·∣τ − i∣/L² |
  | 55/2, f₂ = E₆⁴ | exponent 4 | exponent **2** |
  | 31/2, f₂ = E₆² | m₂/m₃ ∝ ε² | m₂/m₃(i) ≈ 0.044/L, not 0 |
  | 19/2 generic | exponent 1 | exponent 1; the coefficient 7.7× the formula at L = 2.5 |

- **At ω** D's zero is exact at every L, and the m₁ exponents survive.

**B2. A record conflict.** "At n = 1 and 3 … m₁ ≡ 0 on all of ℍ" contradicts B1691's dated S164 correction (m₁/m₃ falls
like 1/L² at finite L), which the draft's Seen first omits.

## CORRECTIONS

- **C1. A missing hypothesis: a(p) ≠ 0** (s₁(p) = 0 iff a(p) = 0).
  - The 3/2 row needs f₁(i) ≠ 0. If f₁(i) = 0, E₆ divides a and a/E₆ lies in the other class: at 27/2 with f₁ = E₆², the
    exponent is 0 and m₂/m₃ = 0.0033.
  - The 7/2 class flips when f₀(i) = f₂(i) = 0: at 31/2 the exponent is 1 and m₂/m₃ → 1.
  - "always for n = 5, 7, 9" also needs f₂ ≢ 0.
- **C2. The cusp bullet's bookkeeping is wrong; the total is right.** ∣D∣/∣R∣² ∝ Im τ·∣q∣^½ (the nome). ∣R∣² and s₁
  grow like ∣q∣^{−¼}, and ∣a·R∣/s₁ ∝ ∣q∣^½. The sum, 1, is B1691's.
- **C3. The post hoc row.**
  - Weight 7/2 is excluded (a = f₀R, m₂ ≡ 0).
  - At 15/2 and 23/2 the condition is f₂ ≡ 0 (B1806's row); it is new from 31/2 on.
  - It needs f₀(i) ≠ 0.
  - "Order 2" should read "≥ 2, generically 2", a priori from a·a's closed form.
  - A second isotropic branch is missing: 2f₀(i) + (5/144)E₄(i)f₂(i) = 0, with a(i) on R̄(i)'s line, m₂/m₃ ∝ ε² and
    m₁(i) ≠ 0.
  - At finite L, m₂/m₃(i) = O(1/L).
- **C4. Normalisation.** The ¼ holds for R = (−θ₂², −θ₄², iθ₃²)/(θ₂θ₃θ₄), the q-series code's R. With B1691's FINDINGS'
  and B1654's 1/π it is 1/(4π²). The same holds for B1806's "∂R·∂R = ¼η⁶".
- **C5. "The object fixes the parity" overclaims.** The parity follows from the section's weight class, which H-cov
  leaves free, and holds only at large L.

## NOTES

- **N2. The disclosure** should say the second launch added two cells: ∂R·∂R/η⁶ (to x¹⁵⁰) and the post hoc m₂/m₃.
- **N3.** The 10⁻⁴⁰ cut for "identically zero" is adequate, with about two orders of margin.
- **N4. Seen first.**
  - State the regex. It matched 34 arcs and 2 rows, mostly "valence" inside "equivalence"; only B1806 and P-431 are
    relevant, and no frontier arc uses the valence formula.
  - Add B1691's S164 correction and B1667.
  - B1691 did attribute its ω column to the residual ℤ₃ charge: it lacked the closed form, not the reading.
- **N5. Value contact.** "Not the Standard Model's pattern in any sector" is itself a comparison; drop it or label it.
- **N6. A candidate row.** At finite L near ω:
  - B1691's "m₁ = 0 at 11/2" becomes ∝ ∣ε∣³;
  - its m₂/m₃ ∝ ∣ε∣² at 23/2 and 11/2 becomes ∝ ∣ε∣ for ∣ε∣ ≲ 1/L.

  B1691's and B1806's m₂ statements are statements about the L-free coupling Y(a, R).
- **N7.** P-431's "D near i in closed form" is not needed: the exponent needs only D(i) ≠ 0.
- **N8, offered.** m₂'s exponent at L = ∞ is ν_p(g): even at i, and ≡ −(2n − 2) mod 3 at ω. This reproduces B1691's ω
  m₂ column and B1806's ε² rows.

## V. Main's verification (2026-10-29)

- **B2: verified.** B1691's S164 correction (2026-10-21, lines 113–120) reads: "'m₁ = 0 without a ∂²R component' …
  holds only in B1654's large-L limit … m₁/m₃ falls like 1/L²". The draft's "m₁ ≡ 0 on all of ℍ" contradicted it. A sweep
  miss on main's side (E54): the arc's own dated corrections were not read before drafting.
- **B1's mechanism: verified by hand.** With u_r = √(2πL + c_r)R_r, a·u = √(2πL)[a·R + a·(c⊙R)/(4πL) + …].
  - In the 3/2 class, a(i) lies on ρ(S)'s simple real line, ∝ (1, −1, 0), where the swapped channels (c₂(i) = c₄(i)) sit,
    so the second term vanishes at i.
  - c₂ − c₄ is odd under S, so it vanishes at i to odd order, generically 1.
  - So at finite L the exponent is min(ν_i(f₂), 1) = 1, with m₁(i) = 0 at every L. This agrees with the P-406 referee's
    r1 (DR at finite L).
  - The determinant identity follows from Y(a, u)'s form. u·u = D is B1654's N4.
  - B1's numbers are being regenerated on main (main_rerun/).
- **The a·a closed form: verified by hand.**
  - ∂R·∂²R = ½ϑ(∂R·∂R) = ⅛ϑ(η⁶) = 0, since η⁶ is annihilated by the weight-3 Serre derivative.
  - ∂²R·∂²R = −(5/144)E₄∂R·∂R is B1806's banked identity (exact to x²⁴⁰).
  - Expanding a·a with R·R = R·∂R = 0 and R·∂²R = −∂R·∂R gives (η⁶/4)(f₁² − 2f₀f₂ − (5/144)E₄f₂²).
- **The ω 19/2 rows (read on main):** in B1691's own L = ∞ coupling, that random section's m₂/m₃ rises to 0.89 at
  ∣ε∣ = 10⁻³ and falls as ∣ε∣ only below. The near-point exponents are asymptotics whose range depends on the section; the
  smallest decade carries them (slope 1.0).
- **C1–C5 and N2–N8: accepted.**
