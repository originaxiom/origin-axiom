# B1881 — `P-776` Whole-Subweave Twin-Odd Hyperbolic Laplacian Read-Out, `R10-A/B/C` Operators, and the Data-Free `FR-FIB` Hierarchy Test (`FINDINGS`)

**Date:** `2026-11-11`  
**Verdict:** `PROVED` (**conditional weave result on stated upstream choices**, two-commit sealed execution: Commit A `8aafb6945` sealed `PREREGISTRATION.md` and `subweave_p776_and_hierarchy.py` prior to seeing any level-5 Maass output; all cells `C0`–`C4` and `H1`–`H4` `PASS` as sealed, overturning our declared `80% FAIL` prior on `H4`; **strictly data-free, `0 of 19`**)  
**Point Register:** `P-776` (`DONE`), `P-761` (first computed state of the whole level-5 subweave under stated choices; closed loop without choices remains open)  
**Locks & Artefacts:**
- Sealed design & symmetry proofs (`Commit A`, untouched): `frontier/B1881_p776_twin_odd_operator_and_whole_subweave_readout/PREREGISTRATION.md` (`87925a996419561a6dd30706f5b5cc792de3324224f3c7b5727c4de92125e2d2`)
- Sealed computation script (`Commit A`, untouched): `frontier/B1881_p776_twin_odd_operator_and_whole_subweave_readout/verification/subweave_p776_and_hierarchy.py` (`abcb2fb3721580a5de859b9815e776edbabab3598e40cbe892506a1454dec6ad`)
- Sealed hash manifest (`Commit A`, untouched): `frontier/B1881_p776_twin_odd_operator_and_whole_subweave_readout/ARTIFACT_HASHES.txt`
- One-shot output certificate: `frontier/B1881_p776_twin_odd_operator_and_whole_subweave_readout/verification/subweave_p776_and_hierarchy.json`
- Independent zero-trust `@referee` lock (`5/5` tests): `tests/test_b1881_p776_whole_subweave_readout.py`

---

## Seen first

- **Repo topic-sweep:** Ran `python3 scripts/checks/topic_sweep.py --full "subweave|Ray-Singer|Maass|FR-FIB"` (`VERDICT topic-sweep /subweave|Ray-Singer|Maass|FR-FIB/ (full text): 64 of 1626 arcs on main match (NEGATIVE 16, OPEN 4, PROVED 44); 28 register rows match (DONE 15, QUEUED 13)`). Read in full: `frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.py`, `frontier/B1724_the_readings_covariance/FINDINGS.md`, `frontier/B1726_the_two_ingredients_replicated/verification/census.py`, `frontier/B1815_the_records_walk_has_minkowskis_exit_law_exactly/FINDINGS.md`, `frontier/B1822_t_norm_on_the_frames_matter/FINDINGS.md`, `frontier/B1838_the_end/verification/exact_end_web_seat.py`, `frontier/B1857_the_read_out_by_a_state_checked/FINDINGS.md`, `frontier/B1868_what_concentrates_under_the_move_count_verified/FINDINGS.md`, `frontier/B1872_all_histories_together_the_exact_facts_verified/FINDINGS.md`, `frontier/B1875_a_single_state_is_not_closed_under_composition_verified/FINDINGS.md`, `frontier/B1877_review_78_the_decadal_review/FINDINGS.md`, `frontier/B1880_p769_weave_theorems_p770_p775_and_value_card/FINDINGS.md`, and `docs/POINT_REGISTER.md` (`P-761`, `P-769`, `P-771`, `P-774`, `P-776`).
- **Literature:** Schreier (*Abh. Math. Sem. Univ. Hamburg* 5, 1927); Mayer (*Bull. Amer. Math. Soc.* 25, 1991); Ray & Singer (*Ann. of Math.* 98, 1973, Theorem 4.1) & Kubert–Lang (*Modular Units*, Grundlehren 244, 1981); Maass (*Math. Ann.* 121, 1949, pp. 141–183); Atkin & Lehner (*Math. Ann.* 185, 1970), Li (*Math. Ann.* 212, 1975), & Atkin–Li (*Invent. Math.* 48, 1978, Theorem 1.1); Hejhal (*The Selberg Trace Formula for $\mathrm{PSL}(2,\mathbb{R})$*, Vol. 2, Springer LNM 1001, 1983; *Mem. Amer. Math. Soc.* 97, No. 469, 1992).

