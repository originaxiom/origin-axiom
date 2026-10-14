# The first row: can the lepton obstacle be escaped at leading order? (chat1, 2026-10-14, evening). Sealed before any code that computes it.

**Why.**
- The owner said "continue" after chat1 proposed three cheap checks. This is the second: whether the lepton obstacle can
  be escaped.
- **The obstacle is B1649's** (§3): "The leptons by the same reading: a trivial PMNS first row at leading order, against
  a large θ₁₂, unless the lepton sector's R differs." chat1's mysteries note first called it new. That was corrected at
  `d8c94c95c`.
- chat1 floated one escape: under Reading B the electroweak condensates act on the block space, which might move the
  neutrino's null vector off R. This check tests that escape. It also tests every other leading-order escape built from
  objects on the record.
- **Name.** "The first-row check." It avoids the record's T- prefix.

**The idea, by hand** (written before any code; the cells test it).
1. **A bound.** Write σ(w) = |w·w|/|w|² ∈ [0, 1] for w ≠ 0 in ℂ³. Here w·w = Σ w_k² is the bilinear form and
   ⟨u, v⟩ = u†v the Hermitian product, compatible in one real basis.
   - σ = 0 means isotropic. σ = 1 means real up to a phase.
   - Put α(w) = ½ arccos σ(w) ∈ [0, π/4]. Then
     **|⟨u, v⟩|² / (|u|²|v|²) ≤ cos²(α_u − α_v) = ½ (1 + σ_uσ_v + √((1 − σ_u²)(1 − σ_v²))).**
   - **Proof.**
     - d(x, y) = arccos(|⟨x, y⟩|/(|x||y|)) is the Fubini–Study metric on lines.
     - Complex conjugation is an isometry of d, and ⟨x̄, x⟩ = x·x, so d(x, x̄) = 2α(x).
     - The triangle inequality gives d(u, ū) ≤ d(u, v) + d(v, v̄) + d(v̄, ū) = 2d(u, v) + d(v, v̄). So
       d(u, v) ≥ |α_u − α_v|.
   - **Sharp.** u = cos α_u x + i sin α_u y and v = cos α_v x + i sin α_v y, with x ⊥ y real unit vectors, attain it.
   - **The case used.** An isotropic u and a real v give **at most ½**.
   - σ is unchanged by conjugation, so the bound does not depend on which side of a mass term is conjugated.
2. **The record's objects.**
   - **B1649.** The electron, the lightest charged lepton at leading order, lies along the theta triplet R. R is
     isotropic at every τ (Jacobi), so σ = 0.
   - **The weave's group.** In the units' basis the weave's group acts on T as z·S, with S a rotation of the cube (the SM
     seat's W49). So its rotation axes are real (σ = 1), and the other eigenlines of a rotation that is not a half-turn
     are isotropic (σ = 0).
   - **TM1, P10 (B1612).**
     - TM1's neutrino column is the line of RRL, a half-turn. That line is its axis, so it is real.
     - TM1's charged-lepton basis is RL's eigenbasis. RL is a 120° turn, so that basis is one real axis and two
       isotropic lines.
     - The column's ⅔ must sit on the real axis (by 1, ⅔ > ½). So **TM1 puts the electron on a real direction, and
       B1649 puts it on an isotropic one.**
3. **Conventions.**
   - Every coupling here pairs fibre zero modes holomorphically, with no conjugation. So a sector's massless direction is
     the kernel vector of its matrix:
     - the charged leptons: Y_e v = 0, so v ∝ R (two-sided, B1649);
     - the neutrinos: M_ν u = 0 (Takagi), so u ∝ R whenever M_ν kills R.
   - Then U_e1 = v†u = 1.
   - Conjugating one side only would give R̂ᵀR̂ = 0. Either way the value is never 0.675.
4. **Which neutrino operators keep R.**
   - Any M_ν = Σ Y(a_k): Y(a)R = a(R·R) = 0. This covers the Weinberg-shaped hook and type II.
   - Any M_ν = Y_Dᵀ A Y_D. This covers type I, with the Dirac coupling at the puncture on the same fibre: by B1649 Y_D
     kills R on both sides.
