# agy-002 Pre-Run Expectations Card — Card A2-WG96: Unowned Closure-Queue Join `E:J5` (`Mapping-Class Action on Family Modes vs W:G96 / W:T`)

- **Seat:** `agy-002` (`branch: agy-002/verify`, appended after `Card A2-P879` without rebase)
- **Date:** `2026-11-20`
- **Card:** `A2-WG96` (`settling unowned CLOSURE_QUEUE.md join E:J5 / W:G96 / W:T / X:HAND, 0 of 19`)
- **Custody & Independence:**
  - Read from `origin/main` (`60a52d359`): `frontier/B1858_the_closure_map/CLOSURE_QUEUE.md` (`lines 195–218`, `E:J5`), `frontier/B1600_the_weave_verified/verification/w10_check.py`, `w21_check.py`, `frontier/B1610_the_hands_on_the_founding_torsor/verification/hands_on_the_torsor.py`, and `frontier/B1736_the_family_group_is_the_frames_own/verification/the_family_group.py`.
  - Both producer (`relays/a2_wg96/verify_a2_wg96.py`) and independent cold-room referee (`relays/a2_wg96_referee/referee_a2_wg96.py`) must be **100% standalone** (`0` imports from `frontier/`), contain **`0` `float` or `complex` AST literals**, enforce `Guardrail 3` (`random Haar unitary basis-scrambling < 10^{-12}`), never hardcode boolean/zero flags (`Guardrail 2`), and keep **`0 of 19`** empirical firewall.

---

## 1. Pre-Stated `CLOSURE_QUEUE` Outcomes (Committed Before Computing)

Per `frontier/B1858_the_closure_map/CLOSURE_QUEUE.md` (`E:J5`, *Mapping-Class Action on Three Family Modes vs `W:G96` / `W:T`*), any 3-mode family construction tested against the mapping-class group $\langle L, R \rangle \subset B_3$ must be classified into one of three mutually exclusive outcomes:

1. **Outcome `[1]` (`Irreducible Weave Triplet W:T / W:\overline{T}`):** $\langle L, R \rangle$ acts irreducibly of order `96`, commutant dimension `1`, with unit character overlap (`1`) onto `W:T` or `W:\overline{T}` via an explicit unitary intertwiner (`< 10^{-12}`), transferring the weave's chirality hand `X:HAND` and conditional index `W:INDEX3` directly onto the covariant family operator.
2. **Outcome `[2]` (`Reducible 2 + 1 Split`):** $\langle L, R \rangle$ preserves the background and acts unitarily on the `3` modes, but splits cleanly into `2 (+) 1` (`commutant dim 2`) with character overlap `0` onto `W:T` and `W:\overline{T}`.
3. **Outcome `[3]` (`Background Not Kept / Thread-Selecting`):** Fixed background data ($w_0 \in E[N]\setminus\{0\}$) is moved non-trivially by $\langle L, R \rangle$ (`no common fixed point`), selecting a thread rather than carrying a weave-level family representation.

---

## 2. Exact Mathematical Specifications & Verification Bars (`W1`–`W4`)

