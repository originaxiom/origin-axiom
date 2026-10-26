# B1759 — THE SECTOR-UNIVERSAL PUNCTURE NORM THEOREM AND STEP 2 OF THE BOUNDARY-DRESSED HIGGS PROBE (P-357 / P-366 / P-377)

**Verdict: PROVED (Theorem 1: exact sector-universal puncture norm identity $c_s^{(\mathrm{up})} = c_s^{(\mathrm{down})} = c_s^{(\mathrm{lep})}$; Theorem 2: structural obstruction to pure $c_s$-dressing and 2-torsion up-sector residue identity at the strip; diagnostic probe, not a new look).**

## 1. Theorem 1 — The Sector-Universal Puncture Norm Theorem (`P-357` Step 2)

For any Standard Model Yukawa bilinear $(q_L, q_R)$ with twists $(x, y) = (q_L w, q_R w)$ on $E_\tau$, let $P_s(u; x, y)$ ($s \in \{1, i, j, k\}$) denote the four parity-resolved zero-mode bilinear channels of `B1650`/`B1656` and $R_s(x, y) = \lim_{u \to 0} \theta_1(u|\tau) P_s(u; x, y) / \theta_1'(0|\tau)$ their puncture residues.

**Theorem 1 (Sector-Universal Normalized Kernel and Puncture Regularization Constant).**
1. *Exact Factorization:* On $E_\tau \setminus \{0\}$, each channel $P_s(u; x, y)$ with $R_s(x, y) \neq 0$ factors identically as
   $$P_s(u; x, y) = R_s(x, y)\,K_s(u; x + y), \qquad K_s(u; x + y) := \frac{P_s(u; x, y)}{R_s(x, y)},$$
   where the normalized elliptic kernel $K_s(u; x + y)$ depends **exclusively** on the sum twist $x + y = (q_L + q_R)w$ and is completely independent of the difference twist $x - y = (q_L - q_R)w$.
   *Proof:* By Riemann's level-2 theta addition theorem, $f_L(u) f_R(u) \theta_1(u|\tau)$ and $f_L(u) f_R(u+\tau) \theta_1(u|\tau)$ lie in the 2-dimensional space $\Theta_2(2\tau; x+y)$ of degree-2 level-$2\tau$ theta functions with sum characteristic $x+y$. Under the half-period translation $u \mapsto u + \tau$ (one generator of the level-2 Heisenberg group on $\Theta_2(2\tau; x+y)$), the two summands in $P_s(u; x, y)$ are swapped up to the fixed multiplier $\epsilon_s e^{-2\pi i(\tau + 2u + x + y)}$, decomposing $\Theta_2(2\tau; x+y)$ into 1-dimensional eigenspaces for $(1, i)$ and $(j, k)$. Because each eigenspace is 1-dimensional and depends only on $x + y$, dividing $P_s(u; x, y)$ by its residue $R_s(x, y)$ at $u = 0$ cancels the entire $(x - y)$-dependent proportionality constant. $\square$

2. *Universal Finite Puncture Norm Constant Across All SM Sectors:* Every Standard Model Yukawa bilinear $Q u^c H_u$, $Q d^c H_d$, $L e^c H_d$ has $|q_L + q_R| = |6 Y_H| = 3$ ($q_Q + q_u = -3$ and $q_Q + q_d = q_L + q_e = +3$). Because $|K_s(-u; -3w)| = |K_s(u; 3w)|$ and $u \mapsto -u$ preserves the symmetric punctured torus $E_\tau \setminus D_\varepsilon(0)$, the finite constant $c_s(\tau, w)$ in the Laurent expansion of the punctured kinetic norm
   $$G_{ss}^{(q_L, q_R)}(\varepsilon; \tau, w) = \int_{E_\tau \setminus D_\varepsilon(0)} |P_s(u; q_L w, q_R w)|^2\,\frac{d^2 u}{\mathrm{Im}\,\tau} = |R_s(q_L w, q_R w)|^2 \left(2\pi \ln\frac{1}{\varepsilon} + c_s(\tau, w) + O(\varepsilon^2 \ln \varepsilon)\right)$$
   satisfies the exact sector-universality identity:
   $$c_s^{(\mathrm{up})}(\tau, w) = c_s^{(\mathrm{down})}(\tau, w) = c_s^{(\mathrm{lep})}(\tau, w) \qquad \forall\,(\tau, w) \in \mathcal{M}_{1,2},\; \forall\,s \in \{1, i, j, k\} \text{ with } R_s \neq 0.$$

Numerical verification across the four strip points of `B1757` on $w = \frac{2}{5}\tau + \frac{1}{10}$ (`verification/sector_universal_puncture_norm.json`) confirms:
- $\max_{u} |K_s^{(\mathrm{down})}(u) - K_s^{(\mathrm{lep})}(u)| \le 2.12 \times 10^{-14}$ and $\max_{u} \bigl||K_s^{(\mathrm{up})}(u)| - |K_s^{(\mathrm{down})}(-u)|\bigr| \le 7.28 \times 10^{-14}$;
- $\max |c_j^{(\mathrm{up})} - c_j^{(\mathrm{down})}| \le 4.26 \times 10^{-13}$, $\max |c_k^{(\mathrm{up})} - c_k^{(\mathrm{down})}| \le 3.98 \times 10^{-13}$, and $|c_i^{(\mathrm{down})} - c_i^{(\mathrm{lep})}| \le 5.68 \times 10^{-14}$.