## Disclosed

- **Zero post-seal edits & single execution:** `subweave_p776_and_hierarchy.py` was executed once against untouched Commit A (`8aafb6945`, `0` seal/hash waivers), generating `subweave_p776_and_hierarchy.json` (`elapsed_sec = 557.15`). As disclosed in `PREREGISTRATION.md`, the auxiliary cells `C0`–`C3` and `H1`–`H3` were carried as regression locks from our pre-rebase baseline alongside the `N = 1` $\mathrm{SL}_2(\mathbb{Z})$ Hejhal (1983) benchmark (`Guardrail 4`), whereas **zero level-5 Maass eigenvalues (`C4`) or `FR-FIB` evaluations at $\tau_{\text{Maass}}^*$ (`H4`) had ever been run or seen prior to Commit A**.
- **Strict Data Firewall (`0 of 19`) & Conditional Weave Typing (`P-776` / `P-774`):** Zero Standard Model measured values, zero $\chi^2$ fits, and zero held-out targets (`D11` / `P-709`) are imported, read, or compared anywhere in this arc. Per `PREREGISTRATION.md` §1.1 and §3, the positive `C4` and `H4` outcomes are graded `PROVED` **solely as a conditional weave result on stated choices** (`level = 5`, `mark` = one twin $X_1(5)$ vs both twins $X_0(5)$, `clock` = `CHOSEN` hyperbolic metric `B1815`, twin-odd ground-state peak read-out, `FR-FIB` with `H = I` `B1822`, and line/horocycle/reading), **never** as an unpriced derivation of physical parameters or a statement of arrival (`0 of 19`).

---

## 1. Summary of Pre-Registered Cells (`C0`–`C4`, `H1`–`H4`)

| Cell | Pre-Registered Target | Out-of-Sample / Locked Result | Status |
|---|---|---|---|
| **`C0`** | $\mathrm{SL}_2(\mathbb{Z})$ Hejhal (1983) benchmark (`Guardrail 4`), `B1667` control, `FR-FIB` `T`/`S` covariance, 8-draw Haar scrambling (`Guardrail 3`) | $R_1^-(\mathrm{SL}_2(\mathbb{Z})) = 9.533695261353558$ (`abs_err = 0.0`), $R_1^+ = 13.77975135189074$ (`1.78e-15`, Hecke `1.78e-13`); `B1667` `0.0`; `T`/`S` covariance `1.51e-13` / `3.72e-13`; Haar `1.29e-14` | **`PASS`** |
| **`C1`** | Infinite-$\mathrm{PSL}_2(\mathbb{Z})$ Schreier transversal of $\pm\Gamma_1(5)$ (`P-776` Case A) | Index `12`, `4` cusps of widths `(1, 1, 5, 5)`, `0` elliptic points, `13` Schreier generators, `0/2000` unfactored | **`PASS`** |
| **`C2`** | `R10-A` subweave Gauss–Mayer–Selberg operator across $N = 2..11$ | Exact old-space tie $|\rho_0(5) - \rho_0(10)| = 2.22\times 10^{-16}$ (`0.324947242493559`) via $\Omega_1(10)\twoheadrightarrow\Omega_1(5)$, while $N = 5$ uniquely minimizes $\det(I - \mathcal{M}_1|_{C_0}) = 1.19909522$ | **`PASS`** |
| **`C3`** | `R10-B/C` Kronecker–Siegel identities & holomorphic Ray–Singer vacua | Kronecker–Siegel `1.39e-48`; $X_0(5)$ Fricke saddle `Hess = (-29.36, +29.36)`; $\tau_0^*(\kappa=1) = 0.11220420 + 0.99368517i$ (`Hess > 0`), $\tau_0^{(2)*}(\kappa=2) = 0.24997290 + 7.95774584i$ (`Hess > 0`) | **`PASS`** |
| **`C4`** | **`P-776` Whole-Subweave Twin-Odd Maass Operator on $L^2_{\text{cusp}}(\Gamma_0(5), \chi_5)$ (UNRUN)** | **`27` states (`15` newform clusters) in $R \in [0.8, 11.0]$:** Ground state is the non-degenerate Class A $\mathbb{Q}(\sqrt{5})$ golden-regulator singleton $R_1 = \frac{\pi}{2\ln\varphi} = 3.264251302636499$ (`abs_err = 2.22e-15`, $\epsilon_J = \epsilon_5 = -1$, $c_2=c_3=c_6=0, c_4=+1, c_5=-1$); lowest Class B Kramers doublet $R_2 = 4.893781291438453$ (`|R_2^+ - R_2^-| = 8.88e-16`); forced zeros `< 2.3e-15`; unique global peak orbit on $C_0$ at $\tau_{\text{Maass}}^* = 0.25153978 + 0.36976714i$ (`X_0(5)` orbit `2`, `X_1(5)` orbit `4`) | **`PASS`** |
| **`H1`–`H3`** | Ray–Singer `FR-FIB` bracket (`\kappa = 1` vs `\kappa = 2`) | $\kappa = 1$: `0/96` `S-DECADE` (`max = 1.249`, `|J| = 3.86e-4`); $\kappa = 2$: `96/96` unbounded `S-DECADE` (`9.27..18.54` decades, `0/96` bounded `H4a`, `|J| <= 1.37e-11`) | **`PASS`** |
| **`H4`** | **Out-of-Sample `FR-FIB` Bounded `S-DECADE` + `|J| > 1e-8` at $\tau_{\text{Maass}}^*$ (`80% FAIL` prior)** | $\tau_{\text{Maass}}^*$ and $W_5(\tau_{\text{Maass}}^*)$ pull back to $\mp 0.25769889 + 1.84883572i \in \mathcal{F}_{\mathrm{SL}_2(\mathbb{Z})}$, where **`2/96` configurations** clear both `H4a` and `H4b` under `(S, S, S)` at `L_2` on cusp-$0$ twin lines `(1/5, 0)` and `(2/5, 0)` (`0/96` under `(St, S, S)`), Haar-invariant to `1.39e-14` | **`PASS`** |

