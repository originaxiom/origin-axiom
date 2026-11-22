# Scope Card `AGY-EXP_X-E6PS-LINK23` — Anomaly-Free `6D` Orbifold $E_6 \to G_{\mathrm{LR}} \times \mathbb{Z}_{18}^{\mathrm{hol}}$ Three-Generation Matter, Right-Handed Seesaw ($M_R \neq 0$), and $P_M = -1$ Majorana Dark-Matter Closure (`0 of 19`)

- **Seat / Branch:** `agy-exp` (`origin/agy/self-consistent-loop-2026-11-11`)
- **Date:** `2026-11-22`
- **Target Missing Links:** Links `#2` (`3-generation chiral matter + UV gravity cap M_g < 31 + Yukawa holomorphy`)
  and `#3` (`nonzero right-handed Majorana neutrino mass M_R != 0 + unbroken P_M = -1 dark matter + freedom from`
  `OW19-B1's 10^{25} Z'_psi Higgs wall and OW19-B3's 1/M_{11}^2 Planck suppression`).
- **Empirical Firewall:** Strictly `0 of 19` (`zero empirical PDG/NuFIT/Planck/CODATA constants`).

## Pre-Registered Expectations & Pass Gates (`E1`–`E6` + `6` Planted Controls)

1. **`E1` — Coroot Orbifold Multiplet-Splitting on $E_8 \supset E_6 \times \mathrm{SU}(3)_{\mathrm{fam}}$ (`PC_L23_1`):**
   - Expect $u_1 = (0,0,0,0,0,-2,-2,-2)$, $u_2 = (0,0,0,1,1,0,0,0)$, $u_3 = (2,2,2,0,0,0,0,0)$ to lie strictly
     in $Q^\vee(E_6) \subset \Lambda_{E_8}$, with $(v_1,v_2,v_3) = (u_1/6, u_2/2, u_3/16)$ + $\mathbb{Z}_2^{\mathcal{C}_\psi}$
     breaking $\mathfrak{e}_6$ (`dim 78`) to $\mathfrak{g}_{\mathrm{LR}} = \mathfrak{su}(3)_C \oplus \mathfrak{su}(2)_L \oplus \mathfrak{su}(2)_R \oplus \mathfrak{u}(1)_{B-L}$
     (`dim 15`), preserving all $3\times 16 = 48$ chiral spinor weights (`vs planted AGY-C26:261 w_WL leaving 0/128`),
     isolating $\Phi_{1,2} = (\mathbf{1},\mathbf{2},\mathbf{2})_0$ (`dim 4` each in $\mathbf{27}_{H,1,2}$) and $S = (\mathbf{1},\mathbf{1},\mathbf{1})_0$
     (`dim 1` in $\mathbf{27}_{H,S}$) away from color triplets $D_3, \bar{D}_3$, isolating pure
     $\overline{\Delta}_R = (\mathbf{1},\mathbf{1},\mathbf{3})_{-2}$ (`dim 3`) and $\Delta_L = (\mathbf{1},\mathbf{3},\mathbf{1})_{+2}$
     (`dim 3`) inside $\mathbf{351}'_H = (\overline{\mathbf{27}}\otimes\overline{\mathbf{27}})_{\mathrm{sym}}\ominus\mathbf{27}$,
     and satisfying exact 6D $E_6$ quartic trace factorization $\mathrm{Tr}_{\mathbf{27}} F^4 \equiv \frac{1}{12}(\mathrm{Tr}_{\mathbf{27}} F^2)^2$
     and $\mathrm{Tr}_{\mathbf{78}} F^4 \equiv \frac{1}{2}(\mathrm{Tr}_{\mathbf{27}} F^2)^2$ (`zero irreducible 6D Tr F^4 anomaly`).
2. **`E2` — Continuous, Witten Global, & Discrete $\mathbb{Z}_3^{\tau_3}$ (`mod 9`) Anomalies + Unique $N_{\mathrm{gen}} = 3$ (`PC_L23_2`):**
   - Expect all `10` continuous $G_{\mathrm{LR}}$ anomalies, both Witten $\pi_4(\mathrm{SU}(2)_{L,R}) = \mathbb{Z}_2$
     anomalies, and all `6` Ibáñez-Ross / Dreiner-Luhn-Thormeier (`including mod-9 cubic [Z_3]^3`) discrete
     anomalies on $N_{\mathrm{gen}}\times(\mathbf{16}_{\tau_3=+1} \oplus \chi_{S,\tau_3=-1})$ to vanish iff
     $3 \mid N_{\mathrm{gen}}$, intersecting DEP $M_g = N_S + 17 N_{\mathrm{gen}} - 4 N_V < 31$ (`M_g(3) = 15` in
     chiral $G_{\mathrm{LR}}$, `13` in $G_{\mathrm{SM}}+S$; `M_g(4) = 32 > 31`) uniquely at $N_{\mathrm{gen}} = 3$.
