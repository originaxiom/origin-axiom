# Phase 9: `dP_8` Georgi–Jarlskog Tier-1 Promotion & Zero-Continuous-Input Gauge/Misalignment Audit (`125` of `125` Controls)

Clean-room (`0 of 19` Track-A empirical inputs, `0` continuous fitted/calibrated parameters) pre-registered implementation and zero-import referee suite advancing the self-consistent geometric loop on both fronts:

1. **Precision `Tier-1` Promotion (`12 -> 17` of `24` SM Dimensionless Observables):**
   - `src/phase9_toe/p9_1_dp8_georgi_jarlskog.py` — Blowing down `1` `(-1)`-curve from parabolic $dP_9$ ($\chi = 12$) to critical Fano $dP_8$ ($r_{\mathrm{crit}} = 8, \chi = 11$) shifts bulk collar localization masses by $m_{\mathrm{bulk}}^{(dP_8)}(f) = T_{3R}(f) - \frac{1}{12}(B-L)(f)$, while canonical $\mathrm{SU}(5) \subset \mathrm{Spin}(10)$ Georgi–Jarlskog couplings ($\overline{\mathbf{45}}_H$ on $y_H = -1/2$ `T1R`, exact diagonal antisymmetry $A_{ii} \equiv 0$ of $\mathbf{10}_f \otimes \mathbf{10}_f \to \overline{\mathbf{45}}_A$, and $P_\perp$ excited KK projection on $u_c$) promote $\sin^2\theta_{13}$, $m_c/m_t$, $m_d/m_s$, $m_e/m_\mu$, and $m_b/m_\tau$ into `Tier 1` (`17` Tier-1 + `7` Tier-2 = `24` of `24`, `0` Tier-3 misses, `10`-trial `SU(3)^5` Haar invariance `< 1e-11`).
2. **Elimination of All `3` Phase-8 Continuous Inputs (`3 -> 0` Continuous Inputs):**
   - `src/phase9_toe/p9_2_zero_input_couplings.py` — Summing the `S^1/Z_2` Contino–Pilo differential zeta threshold across both collar boundaries ($-2 \times \frac{1}{2}\ln\pi = -\ln\pi$) gives $\alpha_{\mathrm{GUT,2-wall}}^{-1} = 42.10164$; solving the internal fixed point $\ln(M_{\mathrm{KK}}/M_Z)_0 = \frac{15}{2}L_c^* - \ln(M_Z^{\mathrm{pred}}/v_{\mathrm{EW}}) = 29.49855$ predicts $\alpha_{\mathrm{EM}}^{-1}(M_Z) = 128.138$ (`+0.15%`, `Tier 1`), $\alpha_s(M_Z) = 0.1135$ (`-3.70%`, `Tier 1`), $v_{\mathrm{EW}}/M_{\mathrm{Pl,red}} = 1.1657\times 10^{-16}$ (`+15.3%`, `Tier 1`), and $\ln(M_{\mathrm{Pl,red}}/M_Z) = 37.6560$ (`-0.168` nepers vs. `37.8235`, `Tier 1`).
   - `src/phase9_toe/p9_3_thooft_coleman_misalignment.py` — `'t Hooft` UV–IR determinant alignment cancels the tree-level `m004` quark phase identically, and Coleman's dilute-instanton-gas partition minimum yields $\theta_{\mathrm{mis},0} = 0.04487\text{ rad}$, giving $\Omega_a h^2 = 0.06597$ (`Tier 2`, `Clause P9-C2`) and $\beta_{\mathrm{iso}}^{(1\text{B-SD})} = 0.01418 < 0.038$.
3. **Unified `36`-Observable Scorecard & `125`-Control Zero-Import Referee:**
   - `src/phase9_toe/p9_4_joint_zero_input_consistency.py`, `src/phase9_toe/track_b_phase9_scorecard.py`, and `scripts/referee_phase9.py` certify **`23` Tier-1 + `9` Tier-2 + `4` Bound/Vacuum Passes = `36` of `36` (`0` misses)** across **`125` of `125` cumulative planted-fault controls**.

## Reproduction

```bash
PYTHONPATH=src python3 -m phase9_toe.phase9_engine
python3 scripts/referee_phase9.py
python3 -m unittest discover -s tests -v
```
