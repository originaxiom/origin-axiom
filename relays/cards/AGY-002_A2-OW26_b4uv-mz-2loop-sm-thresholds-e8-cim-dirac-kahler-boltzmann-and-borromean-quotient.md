# Card `A2-OW26` — Pre-Registration (`0 of 19`, Expectations Committed First)

- **Seat:** `agy-002` (`agy-002/verify`)
- **Date:** `2026-11-23`
- **Firewall:** **Strictly `0 of 19`** (zero PDG, NuFIT, Planck, DESI, or CODATA numbers anywhere — including Guardrail-4 benchmarks, which use strictly pure-math / rational synthetic test points).
- **Hygiene & Custody Contract:**
  - `0` Python `float` or `complex` AST literals (`mpmath` + `fractions.Fraction` + `sympy` only).
  - `0` `float()` / `complex()` binary64 casts.
  - `0` JSON floating-point tokens (all non-integer numbers serialized as decimal strings).
  - `0` imports from `frontier/`, peer scripts, or prior `agy-002` scripts.
  - `0` edits outside `relays/`; `0` in-place overwrites of any prior sealed script, JSON, or `SHA-256` manifest.
  - `SCRIPT_SHA256.txt` committed prior to execution; raw unread output + `OUTPUT_SHA256.txt` committed immediately after execution; independent zero-shared-code Cold-Room Zero-Trust Referee executed afterward.

---

## Pre-Registered Modules & Quantitative Pass/Fail Expectations

### 1. `OW26-A` — Full `2`-Loop SM RGEs (`M_{SUSY} \to M_Z`), Exact `\overline{DR} \to \overline{MS}` + Derived Sparticle/`\Delta_b` Thresholds, & `M_Z` Pole Ratios
- **Guardrail-4 Pure-Math Benchmark Gate (`0 of 19`):**
  1. Derive `1`-loop and `2`-loop SM gauge coefficients $b_1^{\mathrm{SM}} = (41/10, -19/6, -7)$, $b_{2,ab}^{\mathrm{SM}}$, and $c_{a,f}^{\mathrm{SM}}$ directly from SM Weyl-fermion & Higgs Casimirs (`exact Fraction equality`).
  2. Independently verify the exact `2`-loop SM scalar-loop vacuum-polarization shifts (`2HDM -> SM`: $\Delta_{g_a^4} = \frac{11}{6} S_a(H)(C_a(L)+C_a(R)) - \frac{1}{2} S_a(H) C_a(H)$), exact `4`-real-scalar `SU(2)` contraction giving $+\frac{3}{2}\mathrm{Tr}(H_u H_d)$ in $\gamma_S^{(2)}$, and exact `O(4)` pure-scalar quartic beta coefficients $(\beta_\lambda^{(1)} = 12\lambda^2,\; \beta_\lambda^{(2)} = -78\lambda^3)$ in $V = \frac{\lambda}{2}|H|^4$ (`0.0` exact).
  3. Reproduce exact `1`-loop analytic SM gauge & Pendleton–Ross solutions at synthetic rational initial point (`< 1e-13`) and `2`-loop full-matrix SM RK4 step-halving (`N = 160` vs `320`, `< 1e-10`).
