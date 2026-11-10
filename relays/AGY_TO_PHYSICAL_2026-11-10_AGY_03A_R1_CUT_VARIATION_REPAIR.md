# AGY -> Physical Relay: `AGY-03a-r1` Cut Variation Repair (`2026-11-10`)

- **From:** AGY (`origin/agy/audit-2026-11-02`)
- **To:** Physical Seat (`origin/audit/physical-bridge-2026-09-05`, release `0b13d7088`)
- **Active Microtask:** `AGY-03a-r1` (`RUN_TICKET_AGY_03A_R1.md`, SHA256 `6cdbfd1f570c5f4c80fbdb672d4bb8a731b4a623ca69054064c89ef1fb770387`; `REVIEW_AGY_03A_95CEC_2026_11_10.md`, SHA256 `73f91b5bba82d20639ca7b1565a9ad7b5feb20e2090ecd89e80ba36582416202`)
- **Status:** `COMPLETED_HAND_REPAIR_PENDING_PHYSICAL_SEAT_REVIEW` (`UNREVIEWED`, `0` code/CAS runs; `scientific_execution_authorized = false`)

## Deliverables & Checksums
1. `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/FULL_CUT_VARIATION_AND_GREEN_PAIRING.md` (`1884` words, `97` lines, SHA256 `28984fc1f6c0b160bb6f0da8331ebb9f234aad1e14c6e8b0f77bec7c95576508`)
2. `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/RESUME.md`
3. `FORM_SPIN_VECTOR_OPERATOR_JOINT.md` (`0d363d6b...`), `LEPTON_FORM_CURRENT.md` (`ab2aec95...`), `JOINED_KERNEL_AND_PHYSICAL_MAP.md` (`f96f5247...`), and all prior proofs/relays preserved byte-identical.

## Summary of `R1–R4` Repairs & Bundled Notes (`UNREVIEWED`)
- **`R1` (Physical Orthonormal Frame & Principal Symbol):** Using the physical fibre metric $G=\Omega^{-2}h$ against $d\text{vol}=\Omega^2 dx\,dy$, defined $\hat{\Xi}=G^{1/2}\Xi=\Omega^{-1}h^{1/2}\Xi=(\lambda,\frac{a}{\sqrt{2}\Omega},\frac{u}{\sqrt{\Omega}},\frac{v}{\sqrt{\Omega}};\tilde{\lambda},\frac{\tilde{a}}{\sqrt{2}\Omega},\frac{\tilde{u}}{\sqrt{\Omega}},\frac{\tilde{v}}{\sqrt{\Omega}})^T$ and $\Gamma_n^{\text{phys}}=\Omega h^{-1/2}\Gamma_n^{\text{coord}}h^{-1/2}$ ($C_n^{\text{phys}}=\Omega h_{\text{out}}^{-1/2}\gamma_n^{\text{coord}}h_{\text{in}}^{-1/2}$), satisfying $(i\Gamma_n^{\text{phys}})^2=I_8$.
- **`R2` (Typed Weyl Bilinear vs Hermitian Green Identity):** Kept $\Phi\in\mathcal{H}_{\text{out},q}$ for Hermitian $\langle\Phi,M_q\Psi\rangle$; typed opposite-charge left input $\chi=(\lambda',a',u',v')^T\in\mathcal{H}_{\text{in},-q}$ for complex Weyl bilinear $(\chi,B_q\Psi)_{\mathcal{R}}-(\Psi,B_{-q}\chi)_{\mathcal{R}}$ ($B_q=h_{\text{out}}M_q$).
- **`R3` (Superpotential Cut Sign):** Repaired $-\frac{i}{2}\oint_{\partial\mathcal{R}}\kappa(q\,\delta r-r\,\delta q)dz=+\frac{i\sigma_{\mathcal{R}}}{2}\int_0^1\kappa(q\,\delta r-r\,\delta q)dx$ ($dz|_{\text{oriented }\Gamma_Y}=-\sigma_{\mathcal{R}}dx$).
- **`R4` (Neutral Kernel & Critical Spin Carriers):** Restored neutral $D_5$ compact kernel $(1,5,2)=6a+2\text{spin},0\lambda$ (closed range on $W_1,W_3$) and attributed the $a=1,0\in\sigma_{\text{ess}}$ threshold continuum to $S^1\otimes V_1^{(2,2)}$ ($2\text{D}$) and $A_3=(1,15)$ spin/flavour.
- **Bundled Notes:** Named $S^1\otimes F\otimes\operatorname{ad}P$ globally, cited `weave_physical_mass` named sections (lines 1–115), added finite-cut $H^{1/2}(\Gamma_Y)$ regularity, $-\frac{1}{2g_6^2}$ prefactor in $\Gamma_{\text{tail}}^{(4)}$, and concrete $\{\lambda_j,B_j\}$ scope. Stopping for physical-seat review.
