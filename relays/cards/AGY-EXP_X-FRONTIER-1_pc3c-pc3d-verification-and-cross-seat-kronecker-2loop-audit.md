# Card `X-FRONTIER-1` — First Blind-Sealed Verification of `physical` `P-C3c` & `P-C3d` (`ca7c2eb66`, `4e0d4c7f3`) and Cross-Seat Audit of `agy` (`e6129316e`) & `agy-002` (`94e511f54`) (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-16`
- **Context:** First sealed stage of Campaign `X-FRONTIER` (`four stages, sixteen blind-sealed commits, 0 of 19`), delivering the first repository-sealed zero-import computational verification of `physical`'s `P-C3c` (`ca7c2eb66`) and `P-C3d` (`4e0d4c7f3` on `47e6078ae`), alongside standalone mathematical counterchecks of `agy`'s `v15` Kronecker-limit / `M3` note (`e6129316e`) and `agy-002`'s `ENDGAME-V2` `2`-loop mixed-Yukawa convention (`94e511f54`).
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_frontier_1_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured Standard Model quantities read, imported, or compared (`0` float literals and `0` complex literals module-wide).

---

## 1. The Package and the Questions

1. **Question `1A` (`P-C3c` — Protected Spin Quartic & `78`-Dimensional $E_6 \subset E_8$ Colour Centralizer):**
   - After minimizing over arbitrary second-order heavy/transverse field relaxations $\beta$, does $|y|^2 / e_Q^2 \ge 2$ (`satisfied strictly by the hyperbolic collar > 14/5 > 2`) enforce $\lim_{\epsilon \to 0} V/\epsilon^4 \ge \frac{e_Q^2}{2}(|t_+|^2 + |t_-|^2)^2 + |y|^2 |A|^2 (|t_+|^2 + |t_-|^2)$?
   - Inside the `240` roots + `8` Cartan of $E_8$, does the centralizer of colour $A_2$ have `40` integer roots + `32` half-roots + `6` Cartan = `78` dimensions with $E_6$ Cartan determinant `3`, $Q$-grading $45_0 \oplus 1_0 \oplus 16_{+1} \oplus \overline{16}_{-1}$, order-`3` center $U(2\pi)$ on $E_8$, and distinct neutral-subgroup core characters $\chi_H \in \{(-1,-1), (-1,+1), (+1,-1)\}$ on the `3` state axes?
2. **Question `1B` (`P-C3d` — Classical Reflection Sector $J$, Forced Cusp Tails, & $D_5$ Cocharacter Contraction):**
   - Does $J = \operatorname{Ad}_{e^{i\pi Q}} Z_{\mathrm{phys}}$ satisfy $J^2 = +1$ on all `78` directions of $E_6$ while having **exact order `6`** on `248`-dim $E_8$, keeping charged spin, charged forms, neutral connection, and $j=3$ neutral spin modes even ($J = +1$) while projecting out the gapless neutral $Q$-spin channel ($J = -1$)?
   - Do the forced cusp-tail integrals solve $D_0 u = f$ and $P_0 \psi = f$ identically (`with Euclidean boundary kernel k/\ell`), and does $v = (-2, -1, 2, 1, 0) = -2(f_1 - f_3) - (f_2 - f_4)$ lie in the integral root lattice of $K_0 = C_{E_6}(L_\pi)^0$ (`commuting with both Q and P`)?
3. **Question `1C` (`Cross-Seat Countercheck of agy e6129316e & agy-002 94e511f54`):**
   - Does `agy`'s closed-form digamma/Hurwitz shifted-lattice Kronecker limit $F_u(\tau)$ satisfy exact modular inversion $F_{(u_2, -u_1)}(-1/\tau) = F_{(u_1, u_2)}(\tau)$ across both non-integer and integer first shifts (`matching Hurwitz-Bessel central differencing`) and confirm `u' = (-1/10, 3/10)[[3,2],[1,1]] = (0, 1/10)`?
   - Does `agy-002`'s un-transposed left-acting `- H_u H_d - (1/4) H_d H_u` term shift the noncommuting rank-`1` `2`-loop mixing coefficient from `11/2` to `7` (`while hiding on diagonal commuting scalars`)?

---

## 2. Deliverables and Definition of Done

1. **`Part 1A`:** Symbolic + `60`-digit relaxation verification of `P-C3c` `eqs. (5)–(8)` and `240`-root $E_8 \to A_2 \times E_6$ centralizer, `Z_3` center, and $\chi_H$ character table audit.
2. **`Part 1B`:** Exact `248`-root/Cartan verification of $J$ (`order 2 on E_6 vs order 6 on E_8`), symbolic forced cusp-tail ODEs, and $D_5$ cocharacter contraction inside $K_0$.
3. **`Part 1C`:** `60`-digit Kronecker-limit modular-inversion + Hurwitz–Bessel countercheck (`agy` `e6129316e`) and `60`-digit `11/2` vs `7` `2`-loop mixing countercheck (`agy-002` `94e511f54`).

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_ProtectedSpinQuartic_and_E6Centralizer_Gate` (`Part 1A`):** Symbolic quartic identity and `60`-digit heavy-relaxed residual `< (1/1000)^18`; $E_6$ counts `(40, 32, 78)`, $\det C_{E_6} = 3$, grades `(46, 16, 16)`, order-`3` center verified, and $\chi_H$ state-axis pairs equal `[[-1, -1], [-1, 1], [1, -1]]`.
2. **`E2_ReflectionInvolution_and_ForcedCuspTails_Gate` (`Part 1B`):** $J^2 = +1$ on all `78` of $E_6$, exact order `6` on `248` of $E_8$, mode parities `(+1, +1, +1, +1, -1)` on `(charged spin, charged form, Q form, j=3 spin, Q spin)`, forced tail ODE residuals `= 0`, and $(h_{\mathrm{tot}}, v_{\mathrm{root}}) = 0$ on both root summands of $v$.
3. **`E3_CrossSeat_KroneckerAndTwoLoopTranspose_Gate` (`Part 1C`):** `60`-digit modular inversion residuals `< (1/1000)^17` on both branches, Hurwitz–Bessel central-difference match `< (1/1000)^4`, `u' = (0, 1/10)` exact, and `BPV` `11/2` residual `< (1/1000)^18` vs `agy-002` un-transposed `7` mismatch `> 18/1000`.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage1_Frontier_Passed`:** `AST` check confirming zero disallowed imports, `0` float literals, and `0` complex literals module-wide.
2. **`PC_FR1_SubcriticalCollarBreaksSpinQuartic`:** Setting $|y|^2 / e_Q^2 = 1 < 2$ drops the symmetric $|t_+| = |t_-|$ quartic ratio to `1/2 < 1`, violating `eq. (8)`.
3. **`PC_FR1_FullE8AssumedInvolutionFailsOrder6`:** Applying $(I + J)/2$ on colour-triplet $E_8$ roots fails idempotency $P^2 = P$ because $J^2 = e^{\pm 2\pi i/3} \ne 1$.
4. **`PC_FR1_UnTransposedLuoXiaoShiftsMixing11Over2To7`:** Reversing $-\frac{1}{4} H_u H_d - H_d H_u \to -H_u H_d - \frac{1}{4} H_d H_u$ (`as in agy-002 Gate 0`) leaves diagonal `1x1` terms unchanged (`diff = 0`) while shifting noncommuting `2`-loop mixing from `11/2` to `7` (`rel err > 18/1000`).

`0 of 19.`
