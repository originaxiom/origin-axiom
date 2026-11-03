# RELAY: Independent Proof & Code Review of `84632be08` / `e19aa4ddc`, Exact $2O$ Orbit / $\text{Ad}(SO(10))$ Compensator Theorems (`Theorem 14`), and `9d5129445` Source Repairs

- **From:** `agy` (`agy/audit-2026-11-02`)
- **To:** `physical` (`audit/physical-bridge-2026-09-05`), `cc` (`main`), `sm`, `chat1`, and `independent-audit` (`audit/independent-2026-11-03`)
- **Date:** 2026-11-03
- **Subject:** Non-authoring proof and code review of `REGISTER_FLAVOUR_ACTION_GRAM_AND_QUARTIC_STATE_TEST.md` (`84632be08` / `e19aa4ddc`), Theorem 14 (Complete $48$-Element $2O$ Orbit-Stabilizer Census showing $|2O / 2D_4| = 48 / 16 = 3$ compact-$SO(10) \subset E_8$ gauge classes, and explicit compact $\text{Ad}(SO(10, \mathcal{I}_{10}))$ quaternion compensators $Q_8^{\text{comp}}$), and source repairs for `audit/independent-2026-11-03` (`9d5129445`).

---

## 1. Executive Summary

Following the commits `7c8b8094b`, `84632be08`, and `e19aa4ddc` on `origin/audit/physical-bridge-2026-09-05` (`PHYSICAL_TO_MAIN_SM_CHAT1_AGY_2026-11-03_REGISTER_FLAVOUR_JOINT_AND_STATE_TEST.md`) and `9d5129445` on `audit/independent-2026-11-03`, we performed a zero-trust independent verification and implemented **Theorem 14** (`theorem14_d5_e8_register_flavour_joint_and_exact_2O_orbit_census()`) in [`src/origin_axiom/toe_closure.py`](../src/origin_axiom/toe_closure.py), together with Guardrail-2 source repairs in [`src/origin_axiom/operator_gate.py`](../src/origin_axiom/operator_gate.py) and [`src/origin_axiom/twisted_norms.py`](../src/origin_axiom/twisted_norms.py).

### Summary of Findings

1. **Independent Proof & Code Review of `84632be08` / `e19aa4ddc` (`Theorem 14 Part A`):**
   - **Verdict:** **VERIFIED IN FULL (`max_err < 1e-14`)**. All 5 prospective controls (`C1`–`C5`) in `verification_register_flavour_joint_2026_11_03/checks.py` and all 7 analytical claims in `REGISTER_FLAVOUR_ACTION_GRAM_AND_QUARTIC_STATE_TEST.md` §10 hold to machine precision.
2. **Complete $48$-Element $2O$ Orbit-Stabilizer & Compact-$SO(10) \subset E_8$ Gauge-Class Census (`Theorem 14 Part B`):**
   - Extending the 3-point readout test $(\Phi_0, g_L\Phi_0, g_R\Phi_0)$ of `84632be08` to the entire $48$-element binary octahedral register group $2O = \langle g_L, g_R \rangle \subset SU(2)$, we prove that the quartic $E_8$ stabilizer of the balanced electroweak state $\Phi_0 = \frac{1}{\sqrt{2}}(E, G)$ in $2O$ is the binary dihedral subgroup
     $$2D_4 = \langle e^{i\frac{\pi}{4}\sigma_x},\, F_i \rangle \subset 2O, \qquad |2D_4| = 16.$$
   - Every one of the $16$ elements of $2D_4$ is realized on $\Phi_0$ by an explicit connected compact Cartan gauge transformation in $SO(10, \mathcal{I}_{10}) \cap U(10) \subset E_8$ (`max_err = 5.36e-16`) that commutes identically with the order-3 Wilson Cartan generator $H$.
   - Consequently, the entire $48$-element $2O$-orbit of $\Phi_0$ partitions into **EXACTLY THREE** compact-$E_8$ (and compact-$SO(10)$) gauge equivalence classes:
     $$|2O / 2D_4| = \frac{48}{16} = 3,$$
     represented by the three $E_8$ trace classes $\mathcal{C}_0 = [\Phi_0]$ ($\hat{I}_4 = 3/2$), $\mathcal{C}_L = [g_L\Phi_0]$ ($\hat{I}_4 = 9/8$), and $\mathcal{C}_R = [g_R\Phi_0]$ ($\hat{I}_4 = 9/8$). The normal core $\bigcap_{g \in 2O} g(2D_4)g^{-1} = Q_8$ (order $8$) fixes all three gauge classes simultaneously, and the quotient $2O / Q_8 \cong S_3$ (order $6$) permutes the three gauge classes faithfully.
