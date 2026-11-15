# Card `X-FUNNEL-3` — Parameter-Free One-Loop Spectral Action $S_{\mathrm{eff}}(\tau)$, Kronecker Division Cancellation, the Raabe–Epstein Holonomy Sign-Flip Theorem, and the Compactified Weil–Petersson Operator Expectation (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Context:** Third sealed stage of Campaign `X-FUNNEL` (`0 of 19`, pure mathematics). Having established the magnetized triple overlap (`X-FUNNEL-1`) and the `m004` root-orbit parallel transport and torsion-order surjection laws (`X-FUNNEL-2`), this stage attacks the **modulus selection problem** directly from the parameter-free one-loop spectral action of the fixed gauge–scalar–matter bundle $\mathrm{S}(\mathrm{U}(3) \times \mathrm{U}(2)) \oplus \Lambda^{0, 1} \oplus 3\Lambda^{\mathrm{even}}$ on $E_\tau$, with **zero** target coordinates embedded (`AST-checked`).
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no script or output file in `relays/x_funnel_3_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured numbers read, imported, or compared.

---

## 1. The Package and the Questions

1. **Question `3A` (`Two-Dimensional Ray–Singer Spectral Action`):** Does the one-loop determinant $\ln\det'(-\Delta_{\tau, qw})$ of the twisted scalar and Dirac towers over $P_5$ (`or over m004's root orbit O_4`) stabilize an interior modulus $\tau^* \in \mathcal{H}$, or does an exact division identity cancel the twisted matter supertrace?
2. **Question `3B` (`Four-Dimensional Kaluza–Klein Casimir Potential and Holonomy Sign Flip`):** In the untwisted ($w = 0$) vs order-`5` Scherk–Schwarz twisted ($w \in P_5$ or $w \in \mathcal{O}_4$) four-dimensional one-loop Casimir energy density $\mathcal{V}_{\mathrm{Cas}}(\tau)$ of the fixed multiplet (`24` real vector modes at $q = 0$, `4` real scalar doublet modes at $|q| = 3$, and `90` real chiral fermionic modes across $q \in \{+1, -4, +2, -3, +6\}$), where do the critical points lie (`found numerically from generic unspecial initial moduli with zero embedded target coordinates`), and what happens to the cusp sign when order-`5` hypercharge holonomy is switched on?
3. **Question `3C` (`Parameter-Free Weil–Petersson Operator Expectation on F`):** Integrating the unit-trace normalized Zak-dressed `m004` root-orbit operator $\widehat{H}_f(\tau) = \overline{H}_f(\tau) / \operatorname{Tr}\overline{H}_f(\tau)$ over the modular fundamental domain $\mathcal{F} = \{|\operatorname{Re}\tau| \le 1/2,\; |\tau| \ge 1\}$ with the exact compactified Weil–Petersson measure $\frac{3}{\pi}\,dx\,du$ ($u = 1/\operatorname{Im}\tau$, **zero** cusp cutoff, **zero** free temperature parameter, **zero** scalar reading bit), do generation splitting, off-diagonal mixing hierarchy, and the rephasing-invariant CP phase survive modular integration, and where does unweighted bulk integration hit an honest floor?

---

## 2. Deliverables and Definition of Done

1. **`Part 3A` — Kronecker Division Cancellation (`Two Independent Routes`):**
   - Implement $\ln\det'(-\Delta_{\tau, (a, b)})$ via two independent mathematical routes (`Route A`: odd-characteristic theta over Dedekind $\eta$; `Route B`: direct Bernoulli-$B_2$ polylogarithmic spectral series with zero calls to theta or eta) and verify entrywise agreement across all `24` points of $P_5$.
   - Verify across bulk and cusp moduli and all five non-divisible hypercharges $q \in \{1, 2, 3, 4, 6\}$ that $\sum_{w \in P_5} \ln\det'(-\Delta_{\tau, qw}) = 2\ln 5$ identically (`cancelling all -86 twisted supertrace modes in the 24-point two-dimensional Ray–Singer action`), while on $\mathcal{O}_4$ verify Raabe's $B_2$ cusp-slope inversion from `-62` (`untwisted`) to `+206/5 > 0`.
