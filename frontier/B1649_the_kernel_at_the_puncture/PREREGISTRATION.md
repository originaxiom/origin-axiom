# B1649 — PREREGISTRATION: THE KERNEL AT THE PUNCTURE — the theta triplet is massless for every Higgs at the fibre's puncture, so with one fibre for both quark sectors the first generation is massless and unmixed at leading order

cc (main), 2026-10-14. **Sealed before `the_kernel_at_the_puncture.py` runs.** No data. 0 of 19. POINT_REGISTER P-116.

**Why it matters.** P-116 asks for the quark count before any crossing (B1643's C3). B1646 showed that a Higgs in M
leaves the 2–3 sector free: its direction is the 2–3 mass matrix. This arc asks what the residue route fixes in the
first generation, for every Higgs at the puncture and not only one in M, and for two sectors at once.

**The derivation, by hand, written before the run.**
1. **Every Higgs at the puncture.**
   - The residue coupling Y(S)_pq = res F_pᵀ ε S F_q is linear in S ∈ End(ℂ²) = span(𝟙, i, j, k).
   - For S = 𝟙 it is B1642's antisymmetric [v]×, whose null vector is the theta triplet; that is B1642's sealed
     result, "one exactly massless state along the θ-triplet itself".
   - For S = a in M it is B1644/B1645's a Rᵀ + R aᵀ − (a·R)𝟙, and Y R = a(R·R) = 0 by Jacobi.
   - So **Y(S) R = 0 for every S.** Since Y(S)ᵀ = −Y(s₀𝟙) + Y(a), also **Rᵀ Y(S) = 0**: R is a two-sided null vector, at
     every τ, for any number of Higgs fields in any SU(2) content at the puncture.
2. **Two sectors on one fibre.**
   - If the up and the down sectors couple to the same zero modes (one τ, one R), each sector's left massless state is
     R̄ (the left singular vector of the zero singular value).
   - The mixing matrix V = W_uᴴ W_d then has |V₁₁| = 1 and V₁ⱼ = Vⱼ₁ = 0 for j ≠ 1: **V = 1 ⊕ U(2).**
   - At leading order m_u = m_d = 0, θ₁₂ = θ₁₃ = 0, and J = 0.
3. **The count (K3).**
   - The 2–3 block of each sector is free (B1646).
   - With two sectors, the map from the Higgs data to (m_c/m_t, m_s/m_b, |V_cb|) should have full rank 3: nothing in the
     2–3 sector is predicted.
4. **The control (K4).** With R made non-isotropic, Y R = a(R·R) ≠ 0. The zero and the block structure then fail, so the
   zeros come from Jacobi's identity.

## Seen first

`VERDICT topic-sweep /massless (first )?generation|first generation|Cabibbo|block.diagonal|texture zero|rank.two|rank 2|two-sided|null vector|unmixed|CKM.*(zero|trivial)|V_us|kernel at the puncture/: 44 of 1419 arcs on main match (NEGATIVE 8, OPEN 3, PROVED 33)`
— word matches. The only CKM arc is B467, the orientation bit, in another setting.
Full text (Review 63's P-123): `VERDICT topic-sweep /Cabibbo|massless first generation|first generation is massless|V_us/: 8 of 1419 arcs on main match (NEGATIVE 4, PROVED 4)`
— B1644 and B1646, which this arc extends; B1612; and earlier numerical-match negatives (B322, B706). None derives the
first generation's zero from the residue's kernel.
**Literature:** a rank-two leading-order Yukawa with a massless first generation, and the block-diagonal leading-order
CKM it gives, is a standard flavour-model starting point. The Gatto–Sartori–Tonin relation θ₁₂ ≈ √(m_d/m_s) is known
for textures whose (1, 1) entry vanishes. Here the zero is derived, not chosen.

## Disclosed

- Steps 1 and 2 follow from two sealed, banked results (B1642, B1644) by linearity, so K1 and K2 are checks of a
  derivation, not blind predictions.
- The plumbing was tested before the seal on banked or algebraic cases only (`controls.py`): B1642's own case S = 𝟙
  is antisymmetric; the closed form kills an isotropic vector; the mixing routine returns the identity for identical
  sectors. No cell was computed.
- A first draft defined its helpers after the cells. The controls caught it, and the helpers were moved above.
- **Context, not a test** (B1643's C1–C6 are unmet; the adjoint Higgs at the puncture still needs its parent map,
  P-108):
  - the observed m_u/m_t ≈ 10⁻⁵, m_d/m_b ≈ 10⁻³, θ₁₃ ≈ 0.004 and J ≈ 3·10⁻⁵ are small;
  - the Cabibbo angle 0.227 is not;
  - so if K2 holds, the Cabibbo angle must come entirely from what lifts R.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **K1** | at 6 random τ × 4 random complex S = s₀𝟙 + a_i i + a_j j + a_k k, computed by the residue in mpmath (30 digits): ‖Y(S)R‖ and ‖Y(S)ᵀR‖ are below 1e-20 relative to ‖Y‖‖R‖ (B1642's R2 gives its null vector in the units' labels as (−θ₂², −θ₄², iθ₃²), which is B1644's R; a sign convention could still differ) | 92% |
| **K2** | 5 random pairs (S_u, S_d) at one τ: \|V_ud\| = 1 within 1e-10, and V_us, V_ub, V_cd, V_td below 1e-10 (double precision after the residues); both sectors' m₁/m₃ below 1e-10 | 92% |
| **K3** | read-out: the Jacobian of (S_u, S_d) ↦ (m_c/m_t, m_s/m_b, \|V_cb\|) over the 16 real Higgs parameters has rank 3 | — |
| **K4** | control: with θ₃² scaled by 1.1 in R (non-isotropic), m₁/m₃ > 1e-3 and \|V_us\| or \|V_ub\| > 1e-3 | 90% |

**The reading (the cells can only lower it).** If K1, K2 and K4 hold:
- **The residue route fixes the first generation completely at leading order.** For any Higgs content at the puncture
  and any directions, the first generation is massless and unmixed in both quark sectors: m_u = m_d = 0 and
  θ₁₂ = θ₁₃ = J = 0. The 2–3 sector is free (K3).
- **The quark count on this route at leading order:**
  - five zeros, fixed by Jacobi's identity;
  - five free numbers (m_c, m_t, m_s, m_b, θ₂₃), which the Higgs data reproduce without constraint.
- **What lifts R decides the rest:** the first generation's masses, the Cabibbo angle, θ₁₃ and J. The next arc reads
  the Wilson line on the fibre (the SM seat's §66), with its zero mode derived by hand first.

## Instruments

`verification/the_kernel_at_the_puncture.py` (B1642's sealed residue machinery reused unchanged); `verification/controls.py`
(run before the seal); hashes in `ARTIFACT_HASHES.txt`.
