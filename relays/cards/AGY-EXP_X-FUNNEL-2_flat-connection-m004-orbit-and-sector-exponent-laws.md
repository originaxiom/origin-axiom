# Card `X-FUNNEL-2` — The $\Gamma(5)$ Holonomy Obstruction on $X(1)$, Root-Orbit Parallel Transport and Twin-Even Commutator Asymmetry on `m004`, $\mathrm{SU}(3)$ Casimir Shift Test, and Universal Cusp-Exponent Laws at Orders Five, Ten, Fifteen, and Thirty (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Context:** Second sealed stage of Campaign `X-FUNNEL` (`0 of 19`, pure mathematics). It directly addresses `B1945` Section `6` and `P-860 (a)/(b)` (flat unitary connections over torsion points), `P-856` (`the hand` and twin cancellation vs reinforcement), and `P-862` Step Two (data-free derivation of universal inter-sector exponent and spectrum laws at higher torsion orders `10`, `15`, and `30`), while also executing the pre-registered regression gate fixing `X-FUNNEL-1`'s linear Poisson cutoff at small imaginary part.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no script or output file in `relays/x_funnel_2_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured numbers read, imported, or compared.

---

## 1. The Package and the Questions

1. **Question `2A` (`B1945` Section `6`, `P-860 (a)/(b)`, and `P-856`):** Does any $\tau$-independent flat unitary connection over all twenty-four order-five points exist on the modular curve $X(1) = \mathcal{H}/\mathrm{SL}(2, \mathbb{Z})$, and how does restricting to the root `m004`'s own monodromy eigenline (`B1943`'s four-point orbit) affect coherent left-handed Hermitian transport, light-doublet splitting, and the orientation-odd quartic commutator invariant across `Pin(2)` twins?
2. **Question `2B` (`P-862` Step Two and Intra-Order vs Higher-Order Separation):** Can an $\mathrm{SL}(2, \mathbb{Z})$-invariant $\mathrm{SU}(3)$ Casimir shift in the scalar resolvent skew consecutive mass ratios in opposite directions at order five, and what exact universal relations govern the second and third charged sectors at torsion orders `5`, `10`, `15`, and `30` in both Frame C and the magnetized triple overlap?

---

## 2. Deliverables and Definition of Done

1. **`Regression Gate R0` (Linear Poisson Dual-Cutoff Verification):**
   - Implement the exact linear `erfc` dual-sum bound $l_{\max}(n_a) = \max(\lceil \text{thresh}/(2\pi \tau_2 |n_a|)\rceil + 4, l_{\mathrm{quad}})$ and verify that $S$-covariance at $\tau = 13/100 + (17/10)i$ (`where Im(-1/tau) < 3/5`) holds to `< (1/1000)^{14}`, matching the unfolded Gaussian sum entrywise to `< (1/1000)^{12}`.
2. **`Part 2A` — $\Gamma(5)$ Obstruction on $X(1)$ vs `m004` Root-Orbit Transport and Twin-Even Quartic Commutator:**
   - Verify explicitly under $T^5 \in \Gamma(5)$ (`which fixes all twenty-four points of P_5 mod Z^2`) that the fiber holonomy between $\tau + 5$ and $\tau$ at fixed reduced $w = (p/5, q/5) \in P_5$ varies non-trivially across $p \in \{0, 1, 2, 3, 4\}$ in **both** Frame C and the magnetized triple overlap, obstructing any $\tau$-independent flat unitary connection on $X(1)$.
   - Verify directly from `m004`'s monodromy $M = L R = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ and tick $J = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ (`J^2 = M`) that $(M + I_2) w \equiv 0 \pmod 1$ uniquely selects `B1943`'s four-point orbit $\mathcal{O}_4 = \{(1/5, 2/5), (2/5, 4/5), (4/5, 3/5), (3/5, 1/5)\}$ as a single transitive $J^{-1}$-cycle (`while P_5 \ O_4 splits into two length-ten M-orbits`).
   - Evaluate the gauge-invariant quartic commutator trace $\mathcal{I}_{\mathrm{CP}}(\tau, w) = \frac{1}{6}\operatorname{Im}\operatorname{Tr}([H_1(\tau, w), H_2(\tau, w)]^3)$ (`H_f = Y_f Y_f^\dagger`) on $\mathcal{O}_4$, testing its `Pin(2)` twin parity under $w \mapsto -w \equiv M^{-1} w \pmod 1$ vs its fiber-orientation parity under $(\tau, a, b) \mapsto (-\bar{\tau}, a, -b)$, plus Zak-dressed left-handed Hermitian orbit summation $\overline{H}_f(\tau) = \frac{1}{4}\sum_{w \in \mathcal{O}_4} \widetilde{H}_f(\tau, w)$.
