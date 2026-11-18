# Card `X-L5` — Independent Second Computation of `main`'s Level-`5` Point-Phase Law (`P-871` / `B1945` Section `6`) & Audit of `X-FOUNDATION-4`'s Shifted Convention

- **Seat:** `agy-exp` (`branch: agy/self-consistent-loop-2026-11-11`)
- **Authorization:** Pre-approved in `M37` and `M38` on `docs/seats/agy-exp.md` (`4921ee923`; `0 of 19`, zero empirical data, zero reading of `main`'s check script).
- **Protocol:** `4`-commit blind-sealed execution (`Commit 1` Card -> `Commit 2` Standalone Verifier Script -> `Commit 3` Raw JSON Output + `OUTPUT_SHA256.txt` -> `Commit 4` Mask-Clean Results Note).

## 1. Statement Under Test (`From M37 & B1945 Section 6 Prose Alone`)

Let $w = (a, b)$ be any of the `24` order-`5` points of $(\frac{1}{5}\mathbb{Z}/\mathbb{Z})^2 \setminus \{(0, 0)\}$, $\zeta = \exp(2\pi i / 5)$, and $q_H = -(q_L + q_R)$ across the three charged sectors `sec_1 = (1, -4)` ($q_H = +3$), `sec_2 = (1, 2)` ($q_H = -3$), and `sec_3 = (-3, 6)` ($q_H = -3$). Place the Higgs Szegő zero at $h = c \cdot q_H \cdot w$ (`residue at u_0 = -h` in `Frame D1`'s bilinear $v_{q_L w}(u \mid 2\tau)\, v_{q_R w}(u \mid 2\tau)^T / \theta_1(u + h \mid \tau)$):

1. **Pointwise fifth-root phase (`C1`):** Under $\tau \mapsto \tau + 5$ (holding the point representative $(a, b)$ fixed), relative to the $w$-independent $T^5$ transformation (`at a = 0`), the residue's diagonal channels change by $\zeta^{E \cdot (5a)^2}$ with
   $$E \equiv q_L^2 + q_R^2 + c \cdot q_H^2 \pmod 5,$$
   and at even $c \in \{0, 2, -2\}$ the entire `2 x 2` residue and contracted `3 x 3` coupling (`in both S and \tilde{S}`) transform by the scalar point phase $\zeta^{E \cdot (5a)^2}$ (`closing to 1 under \tau + 25`).
2. **Odd-$c$ off-diagonal sign (`C2`):** At odd $c \in \{1, -1, 5, 7\}$, the two off-diagonal entries of the `2 x 2` residue additionally change by $(-1)^{5a}$ relative to the diagonal entries under **both** $\tau \mapsto \tau + 5$ and $\tau \mapsto \tau + 25$.
3. **Incompatible level-`5` closure (`C3`):** Across all $c \in \mathbb{Z}$, `sec_1` requires $c \equiv 2 \pmod 5$ while `sec_2` and `sec_3` require $c \equiv 0 \pmod 5$, so no integer placement $c$ closes both `sec_1` and `sec_2` at level `5`.
4. **Classification of `X-FOUNDATION-4`'s `"shifted"` convention (`C4`):** Compare `X-FOUNDATION-4`'s `2D` magnetized overlap (`q_H = -(q_L + q_R)`) against `Frame D1` across all `24` order-`5` points and all `3` sectors: test whether its sector-closure pattern matches $c = 2$ while determining its exact pointwise exponent $E_{\mathrm{mag}} \pmod 5$ (`expected q_L^2 - q_R^2 \equiv (0, 2, 3) \pmod 5 vs Frame D1 c = 2's (0, 3, 3)`) and chord spread $2\sin(\pi/5)$.

## 2. Preregistered Gates & Planted Controls

- **`Gate_U0`:** Exact `50`-digit match (`< (1/1000)^14`) at $c = 0$ between the `2 x 2` level-`2` bilinear residue and our standalone `Frame C` channel-residue engine across `3` bulk moduli (`13/100 + (17/10)i`, `-31/100 + (12/5)i`, `27/100 + (27/20)i`).
- **`Gate_C1_C2_C3`:** Exact verification (`< (1/1000)^14`) of `C1`, `C2`, and `C3` across all `7` placements $c \in \{0, 1, -1, 2, -2, 5, 7\}$, all `3` sectors, `2` representative sets (`[0, 4/5]` and `[-2/5, 2/5]`), and `3` bulk moduli.
- **`Gate_C4`:** Exact extraction (`< (1/1000)^9`) of $E_{\mathrm{mag}} \pmod 5$ and `T^5`/`T^{25}` spreads on `X-FOUNDATION-4`'s magnetized overlap vs `Frame D1` at $c = 2$.
- **`Gate_PC` (`4` Planted Controls + AST Gate):** `PC_XL5_1_WrongQuadraticC` ($q_L^2 + q_R^2 + (c + c^2/4)q_H^2$ rejected), `PC_XL5_2_OmittedOddCSign` (omitting $(-1)^{5a}$ at odd $c$ rejected by `2`), `PC_XL5_3_SimultaneousLevel5Closure` (rejected across all $c \in \mathbb{Z}/5\mathbb{Z}$), and `PC_XL5_4_PlainSumT5Invariance` (plain sum at $E \not\equiv 0$ rejected), plus zero float literals in model helpers.
