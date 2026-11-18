# Card A2-X1 (`M47` + `M48`): Frame `D1`'s Higgs Ground Plane Across Three Seats, Deciding Computations, and Independent `2D` Quadrature Second Computation of `SM-C21` & `h*`

- **Seat:** `agy-002` (`branch: agy-002/verify`, appended onto `62420b533` without rebase)
- **Custody Seal:** Expectations committed prior at `4214628c8` (`relays/cards/AGY-002_A2-X1_frame-d1-higgs-three-seat-cross-read-sm-c21-and-hstar-plane.md`); standalone zero-float-literal `65`-digit `2D` torus-quadrature script sealed prior at `552f4ca17` (`relays/a2_x1/verify_a2_x1.py`, `relays/a2_x1/SCRIPT_SHA256.txt`); raw outputs committed unread at `20b911fd4` (`relays/a2_x1/verify_a2_x1_out.json`, `relays/a2_x1/verify_a2_x1_out.txt`, `relays/a2_x1/OUTPUT_SHA256.txt`).
- **Rule Compliance:** Read-only notes and cards only on `SM` (`a69cee901`) and `physical` (`a47e76da6` and its immediate six-note completion `aa9facef6`, pinned by `main` at `frontier/B1957_the_seats_claims_register/verification/checks/physical_c8_tick_higgs.py:1`); **zero `.py` files of any other seat opened or run**; **zero use of `main`'s closed form `cim_closed.py`**; **zero comparison with measured data (`0 of 19`)**.

---

## 1. Each Source's Statement of the Exchange Operation and What Would Fix the Higgs Choice

### Source `1` — `SM` Seat (`SM-C18` to `SM-C21` at `a69cee901`)
- **Which operation exchanges the two Higgs worlds:**
  - `a69cee901:relays/SM_C19_WHICH_BIT.md:10-14`:
    ```text
    - **The bit is exchanged only by an antiunitary,** complex conjugation composed with a modular transformation of the
      modes: A·conj with A = T₆S₆, T₆S₆⁻¹, S₆T₆ or S₆⁻¹T₆. Each satisfies A·conj(U_M)·A⁻¹ = U_M and sends v₊ to v₋ with
      overlap 1.000. These are the shortest words found among the record's operators.
    - An antiunitary composed with a modular transformation is an orientation-reversing element of GL(2, ℤ) acting on the
      modes. **So frame D1's undetermined Higgs bit is the hand.**
    ```
  - `a69cee901:relays/cards/SM_C20_is-the-exchange-the-tick.md:11-13`:
    ```text
    - R₀ is τ → −τ̄, z → z̄. On the flux-6 modes θ[k/6, 0](6z, 6τ), whose Fourier coefficients are real, it acts as plain
      complex conjugation K, with no permutation of k.
    - So the tick acts on the six modes as the antiunitary Σ = ρ(T)ρ(S)·K = T₆S₆·K.
    ```
- **What would fix the bit (and its cusp consequence):**
  - `a69cee901:relays/SM_C18_THE_TRIPLE_OVERLAPS_COVARIANCE.md:48-51`:
    ```text
      - (a) read it on the double cover of the w-torus, which is one extra bit. It is the two-dimensional ground space
        B1957 found;
      - (b) give the Higgs an even charge, which changes the hypercharges.
    - Nothing here chooses between them.
    ```
  - `a69cee901:relays/SM_C20_THE_EXCHANGE_IS_THE_TICK.md:13-18, 39-40`:
    ```text
    - **So frame D1's one undetermined Higgs bit is the tick's own orientation:** one bit, carried by one move of the
      genesis.
      - A history with an odd number of ticks flips it. One with an even number keeps it.
      - This ties the Higgs vacuum to the even-tick condition (the author's ruling of 2026-11-11; B1926), and to the hand's
        invariant (SM-C9, B1929).
    - **Not decided here:** which sign is realised.
    ```
    ```text
    So the Higgs's vacuum bit in frame D1 is not a free input. It is the same bit as the tick's orientation, which the
    record already carries. The choice of sign is the record's single orientation choice, not a new one.
    ```
  - `a69cee901:relays/SM_C21_THE_D1_CUSP_MIXING.md:9-10, 16`:
    ```text
    - **With the Higgs at either tick-fixed ground state v±, D1's mass ratios do not fall with height:** the cusp
      exponents go to 0.
    ```
    ```text
    - **So the cusp-exponent route is closed for frame D1 at its tick-fixed Higgs.** Frame C's cusp exponents were rational
    ```