2. **`Part 3B` — Epstein Sublattice Reduction, Unbiased Critical-Point Search, and the Holonomy Sign-Flip Theorem:**
   - Verify at $s = 3$ both `24`-point identities against the Chowla–Selberg Bessel expansion of $E(\tau; 3)$: shifted-lattice $\sum_{w \in P_5} \mathcal{Z}(\tau; qw; 3) = (5^6 - 1) E(\tau; 3)$ and character-winding $\sum_{w \in P_5} E^*(\tau; qw; 3) = (5^{-4} - 1) E(\tau; 3) = -(624/625) E(\tau; 3)$.
   - Enforce via Python `AST` inspection that the Casimir potential functions contain **zero** target orbifold constants, then run positive-definite modified Newton minimization from generic unspecial starting points `(37/100, 94/100)` and `(23/100, 117/100)` on $\mathcal{V}_{\mathrm{Cas}}(\tau; 0)$ (`locating the strict Z_3 minimum`) and full Newton root-finding from `(8/100, 107/100)` (`locating the Z_4 saddle`).
   - Evaluate $\mathcal{V}_{\mathrm{Cas}}^{P_5}(\tau)$ and $\mathcal{V}_{\mathrm{Cas}}^{\mathcal{O}_4}(\tau)$ across increasing heights (`1`, `3/2`, `5/2`, `5`) and verify the exact Bernoulli-$B_6$ cusp supertrace inversion (`from -62 < 0 at w = 0 to +17236/625 > 0 on P_5 and +142166/3125 > 0 on O_4`), proving that order-`5` hypercharge holonomy converts the bulk orbifold minimum into a cusp-directed runaway ($\mathcal{V}_{\mathrm{Cas}} \to -\infty$ as $\operatorname{Im}\tau \to \infty$).
3. **`Part 3C` — Exact Compactified Weil–Petersson Operator Expectation $\langle \widehat{H}_f \rangle_{\mathrm{WP}}$:**
   - Cross-check the fast `float64` mended Poisson-`erfc` kernel against `40`-digit `mpmath`, integrate $\widehat{H}_f(\tau)$ (`f in {1, 2}`) over $\mathcal{F}$ via `8`-node and `12`-node two-dimensional Gauss–Legendre quadrature in $(x, u = 1/y) \in [-1/2, 1/2] \times (0, (1 - x^2)^{-1/2}]$, and extract the converged singular-value ratios, mixing matrix $|V_{\mathrm{WP}}|$, quartic commutator $\mathcal{I}_{\mathrm{CP}}^{\mathrm{WP}}$, and rephasing-invariant phase $|\sin\delta_{\mathrm{CP}}^{\mathrm{WP}}|$.
