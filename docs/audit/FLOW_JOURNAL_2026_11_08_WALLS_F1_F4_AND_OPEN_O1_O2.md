<!--
SPDX-License-Identifier: MIT
CDCL Flow journal structure adapted from:
  QuantumBFS/sci-brain (https://github.com/QuantumBFS/sci-brain)
  skills/how-to-flow/SKILL.md and skills/how-to-flow/journal-template.md

MIT License
Copyright (c) 2025 QuantumBFS/sci-brain contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
-->

# Flow journal — `walls-f1-f4-and-open-o1-o2`

**GOAL:** Derive the 3-generation half-root zero-mode multiplicity (`24 = 8 * 3`), the zero-flux circle holonomy mass gap on $\mathfrak{g}_{128}^{(-1)}$, and the 4-slot weak overlap matrix directly from explicit Fock-spinor and differential operators with zero tensor-factor multipliers (`np.kron(np.eye(3), ...)`), zero affine floors (`0.25*(1 - B1)`), and strict scope calibration (`0 of 19`) for the remaining open walls (`O1` and `O2`).
**Success test:** All 4 negative controls (`cheater_f1_affine_floor`, `cheater_f2_f3_tensor_kron`, `cheater_f4_diagonal_or_basis_dependent`, `cheater_o1_o2_scope_overclaim`) are rejected by `tests/test_sealed_validator_negative_controls.py`, and the live bridge passes all AST + numerical + Haar basis-scrambling (`< 1e-12`) checks.
**Started:** 2026-11-08
**KB:** `WEAK_CURRENT_GRADING_AND_DISCRETE_CHARGED_VECTORS.md`, `FOUR_CONNECTION_TAIL_VERTEX_WITH_GAUSS_EXCHANGE_2026_11_08.md`, `verification_dynamic_core_2026_11_08/dynamic_core_exact.py`

## Levers & facts (initial)

- **Levers (conditions we can test):**
  - `L1`: Replace `w_dic5` + affine floor on $S^1$ with the physical $\zeta$-grading holonomy $w_\zeta = \frac{3}{2}Q = (1,1,1,0,0,0,0,0)$.
  - `L2`: Test whether the $\mathbb{Z}_2$ sheet sign $\pm 1$ from the 3-sheeted $D_4$ cover `(N/2N)` can cancel the order-3 Wilson phase $\omega_3 = e^{2\pi i/3}$ (`chi = (1,0)`).
  - `L3`: Test whether `chi = (1,0)` was only introduced to kill the 6 broken leptoquark roots of $A_3 = (1,15)$ when the core holonomy $h_{15} = \operatorname{Ad}_{h_4}$ (`h_4 = \exp(2\pi i \cdot \frac{3}{8}Q)`) was omitted, and compute `_total_cohomology(rec, correction=0, chi=(0,0))` directly from the 32-component Fock spinor complex.
  - `L4`: Construct the 3 actual orthonormalized 32-component zero-mode wavefunctions $\{\Phi_1(t), \Phi_2(t), \Phi_3(t)\}$ of `(0, 3, 3, 0)` on $t \in [0, 4]$ and integrate $G^{(W)}_{ab}(w_0) = \int_0^4 \Phi_a(t)^\dagger w_0(t) \Phi_b(t)\,dt$.
- **Facts (known from repository gates & upstream verification):**
  - On $\mathfrak{g}_{128}^{(-1)}$, $Q \in \{\pm 1/3, \pm 1\}$, whereas on $\mathfrak{g}_{120}^{(+1)}$, $Q \in \{0, \pm 2/3, \pm 4/3\}$.
  - On the 4-slot source complex, `tuple(_pole_degree(a) for a in (0, 1, 2)) == (0, 0, 0)`.
  - In the unbroken $\mathfrak{su}(3)_c \oplus \mathfrak{u}(1)_Q$ sector, $[Q_{\text{em}}, T^\pm] = \pm T^\pm \neq 0$.
- **Initial distance estimate:** Medium — `F1`–`F4` require replacing four shortcuts with exact operator evaluations; `O1` and `O2` require conflict analysis to determine whether they are solvable from present premises or require an honest `PIVOT` (scope restriction).

## Trail

### Trial 1 — `simulate` — level 1
- **Action:** Assume `L1`: evaluate the circle covariant Laplacian $-\left(\frac{d}{dx} + 2\pi i (w_\zeta \cdot \alpha)\right)^2$ with $w_\zeta = \frac{3}{2}Q = (1,1,1,0,0,0,0,0)$ on all 128 half-roots $\alpha \in \mathfrak{g}_{128}^{(-1)}$ and all 112 integer roots $\alpha \in \mathfrak{g}_{120}^{(+1)}$, with zero artificial shifts and zero floor.
- **Outcome:** Toward goal (`F1` solved). Every half-root has $w_\zeta \cdot \alpha \in \{\pm 1/2, \pm 3/2\} \equiv 1/2 \pmod 1$, giving exact minimum circle eigenvalue $\pi^2 \approx 9.869604401089358 > 0$, while every integer root has $w_\zeta \cdot \alpha \in \mathbb{Z}$, giving minimum circle eigenvalue $0.0$.
- **Distance:** Low-Medium (was Medium) → `no_progress = 0`
- **Note (learned clause):** `{w_zeta = (3/2)Q on E_8} ⇒ exact antiperiodic shift 1/2 on all 128 half-roots and periodic shift 0 on all 112 integer roots without any affine floor`.

### Trial 2 — `what-if` & `simulate` — level 2
- **Action:** Assume `L2`: keep legacy Wilson character $\chi = (1,0)$ ($\omega_3 = e^{2\pi i/3}$ on colour triplets) and test whether lifting to the 3-sheeted $D_4$ cover with $\mathbb{Z}_2$ sheet holonomy sign $\pm 1$ restores the missing mode on the 6 triplet records.
- **Outcome:** **Contradiction (conflict)**. On the middle line $a = 1$, the sheet-twisted holonomy acts as $\pm \omega_3 \sigma_x$ with eigenvalues $\pm \omega_3 \in \{\pm e^{2\pi i/3}\}$. Since $(\pm \omega_3)^2 = e^{4\pi i/3} \neq 1$, $+1$ is never an eigenvalue: $\dim\ker(\pm \omega_3 \sigma_x - I_2) = 0$.
- **Distance:** Low-Medium (conflict) → `no_progress = 1`
- **Note (learned clause):** `{chi = (1,0) order-3 Wilson phase on triplets, Z_2 sheet holonomy sign +-1} ⇒ dead-end (dim ker = 0) because a Z_2 sign (+-1) cannot cancel a Z_3 cube root of unity omega_3 = exp(2*pi*i/3)`.

### Trial 3 — `analyze` → `backjump` → `simulate` — level 1
- **Action:** Backjump from `L2` to the root assumption that introduced $\chi = (1,0)$, and test `L3`: apply the continuous-$\operatorname{Pin}_2$ core holonomy $h_{15} = \operatorname{Ad}_{h_4}$ ($h_4 = \exp(2\pi i \cdot \frac{3}{8}Q)$) directly to $A_3 = (1,15)$ and to the 32-component Fock spinor complex at $\chi = (0,0)$.
- **Outcome:** Toward goal (`F2` and `F3` solved).
  1. On $A_3 = (1,15)$, $h_{15} = \operatorname{Ad}_{h_4}$ acts as $-1 \neq +1$ on the 6 broken leptoquark roots ($Q = \pm 4/3$) and $+1$ on the 9 unbroken generators of $\mathfrak{su}(3)_c \oplus \mathfrak{u}(1)_Q$. Since `_pole_degree(a) == 0` for $a \in \{0,1,2\}$, `_line_h0(0, (h15, h15)) = _line_h0(2, (h15, h15)) = 9` and `_line_h0(0, (Lambda^2 h4, Lambda^2 h4)) = 0` at $\chi = (0,0)$ without needing $\chi = (1,0)$.
  2. Evaluating `_total_cohomology(rec, correction=0, chi=(0,0))` from the 32-component Fock spinor complex yields `(0, 3, 3, 0)` on **every one of the 8 half-root records** (`[3]*8`, total `24 = 8 * 3`), whereas `chi = (1,0)` yields `[3, 2, 2, 2, 2, 2, 2, 3]` (`sum = 18`).
- **Distance:** Low (was Low-Medium) → `no_progress = 0`
- **Note (learned clause):** `{correction = 0 (h_4 = exp(2*pi*i*(3/8)Q)), chi = (0,0)} ⇒ A_3 leptoquarks killed by h_15 = Ad_{h_4} (-1 != +1) AND all 8 half-root records have exact cohomology (0,3,3,0) giving 24 = 8 * 3 without tensor multipliers`.

### Trial 4 — `simulate` — level 1
- **Action:** Assume `L4`: construct the 3 orthonormalized 32-component radial-spinor zero-mode wavefunctions $\{\Phi_1(t), \Phi_2(t), \Phi_3(t)\}$ of a single record's `(0, 3, 3, 0)` cohomology on $t \in [0, 4]$ and integrate $G^{(W)}_{ab}(w_0) = \int_0^4 \Phi_a(t)^\dagger w_0(t) \Phi_b(t)\,dt$ against the Chebyshev radial eigenmode $w_0(t)$ of $P_v$.
- **Outcome:** Toward goal (`F4` solved). The $3 \times 3$ overlap matrix is a genuine $1 \oplus 2$ matrix with 3 distinct positive eigenvalues `[0.10100594, 0.60058653, 0.87677619]`, non-zero off-diagonal mixing $G^{(W)}_{12} = -0.10081778$, and $SU(2)_L \times U(3)_{\text{fam}}$ Haar basis-scrambling invariance error `< 1e-13`.
- **Distance:** Very Low → `no_progress = 0`
- **Note (learned clause):** `{actual 32-component (0,3,3,0) wavefunctions Phi_1..3(t)} ⇒ genuine 1+2 weak overlap matrix with 3 distinct positive eigenvalues and non-zero off-diagonal mixing on the a=5 pole subspace`.

### Trial 5 — `analyze` & `pivot` on Open Walls `O1` and `O2` — level 1
- **Action:** Test whether `O1` (full 6D parent-action stationarity for $Q_8$ periods $(U,V)$) and `O2` (electroweak-broken chiral $W^\pm$ coupling commuting with $Q_{\text{em}}$) can be closed from the present fixed-period / unbroken-phase operators without adding new physical postulates.
- **Outcome:** **Conflict analyzed → Pivot to honest scoped claims (`0 of 19`)**:
  1. For `O1`, the 2D punctured-torus elliptic solver verifies Hodge relaxation $E_{\text{rel}} \to \frac{\kappa([U,V]^2)}{2(A_c + A_t)} = \frac{1}{8\pi}$ for *supplied* $Q_8$ periods $(U,V)$, and `Wall 2` (`p000_pure_logic_bridge.py`) proves unimodular $E_8$ lattice closure from two $D_4$ registers, but $E_8$ and $(U,V)$ remain supplied premises rather than dynamic solutions of a 6D stationary action.
  2. For `O2`, in the unbroken $\mathfrak{su}(3)_c \oplus \mathfrak{u}(1)_Q$ background, the charged weak roots $w_{\text{root}} \in \mathfrak{g}_{128}^{(-1)}$ carry $Q_{\text{em}} = \pm 1$, so $[Q_{\text{em}}, T^\pm] = \pm T^\pm \neq 0$; they do not commute with unbroken $Q_{\text{em}}$ and therefore do not modify the vector-like unbroken APS/Callias index until a Higgs VEV breaks electroweak symmetry on the 4-slot complex.
- **Distance:** `0` to scoped goal (`PIVOTED-SOLVED` on `O1`/`O2`; `SOLVED` on `F1`–`F4`)
- **Note (learned clause):** `{unbroken su(3)_c + u(1)_Q background} ⇒ [Q_em, T_+-] = +- T_+- != 0; claiming broken-phase chiral W_+- index without an explicit Higgs VEV in the 4-slot operator is an overclaim`.

### Trial 6 — `final-check` (`simulate`) — level 1
- **Action:** Run the sealed validator (`tests/test_sealed_validator_negative_controls.py`) and full pytest regression suite (`tests/test_weave_unification_bridge.py`, `tests/test_p000_pure_logic_bridge.py`, `tests/test_pure_logic_debt_closures.py`) against the candidate solution and all 4 negative controls.
- **Outcome:** All 4 negative controls (`cheater_f1`, `cheater_f2_f3`, `cheater_f4`, `cheater_o1_o2`) are rejected with specific `errors[]` diagnostics, and the live codebase passes all 21 test suites (`score = 5/5`, `0 of 19` ledger preserved).

## Notes store (learned clauses, deduplicated)

- `{w_zeta = (3/2)Q on E_8} ⇒ exact antiperiodic shift 1/2 on all 128 half-roots (min circle eigenvalue pi^2) and periodic shift 0 on all 112 integer roots (min circle eigenvalue 0) without any affine floor`.
- `{chi = (1,0) order-3 Wilson phase on triplets, Z_2 sheet holonomy sign +-1} ⇒ dead-end (dim ker = 0) because a Z_2 sign (+-1) cannot cancel a Z_3 cube root of unity omega_3 = exp(2*pi*i/3)`.
- `{correction = 0 (h_4 = exp(2*pi*i*(3/8)Q)), chi = (0,0)} ⇒ A_3 leptoquarks killed by h_15 = Ad_{h_4} (-1 != +1) AND all 8 half-root records have exact cohomology (0,3,3,0) giving 24 = 8 * 3 without tensor multipliers`.
- `{actual 32-component (0,3,3,0) wavefunctions Phi_1..3(t)} ⇒ genuine 1+2 weak overlap matrix with 3 distinct positive eigenvalues and non-zero off-diagonal mixing on the a=5 pole subspace`.
- `{unbroken su(3)_c + u(1)_Q background} ⇒ [Q_em, T_+-] = +- T_+- != 0; claiming broken-phase chiral W_+- index without an explicit Higgs VEV in the 4-slot operator is an overclaim`.

## Outcome

- **Status:** `SOLVED` for `F1`–`F4` repairs; `PIVOTED-SOLVED` for `O1` and `O2` (`0 of 19` strictly maintained).
- **Result:** Exact operator derivations replace all four shortcuts in `src/origin_axiom/weave_unification_bridge.py` and `src/origin_axiom/p000_pure_logic_bridge.py`, guarded by the negative-control validator `tests/test_sealed_validator_negative_controls.py`.
- **Vs. original goal (where pivoted):** `O1` is proved at the level of 2D fixed-period non-Abelian Hodge relaxation + 2-register $D_4 \oplus D_4 \to E_8$ unimodular closure; `O2` is proved at the level of unbroken cross-grading $\mathfrak{g}_{128}^{(-1)} \leftrightarrow \mathfrak{g}_{120}^{(+1)}$ weak current overlap and $SU(2)_L \times U(3)_{\text{fam}}$ Haar invariance.
- **Reasoning trail (clean):** `L1` ($\zeta$-grading holonomy $w_\zeta = \frac{3}{2}Q$) → Conflict on `L2` ($\mathbb{Z}_2$ sheet sign vs $\omega_3$) → Backjump to `L3` ($h_{15} = \operatorname{Ad}_{h_4}$ at $\chi=(0,0)$ gives `(0,3,3,0)` on all 8 records = `24`) → `L4` (32-component zero-mode wavefunction overlap $G^{(W)}_{ab}(w_0)$) → Scope calibration on `O1`/`O2`.
- **What would unblock full `SOLVED` on `O1` and `O2`:**
  1. **Subgoal `O1-dyn`:** Derive a stationary point $(U^*, V^*) \in Q_8$ from a coupled 6D gauge + surface + boundary action without pre-specifying the $Q_8$ holonomy constraint.
  2. **Subgoal `O2-ewsb`:** Introduce an explicit electroweak-breaking scalar condensate $H_0 \neq 0$ into `physical_mass(q, r, omega, pbar, pz)` and compute the broken-phase chiral fermion zero-mode splitting under $Q_{\text{em}} = T_3 + Y$.