### Source `2` — `physical` Lane (`tick_higgs_alignment_2026_11_18` at `a47e76da6` & `aa9facef6`)
- **Which operation exchanges the two eigenlines (and coordinate-lift correction):**
  - `a47e76da6:reports/physical_bridge_2026_09_05/tick_higgs_alignment_2026_11_18/EXACT_GROUND_SPACE_AND_SELECTION.md:65-70`:
    ```text
        Sigma²=U.                                          (1)

    Composition implies Sigma U=U Sigma as maps. Antilinearity therefore
    takes an eigenvalue to its complex conjugate. The two normalized
    ground vectors v_+,v_- of phases +-theta, theta=pi/6, are exchanged.
    This preserves the genuine matrix content of SM-C20 exactly.
    ```
  - `a47e76da6:reports/physical_bridge_2026_09_05/tick_higgs_alignment_2026_11_18/COVARIANT_LIFTS_AND_KINETIC_RESPONSE.md:16-19, 23-24`:
    ```text
        psi_j(-conjugate(z),-conjugate(tau);-conjugate(zeta))
                                          =conjugate(psi_j(z,tau;zeta)),
        psi_j( conjugate(z),-conjugate(tau); conjugate(zeta))
                                          =conjugate(psi_-j(z,tau;zeta)). (1)
    ```
    ```text
    Thus the first geometric lift induces K and the second P K on
    coefficients after conjugating the field, with P:j -> -j.
    ```
- **Why the ground space is a complex `2D` plane `E` (`CP^1`) and what would fix a direction:**
  - `a47e76da6:reports/physical_bridge_2026_09_05/tick_higgs_alignment_2026_11_18/EXACT_GROUND_SPACE_AND_SELECTION.md:101-106, 143-148, 212-214`:
    ```text
        K|E=theta²/L² I_2,
        M_H²|E=(theta²/L²-c b) I_2.                         (3)

    Every unit `h=a v_+ + b_0 v_-`, with `|a|²+|b_0|²=1`, is a ground
    direction of this quadratic problem. Already modulo a common phase,
    these directions are CP1. A direction is a monodromy eigenline only
    ```
    ```text
    entries, so **H=alpha I_2**. A fully tick-symmetric quadratic law
    protects this doublet's degeneracy; it does not prefer one line.

    There is also no Sigma-fixed coefficient ray in E. If
    `Sigma h=lambda h`, antiunitarity gives `U h=|lambda|² h=h` for
    a unit h, whereas neither eigenvalue of U on E is one. This is a
    ```
    ```text
    For the **complete relaxed** quartic, an exact target is

        B=V4_eff(v_+)-V4_eff((v_+ + v_-)/sqrt(2)).          (8)
    ```
  - `aa9facef6:reports/physical_bridge_2026_09_05/tick_higgs_alignment_2026_11_18/C21_EXACT_CUSP_SCOPE_AND_COHERENT_CONTROL.md:97-101, 164, 188`:
    ```text
    The two-mode ground space is not the set of those two vectors.
    An explicit unit vector in it is

        h_*=(1/sqrt(2), exp(i pi/12)/2, 0, 0, 0,
                                                  exp(i pi/12)/2).        (3)
    ```
    ```text
        E_up(s2/s1)=0, E_up(s3/s1)=4/3.                   (6)
    ```
    ```text
        E_down(s2/s1)=1/5, E_down(s3/s1)=4/5.             (8)
    ```