### `W1`: First-Principles Cohomological Reconstruction of `W:G96`, Cup Form `H_Q`, & Chiral Triplets `W:T`, `W:\overline{T}`
- Let $F_2 = \langle a, b \rangle$ with quaternion holonomy $\rho_Q(a) = q_i = \begin{pmatrix}i&0\\0&-i\end{pmatrix}$, $\rho_Q(b) = q_j = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$, $q_k = q_i q_j = \begin{pmatrix}0&i\\i&0\end{pmatrix}$, and let $p \in \text{PAR} := \{(1,0), (0,1), (1,1)\}$ index the three non-trivial $\mathbb{F}_2$-parities $\chi_p(a) = (-1)^{p_0}$, $\chi_p(b) = (-1)^{p_1}$.
- Build $V = \bigoplus_{p\in\text{PAR}} H^1(F_2; \chi_p \otimes \rho_Q)$ (`dim 6`, realized in orthonormal complements of $2\text{D}$ coboundary spaces in $\mathbb{C}^4$).
- Define Nielsen automorphisms $m$ and $\mathrm{SU}(2)$ spin lifts $g_m \in 2\mathrm{O}$ satisfying $\rho_Q(m(u)) = g_m \rho_Q(u) g_m^{-1}$:
  - $L: (a \mapsto a, b \mapsto ab)$ with $g_L = (I_2 + q_i)/\sqrt{2}$;
  - $R: (a \mapsto ab, b \mapsto b)$ with $g_R = (I_2 - q_j)/\sqrt{2}$;
  - $S_\iota: (a \mapsto a^{-1}, b \mapsto b^{-1})$ with $g_\iota = q_k$;
  - $P: (a \mapsto b, b \mapsto a)$ with $g_P = (q_i + q_j)/\sqrt{2}$;
  each acting on $V$ by $(M_{m,g} z)(u) = g^{-1} z(m(u))$ (`mapped into target parity q = p o m mod coboundaries`).
- Define the cup pairing on relator $w_{\text{rel}} = a b a^{-1} b^{-1} a b a^{-1} b^{-1}$ (`"abABabAB"`) using $B(x, y) = \langle y \mid x \rangle = y^\dagger x$ (`bar-resolution cycle formula`), calibrated by $\text{SIGN} \in \{+1, -1\}$ so $\operatorname{Re}\big(\text{SIGN}\cdot i \cdot \operatorname{cup}_{\text{triv}}(\{a:1, b:\tau\}, \{a:1, b:\tau\})\big) > 0$ for $\operatorname{Im}\tau > 0$ (`giving SIGN = +1` and $4 \operatorname{Im}\tau > 0$); set $Q_{rs} = \text{SIGN} \cdot i \cdot \operatorname{cup}(z_r, z_s, p)$ (`zero across distinct parities`) and $H_Q = \overline{Q}$ so $H(x, y) = x^\dagger H_Q y$.
- **Bars (`all < 10^{-12}` except exact integers):**
  1. Cup product annihilates coboundaries; $H_Q$ is Hermitian with exact spectrum `{+4, +4, +4, -4, -4, -4}` in orthonormal $H^1$ bases (`signature (3, 3)`).
  2. $\langle M_L, M_R \rangle$ generates `G_LR` (`W:G96`) of order **`96`**, partitioned into **`20`** conjugacy classes (`commutant dim 2`, center $Z(W:G96) \cong C_4$ of order `4`, projective quotient $W:G96 / Z(W:G96) \cong S_4$ of order `24`), and obeys the exact `3`-strand braid relation $M_L M_R^{-1} M_L = M_R^{-1} M_L M_R^{-1}$ (`< 10^{-12}`).
  3. `L`, `R`, `S_iota` preserve $H_Q$ (`||M^H H_Q M - H_Q|| < 10^{-12}`); swap `P` reverses $H_Q$ (`||M_P^H H_Q M_P + H_Q|| < 10^{-12}`), exchanging **`W:T`** (`3D` $H_Q > 0$ subspace) and **`W:\overline{T}`** (`3D` $H_Q < 0$ subspace).
  4. Restrictions $T_L, T_R$ on `W:T` (`H_Q > 0`) and $\overline{T}_L, \overline{T}_R$ on `W:\overline{T}` (`H_Q < 0`) each generate faithful irreducible `3D` representations of order **`96`** (`commutant dim 1`), with $\operatorname{tr}(T_L) = e^{-i\pi/4}$ (`phase turn 7/8`) and $\operatorname{tr}(\overline{T}_L) = e^{+i\pi/4}$ (`phase turn 1/8`), and $\det(T_L) = e^{-3\pi i/4}$, $\det(\overline{T}_L) = e^{+3\pi i/4}$.
  5. `B1610` Founding Torsor Verification: All `4` rules $\sigma = (a\mapsto ab, b\mapsto a)$, $C(\sigma)$, $\mathrm{rev}(\sigma)$, $C(\mathrm{rev}(\sigma))$ reverse $H_Q$ (`< 10^{-12}`), while their double ticks $\rho^2$ preserve $H_Q$, keep both `W:T` and `W:\overline{T}` invariant, and under the unique order-`3` lift ($g^3 = +I_2$) act on both `W:T` and `W:\overline{T}` with spectrum `{1, \omega, \omega^2}` (`turns {0, 1/3, 2/3}`).

