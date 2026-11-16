# Card `X-CLOSURE-2` — First Standalone Verification of `physical` `P-C3b` Proofs `1–3` (`bc729239d`: Orthogonal Reduction, Half-Root Spin/Form Modes, and Spin-Line Triplet Inclusion, `0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-16`
- **Context:** Second sealed stage of Campaign `X-CLOSURE` (`four stages, sixteen blind-sealed commits, 0 of 19`), delivering the first independent zero-import computational verification of `physical`'s three hand-derived state-orbit proofs (`bc729239d` on `e250dab15`), explicitly scoped to the finite fibre, radial cusp-exponent, and `2O` representation identities while keeping infinite-dimensional `PDE` graph-closure duties visibly separated.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_closure_2_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured Standard Model quantities read, imported, or compared (`0` float literals module-wide).

---

## 1. The Package and the Questions

1. **Question `2A` (`Proof 1` — `PARALLEL_BACKGROUND_ORTHOGONAL_REDUCTION`):**
   - Do the degreewise maps $J_0, J_1, J_2, J_3$ reproduce the four source kinetic densities $(\Omega^2;\, (\frac{1}{2}, \Omega, \Omega);\, (\Omega^{-1}, \Omega^{-1}, 2);\, 2\Omega^{-2})$ and satisfy $J_{n+1} D_n = \sqrt{2}\, d_n J_n$ identically for $n \in \{0, 1, 2\}$?
   - On the parallel balanced pair $\widehat{\Phi}_0 = \frac{1}{2\sqrt{2}\ell}(E_+ + E_-,\, E_+ - E_-)$ with $A_{\mathrm{spin}} = s_{\mathrm{conn}} H / 2$, do $\nabla\widehat{\Phi}_0 = 0$ and the mixed Dolbeault–algebraic anticommutators vanish identically, and on the `16`-dimensional $V_{3/2} \otimes V_{3/2}$ half-root fibre block does $\ker\Delta_\delta$ have exact dimensions `(1, 2, 1)` across degrees `(0, 1, 2)` with positive complement gap $c_\delta > 0$ and exact norm identity `eq. (8)`?
2. **Question `2B` (`Proof 2` — `CORRELATED_ORBITS_AND_DIRECT_ZERO_MODES`):**
   - Does the binary octahedral register $2O$ (`order 48`) intersect $\mathrm{Pin}_{2,x}$ in a subgroup $D$ of order `16`, partitioning the `12` spin/state pairs into `3` odd (`p = 0`), `3` aligned (`spin = state`), and `6` misaligned (`spin != state`, stabilizer order `8`) classes?
   - Does the `5`-component torus weight pairing yield $\alpha_+ = -1$, $\alpha_- = +1$ (`reversing both under Zeta`), `1` pure-spin line per colour-singlet charge on odd/aligned seeds vs `0` on misaligned/triplet/bare-lift cases, `2` form modes (`pole order n <= 2`) and `0` gaugino modes (`vanishing order >= 2`), totaling `18` modes on coherent odd/aligned vs `16` on misaligned across the `8` half-root blocks?
3. **Question `2C` (`Proof 3` — `PHYSICAL_SPIN_MODE_TRIPLET_AND_RETAINED_LINE`):**
   - Does $\operatorname{Ind}_D^{2O} \chi_{\mathrm{aligned}} \cong \sigma \otimes O$ produce the exact $3 \times 3$ generator matrices $A_L, A_R$ and distinct inner parity characters (`vs 1 + 2 reducible splitting on \sigma \otimes \Pi for odd spin`), with $\mu^4 = \sigma(g_e)$ yielding $U_{\mathrm{aligned}} = j \mu^4 O$ (`L^4 = +I_3` vs native $T_+$ `L^4 = -I_3`) and retaining the central sheet (`epsilon -> -I_3, J_c -> +I_3, Delta^4 -> -I_3`)?

---

## 2. Deliverables and Definition of Done

