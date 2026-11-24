# Scope Card `A2-P135` (`2026-11-24`): Escalated Debt `P-135` (`M57`) — Independent Derivation of Simpson's Tame Table (`B1650` `O3`), Disjoint $E_8$ Condensate Embedding Count (Zero Shared Code with `W70`), & Cross-Check of `agy-exp` `9b34bfc03` (`A2-OW27-F2` / `A2-OW26-F1`) (`0 of 19`)

- **Seat / Branch:** `agy-002` (`origin/agy-002/verify`), answering `main` `M57` (`5988bd5de`, `docs/seats/agy-002.md`)
- **Firewall:** Strictly **`0 of 19`** (zero empirical SM / PDG / NuFIT / Planck / DESI / CODATA numbers; zero Python `float`/`complex` AST literals; zero binary64 casts; zero JSON float tokens; zero edits outside `relays/`).
- **Zero-Shared-Code Pledge (`M57` & `B1888` Condition 1):** Neither `W70`'s script (`origin/claude/standard-model-derivation-0qt6ao`) nor `chat1`'s scripts (`origin/chat1/web-seat`) were opened or inspected. All derivations start strictly from primary mathematics (Simpson, *J. Amer. Math. Soc.* 3 (1990), 713–770, p. 720 & Theorem 5; exact $\mathbb{R}^8$ $E_8$ root system & regular $A_5 \oplus A_2 \oplus A_1$ Lie-algebraic structure) and the prose statements in `B1650`, `W70_RULE.md`, and `weave_field_map_2026_10_14/PROOF.md`.

## 1. Pre-Registered Expectations & Disagreement Criteria (`expectations committed first`)

### Block `P135-A` — Simpson's 1990 Tame Table (p. 720) & Full Non-Diagonal Nilpotent Jordan Model (`B1650` `O3`)
1. **3-Column Local Correspondence (Exact SymPy Derivation):** On a punctured disc $\Delta^*$ with holomorphic frame $e$ of $E_\alpha$, harmonic metric $h(e, e) = |z|^{2\alpha}$, and tame Higgs field $\theta = (b + ic)\frac{dz}{z}$:
   - The $D''$-holomorphic frame $v = |z|^{-2(b-ic)} e$ satisfies $D'' v = 0$, has norm $|v|_h = |z|^{\alpha - 2b}$ (**de Rham weight $\alpha - 2b$**), and $D' v = (\alpha + 2ic)\frac{dz}{z} v$ (**de Rham residue eigenvalue $\alpha + 2ic$**).
   - The flat section $s = r^{-(\alpha+2b)} e^{(-i\alpha+2c)\vartheta} e$ satisfies $D s = 0$, has norm $|s|_h = |z|^{-2b}$ (**Betti weight $-2b$**), and counterclockwise monodromy eigenvalue **$\exp(-2\pi i\alpha + 4\pi c)$**.
   - At the common point $\alpha = (1/2, 1/2)$ with $\operatorname{Res}\Phi_a = \sigma_a$ ($\sigma_a^2 = -(a\cdot a)I_2$, eigenvalues $\pm(b+ic)$):
     - Unfiltered flat side ($b = 0$) forces $a\cdot a = +c^2$ and $\kappa = \operatorname{tr} M = -2\cosh(4\pi c)$, so $\kappa = -2 \iff c = 0 \iff a\cdot a = 0$ (nilpotent residue).
     - Filtered flat side ($b \neq 0, c = 0$) gives $\kappa = -2$ with $a\cdot a = -b^2 \neq 0$ and Betti weights $\mp 2b \neq 0$ (confirming `O3` requires the unfiltered flat side).