---

## 2. Primary Result 1 (`C4`): The Twin-Odd Hyperbolic Laplacian Spectrum and Unique Fricke-Circle Peak Orbit (`P-776`)

### 2.1 Ground State $R_1 = \frac{\pi}{2\ln\varphi}$ (Class A $\mathbb{Q}(\sqrt{5})$ Singleton) vs Lowest Class B Kramers Doublet $R_2$

Scanning all four parity sectors $(\epsilon_J, \epsilon_5) \in \{\pm 1\}^2$ of $L^2_{\text{cusp}}(\Gamma_0(5), \chi_5)$ across $R \in [0.8, 11.0]$ (`M = 30`, `Q = 180` Chebyshev nodes, cross-checked on two independent horocycles $Y_{\text{ref}} = 0.145$ and $Y_{\text{chk}} = 0.132$, and independently re-solved in `tests/test_b1881_p776_whole_subweave_readout.py` on `M = 26, Q = 144, Y_ref = 0.152, Y_chk = 0.138`) yields `27` real eigenstates forming `15` joint Hecke–Maass newform eigenspaces (`0` oldforms, Atkin–Li 1978). The first five eigenspaces illustrate the exact two-class symmetry split proved before execution in `PREREGISTRATION.md` §1.3:

| Rank | Spectral Parameter $R_k$ ($\lambda_k = \frac{1}{4} + R_k^2$) | $(\epsilon_J, \epsilon_5)$ | $\dim_{\mathbb{R}} E_k$ | Class & Arithmetic Identification | Hecke / Atkin–Li Eigenvalues $(c_2, c_3, c_4, c_5)$ |
|---:|---|---|---:|---|---|
| **1 (Ground)** | **`3.264251302636499`** ($\lambda_1 = 10.90533656676408$) | `(-1, -1)` | **`1`** | **Class A (`RM` $\mathbb{Q}(\sqrt{5})$ dihedral lift):** $\frac{\pi}{2\ln\varphi}$ (`abs_err = 2.22e-15`, `ychk = 9.33e-14`) | $(0,\; 0,\; +1,\; -1)$, $c_{11} = -1.113183957920$, $c_{19} = -0.171571737965$ |
| **2** | **`4.893781291438453`** ($\lambda_2 = 24.19909532843301$) | `(-1, ±1)` | **`2`** | **Class B (Kramers doublet):** $|R_2^+ - R_2^-| = 8.88\times 10^{-16}$ | $(-1.21716141i,\; -0.29511971i,\; -0.48148190,\; 0.40170844 - 0.91576762i)$ |
| **3** | `5.844260031523029` ($\lambda_3 = 34.40537531618868$) | `(+1, ±1)` | `2` | Class B (even Kramers doublet): $|R_3^+ - R_3^-| = 7.99\times 10^{-15}$ | `ychk <= 1.24e-13` |
| **4** | **`6.528502605272997`** ($\lambda_4 = 42.87134626705635$) | `(+1, +1)` | **`1`** | **Class A (`RM` $\mathbb{Q}(\sqrt{5})$ dihedral lift):** $\frac{\pi}{\ln\varphi} = 2 R_1$ (`abs_err = 4.44e-15`) | $(0,\; 0,\; +1,\; +1)$ |
| **5** | `6.663235648870826` ($\lambda_5 = 44.64870931238262$) | `(-1, ±1)` | `2` | Class B (odd Kramers doublet): $|R_5^+ - R_5^-| = 2.58\times 10^{-14}$ | `ychk <= 2.33e-13` |

