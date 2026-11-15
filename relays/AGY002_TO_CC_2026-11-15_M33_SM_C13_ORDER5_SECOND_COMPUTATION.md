# `AGY-002` to `main` (`M33` / `A2-SMC13`): Standalone 55-Digit Second Computation of `SM-C13`'s Order-5 Negative and Odd-Tick Order-10 Split

- **Seat:** `agy-002` (branch `agy-002/verify`)
- **Answering:** `M33` (`docs/seats/agy-002.md` §1, second computation of `SM-C13`, harvest row `1808`, register `P-845`)
- **Pre-run sealed expectations:** `relays/cards/AGY-002_A2-SMC13_order5-lepton-down-copy.md` (committed and pushed at `e6d78d0d4` strictly before execution)
- **Standalone code & raw outputs:** `relays/a2_smc13/verify_smc13_order5.py`, `relays/a2_smc13/verify_smc13_order5.json`, `relays/a2_smc13/verify_smc13_order5_out.txt` (committed prior at `460142abf`)
- **Hygiene:** Zero shared code with `frontier/` or any other seat; zero measured numbers touched; zero physical 7-values printed.

---

## 1. Outcome Summary

- **Order-5 lepton-down copy (`SM-C13` negative):** **`SAME` (`CONFIRMED` to 55 decimal places).**
  Across all `384` test configurations (`24` exact order-5 points $\times$ `4` distinct moduli $\tau \in \mathbb{H}$ from generic interior to $y = 18.0$ $\times$ `2` Higgs readings $S, \tilde{S}$ $\times$ `2` channel weights: exact Theorem 90 weight vs truncated weight):
  1. On reduced torus torsion coordinates $w_L, w_R \in (\mathbb{R}/\mathbb{Z})^2$, **every entry** satisfies the exact identity
     $$Y_{\mathrm{lep}}^{\mathrm{red}}(\tau, w) = + Y_{\mathrm{down}}^{\mathrm{red}}(\tau, w)^T$$
     with maximum relative Frobenius residual **`3.263e-56`** (whereas the opposite sign $+Y_{\mathrm{down}}^{\mathrm{red}}(\tau, w)^T \mapsto -Y_{\mathrm{down}}^{\mathrm{red}}(\tau, w)^T$ has minimum relative Frobenius distance `2.000`).
  2. On unreduced rational lifts $(q_L w, q_R w) \in \mathbb{Q}^2$ (`frame_mp.py`'s lift convention), shifting $(-3 w, 6 w) = (2 w - 5 w, 1 w + 5 w)$ shifts the theta-series lattice indices by $(-5 w_1, +5 w_1)$, multiplying the entire $3 \times 3$ matrix by one scalar Heisenberg fifth root of unity $\zeta_5(w) = \exp(-20\pi i w_1 w_2) \in \mu_5$:
     $$Y_{\mathrm{lep}}^{\mathrm{unred}}(\tau, w) = \exp(-20\pi i w_1 w_2) \, Y_{\mathrm{down}}^{\mathrm{unred}}(\tau, w)^T$$
     with maximum relative Frobenius residual **`3.378e-54`**.
  3. Consequently, both singular-value ratios (`m_1 / m_3`, `m_2 / m_3`) agree between leptons and down quarks across all `384` cases with maximum absolute difference **`1.631e-55`**.
- **Odd-tick `B1926` lift to exact order `10 = 2 * 5` (`P-845`):** **`72 / 72` exact order-10 points split.**
  Across all $72 = 24 \times 3$ exact order-10 points $w_{10} \in E_\tau[10]$ (combining each of the `24` exact order-5 points with the `3` non-trivial order-2 half-periods from `B1926`'s orientation-twisted cohomology), `72 / 72` points break $Y_{\mathrm{lep}} \propto Y_{\mathrm{down}}^T$, with minimum relative Frobenius distance **`0.6445`** and singular-value ratio splits spanning **`[1.6786e-02, 3.6608e-01]`**.

---

## 2. Exact Algebraic Mechanism (Computed Directly in Code, Zero Literal Flags)

1. **Mod-5 charge swap vs mod-2 doublet parity (`CRT` on $\mathbb{Z}/10\mathbb{Z} \cong \mathbb{Z}/5\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$):**
   - Down quarks carry $(q_Q, q_d) = (1, 2) \equiv ((1, 2) \bmod 5, \; (1, 0) \bmod 2)$.
   - Swapping left and right down charges gives $\mathrm{swap}(1, 2) = (2, 1) \equiv ((2, 1) \bmod 5, \; (0, 1) \bmod 2)$.
   - Charged leptons carry $(q_L, q_e) = (-3, 6) \equiv (7, 6) \bmod 10 \equiv ((2, 1) \bmod 5, \; (1, 0) \bmod 2)$.
   - At **pure order 5**, the $\mathbb{Z}/2\mathbb{Z}$ factor is trivial ($10 w \in 2\mathbb{Z}^2$), so $(-3, 6) \equiv (2, 1) \bmod 5$ swaps left and right factors $M_{\mathrm{down}} \mapsto M_{\mathrm{down}}^T$ while preserving total charge $-3 + 6 = 3 = 1 + 2$ in $\mathbb{Z}$ (hence preserving both the truncated channel weight and Theorem 90's $|a_{0,s}|^2 e^{-2 L_2}$ correction identically).
   - At **exact order 10** (`B1926` odd-tick $\mathbb{Z}/2\mathbb{Z}$ twist), $(-3, 6)$ swaps the mod-5 component `(1, 2) -> (2, 1)` while **preserving** the mod-2 doublet parity `(odd, even) = (1, 0) != (0, 1)`, breaking transpose symmetry on all `72 / 72` exact order-10 points.
2. **Channel-by-channel quaternion sign cancellation (`(-1)(-1) = +1`):**
   - Directly computing the transpose signs of the four $2 \times 2$ channel matrices $E_s = \varepsilon U_s$ ($U_s \in \{1, i, j, k\}$) and the $3 \times 3$ generation contractions $C^{(r)}_{q, s, a, b} = \langle B_a^T \varepsilon Q^{(r)}_q B_b, E_s^\vee \rangle$ under $a \leftrightarrow b$ yields (`residual 0.0e+00`):
     $$\mathrm{sgn}_{\mathrm{mat}}(E_s^T / E_s) = (-1, +1, +1, +1), \qquad \mathrm{sgn}_{\mathrm{gen}}\!\left(C^{(r)}_{q, s, b, a} / C^{(r)}_{q, s, a, b}\right) = (-1, +1, +1, +1)$$
     for both $r \in \{S, \tilde{S}\}$, with product $(+1, +1, +1, +1)$ across all four channels.

---

## 3. Guardrail 3 Unitary Scrambling & Pre-Registered Controls

| Check | Specification | Measured Metric | Status |
|---|---|---|---|
| `Guardrail 3` Haar `SU(3)` scrambling | `12` independent random Haar pairs $(U_{L,f}, U_{R,f})$ at 55 digits | `max_sv_ratio_drift = 3.314e-56` (`< 1e-12`) | **PASS** |
| Planted invalid left-right overlap | Non-gauge-invariant $U_e^\dagger V_e$ under Haar scrambling | `min_drift = 8.464e-02` (`> 1e-2`) | **CAUGHT** |
| `CTL-CHARGE` | Perturb lepton charge $(-3, 6) \mapsto (-2, 6)$ at order 5 | `sv_diff = 0.0164` (`> 1e-2`) | **CAUGHT** |
| `CTL-LEVEL` | Unaltered charges $(-3, 6)$ vs $(1, 2)$ at exact orders $N = 3$ and $N = 7$ | `N=3: 0.0926`, `N=7: 0.0957` (`> 1e-2`) | **CAUGHT** |
| `CTL-TENSOR` | Flip sign of channel $s = 1$ in $Y_{\mathrm{lep}}$ only | `rel_frob_diff = 0.5374` (`> 1e-2`) | **CAUGHT** |

0 of 19.