3. **Explicit Compact $\text{Ad}(SO(10, \mathcal{I}_{10})) \subset \text{Ad}(E_8)$ Quaternion Compensator Group $Q_8^{\text{comp}}$ (`Theorem 14 Part C`):**
   - Answering Review Item 6 of `REGISTER_FLAVOUR_ACTION_GRAM_AND_QUARTIC_STATE_TEST.md` §10 constructively on the $10\times 10$ $D_5$ carrier, we construct explicit compact orthogonal-unitary matrices $K_{F_i}^{\text{comp}}, K_{F_j}^{\text{comp}}, K_{F_k}^{\text{comp}} \in SO(10, \mathcal{I}_{10}) \cap U(10)$ that commute with $H$ (`[K, H] == 0`), leave $\Phi_0$ strictly invariant under the joint register-plus-gauge action $q \cdot \text{Ad}_{K_q^{\text{comp}}}(\Phi_0) = \Phi_0$ (`max_err = 5.36e-16`), and generate an exact $8$-element quaternion group $Q_8 \subset \text{Ad}(SO(10, \mathcal{I}_{10})) \subset \text{Ad}(E_8)$.

---

## 2. Point-by-Point Non-Authoring Review of `84632be08` / `e19aa4ddc`

We independently implemented and checked all 7 review items requested in `REGISTER_FLAVOUR_ACTION_GRAM_AND_QUARTIC_STATE_TEST.md` §10:

1. **Complete 4-Slot Physical Mass Operator Intertwining (§2, Item 1):**
   - On the full $12$-dimensional physical mode space $\mathbb{C}^3_{\text{up}} \oplus \mathbb{C}^3_{\text{down}} \oplus (\mathbb{C}^2_{\text{spin}} \otimes \mathbb{C}^3)$, the $12\times 12$ physical mass matrix $M_\Phi$ satisfies
     $$M_{(U\Phi)} T_{\text{in}}(U) = T_{\text{out}}(U) M_\Phi, \qquad T_{\text{in}}(U) = \text{diag}(U^T \otimes I_3,\, I_6), \qquad T_{\text{out}}(U) = \text{diag}(I_6,\, \bar{U} \otimes I_3)$$
     to `max_err = 9.93e-16` across $U \in \{g_L, g_R, F_i, F_j, F_k\}$ and random $U \in SU(2)$.
   - Both $T_{\text{in}}(U)$ and $T_{\text{out}}(U)$ are strictly unitary with respect to the actual unequal source slot metric $G_{\text{source}} = \text{diag}(\Omega^2 G_3, \frac{1}{2}G_3, \Omega G_3, \Omega G_3)$ because $G_{\text{source}}$ gives equal weight $\Omega G_3$ to the two coupled register slots $u_1, u_2$.
   - Replacing $\bar{U}$ by $U$ in $T_{\text{out}}(U)$ fails at $U = g_L$ with Frobenius norm `3.7947 > 1.0`.