### Source `3` — `origin/main` (`B1945 § 6`, `P-871`, `P-873`, `docs/seats/sm.md` at `4921ee923`)
- **Which operations exchange the $\pm\pi/6$ pair (and why amphicheirality blocks fixing a sign):**
  - `4921ee923:docs/seats/sm.md:44-45, 54-56`:
    ```text
      S M S⁻¹ = M⁻¹, so S₆ carries U_M to its inverse and v₊ to v₋ with overlap 1.000000. Over the whole group generated
      by T₆ and S₆ (576 elements up to phases):
    ```
    ```text
      So the pair is exchanged exactly when the bundle's orientation is reversed, counting the fibre and the direction of
      the act together. Your conclusion that the bit is the hand stands in that sharper form. One consequence your cards
      do not draw: the figure-eight has an orientation-reversing symmetry of its own, so the object cannot fix the sign.
    ```
- **Level-`5` point-phase obstruction (`P-871`) and unselected `2D` ground plane (`P-873`):**
  - `4921ee923:frontier/B1945_the_frames_cusp_exponents/FINDINGS.md:216-220`:
    ```text
        - **In frame D1** (the residue at the pole, the Higgs zero placed at c·q_H·w; main's rebuild of the web seat's
          W-B2) the same law holds with E = q_L² + q_R² + c·q_H², checked for c = 0, ±1, ±2, 5, 7 and all three sectors.
          At c = 2 the up sector closes and the down and lepton sectors do not: the obstruction changes sector.
        - **No placement closes both.** Up needs c ≡ 2 and down needs c ≡ 0 modulo 5.
        - At odd c the residue's two off-diagonal entries also change by (−1)^(5a), under τ + 5 and under τ + 25.
    ```
  - `4921ee923:docs/POINT_REGISTER.md:1086` (`P-873`):
    ```text
    NOTHING COMPUTED SELECTS A DIRECTION: the quartic invariant under the common phase, the transport and the tick is A N^2 + B Delta^2 (B < 0 the eigenlines, B > 0 the equal-magnitude circle, which contains h*), and the relative phase first enters an invariant at degree 14 (Delta w^6) and on the circle at degree 24 (w^12).
    ```

---

## 2. Every Contradiction Across the Three Sources & Its Deciding Computation

