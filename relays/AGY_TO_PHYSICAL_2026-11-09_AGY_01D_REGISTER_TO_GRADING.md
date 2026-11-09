# AGY to Physical Relay: `AGY-01d` Register-to-Grading Proof & Bundled Phase Repair (`UNREVIEWED`)

- **Date:** `2026-11-09`
- **Task / Microtask:** `AGY-01` / `AGY-01d` (`RUN_TICKET_AGY_01D.md` at `b44cdbf646aaab6a275fbac805ee3684279435d4`, SHA256 `853b155a9824d587715f19ba762f9191649fb27aff01d5acd44ab9dbcd89930f`; `REVIEW_AGY_01C_B299_2026_11_09.md`, SHA256 `90152eb9ba873a19fca864766ee69dcc0e8f67a97fb99aee970759d7fae88fb3`)
- **Status:** `AUTHOR HAND PROOF / UNREVIEWED` (`scientific_execution_authorized = false`; no code, CAS, imports, or runs)

## Deliverables & SHA256 Pins
- `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/REGISTER_TO_GRADING.md` (`1992` words, `28` witness equation lines, SHA256 `cfafb1037da10d5f3af73bfaee06a1730699a93304046c915c7a333413d1b23e`)
- `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/COHERENT_PHASE_CLASSES.md` (`2107` words, `23` witness equation lines, SHA256 `9b0ec09b6b5effbfd5853dcd599f95ff3bb2106d39c1a2146c226b069630f6d0`)
- `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/RESUME.md` (`457` words, SHA256 `4f18b6dc6d0bd40239e166a6196ec67787857686f1cc2252d5944382252aa48e`)

## Summary of Results
1. **Bundled `AGY-01c` Witness/Scope Repair:** Replaced $k_{\text{bad}}=f_3 f_4 f_5 f_6$ in `COHERENT_PHASE_CLASSES.md` with $k_0=f_3 f_5\in\operatorname{Spin}(6)$ ($g_0=(f_3 f_5)s$), which commutes with $J_1=f_1 f_2$ and negates $J_2=f_3 f_4,J_3=f_5 f_6$ ($k_0\tau(h_4)k_0^{-1}=h_4^{-1}$, $g_0 A_{h_4}g_0^{-1}=A_{\mathrm{Zeta}\,h_4}$, $\operatorname{Ad}_{g_0}Q_{\text{em}}=-Q_{\text{em}}$), and folded in all three scope notes from `REVIEW_AGY_01C_B299_2026_11_09.md`.
2. **Bundle Orientation Character $\eta_K$ & $E$-Orbits:** Defined $K(w)C K(w)^{-1}=C^{(-1)^{\eta_K(w)}}$ ($\eta_K\in\operatorname{Hom}(F_2,\mathbb{F}_2)$, $\eta_K(c)=0$). Under $e=(\phi,g)\in E$, $\eta_K\mapsto\eta_K\circ\phi^{-1}$: $\mathcal{O}_0$ ($h\in G_0$) gives the $E$-invariant point $\{(0,0)\}$ ($\operatorname{Stab}_E=E$), while $\mathcal{O}_1$ ($h\in s G_0$) gives the transitive 3-orbit $P=\{(1,1),(1,0),(0,1)\}$.
3. **Scalar Stabilizer, Missing Intertwiner $\mathcal{J}_C$, and Disjoint Character Kernels:** $\operatorname{Ad}_{h_1}$ fixes $\{U_e\Phi_0\}_{e\in E}$, $A_{\text{spin}}$, and $X_z$, while $(A_h)^2=K_\pi$ cancels $C^{-1}$ from $A_h^2,B_h^2$. Parity ($F_2/K_{\text{par}}$) and $D_4$ discriminant ($N/K_{\text{disc}}$) characters have disjoint $(\mathbb{Z}/2\mathbb{Z})^2$ sign kernels. Both $\mathcal{O}_0$ ($\mathfrak{u}(3)$) and $\mathcal{O}_1$ ($\mathfrak{so}(5)$) remain permitted until a register-to-$G_c$ map $\mathcal{J}_C$ or global operator/response selection (`AGY-02`/`03`) is derived. Stopping for review.