5. **Reading B** (conditional: the generation index is the block space 3_B).
   - A condensate with block root ±(e_r − e_s) acts as E_rs or E_sr. It kills e_t, where t is the block whose
     Y = −5/6.
   - So any operator with one condensate on each leg, M_ν = sym(Aᵀ Y(a) B) with A, B ∈ span(E_rs, E_sr), kills e_t.
     Then ν₁ = e_t is real, and |U_e1|² = |R_t|²/|R|² ≤ ½.
   - On τ = iy with t = k it equals θ₃⁴/(θ₂⁴ + θ₃⁴ + θ₄⁴) = ½ exactly.
   - If the charged leptons' operator takes the same two condensates, which puncture parity requires of B1644's pairing,
     the electron is e_t too, and the row is trivial again.
6. **Nature.**
   - |U_e1|² = (1 − sin²θ₁₂)(1 − sin²θ₁₃) = **0.6753 ± 0.0085**.
   - Inputs: JUNO's first result, sin²θ₁₂ = 0.3092 ± 0.0087 (arXiv:2511.14593), and B1613's sin²θ₁₃ = 0.02248.
   - That is 20.6σ above ½ and 38σ below 1.
   - With the electron isotropic, it needs a neutrino direction with σ_ν ≤ 2√(p(1−p)) = 0.937 (0.943 for TM1's ⅔).
   - With a real ν₁, the electron must turn by at least 45° − ½ arccos(2p − 1) = 10.3° off R (9.7° for TM1).

**Seen first.**
- B1612, B1613 (TM1, P10), B1625 and THE_WEAVE (TM1 under T̄ ⊗ T only), B1640 (P-004: one τ cannot give both residuals).
- B1644, B1645, B1646 and B1649 (FINDINGS in full); POINT_REGISTER P-128 and P-129.
- The SM seat's W43, W49 (the units are the generation multiplicity; the Hodge–Riemann pairing is 2·I₃ on them), W55
  and W70.
- chat1's `condensate_in_M` (Reading A and B; finding 3, two condensates required).
- **Sweep.** No arc or relay on main, the SM seat or the audit lane links isotropy to the PMNS or bounds an overlap this
  way.
- **Plumbing control run before this seal.** Main's B1611 module loads from main at `60c5470ae` and gives |G| = 96 (a
  banked number). No σ, overlap or form has been computed.

**Objects and instrument.**
- **Main's banked modules,** read-only, extracted by `git archive` from main at `60c5470ae1747e5bd31a1a889ce38739791e0af3`
  into a temporary directory: B1600, B1610, B1611, B1612, B1642 and B1649. Nothing on main is touched.
  - G and T come from B1611: TB, restrict, and W's L and R. B1612's word order applies: "RL" = MR·ML.
  - Y(S) is B1649's `Y_of`, from mpmath residues at 30 digits.
  - R is B1645's closed form, R = (−θ₂², −θ₄², iθ₃²)/(πθ₂θ₃θ₄) in the units' labels (i, j, k).
- **The invariant form on T.** B is the symmetric 3 × 3 matrix with AᵀBA ∈ ℂ·B for both generators, normalised to be
  unitary. Then σ_B(v) = |vᵀBv|/|v|².
- **The units in B1612's coordinates.**
  - f_L and f_R are the σ_B = 1 eigenlines of ρ(L) and ρ(R). f_3 is the line Hermitian-orthogonal to both.
  - Each is phased so that fᵀBf = 1, which leaves a sign.
  - W49's labels are L about i and R about j. All 6 labellings and 4 sign classes are also run.
- **τ grid.** i, 1.5i, 2i, 4i, ω, 0.3 + 1.1i, −0.2 + 0.9i, 0.45 + 2.5i.