| ID | Contradiction Between Sources | Single Deciding Computation (`verify_a2_x1.py`) | Verdict (`20b911fd4`) |
|---|---|---|---|
| **`DC-1`** | `SM-C19` (`SM_C19_WHICH_BIT.md:10`) says $(v_+, v_-)$ is exchanged *"only by an antiunitary"*; `main` (`docs/seats/sm.md:44-56`) says unitary $S_6$ ($\det S = +1$) and `12` unitaries in $\langle T_6, S_6\rangle/U(1)$ also exchange $(v_+, v_-)$ *(untouched by `physical`)*. | Enumerate $\langle T_6, S_6\rangle / U(1)$ (`576` projective elements) as unitaries and antiunitaries on $(U_M, v_+, v_-)$; check $\|S_6 U_M S_6^{-1} - U_M^{-1}\|$ and $|\langle v_-, S_6 v_+\rangle|$. | **`main` holds (`SM-C19` refuted on `"only"`):** `12` unitaries invert $U_M$ & exchange $v_\pm$ (`including S_6`, error `< (1/10)^64`, overlap `1`), `12` antiunitaries keep $U_M$ & exchange $v_\pm$ (`including Sigma = T_6 S_6 K`, $\|\Sigma^2 - U_M\| < (1/10)^64$). Exchange $\iff$ bundle orientation reversal. |
| **`DC-2`** | `SM-C20` (`SM_C20_THE_EXCHANGE_IS_THE_TICK.md:39-40`) calls the ground choice *"one bit ... not a free input"*; `physical` (`C8-02`) & `main` (`P-873`) say $M_H^2|_E \propto I_2$ leaves a complex `2D` plane ($\mathbb{CP}^1$), $\Sigma$ fixes no ray, quadratic invariants are $\alpha I_2$, and relative phase is unseen until degree `14` (`24` on $|z_+| = |z_-|$). | Compute $\frac{1}{2}(U_M + U_M^\dagger)|_E$, $\dim_{\mathbb{R}}\{H = H^\dagger : \Sigma H \Sigma^{-1} = \pm H\}$, and $(U(1), U_M, \Sigma)$-invariant polynomial dimensions through degree `24`. | **`physical` & `main` hold:** $\frac{1}{2}(U_M + U_M^\dagger)|_E = \frac{\sqrt{3}}{2}I_2$ to `< (1/10)^64`; $\Sigma$-even/odd Hermitian dimensions are `(1, 1)`; invariant polynomial dimensions at degrees `(2, 4, 6, 8, 10, 12, 14, 24)` are `(1, 2, 2, 3, 3, 4, 6, 15)` vs `(1, 2, 2, 3, 3, 4, 4, 7)` for $\mathbb{R}[N, \Delta^2]$; circle phase enters at degree `24`. |
| **`DC-3`** | `SM-C21` (`SM_C21_THE_D1_CUSP_MIXING.md:9-16`) closes `Frame D1`'s cusp-exponent route (`exponents -> 0`); `physical` (`C8-05`) & `main` (`K5, K6`) find $h_* \in E$ has rational exponents `(0, 4/3)` (`up`) and `(1/5, 4/5)` (`down`, `lepton`). | Recompute both $v_\pm$ and $h_*$ on `agy-002`'s independent `2D` torus wavefunction quadrature (`zero cim_closed.py`), plus $h_*$'s CKM moduli (`P-873 Q3`). | **Scoped synthesis:** `SM-C21` holds on $v_\pm$ and generic $E$-vectors (`exponents -> 0`), while $h_* \in E$ (`|<v_+- , h*>|^2 = 1/2`) gives `(0, 4/3)` and `(1/5, 4/5)` — **but** $|V_{\text{mark}}(h_*)|$ has maximal `1-3` mixing (`0 / 96` aligned; § `3` below). |
| **`DC-4`** | `SM-C20` card (`cards/SM_C20_is-the-exchange-the-tick.md:11-12`) assigns $(\tau, z) \mapsto (-\bar{\tau}, +\bar{z})$ to plain $K$; `physical` (`C8-03`, `COVARIANT_LIFTS_AND_KINETIC_RESPONSE.md:16-24`) & `main` (`K9`) say $+\bar{z}$ induces $P K$ while $-\bar{z}$ induces $K$. | Evaluate literal flux-`6` spin-`(0,0)` modes at $(-\bar{\tau}, \pm\bar{z}, \pm\bar{\zeta})$ vs $\overline{\psi_{\pm k}}$ and compare $T_6 S_6 K$ vs $P_6 T_6 S_6 K$ on $E$ and $E_{\text{odd}}$. | **`physical` & `main` hold:** $-\bar{z}$ matches $K$ (`0` error), $+\bar{z}$ matches $P K$ (`< (1/10)^64`, failing $K$ by `> 2`); both square to $U_M$ and agree on $P$-even $E$ (`< (1/10)^64`), differing by norm `2` on $P$-odd $\pm\pi/3$. |
| **`DC-5`** | `SM-C18` (`SM_C18_THE_TRIPLE_OVERLAPS_COVARIANCE.md:24, 48-49`) identifies the half-Wilson cover as a *"double cover ... one extra bit = the 2D ground space"*; `physical` (`C8-01, C8-04`) & `main` (`K2, K8`) show `4` sheets $E[2]$, `2/3` leakage out of $E$, `0` $M$-invariant $\mathbb{Z}_2$ characters, and non-scalar covariant $B(w)$ prior to averaging. | Compute $\|(I_6 - P_E) g v_+\|_2^2$ for $g \in \{Z^3, X^3, Z^3 X^3\}$, $\ker_{\mathbb{F}_2^2}((M - I_2)^T)$, and $B(w+1), B(w+\tau)$ vs `4`-lift twirl. | **`physical` & `main` hold:** $Z^3 X^3 = -X^3 Z^3$ (`4` sheets), every non-trivial lift has $\langle v_-, g v_+\rangle = 0$ and leaks `2/3` outside $E$ (`< (1/10)^64`), `0` non-zero $M$-invariant $\mathbb{F}_2$ characters exist, and single-point $B(w)$ has relative spread `> 17/100` (`covariant to < (1/10)^62`) before `4`-lift averaging (`scalar to < (1/10)^64`). |
| **`DC-6`** | `SM-C18` tests $T$-covariance at fixed $\xi$ and treats `"frame D1"` as one object; `main` (`B1945 § 6`, `P-871`) proves at fixed order-`5` torsion $(a, b)$ under $\tau \mapsto \tau + 5$ that `up` needs $c \equiv 2$ and `down` needs $c \equiv 0 \pmod 5$ (`no c closes both`). | Evaluate $\tau \mapsto \tau + 5, \tau + 25$ at all `24` points $(a, b) \in E[5]\setminus\{0\}$ on **both** Szegő-residue `D1` ($h = c q_H w$) and closed-fibre flux-`(3,3,6)` `D1` (`2D` quadrature). | **Unified obstruction proved (`< (1/10)^52`):** Szegő-residue `D1` obeys $\zeta_5^{(q_L^2 + q_R^2 + c q_H^2)(5a)^2}$ (`< (1/10)^61`, `0` placements close both); closed-fibre `D1` ($\zeta_H = \frac{q_L+q_R}{2}w \leftrightarrow c \equiv 2 \pmod 5$) obeys $\exp(\frac{5\pi i c_{ijm}^2}{6} + \pi i c_{ijm}\Delta_s(5a) + \frac{3\pi i \Delta_s^2(5a)^2}{10})$ (`< (1/10)^52`), closing the `5`th-root factor in `up` (`0 / 24` obstructed) while obstructing `down` and `lepton` (`20 / 24` points carry $\zeta_5^{2(5a)^2}$). |

