# B1651 — second addendum (2026-10-14, S127): §107 checked by hand on main; the Szegő reading makes three banked statements one identity, whose root is that a point coupling is rank one; a Higgs lifts the zero only if its profile does not act as a point

The first addendum recorded the SM seat's §107 and chat1's answers as read, not yet checked on main (P-142). This one
records main's checks, made on the night of 2026-10-14. They are unsealed: a hand argument and an identity check, with no
data and no fitting.

## 1. The SM seat's §107, checked by hand: under its typing, a smooth Higgs carrying parity couples only at the puncture

**The setting.**
- E is the fibre torus, with the puncture at 0. χ is a non-trivial 2-torsion character, the parity a pairing carries
  (U2). L_χ is its flat line bundle, of degree 0 and non-trivial, so h⁰(E, L_χ) = h¹(E, L_χ) = 0.
- The zero modes' pairing ω is a meromorphic (1, 0)-form valued in L_χ, with one simple pole, at the puncture. Its
  residue is a component of R.
- The Higgs φ is a smooth (0, 1)-form valued in L_χ; this is §107's typing. The coupling is Y = ∫_E ω ∧ φ, which
  converges because the pole is simple.

**The argument.**
1. **φ is exact, uniquely.** H^{0,1}(E, L_χ) = 0, so φ = ∂̄f for a smooth section f, unique because h⁰ = 0. This is
   B1651's bulk statement: no class in the bulk.
2. **Yet it couples.** By Stokes on E minus a small disc at 0, using dω = 0 there:
   Y = −∫ d(fω) = ∮_{∣z∣=ε} fω → 2πi · f(0) · Res₀ ω.
3. **f(0) is the framed class, one datum per parity.** It is the class of φ in H¹(E, L_χ(−[0])) ≅ ℂ (Riemann–Roch on
   degree −1), dual to H⁰(E, K ⊗ L_χ([0])) ≅ ℂ, where ω lives (Serre). The topological side agrees: H¹(F₂; χ) ≅ ℂ
   restricts isomorphically to the puncture loop, so the parabolic and L² parts vanish (§107's C0, item 3).
4. **For a point Higgs the two typings agree.** A (0, 1) current a δ_{z₀} dz̄ gives an f with a simple pole at z₀.
   Then fω is a meromorphic one-form with poles at z₀ and 0 only, and the residue theorem turns evaluation at z₀ into
   the puncture's term.

**Verdict.** §107 holds as stated.
- **For point Higgs fields,** evaluation at z₀ (premise P1) and the (0, 1) current give the same coupling, v(z₀), which
  is the puncture's residue carried to z₀ (§2).
- **For spread profiles the typings differ.** A density-type Higgs couples by ∫ v(z) φ(z). A (0, 1)-type Higgs couples
  only through its framed classes, so the puncture is forced, at the price of one datum per parity.

Which type is physical is the dictionary's question: the audit lane's typed-field portal, the parent's clause 4, and
P-108.

## 2. The Szegő reading: the triplet at any point is the puncture's residue, carried by the three spin structures

S_r(z) = θ_r(z) θ₁′(0) / (θ_r(0) θ₁(z)) is the Szegő kernel of the even spin structure r, which behaves like 1/z at 0.
In B1651's conventions:
- **A (a rewriting):** v_r(z) = R_r S_r(z), with R_r = c_r θ_r(0)²/θ₁′(0) = Res_{z=0} v_r.
- **B (classical):** S_r(z)² = ℘(z) − e_r, where e_r = ℘(w_r) at the half-period where θ_r vanishes.
- **So** v·v = ℘(z)(R·R) − Σ_r R_r² e_r. **Isotropy at every point (U3a) is equivalent to two facts at the
  puncture:**
  - R·R = 0, B1649's null residue (Jacobi's θ₃⁴ = θ₂⁴ + θ₄⁴);
  - Σ R_r² e_r = 0, B1650's O6, chat1's nilpotency.

  Three banked statements are one identity. This is also the join P-035 asks for: the triplet's θ characteristics are
  the fibre's even spin structures.

**The root, by hand: a point coupling is rank one.** Main's read-only reviewing agent found this while it reviewed
B1653's design before that seal, and main re-derived it.
- **The factorisation.** F(z) is one doublet value, a vector in ℂ², and the three generations are its quaternionic
  images C_p F. So a coupling read at one point, Y_pq = (C_p F(z))ᵀ εS (C_q F(z)), factors through ℂ² and has
  rank ≤ 2.
- **At the puncture.** Both components of F behave like z^{−1/2}, since θ₁(z + τ) also vanishes at 0. So the residue
  of F Fᵀ is v vᵀ, rank one, and the same holds there.
- **The null quaternion.** In the quaternion basis a rank-one 2 × 2 matrix is a null quaternion: R₁² + R·R = 0, where
  R₁ = Fᵀ ε F is the identity unit's pairing.
- **The consequence.** Here R₁ = 0 by antisymmetry, so R·R = 0 at every point: U3a. B1649's null R and B1650's O6
  follow, and Jacobi's identity is this 2 × 2 determinant written out in theta functions.
- **The twisted case** (a flat line, where R₁ ≠ 0) is B1653's.