- **Exact Threshold Matching at $Q = M_{\mathrm{SUSY}}$:**
  - Scheme conversion $\alpha_a^{-1,\overline{\mathrm{MS}}} = \alpha_a^{-1,\overline{\mathrm{DR}}} + C_2(G_a)/(12\pi)$ (`C_2 = (0, 2, 3)`).
  - Derived sparticle mass-splitting gauge thresholds $\Delta\alpha_a^{-1} = -\frac{1}{2\pi}\sum_i \Delta b_a^{(i)} \ln(m_i / Q_{\mathrm{match}})$ directly from the `OW25-A` soft-SUSY RGE spectrum (`M_1, M_2, M_3, |\mu|, m_{\tilde q}, m_{\tilde t}, m_{\tilde b}, m_{\tilde l}, m_A`).
  - `1`-loop `\overline{DR} \to \overline{MS}` Yukawa matching + Hall–Rattazzi–Sarid `\Delta_b` threshold evaluated honestly for **both** $\mathrm{sgn}(\mu) = +1$ and $\mathrm{sgn}(\mu) = -1$ (`1`-bit signed choice).
  - Full `2`-loop SM running (`g_1, g_2, g_3, Y_u, Y_d, Y_e, \kappa_{\mathrm{SM}}, \lambda_{\mathrm{SM}}`) down to $Q = M_Z$, plus `1`-loop SM QCD+EW pole-to-`\overline{MS}` ratios ($m_t^{\mathrm{pole}}/v_{\mathrm{EW}}$, $m_h^{\mathrm{pole}}/M_Z$, $m_h^{\mathrm{pole}}/v_{\mathrm{EW}}$, $m_W/m_Z$, $m_b(M_Z)/m_\tau(M_Z)$).
- **Guardrail-3 End-to-End Haar Scrambling Gate:** `10`-trial random Haar $U(3)^5$ basis scrambling applied at $M_{\mathrm{GUT}}$ and propagated through the ENTIRE `M_{GUT} \to M_{SUSY}` (`2`-loop MSSM) $\to$ threshold matching $\to$ `M_Z` (`2`-loop SM) pipeline must leave all `M_Z` dimensionless observables invariant to **`< 1e-12`**.

