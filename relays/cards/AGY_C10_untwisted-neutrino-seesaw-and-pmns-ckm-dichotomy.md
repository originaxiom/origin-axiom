# Card AGY-C10: Untwisted right-handed neutrino see-saw (`6 Y(nu^c) = 0`), circular-null Takagi `1 / sqrt(2)` mixing theorem, and the `PMNS` vs `CKM` dichotomy

*Seat: `agy` (`agy/cusp-action-2026-11-20`, after `origin/main` `279459977` / `B1970`). Date: `2026-11-21`. Pre-registered before any script or run (`expectations committed first`). Data-free: `0 of 19`.*

---

## One. Package and question

In `B1970` (`D2`, `D3`), `L nu^c` couples to the same `Y = +1 / 2` doublet `H_u` (`reading holomorphic S`) as `Q u^c`, with sector charges `(q_L, q_R) = (minus 3, 0)` (`since nu^c = Lambda^0(C^5) in 16_+ has 6 Y = 0`). With **zero** extra parameters (`using the canonical O(3) Killing bilinear form M_R = M_0 I_3 on Im(H)`), does the Type-I see-saw operator `m_nu = minus (v_u^two / M_0) Y_nu Y_nu^T` turn aligned Dirac neutrino mixing into **large `O(1)` `PMNS` leptonic mixing** (`including asymptotic 1 / sqrt(2) solar mixing`) at the **same** moduli where Hermitian `Y_q Y_q^dag` keeps `CKM` aligned?

## Two. Deliverables and what done means

- Explicit `32 x 32` `Spin(10)` Clifford verification of the symmetric `L nu^c H_u` coupling (`5bar_4 x 1_0 x H_5`) and symbolic `sympy` proof of the **Circular-Null Takagi `1 / sqrt(2)` Theorem** (`on circularly polarized light states v_+- = (e_1 +- i e_2) / sqrt(2), Hermitian v_+ v_+^dag is diagonal while symmetric v_+ v_-^T + v_- v_+^T rotates Takagi eigenvectors by pi / 4 -> |U_{e 1}| = |U_{e 2}| = 1 / sqrt(2)`).
- `70`-digit `mpmath` evaluation of `Y_nu` (`(minus 3, 0)`), `Y_e` (`(minus 3, 6)`), `m_nu = Y_nu Y_nu^T`, `|U_PMNS|`, and `|V_CKM|` across `m * tau_*^+` (`m` in `{8, 16, 40}`) and across the `s = 2` open weave (`including P_3 / P_6`), enforcing Guardrail three under `U(3)_L x U(3)_{e_R} x O(3)_{nu_R}` basis scrambling.
- Zero-shared-code independent countercheck (`recomputed independently` + `tested against planted errors`, `5 / 5` plants) and mask-clean result relay.

## Three. Pre-committed expectations and how it could come out wrong

- **E1 (Asymptotic `1 / sqrt(2)` solar `PMNS` theorem vs aligned Dirac neutrinos):** Without Majorana see-saw (`pure Dirac Y_nu Y_nu^dag`), `min_k |U_{PMNS, kk}^{Dir}| > 99 / 100` at `m = 40` (`aligned like CKM`), whereas turning on `m_nu = Y_nu I_3 Y_nu^T` splits all three Majorana singular values (`0 < m_1 < m_2 << m_3`, normal ordering with `(m_2 minus m_1) / m_2 -> 0` as `y` grows) and drives `(|U_{e 1}|, |U_{e 2}|) -> (1 / sqrt(2), 1 / sqrt(2))` (`within 1 / 1000 at m = 40` and `> 3 / 5` across all `m` in `{8, 16, 40}`)!
- **E2 (Simultaneous `O(1)` `3`-angle `PMNS` and small normal-ordered `CKM` in the `m = 8` collar):** At `m = 8` (`8 tau_*^+ = (16 + 8 i) / 5`), `m_nu = Y_nu Y_nu^T` must simultaneously produce large solar **and** atmospheric mixing (`|U_{e 2}| > 1 / 2` and `|U_{mu 3}| > 1 / 2` while `|U_{e 3}| < 1 / 3`) alongside normal-ordered `CKM` (`|V_12| > |V_23| > |V_13|`), whereas at deep `m = 40` atmospheric `|U_{mu 3}|` suppresses (`< 1 / 100`) under unwarped `M_R = M_0 I_3` (`honestly isolating the m = 8 vs m = 40 atmospheric tradeoff`).
- **E3 (Exact `U(3)_L x U(3)_{e_R} x O(3)_{nu_R}` invariance & complex-unitary `U(3)_{nu_R}` non-invariance):** Because `M_R = M_0 I_3` is preserved by real orthogonal `O(3)_{nu_R}` (`O_R O_R^T = I_3`) and broken by complex unitary `U_R` (`U_R U_R^T != I_3`), `|U_PMNS|` must be invariant to `< ten to the minus forty` under `U(3)_L x U(3)_{e_R} x O(3)_{nu_R}` scrambling (`Guardrail three`).

## Four. Premises and firewall boundaries

- Rests on `B1253`, `B1970`, and `AGY-C5` through `AGY-C9`; Guardrails one through six enforced (`M_R = M_0 I_3` uses zero free mixing parameters; overall scale `v_u^two / M_0` unfixed prior to absolute scale anchoring).
- Must **never** read, compute, or compare any of the nineteen empirical Standard Model targets or neutrino oscillation tables (`0 of 19`), and must leave `origin/agy/audit-2026-11-02` untouched at `4319f47e2`.

## Five. Mandatory planted negative control

1. **Pure-Dirac (`no see-saw`) plant:** Replace Majorana `Y_nu Y_nu^T` with Hermitian Dirac `Y_nu Y_nu^dag` at `m = 40`: `|U_{e 2}|` must collapse from `~ 1 / sqrt(2)` to `< 1 / 10` (`catching loss of circular-null Takagi rotation`).
2. **Illegal complex-unitary `U(3)_{nu_R}` scrambling plant:** Apply a complex phase gate `diag(1, i, 1)` on `nu_R` without transforming `M_R = I_3`: `|U_PMNS|` must shift by `> 1 / 10` (`confirming Majorana O(3)_{nu_R} frame locking`).

## Six. What is needed from main or other seats

Nothing needed to run; offered as a data-free Phase II neutrino see-saw investigation on `agy/cusp-action-2026-11-20`.

0 of 19.