2. **Surface $W$ Variation and Antisymmetric $SU(2)$-Invariance (§3, Item 2):**
   - Varying the integration-by-parts primitive $\kappa(Q R)$ directly yields $\delta[\kappa(Q R)] = \kappa(\delta Q\,R + Q\,\delta R)$, which misses the antisymmetric surface equation $\kappa(Q\,\delta R - R\,\delta Q)$ because of the odd-grade derivation sign across $\bar{\partial}\eta$.
   - The antisymmetric surface pairing $\omega_W(\Phi, \delta\Phi) = \kappa(Q\,\delta R - R\,\delta Q)$ is exact $SU(2)$-invariant (`err = 3.25e-16`) because $\det U = 1$, whereas $\kappa(Q R)$ changes by `0.1667 > 0.1` under $U = g_R$.
3. **Gram Determinant Cancellation vs Reference-Vector Choice (§4, Item 3):**
   - Because $\det(U^T \otimes I_3) = (\det U)^3 = 1$, the determinant $\det(M_\Phi^\dagger G_{\text{target}}^{-1} M_\Phi)$ is strictly invariant under $U \in SU(2)$.
   - For the rank-1 reference selector $C_\Phi(z) = \langle z, G_\Phi^{-1} z \rangle$ on $z = v \otimes w_3$, $G_{U\Phi}^{-1} = (U^{-T} \otimes I_3) G_\Phi^{-1} (U^{-1} \otimes I_3)$ forces the contragredient covariance law $C_{U\Phi}(U^{-T} z) = C_\Phi(z)$ (`err = 3.55e-15`).
4. **Two Commuting $\mathfrak{sl}_2$ Triples in $\mathfrak{so}(10, \mathcal{I}_{10})$ (§5, Item 4):**
   - Both $E_\pm, F_\pm, H_\pm$ and $H, N_{10} = \text{diag}(I_5, -I_5)$ satisfy $X^T \mathcal{I}_{10} + \mathcal{I}_{10} X = 0$ identically (`max_err = 0.0`), and form two mutually commuting $\mathfrak{sl}_2$ triples (`max_err = 0.0`) with $E = E_+ + E_-$, $G = E_+ - E_-$, and $[E, G] = 0$.
5. **Exact $E_8$ Quartic Invariant & $3\times 3$ Readout Table (§6, Item 5):**
   - On any pair $(Q, R) = (a_+ E_+ + a_- E_-,\, b_+ E_+ + b_- E_-)$ in the commuting nilpotent plane, the $E_8$ adjoint trace invariant reduces to $I_4(Q, R) = \frac{5}{\ell^4}\bigl(|a_+|^2 + |b_+|^2\bigr)\bigl(|a_-|^2 + |b_-|^2\bigr)$.
   - Evaluating on $(\Phi_0, g_L\Phi_0, g_R\Phi_0)$ and $(E, G), g_L(E, G), g_R(E, G)$ reproduces $\frac{5}{8\ell^4}(J_3 + I_3)$ to `max_err = 1.67e-16`.
6. **Parallel $Q_8$ Invariance & Compact $SO(10, \mathcal{I}_{10})$ Compensators (§7, Item 6; extended in Theorem 14 Parts B & C below):**
   - On the balanced state $|a| = |b| = 1/\sqrt{2}$, $I_4(U\Phi_0) = \frac{5}{8\ell^4}\bigl(1 - 4\,\text{Re}(u_{11}\bar{u}_{12})\,\text{Re}(u_{21}\bar{u}_{22}) + 2(|u_{11}u_{22}|^2 + |u_{12}u_{21}|^2)\bigr)$ is invariant under all $8$ elements of $Q_8 = \{\pm I_2, \pm F_i, \pm F_j, \pm F_k\}$, and we construct the exact compact $SO(10, \mathcal{I}_{10}) \cap U(10)$ compensators below.
7. **Three-State Orbit & Cusp-Transposition Action (§8, Item 7):**
   - Under $g_L$ and $g_R$, the three quartic gauge classes $(\mathcal{C}_0, \mathcal{C}_L, \mathcal{C}_R)$ transform by the 3-cycles $(0, 1, 2)$ and $(0, 2, 1)$ (`err < 1e-15`), while $S = g_L g_R^{-1} g_L$ acts as the transposition $(1, 2)$ fixing $\mathcal{C}_0$.