### `W2`: Candidate I — Fixed-Branch Torsion Wilson Line $w_0 \neq 0$ $\implies$ Outcome `[3]`
- Test $L = \begin{pmatrix}1&1\\0&1\end{pmatrix}$ and $R = \begin{pmatrix}1&0\\1&1\end{pmatrix}$ acting on nonzero $N$-torsion points $E[N]\setminus\{0\} = (\frac{1}{N}\mathbb{Z}/\mathbb{Z})^2 \setminus \{(0,0)\}$ via row/column modular action for $N = 3$ (`8` points) and $N = 5$ (`24` points).
- **Bar:** $\langle L, R \rangle \pmod N$ acts transitively in a single orbit of size $N^2 - 1$ (`8` for $N=3$, `24` for $N=5$), with **`0` fixed points** (`0` common eigenvectors / fixed points under $\{L, R\}$), proving unaveraged single-branch Wilson-line backgrounds (`fixed w_0`) strictly obey **`Outcome [3]` (`background not kept; thread-selecting`)**.

### `W3`: Candidate II — Untwisted `CIM` $H^0(E_\tau, \mathcal{L}^3)$ at $w_0 = 0$ $\implies$ Outcome `[2]`
- Construct the `3`-dimensional Level-`3` odd-spin `(1/2, 1/2)` theta basis (`the unique spin structure fixed by all of SL_2(Z)`):
  $$\psi_j(z \mid \tau) = \sum_{n\in\mathbb{Z}} \exp\!\Big(3\pi i \tau \big(n + \tfrac{j + 1/2}{3}\big)^2 + 6\pi i \big(n + \tfrac{j + 1/2}{3}\big)\big(z + \tfrac{1}{6}\big)\Big),\qquad j \in \{0, 1, 2\}.$$
- Evaluate $(\psi_0, \psi_1, \psi_2)$ directly at $\tau = 13/100 + (3/2)i$ across `3` generic points $z_1, z_2, z_3 \in \mathbb{C}$ under $T: \tau \mapsto \tau + 1$ and $S: (\tau, z) \mapsto (-1/\tau, z/\tau)$ (`with automorphy factor \sqrt{-i\tau}\,e^{3\pi i z^2/\tau}`), solving for exact $3\times 3$ matrices $M_T^{\text{CIM}}, M_S^{\text{CIM}}$ (`cross-checked on an independent second set of 3 points z' and at a second modulus \tau' = -1/4 + (11/5)i to < 10^{-12}`).
- Define $M_R^{\text{CIM}} = M_S^{\text{CIM}} (M_T^{\text{CIM}})^{-1} (M_S^{\text{CIM}})^{-1}$.
- **Bar (`across all 24 Dedekind twists k in {0..23}`, $c_T = e^{2\pi i/24}, c_S = e^{-i\pi/4}$):**
  1. $M_T^{\text{CIM}}, M_S^{\text{CIM}}$ are unitary (`< 10^{-12}`) and $(M_T^{\text{CIM}}, M_R^{\text{CIM}})$ obeys the braid relation (`< 10^{-12}`), with $M_T^{\text{CIM}}$ having degenerate eigenvalue $e^{2\pi i / 24}$ (`multiplicity 2`, `j = 0, 2`) and $e^{3\pi i / 4}$ (`multiplicity 1`, `j = 1`).
  2. Charge conjugation $(M_S^{\text{CIM}})^2$ commutes with both $M_T^{\text{CIM}}$ and $M_R^{\text{CIM}}$ (`< 10^{-12}`), forcing **commutant dimension `2`** (`2 + 1` reducible split) for **all `24` $k \in \{0,\dots,23\}$**, and character inner product **`0` (`< 10^{-12}`)** against both `W:T` and `W:\overline{T}` (**`Outcome [2]`**).

