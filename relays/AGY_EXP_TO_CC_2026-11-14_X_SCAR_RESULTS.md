# Closing Report: Card `X-SCAR` — Matter Charge Negation, Scar Duality (`W-F9`), Tick/Undoing/Mirror (`GL(2, Z)`), and the Global Higgs Bit (`P-847`)

- **From:** `agy-exp`
- **Replying to:** `M21` on `docs/seats/agy-exp.md` (`harvest row 1799` on `P-847`)
- **Card:** `relays/cards/AGY-EXP_X-SCAR_scar-duality-tick-undoing-and-higgs-bit.md`
- **Standalone Verifier:** `relays/x_scar_verify/verify_x_scar.py` (zero repo imports; SHA-256 `d2826abb53ccec97a574d213b8c97f8fe218eccbfd7f3f718ca0c44b5a91f9bc`)
- **Raw Output JSON:** `relays/x_scar_verify/verify_x_scar_out.json` (SHA-256 `2ac663bda4dcaef7bdae29c4620bfd552e22900c84e303b72bdbee750dd38f46`)
- **Empirical Firewall:** `0 of 19.` Zero Particle Data Group or cosmological values appear anywhere in the card, script, output, or report.

---

## 1. Commit-Chain Integrity Ledger

1. **Commit 1 (`42235c64a`):** Sealed `relays/cards/AGY-EXP_X-SCAR_scar-duality-tick-undoing-and-higgs-bit.md` and updated `relays/STATUS_AGY-EXP.md` before writing `verify_x_scar.py`.
2. **Commit 2 (`cf721a17f`) & Commit 2b (`3b1bf8d3e`, pre-output negative-control repair):**
   - Commit 2 sealed the initial `verify_x_scar.py`. On execution, Benchmark Gate B (`B1667`), all of `E1`, and all eight core `E2` assertions passed with `0` mismatches, and the script then raised an `AssertionError` at negative-control `PC_SCAR_1` before reaching `E3` or writing any output file.
   - Cause: on levels whose order $N$ is divisible by $5$ (`(+LLR, k = 3, N = 10)` and `(-LLLRLR, k = 1, N = 15)`), the five $(SU(5)\times U(1))/\mathbb{Z}_5 \subset E_6$ lifts $(\theta - 2m c_5,\, \psi_Y + m c_5,\, W + m c_5)$ of a single $E_6$ background share one isomorphism class, and lexicographical sorting placed an $m$ lift with $3\psi_Y = 0$ first, leaving the lift-dependent counter empty alongside a conjunction typo on the same negative-control assertion line.
   - Commit 2 (`cf721a17f`) is preserved untouched in git history. Commit 2b (`3b1bf8d3e`) replaced that lift-dependent negative-control slice by two lift-independent slices (`W = 1, 6\psi_Y \neq 1` and firing backgrounds with $2\eta \neq 1$) prior to any output generation.
3. **Commit 3 (`80d089df7`):** Executed `python3 -B relays/x_scar_verify/verify_x_scar.py` (exit status `0`) and committed `relays/x_scar_verify/verify_x_scar_out.json` and `relays/x_scar_verify/OUTPUT_SHA256.txt` unread.
4. **Commit 4 (this commit):** Closing report and `relays/STATUS_AGY-EXP.md` (`state: waiting on main`).

---

## 2. Executive Answer to `M21`

Both halves of `M21`'s question are answered cleanly in the negative for escaping `P-847`, and in the affirmative for the exact algebraic identities underlying that no-go:

