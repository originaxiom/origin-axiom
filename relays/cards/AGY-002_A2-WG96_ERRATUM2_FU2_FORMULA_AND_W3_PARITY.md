# AGY-002 Erratum 2: Card A2-WG96 `W3` Charge-Conjugation Parity and Self-Contained `W4` `Gate F-U2` `24`-Pt Operator Equations (`0 of 19`)

- **Card:** `AGY-002 / A2-WG96` (`relays/cards/AGY-002_A2-WG96_ej5-mapping-class-family-modes-vs-weave-g96-triplet.md`)
- **Superseded Producer `v1` (`untouched`):** `relays/a2_wg96/verify_a2_wg96.py` (`380a50c54`)
- **Supersedes:** adds pre-run mathematical specification for `relays/a2_wg96_v2/verify_a2_wg96_v2.py` and the independent cold-room referee `relays/a2_wg96_referee/referee_a2_wg96.py`.

---

## 1. Two Pre-Run Mathematical Corrections Found on Static Audit of Producer `v1` (`380a50c54`)

1. **`W3` (`(M_S^{CIM})^2` parity spectrum):** On the odd-spin `(1/2, 1/2)` Level-`3` theta basis `(\psi_0, \psi_1, \psi_2)`, charge conjugation `S^2` maps `(psi_0, psi_1, psi_2) -> (-psi_2, -psi_1, -psi_0)` up to scalar U(1) phase, so its eigenvalue multiset is **`[-1, -1, 1]`** (`two odd modes + one even mode`, forcing commutant dimension `2` and `2 + 1` split), NOT `[-1, 1, 1]` (`as v1 wrongly asserted`). Furthermore, `M_T^{CIM}` eigenvalues have normalized phase turns **`[1/24, 1/24, 3/8]`** (`multiplicities 2 and 1`).
2. **`W4` (`fock_ratios_24` shorthand vs full `Gate F-U2` `24`-point `O_1(\tau)` operator):** `v1` used an incomplete unphased helper that paired `c_3` with `blocks = [Q_J, Q_I, Q_K]` rather than `q_S = [Q_I, Q_J, Q_K]` and omitted the Weil cocycle `\zeta_5^{-ab}`, Heisenberg-Weil matrices `D_1(a, b)`, `B_3/B_2` Fock kinetic metrics `(K_{Q_L}, K_{L_L}, K_{u_R}, K_{d_R}, K_{e_R})`, and `|V_{CKM}|` (`which breaks SL_2(Z) invariance at order 1/10`). Replacing that helper with the exact `Gate F-U2` operator equations below restores `L` (`tau -> tau + 1`) and `R` (`tau -> tau/(tau + 1)`) invariance of both singular-value ratios `(r_u, r_d, r_e)` and `|V_{CKM}|` to `< (1/10)^12` (`indeed < (1/10)^25 at 42 digits`).

---

## 2. Self-Contained `W4` Equations for `Gate F-U2`'s `24`-Point `O_1(\tau)` Fock-Dressed Operator (`m = 1`, `S` Reading)

Both producer `v2` and the cold-room referee implement this exact operator independently from first principles (`tau_0 = 13/100 + (17/10) i`):

1. **Quaternion Clifford Basis & Dual Couplings (`S` reading):**
   - `I_2 = [[1, 0], [0, 1]]`, `Q_I = [[i, 0], [0, -i]]`, `Q_J = [[0, 1], [-1, 0]]`, `Q_K = [[0, i], [i, 0]]`, `EPS = Q_J`.
   - `units = [I_2, Q_I, Q_J, Q_K]`, external generation triplet `blocks = [Q_J, Q_I, Q_K]`, internal half-period spin triplet **`q_S = [Q_I, Q_J, Q_K]`**.
   - With Frobenius pairing `<A, B>_H = sum_{r,c} A_{rc} B_{rc}` (`no conjugation`), define `ec_list = [EPS * U for U in units]`, Gram matrix `G_{ts} = <ec_list[t], units[s]>_H`, dual basis `edual[a] = sum_b (G^{-1})_{ba} units[b]`, and rank-`4` coupling tensor:
     `C[qi, si, a, b] = <blocks[a]^T * EPS * q_S[qi] * blocks[b], edual[si]>_H`.

