# Sealed Card `X-SCAR` — Testing `M21`'s Scar Lead (`W-F9`, the Tick, the Undoing, and the Hand) Against `P-847`'s Global Higgs-Reading Bit, Plus Standalone Closed-Form Verification of Matter-Charge Negation

**Seat:** `agy-exp`  
**Branch:** `agy/self-consistent-loop-2026-11-11`  
**Answering:** `M21` on `docs/seats/agy-exp.md` (`P-847`, `W-F9`, `B1438`, `B1656`, `B1662`, `B1790`, `B1879`, `B1915`, `B1919`, `B1927`, `B1928`)  
**Empirical Firewall:** `0 of 19.` Pure mathematics only; zero measured physical inputs read or compared anywhere.

---

## 1. Question Put by `M21`

`M21` notes two items on `P-847`:
1. Recomputing from `B1656`'s closed forms our algebraic identity that negating every matter charge $(q_x, q_y) \mapsto (-q_x, -q_y)$ leaves the weighted matter operator $M_w$ unchanged at every $(\tau, w)$.
2. Testing the scar lead (`W-F9`): `W-F9`'s cohomology-degree order bit ($H^1_{\mathrm{int}}(M; V)$ versus $H^2_{\mathrm{int}}(M; V) \cong H^1_{\mathrm{int}}(M; V^*)$) coincides with `P-847`'s global Higgs-reading bit between $\mathcal{W}_- = (\tilde{S}, S, S)$ and $\mathcal{W}_+ = (S, \tilde{S}, \tilde{S})$ **if and only if** a map in the record flips matter's hypercharge sign while leaving the Higgs's unflipped (or conjugates $S \leftrightarrow \tilde{S}$ without conjugating $M_w$). `M21` invites a short card with expectations committed first checking whether such a map can come from the scar duality, the tick, the undoing, or the hand — or proving cleanly that **no such map exists**.

---

## 2. Sealed Expectations (Committed Before Writing or Running `verify_x_scar.py`)

### Expectation `E1` — Exact Matter-Charge Negation Invariance in Both `B1656` Strip Quadrature and `B1919` Closed Kronecker Form
- Across multiple complex moduli $\tau \in \mathbb{H}$ and both order-five torsion points and generic irrational off-torsion shifts $(\psi_1, \psi_2)$, negating $(q_x, q_y) \mapsto (-q_x, -q_y)$ in all three sectors `up (1, -4)`, `down (1, 2)`, and `lep (-3, 6)` satisfies:
  1. $M_w(-q_x, -q_y; w, \tau) = M_w(q_x, q_y; w, \tau)$ and $Y_f(-q_x, -q_y) = Y_f(q_x, q_y)$ (in both `S` and `S~`) to residual below ten to the minus twenty-eight in `B1919` + `B1927`'s closed shifted-Kronecker formula;
  2. Direct two-dimensional subtracted Gauss–Legendre strip quadrature of `B1656`'s raw theta-bilinear kernel (`bil_mp` + `cB`, built from scratch with zero imports from `main`) agrees with `B1919`'s closed channel norms and independently confirms $M_w(-q_x, -q_y) = M_w(q_x, q_y)$ to quadrature precision (below ten to the minus twelve).

### Expectation `E2` — `W-F9` Scar Duality Flips Matter and Spin-Zero Higgs Hypercharges Simultaneously (`No Asymmetric Flip Exists in the Scar Frame`)
- In the three-manifold scar / slope frame (`B1432`, `B1434`, `B1435`, `B1438`), where a background is $(\theta, \psi_Y, W)$ with scar extension character $\ell = \theta^2 / W$, sector sub-characters $\alpha_s = \theta \psi_Y^{s_Y} W^{(s_\gamma - 1)/2}$, quotient characters $\beta_s = \alpha_s / \ell$, and $E_6$-invariant spin-zero partner character $\eta^{(\pm)}(A, B) = (\alpha_A \beta_B)^{\mp 1}$:
  1. Dualizing $V_s \mapsto V_s^* \cong V(\ell, \ell \alpha_s^{-1})$ acts on **every** background across tested cyclic levels (`(+LR, k = 2, 3)`, `(+LLR, k = 3)`, `(-LLRLR, k = 1)`) by the exact involution
     $$(\theta,\; \psi_Y,\; W,\; \ell) \longmapsto \bigl(\theta W^{-1},\; \psi_Y^{-1},\; W^{-1},\; \ell\bigr),$$
     preserving $\ell$, negating the interior index $I(V_s^*) = -I(V_s)$, inverting matter's $\psi_Y \mapsto \psi_Y^{-1}$, **and** inverting every forced spin-zero Higgs character simultaneously: $\eta^{(-)}(A, B) = (\eta^{(+)}(A, B))^{-1}$ (`zero` instances where $\psi_Y$ flips while $\eta$ stays fixed).
  2. On every orientable state tested, `B1438`'s character slope satisfies $s(\chi^{-1}) = s(\chi)$, so the normalized cubic coupling $Y(A, B) = s(\ell) - s(\eta)$ is strictly invariant under `W-F9` duality ($Y^{(-)}(A, B) = Y^{(+)}(A, B)$ with `zero` mismatches).