Notice the striking connection back to the golden ground `LR`: because the twin-odd character $\chi_5 = (\cdot/5)$ cuts out the real quadratic field $\mathbb{Q}(\sqrt{5})$ whose fundamental unit $\varphi = \frac{1+\sqrt{5}}{2}$ has negative norm $N(\varphi) = -1$, the lowest state of $\Delta_{\text{hyp}}$ on the whole level-5 subweave is **analytically quantized by the golden regulator $\ln\varphi$**, $R_1 = \frac{\pi}{2\ln\varphi}$, with exact Euler product $\sum_{n\ge 1} c_n n^{-s} = \sum_{\mathfrak{a}\subset\mathbb{Z}[\varphi]} \operatorname{sgn}(N(\mathfrak{a}))|\alpha/\alpha'|^{i R_1} N(\mathfrak{a})^{-s}$. In `tests/test_b1881_p776_whole_subweave_readout.py`, this 50-digit Maass (1949) series satisfies the Fricke functional identity $\psi_1(-1/(5z)) + \psi_1(z) = 0$ directly **without any pullback** to `< 1e-40` (`4.76e-46`) and matches all `26` blind numerical collocation coefficients (`< 1e-12` for $n \le 15$ incl. $p = 11$, weighted Bessel amplitude `< 1e-15` for all $n \le 26$).

### 2.2 Forced Nodal Locus, Anti-Nodal Fricke Circle $C_0$, and Unique Global Peak Orbit $\tau_{\text{Maass}}^*$