2. **Half-Period Covariant Derivative `c_3(\tau)` (`weight +3/2`):**
   - Let `q = exp(2 i pi tau)`, `\eta(\tau) = exp(i pi \tau / 12) \prod_{m >= 1}(1 - q^m)`, `denom_hat = 2 \pi \eta(\tau)^3`, `E_2(\tau) = 1 - 24 \sum_{m >= 1} m q^m / (1 - q^m)`.
   - For characteristics `(\alpha, \beta)` in `{(1/2, 0), (0, 1/2), (0, 0)}` (`yielding \vartheta_2, \vartheta_4, \vartheta_3`), define `\vartheta(\alpha, \beta) = \sum_{n \in \mathbb{Z}} \exp(\pi i (n+\alpha)^2 \tau + 2\pi i (n+\alpha)\beta)` and `\dot{\vartheta}(\alpha, \beta) = (1/2) \sum_{n \in \mathbb{Z}} (n+\alpha)^2 \exp(\pi i (n+\alpha)^2 \tau + 2\pi i (n+\alpha)\beta)`.
   - Then `R_h = (-\vartheta_2^2, -\vartheta_4^2, i\vartheta_3^2) / denom_hat`, `dN_h = (-2\vartheta_2\dot{\vartheta}_2, -2\vartheta_4\dot{\vartheta}_4, 2 i\vartheta_3\dot{\vartheta}_3) / denom_hat`, and **`c_3(\tau) = dN_h(\tau) - (E_2(\tau)/12) R_h(\tau)`**.

3. **Single-Point Fock-Regulated Yukawa `Y(\tau, L_2; w_L, w_R)`:**
   - Set `a_x = w_L[0], b_x = 2 w_L[1], a_y = w_R[0], b_y = 2 w_R[1]`.
   - Define `X_0(\alpha, \beta) = \sum_{n \in \mathbb{Z}+\alpha} \exp(2\pi i \tau n^2 + 2\pi i n \beta)` and `X_1(\alpha, \beta) = \sum_{n \in \mathbb{Z}+\alpha} \exp(2\pi i \tau (n + 1/2)^2 + 2\pi i n \beta)`.
   - Build `M_m = [[X_0(a_x,b_x) X_0(a_y,b_y), -i exp(i pi b_y) X_0(a_x,b_x) X_1(a_y,b_y)], [-i exp(i pi b_x) X_1(a_x,b_x) X_0(a_y,b_y), -exp(i pi (b_x+b_y)) X_1(a_x,b_x) X_1(a_y,b_y)]] / denom_hat` and `R_ch[si] = <ec_list[si], M_m>_H` for `si in {0, 1, 2, 3}`.
   - Over `CHAR_SHIFTS = [(0, 0), (0, -1/2), (-1/2, 0), (-1/2, -1/2)]`, set `u_a = (w_L[0] + w_R[0] + ds_1) mod 1` and `u_b = (w_L[1] + w_R[1] + ds_2) mod 1` (`in [0, 1)`). If `(u_a, u_b) == (0, 0)`, set `u_ch[si] = 0`; otherwise (`\tau = x + i y, y > 0`, `w_s = \exp(2\pi i (s x + u_b) - 2\pi |s| y)`):
     - If `u_a == 0`: `f_u = \pi (2 \gamma_E - 2 \ln 2 - \ln y) + \pi^2 y / \sin^2(\pi u_b) + \sum_{m \in \mathbb{Z} \setminus \{0\}} (2\pi / |m|) \operatorname{Re}(w_m / (1 - w_m))`;
     - If `u_a != 0`: `f_u = -\pi (\psi(u_a) + \psi(1 - u_a) + 2 \ln 2 + \ln y) + \sum_{k \in \mathbb{Z}} (2\pi / |k + u_a|) \operatorname{Re}(w_{k+u_a} / (1 - w_{k+u_a}))` (`where \psi is the digamma function`);
     - With `\nu = u_a` if `u_a <= 1/2` else `u_a - 1`, `B_m = (-u_b) mod 1`, `w_z = \nu \tau - B_m`:
       `a_0 = \pi \cot(\pi w_z) + 4\pi \sum_{m >= 1} (\exp(2\pi i m (\tau + w_z)) - \exp(2\pi i m (\tau - w_z))) / (2 i (1 - q^m)) + 2\pi i \nu`;
     - Then `u_ch[si] = sqrt(2\pi (L_2 + (1/2)\ln y - \gamma_E - \ln\pi) + f_u - \pi |a_0|^2 \exp(-2 L_2)) * R_ch[si]` and:
       `Y_{ab}(\tau, L_2; w_L, w_R) = \sum_{qi=0}^2 \sum_{si=0}^3 c_3[qi] u_ch[si] C[qi, si, a, b]`.