1. **`Part 2A`:** `60`-digit + exact `SymPy` verification of `eqs. (1)–(8)` of `PARALLEL_BACKGROUND_ORTHOGONAL_REDUCTION` on the `16`-dimensional $V_{3/2} \otimes V_{3/2}$ block (`including finite Fourier-mode check of ||M x||^2 >= 2 c_delta ||x||^2 on (ker Delta_delta)^perp`).
2. **`Part 2B`:** Exact group-theoretic, weight-pairing, and radial cusp-integrability verification of `CORRELATED_ORBITS_AND_DIRECT_ZERO_MODES` (`3 + 3 + 6` orbit split, $\alpha_\pm = \mp 1$, `18` vs `16` total half-root zero modes).
3. **`Part 2C`:** Explicit `48`-element $2O$ induced-module verification of `PHYSICAL_SPIN_MODE_TRIPLET_AND_RETAINED_LINE` (`U_aligned = j mu^4 O` vs `U_odd = j mu^4 Pi` vs native `T_+ = mu O`).

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_OrthogonalReduction_and_HalfRootGap_Gate` (`Part 2A`):** `J` metric ratios and $J_{n+1} D_n - \sqrt{2}\, d_n J_n$ vanish symbolically (`exact 0`); parallel $\nabla\widehat{\Phi}_0 = 0$ and mixed anticommutator $= 0$; $\dim\ker\Delta_{\delta, k} = (1, 2, 1)$ for $k = (0, 1, 2)$; norm identity `eq. (8)` residual `< (1/1000)^18`; and $c_\delta > 0$ with $\|M x\|^2 \ge 2 c_\delta \|x\|^2$ across all tested Fourier modes on $(\ker\Delta_\delta)^\perp$.
2. **`E2_CorrelatedOrbits_and_DirectZeroModes_Gate` (`Part 2B`):** $|2O| = 48$, $|D| = 16$, orbit counts `(3, 3, 6)`; exact torus phases $\alpha_+ = -1, \alpha_- = +1$; pure-spin counts `(1, 1, 0, 0, 0)` on `(odd, aligned, misaligned, colour-triplet, bare-lift)`; and total `128` half-root kernel dimensions `(18, 18, 16)` on `(odd, aligned, misaligned)`.
3. **`E3_InducedSpinTriplet_and_ScalarLine_Gate` (`Part 2C`):** $\chi_{\mathrm{aligned}}(r, s) = (-1, -1)$ for both coherent signs, $\chi_{\mathrm{odd}}(r, s) = (-1, +1)$; induced matrices match `eq. (6)` with inner parities `(1, -1, -1)` and `(-1, 1, -1)`; $\mu^4 = \sigma$ on all generators; $U_{\mathrm{aligned}}(L^4) = +I_3 \ne T_+(L^4) = -I_3$; and central sheet signs `(-1, +1, -1)` hold on `(\epsilon, J_c, \Delta^4)`.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage2_Closure_Passed`:** `AST` check confirming zero disallowed imports, `0` float literals, and `0` complex literals module-wide.
2. **`PC_CL2_NonparallelHiggsAndWrongConnectionNorm`:** Changing $A_{\mathrm{spin}} = s_{\mathrm{conn}} H / 2$ away from $1/2$ breaks $\nabla\widehat{\Phi}_0 = 0$, and spatially varying $\widehat{\Phi}$ produces a nonzero mixed anticommutator `> 1/10`.
3. **`PC_CL2_MisalignedAndColourTripletZeroSpinCount`:** Unequal spin signs $\eta(a) \ne \eta(b)$ (`misaligned`) or nontrivial order-`3` colour character $\chi_3$ force pure-spin zero-mode count `= 0`.
4. **`PC_CL2_NativeTripletAndErasedCentralSheetControls`:** Replacing $U_{\mathrm{aligned}} = j\mu^4 O$ by native $T_+ = \mu O$ flips $L^4$ from $+I_3$ to $-I_3$ (`Frobenius mismatch > 3`), and erasing $j_\epsilon = -1$ corrupts $\Delta^4 = \epsilon J_c$.

`0 of 19.`
