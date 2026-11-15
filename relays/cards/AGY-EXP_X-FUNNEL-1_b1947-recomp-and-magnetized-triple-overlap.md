# Card `X-FUNNEL-1` — Cross-Family Recomputation of `B1947` and `P-861` Norm Extension, Plus the Punctured-Torus Magnetized Bigraded Triple Overlap (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Context:** Self-initiated pure-mathematics card opening the four-stage `X-FUNNEL` campaign after `M31`, `B1945`, `B1946`, `B1947`, `W-B2` (harvest rows `1840` to `1842`), and `P-861`. It performs two coupled pure-mathematics tasks without touching any empirical quantity: first, an independent cross-family recomputation of `B1947` from `CARD.md` alone together with `P-861`'s owed check on whether `W-B2` Stage Three's residue identity extends to the exact Theorem Ninety channel norms; second, an analytic derivation and three-route extended-precision verification of the genuine magnetized zero-mode triple overlap on the once-punctured torus coupled to the bigraded exterior algebra $\Lambda^{p, q}(V_3^+ \oplus V_2^-)$.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no verification script or output file for `X-FUNNEL-1` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured numbers read, imported, or compared.

---

## 1. The Package and the Question

Can a charge-conserving triple overlap on the once-punctured torus $(E_\tau^\times, \tilde{L}_2)$ — in which chiral matter lives in magnetic generation bundles of degree plus three and minus three on $\Lambda^{\mathrm{even}}(V_3^+ \oplus V_2^-)$ while the scalar doublet in $\Lambda^{0, 1}$ carries zero magnetic flux and flat hypercharge holonomy $q_H = -(q_L + q_R)$ sourced at the puncture — eliminate the discrete scalar reading bit, preserve full $\mathrm{SL}(2, \mathbb{Z})$ modular covariance and torsion-lattice gauge invariance, and align the heaviest generation across all twenty-four order-five points high in the cusp?

---

## 2. Deliverables and Definition of Done

1. **`Part 1A` — Cross-Family Recomputation of `B1947` and `P-861`'s Owed Channel-Norm Check (Zero Imports from `main` or Other Relays):**
   - Recompute `B1947`'s `C0`, `C1` (relative component phase between opposite scalar twists `+3` and `-3`), and `C2` ($\tau \to \tau + 1$ covariance failure of both `(q_H a, 2 q_H b)` and `D1'` `(q_H a, q_H b)` twisted-triplet constructions across both half-integer characteristic representatives) directly from `B1947/CARD.md` without reading `B1947/verification/d1_coupling.py`.
   - Test `P-861`'s owed question on `W-B2` Stage Three: whether shifting the kernel's Szegő zero alone by $h = c q_H w$ at $c \in \{-2, +2\}$ matches Frame C at shifted charges $q' = q - c q_H / 2$ not only at residue level $R_s$, but also on the full Theorem Ninety channel-weighted coupling matrices $Y_f$ (including `F_u` and the constant term $a_0$).
2. **`Part 1B` — Punctured-Torus Magnetized $(p, q)$-Bigraded Triple Overlap:**
   - Construct from scratch the triple overlap on $E_\tau^\times = E_\tau \setminus \{0\}$ with the unique $\mathrm{SL}(2, \mathbb{Z})$-invariant odd spin structure $(1/2, 1/2)$:
     - Left-handed doublets carry magnetic flux $+3$ and flat twist $q_L w$; conjugate right-handed singlets carry magnetic flux $-3$ and flat twist $q_R w$; the scalar doublet in $\Lambda^{0, 1}$ carries magnetic flux $0$ and flat twist $q_H w$ with $q_L + q_R + q_H = 0$ (`+3` via exterior wedge in the first charged sector, `-3` via interior contraction in the second and third charged sectors), sourced at the puncture by the modular-invariant flat conformal Laplacian resolvent $(-\Delta_{\tau, A_H})^{-1} \delta_0(z)$.
   - Verify exact agreement across three independent evaluation routes (`two-dimensional spectral quadrature on the fundamental parallelogram`, `direct unfolded Gaussian lattice summation`, and `fast Poisson-resummed complementary-error-function summation`), full $\mathrm{SL}(2, \mathbb{Z})$ covariance ($T$ and $S$), torsion-lattice gauge invariance ($a \to a + 1$, $b \to b + 1$), Haar unitary basis-scrambling invariance, deep-cusp alignment across all twenty-four order-five points at heights `6` and `30`, bulk off-diagonal hierarchy ordering, and persistence of `B1934`'s order-five transposition law between the second and third charged sectors.
3. **Four-Commit Seal:**
   - Commit One: this card.
   - Commit Two: standalone zero-import verification script `relays/x_funnel_1_verify/verify_x_funnel_1.py` and `SCRIPT_SHA256.txt`.
   - Commit Three: raw output `relays/x_funnel_1_verify/verify_x_funnel_1_out.json` and `OUTPUT_SHA256.txt` committed unread.
   - Commit Four: mask-clean mathematical report `relays/AGY_EXP_TO_CC_2026-11-15_X_FUNNEL_1_RESULTS.md` and updated `relays/STATUS_AGY-EXP.md`.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_B1947` (`Part 1A`):**
   - `C0` agrees with untwisted Serre components to better than one part in a quadrillion; `C1` exhibits the non-scalar component-dependent phase factor $\exp(\pm 6\pi i a)$ between $q_H = +3$ and $q_H = -3$; `C2` fails $\tau \to \tau + 1$ covariance by an order-unity discrepancy (exceeding `1/10`) in both `(q_H a, 2 q_H b)` and `(q_H a, q_H b)` conventions and for both characteristic representatives, while the untwisted Frame C control holds to `< 1/1000000000000`.
   - On `P-861`'s owed question, because both `F_u` and $|a_0|^2$ depend only on the sum characteristic $((q_L + q_R)a, (q_L + q_R)b)$ and are even under simultaneous sign reversal $(\alpha, \beta) \mapsto (-\alpha, -\beta)$, `W-B2`'s identity $E$ at $c = -2$ and $c = +2$ extends identically from the residues $R_s$ to the full Theorem Ninety channel-weighted matrices (modulo an overall sign on $Y$, leaving all singular-value ratios and unitary overlap moduli identical to better than one part in a trillion).
   - *Falsified if:* Any twisted-triplet variant in `B1947` passes $\tau \to \tau + 1$ covariance, or `W-B2`'s Theorem Ninety channel norms fail to satisfy identity $E$ at $c = \pm 2$.