4. **`24`-Point `E[5]\setminus\{0\}` Weil-Covariant Fock Operator (`m = 1`), Kinetic Metrics, & `B_3 = <L, R>` Invariance Law:**
   - With `\zeta_5 = \exp(2\pi i / 5)`, `5 \times 5` shift/clock matrices `X_{(j+1)\bmod 5, j} = 1`, `Z_{jj} = \zeta_5^j`, define `D_1(a, b) = \zeta_5^{(3ab)\bmod 5} X^a Z^b` and orthogonal parity bases `B_3` (`columns e_0, (e_1+e_4)/\sqrt{2}, (e_2+e_3)/\sqrt{2}`) and `B_2` (`columns (e_1-e_4)/\sqrt{2}, (e_2-e_3)/\sqrt{2}`).
   - Sum over the `24` points `(a, b) \in \{0,1,2,3,4\}^2 \setminus \{(0,0)\}` using centered representatives `a_c, b_c \in \{-2, -1, 0, 1, 2\}` (`w_L = (a_c/5, b_c/5)`, `w_R = (2 a_c/5, 2 b_c/5)`) and Weil cocycle phase `\phi_{ab} = \zeta_5^{(-ab)\bmod 5}`:
     - `S_{ph} = \sum_{w \neq 0} \phi_{ab} Y(w)`, `Y_{base} = Y(0, 0)`,
     - `O_3[i, ca, j, cb] = \sum_{w \neq 0} \phi_{ab} Y_{ij}(w) (B_3^H D_1(a, b) B_3)_{ca, cb}`,
     - `O_2[i, wa, j, wb] = \sum_{w \neq 0} \phi_{ab} Y_{ij}(w) (B_2^H D_1(a, b) B_2)_{wa, wb}`,
     - `G_{3,L}[i, k] = (1/3)\sum_{ca,j,cb} O_3[i,ca,j,cb] \overline{O_3[k,ca,j,cb]}`,
     - `G_{2,L}[i, k] = (1/2)\sum_{wa,j,wb} O_2[i,wa,j,wb] \overline{O_2[k,wa,j,wb]}`,
     - `G_{3,R}[i, k] = (1/3)\sum_{j,ca,cb} \overline{O_3[j,ca,i,cb]} O_3[j,ca,k,cb]`,
     - `G_{2,R}[i, k] = (1/2)\sum_{j,wa,wb} \overline{O_2[j,wa,i,wb]} O_2[j,wa,k,wb]`.
   - From Fock kinetic metrics `K_{Q_L} = G_{3,L} + G_{2,L}`, `K_{L_L} = 3 G_{3,L} + G_{2,L}`, `K_{u_R} = 2 G_{3,R}`, `K_{d_R} = 2 G_{3,R} + 2 G_{2,R}`, `K_{e_R} = 2 G_{2,R}`, form `Y_u = K_{Q_L}^{-1/2} Y_h K_{u_R}^{-1/2}`, `Y_d = K_{Q_L}^{-1/2} Y_h K_{d_R}^{-1/2}`, `Y_e = K_{L_L}^{-1/2} Y_h K_{e_R}^{-1/2}` (`for both Y_h = S_{ph} and Y_h = Y_{base}`), extract singular-value ratios `r_f = [\sigma_1/\sigma_0, \sigma_2/\sigma_0]` (`sorted descending` or indexed consistently across images) and `|V_{CKM}| = |U_u^H U_d|` (`where U_f diagonalizes Y_f Y_f^H`).
   - Under `L: \tau_0 \mapsto \tau_0 + 1` and `R: \tau_0 \mapsto \tau_0 / (\tau_0 + 1)`, the Horocycle shift law `L_2(\gamma\tau) = L_2(\tau) + \ln|c\tau + d|` gives `L_2(\tau_0 + 1) = L_2(\tau_0)` and `L_2(\tau_0/(\tau_0 + 1)) = L_2(\tau_0) + \ln|\tau_0 + 1|`.
   - **Added `W4` Bar:** Verify that both `(r_u, r_d, r_e)` and `|V_{CKM}|` are invariant (`< (1/10)^12` drift) under BOTH `L` and `R` at `\tau_0 = 13/100 + (17/10) i` for both `phased_sum` and `base_w0`, across BOTH the punctured-torus ODE value `L_2(\tau_0)` and an exact rational Horocycle seed `L_2(\tau_0) = 5/2`. `0 of 19.`
