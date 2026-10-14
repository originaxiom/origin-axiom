# B1646 — PREREGISTRATION: THE DIRECTION IS THE MASS MATRIX — a Higgs in M maps its direction one-to-one onto the two massive generations' symmetric mass matrix; no symmetric potential puts it near the isotropic cone without a tuned coefficient

cc (main), 2026-10-14. **Sealed before `direction_mass_matrix.py` runs.** No data. 0 of 19. POINT_REGISTER P-115.

**Why it matters.** B1645 showed that a Higgs in M leaves the theta triplet R massless. The ratio m = m₂/m₃ of the
other two is the Higgs's isotropy defect: zero on the cone a·a = 0, at least ½ for real directions. P-115 asks what
fixes the Higgs's direction, and what drives it near the cone. This arc first asks how much the direction carries. The
answer, derived by hand below, is all of it: the direction is the 2–3 mass matrix. So what fixes the direction fixes
the 2–3 sector, and nothing else in B1644's coupling does. The arc then reads the two candidates the register names:
- a symmetric potential;
- the cusp's unit read as a direction in M (P-113).

**The derivation, by hand, written before the run** (from B1645's Y(a) = a Rᵀ + R aᵀ − (a·R)𝟙, R·R = 0).
1. **A unitary frame fixed by τ.**
   - Write R = r(e₁ + i e₂) with e₁, e₂ real and orthonormal, and n = e₁ × e₂. This is possible because R·R = 0.
   - Then R/|R|, R̄/|R| and n are orthonormal for the Hermitian product: ⟨R̄, R⟩ = R·R = 0 and n·R = 0.
   - Here |R| = √2 r.
2. **The block form.** Write a = αR + βR̄ + γn, so a·R̄ = 2r²α, a·R = 2r²β and a·n = γ. Then:
   - Y R = 0;
   - Y R̄ = 2r²(2αR + γn);
   - Y n = γR − 2r²β n.

   So in the frame U = (R/|R|, R̄/|R|, n),
   **U†Y(a)U = [[0, 2(a·R̄), |R|(a·n)], [0, 0, 0], [0, |R|(a·n), −(a·R)]].**

   Y kills R and maps span(R̄, n) into span(R, n) by the complex symmetric matrix
   **M₂(a) = [[2(a·R̄), |R|(a·n)], [|R|(a·n), −(a·R)]],** with det M₂ = −|R|²(a·a).
3. **The bijection.**
   - a ↦ M₂(a) is linear, and in the coordinates (α, β, γ) it is diagonal: (4r²α, |R|γ, −2r²β).
   - So it is a bijection from ℂ³ onto the complex symmetric 2 × 2 matrices.
   - **Every symmetric mass matrix for the two massive generations is reached by exactly one Higgs direction.** The
     direction carries the 2–3 sector's whole content.
   - B1644's coupling predicts the massless generation (along R(τ)) and the symmetric form of the 2–3 block, and nothing
     more.
   - τ enters the masses only through |R| and the frame.
4. **The invariants for a complex direction.** From the block form:
   - s₁s₂ = |det M₂| = |R|²|a·a|;
   - s₁² + s₂² = ‖M₂‖² = 2|R|²|a|² + 2|a·R̄|² − |a·R|².

   These reduce to B1645's for real a, where a·R̄ is the conjugate of a·R.
5. **The potential.** A potential invariant under SO(3) on M and under a phase has, to quartic order,
   V = −μ²|a|² + λ₁|a|⁴ + λ₂|a·a|².
   - At fixed |a|, |a·a| ranges over [0, |a|²]: 0 on the cone, |a|² on the real locus (a real up to a phase).
   - λ₂|a·a|² is monotone in it, so the minimum sits on the cone if λ₂ > 0 (then m = 0) and on the real locus if
     λ₂ < 0 (then m ∈ [½, 1]).
   - **No such potential puts the minimum in between,** so a small non-zero m needs a term outside it.
6. **The zero modes' own loop.**
   - A fermion loop depends on the direction only through the masses, so through S = s₁² + s₂² and P = s₁s₂.
   - For f = Σ s⁴ ln s², expanding at fixed S gives f(S, P) = f(S, 0) − (2 ln S + 1)P² + O(P⁴ ln P).
   - Since P² = |R|⁴|a·a|², near the cone the loop adds only to the coefficient of |a·a|² (and moves the direction
     within the cone through S).
   - So a small non-zero m needs that total coefficient negative and small: a free number set near zero. Zero is the
     U(3)-symmetric point, so the setting is technically natural, but it is not derived.
7. **The cusp's unit as a direction (P-113, read simply).**
   - On τ = iy the thetas are real, Re R ∝ (θ₂², θ₄², 0) and Im R ∝ e_k.
   - With u = |a·R|²/(r²|a|²) and B1645's m(u):
     - **a = e_k:** u = θ₃⁴/(θ₂⁴ + θ₄⁴) = 1 by Jacobi, so m = ½ exactly;
     - **a = e_i:** u = θ₂⁴/(θ₂⁴ + θ₄⁴), which goes to 0 at the cusp, so m → 1;
     - **a = e_j:** u → 1, so m → ½.
   - At τ = i, θ₂ = θ₄, so u = ½ for e_i and e_j, and m = m(½) = 0.6096.
   - **A unit, or any real combination of units, gives m ≥ ½:** no hierarchy.

## Seen first

`VERDICT topic-sweep /vacuum alignment|flavon potential|isotropic cone|Higgs's direction|complex triplet|mass matrix of the second|Takagi|Cabibbo.*zero|first generation.*mix/: 2 of 1417 arcs on main match (NEGATIVE 1, PROVED 1); 10 other lanes match`
— B1644 and B1645 on main.
- The SM seat's W56 (lane `standard-model-derivation-0qt6ao`, pinned d7d41817) was read before the seal:
  - its setting has free coefficients (8 complex per dual-triplet sector), and it concludes "a field that only selects
    the Higgs's direction cannot make this predictive";
  - B1644's coupling has no free coefficient (the residue fixes it), so here the direction is the only freedom. This arc
    measures how much that freedom is.

**Literature:**
- the two quartic invariants of a complex SO(3) triplet, (a†a)² and |a·a|², with real and complex-isotropic vacuum
  alignments (flavour-model vacuum alignment);
- Takagi's factorisation of complex symmetric matrices;
- the Coleman–Weinberg form Σ m⁴ ln m².

## Disclosed

- Every cell checks a statement derived by hand above, so none is a blind prediction.
- D5's reading (a free number near the U(3) point) is an interpretation of an identity.
- D6 is the simplest reading of P-113; it does not exhaust FK10's unit.
- Tolerances are set at 10⁻¹² relative. The instrument runs in double precision, and B1645 sealed tolerances it could
  not reach (an E82 instance).

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **D1** | at 9 τ (6 random, i, ω, 4i) × 20 random complex a: U is unitary to 1e-12 and U†Y(a)U equals the block form of step 2 to 1e-12 relative | 95% |
| **D2** | the linear map a ↦ (M₂₁₁, M₂₁₂, M₂₂₂) has full rank at every τ (smallest singular value over largest above 1e-3); for 20 random symmetric K per τ, Y(L⁻¹K) has non-zero singular values equal to K's and a zero third one, to 1e-12 relative | 95% |
| **D3** | 200 random complex a per τ: s₁s₂ = \|R\|²\|a·a\| and s₁² + s₂² = 2\|R\|²\|a\|² + 2\|a·R̄\|² − \|a·R\|², to 1e-12 relative | 95% |
| **D4** | V = −\|a\|² + \|a\|⁴ + λ₂\|a·a\|², λ₂ ∈ {−0.5, −0.1, 0.1, 0.5, 1}, 30 BFGS starts each: for λ₂ > 0 every minimum has \|a·a\|/\|a\|² < 1e-4 and m < 1e-3 (at τ = i and a random τ); for λ₂ < 0 every minimum has \|a·a\|/\|a\|² > 1 − 1e-6 and m ∈ [½, 1]; no minimum has 1e-3 < m < 0.45 | 95% |
| **D5** | [f(S, P) − f(S, 0)]/P² equals −(2 ln S + 1) within 1% relative, for S ∈ {0.3, 1, 3} and P/S ∈ {1e-3, 1e-4} | 90% |
| **D6** | on τ = iy, y ∈ {1, 2, 4, 8}: m(e_k) = ½ to 1e-12; at y = 1, m(e_i) = m(e_j) = 0.6096 (to 1e-4); m(e_i) increases toward 1 and m(e_j) decreases toward ½ as y grows | 90% |

**The reading (the cells can only lower it).** If D1–D6 hold:
- **The direction is the 2–3 mass matrix.** A Higgs in M with B1644's coupling predicts one massless generation along
  R(τ) and a symmetric 2–3 block, and nothing more: the Higgs's six real direction parameters per sector are the
  block's six.
- **Nothing on the record drives the direction near the cone.**
  - A symmetric potential gives either extreme: m = 0 (one massive generation) or m ≥ ½.
  - The zero modes' loop only shifts the coefficient that decides between them.
  - A unit direction gives m ≥ ½.
- **P-115 is answered for this route:** a small non-zero m₂/m₃ is a free number per sector (the tuned coefficient). The
  count before any crossing (P-116) inherits it.

## Instruments

`verification/direction_mass_matrix.py` (B1645's closed form for R, which B1645's T1 tied to the residue); hashes in
`ARTIFACT_HASHES.txt`.