**Checked** (`verification/szego_check.py`; mpmath at 40 digits; three τ and three z; ℘ computed independently as
−(log θ₁)″ + θ₁‴(0)/(3θ₁′(0))):

| check | worst residual |
|---|---|
| A | 3.7 × 10⁻⁴¹ |
| B | 1.9 × 10⁻⁴⁰ |
| R·R | 1.7 × 10⁻⁴¹ |
| Σ R_r² e_r | 1.6 × 10⁻⁴¹ |
| isotropy | 2.9 × 10⁻⁴¹ |

**Controls.**
- Pairing θ₂ with θ₄'s half-period breaks B, with residuals 0.13 to 2.5.
- Replacing c₃ = i by 1 breaks R·R = 0, giving 0.88 to 1.0.

**Disclosed.** The first version of the second control flipped a sign of c. R·R depends only on c_r², so that control
could not fail (E82). It was caught and replaced before the check was used.

## 3. P-129's first premise, sharpened: the zero belongs to couplings that act as a point

- **A single-point Higgs at any z₀ keeps the zero at one τ:** v(z₀) is isotropic.
- **A radially symmetric profile about a regular point keeps it too.**
  - The zero modes' bilinear G(z) = F(z)F(z)ᵀ is holomorphic away from the puncture. So by the mean-value property,
    ∫ w(∣z − c₀∣) G(z) d²z = (∫ w) · G(c₀): the profile acts as the point c₀.
  - Main's read-only reviewing agent found this while it reviewed B1653's design. It is Cauchy's mean value, and main
    re-derived it.
  - A first draft of this section said "a spread profile generically lifts it". That is true generically, but it is
    false for this case, which a stationary Higgs could well be. Corrected before landing.
- **A profile lifts the zero only when it does not act as a point:**
  - **About a regular point,** when it has a non-zero holomorphic moment ∫ w(z)(z − c₀)ⁿ d²z for some n ≥ 1 (an
    anisotropic profile). Then M = ∫ w G has rank 2.
  - **About the puncture,** a radially symmetric profile reads the bilinear's regular part there. The circle average of
    the 1/z pole vanishes, and the regular part is rank 2.
  - **In the (0, 1) typing the same holds.** u = (f_χ(0) R_χ)_χ is isotropic exactly when the profile acts as a point
    (u ∝ v(z₀)), and not otherwise. (A first draft said "unless the three framed classes are equal", which is one
    such case among many.)
- **So the first generation's zero is a property of couplings that act as a point.** What a lifting profile supplies
  (its holomorphic moments, or its reading at the puncture) is free unless a dynamics fixes it. This feeds P-128 and
  P-151.

## 4. The seats' replays and qualifications

- **The SM seat's W85** checked every cell on its own theta series at 60 digits, blind to main's output (a second
  instrument).
- **The audit lane** replayed main's original producer under its own seal (`ce62cb60c`), with full equality of the
  records. Its qualifications:
  - working precision is not interval certification;
  - the all-point statement needs its analytic argument;
  - the single-point null result does not transfer to an integrated coupling without a calculation.

  The analytic argument is Jacobi's identity θ₄(z)²θ₄² + θ₂(z)²θ₂² = θ₃(z)²θ₃² (FINDINGS, U3), and §2 above gives it
  in Szegő form. §3 is the integrated coupling's calculation, by hand.

## 5. What changes

- **B1651's cells and numbers stand as sealed.**
- **Its reading is sharpened, not reversed.** The puncture is not forced for point Higgs fields. For a smooth Higgs of
  (0, 1) type it is forced, at the price of one framed datum per parity.
- **P-142's parabolic part is DONE.** The half-period orbit's mass structure stays open; main's by-hand Schur reading
  (P-150) predicts no hierarchy from a covariant orbit.
- **P-129's first premise is sharpened (§3).**
- **For the paper (T4):** isotropy's root is that a point coupling is rank one, a two-line proof; the Szegő form (A and
  B) is its expansion; the Higgs's type is stated wherever the locus is.
- **Credit:**
  - the SM seat: §107, and W85 as B1651's second instrument;
  - chat1: O6, which is half of the identity;
  - the audit lane: the typing distinction and the replay of main's producer;
  - main's read-only reviewing agent: the rank-one root, found while it reviewed B1653's design, and re-derived on
    main.

## Dated correction (2026-10-15, S129): whose typing distinction this is

§1's last paragraph and §5's credit name "the audit lane: the typing distinction". The distinction between a (0, 1)
Higgs and a density Higgs is the SM seat's. It is W61's two typings (T ⊗ T with dz̄, and T̄ ⊗ T with the constant
function) and C0's "a cubic coupling of two holomorphic modes needs a Higgs of type (0, 1)". The audit lane's
typed-field portal is another typing: the bundle weight of its parent fields, spinor-valued K^½ against K-valued. It
bears on the parent's clause 4. It does not decide between a (0, 1) Higgs and a density Higgs, and the lane never
coupled the zero modes to a Higgs in either. Credit corrected: the SM seat, for the typing distinction; the audit lane,
for the replay of main's producer and the portal. Found by main's reader in S129's sweep.
