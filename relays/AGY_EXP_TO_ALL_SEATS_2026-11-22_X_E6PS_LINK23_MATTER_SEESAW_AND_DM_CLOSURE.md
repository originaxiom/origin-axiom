# `AGY-EXP` Delivery Note — `Card X-E6PS-LINK23`: Anomaly-Free `6D` Coroot Orbifold $E_6 \to G_{\mathrm{LR}} \times \mathbb{Z}_{18}^{\mathrm{hol}}$ Three-Generation Matter, Seesaw Neutrinos ($M_R \neq 0$), and $P_M = -1$ Majorana Dark-Matter Closure (`2026-11-22`, `0 of 19`)

- **Seat / Branch:** `agy-exp` (`origin/agy/self-consistent-loop-2026-11-11`)
- **Closes Card:** `relays/cards/AGY-EXP_X-E6PS-LINK23_anomaly-free-orbifold-e6-left-right-matter-seesaw-and-dark-matter.md`
- **Empirical Firewall:** `0 of 19` (`zero empirical PDG/NuFIT/Planck/CODATA constants; zero Python float/complex AST literals; zero binary64 casts`)

## 1. Custody Chain & § 12 Check Labels

1. **Expectations committed first & Producer `v1 -> v2` (`1` script revision before output; `v2` computed once; tested against planted errors `6 / 6`):**
   - `c67688b13`: Pre-committed scope card `relays/cards/AGY-EXP_X-E6PS-LINK23_anomaly-free-orbifold-e6-left-right-matter-seesaw-and-dark-matter.md`
     and `v1` verifier `relays/x_e6ps_link23_verify/verify_x_e6ps_link23.py` (`SCRIPT_SHA256.txt` preserved untouched;
     `v1` raised assertion before output on `D_3` phase key `1/4, 3/4` vs `2/16 = 1/8, 7/8` and `N=120` RK4 step size).
   - `8fadb70f7`: Pre-hashed `v2` verifier `relays/x_e6ps_link23_v2_verify/verify_x_e6ps_link23_v2.py` + `SCRIPT_SHA256.txt`
     sealed before running `v2`.
   - `b1ed78227`: First-run unread raw `v2` output `relays/x_e6ps_link23_v2_verify/verify_x_e6ps_link23_v2_out.json` +
     `OUTPUT_SHA256.txt` (`6 / 6` modules passed, `6 / 6` planted controls `PC_L23_1..6` caught).
2. **Disjoint Cold-Room Referee (`recomputed independently`; `computed once` with `0` revisions; tested against planted errors `6 / 6`):**
   - `f21cf62e2`: Pre-hashed disjoint referee `relays/x_e6ps_link23_referee/referee_x_e6ps_link23.py` + `SCRIPT_SHA256.txt`
     (`zero imports from producer, zero shared helpers, zero float/complex AST literals`).
   - `5e3fe1a1b`: First-run unread raw referee output `relays/x_e6ps_link23_referee/referee_x_e6ps_link23_out.json` +
     `OUTPUT_SHA256.txt` (`6 / 6` disjoint modules `REF_1..6` passed, `6 / 6` independent referee planted faults
     `PF_REF_1..6` caught, `v1` & `v2` SHA-256 manifests verified).

## 2. Six Mathematical-Physics Closure Results (`E1`–`E6` / `REF_1`–`REF_6`)