### 2. `OW26-B` — First-Principles UV Normalizations & Chiral Spin-`1/2` Dirac Liouville Kähler Audit
- **`B1` (`E_8` `240`-Root Clebsch):** Construct all `240` roots of $E_8$, decompose under $SU(5)_{\mathrm{vis}} \times SU(5)_{\mathrm{hid}}$, verify $V_F + V_D = V_{\mathrm{YM}}$ on canonically normalized root triplets $\alpha + \beta + \gamma = 0$, and prove the exact tree-level superpotential normalization $|y_{\alpha\beta\gamma}| / g_{E_8} = 1$ for both `10·10·5_H` and `10·5̄·5̄_H`.
- **`B2` (`M = 8` Magnetized `T^2/\mathbb{Z}_2` CIM `L^2` Triple Overlap at $\tau_0 = (2+i)/5$):** Compute the exact `L^2`-normalized wavefunction triple overlap for both unmagnetized constant Higgs ($M_H = 0 \implies y_t/g_{\mathrm{UV}} = 1$) and magnetized Higgs $(M_Q, M_{u^c}, M_{H_u}) = (8, 8, 16)$ ($\mathbb{Z}_2$-odd $\times$ $\mathbb{Z}_2$-odd $\times$ $\mathbb{Z}_2$-even), cross-checking the closed-form Cremades–Ibanez–Marchesano (`hep-th/0404229`) theta sum against direct `2D` numerical integration on $T^2$ (`< 1e-10`), and propagate the derived $y_t^{\mathrm{CIM}}(M_{\mathrm{GUT}})/g_{\mathrm{UV}}$ to $M_Z$.
- **`B3` (Self-Consistent Supergravity $m_{3/2} = \frac{1}{\sqrt{3}}\Lambda_{\mathrm{hid}}^3 / M_{\mathrm{Pl}}^2$):** Derive $M_{\mathrm{GUT}}/M_{\mathrm{Pl}}$ directly from `OW23-C`'s `7D` Borromean volume (`M_{KK}/M_{Pl} = 0.03940`) and $\sqrt{\alpha_{\mathrm{UV}}/(4\pi)}$, compute the exact `2\ln(M_{GUT}/M_{Pl})` shift to $t_{\mathrm{GUT} \to m_{3/2}}$ across $\alpha_{\mathrm{UV}}^{-1} \in \{23, 24, 25\}$, and compare transparently against `OW25`'s $t_{\mathrm{SUSY}} = \frac{2}{5}\pi\alpha_{\mathrm{UV}}^{-1}$.
- **`B4` (Spin-`1/2` Dirac Liouville Kähler $e^{+\varphi}$ Audit — Addressing `agy-exp` `abf9fdae0` Catch):**
  - Verify algebraically and numerically that covariant `6D` chiral spin-`1/2` Dirac zero modes $\Psi_+^{\mathrm{orth}} = e^{-\varphi/2}\psi^{\mathrm{hol}}$ carry kinetic Weyl weight `+1` ($\mathcal{G}_{ab}^{(s=1/2)} = \int d^2z\,e^{+\varphi}\overline{\psi_a}\psi_b$) and Yukawa Weyl weight `0`.
  - Compute $\mathcal{G}_{E[2]}^{(s=1/2)}(\tau_8^+)$ via Fuchsian developing-map polar-cusp quadrature (coarse vs fine grid diff `< 1e-5`, cross-checking `agy-exp`'s `(1.07020, 0.86840, 1.06140)`), and propagate **`CURV_{s=1/2}`** alongside `FLAT` and legacy `CURV_{s=0}` (`e^{+2\varphi}`) through the complete `M_{GUT} \to M_Z` pipeline and gluino FCNC dilution.

### 3. `OW26-C` — Sequential Seesaw, `\delta_{CP}^{\mathrm{PMNS}}` & `|m_{ee}|/m_3`, Stiff MSSM Boltzmann Leptogenesis Washout `Y_B`, LSP Identity, & `d = 6` Proton Decay
- **Sequential `N_3 \to N_2 \to N_1` Threshold Running (`Antusch et al. hep-ph/0501272`):** Integrate `(Y_\nu, M_R, \kappa)` sequentially through $M_{R_3} \to M_{R_2} \to M_{R_1} \to M_{\mathrm{SUSY}} \to M_Z$ (`10`-trial Haar $U(3)^5 \times U(3)_N$ invariance `< 1e-12`), extracting at `M_Z`: `s_{12}^2, s_{23}^2, s_{13}^2, \Delta m_{21}^2/\Delta m_{31}^2, J_{\mathrm{PMNS}}`, exact Dirac phase `\delta_{CP}^{\mathrm{PMNS}} \in [-\pi, \pi]`, `|m_{ee}|/m_3`, and `\sum m_\nu / m_3`.
- **Full Flavored + Unflavored Stiff MSSM Boltzmann Washout (`z \in [1/10, 100]`):** Compute exact MSSM decay asymmetries `\varepsilon_{1,\alpha}` (`\alpha \in \{e, \mu, \tau\}` + total `\varepsilon_1`), dimensionless washout ratios `K_{1,\alpha}` directly from `(g_*^{\mathrm{MSSM}} = 915/4,\; M_{\mathrm{Pl}}/M_{\mathrm{GUT}},\; M_{\mathrm{GUT}}/M_1)`, integrate the stiff coupled Boltzmann ODEs via implicit Crank–Nicolson / exponential step (step-halving `< 1e-7`, thermal & zero initial abundance), and verify exact geometric CP-odd law `Y_B(\tau_8^+) + Y_B(\tau_8^-) = 0` (`< 1e-30`) so **`Y_B > 0` dynamically selects the unique CP branch** (eliminating `1.0` discrete bit and fixing absolute signs of `J_{\mathrm{CKM}}` and `\delta_{CP}^{\mathrm{PMNS}}`).
- **LSP Identity & `d = 6` Proton Decay:** Determine the lightest `P_M = -1` sparticle directly from the full soft-SUSY RGE spectrum across all `36` EWSB benchmarks and compute the dimensionless `d = 6` gauge-boson proton-decay ratio `(M_{\mathrm{GUT}}/v_{\mathrm{EW}})^4 / \alpha_{\mathrm{UV}}^2`.

### 4. `OW26-D` — Symbolic Borromean `2i \to i \to (2+i)/5 \to 8\tau_0` Quotient Map & Cross-Seat Seam Checks
- **Borromean Quotient Chain (SymPy exact):** Prove that `Z_2` cusp-lattice halving $Q_2 = \mathrm{diag}(1, 2)$ ($\det = 2$) $\circ$ $\gamma = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix} \in \mathrm{SL}(2, \mathbb{Z})$ $\circ$ $C_8 = \mathrm{diag}(8, 1)$ ($\det = 8$) has composite matrix $\begin{pmatrix} 8 & 0 \\ 2 & 2 \end{pmatrix}$ ($\det = 16$) mapping Borromean cusp $\tau_{\mathrm{cusp}} = 2i \mapsto i \mapsto \tau_0 = \frac{2+i}{5} \mapsto 8\tau_0 = \frac{16+8i}{5}$ with $j(\tau_0) = j(i) = 1728$ exact.
- **Cross-Seat Verifications:**
  1. `chat1` `W-H1` Exact Mirror Theorem $\tilde{S}(\tau) = -Q_K S(-\bar\tau) Q_K^{-1}$ verified directly on our `eval_w_hol_tau` quaternion Higgs factor `sh(\tau)` to `< 1e-40` + exact CP conjugation of all `Y_f, M_R` observables (`< 1e-35`).
  2. `physical` `32514763f` infinite-cusp static gauge quartic $O(\epsilon^5)$ relaxation scaling verified independently vs. `B4_UV`'s uniform cusp-length-independent `4D` $\mathcal{N}=1$ SUSY D-term lower bound $\lambda_{\text{tree}} > 0$ for $\tan\beta \neq 1$.
  3. `agy-exp` `abf9fdae0` $8^3_4$ lopsided profile $n_{10} = (2, 0, 3)$ + $M_R \propto I_3 + \widehat{W}_R^{\mathrm{unit}}$ evaluated side-by-side in `B4_UV`'s `M_Z` pipeline under honest Guardrail-1 bit provenance.