## 2. Theorem 2 — Off-Cone Scale vs. Sector Splitting at the Strip (`P-357` / `P-366` / `P-377`)

Comparing the data-free boundary-norm and sector-twist constructions against the committed free-doublet vectors of `B1757` (`frontier/B1757_step_twos_free_doublets_at_the_strip/verification/free_doublets.json`) establishes three structural facts:

1. **Both `B1757` doublets share the same $(e_2, e_3)$ chirality $(1, +i)/\sqrt{2}$ when phase-aligned on $h_2 > 0$:**
   At all four strip points on $L_{\max}$, once overall phases are fixed by $h_2 \in \mathbb{R}_{>0}$ (rather than largest-component normalization, which flips $H_u$ by $-i$ whenever $|h_{u,3}| > |h_{u,2}|$), both $H_u$ and $H_d$ have overlap $0.992\text{–}0.998$ with the **same** null ray $n = (0, 1, +i)/\sqrt{2}$, with off-cone invariants $I_u = |H_u \cdot H_u|/\|H_u\|^2 \in [0.0096, 0.0140]$ and $I_d \in [0.0179, 0.0299]$, and small $e_1$ ($i$-channel) admixtures $|H_{u,1}| \in [0.084, 0.122]$ and $|H_{d,1}| \in [0.056, 0.098]$.

2. **Boundary-norm dressing $(2\pi L + c_s)^\alpha$ reproduces the $\tau$-flat off-cone $(e_2, e_3)$ scale $O(10^{-2})$ without free parameters, but is sector-blind and preserves $e_1 = 0$:**
   On the strip ($\mathrm{Im}\,\tau \in [2.95, 3.10]$, $L_{\max} \in [3.39, 3.63]$), the doublet puncture constants split by $c_j - c_k \in [+0.0334, +0.0443]$ ($c_j \in [-0.3216, -0.3163]$, $c_k \in [-0.3606, -0.3550]$, while $c_i \in [+4.887, +4.972]$). Dressing the Dedekind-period vector $v_{\mathrm{DR}}(\tau) = (0, 1, \rho(\tau))$ by $(2\pi L_{\max} + c_s)^\alpha$ lifts $(e_2, e_3)$ off the null cone with
   - $I(\alpha = +1/2) \in [0.0100, 0.0151]$ (matching $I_u \in [0.0096, 0.0140]$),
   - $I(\alpha = +1) \in [0.0194, 0.0292]$ (matching $I_d \in [0.0179, 0.0299]$),
   - $I(\alpha = -1) \in [0.0078, 0.0102]$ (with $|e_2| - |e_3| < 0$, matching the sign of $|H_{u,2}| - |H_{u,3}|$ at three of the four $L_{\max}$ points).
   However, by Theorem 1, $c_s(\tau, w)$ is sector-universal, and $v_{\mathrm{DR}}(\tau)$ has $e_1 = 0$. Therefore, diagonal boundary-norm dressing alone gives $H_u = H_d$ with $e_1 = 0$ ($\chi^2_{\mathrm{nine}} \ge 1420$).

3. **Exact 2-torsion up-sector vanishing $R_i^{(\mathrm{up})} = 0$ vs. down-sector $i$-channel overshoot in the raw matter vectors:**
   All sector differentiation in $G_{ss}^{(q_L, q_R)} = |R_s(q_L w, q_R w)|^2 (2\pi L + c_s)$ enters through the residue factor $R_s(q_L w, q_R w)$, which depends on the difference charge $q_L - q_R$:
   - In the **up sector**, $q_Q - q_u = 1 - (-4) = 5$. On any primitive order-10 line $w = \frac{2}{5}\tau + \frac{1}{10}$, the difference twist is $5w = 2\tau + \frac{1}{2}$ (a 2-torsion point modulo $\mathbb{Z}\tau + \mathbb{Z}$), forcing $R_i^{(\mathrm{up})}(\tau, w) = 0$ **identically** ($|R_i^{(\mathrm{up})}| \le 5.31 \times 10^{-16}$) and placing the raw matter vector $u_{\mathrm{up}}$ at $I(u_{\mathrm{up}}) \in [0.0065, 0.0087]$!
   - In the **down and lepton sectors**, $|q_L - q_R| = 1$ is not 5-divisible, so $R_i^{(\mathrm{down})} \neq 0$ turns on the $e_1$ ($i$-channel) component, but at raw unit weight $|u_{\mathrm{down}, i}| \in [0.938, 0.943]$ ($I(u_{\mathrm{down}}) \in [0.902, 0.909]$), overshooting the small $e_1$ admixture $|H_{d,1}| \in [0.056, 0.098]$ required by `B1757` ($\chi^2_{\mathrm{six}}(u_{\mathrm{up}}, u_{\mathrm{down}}) \in [3093, 3291]$).

## Files

- `verification/sector_universal_puncture_norm.py` → `verification/sector_universal_puncture_norm.json`, `verification/sector_universal_puncture_norm_run.txt`
- `tests/test_b1759_sector_universal_puncture_norm_and_higgs_dressing.py`

## Seen first

`VERDICT topic-sweep /puncture norm|c_s|L_max|two doublets|H_u|H_d|B1757/ (full text): 44 of 1529 arcs on main match (NEGATIVE 6, OPEN 4, PROVED 33, no verdict file 1)`
— among them B1654, B1656, B1667, B1743, B1757. **The register:** P-357, P-366, P-377. **Literature:** arXiv:2209.07249, arXiv:2302.11183 (P-382).