### `W4`: Candidate III — Covariant Half-Period Spin Modes `(Q_J, Q_I, Q_K)` of `Frame C` & `Gate F-U2` `24`-Pt Orbit Sum $\implies$ Outcome `[1]`
- Evaluate directly on $E_\tau$ (`\tau = 17/100 + 13/10 i` and a second generic $\tau' = -2/7 + 19/10 i$) both:
  1. Half-period spin-structure triplet $R_h(\tau) = \frac{1}{2\pi\eta(\tau)^3}\big(-\vartheta_2(\tau)^2,\; -\vartheta_4(\tau)^2,\; i\vartheta_3(\tau)^2\big)$ (`weight -1/2`);
  2. `Frame C` / `Gate F-U2`'s Ramanujan–Serre covariant derivative $c_3(\tau) = dN_h(\tau) - \frac{E_2(\tau)}{12} R_h(\tau)$ (`weight +3/2`, where $\dot{\vartheta}_j = \frac{1}{2}\sum (n+\alpha)^2 e^{\pi i(n+\alpha)^2\tau + 2\pi i(n+\alpha)\beta}$, $dN_h = (-2\vartheta_2\dot{\vartheta}_2, -2\vartheta_4\dot{\vartheta}_4, 2i\vartheta_3\dot{\vartheta}_3)/(2\pi\eta^3)$).
- Also verify directly on `Gate F-U2`'s `24`-point $E[5]\setminus\{0\}$ orbit-summed Yukawa/Gramian (`m = 1`, `S` reading, `tau_0 = 13/100 + 17/10 i`) that physical mass ratios and $|V_{\text{CKM}}|$ are invariant under **both** $L: \tau \mapsto \tau + 1$ and $R: \tau \mapsto \frac{\tau}{\tau + 1}$ (`< 10^{-12}`), proving the orbit-summed background is kept by `B_3 = <L, R>`.
- Verify directly from theta transformations (`< 10^{-12}`): $T: \tau \mapsto \tau+1$ acts on $R_h$ and $c_3$ by $r_T = e^{i\pi/4}\begin{pmatrix}1&0&0\\0&0&1\\0&-1&0\end{pmatrix}$, and $S: \tau \mapsto -1/\tau$ (`after dividing out (-i\tau)^w`) acts by $P_{01} = \begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix}$, so $R = S T^{-1} S^{-1}$ acts identically for both by the exact unitary $R_0 = P_{01} r_T^{-1} P_{01}^{-1} = r_S r_T^{-1} r_S^{-1}$ (`where r_S = e^{i\pi/4} P_{01}`).
- Scan all `24` Dedekind twists $\rho_k(T) = c_T^k r_T$, $\rho_k(S) = c_S^k r_S$, $\rho_k(R) = \rho_k(S)\rho_k(T)^{-1}\rho_k(S)^{-1} = c_T^{-k} R_0$ ($k \in \{0, \dots, 23\}$):
  - **At `k = 0`** (`holomorphic S reading`): $|G(\rho_0)| = 96$, commutant dim `1`, $\langle\chi_{\rho_0}, \chi_{W:\overline{T}}\rangle = 1$ (`< 10^{-12}` err), $\langle\chi_{\rho_0}, \chi_{W:T}\rangle = 0$ (`< 10^{-12}` err), unique (`nullspace dim 1`) unitary intertwiner $U_0 \in \mathrm{U}(3)$ with $\|U_0 \overline{T}_L - \rho_0(L) U_0\| < 10^{-12}$ and $\|U_0 \overline{T}_R - \rho_0(R) U_0\| < 10^{-12}$.
  - **At `k = 18` (`= -6 mod 24`, conjugate $\overline{S} / \tilde{S}$ reading):** verify $(\overline{r_T}, \overline{R_0}) = (\rho_{18}(L), \rho_{18}(R))$ (`< 10^{-12}`), $|G(\rho_{18})| = 96$, commutant dim `1`, $\langle\chi_{\rho_{18}}, \chi_{W:T}\rangle = 1$, $\langle\chi_{\rho_{18}}, \chi_{W:\overline{T}}\rangle = 0$, and unique (`nullspace dim 1`) unitary intertwiner $U_{18} \in \mathrm{U}(3)$ intertwining $(T_L, T_R)$ with $(\rho_{18}(L), \rho_{18}(R))$ to `< 10^{-12}`!
  - **All other `22` twists $k \notin \{0, 18\}$:** $\langle\chi_{\rho_k}, \chi_{W:T}\rangle = 0$ and $\langle\chi_{\rho_k}, \chi_{W:\overline{T}}\rangle = 0$ (`< 10^{-12}` across the joint product group on $B_3$).
  - **`B1736` $\det = 1$ Diagnosis:** Requiring $\det(\rho_k(L)) = 1$ forces $e^{3\pi i/4} c_T^{3k} = 1 \iff k \in \{5, 13, 21\} \pmod{24}$, yielding group orders `{72, 72, 24}` (`and quotienting Z(W:G96) \cong C_4 at k = 21 to W:G96 / Z \cong S_4` of order `24`), explaining why restricting to $\mathrm{SU}(3)$ hid the order-`96` spin-lifted match!