4. **Four-Commit Seal:** Card (`Commit One`), standalone zero-import verifier + `SHA256` (`Commit Two`), unread raw output + `SHA256` (`Commit Three`), mask-clean report + status update (`Commit Four`).

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_Kronecker_Division_Cancellation` (`Part 3A`):**
   - `Route A` and `Route B` agree across all `24` points of $P_5$ to `< (1/1000)^{13}`.
   - For every $q \in \{1, 2, 3, 4, 6\}$ and across three distinct moduli $\tau$, $|\sum_{w \in P_5} \ln\det'(-\Delta_{\tau, qw}) - 2\ln 5| < (1/1000)^{13}$, while on $\mathcal{O}_4$ the four-point sum varies with $\tau$ by `> 1` between bulk and height `5`.
   - *Falsified if:* `Route A` and `Route B` disagree, or any $q \not\equiv 0 \pmod 5$ deviates from $2\ln 5$ on $P_5$.
2. **`E2_Epstein_Sublattice_and_Holonomy_SignFlip` (`Part 3B`):**
   - Both `24`-point Epstein/Eisenstein sublattice identities at $s = 3$ hold to `< (1/1000)^{11}` (`verified against direct two-dimensional lattice summation as well`).
   - From both unspecial bulk starting points `(37/100, 94/100)` and `(23/100, 117/100)`, modified Newton minimization on $\mathcal{V}_{\mathrm{Cas}}(\tau; 0)$ converges to the same interior minimum (`gradient norm < (1/1000)^8`, both Hessian eigenvalues strictly positive and equal within `< (1/1000)^6`), while Newton root-finding from `(8/100, 107/100)` converges to a strict saddle (`gradient norm < (1/1000)^8`, Hessian determinant `< -1`).
   - Switching on order-`5` hypercharge holonomy flips the Casimir potential sign on both $P_5$ and $\mathcal{O}_4$: $\mathcal{V}_{\mathrm{Cas}}^{\mathcal{O}_4}(\tau)$ is strictly negative and monotonically decreasing across heights `1`, `3/2`, `5/2`, and `5`, with asymptotic ratio $\mathcal{V}_{\mathrm{Cas}}^{\mathcal{O}_4}(x + i y) / y^3$ at $y = 12$ matching the exact Bernoulli-$B_6$ supertrace formula $-(2\zeta(6)/(2\pi^3))(142166/3125)$ to `< (1/1000)^4`.
   - *Falsified if:* untwisted minimization fails to find a positive-definite minimum, or twisted $\mathcal{V}_{\mathrm{Cas}}^{\mathcal{O}_4}(\tau)$ remains bounded from below toward the cusp.
3. **`E3_WeilPetersson_ParameterFree_Operator` (`Part 3C`):**
   - `8`-node and `12`-node Gauss–Legendre quadratures over $\mathcal{F}$ reproduce $\operatorname{Vol}_{\mathrm{WP}}(\mathcal{F}) = \pi/3$ (`12-node error < (1/1000)^4`) and agree on all singular-value ratios and mixing moduli to `< (1/1000)^3`.
   - On $\langle \widehat{H}_f \rangle_{\mathrm{WP}}$ (`12`-node): light-doublet splitting satisfies `1 - sigma_1/sigma_2 > 3/100`, mixing moduli satisfy $|V_{3, 3}| > 9999/10000$ and $1 > |V_{1, 2}| > |V_{2, 3}| > |V_{1, 3}| > 0$, the effective CP phase satisfies $|\sin\delta_{\mathrm{CP}}^{\mathrm{WP}}| > 1/2$ (`surviving x <-> -x integration because O_4 is chiral under b -> -b mod 1`), and the lightest singular-value ratio exhibits the bulk floor $\sigma_1/\sigma_3 > 3/10$.
   - *Falsified if:* Weil–Petersson quadrature fails to converge, or $x \leftrightarrow -x$ integration cancels $\mathcal{I}_{\mathrm{CP}}^{\mathrm{WP}}$ to machine zero.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_Haar_WP`:** Ten random $\tau$-independent gauge-allowed Haar basis scramblings $Y_f(\tau, w) \mapsto U_L Y_f(\tau, w) U_{R, f}^\dagger$ leave the eigenvalues, $|V_{\mathrm{WP}}|$, and $\mathcal{I}_{\mathrm{CP}}^{\mathrm{WP}}$ of $\langle \widehat{H}_f \rangle_{\mathrm{WP}}$ invariant to `< (1/1000)^4` (`< (1/1000)^{4}` relative on $\mathcal{I}_{\mathrm{CP}}^{\mathrm{WP}}$ and `< (1/1000)^{12}` absolute on spectra and $|V_{\mathrm{WP}}|$), whereas distinct left-handed Haar rotations $U_{L, 1} \neq U_{L, 2}$ scramble $|V_{\mathrm{WP}}|$ by `> 2/10`.
2. **`PC_FUNNEL3_ZeroCharge`:** Setting $q = 5 \equiv 0 \pmod 5$ breaks the Kronecker $2\ln 5$ cancellation (`diverging on P_5` or shifting a non-zero multiple of $5$ on higher torsion by a $\tau$-dependent Dedekind $\eta$ term `> 1`).
3. **`PC_FUNNEL3_FlippedSupertrace`:** Flipping the untwisted supertrace sign from fermion-dominated (`-62`) to boson-dominated (`+62`) converts the untwisted interior minimum into a strict local maximum (`both Hessian eigenvalues < 0`).
4. **`PC_FUNNEL3_ReflectionSymmetricOrbit`:** Replacing chiral $\mathcal{O}_4$ (`b == 2a mod 1`) by the reflection-symmetric `4`-point subset $\{(1/5, 2/5), (1/5, 3/5), (4/5, 2/5), (4/5, 3/5)\}$ (`invariant under b -> -b mod 1`) kills $|\mathcal{I}_{\mathrm{CP}}^{\mathrm{WP}}|$ across $x \in [-1/2, 1/2]$ to `< (1/1000)^8` (`proving that non-zero CP in <H_hat>_WP comes specifically from O_4's chirality!`).

`0 of 19.`
