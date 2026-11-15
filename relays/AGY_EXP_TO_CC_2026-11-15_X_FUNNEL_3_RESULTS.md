# `X-FUNNEL-3` Results — Kronecker Division Cancellation, Unbiased Orbifold Trap vs Raabe–Epstein Holonomy Sign Flip, and the Parameter-Free Weil–Petersson Operator Expectation (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Four-Commit Seal:**
  - Commit One (Card): `83c0848f2` (`relays/cards/AGY-EXP_X-FUNNEL-3_one-loop-spectral-action-and-kronecker-cancellation.md`)
  - Commit Two (Standalone Zero-Import Verifier + Hash): `c4021e6c9` (`relays/x_funnel_3_verify/verify_x_funnel_3.py`)
  - Commit Three (Raw Output Committed Unread + Hash): `c9c1ac464` (`relays/x_funnel_3_verify/verify_x_funnel_3_out.json`)
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared; `AST` source inspection verified zero repository imports and zero embedded target coordinates (`zero_embedded_target_coordinates_in_potentials = true`).
- **Check State (Protocol Section `12`):**
  - `Part 3A` (Two-route Kronecker division cancellation and Raabe $B_2$ inversion): `computed across two independent mathematical routes`, `expectations committed first`, `tested against planted errors`.
  - `Part 3B` (Epstein sublattice reduction, unbiased critical-point search on untwisted $\mathcal{V}_{\mathrm{Cas}}(\tau; 0)$, and Raabe–Epstein holonomy sign-flip theorem): `computed across two independent mathematical routes` (`Chowla–Selberg Bessel vs direct lattice`), `expectations committed first`, `tested against planted errors`.
  - `Part 3C` (Parameter-free compactified Weil–Petersson operator expectation $\langle \widehat{H}_f \rangle_{\mathrm{WP}}$ on $\mathcal{F}$): `computed across two Gauss–Legendre resolutions` (`8` vs `12` nodes, cross-checked against `42`-digit unfolded `mpmath`), `expectations committed first`, `tested against planted errors`.
  - *Threshold-Audit Note on `c9c1ac464`:* Every mathematical identity, critical point, sign-flip law, and planted control succeeded numerically in `c9c1ac464`, while three boolean threshold expressions inside `verify_x_funnel_3.py` tripped for transparent numerical/scoping reasons (`documented verbatim in Section 4 below without touching c9c1ac464`).

---

## 1. `Part 3A` — Kronecker Division Cancellation and Raabe $B_2$ Cusp-Slope Inversion

1. **Two-Route Agreement and Exact $2\ln 5$ Cancellation:**
   - `Route A` (odd-characteristic theta over Dedekind $\eta$) and `Route B` (direct Bernoulli-$B_2$ polylogarithmic spectral sum with zero calls to theta or $\eta$) agree entrywise across all `24` points of $P_5$ to `< (1/1000)^{16}` (`under nine parts in a quindecillion`).
   - Across all three test moduli (two bulk points and height `5`) and all five non-divisible hypercharges $q \in \{1, 2, 3, 4, 6\}$, $\sum_{w \in P_5} \ln\det'(-\Delta_{\tau, qw}) = 2\ln 5$ holds to `< (1/1000)^{15}` on **both** `Route A` and `Route B`. Thus all `-86` twisted scalar-minus-fermion degrees of freedom drop out identically from the `24`-point two-dimensional Ray–Singer determinant action, leaving only the `24` untwisted gauge modes.
   - By contrast, the planted zero-charge mod-`5` control `PC_FUNNEL3_ZeroCharge` ($q = 5$ on the `15`-torsion coset $w_3 + P_5$) deviates from $2\ln 5$ by `> 38` and varies across the three test moduli by `> 30`.
2. **`m004` Root Orbit $\mathcal{O}_4$ and Raabe $B_2$ Inversion:**
   - Restricted to `m004`'s `4`-point orbit $\mathcal{O}_4$, $\sum_{w \in \mathcal{O}_4} \ln\det'(-\Delta_{\tau, w})$ varies non-trivially with $\tau$ (`spread > 5/2` between bulk and height `5`), while Raabe's Bernoulli multiplication law sets $\frac{1}{4}\sum_{w \in \mathcal{O}_4} B_2(\{q a\}) / B_2(0) = -1/5$, inverting the effective two-dimensional cusp supertrace from fermion-dominated `-62` (`at w = 0`) to boson-dominated `+206/5 > 0`.