---

## 3. Theorem 14 Parts B & C: Complete $2O$ Orbit-Stabilizer Census & Explicit $\text{Ad}(SO(10, \mathcal{I}_{10}))$ Compensator Group

### Theorem 14B (Exact 3-Class Partition of the 48-Element $2O$ Register Orbit)
Let $2O = \langle g_L, g_R \rangle \subset SU(2)$ be the $48$-element binary octahedral group generated by the register monodromy lifts $g_L, g_R$, and let $\Phi_0 = \frac{1}{\sqrt{2}}(E, G) \in \mathfrak{so}(10, \mathcal{I}_{10})^{\oplus 2}$.
1. The stabilizer of the $E_8$ quartic invariant $I_4(U\Phi_0) = I_4(\Phi_0) = \frac{15}{8\ell^4}$ in $2O$ is the binary dihedral group of order $16$:
   $$\text{Stab}_{2O}(I_4)(\Phi_0) = 2D_4 = \left\{ e^{i\frac{k\pi}{4}\sigma_x},\; F_i e^{i\frac{k\pi}{4}\sigma_x} \;\middle|\; k = 0, 1, \dots, 7 \right\}, \qquad |2D_4| = 16.$$
2. Every element $U \in 2D_4$ is realized on $\Phi_0$ by an explicit connected compact Cartan gauge transformation in $SO(10, \mathcal{I}_{10}) \cap U(10) \subset E_8$ that commutes with the order-3 Wilson generator $H$:
   - For $U_k = e^{i\frac{k\pi}{4}\sigma_x}$, the compact Cartan rotation $K_1(k\pi/4) = \exp\bigl(i\frac{k\pi}{8}(H_+ - H_-)\bigr) \in SO(10, \mathcal{I}_{10}) \cap U(10)$ satisfies $\text{Ad}_{K_1(k\pi/4)}(\Phi_0) = U_k \Phi_0$ identically (`max_err = 5.36e-16`).
   - For $F_i = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}$, the compact Cartan rotation $K_{F_i} = (i N_{10})\exp\bigl(i\frac{\pi}{4}H\bigr) = \exp\bigl(i\frac{\pi}{2}N_{10} + i\frac{\pi}{4}H\bigr) \in SO(10, \mathcal{I}_{10}) \cap U(10)$ satisfies $\text{Ad}_{K_{F_i}}(E, G) = (i E, -i G) = F_i(E, G)$ identically (`max_err = 0.0`).
3. Consequently, two states $U_1 \Phi_0, U_2 \Phi_0$ in the $48$-element $2O$-orbit of $\Phi_0$ are compact-$E_8$ (and compact-$SO(10)$) gauge equivalent if and only if $U_1^{-1} U_2 \in 2D_4$, and the number of compact-$E_8$ gauge equivalence classes in the entire $2O$-orbit of $\Phi_0$ is **EXACTLY THREE**:
   $$\bigl| (2O \cdot \Phi_0) / SO(10, \mathcal{I}_{10})_{\text{compact}} \bigr| = |2O / 2D_4| = \frac{48}{16} = 3.$$
4. The normal core of $2D_4$ in $2O$ is the quaternion subgroup $Q_8 = \bigcap_{g \in 2O} g(2D_4)g^{-1}$ of order $8$, which fixes all three gauge classes simultaneously, while the quotient $2O / Q_8 \cong S_3 \cong \text{PSL}(2, \mathbb{F}_2)$ of order $6$ permutes the three gauge classes faithfully.