| | prediction | prior |
|---|---|---|
| Q0 (controls) | B1612's TM1 column (⅔, ⅙, ⅙) is reproduced as RL's basis against RRL's line, to 1e-9. \|R·R\|/\|R\|² < 1e-12 on the grid (numpy), and < 1e-25 at three τ (mpmath). f_L ⊥ f_R (Hermitian, to 1e-9), and σ_B(f_3) = 1 | 97% |
| F1 | The bound holds on 2·10⁵ random pairs in ℂ³ (Gaussian, isotropic against real, near-isotropic, near-real), and under 200 adversarial maximisations: ratio ≤ bound + 1e-9. The sharp pairs reach the bound to 1e-12 at 25 (σ_u, σ_v) points | 99% |
| F2 | The invariant symmetric form on T is unique (one solution, up to scale) and unitary up to scale (singular values equal to 1e-9) | 90% |
| F3 | TM1's neutrino line (RRL's non-degenerate eigenline) has σ_B = 1 to 1e-9. RL's eigenbasis has σ_B = (1, 0, 0) to 1e-9. The ⅔ entry sits on the σ_B = 1 vector | 92% |
| F4 | **The cap.** At every τ on the grid: max over real unit v of \|⟨R̂, v⟩\|² is ½ to 1e-12; and TM1's line against R̂ is ≤ ½ + 1e-12 under every labelling and sign class (24 frames) | 97% |
| F5 | **One fibre, every neutrino operator.** At 6 τ × 3 draws, with residue couplings: the charged leptons Y(S_e) with s₀ ≠ 0, and the neutrinos from (i) Y(a_ν), (ii) −Y(S_D)ᵀM_R⁻¹Y(S_D) with M_R random complex symmetric, and (iii) their sum, type I plus type II. In every case \|U_e1\| = 1 to 1e-10, \|U_e2\| and \|U_e3\| < 1e-10, and m_e/m_τ and m₁/m₃ < 1e-10 | 96% |
| F6 | **Reading B** (conditional). For t = i, j, k and random A, B ∈ span(E_rs, E_sr) on the grid: sym(AᵀY(a)B) has rank 2 (m₁/m₃ < 1e-12, m₂/m₃ > 1e-6); its null line is e_t (overlap 1 to 1e-10); \|U_e1\|² = \|R_t\|²/\|R\|² ≤ ½ + 1e-12. The both-sectors variant, with the charged leptons' Dirac matrix A′ᵀY(S_e)B′ (not symmetrised), gives \|U_e1\| = 1 | 92% |

**Read-outs (no prior).**
- TM1's line against R̂ in W49's labelling, all 4 sign classes, on the grid and along τ = iy (y from 0.6 to 6). The
  hand values on τ = iy are (θ₃⁴ + θ₄⁴)/(4θ₃⁴): 3/8 at i, rising to ½ at the cusp.
- The minimum and maximum over the 24 frames.
- |R_t|²/|R|² for t = i, j, k on the grid and along τ = iy.
- The placement with both condensates on one leg, sym(Y(a)AB): its rank (the hook needs rank 2).
- The data line and the two requirements of §6, recomputed.
- Every real eigenline of B1612's group against R̂: the largest overlap.

**What a result means, fenced.**
- **If F1–F6 hold.**
  - At leading order on the residue route, with the electron along the isotropic R (B1649), the PMNS first row is
    |U_e1|² = 1 when ν₁ comes from any operator built on the puncture's couplings (the hook, type I, type II).
  - It is at most ½ when ν₁ is real: Reading B's block vector, or any axis of the weave's group, TM1's included.
  - Nature's 0.675 lies strictly between. Reaching it needs one of two things:
    - a charged-lepton lift that turns the electron at least 10° off R;
    - or a neutrino direction that is complex but not R (σ ≤ 0.94), that is, a sector-dependent R, which is P-128's
      ground.
- **[READING] for cc.** P10's TM1 puts the electron on RL's real axis, and B1649 puts it on an isotropic line. They
  cannot both be the leptons' leading order: one is corrected at order one, or does not apply to leptons. This is a third
  incompatibility, independent of the tensor (B1625) and of the one-τ residual pair (B1640).
- **Not tested.**
  - P-128 (cc's, firewalled) and any Wilson-line R.
  - The physical L² normalisation (T-NORM). This check uses the weave's own Hodge–Riemann pairing.
  - Any lift; H-RES; the parent map (P-108); inverted ordering.
- No value. **0 of 19.**
