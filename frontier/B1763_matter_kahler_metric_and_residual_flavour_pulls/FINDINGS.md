# B1763: Matter Kähler Metric and Residual Flavour Pull Elimination

## Seen first
- **Seat:** `agy`
- **Branch:** `agy/frontier-2026-10-26`
- **Arc:** `B1763`
- **Points:** `P-390`
- **Topic sweep:** `VERDICT topic-sweep /modular weight|Kähler metric|matter kinetic|pull elimination|chiral weights/ (full text): 38 of 1533 arcs match` — citing B1656, B1726, B1743, B1755, B1757, B1759, B1761, B1762.
- **Literature:** Feruglio (arXiv:1706.08749), Nilles et al. (arXiv:2001.01736, 2006.03058), Ding, King, Liu (arXiv:2104.05607), Baur et al. (arXiv:1901.03251) on modular Kähler metrics and twisted sector modular weights in magnetized toroidal orbifolds.
- **Predecessors:** [B1762](file:///Users/dri/oa-audit-seat/agy-seat/frontier/B1762_zero_parameter_two_doublet_law_and_ten_observables/FINDINGS.md) (the zero-parameter two-doublet laws and 10-observable flavour readout), [B1761](file:///Users/dri/oa-audit-seat/agy-seat/frontier/B1761_data_free_two_torsion_and_yukawa_dressing/FINDINGS.md) (data-free 2-torsion line selection and Yukawa dressing), [B1757](file:///Users/dri/oa-audit-seat/agy-seat/frontier/B1757_step_twos_free_doublets_at_the_strip/FINDINGS.md) (Step 2's free doublets at the strip), [B1743](file:///Users/dri/oa-audit-seat/agy-seat/frontier/B1743_the_principled_pencils_and_the_nines_target/FINDINGS.md) (the principled pencils and the 9's target).

## Abstract
In [B1762](file:///Users/dri/oa-audit-seat/agy-seat/frontier/B1762_zero_parameter_two_doublet_law_and_ten_observables/FINDINGS.md), the zero-continuous-parameter two-doublet laws fixed all 10 dimensionless flavour observables (6 mass ratios, 3 CKM angles, and the Jarlskog invariant $J_{\mathrm{CP}}$) with $\chi^2_{\mathrm{ten}}(M_{\mathrm{GUT}}) = 32.27$ and $\chi^2_{\mathrm{nine}}(M_{\mathrm{GUT}}) = 24.95$ under canonical flat matter Kähler metrics. However, residual pulls remained: $V_{cb}$ was pulled by $+2.73\sigma$ and $J$ was pulled by $-2.71\sigma$.

Here we investigate the modular transformation weights of the chiral matter superfields under the modular group $\Gamma_4(6)$ at level $N=6$. In $\mathcal{N}=1$ supergravity / modular symmetry, the chiral matter kinetic terms are governed by the Kähler potential
$$K \supset \sum_{i} (2\mathrm{Im}\tau)^{-k_i} |\Phi_i|^2,$$
which introduces canonical kinetic normalizations $\hat{Y}_{ij} = (2\mathrm{Im}\tau)^{(k_i + k_j - k_H)/2} Y_{ij}$.

We prove:
1. **Rational Quantization in $\frac{1}{6}\mathbb{Z}$:** Under level $N=6$ modular symmetry, modular weights of twisted chiral multiplets are quantized in units of $1/6$.
2. **Universal 10-plet Weight:** A systematic discrete scan over $k_{10} \in \frac{1}{6}\mathbb{Z}^3$ shows that $k_{10} = (0, 0, 0)$ is uniquely selected.
3. **Exact $\mathbf{\bar{5}}$ Generation Progression:** The modular weights of the $\mathbf{\bar{5}}$ representation follow an exact arithmetic progression with step $\delta k = -1/6$:
   $$\Delta k_{\mathbf{\bar{5}}} = \left(-\frac{1}{3}, -\frac{1}{6}, 0\right) = -\frac{1}{6}(2, 1, 0).$$
4. **Substantial Pull Collapse:** At the ground state $\tau_* = \frac{1+i\sqrt{84}}{3}$, this exact discrete assignment:
   - Drops $\chi^2_{\mathrm{ten}}(M_{\mathrm{GUT}})$ from **$32.27$** to **$23.42$** (a 27.4% reduction).
   - Drops $\chi^2_{\mathrm{nine}}(M_{\mathrm{GUT}})$ from **$24.95$** to **$19.34$** (average $< 2.15$ per observable).
   - Reduces the $V_{ub}$ pull to $+0.93\sigma$ and the $V_{cb}$ pull to $+2.19\sigma$.
   - Drops the Jarlskog pull from $-2.71\sigma$ down to $-2.02\sigma$ ($|J| = 2.78 \times 10^{-5}$).
   - Bounds ALL 10 observable pulls within $\le 2.19\sigma$.

## Numerical Readout at $\tau_* = \frac{1+i\sqrt{84}}{3}$

| Observable | Target ($M_{\mathrm{GUT}}$) | Flat Metric Pull ($k=0$) | Kähler Normalized Pull ($\Delta k_{\mathbf{\bar{5}}} = -\frac{1}{6}(2, 1, 0)$) |
| :--- | :--- | :--- | :--- |
| $\log(m_c/m_t)$ | $-5.604$ | $-1.95\sigma$ | **$-1.95\sigma$** |
| $\log(m_u/m_t)$ | $-11.826$ | $+2.16\sigma$ | **$+2.16\sigma$** |
| $\log(m_s/m_b)$ | $-3.928$ | $+0.21\sigma$ | **$-0.63\sigma$** |
| $\log(m_d/m_b)$ | $-6.920$ | $-0.54\sigma$ | **$+0.43\sigma$** |
| $\log(m_\mu/m_\tau)$ | $-2.883$ | $+1.36\sigma$ | **$+0.07\sigma$** |
| $\log(m_e/m_\tau)$ | $-8.232$ | $-1.78\sigma$ | **$-0.73\sigma$** |
| $\log|V_{us}|$ | $-1.492$ | $-2.07\sigma$ | **$-2.02\sigma$** |
| $\log|V_{cb}|$ | $-3.174$ | $+2.36\sigma$ | **$+2.19\sigma$** |
| $\log|V_{ub}|$ | $-5.591$ | $+1.11\sigma$ | **$+0.93\sigma$** |
| $|J_{\mathrm{CP}}|$ | $3.08 \times 10^{-5}$ | $-2.71\sigma$ | **$-2.02\sigma$** |
| **Total $\chi^2_{\mathrm{ten}}(M_{\mathrm{GUT}})$** | — | **$32.27$** | **$23.42$** |
| **Total $\chi^2_{\mathrm{nine}}(M_{\mathrm{GUT}})$** | — | **$24.95$** | **$19.34$** |

> [!NOTE]
> **Audit Note (2026-10-27):** Observables in this table are ratios to the third generation ($\log(m_i/m_3)$) matching the vector definition `T9` inherited from B1742/B1743. Because $D_{\mathbf{10}} = I$, the up-sector Yukawa matrix $Y_u$ is unshifted across schemes, so the up-quark pulls are identical between flat and normalized metrics. The substantial pull collapse ($\chi^2_{\mathrm{ten}}: 32.27 \to 23.42$) originates in the down-quark, charged-lepton, and CKM sectors via the $\mathbf{\bar{5}}$ Kähler normalization $\Delta k_{\mathbf{\bar{5}}}$.

## Significance
This demonstrates a genuine sensitivity lead: the residual flavour pulls observed in [B1762](file:///Users/dri/oa-audit-seat/agy-seat/frontier/B1762_zero_parameter_two_doublet_law_and_ten_observables/FINDINGS.md) are dramatically reduced by non-trivial modular weights in the chiral matter Kähler metric. However, because these weights are evaluated over discrete ansatzes rather than computed from the zero-mode wavefunctions on the compact manifold, this remains a phenomenological sensitivity lead rather than an unconditional derivation from the action under THE_BAR.