2. **Exact Non-Diagonal Rank-2 Nilpotent Jordan Model (Closing `C7`'s Gap):** With $u = -\ln|z|$, $h = |z|^{2\alpha}\mathrm{diag}(u^{-1}, u)$, $\alpha = 1/2$, and $\Phi = \frac{1}{2}\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}\frac{dz}{z}$:
   - Exact Hitchin equation $F_h + [\Phi, \Phi^{*_h}] = 0$ and flatness $D^2 = 0$ hold identically in SymPy.
   - Exact closed-form flat sections $s_1 = z^{-1/2}(1, -1/u)^T$ and $s_2 = z^{-1/2}(\ln z, -2 - (\ln z)/u)^T$ satisfy $D s_1 = D s_2 = 0$, yield genuine non-semisimple Jordan monodromy $M = -\begin{pmatrix} 1 & 2\pi i \\ 0 & 1 \end{pmatrix}$ ($\operatorname{tr} M = -2, M \neq -I_2$), and satisfy exact Simpson logarithmic weight norms $|s_1|_h \sim (-\ln|z|)^{-1/2}$ ($\mathrm{Gr}^W_{-1}$) and $|s_2|_h \sim (-\ln|z|)^{+1/2}$ ($\mathrm{Gr}^W_{+1}$) with Betti power weight $0$.
3. **Global Half & Parabolic Stability:**
   - Symbolic $SL(2,\mathbb{C})$ proof that $XY = -YX \implies \operatorname{tr} X = \operatorname{tr} Y = \operatorname{tr}(XY) = 0 \implies X^2 = Y^2 = (XY)^2 = -I_2$ (unique $Q_8$ unitary point, $\Phi = 0$).
   - Parabolic stability check for Atiyah's degree-$-1$ bundle $E$ with equal weights $(1/2, 1/2)$: every line subbundle $L \subset E$ has $\deg L \le -1 \implies \operatorname{pardeg} L \le -1/2 < 0 = \frac{1}{2}\operatorname{pardeg} E$ (including $K = \ker\Phi_R$ with $\deg K = -1, \Phi_R: E/K \xrightarrow{\sim} K(p)$), discharging Simpson Theorem 5's polystability prerequisite.
   - *Disagreement criterion:* Any non-zero symbolic residual in $D'' v$, $D s$, $F_h + [\Phi,\Phi^{*_h}]$, $D^2$, or $M \neq -\bigl(\begin{smallmatrix}1&2\pi i\\0&1\end{smallmatrix}\bigr)$.

### Block `P135-B` — Disjoint $E_8 \supset A_5 \oplus A_2 \oplus A_1$ Condensate Embedding Count (Zero Shared Code with `W70`)
1. From exact $\mathbb{R}^8$ construction of the `240` $E_8$ roots and the prose-specified regular subalgebra ($A_2$: $e_0-e_1, e_1-e_2$; $A_1$: $e_3-e_4$; $A_5$: $e_6-e_7, e_5-e_6, e_6+e_7, -\frac{1}{2}(1^8), e_3+e_4$):
   - Exact $A_5 \oplus A_2 \oplus A_1$ Cartan matrix and complete `248`-dim branching `(35,1,1)+(1,8,1)+(1,1,3)+(20,1,2)+(15,3bar,1)+(15bar,3,1)+(6,3,2)+(6bar,3bar,2)`.
   - With $h_Q = \sum_{k=0}^5 (-1)^k w_k$ and $h_W = e_3 - e_4$: $r \cdot (h_Q - h_W) \in 2\mathbb{Z}$ for all `240` roots (`Ad(puncture) = Ad(weak center)` on `248`), yielding **exact count `112` puncture-odd roots** (`40+36+36`) and `128` puncture-even (`+8 = 136`).
   - Exact algebraic proof over **all $\mathbb{C}^3$** (and exhaustive verification over the `469`-point $k/6$ grid) that block-scalar $Y = y_1(w_0+w_1)+y_2(w_2+w_3)+y_3(w_4+w_5)$ ($y_1+y_2+y_3=0$) admits **exactly `6` admissible hypercharges** (permutations of `(1/6, -5/6, 2/3)`) with $k_Y = \operatorname{Tr}_{248}(Y^2)/\operatorname{Tr}_{248}(T_3^2) = 14/3$.
   - $\mathfrak{su}(2)_Q = \operatorname{span}(h_Q, E_{\beta_1}+E_{\beta_3}+E_{\beta_5}, E_{-\beta_1}+E_{-\beta_3}+E_{-\beta_5})$ is colour-singlet, weak-singlet, puncture-even (`0/112` overlap), and satisfies $Y = 0$ identically under all `6` admissible hypercharges (complete SM singlet).
   - Exactly `4/112` neutral colour-singlet Higgs-like doublet roots per $Y$ (`2` with $Y=+1/2$, `2` with $Y=-1/2$), union across all `6` $Y$ = **`24` distinct roots** (`==` all `24` block roots of $\mathrm{SU}(3)_{\text{block}}$); backreaction $(\alpha\cdot h_Q)/(h_Q\cdot h_Q) \in \{\pm 1/6\text{ (108)}, \pm 1/2\text{ (4)}\}$ (real, never isotropic); $\alpha = e_3 + e_5$ has $T_3 = +1/2$, weight $w_0+w_1+w_4$, neutral under unique `(1/6, 2/3, -5/6)` leaving $\mathrm{SU}(3)_c \times \mathrm{U}(1)_{\text{em}}$.
   - *Disagreement criterion:* Any mismatch in the `240`/`112`/`136`/`6`/`4`/`24` counts, $k_Y \neq 14/3$, or nonzero SM charge on $\mathfrak{su}(2)_Q$.

### Block `P135-C` — Independent Audit of `agy-exp` `9b34bfc03` (`A2-OW27-F2` & `A2-OW26-F1`)
1. Independently evaluate `agy-exp` `9b34bfc03`'s `A2-OW27-F2` PMNS construction at $\tau_8^+ = \frac{16+8i}{5}$ with curved Dirac $\mathcal{G}^{(s=1/2)}(\tau_8^+)$, `M_R = I_3 + W_R^unit`, true gauge-invariant $U_{\text{PMNS}} = U_e^\dagger U_T$ (10-trial random $U(3)_L$ Haar test `< 1e-40`), testing:
   - `agy-exp`'s exact branch (`K_6^+`, `n_10 = (3,0,2)` vs `(3,2,0)`, asymmetric `Y_nu = K^{-1/2} W_nu` without right `K^{-1/2}`);
   - Symmetric `Y_nu = K^{-1/2} W_nu K^{-1/2}` (as in `LINK8` `L8_5`);
   - Twin `K_6^- = <(1,5)>` (`FL8-F3`) with both `(3,0,2)` and `(3,2,0)`.
2. Quantify precisely whether `A2-OW27-F2`'s simultaneous `OW24-C` hit `(0.3441, 0.6192, 0.01265)` reproduces under true gauge-invariant Takagi AND how it depends on the extra `8^3_4` `D_10` cusp dressing, `K_6^+` vs `K_6^-`, and right-`K^{-1/2}` convention. Confirm `A2-OW26-F1` (`m_0/v_EW` is a 6th continuous ratio in `LOCK_V3`).

### Block `P135-D` — Planted Fault Controls (`6/6` Must Trigger)
- `PF-1`: Non-zero Betti weight $b = 1/4, c = 0$ keeps $\kappa = -2$ while breaking nilpotency ($a\cdot a = -1/16 \neq 0$).
- `PF-2`: Wrong nilpotent coupling $|c_0| = 1$ (instead of $1/2$) violates Hitchin's equation $F_h + [\Phi, \Phi^{*_h}] = 0$.
- `PF-3`: Flipping $h_Q$ sign on one doublet breaks `Ad(puncture) == Ad(weak center)` (non-even pairings in `240` roots).
- `PF-4`: Dropping the `e^c` hypercharge condition allows the spurious solution `(1/6, -1/3, 1/6)` (`> 6` solutions).
- `PF-5`: Replacing true $U_e^\dagger U_T$ with `U_e^H U_T^*` breaks $SU(2)_L$ Haar invariance by `> 0.1`.
- `PF-6`: Removing `D_10` (or using `(3,2,0)`) fails the simultaneous `OW24-C` window check.

0 of 19.