3. **`Part 2B` — $\mathrm{SU}(3)$ Casimir Shift Test and Universal Cusp-Exponent & Order-`15` Surjection Laws (`P-862` Step Two):**
   - Test the $\mathrm{SL}(2, \mathbb{Z})$-covariant $\mathrm{SU}(3)$ Casimir shift $M_{\mathrm{Cas}}^2 = 4/3$ (on $p \in \{1, 2\}$) vs $0$ (on $p \in \{0, 3\}$) in $(-\frac{1}{4\pi^2}\Delta_{\tau, A_H}^{\mathrm{conf}} + M_{\mathrm{Cas}}^2)^{-1}$ for both modular covariance and consecutive-ratio ordering.
   - Prove and verify numerically across **all `192` primitive order-`15` points** $w_{15} = w_3 + w_5$ (`w_3 in E_tau[3] \ {0}, w_5 in P_5`) the **Order-Three Blindness and Order-Fifteen Surjection Theorem**: in both Frame C and the magnetized triple overlap, the third charged sector's singular-value ratios at $w_{15}$ equal the second charged sector's singular-value ratios at $w_5$ at **every** bulk modulus $\tau \in \mathcal{H}$, while the second charged sector at $w_{15}$ splits strictly away from $w_5$.
   - Compute the exact cusp-exponent tables (`P-862` Step Two) across all primitive torsion points of orders `5` (`24` points), `10` (`72` points), `15` (`192` points), and `30` (`576` points) in Frame C (`cross-checked against high-height mpmath`) and on representative primitive points of orders `5`, `10`, `15`, and `30` in the magnetized triple overlap.