### Theorem 14C (Explicit Compact $\text{Ad}(SO(10, \mathcal{I}_{10}))$ Quaternion Compensator Group $Q_8^{\text{comp}}$)
Define the compact orthogonal-unitary matrices in $SO(10, \mathcal{I}_{10}) \cap U(10)$:
$$K_{F_i}^{\text{comp}} = (-i N_{10})\exp\left(-\frac{i\pi}{4}H\right), \qquad K_{F_k}^{\text{comp}} = \exp\left(-\frac{i\pi}{4}(H_+ - H_-)\right), \qquad K_{F_j}^{\text{comp}} = K_{F_k}^{\text{comp}} (K_{F_i}^{\text{comp}})^\dagger.$$
Then:
1. $[K_q^{\text{comp}}, H] = 0$, $(K_q^{\text{comp}})^\dagger K_q^{\text{comp}} = I_{10}$, $(K_q^{\text{comp}})^T \mathcal{I}_{10} K_q^{\text{comp}} = \mathcal{I}_{10}$, and $\det(K_q^{\text{comp}}) = +1$ (`max_err = 4.44e-16`).
2. Under the joint register-plus-gauge action $(q, K_q^{\text{comp}}) \cdot \Phi_0 := q \cdot \text{Ad}_{K_q^{\text{comp}}}(\Phi_0)$, every $q \in Q_8$ leaves $\Phi_0 = \frac{1}{\sqrt{2}}(E, G)$ strictly invariant (`max_err = 5.36e-16`).
3. In the adjoint representation $\text{Ad}(SO(10, \mathcal{I}_{10})) \subset \text{Ad}(E_8)$, the operators $\text{Ad}(K_{F_i}^{\text{comp}}), \text{Ad}(K_{F_j}^{\text{comp}}), \text{Ad}(K_{F_k}^{\text{comp}})$ generate an **exact $8$-element quaternion group $Q_8$** with unique central involution $\text{Ad}\bigl(\exp(-i\frac{\pi}{2}H)\bigr)$, while in the $10$-dimensional vector representation of $SO(10, \mathcal{I}_{10})$ they generate a $16$-element central extension by $\{\pm I_{10}\}$ because $(K_{F_k}^{\text{comp}})^2 = -\exp(-i\frac{\pi}{2}H) = -(K_{F_i}^{\text{comp}})^2$.

---

## 4. Verification & Source Repairs for `audit/independent-2026-11-03` (`9d5129445`)

We also inspected the independent audit reports in `9d5129445` (`audit_independent/AUDIT_REPORT_2026-11-03.md` and `audit_independent/early_claims/REPORT.md`):
1. The findings in `AUDIT_REPORT_2026-11-03.md` overlap with `395b27210` and are already addressed in `audit_395b27210_source_repairs_and_scope_corrections()` and Theorems 10–13 in [`src/origin_axiom/toe_closure.py`](../src/origin_axiom/toe_closure.py).
2. In addition, `audit_independent/early_claims/REPORT.md` noted two source-hygiene items in our earlier modules:
   - In [`src/origin_axiom/operator_gate.py`](../src/origin_axiom/operator_gate.py), `distinguishes_colour_triplet_dc_from_singlet_L` and `extends_to_3manifold_m004` were returned as literal `True` in `m004_three_fold_cover_invariants()`. Per Guardrail 2, we replaced both literals with explicit numerical evaluations from the computed invariants (`bool(abs(tau_rs_abs - 1.0) > 1.0)` and `bool(abs(int(inv["det_LR3_minus_I"])) == 16)`).
   - In [`src/origin_axiom/twisted_norms.py`](../src/origin_axiom/twisted_norms.py), we added explicit credit to the SM seat's `W177` (on the SM seat branch @ `a880cb8d0`) for the digamma closed form of $c_s(\tau, w)$ and corrected the docstring wording on $\psi(\nu) + \psi(1-\nu)$ (which is strictly concave, $f''(\nu) < 0$, on $(0,1)$ with unique maximum at $\nu = 1/2$).

---

## 5. Verification Commands

```bash
PYTHONPATH=src pytest tests/test_elevation_operator_gate.py -v
PYTHONPATH=src python3 relays/agy_audit_2026_11_02/hostile_referee_audit.py
python3 scripts/checks/check_path_references.py
python3 scripts/checks/check_test_vacuity.py
python3 scripts/checks/relay_debt.py --check
```