### Expectation `E3` — Complete `GL(2, Z)` No-Go Theorem for the Tick, the Undoing, and the Hand (`Orthogonality of SE2, W-F9, and P-847`)
- Using exact analytic $q$-series Serre derivatives (zero finite-difference error) for `B1691`'s triplet $S(\tau)$ and independent Lamé evaluation of $\tilde{L}_2(\tau)$:
  1. **Exact anti-holomorphic conjugation law:** Under the undoing / reflection generator $D = \operatorname{diag}(1, -1): (\tau, \psi_1, \psi_2) \mapsto (-\bar{\tau}, \psi_1, -\psi_2)$, **both** the Higgs slot and the matter slot are conjugated simultaneously up to $P_K = \operatorname{diag}(1, 1, -1)$:
     $$Y_f\bigl(-\bar{\tau},\, \psi_1,\, -\psi_2;\, \mathcal{R}_f\bigr) = P_K \, \overline{Y_f(\tau,\, \psi_1,\, \psi_2;\, \mathcal{R}_f)} \, P_K \qquad (\mathcal{R}_f \in \{S, \tilde{S}\}),$$
     holding to residual below ten to the minus thirty across all three sectors.
  2. **All generators preserve each world separately while $\det = -1$ moves flip $\hat{J}_{\mathrm{CP}}$:** Every generator of the full move/symmetry group — forward moves $L, R \in \mathrm{SL}(2, \mathbb{Z})$, the central turn $-I_2 = (L^{-1}R)^3$ (`B1662`), the undoing reflection $D = \operatorname{diag}(1, -1)$ (`B1662`), the golden tick $J = \bigl(\begin{smallmatrix}1 & 1 \\ 1 & 0\end{smallmatrix}\bigr)$ (`B1879`), and the swap mirror $P = \bigl(\begin{smallmatrix}0 & 1 \\ 1 & 0\end{smallmatrix}\bigr)$ (`B1915`) — preserves all singular-value ratios and $|V_{\mathrm{CKM}}|$ entries of $\mathcal{W}_-$ and of $\mathcal{W}_+$ separately (to below ten to the minus twenty-eight), while $\det = +1$ elements preserve the normalized Jarlskog invariant $\hat{J}_{\mathrm{CP}}$ and $\det = -1$ elements (`D`, `J`, `P`) negate $\hat{J}_{\mathrm{CP}} \mapsto -\hat{J}_{\mathrm{CP}}$ (to below ten to the minus twenty-eight).
  3. **Non-equivalence of $\mathcal{W}_-$ and $\mathcal{W}_+$ on `B1928`'s twenty-four-point orbit:** Averaged over all `24` points of order five in $P_5$, the outputs of $\mathcal{W}_- = (\tilde{S}, S, S)$ and $\mathcal{W}_+ = (S, \tilde{S}, \tilde{S})$ differ by an $O(1)$ gap (above one hundredth), proving that **no map in the record** exchanges or identifies `P-847`'s global bit with `W-F9`, `SE2`, `GM5b`, or `GM5c`.

---

## 3. Pre-Registered Negative Controls (`All Four Must Fire`)

1. **`PC_SCAR_1` (Un-dualized Higgs character under `W-F9`):** Keeping $\eta = \eta^{(+)}$ unflipped when replacing $V_s \mapsto V_s^*$ on backgrounds with $\psi_Y^3 \neq 1$ violates $E_6$ gauge/character invariance $\alpha_A' \beta_B' \eta = 1$ on every such background.
2. **`PC_SCAR_2` (Broken $\vartheta_1$ oddness in one factor):** Flipping the oddness sign of $\vartheta_1(-\bar{u})$ while leaving $\vartheta_1(-\delta)$ odd breaks $M_w(-q_x, -q_y) = M_w(q_x, q_y)$ by an $O(1)$ discrepancy (above one hundredth).
3. **`PC_SCAR_3` (Hypothesis that the golden tick $J$ exchanges $\mathcal{W}_- \leftrightarrow \mathcal{W}_+$):** Comparing $\mathcal{W}_-$ at $J(\tau, \psi)$ against $\mathcal{W}_+$ at $(\tau, \psi)$ fails by an $O(1)$ discrepancy (above one hundredth).
4. **`PC_SCAR_4` (Omitting $P_K = \operatorname{diag}(1, 1, -1)$ in the $D$-reflection identity):** Replacing $P_K$ by $I_3$ in $Y_f(-\bar{\tau}, \psi_1, -\psi_2) = P_K \overline{Y_f(\tau, \psi_1, \psi_2)} P_K$ fails by an $O(1)$ discrepancy (above one hundredth).

---

## 4. Planned Artifacts (Four-Commit Sealed Chain)

1. **Commit One:** `relays/cards/AGY-EXP_X-SCAR_scar-duality-tick-undoing-and-higgs-bit.md` and `relays/STATUS_AGY-EXP.md`.
2. **Commit Two:** Standalone zero-import verifier `relays/x_scar_verify/verify_x_scar.py` and `relays/x_scar_verify/SCRIPT_SHA256.txt` (sealed before execution).
3. **Commit Three:** Raw output `relays/x_scar_verify/verify_x_scar_out.json` and `relays/x_scar_verify/OUTPUT_SHA256.txt` (committed unread).
4. **Commit Four:** Closing report `relays/AGY_EXP_TO_CC_2026-11-14_X_SCAR_RESULTS.md` and updated `relays/STATUS_AGY-EXP.md`.

`0 of 19.`