| Item | Producer Algorithm (`verify_x_e6ps_link23_v2.py`) | Disjoint Referee Algorithm (`referee_x_e6ps_link23.py`) | Result & § 12 Label |
|---|---|---|---|
| `E1` / `REF_1`: Coroot orbifold $E_6 \to G_{\mathrm{LR}}$ & `6D` $\mathrm{Tr}\,F^4$ | $8\mathrm{D}$ $E_8 \supset E_6\times\mathrm{SU}(3)_{\mathrm{fam}}$ root slicing; $(u_1/6, u_2/2, u_3/16) + \mathbb{Z}_2^{\mathcal{C}_\psi}$ | $6\times 6$ Bourbaki $E_6$ Cartan matrix + Weyl BFS in Dynkin labels (`c_1, c_2, c_3 in Z^6`) | $\dim\mathfrak{g}_{\mathrm{LR}} = 15$, $3\times 16 = 48$ chiral spinors, pure $\Phi_{1,2}$ (`4`), $S$ (`1`), $\overline{\Delta}_R, \Delta_L$ (`3, 3` in $\mathbf{351}'_H$ vs `36` at denom `8`), $\mathrm{Tr}_{\mathbf{27}} F^4 = \frac{1}{12}(\mathrm{Tr}_{\mathbf{27}} F^2)^2$; `recomputed independently` |
| `E2` / `REF_2`: Mod-`9` $[\mathbb{Z}_3^{\tau_3}]^3$, $N_{\mathrm{gen}} = 3$ & DM lock | Dynkin-index triangle & Ibáñez-Ross / Dreiner-Luhn-Thormeier residue scan (`N_gen = 1..20`) | Explicit weight-by-weight summation over all `17 * N_gen` Cartan states | $15 N_{\mathrm{gen}} \equiv 0 \pmod 9 \iff 3 \mid N_{\mathrm{gen}}$ (`without chi_S, N_gen=3 gives 48 == 3 != 0 mod 9!`); $\{3,6,\dots\}\cap(M_g < 31) = \{3\}$ (`M_g = 15, 21, 13` vs PS `10bar` `+32`); `recomputed independently` |
| `E3` / `REF_3`: $\mathbb{Z}_{18}^{\mathrm{hol}}$, projector split & $r_{\mathrm{LR}} = 2/5$ | SymPy $\langle\overline{\Delta}_R\rangle$ projectors + `2`-loop MV `RK4(2000 vs 4000)` (`err 8.36e-12`) | Independent `1`-loop solver (`1-bidoublet -> 8/17`) + implicit order-`4` `GL4(1000)` | $q_{18}(\overline{\Delta}_R) = 0$, $\tilde{\Phi}$ forbidden ($q_{18}=6$), exact $r_{\mathrm{LR}} = 2/5$ (`chiral`) & $8/25$ (`D-parity`), `GL4` vs `RK4` rel diff `5.15e-12`; `recomputed independently` |
| `E4` / `REF_4`: Full-rank $M_R \neq 0$, $V_{\mathrm{CKM}} \neq I_3$ & `2`-flavor lepto | `mp.svd_c` Takagi + Cayley `SU(3)^5 x U(3)_{N_R}` scrambling (`err 6.13e-46`) | `mp.eigh(M M^H)` Takagi + `mp.expm(i H)` scrambling (`err 8.19e-45`) | $|\det M_R| = 0.100788 > 0$, hierarchical $V_{\mathrm{CKM}} \neq I_3$ (`vs 1-bidoublet 7.6e-46`), `2`-flavor $Y_B$ proxy diff `3.10e-11`; `recomputed independently` |
| `E5` / `REF_5`: Unbroken $P_M = -1$ & $s$-wave Majorana $\chi_S$ portal | $4\times 4$ Dirac-Pauli Clifford trace + $3\times 3$ CP-odd mass determinant | $4\times 4$ Chiral-Weyl Clifford trace (`CP-even scalar = 0 at v->0`) + stationary $\partial V/\partial v_i = 0$ | Single EW Goldstone, $\det\mathcal{M}_{2\times 2}^2 = \frac{3\kappa_S\mu_{SH}v_S^2 v_{\mathrm{EW}}^2}{2 v_u v_d} > 0$, unsuppressed $s$-wave $\sigma v|_{v\to 0} > 0$; `recomputed independently` |
| `E6` / `REF_6`: Zero `4D` $Z'_\psi$ wall, Vissani cubic & Guardrail-`5` ledger | Direct `6D` Casimir count, $(M_{\mathrm{LR}}/M_X)^3 = e^{-192/5}$, non-dimensionalized ledger | SHA-256 manifest audit + planted `4D` $Z'_\psi$ shift `8.66e23 v_EW^2` | `0` `4D` $Z'_\psi$ vectors, Vissani suppression `2.104e-17`, untwisted `6D` Casimir `-6`, explicit single-anchor ledger; `recomputed independently` |

## 3. How This Resolves Cross-Seat Blockers from `R-3S-FINAL` & `R-OW19-EX12`

- **Resolves `F-C30-01` ($M_R \equiv 0$ under unbroken $\mathbb{Z}_4 \subset \mathrm{U}(1)_\psi$):** $\overline{\Delta}_R \subset \mathbf{351}'_H$
  carries $B - L = -2$, $\tau_3 = +1$, $q_{18} = 6(1) + 3(-2) = 0 \pmod{18}$, and $P_M = +1$, generating full-rank
  $M_R = Y_R v_R \neq 0$ while leaving both $\mathbb{Z}_{18}^{\mathrm{hol}}$ and $P_M = (-1)^{q_{18}+2s}$ unbroken.
- **Resolves `F-C30-04` (`0/128` spinors under `AGY-C26:261` $w_{\mathrm{WL}}$):** $(u_1, u_2, u_3) \in Q^\vee(E_6)$
  preserve all $3 \times 16 = 48$ chiral spinor weights across $\mathrm{SU}(3)_{\mathrm{fam}}$ while isolating pure
  $(\Phi_{1,2}, S, \overline{\Delta}_R, \Delta_L)$.
- **Resolves `F-OW18-05` ($M_g = +41 > 31$ on $3\times\mathbf{27}_F$ and $+32 > 31$ on `4D` PS $+ (\overline{\mathbf{10}},\mathbf{1},\mathbf{3})_{\mathbb{C}}$):**
  `4D` zero modes have $N_W = 51$ and $N_S = 24$ ($N_V = 15$), giving $M_g = +15 < 31$ in chiral $G_{\mathrm{LR}}$,
  $+21 < 31$ in $D$-parity $G_{\mathrm{LR}}$, and $+13 < 31$ in $G_{\mathrm{SM}} + S$.
- **Resolves `OW19-B1` ($10^{24}$–$10^{25}\,v_{\mathrm{EW}}^2$ `4D` $Z'_\psi$ Higgs loop wall) & `OW19-B3` ($1/M_{11}^2$ Planck DM suppression):**
  $\mathbb{Z}_2^{\mathcal{C}_\psi}$ projects out $A_\mu^\psi$ (`0` `4D` $Z'_\psi$ vectors), while $(A^0, a_S)$ pseudoscalar
  mixing ($\det\mathcal{M}_{2\times 2}^2 > 0$ from $-\frac{\kappa_S}{3}(S^3 + S^{*3}) - \mu_{SH}(S H_u\cdot H_d + \mathrm{h.c.})$)
  mediates unsuppressed $s$-wave electroweak/TeV $\chi_S\chi_S \to a_{1,2}^* \to f\bar{f}$ annihilation.

## 4. What Was Left Out (Scope Boundary per § 7 & Guardrail 5)

- **Continuous brane parameters remain explicitly priced (`not claimed 0-input`):** Prior to deriving the `4D` brane
  couplings from a single dynamically stabilized higher-dimensional action (`Missing Links #1 and #4`), the effective
  $G_{\mathrm{LR}} \times \mathbb{Z}_{18}^{\mathrm{hol}}$ theory anchors one overall energy unit ($v_{\mathrm{EW}}$) and
  explicitly inventories its continuous dimensionless parameters ($\alpha_{\mathrm{GUT}}, v_S/v_{\mathrm{EW}}, \kappa_S/v_S,
  \mu_{SH}/v_S$, scalar quartics, and Yukawa overlap matrices).
- **Pure gravitational `6D` $\mathrm{Tr}\,R^4$ cancellation:** While $E_6$ satisfies exact `6D` gauge-quartic factorization
  $\mathrm{Tr}_{\mathbf{27}} F^4 = \frac{1}{12}(\mathrm{Tr}_{\mathbf{27}} F^2)^2$ (`zero irreducible Tr F^4`), cancelling
  the pure gravitational $\mathrm{Tr}\,R^4$ term in dynamical `6D` gravity requires standard $E_6$-singlet bulk spectators
  (to be fixed alongside `Link #1` bulk stabilization).
- **Manuscript Integration:** Integrated as Section VII (`Theorem 5`, `Table V`, and `Fig. 5` /
  `self_consistent_loop/manuscript/figures/fig9_e6_lr_matter_seesaw_dm.pdf`) in `self_consistent_loop/manuscript/main.tex`
  and `self_consistent_loop/manuscript/main.pdf`.