3. **`E3` — $\mathbb{Z}_{18}^{\mathrm{hol}}$ Holomorphy, Two-Bidoublet Projector Splitting, & `1`/`2`-Loop Unification at $r_{\mathrm{LR}} = 2/5$ (`PC_L23_3`):**
   - Expect $q_{18} \equiv 6\tau_3 + 3(B-L) \pmod{18}$ to remain unbroken under $\langle\overline{\Delta}_R^0\rangle \neq 0$
     ($q_{18} = 0$), allow $Q Q^c\Phi_{1,2}$, $L L^c\Phi_{1,2}$, $L^c L^c\overline{\Delta}_R$, $S H_u\cdot H_d$,
     $S^3$, and $S^*\chi_S^2$, and forbid $Q Q^c\tilde{\Phi}_{1,2}$ and $L L^c\tilde{\Phi}_{1,2}$ ($q_{18} = 6$).
   - Expect rank-`1` $\langle\overline{\Delta}_R\rangle$ projectors to split $(H_{u1}, H_{d2})$ (`mass 0`) from
     heavy $(H_{d1}, H_{u2})$, hit $B_{\mathrm{eff}} = 5/7$ at exact $r_{\mathrm{LR}} = 2/5$ (`chiral`) and
     $8/25$ (`D-parity`), reproduce Buttazzo/MV `1HDM` `3x3` $b^{(2)}$ (`err 0`), and pass `2`-loop `N=2000 vs 4000`
     step-halving `< 10^{-11}`. (`Revision note: v1 at c67688b13 preserved untouched; v2 fixes D_3 phase key`
     `2/16 = 1/8, 7/8 and refines RK4 grid N=120 -> 2000 before v2 run.`)
4. **`E4` — Full-Rank Seesaw $M_R \neq 0$, Holomorphic $V_{\mathrm{CKM}} \neq I_3$, & `2`-Flavor Leptogenesis (`PC_L23_4`):**
   - Expect two-bidoublet punctured-torus holomorphic matrices $(Y_u, Y_d, Y_e, Y_\nu, Y_R)$ to yield
     $\det M_R \neq 0$, hierarchical $V_{\mathrm{CKM}} \neq I_3$ (`vs planted 1-bidoublet V_CKM == I_3`), and
     `SU(3)^5 x U(3)_{N_R}` basis-scrambling invariance `< 10^{-30}` across all mass, CKM, PMNS, and `2`-flavor
     ($\tau$ vs coherent $e+\mu$) leptogenesis observables.
5. **`E5` — Unbroken $P_M = (-1)^{q_{18}+2s}$, `3x3` Pseudoscalar Mixing ($\det\mathcal{M}_{\mathrm{phys}}^2 > 0$), & $s$-Wave Majorana DM (`PC_L23_5`):**
   - Expect $P_M = +1$ on all scalar VEVs/SM fermions and $P_M(\chi_{S,a}) = -1$, exact single EW Goldstone
     $\mathcal{M}_{\mathrm{odd}}^2 g_{\mathrm{EW}} = 0$ with $\det\mathcal{M}_{\mathrm{phys},2\times 2}^2 = \frac{3\kappa_S\mu_{SH}v_S^2 v_{\mathrm{EW}}^2}{2 v_u v_d} > 0$,
     and explicit $4\times 4$ Dirac Clifford trace giving unsuppressed $s$-wave ($v_{\mathrm{rel}}^0$)
     pseudoscalar-portal annihilation $\sigma v_{\mathrm{rel}}|_{v\to 0} > 0$ (`overcoming OW19-B3's 1/M_{11}^2`).
6. **`E6` — Radiative Higgs Stability (`Zero Z'_psi Wall`), `6D` Bulk Casimir, & Honest Guardrail-`5` Ledger (`PC_L23_6`):**
   - Expect zero 4D $Z'_\psi$ gauge tadpole, intermediate-scale Vissani threshold suppression $> 10^{10}\times$
     relative to GUT-scale seesaw at $r_{\mathrm{LR}} = 2/5$, untwisted `6D` bulk Casimir $\Delta n_{\mathrm{Cas}} = -6 < 0$,
     and an explicit Guardrail-`5` continuous/discrete parameter ledger (`rejecting fake 0-parameter smuggling`).