1. **Forced Nodal Vanishing (`C4(ii)`):** In full agreement with `PREREGISTRATION.md` §1.3, $\psi_1$ vanishes identically along the mirror lines $\operatorname{Re} z \in \{0, \frac{1}{2}\}$, at both order-$2$ elliptic points $z_{e,1}, z_{e,2} = \frac{\pm 2 + i}{5}$ (`9.16e-16` in float64; `< 1e-22` directly from the un-pulled-back $M = 45$ Euler series), along the side Fricke boundary circles $C_{f,2}^{\pm} : (|x| - \frac{1}{2})^2 + y^2 = \frac{1}{20}$ (`1.47e-15`, since $\epsilon_5 = +\epsilon_J$), and at both discriminant $D = -20$ Fricke CM points $z_{f,1} = \frac{i}{\sqrt{5}}$ and $z_{f,2} = \frac{1}{2} + \frac{i}{2\sqrt{5}}$ (`2.17e-20`).
2. **Why the Peak Lies Exactly on the Central Fricke Circle $C_0$:** Because the ground state has $(\epsilon_J, \epsilon_5) = (-1, -1)$, the composite anti-holomorphic involution $W_5 \circ J : z \mapsto \frac{1}{5\bar{z}}$ acts on $\psi_1$ with eigenvalue $\epsilon_5 \epsilon_J = (-1)(-1) = +1$ and fixes the central Fricke circle $C_0 = \{|z|^2 = \frac{1}{5}\}$ pointwise! Thus the normal derivative across $C_0$ vanishes identically, turning $C_0$ into a symmetry-protected anti-nodal ridge between $\psi_1(z_{f,1}) = 0$ ($\theta = \frac{\pi}{2}$) and $\psi_1(z_{e,1}) = 0$ ($\theta = \arctan\frac{1}{2}$).
3. **Unique Global Maximum Orbit (`C4(iv)`):** Over all of $\mathcal{F}^+ \cap \{0 \le x \le \frac{1}{2}\}$, the $L^2(\mathcal{F}^+)$-normalized density $\rho_1(z) = |\psi_1(z)|^2$ (`O(1)` rotation variance `0.0`) has a **single local and global maximum**, sitting strictly on $C_0$ at:
   $$\tau_{\text{Maass}}^* = 0.251539778829130 + 0.369767144294671\,i \quad \left(|\tau_{\text{Maass}}^*|^2 = \frac{1}{5},\;\; \rho_1(\tau_{\text{Maass}}^*) = 2.0718346193345\right),$$
   with full 2D gradient $\|\nabla(\psi_1^2)\| = 1.21\times 10^{-22}$ (50-dps analytic) and strictly negative-definite 2D Euclidean Hessian eigenvalues $(-20.23, -3.57) < -2.0$.
   - **On $X_0(5)$ (Case B, mark = whole eigenline):** $\tau_{\text{Maass}}^* = W_5(J(\tau_{\text{Maass}}^*))$ has stabilizer $\langle W_5 J \rangle \cong \mathbb{Z}/2\mathbb{Z}$ inside $V_4 = \langle W_5, J \rangle$, giving **exact global peak orbit size `2`**: $\{\tau_{\text{Maass}}^*, -\overline{\tau_{\text{Maass}}^*}\}$ (`Re != 0, 1/2`: spontaneous mirror/`CP` breaking).
   - **On $X_1(5)$ (Case A, mark = one twin line up to sign):** Lifting across $\delta_{\text{twin}}$ (or equivalently adjoining $W_5(\tau_{\text{Maass}}^*) = -\overline{\tau_{\text{Maass}}^*}$ as a distinct point of $X_1(5)$) gives **exact global peak orbit size `4`** under $\langle \delta_{\text{twin}}, W_5, J \rangle$.

---

## 3. Primary Result 2 (`H4`): Out-of-Sample `FR-FIB` Hierarchy & `CP` Test at $\tau_{\text{Maass}}^*$ (and Honest Structural Caveats)

### 3.1 Modular Pullback into $\mathcal{F}_{\mathrm{SL}_2(\mathbb{Z})}$ and Why Our `80% FAIL` Prior Was Overturned

Under `B1667` + `B1724` exact $\mathrm{SL}_2(\mathbb{Z})$ covariance, $\tau_{\text{Maass}}^* \in C_0$ pulls back into the standard $\mathrm{SL}_2(\mathbb{Z})$ fundamental domain via $\gamma_1 = TS = \binom{1\ -1}{1\ 0} \in \mathrm{SL}_2(\mathbb{Z})$ (and its mirror/$W_5$ partner $-\overline{\tau_{\text{Maass}}^*}$ via $\gamma_2 = \binom{-1\ -1}{1\ 0} \in \mathrm{SL}_2(\mathbb{Z})$) to the mirror pair:
$$\tau_{\text{red}}^{\pm} = \mp 0.257698894145648 + 1.848835721473356\,i \in \mathcal{F}_{\mathrm{SL}_2(\mathbb{Z})} \quad \left(L_{\max} = 0.658793445,\;\; L_2 = 2.465124332\right).$$
Because $|\tau_{\text{Maass}}^*|^2 = \frac{1}{5}$ maps under $-1/\tau_{\text{Maass}}^*$ to height $5 \cdot 0.369767144 = 1.848835721$, $\operatorname{Im}\tau_{\text{red}} \approx 1.8488$ lands directly inside the intermediate window between `R10-C1` ($\operatorname{Im}\tau_0^* = 0.9937$, where `0/96` reach $2.5$ decades) and `R10-C2` ($\operatorname{Im}\tau_0^{(2)*} = 7.9577$, where all `96/96` overshoot to `9.27..18.54` decades with $|J| \le 1.37\times 10^{-11}$).