---

## 3. Independent Second-Family Computation of `SM-C21`, `h*`, and `P-873 Q3` (`M48` Additions `1` & `2`)

1. **Non-Closed-Form Instrument Calibration:** Direct `65`-digit `mpmath` `2D` torus wavefunction quadrature on grids `(11, 64)` vs `(17, 84)` at $y = 8$ agrees to `< 3 * (1/10)^58`, matches unfolded universal-cover `1D` real-line quadrature to `< 3 * (1/10)^58` (`with all 36 Z_3-forbidden triples < 5 * (1/10)^65`), and converges at $y = 14$ (`(11, 80)` vs `(17, 100)`) to `< 5 * (1/10)^52`.
2. **Mark `(2/5, 4/5)` Ratio Exponents ($\tau = 13/100 + y i$, Unshifted Lift, $M_{\text{lepton}}(h) = e^{i\phi} M_{\text{down}}(h)^T$ to `< (1/10)^64`):**

   | Higgs Vector in $E$ | Sector | $(E_2, E_3)$ on `6 -> 8` (nearest `1/10000`) | $(E_2, E_3)$ on `8 -> 10` (nearest `1/10000`) | $(E_2, E_3)$ on `11 -> 14` (nearest `1/10000`) | Exact Cusp Limit |
   |---|---|---|---|---|---|
   | $v_+$ (`+pi/6` eigenline) | `up` | `(-32/10000, -16/10000)` | `(-12/10000, -6/10000)` | `(-2/10000, -1/10000)` | **`(0, 0)`** (`SAME` as `SM-C21`) |
   | $v_+$ (`+pi/6` eigenline) | `down` = `lepton` | `(-188/10000, -268/10000)` | `(-104/10000, -116/10000)` | `(-33/10000, -26/10000)` | **`(0, 0)`** (`SAME` as `SM-C21`) |
   | $v_-$ (`-pi/6` eigenline) | `up` | `(+198/10000, -286/10000)` | `(+77/10000, -87/10000)` | `(+14/10000, -14/10000)` | **`(0, 0)`** (`SAME` as `SM-C21`) |
   | $v_-$ (`-pi/6` eigenline) | `down` = `lepton` | `(+72/10000, -70/10000)` | `(+40/10000, -41/10000)` | `(+14/10000, -14/10000)` | **`(0, 0)`** (`SAME` as `SM-C21`) |
   | $v_{\text{gen}} \in E$ (`3/5, 4/5` weights) | `up` / `down` | `(<= 45/10000, <= 80/10000)` | `(<= 34/10000, <= 44/10000)` | `(<= 14/10000, <= 15/10000)` | **`(0, 0)`** (`SAME` as `main K6`) |
   | $h_* = (\frac{1}{\sqrt{2}}, \frac{e^{i\pi/12}}{2}, 0, 0, 0, \frac{e^{i\pi/12}}{2})$ | `up` | `(-124/10000, +13393/10000)` | `(-43/10000, +13355/10000)` | `(-7/10000, +13337/10000)` | **`(0, 4/3)`** (`SAME` as `physical C8`) |
   | $h_* = (\frac{1}{\sqrt{2}}, \frac{e^{i\pi/12}}{2}, 0, 0, 0, \frac{e^{i\pi/12}}{2})$ | `down` = `lepton` | `(+1978/10000, +7981/10000)` | `(+1994/10000, +7995/10000)` | `(+1999/10000, +7999/10000)` | **`(1/5, 4/5)`** (`SAME` as `physical C8`) |

