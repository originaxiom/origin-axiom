# CLAIM CARD — the three boundary-free classes of H¹(fibre, ad Q₈) all move the cusp; FL-08 prices only the lines

- card id: new
- seat code: fam1-v1-unset-04
- seat, branch, commit: fam1-v1-unset-04, sm/cards, 3372dd041787d8e874121937af041a1747bb9afa
- kind: computation
- touches: P-635, P-567 (FL-08 as the register states it)
- effect: conditions — P-635: FL-08 prices the 2 line classes only; holding the cusp at −1 is one discrete end
  condition that removes all 3 Q₈ classes, and 1 survives on m004
- scope: frame: none evaluated (only the frame's Q₈ constants are read: QI, QJ, QK, EPS, BLOCKS in B1723's
  b1656_funcs); object: the flat SU(2) representation ρ(a) = Q_I, ρ(b) = Q_J of the fibre's group, with coefficients
  ad = su(2) = R³; reach: single; hypotheses: the frame's Q₈ bundle has this holonomy pair (as B1836's C6 takes
  it); m004's monodromy is a ↦ ab, b ↦ bab (only its abelianised class [[1, 1], [1, 2]] is checked)
- identifications: none
- definitions: closed fibre group Z² = ⟨a, b | aba⁻¹b⁻¹⟩. Punctured fibre group F₂ = ⟨a, b⟩, with boundary loop
  c = aba⁻¹b⁻¹, and ρ(c) = −1. Z¹ is the kernel of the relators' Fox Jacobian in Ad ρ, B¹ = {((Ad g − 1)v)_g},
  H¹ = Z¹/B¹. H¹_par (boundary held) = {u ∈ Z¹ : u(c) ∈ (Ad ρ(c) − 1)V}/B¹. The lines are the centre u(1) with
  trivial coefficients. The family is A(s) = Q_I e^{s₁Q_I} e^{s₃Q_K}, B(s) = Q_J e^{s₂Q_J}, with
  e^{sX} = cos s + X sin s for a unit pure quaternion X, and κ(s) = tr(ABA⁻¹B⁻¹). φ* on H¹ is u ↦ (x ↦ P u(φx)),
  with P ∈ SO(3) such that P Ad ρ(φx) P⁻¹ = Ad ρ(x). By the Wang sequence (H⁰ = 0), dim H¹(m004; ad) = dim ker(φ* − 1).
- imports: none
- premises on main: B1836 § 5 (the dimensions 0/0/3); B1656 and B1723's b1656_funcs (the frame's Q₈ constants, whose
  import brings numpy and mpmath); B1945
  (the channels as half-period shifts); B1653 (the null quaternion); register rows P-635 and P-567
- decisive script: relays/claims/sm_refile/r635_decisive.py, SHA-256 75501d78f067cd24, depends on the standard library,
  sympy, numpy and mpmath, run as python3 relays/claims/sm_refile/r635_decisive.py, output SHA-256 619e5931ac37bf8c
- decisive lines: 16 lines marked "DECISIVE:", SHA-256 619e5931ac37bf8c
- failing control: python3 relays/claims/sm_refile/r635_control.py
- second computation: none
- already on main?: `grep -il "boundary free\|ad Q₈\|ad Q8" frontier/*/FINDINGS.md` on be8c83d4f: B1836 only (the
  dimensions, without the boundary motion, the family or the monodromy); closest arc B1836
- what would make it fail: any of the following.
  - H¹ ≠ 0 on the closed torus, H¹ ≠ 3 with the boundary free, or H¹_par ≠ 0 with it held.
  - A boundary-free direction keeping κ at −2: a restriction rank below 3, or a κ Hessian at 0 that is not positive
    definite.
  - The lines' restriction to the boundary not zero.
  - dim ker(φ* − 1) ≠ 1.
  If any of these happens, the pricing sentence (FL-08 prices only the 2 line classes; holding the cusp at −1 removes
  all 3 Q₈ classes; on m004, 1 survives) is withdrawn. The CKM corner along the family is not claimed: it is undefined
  in the frame as built.
