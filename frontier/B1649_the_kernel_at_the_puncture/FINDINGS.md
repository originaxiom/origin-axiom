# B1649 — THE KERNEL AT THE PUNCTURE: for every Higgs at the fibre's puncture the theta triplet is a two-sided null vector, so with one fibre for both quark sectors the first generation is massless and unmixed at leading order; the 2–3 sector is free

**Verdict: PROVED.** Every cell holds as sealed. cc (main), 2026-10-14. Sealed `a1bd642a6` before the run. No data.
**0 of 19.** POINT_REGISTER P-116 (its leading-order half).

## 0. Seen first

As sealed: `VERDICT topic-sweep /massless (first )?generation|first generation|Cabibbo|block.diagonal|texture zero|rank.two|rank 2|two-sided|null vector|unmixed|CKM.*(zero|trivial)|V_us|kernel at the puncture/: 44 of 1419 arcs on main match (NEGATIVE 8, OPEN 3, PROVED 33)`
and, over the full text, `VERDICT topic-sweep /Cabibbo|massless first generation|first generation is massless|V_us/: 8 of 1419 arcs on main match (NEGATIVE 4, PROVED 4)`.
- The nearest are B1644 and B1646, which this arc extends. None derives the first generation's zero from the residue's
  kernel.
- **Literature:** a rank-two leading-order Yukawa and its block-diagonal CKM are a standard starting point; here the
  zero is derived.

## 1. The sealed run (`verification/the_kernel_at_the_puncture.py`, unchanged; `the_kernel_at_the_puncture.json`, `_run.txt`)

| cell | prediction | prior | result |
|---|---|---|---|
| **K1** | ‖Y(S)R‖ and ‖Y(S)ᵀR‖ below 1e-20 relative, at 6 τ × 4 random complex S = s₀𝟙 + a·(i, j, k), by contour residues at 30 digits | 92% | **HOLDS:** 4.6·10⁻³¹ and 2.8·10⁻³¹. B1642's antisymmetric null vector is B1644's R exactly. |
| **K2** | 5 random pairs (S_u, S_d) on one fibre: \|V_ud\| = 1, V_us, V_ub, V_cd, V_td and both m₁/m₃ below 1e-10 | 92% | **HOLDS:** \|1 − \|V_ud\|\| ≤ 2.2·10⁻¹⁶; the four zeros ≤ 3.4·10⁻¹⁶; m₁/m₃ ≤ 9.5·10⁻¹⁷ |
| **K3** | read-out: the rank of (S_u, S_d) ↦ (m_c/m_t, m_s/m_b, \|V_cb\|) | — | **3** (singular values 0.59, 0.49, 0.35); the random pairs give \|V_cb\| from 0.31 to 0.86 |
| **K4** | control: R made non-isotropic (θ₃² × 1.1) gives m₁/m₃ > 1e-3 and V_us or V_ub > 1e-3 | 90% | **HOLDS:** m₁/m₃ = 0.060, V_us = 0.028, V_ub = 0.017 |

## 2. What it says

- **The residue route fixes the first generation completely at leading order.**
  - For any Higgs content at the puncture, in any directions and any number of Higgs fields, the theta triplet R is a
    two-sided null vector of the coupling.
  - With both quark sectors on one fibre, the first generation is massless and does not mix: m_u = m_d = 0 and
    θ₁₂ = θ₁₃ = J = 0. That is five zeros, each fixed by Jacobi's identity (K4 shows they go when R is not isotropic).
- **The 2–3 sector is free.** m_c/m_t, m_s/m_b and \|V_cb\| are an open map of the Higgs data (K3), and B1646 shows why:
  each direction is a 2–3 mass matrix.
- **The quark count on this route at leading order** (B1643's C3, before any crossing):
  - five zeros fixed;
  - five numbers free (m_c, m_t, m_s, m_b, θ₂₃);
  - none predicted.
- **Context, not a test** (C1–C6 unmet; P-108 owed):
  - four of the five zeros sit close to nature: m_u/m_t ≈ 10⁻⁵, m_d/m_b ≈ 10⁻³, θ₁₃ ≈ 0.004, J ≈ 3·10⁻⁵;
  - the Cabibbo angle, 0.227, does not;
  - so on this route the Cabibbo angle, the first generation's masses, θ₁₃ and J all come from whatever lifts R.

## 3. Owed (POINT_REGISTER)

- **What lifts R.** The Wilson line on the fibre (the SM seat's §66) is the first candidate. Its twisted zero mode must
  be derived by hand before any seal; the crux is whether the flat connection's relative phase between the doublet's
  components cancels in ε. If it enters as θ_r(ū)θ_r(δ), a classical identity gives R·R ∝ θ₁(ū)²θ₁(δ)², and with
  hypercharge as the charge the three charged sectors get different R's (firewalled; P-128).
- The leptons by the same reading: a trivial PMNS first row at leading order, against a large θ₁₂, unless the lepton
  sector's R differs.

## 4. Files

`verification/the_kernel_at_the_puncture.py` (sealed, unchanged), `controls.py` (run before the seal),
`the_kernel_at_the_puncture.json`, `the_kernel_at_the_puncture_run.txt`; the lock
`tests/test_b1649_the_kernel_at_the_puncture.py`.