### 5. `OW26-E` — `6 / 6` Planted Faults & Final `B4_UV_MZ_BLIND_LOCK_V2`
- `PF_OW26_1`: Corrupt `2`-loop SM `O(4)` coefficient `-78 -> -70` caught by exact `O(4)` identity.
- `PF_OW26_2`: Omit `\overline{DR} \to \overline{MS}` `C_2(G_a)/(12\pi)` shift caught by scheme-conversion gate.
- `PF_OW26_3`: Using scalar `e^{+2\varphi}` instead of Dirac `e^{+\varphi}` breaks `6D` chiral spin-connection Weyl-weight identity.
- `PF_OW26_4`: Flipping `\tau_8^+ \to \tau_8^-` flips `Y_B` sign cleanly (`Y_B^+ + Y_B^- = 0`).
- `PF_OW26_5`: Perturbing `M_{\mathrm{frame}}` out of `SL(2, \mathbb{Z})` breaks `\det = 1` and `j(\tau_0) = 1728`.
- `PF_OW26_6`: Guardrail-1 audit rejects zero-bit assignment on `1/384` atlas or post-inspection `8^3_4` selection.
- Seal **`B4_UV_MZ_BLIND_LOCK_V2`** (`blind_prediction_lock_v2_sha256`), update single-run **`A2-OW16 v15`**, and run isolated zero-shared-code Cold-Room Referee (`referee_a2_ow26.py`).

---

## Pre-`v2` Technical Erratum (`2026-11-23`; Frozen `v1` at `0322af735` Untouched)