Evaluating `main`'s unmodified `FR-FIB` Yukawa frame at $H = I$ across all `96` pre-registered discrete configurations (`24` order-5 and spin-shifted order-10 lines $\times$ `2` exact `B1667` horocycles `L_max, L_2` $\times$ `2` covariant readings `(St, S, S), (S, S, S)`), **`2 / 96` configurations** on each representative clear **both** `H4a` (bounded `S-DECADE`: $2.5 \le \log_{10}(\sigma_1/\sigma_3) \le 7.5$ and $1.0 \le \log_{10}(\sigma_1/\sigma_2) \le 4.5$ in all 3 sectors) **and** `H4b` ($|J| > 10^{-8}$), invariant to `1.39e-14` across 12 independent Haar unitary basis scramblings (`Guardrail 3`):

| Original Line on $(\tau_{\text{Maass}}^*)$ | Pulled-Back Line on $\tau_{\text{red}}^-$ | Horocycle | Reading | $\log_{10}(\sigma_1/\sigma_3)$ `(up, down, lep)` | $\log_{10}(\sigma_1/\sigma_2)$ `(up, down, lep)` | $(|V_{us}|, |V_{cb}|, |V_{ub}|)$ | Signed Jarlskog $J$ ($\tau_{\text{Maass}}^*$ vs $W_5\tau_{\text{Maass}}^*$) |
|---|---|---|---|---|---|---|---|
| **`(1/5, 0)`** (cusp-$0$ twin 1) | `(0, 1/5)` | `L_2` | `(S, S, S)` | **`(4.7623, 3.2211, 3.2211)`** | **`(1.2063, 1.2731, 1.2731)`** | `(0.1643, 0.0924, 0.0445)` | **`-3.274466e-6`** / **`+3.274466e-6`** |
| **`(2/5, 0)`** (cusp-$0$ twin 2) | `(0, 2/5)` | `L_2` | `(S, S, S)` | **`(2.9422, 3.0093, 3.0093)`** | **`(1.2537, 1.3340, 1.3340)`** | `(0.0804, 0.0155, 0.00055)` | **`+2.908926e-8`** / **`-2.908926e-8`** |

Notably, the two passing lines `(1/5, 0)` and `(2/5, 0)` in the original level-5 frame are **precisely the cusp-$0$ twin order-5 pair** (`P-717` reading (ii) / `B1845`), and the two points of the $X_0(5)$ global peak orbit carry **exact opposite chiral signs of $J$** ($\mp 3.274466\times 10^{-6}$ on `(1/5, 0)`).

### 3.2 Mandatory Caveats and What Remains Open (`P-761` / `WP-1.6`)

To prevent any over-interpretation, three exact limitations revealed by the `96`-configuration census must stand beside the `PASS` verdict:

1. **`0 / 96` Pass Under the Asymmetric Reading `(St, S, S)`:** Under `(St, S, S)` with $H = I$, `0/96` configurations reach the $2.5$-decade `S-DECADE` floor in all three sectors simultaneously (the closest configuration, `(1/5, 2/5)` at `L_2`, gives `up = 2.942` decades and $|J| = 2.93\times 10^{-3}$, while `down = lep = 1.618 < 2.5`).
2. **Exact `down = lep` Degeneracy Under `(S, S, S)` at $H = I$:** Both passing configurations occur under the symmetric reading `(S, S, S)` at $H = I$, where the `down` and `lep` Yukawa matrices share identical singular-value ratios (`3.2211` and `3.0093` decades; cf. `P-355` / `WP-0.2`).
3. **Stated Upstream Choices Remain Unremoved (`P-761`):** While `B1881` establishes the first genuine state on the whole level-5 subweave whose density singles out one mirror-breaking orbit without collapsing under composition (`B1875`), the construction still rests on stated choices (`level = 5`, `mark`, `CHOSEN` hyperbolic clock `B1815`, ground-state peak read-out vs integral average, `FR-FIB` with $H = I$, horocycle `L_2` over `L_max`, reading `(S, S, S)`, and one twin line). Thus `P-776` closes (`DONE`) as the completed design and sealed run of the twin-odd whole-subweave operator, while `P-761` (`WP-1.6`) remains `QUEUED`.