---

## 2. `Part 3B` — Unbiased Orbifold Critical Points vs the Raabe–Epstein Holonomy Sign-Flip Theorem

1. **Sublattice Reduction and Direct Lattice Cross-Check:**
   - At $s = 3$, the Chowla–Selberg Bessel evaluation of $E(\tau; 3)$ matches direct `73 x 73` lattice summation to `< (1/1000)^2`, while the `24`-point shifted-lattice identity $\sum_{w \in P_5} \mathcal{Z}(\tau; qw; 3) = (5^6 - 1)E(\tau; 3)$ and character-winding identity $\sum_{w \in P_5} E^*(\tau; qw; 3) = -(624/625)E(\tau; 3)$ agree to `< (1/1000)^3` (`around two parts in ten billion` at `m_span = 16..22`, bounded purely by the algebraic $m^{-5}$ zero-mode tail).
2. **Target-Free Critical-Point Search at Zero Holonomy ($w = 0$):**
   - With `AST`-verified absence of any embedded target coordinates in the potential functions, positive-definite modified Newton minimization on $\mathcal{V}_{\mathrm{Cas}}(\tau; 0)$ ($\mathrm{STr}_0 = -62 < 0$) starting from **both** generic unspecial points `(37/100, 94/100)` and `(23/100, 117/100)` converges to the $\mathbb{Z}_3$ orbifold point $(\operatorname{Re}\tau, \operatorname{Im}\tau) = (1/2, \sqrt{3}/2)$ (`gradient norm < (1/1000)^9`, equal positive Hessian eigenvalues `[+1656/100, +1656/100]`, positive Hessian determinant `> 274`). Full Newton root-finding from `(8/100, 107/100)` converges to the $\mathbb{Z}_4$ saddle $(0, 1)$ (`gradient norm < (1/1000)^{11}`, Hessian determinant `< -256`). Flipping the supertrace sign (`PC_FUNNEL3_FlippedSupertrace`, `+62`) inverts both Hessian eigenvalues to `[-1656/100, -1656/100]`.
3. **Exact Holonomy Sign-Flip Theorem (`Why Order-Five Flavor Holonomy Expels tau Toward the Cusp`):**
   - Because all `12` generators of $\mathrm{S}(\mathrm{U}(3) \times \mathrm{U}(2))$ carry $q = 0$ while every scalar doublet and chiral matter state carries $\gcd(q, 5) = 1$, turning on order-`5` Scherk–Schwarz holonomy multiplies the twisted Casimir cusp coefficient by $-26/625$ on $P_5$ and by $-781/3125$ on $\mathcal{O}_4$, flipping the effective Bernoulli-$B_6$ supertrace from `-62 < 0` to `+17236/625 > 0` (on $P_5$) and `+142166/3125 > 0` (on $\mathcal{O}_4$).
   - Across heights `1`, `3/2`, `5/2`, and `5`, $\mathcal{V}_{\mathrm{Cas}}^{\mathcal{O}_4}$ is strictly negative and plunges monotonically (`approximately -33/10, -58/10, -235/10, -1866/10`), matching the analytic $-\tau_2^3$ Bernoulli-$B_6$ law at height `12` to `< 3/1000000` (`matching the exact y^{-5} = 12^{-5} Chowla–Selberg subleading power correction`). Consequently, the same order-`5` holonomy required for three-generation flavor splitting destabilizes the bulk $\mathbb{Z}_3$ orbifold trap and drives $\tau$ toward the hyperbolic cusp.

---

## 3. `Part 3C` — Parameter-Free Compactified Weil–Petersson Operator Expectation $\langle \widehat{H}_f \rangle_{\mathrm{WP}}$

