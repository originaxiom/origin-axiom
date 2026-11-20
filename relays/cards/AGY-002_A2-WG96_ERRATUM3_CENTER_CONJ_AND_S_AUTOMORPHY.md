# AGY-002 Erratum 3: Card A2-WG96 `v2` Review Fixes (`Z(W:G96)` Split Center, SVD Conjugation, and `c_3` `S`-Automorphy Sign) (`0 of 19`)

- **Card:** `AGY-002 / A2-WG96` (`relays/cards/AGY-002_A2-WG96_ej5-mapping-class-family-modes-vs-weave-g96-triplet.md`)
- **Superseded Producer Artifacts (`untouched`):** `relays/a2_wg96/verify_a2_wg96.py` (`380a50c54`), `relays/a2_wg96_v2/verify_a2_wg96_v2.py` (`1053d2355`, `7af361ec7`)
- **Authoritative Producer Artifact:** `relays/a2_wg96_v3/verify_a2_wg96_v3.py`

---

## 1. Passing Results Confirmed in Sealed `v2` (`7af361ec7`)

In `relays/a2_wg96_v2/verify_a2_wg96_out.json`, `section_0_ast_and_custody` (`0` float/complex AST literals, exact `SHA-256` match), `W2` (`N_3` orbit `8/8`, `N_5` orbit `24/24`, `0` common fixed points), `W3` (`charge_conj_S2_eigenvalues == [-1, -1, 1]`, `M_T` turns `[1/24, 1/24, 3/8]`, commutant dim `2` and zero overlap with `W:T` / `W:\overline{T}` across all `24` twists), `W4` `Gate F-U2` `24`-pt `L/R` invariance (`ratio` and `|V_{CKM}|` drifts `< (1/10)^27` on both `ODE L_2` and `seed 5/2`, and `ODE L_2` covariance `< (1/10)^42`), `B1736` `\det=1` orders `{5: 72, 13: 72, 21: 24}`, `k = 0 / 18` character inner products `1`, and all `5` planted faults `PF1..PF5` passed.

## 2. Three Implementation & Automorphy-Sign Clarifications Applied in `v3` and For Cold-Room Referees

1. **`W1` Split-Chirality Center `Z(W:G96)` (`order 4`) and Quotient `W:G96 / Z(W:G96)` (`S_4`, order `24`):**
   - `V = W:T \oplus W:\overline{T}` (`dim 6`) carries the complex representation `W:T` on `H_Q > 0` (`3D`) and its conjugate `W:\overline{T}` on `H_Q < 0` (`3D`), so a central element of order `4` acts as `+i I_3` on `W:T` and `-i I_3` on `W:\overline{T}` rather than a scalar multiple `e^{i\phi} I_6` (`which captured only {+I_6, -I_6}`).
   - `center_and_projective_order` computes the true finite-group centralizer `Z = {g \in G_{LR} : g M_L = M_L g \text{ and } g M_R = M_R g}` (`|Z| = 4`) and the exact coset partition `G_{LR} / Z` (`|G_{LR}/Z| = 24`).
2. **SVD Right-Vector Conjugation in `intertwiner_space`:**
   - Standard `SVD` factorizes `M = U \Sigma V^H`, so rows of `Vh` hold `\overline{v_k}` rather than `v_k`. Conjugating `Vh[sv < tol].conj()` removes the spurious `norm = 2` residual (`and restores unique unitary intertwiners at k = 0 onto W:\overline{T} and at k = 18 onto W:T to < (1/10)^14`, as well as `10`-trial `Haar` scrambling to `< (1/10)^13`).
3. **`W4` `S`-Transformation Sign of `c_3(\tau)` (`weight +3/2` vs `R_h(\tau)` weight `-1/2`):**
   - Under `S: \tau \mapsto -1/\tau`, `R_h(\tau)` (`weight -1/2`) obeys `R_h(-1/\tau) = (-i\tau)^{-1/2} (+P_{01}) R_h(\tau)`.
   - Because `c_3(\tau) = \frac{1}{2\pi\eta(\tau)^3} \big( \frac{1}{2\pi i}\partial_\tau - \frac{E_2(\tau)}{12}\big) (\pm \vartheta_j(\tau)^2)` differentiates `\vartheta_j^2` once wrt `\tau`, and `\frac{d(-1/\tau)}{d\tau} = \frac{1}{\tau^2} = -\frac{1}{(-i\tau)^2}`, `c_3` picks up `-(-i\tau)^{+3/2}`: **`c_3(-1/\tau) = \tau^2 (-i\tau)^{-1/2} P_{01} c_3(\tau) = -(-i\tau)^{+3/2} P_{01} c_3(\tau)`** (`Card line 59`'s phrasing `"after dividing out (-i\tau)^w acts by P_{01}"` omitted this `-1` relative phase between `(-i\tau)^2` and `\tau^2`).
   - Because `R = S T^{-1} S^{-1}` conjugates by `S`, the `-1` sign cancels identically on `R`, so both `R_h` and `c_3` share the exact same projective/automorphy `<L, R>` matrices `(r_T, R_0)` (`R_0 = P_{01} r_T^{-1} P_{01}^{-1}`). `0 of 19.`