4. **Four-Commit Seal:** Card (`Commit One`), standalone zero-import verifier + `SHA256` (`Commit Two`), unread raw output + `SHA256` (`Commit Three`), mask-clean report + status update (`Commit Four`).

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E0_S_Covariance_Fix`:** Mended `y_mag_poisson_fixed` satisfies $S$-covariance at $\tau = 13/100 + (17/10)i$ to `< (1/1000)^{14}` and matches the unfolded Gaussian lattice sum at both $\tau$ and $-1/\tau$ to `< (1/1000)^{12}`. *Falsified if:* residual exceeds `(1/1000)^{12}`.
2. **`E1_Gamma5_Obstruction_and_m004_CP` (`Part 2A`):**
   - Under $\tau \to \tau + 5$ at fixed reduced $w \in P_5$, the fiber transformation depends non-trivially on $5a \pmod 5$ in Frame C and on $5a \pmod 3$ in magnetized level three (`inter-point holonomy spread > 1/2`), moving the naive twenty-four-point coherent sum's singular-value ratios by `> 1/20`.
   - On $\mathcal{O}_4$ at $\tau = 13/100 + (17/10)i$, $|\mathcal{I}_{\mathrm{CP}}(\tau, w)| > 1/1000$ at all four points, $\mathcal{I}_{\mathrm{CP}}(\tau, -w) = +\mathcal{I}_{\mathrm{CP}}(\tau, w)$ to `< (1/1000)^{14}` (`twins reinforce rather than cancel`), and $\mathcal{I}_{\mathrm{CP}}(-\bar{\tau}, a, -b) = -\mathcal{I}_{\mathrm{CP}}(\tau, a, b)$ to `< (1/1000)^{14}` (`orientation-odd`). On the Zak-dressed orbit Hermitian sum $\overline{H}_f(\tau)$, $b \to b + 1$ periodicity holds entrywise to `< (1/1000)^{14}`, and at height `30` (`Re tau = 13/100`) the light-doublet degeneracy at $a \in \{2/5, 3/5\}$ is lifted (`1 - sigma_1/sigma_2 > (1/1000)^3`, and `> 1/10` in the bulk) while $|(Q_1^\dagger Q_2)_{3, 3}| > 1 - (1/1000)^4$.
   - *Falsified if:* $\Gamma(5)$ holonomy is $w$-independent, or $\mathcal{I}_{\mathrm{CP}}$ vanishes or cancels between $+w$ and $-w$, or $\overline{H}_f$ fails $b \to b + 1$ periodicity.
3. **`E2_Casimir_PartialKill` (`Part 2B`):**
   - $M_{\mathrm{Cas}}^2 = 4/3$ preserves exact $T$ and $S$ covariance to `< (1/1000)^{14}` and gives $(\sigma_2/\sigma_3)_{\mathrm{sec3}} > (\sigma_2/\sigma_3)_{\mathrm{sec2}}$ across all four points of $\mathcal{O}_4$, **but fails opposite-direction skewing** because $(\sigma_1/\sigma_2)_{\mathrm{sec3}} > (\sigma_1/\sigma_2)_{\mathrm{sec2}}$ as well (`honest partial-kill of a pure scalar Casimir mass shift`).
   - *Falsified if:* $M_{\mathrm{Cas}}^2 = 4/3$ breaks $\mathrm{SL}(2, \mathbb{Z})$ covariance.
4. **`E3_Order15_Surjection_and_P862_Exponents` (`Part 2B`):**
   - Across all `192` primitive order-`15` points $w_{15} = w_3 + w_5$ at bulk $\tau$, `sec3(w_15)` matches `sec2(w_5)` in singular-value ratios to `< (1/1000)^{14}` in **both** Frame C and the magnetized triple overlap, while `sec2(w_15)` differs from `sec2(w_5)` by `> 1/10`.
   - In Frame C (`B1788` tropical law, verified against `mpmath` at heights `20` and `30`): at order `10` (`72` points), $e_{23, \mathrm{sec3}}(w) = e_{23, \mathrm{sec2}}(w) \in \{1/5, 1/2\}$ identically at all `72` points; at orders `15` (`192` points) and `30` (`576` points), $\min e_{23, \mathrm{sec2}} = 2/15 < \min e_{23, \mathrm{sec3}} = 1/5$.
   - In the magnetized triple overlap: `sec2` and `sec3` already split on $e_{23}$ at order `10` (`by > 1/20` at `(1/10, 1/5)`), and at `(2/15, 4/15)` (`order 15`) consecutive exponents skew in opposite directions ($e_{23, \mathrm{sec2}} < e_{23, \mathrm{sec3}}$ while $e_{12, \mathrm{sec2}} > e_{12, \mathrm{sec3}}$).
   - *Falsified if:* any of the `192` order-`15` points violates the $w_5$-surjection identity, or Frame C's order-`10` / order-`15` exponent laws fail against `mpmath`.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_Haar_CP`:** Ten random gauge-allowed $\mathrm{U}(3)_L \times \mathrm{U}(3)_{R, 1} \times \mathrm{U}(3)_{R, 2}$ scramblings leave $\mathcal{I}_{\mathrm{CP}}$ invariant to `< (1/1000)^{14}`, whereas distinct left-handed Haar unitaries $U_{L, 1} \neq U_{L, 2}$ alter $\mathcal{I}_{\mathrm{CP}}$ by `> 1/1000`.
2. **`PC_FUNNEL2_WrongOrbit`:** Replacing $\mathcal{O}_4$ by a non-eigenline four-point subset fails closure under `m004`'s tick $J^{-1}$ and monodromy $M^{-1} w \equiv -w \pmod 1$.
3. **`PC_FUNNEL2_NotDivBy3`:** Perturbing `sec3`'s charges from `(-3, 6)` to `(-2, 5)` (`preserving q_L + q_R = +3, breaking divisibility by 3`) breaks order-`3` blindness at `(2/15, 4/15)` vs `(2/5, 4/5)` by `> 1/10`.

`0 of 19.`