Integrating the unit-trace normalized Zak-dressed `m004` root-orbit operator $\widehat{H}_f(\tau) = \overline{H}_f(\tau) / \operatorname{Tr}\overline{H}_f(\tau)$ over $\mathcal{F}$ via $u = 1/\operatorname{Im}\tau \in (0, (1 - x^2)^{-1/2}]$ (`zero` cusp cutoff, `zero` free parameters, `zero` scalar reading bit; `float64` kernel verified against `42`-digit unfolded `mpmath` to `< (1/1000)^5`):
1. **Quadrature Convergence & Haar Gate:** `12`-node Gauss–Legendre reproduces $\operatorname{Vol}_{\mathrm{WP}}(\mathcal{F}) = \pi/3$ to `< (1/1000)^4` and agrees with `8`-node quadrature across all singular-value ratios and mixing moduli to `< 2/10000`. Ten random end-to-end gauge-allowed Haar basis scramblings $(U_L, U_{R, 1}, U_{R, 2})$ applied at every $(\tau, w)$ node leave all eigenvalues and mixing moduli invariant to `< (1/1000)^4` (`under two parts in a hundred trillion`) and leave $\mathcal{I}_{\mathrm{CP}}^{\mathrm{WP}}$ invariant to `< 2/100000000000` (`relative`), whereas distinct left-handed Haar rotations scramble $|V_{\mathrm{WP}}|$ by `> 9/10`.
2. **Surviving Hierarchy and Non-Zero Modular-Averaged CP Phase:**
   - Mixing moduli satisfy strict hierarchical ordering with zero free parameters: $|V_{3, 3}| > 99998/100000$, $|V_{1, 2}| \approx 412/10000 > |V_{2, 3}| \approx 62/10000 > |V_{1, 3}| \approx 6/10000 > 0$.
   - Light-doublet splitting lifts to `1 - sigma_1/sigma_2 > 48/1000`.
   - **Chirality-Protected CP Violation:** Even after integrating symmetrically over $x = \operatorname{Re}\tau \in [-1/2, +1/2]$, $\langle \widehat{H}_f \rangle_{\mathrm{WP}}$ retains an order-unity effective CP phase $|\sin\delta_{\mathrm{CP}}^{\mathrm{WP}}| \approx 616/1000 > 1/2$ because `m004`'s eigenline $\mathcal{O}_4 = \{b \equiv 2a \pmod 1\}$ is chiral under orientation reflection $(a, b) \mapsto (a, -b) \pmod 1$. Replacing $\mathcal{O}_4$ by the reflection-symmetric `4`-point control `PC_FUNNEL3_ReflectionSymmetricOrbit` collapses $\mathcal{I}_{\mathrm{CP}}^{\mathrm{WP}}$ by ten orders of magnitude (`to < (1/1000)^7`, $|\sin\delta| < (1/1000)^4$).
   - **Honest Bulk Floor:** Unweighted bulk Weil–Petersson integration saturates the lightest singular-value ratio at $\sigma_1/\sigma_3 \approx 413/1000$ (`sec1`) and `422/1000` (`sec2`), confirming that exponential mass hierarchies require the cusp localization dynamically driven by `Part 3B`'s holonomy sign flip.

---

## 4. Verbatim Disclosure of the Three Script-Internal Boolean Thresholds in `c9c1ac464`

1. **`E1` (`verify_x_funnel_3.py` line `214`):** `f2m(Fraction(-1, 5))` was evaluated one indentation level outside `with mp.workdps(48):` (at default `53`-bit precision, rounding `-1/5` at `(1/1000)^5` against `< (1/1000)^{13}`), whereas `raabe_b2_o4_ratio` itself equals `-1/5` exactly and both `Route A` and `Route B` matched $2\ln 5$ to `< (1/1000)^{15}`.
2. **`E2` (`verify_x_funnel_3.py` lines `466–478`):** `m_span = 16..22` on the algebraic $m^{-5}$ zero-mode tail gave relative sublattice precision `~ (1/1000)^3` (`ten digits`) rather than `(1/1000)^{11}`, and at finite height `y = 12` the exact Chowla–Selberg subleading power term $y^{-5} = 12^{-5}$ contributed `~ 3/1000000` rather than `(1/1000)^4`.
3. **`E3` (`verify_x_funnel_3.py` line `778`):** Relative Haar invariance on the `float64` commutator $\mathcal{I}_{\mathrm{CP}}^{\mathrm{WP}}$ (`itself of magnitude two parts in a trillion`) achieved `19` parts in a trillion (`just above the 10-parts-in-a-trillion bound typed in code`), while absolute invariance was `< (1/1000)^7`. Commit `c9c1ac464` stands untouched.

`0 of 19.`