3. **`96`-Case Mixing Sweep (`24` Order-`5` Points $\times$ `4` Lifts at Height `8`, Direct `2D` Quadrature) & Resolution of `P-873 Q3`:**
   - **$v_+$ (`all 4 lifts`):** `full rank 3` (`s_3 > (1/10)^12 s_1`) on `24 / 24` points; `(aligned: 0, top-aligned: 0, permutation: 0, other: 24)` (`SAME` as `SM-C21`).
   - **$v_-$ (`all 4 lifts`):** `full rank 3` on `24 / 24` points; `(aligned: 0, top-aligned: 4, permutation: 0, other: 20)`, where the `4` `top-aligned` points are `[(0, 1/5), (0, 2/5), (0, 3/5), (0, 4/5)]` (`SAME` as `SM-C21`).
   - **$h_*$ (`96` cases at height `8`):** **`aligned: 0` and `permutation: 0` on all `4` lifts (`0 / 96` aligned)** — lifts `(0, 0), (0, 1)` give `(0, 0, 0, 24)` (`with 10/24 up and 15/24 down above the (1/10)^12 cutoff because exponential cusp suppression already pushes s_3/s_1 below (1/10)^12!`), while lifts `(1, 0), (1, 1)` ($X^3$ shifting the zero triple `(2, 3, 4) -> (5, 0, 1)`) give `(0, 4, 0, 20)` on `a_0 = 0`.
   - **`P-873 Q3` Answered (`|V(h*)|` at the mark `(2/5, 4/5)`):** Because $\xi_{\text{up}} = \tau + 2$ gives equal leading moduli $|p B \Theta_0| = |p^{-1} B \Theta_0| = 1/2$ in rows `(0, 2)` split at $O(e^{-\pi y/6})$ by $|\Theta_1| = |\Theta_5|$ with zero diagonal splitting, while $U_{\text{down}} \to (e_0, e_1, e_2)$ at rate $|\Theta_2/\Theta_1| \sim e^{-\pi y/10}$, $|V_{\text{mark}}(h_*)|$ converges (`max entrywise error < 65/1000 at y=8, < 9/1000 at y=14, < 4/10000 at y=24`) to $\begin{pmatrix} 1/\sqrt{2} & 0 & 1/\sqrt{2} \\ 1/\sqrt{2} & 0 & 1/\sqrt{2} \\ 0 & 1 & 0 \end{pmatrix}$ (`class "other"`). All `5 / 5` planted-fault controls (`PFA2X1-1..5`) passed. `0 of 19.`
