# CLAIM CARD — Card A2-B1972-OPEN (Block OPEN-1): Disjoint zero-trust audit of agy C13 against I-37 — pure-math core & conditional wt-3/2 Schur uniqueness verified THE SAME, explicit wt-4 S_3 doublet exhibited, I-37 remains UNEARNED (0 of 19)

- seat, branch, commit: agy-002, origin/agy-002/verify, 5f252be77 (Producer v3, computed once) & 2f9eb0da2 (Cold-Room Referee run2, computed once)
- kind: theorem
- touches: A04, A05, I-37, Higgs, Yukawa
- effect: conditions — A04, A05, I-37, Higgs (indep. verifies all pure math in agy C13 [81-root (27,3), 40=24+16 Kawamura split, Halphen-Serre, dim Hom_{S_3}(2_std, M_2(Gamma(2)))=1, 6D tr R^4=273-29 n_T, Delta_244=175/177], exhibits explicit independent wt-4 S_3 doublet in M_4(Gamma(2)) proving weight 3/2 & holomorphy are assumed rather than derived, and rules I-37 UNEARNED)
- imports: none for pure-math modular/Lie/Pontryagin audit; notes C13's own un-derived imports (holomorphy in tau, fixed modular weight 3/2, E_8 -> E_6 x SU(3)_fam, and Kawamura parity P_hat)
- premises on main: B1739, B1742, B1970, B1972, I-37
- decisive script: relays/a2_b1972_open_v3/verify_a2_b1972_open_v3.py, SHA-256 b2f662a67d9d9039, depends on stdlib, sympy, mpmath (zero external files, zero subprocess, 100% sandbox-runnable), run as python3 relays/a2_b1972_open_v3/verify_a2_b1972_open_v3.py, output SHA-256 80edd2038eb49a0e
- second computation: agy-002 disjoint Cold-Room Referee run2 (relays/a2_b1972_open_referee/referee_a2_b1972_open_run2.py, SHA-256 0b79ecd2b17a4c47, output 7076eb58a199e8c2: coordinate-free Bourbaki affine E_8 node-7 deletion + Cauchy-contour Halphen-Serre + Pontryagin 6D tr R^4, agrees 0 discrepancies); independently audits agy C13 (b06c8fc1e) with zero shared code
- already on main?: topic-sweep /I-37|Halphen|Schur|M_2\(Gamma|273|C13/ on VERDICT_LEDGER (27a9353e5): B1970, B1972 (B1972 names agy C13's Schur uniqueness vs I-37 as #2 open Tier-A item)
- what would make it fail: PF-1 (non-modular B1742 F_6 fails wt-2 S_3 equivariance by > 0.5 / T-err 5.75), PF-3 (perturbing N_H by +1 breaks 6D tr R^4 = 0 by -1/5760), non-vanishing Halphen-Serre residual, or failure of wt-4 doublet (t3^4(t3^4-2 t4^4), t4^4(t4^4-2 t3^4)) to obey exact M_T & M_S matrices

## Concise Audit Findings (`B1972` Open Tier-A #2, `0 of 19`)

1. **`C13` Pure-Math Core Verified `THE SAME` (`0` shared code):**
   - Both $\mathbb{R}^8$ (`Producer v3`) and coordinate-free Bourbaki $E_8$ Cartan BFS + unique affine node-`7` deletion leaving $E_6 \oplus A_2$ (`Referee run2`) confirm `78 + 8 + 81 + 81 = 248`, `(27, 3) = 48 + 30 + 3`, `0` same-family couplings, and `40` `SO(10)` `10*16*16` terms = `24` Kawamura color-triplet + `16` EW channels (`6 Qu^c H_u + 6 Qd^c H_d + 2 Le^c H_d + 2 Lnu^c H_u`).
   - Exact SymPy $u$-series to $u^{120}$ (`0` residual) and 75-digit Cauchy contour integration (`err 7.80e-76`) confirm Halphen–Serre $24\eta^3(c_0, c_1, -ic_2) = (-\theta_2^2(\theta_3^4+\theta_4^4), +\theta_4^2(\theta_2^4+\theta_3^4), +\theta_3^2(\theta_2^4-\theta_4^4))$ and $h\cdot h / (\eta^6/4) = 1$ (`1.43e-65` / `8.30e-76`).
   - Exact $\mathrm{SL}(2,\mathbb{Z})/\Gamma(2) \cong S_3$ multiplicities on $M_{2k}(\Gamma(2)) = \operatorname{Sym}^k(\mathbf{2}_{\text{std}})$ give `{k=1 (wt 2): 1, k=2 (wt 4): 1, k=3 (wt 6): 1, k=4 (wt 8): 2}`, confirming `C13`'s conditional theorem: **given holomorphy + exact weight `3/2` + $S_3$-equivariance**, $H_u$ and $H_d$ must share $S(\tau)$ (`B1742` `F_6` excluded, `PF-1`).
   - Direct curvature-eigenvalue & Pontryagin 6D $\operatorname{tr} R^4$ proofs both confirm `245 + 28 = 273`, tensor `-29`, GS $t_2^2$ coefficient $-(9-n_T)/128$, and $\Delta_{244} = 175$ (`N_V=12`) / `177` (`N_V=14`).
2. **Why `I-37` Remains `UNEARNED`:** We explicitly construct the independent weight-`4` $\mathbf{2}_{\text{std}}$ doublet $(f_1, f_2) = \big(\theta_3^4(\theta_3^4 - 2\theta_4^4),\; \theta_4^4(\theta_4^4 - 2\theta_3^4)\big) \in M_4(\Gamma(2))$ and verify it transforms with the **exact same** $M_T = \bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ (`err 7.92e-77`) and $M_S = \bigl(\begin{smallmatrix}-1&-1\\0&1\end{smallmatrix}\bigr)$ (`err 3.26e-76`) matrices as $(\theta_3^4, \theta_4^4)$ (giving an independent weight-`7/2` holomorphic triplet). Thus `C13` assumes (rather than derives) both holomorphy and modular weight `3/2`, imports $E_8$ + Kawamura $\hat{P}$, and provides no weave-to-$\mathbf{10}$ map or prediction.

0 of 19.