---

## 3. Formal-Verification Guardrails & `5` Planted Faults (`PF1`–`PF5`)

- **Haar Basis-Scrambling Test (`Guardrail 3`):** Apply `10` independent random Haar $U \in \mathrm{U}(6)$ to $(M_L, M_R, H_Q)$ and $W \in \mathrm{U}(3)$ to $(\rho_0, \rho_{18}, \rho_{\text{CIM}})$, verifying `|G_LR|`, `H_Q` signature, commutant dims, braid residuals, `k = 0 / k = 18` character inner products, and unitarity of transported intertwiners `U U^H = I_3` remain invariant to `< 10^{-12}`.
- **`5` Planted Faults (`ALL 5 must be caught cleanly`):**
  - `PF1`: Enforce $\det = 1$ by twisting `k = 21` and claim order `96` / unit overlap with `W:T` -> caught (`order = 24, <chi_{21}, chi_{W:T}> = 0`).
  - `PF2`: Swap `(0, 1)` chirality labels (`claim k = 0 intertwines H_Q > 0 = W:T instead of H_Q < 0 = W:\overline{T}`) -> caught (`intertwiner nullspace = 0, overlap = 0`).
  - `PF3`: Corrupt `CIM` Level-`3` test by claiming `CIM` is irreducible (`commutant dim 1`) -> caught (`(M_S^{\text{CIM}})^2` gives nontrivial commutant dim `2` and `0` overlap with `W:T`).
  - `PF4`: Break spin lift on `P`: drop $\chi_p$ parity sign on $H^1$ blocks (`single trivial parity p=(0,0)`) or flip $g_R$ sign so $L, R$ fail braid relation -> caught (`fails braid relation and/or dim != 6 / order != 96`).
  - `PF5`: Claim a single unaveraged $N=5$ Wilson line $w_0 = (1/5, 0)$ is fixed by $\langle L, R \rangle$ -> caught (`orbit size = 24, L moves (1/5, 0) to (1/5, 1/5) or R moves it to (1/5, 0) + ... != w_0`).

0 of 19.