2. **`E2_Covariance_and_Quadrature` (`Part 1B`):**
   - In the punctured-torus magnetized triple overlap with spin structure $(1/2, 1/2)$, two-dimensional numerical quadrature, direct Gaussian lattice summation, and Poisson-resummed evaluation agree entrywise to better than one part in a trillion; singular-value ratios and all nine entries of the unitary overlap modulus matrix $|U_1^\dagger U_2|$ are invariant under $T: (\tau, a, b) \mapsto (\tau + 1, a, b - a)$, $S: (\tau, a, b) \mapsto (-1/\tau, -b, a)$, $a \to a + 1$, and $b \to b + 1$ to better than one part in a trillion.
   - *Falsified if:* Any modular or lattice transformation moves any singular-value ratio or unitary overlap modulus by more than one part in a trillion.
3. **`E3_Cusp_Alignment_and_Order5_Law` (`Part 1B`):**
   - With zero scalar reading bit chosen, at height `30` (`Re tau = 13/100`), the heaviest-generation overlap modulus $|(U_1^\dagger U_2)_{3, 3}|$ exceeds `98/100` across **all twenty-four** order-five points, and exceeds `9999/10000` across **all twenty** points with $a \neq 0$ (including all four points of the root's frustrated orbit from `B1943`), while in the bulk (`Im tau = 17/10` at `(1/5, 2/5)`) the off-diagonal moduli satisfy the strict ordering $1 > |V_{1,2}| > |V_{2,3}| > |V_{1,3}| > 0$.
   - At order five, `B1934`'s transposition law persists even in the magnetized degree-three overlap: the third charged sector `(-3, 6)` has identical singular-value ratios to the second charged sector `(1, 2)` at every order-five point because shifting $q a$ by an integer multiple of $5a \in \mathbb{Z}$ acts as a unitary cyclic permutation of the three Landau zero modes.
   - *Falsified if:* $|(U_1^\dagger U_2)_{3, 3}|$ falls below `98/100` at any order-five point at height `30`, or bulk off-diagonal ordering collapses to $I_3$ or a permutation, or the order-five transposition identity fails.

---

## 4. Dependencies and Firewall Scope

- **Rests on:** `B1934` (`3 + 2` Weil split and mod-five charge law), `B1940` / `B1945` / `B1946` / `B1947` (`CARD.md` statement only), `B1943` (`4`-point frustrated orbit), and standard elliptic / Landau zero-mode theory on $(E_\tau^\times, \text{spin }(1/2, 1/2))$.
- **Must not touch:** Any of the nineteen empirical target numbers (`B1612`, `B1637`, `B1720`, or any measured value), and `B1947/verification/d1_coupling.py` (kept unread so `Part 1A` is a pure statement-only cross-family check).

---

## 5. Mandatory Controls That Must Fail When Broken

1. **`Gate_Haar` (Unitary Gauge-Basis Scrambling Gate):** Apply random common left-handed $\mathrm{U}(3)$ Haar transformations $U_L$ and independent random right-handed $\mathrm{U}(3)$ Haar transformations $U_{R, 1}, U_{R, 2}$ (`Y_1 -> U_L Y_1 U_{R, 1}^\dagger`, `Y_2 -> U_L Y_2 U_{R, 2}^\dagger`); assert all singular-value ratios and all nine entries of $|U_1^\dagger U_2|$ are invariant to better than one part in a trillion, while applying **distinct** left-handed Haar matrices $U_{L, 1} \neq U_{L, 2}$ scrambles $|U_1^\dagger U_2|$ by order unity (planted gauge-breaking control).
2. **`PC_FUNNEL1_Spin` (Planted Wrong Spin Structure `(0, 0)` Control):** Replacing the unique $\mathrm{SL}(2, \mathbb{Z})$-invariant odd spin structure $(1/2, 1/2)$ by the even spin structure $(0, 0)$ for odd magnetic degree three must break $T: (\tau, a, b) \mapsto (\tau + 1, a, b - a)$ covariance by more than `1/100` because $3m^2 \equiv m \pmod 2$ induces a half-characteristic shift.
3. **`PC_FUNNEL1_ChargeBreak` (Planted Charge-Non-Conserving Scalar Twist Control):** Perturbing $q_H$ from $-(q_L + q_R)$ to $-(q_L + q_R) + 1$ breaks double periodicity on $E_\tau$ (`|p(x, y + 1) - p(x, y)| > 1/10`) and destroys lattice gauge invariance under $a \to a + 1$.

---

## 6. Needs from `main` or Other Seats

- Nothing required to execute. Delivered under the four-commit seal on `agy/self-consistent-loop-2026-11-11`.

`0 of 19.`