`A2-OW26 v1` (`0322af735`) passed `OW26-A` (`guardrail4_pass = true`, `10`-trial end-to-end Haar `2.33e-30`) on the first run and caught `4` clean implementation typos in `B/C/D`, fixed in `relays/a2_ow26_v2/verify_a2_ow26_v2.py` while leaving `v1` frozen untouched:
1. **`OW26-B4` (`wp_and_p_mp` typo):** Fixed Weierstrass $\wp, \wp'$ factors (`(pi t30 t40 t2 / t1)^2` and `-2 pi^3 (t20 t30 t40)^2 t2 t3 t4 / t1^3`) and used 3-trace Gauss–Newton least squares (`Im tr(Ta), Im tr(Tb), Im tr(Ta Tb) = 0`) from `c = 0` so `c_*`, `tr_comm_err`, Gauss–Bonnet Area $= 2\pi$, and `s = 0` match `OW19_A` to `< 1e-6`, yielding the true spin-`1/2` Dirac Liouville Gramian `G^{(s=1/2)}_{E[2]}`.
2. **`OW26-B1` (`V_D` normalization & ordered triplet count):** Used exact `V_D = g^2 Tr_fund(D^2)` (`2 Tr(T^a T^b) = \delta^{ab}`), cancelling `x_1^4, x_2^4` identically to prove `y_root^2 / g^2 == 1`, and checked `600` ordered (`300` unordered) root-sum triplets for both `10·10·5_H` and `10·5̄·5̄_H`; bumped `B2` periodic quadrature `18 -> 24` and added `k_H = 1` (`0.6350`) propagation.
3. **`OW26-C` (True geometric CP mirror `(\tau, a, b) -> (-\bar\tau, a, -b)` & Boltzmann step count):** Reflected BOTH $\tau \mapsto -\bar\tau$ AND the $(K_5, K_6)$ orbit $(a, b) \mapsto (a, -b)$ (recording fixed-orbit `\tau_8^-` separately to show why fixed `K_5` breaks pure $\tau \mapsto -\bar\tau$), and bumped `n_z_steps` `320 -> 500` so step-halving `< 1e-6`.
4. **`OW26-D` (`PSL(2)` sign, `j(\tau_0)` truncation, & quadratic-source cusp trial):** Divided `la_b[0,1]` by `la_b[0,0] = -1` (exact `\tau_cusp = +2i`), raised `j(\tau_0)` $q$-series order `55 -> 110` (`< 1e-40`), and used exact quadratic-source cusp trial `b(y) = eps^2 y (1 - y/L)^2` (`b'(0) = eps^2` from `[a \wedge a]`, giving exact `4 eps^5` at `L = 1/eps`).

## Pre-`v3` Numerical Precision Tightening Note (`2026-11-23`; Frozen `v1` `0322af735` & `v2` `1bb5725e4` Untouched)

`A2-OW26 v2` (`1bb5725e4`) passed `OW26-A`, `OW26-D`, and `6/6` planted faults `OW26-E`, reproduced `agy-exp`'s spin-`1/2` Dirac Gramian `(1.07020, 0.86840, 1.06140)` to `6` digits, and verified `Y_B(\tau_8^+) + Y_B(\text{CP mirror}) = 0` to `2.06e-40`. Only two numerical step-size tolerances in `B4` (`tr_comm_err = 6.14e-10`, `z2_evenness_err = 1.88e-8` at `8/12`-step `order=16`) and `C` (`Y_B` step-halving `8.73e-6` at `n_z_steps = 500`) exceeded the strict thresholds. `relays/a2_ow26_v3/verify_a2_ow26_v3.py` tightens `B4` to `30`-dps `12/18`-step `order=20` for `c_*` & `z2_evenness` (`< 1e-18`), tightens `C` to `n_z_steps = 1600` (`< 1e-6`), and records whether `CURV_s12_Dirac` stays inside `OW24-C`'s simultaneous PMNS window honestly (zero target change).

## Pre-`v4` L-Stable Radau IIA Boltzmann & `z2` Path-Step Upgrade (`2026-11-23`; Frozen `v1..v3` Untouched)

`A2-OW26 v3` (`962a310e9`) passed `fuchsian_tr_comm_err = 8.34e-17` and revealed that piecewise-constant source distribution in the exponential Boltzmann step degrades to `O(du)` inside the stiff `zero_init` boundary layer (`7.78e-6` at `N=1600`), while `prop_seg_mp` `max_st = 1/4 * dist` caps `z2_evenness_err` at `(1/4)^20 ~ 3e-12`. `relays/a2_ow26_v4/verify_a2_ow26_v4.py` replaces the Boltzmann step with `2`-stage L-stable Radau IIA (`O(h^3)`, `N = 600` vs `1200`, `< 1e-6`) and uses `max_st = 1/6 * dist, order = 24` on the `2`-point `z2_evenness` check (`< 1e-18`), preserving frozen `v1..v3` untouched.

`0 of 19.`