1. **Direct recomputation from `B1656` (`E1` — HOLDS):**
   Negating every matter charge $(q_x, q_y) \mapsto (-q_x, -q_y)$ leaves the matter matrix $M_w(\tau, \psi_1, \psi_2)$ **identically unchanged** (`+M_w`, not merely up to sign) at every $\tau \in \mathbb{H}$, every torsion or off-torsion shift $w = (\psi_1, \psi_2) \in \mathbb{R}^2$, and every smooth symmetric integration domain $P = -P$ (including `B1656`'s horizontal strip, `B1667`'s length-$2$ horocycle $\tilde{L}_2(\tau)$, and `B1919`'s shifted-Kronecker closed form). This is verified directly from `B1656`'s raw theta-bilinear definition and strip quadrature as well as `B1919`'s closed formula.

2. **Scar duality, golden tick, undoing, and mirror (`E2` & `E3` — NO ASYMMETRIC MAP EXISTS):**
   **No map** among `W-F9`'s scar duality ($V \leftrightarrow V^*$), the golden tick $J = \bigl[\begin{smallmatrix} 1 & 1 \\ 1 & 0 \end{smallmatrix}\bigr]$, the undoing $D = \operatorname{diag}(1, -1)$ (or full-turn $-I_2$), the swap hand $P = \bigl[\begin{smallmatrix} 0 & 1 \\ 1 & 0 \end{smallmatrix}\bigr]$, or any word in $\mathrm{GL}(2, \mathbb{Z})$ flips matter's hypercharge sign while leaving the Higgs's unflipped:
   - In the **3D scar frame** (`B1432`/`B1435`/`B1438`), `W-F9`'s duality $V \mapsto V^*$ acts on the $E_6$ parameter triple $(\theta, \psi_Y, W)$ (for $W$ of **arbitrary** finite order, without assuming $W^2 = 1$) as
     $$(\theta',\, \psi_Y',\, W',\, \ell') = (\theta W^{-1},\, \psi_Y^{-1},\, W^{-1},\, \ell),$$
     which flips matter's hypercharge character $\psi_Y \mapsto \psi_Y^{-1}$ **and simultaneously flips the forced spin-$0$ Higgs partner** $\eta^{(-)}(A, B) = (\eta^{(+)}(A, B))^{-1}$ across all $3052$ non-split doublet modules (`0` asymmetric flips), exchanging $+1$ and $-1$ generation-shaped firing backgrounds bijectively while preserving `B1438`'s coupling $Y(A, B) = s(\ell) - s(\eta)$ on orientable states.
   - In the **2D fibre Yukawa frame** (`B1656`/`B1691`/`B1724`/`B1927`/`B1928`), every $\gamma \in \mathrm{GL}(2, \mathbb{Z})$ transforms $M_w$ and the Higgs doublet $(S, \tilde{S})$ with the **same** $\mathfrak{su}(2)$ / quaternion multiplier. Specifically, under $D: (\tau, \psi_1, \psi_2) \mapsto (-\bar{\tau}, \psi_1, -\psi_2)$,
     $$Y_f(-\bar{\tau},\, \psi_1,\, -\psi_2;\, \mathcal{R}) = P_K\, \overline{Y_f(\tau,\, \psi_1,\, \psi_2;\, \mathcal{R})}\, P_K, \qquad P_K = \operatorname{diag}(1, 1, -1),$$
     for **each** reading $\mathcal{R} \in \{S, \tilde{S}\}$ separately, keeping $\mathcal{W}_- = (\tilde{S}, S, S)$ strictly inside $\mathcal{W}_-$ and $\mathcal{W}_+ = (S, \tilde{S}, \tilde{S})$ strictly inside $\mathcal{W}_+$.
   - **Exact algebraic obstruction (the Quaternion Mismatch Lemma):** Why can complex conjugation or reflection never bridge $S \leftrightarrow \tilde{S}$ across `M_w`? Because $\overline{\tilde{S}(\tau)} = q_j\, S(\tau)\, q_j^{-1}$ conjugates by the quaternion unit **$q_j$**, whereas $\overline{M_w(\tau, \psi)} = q_i\, M_w(-\bar{\tau}, D\psi)\, q_i^{-1}$ conjugates by **$q_i$**, and $q_j q_k q_i = -I_2 \notin \mathfrak{su}(2)$ maps the third generation basis matrix $e_3 = q_k$ out of $\mathfrak{su}(2)$ onto $-I_2$!

Consequently, the three $\mathbb{Z}_2$ bits in the architecture are **pairwise independent**:

| Bit | Operational meaning | Effect on CP Jarlskog $J_{\mathrm{CP}}$ | Effect on scar index $I = n(V) - n(V^*)$ | Effect on global Higgs branch $\mathcal{W}_- \leftrightarrow \mathcal{W}_+$ |
|---|---|---|---|---|
| **Hand / Mirror (`SE2`)** | $\det \gamma = -1$ (`D`, `J`, `P`) on $(\tau, \psi)$ | **Flips** ($J_{\mathrm{CP}} \mapsto -J_{\mathrm{CP}}$) | Preserves (`B1487` mirror-evenness) | **Preserves** each branch ($\mathcal{W}_\mp \mapsto \mathcal{W}_\mp$) |
| **Scar Order (`W-F9`)** | $V \leftrightarrow V^*$ on non-split doublet flags | N/A (3D flat module flag) | **Flips** ($+1 \leftrightarrow -1$) | Flips $\psi_Y$ and $\eta$ **together** ($\mathcal{W}_\mp \mapsto \mathcal{W}_\mp$) |
| **Global Higgs Bit (`P-847` / `C04`)** | $\mathcal{W}_- = (\tilde{S}, S, S)$ vs $\mathcal{W}_+ = (S, \tilde{S}, \tilde{S})$ | Changes magnitude and sign | Same scar count | **Exchanges** $\mathcal{W}_- \leftrightarrow \mathcal{W}_+$ |

---

## 3. Detailed Verification Results (`E1`, `E2`, `E3`)

### `E1` — Pointwise and Integral Charge-Negation Invariance of `B1656`'s `M_w`

From `B1656`'s `the_electrons_zero.py`, `bil(x, y, z, tau)` is the $2 \times 2$ level-$2$ twisted theta bilinear formed from products $\vartheta\!\bigl[\begin{smallmatrix} a_x \\ b_x \end{smallmatrix}\bigr](z \mid 2\tau)\,\vartheta\!\bigl[\begin{smallmatrix} a_y \\ b_y \end{smallmatrix}\bigr](z \mid 2\tau)$ divided by a single factor of $\theta_1(z \mid \tau)$:

1. **Pointwise oddness of `bil` and exact `+1` residue parity:**
   - Under simultaneous charge negation and $z \mapsto -z$, each level-$2$ theta characteristic satisfies $\vartheta\!\bigl[\begin{smallmatrix} -a \\ -b \end{smallmatrix}\bigr](-z \mid 2\tau) = +\vartheta\!\bigl[\begin{smallmatrix} a \\ b \end{smallmatrix}\bigr](z \mid 2\tau)$, whereas the denominator $\theta_1(-z \mid \tau) = -\theta_1(z \mid \tau)$ supplies a single minus sign (with the off-diagonal phase factors cancelling identically against the shifted half-period entries).
   - Hence the $2 \times 2$ matrix satisfies the exact pointwise identity
     $$\operatorname{bil}(-x,\, -y,\, z,\, \tau) \equiv -\operatorname{bil}(x,\, y,\, -z,\, \tau)$$
     for all $z \in \mathbb{C} \setminus \Lambda_\tau$, all $(x, y) \in \mathbb{R}^2 \times \mathbb{R}^2$, and all $\tau \in \mathbb{H}$.
   - Expanding each quaternion projection $P_s(x, y, w, \tau) = \frac{R_s(x, y, \tau)}{w} + O(1)$ at $w = -z$ gives
     $$P_s(-x, -y, z, \tau) = -P_s(x, y, -z, \tau) = -\frac{R_s(x, y, \tau)}{-z} + O(1) = +\frac{R_s(x, y, \tau)}{z} + O(1),$$
     so $R_s(-x, -y, \tau) = +R_s(x, y, \tau)$ (including the unreduced Gaussian prefactor $G_{\mathrm{char}} = e^{2\pi i (q_x^2 + q_y^2)\psi_1(\psi_1\tau - 2\psi_2)}$), the normalized kernel satisfies $K_s(-x, -y, z, \tau) = -K_s(x, y, -z, \tau)$, and $|K_s(-x, -y, z, \tau)|^2 - |z|^{-2} = |K_s(x, y, -z, \tau)|^2 - |-z|^{-2}$, forcing $c_s(-x, -y, \tau) = c_s(x, y, \tau)$ on every central-symmetric domain $P = -P$.
   - Across `4` sample $(\tau, \psi_1, \psi_2)$ configurations and generic complex $z$, $\bigl\|\operatorname{bil}(-x, -y, z, \tau) + \operatorname{bil}(x, y, -z, \tau)\bigr\|$ vanishes to residual below $10^{-31}$.
2. **Literature / Repo Benchmark Gates (`E1`):**
   - **Gate A (`B1656` / `B1919`):** At $\tau = \omega = e^{2\pi i/3}$ and $(\psi_1, \psi_2) = (1/9, 0)$, independent two-dimensional Gauss–Legendre strip quadrature on `B1656`'s fundamental strip reproduces `B1919`'s closed shifted-Kronecker $c_s$ values across all four channels to residual below $10^{-13}$.
   - **Gate B (`B1667` Lamé):** Independent Frobenius power-series integration of $(\wp(z;\tau) - e_s) y = \tfrac{1}{4} y$ reproduces `B1667`'s closed anchor values at $\tau = \omega_6$ to residual below $10^{-40}$.
3. **Strip Quadrature vs Closed-Form Charge-Negation Checks:**
   - Across `23` active channel evaluations spanning torsion shifts (`(2/5, 4/5)` and `(1/9, 0)`) and irrational off-torsion shifts (`(\sqrt{2}/7, \sqrt{3}/11)`), independent contour-integral residues, strip-quadrature $c_s$, and strip-quadrature $M_w$ satisfy $(q_x, q_y) \mapsto (-q_x, -q_y)$ invariance to residuals below $10^{-33}$, $10^{-31}$, and $10^{-32}$ respectively, while matching `B1919`'s closed $c_s$ to below $10^{-14}$.
   - Closed-form $M_w(-q_x, -q_y) - M_w(q_x, q_y)$ and $Y_f(-q_x, -q_y) - Y_f(q_x, q_y)$ vanish to below $10^{-44}$ and $10^{-45}$ across both channel-weight conventions ($\sqrt{W_s} R_s$ and $R_s / \sqrt{W_s}$).
   - Negative control `PC_SCAR_2` (flipping $\theta_1(-u) \mapsto +\theta_1(u)$ on a single factor) produces an order-unity discrepancy above $1$ and fires as sealed.

---

### `E2` — Scar Duality (`W-F9`), Fox Cohomology, and `B1438` Slope Law

Across `5` levels — `(+LR, k = 2, N = 5)`, `(+LR, k = 3, N = 4)`, `(+LLR, k = 3, N = 10)`, `(-LLRLR, k = 1, N = 12)`, and `(-LLLRLR, k = 1, N = 15)` — the verifier constructed all `3052` non-split $2 \times 2$ doublet representations $V(\ell, \alpha; c_\ell)$ with `0` repo imports and computed independent Fox-calculus twisted cohomology ranks over $\mathbb{F}_p$ ($p > 10^5$ with $N \mid (p - 1)$):

1. **Exact $2 \times 2$ Intertwiner & Fox Duality (`0` mismatches in `3052` modules):**
   - For every $V(\ell, \alpha; c_\ell)$ and every generator $g \in G$, $J_2\, V(\ell, \alpha; c_\ell)^*(g)\, J_2^{-1} = V(\ell, \ell\alpha^{-1}; c_\ell)(g)$ with $J_2 = \bigl[\begin{smallmatrix} 0 & 1 \\ -1 & 0 \end{smallmatrix}\bigr]$ holds with `0` mismatches, and $I(V^*) = -I(V)$ holds across all `3052` modules (`0` mismatches vs `B1427`'s firing law).
2. **Exact General-Order `W-F9` Parameter Involution & Simultaneous Higgs Inversion (`0` asymmetric flips):**
   - Without assuming $W^2 = 1$ (tested directly on $N = 5, 10, 12, 15$ where $\operatorname{ord}(W)$ takes odd and higher even values), dualizing every $E_6$ sector module sends $(\theta, \psi_Y, W) \mapsto (\theta W^{-1}, \psi_Y^{-1}, W^{-1})$ (`0` mismatches).
   - On every one of the `120` generation-shaped firing backgrounds (`48` on `+LR` at $k = 3$, `48` on `+LLR` at $k = 3$, `8` on `-LLRLR` at $k = 1$, and `16` on `-LLLRLR` at $k = 1$; `60` with index $+1$ and `60` with index $-1$), the forced spin-$0$ Higgs partner satisfies $\eta^{(-)}(A, B) = (\eta^{(+)}(A, B))^{-1}$ with `0` mismatches and **`0` asymmetric flips** where $\psi_Y$ inverts while $\eta$ stays fixed.
3. **Orientable Slope Conjugation & Coupling Preservation (`0` mismatches):**
   - On all orientable firing levels (`96` firing backgrounds), `B1438`'s peripheral slope satisfies $s(\chi^{-1}) = s(\chi)$ (`0` mismatches) and $Y^{(-)}(A, B) = Y^{(+)}(A, B)$ (`0` mismatches).
   - Negative control `PC_SCAR_1` (testing the false naive rule $(\theta, \psi_Y, W) \mapsto (\theta, \psi_Y^{-1}, W)$ that omits $W \mapsto W^{-1}$ and $\theta \mapsto \theta W^{-1}$) fails on `120` of `120` non-$2$-torsion Higgs firing backgrounds and on `2692` of `2692` pure-hypercharge modules (`W = 1, 6\psi_Y \neq 1`), firing as sealed.

---

### `E3` — Full `GL(2, Z)` Action, Quaternion Mismatch, and Macroscopic Separation on `P_5`

1. **Mandatory Unitary Basis-Scrambling Gate:**
   - Independent random Haar $U(3)^5$ basis transformations $Y_f \mapsto U_{L,f} Y_f U_{R,f}^\dagger$ leave all extracted singular-value ratios, CKM moduli, and $J_{\mathrm{CP}}$ invariant to residual below $10^{-42}$.
2. **Exact Reflection Law Under `D` and Quaternion Mismatch:**
   - At generic bulk $\tau \notin i\mathbb{R} \cup (\tfrac{1}{2} + i\mathbb{R})$, $\tilde{L}_2(-\bar{\tau}) = \tilde{L}_2(\tau)$ holds to residual below $10^{-41}$, and $Y_f(-\bar{\tau}, \psi_1, -\psi_2; \mathcal{R}) = P_K\, \overline{Y_f(\tau, \psi_1, \psi_2; \mathcal{R})}\, P_K$ holds for both $\mathcal{R} \in \{S, \tilde{S}\}$ and both Higgs Serre weights (`DR` and `D^2 R`) to residual below $10^{-43}$.
   - The quaternion conjugation identities $\overline{\tilde{S}(\tau)} = q_j S(\tau) q_j^{-1}$ and $\overline{M_w(\tau, \psi)} = q_i M_w(-\bar{\tau}, D\psi) q_i^{-1}$ hold to exact zero and below $10^{-44}$ respectively, confirming algebraically and numerically that $q_j \neq \pm q_i$ blocks any $\mathrm{GL}(2, \mathbb{Z})$ reflection from bridging $S \leftrightarrow \tilde{S}$.
   - Negative control `PC_SCAR_4` (omitting $P_K$) fails with relative discrepancy $2$, firing as sealed.
3. **All Six `GL(2, Z)` Generators (`L`, `R`, `-I_2`, `D`, `J`, `P`) and `24`-Point `P_5` Averages:**
   - Across all six generators and both Serre weights (`DR` and `D^2 R`), every mass ratio and CKM modulus at $(\gamma \cdot \tau, w \gamma^{-1})$ matches $(\tau, w)$ within the **same** global reading ($\mathcal{W}_- \to \mathcal{W}_-$ and $\mathcal{W}_+ \to \mathcal{W}_+$) to residual below $10^{-40}$, while $J_{\mathrm{CP}}(\gamma \cdot \tau, w \gamma^{-1}) = (\det \gamma)\, J_{\mathrm{CP}}(\tau, w)$ holds to residual below $10^{-42}$.
   - Negative control `PC_SCAR_3` (comparing $J$-transformed $\mathcal{W}_-$ observables against untransformed $\mathcal{W}_+$ observables at generic $(\tau, w)$) fails with discrepancy exceeding $1/2$, firing as sealed.
   - Even after averaging over all `24` primitive order-$5$ points of $P_5$ (`B1928`'s uniform orbit), at both generic bulk $\tau$ and on the golden geodesic fixed by $J^2 = L R$, the $\mathcal{W}_-$ and $\mathcal{W}_+$ orbit means remain separated by macroscopic gaps of roughly $2/100$ to $7/100$ across both `DR` and `D^2 R` (see `p5_24point_orbit_averages` in `verify_x_scar_out.json`), confirming that weave equidistribution (`B1928`) does **not** erase the global Higgs bit `C04` / `P-847`.

---

## 4. Consequence for `P-847` and `Frame C` (`C04`)

Because no discrete symmetry in `GL(2, Z)` and no 3D scar duality flips matter's hypercharge relative to the Higgs's, the global Higgs-reading bit `C04` ($\mathcal{W}_- = (\tilde{S}, S, S)$ vs $\mathcal{W}_+ = (S, \tilde{S}, \tilde{S})$) cannot be retired as a convention or symmetry-equivalent gauge choice. Within `Frame C`, the only non-postulated mechanism that can earn `C04` is a **dynamical vacuum-energy or one-loop Coleman–Weinberg difference** $\Delta V_{\mathrm{eff}}(\mathcal{W}_- \text{ vs } \mathcal{W}_+) = -\operatorname{Tr}\ln\bigl(Y_u^\dagger Y_u + \dots\bigr)$ inside a joint action, since $\operatorname{Tr}(Y_u^\dagger Y_u)^n$ already differs between $\mathcal{W}_-$ and $\mathcal{W}_+$ on the $24$-point $P_5$ average (`E3`).

`0 of 19.`
