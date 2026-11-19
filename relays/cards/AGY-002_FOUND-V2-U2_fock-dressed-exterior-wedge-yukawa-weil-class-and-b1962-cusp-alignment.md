# Card `AGY-002_FOUND-V2-U2` — Fock-Dressed `SL_2(Z)`-Covariant Exterior-Wedge `Yukawa` Operator, `P-874(1,2)`, & Passing `B1962`/`B1963`'s Cusp + Lepton-Down Gate (`0 of 19`)

## 1. Package and Question

Joining `B1953`'s `15 x 15` `SL_2(Z)`-covariant operator `O_m(tau) = sum_{w != 0} zeta_5^{-a b} Y_{(1,2)}(tau, w) (x) D_m(w)` (`O_3 (+) O_2` on `C^3_fam (x) W_5`) functorially to the Fock exterior-wedge matter representations of `Gate F-U1` (`Lambda^{even}(W_5)`) to answer `P-874(1)`/`W-P1b`, `P-874(2)`/`W-L1`, `B1949`, `B1953`, and `B1962`/`B1963` (`0 of 19`):

1. **`P-874(1) / W-P1b` `Weil`-Class Separation Theorem (`m = 1` vs `m = 3`):**
   - Construct `O_m(tau)` at `tau_0 = 13/100 + 17/10 i` and `tau_1 = 31/100 + 6/5 i` (`45` digits) using centered torsion representatives `a_c, b_c in {-2, -1, 0, 1, 2}` (`w_L = (a_c/5, b_c/5), w_R = (2 a_c/5, 2 b_c/5)`) for both `Weil` classes (`m = 1` for `2 x^2 / 5`, `m = 3` for `x^2 / 5`).
   - Verify for both `m = 1` and `m = 3`: off-diagonal `3 <-> 2` block norm `< (1/10)^25`, `15`-singular-value `T`-drift (`tau -> tau + 1`) and scaled `S`-drift (`tau -> -1/tau`) `< (1/10)^20`, and prove that `G_{3,L}` and `G_{2,L}` normalized square-root eigenvalue ratios differ between `m = 1` and `m = 3` by `> 1/20` on `G_{3,L}` and `> 1/4` on `G_{2,L}` at both bulk moduli.
2. **Functorial Fock Kinetic Dressing on `Lambda^{even}(W_5)` & Passing `B1962`/`B1963`'s Cusp + Lepton-Down Gate (`P-861`, `B1949`):**
   - From the `Gate F-U1` Fock bidegrees `Q_L(1,1)`, `u_R^c(2,0)`, `d_R^c(2,2)`, `L_L(3,1)`, `e_R^c(0,2)` on `Lambda^{p3}(W_3^+) (x) Lambda^{p2}(W_2^-)`, define covariant Kähler kinetic metrics `K_{Q_L} = G_{3,L} + G_{2,L}`, `K_{L_L} = 3 G_{3,L} + G_{2,L}`, `K_{u_R^c} = 2 G_{3,R}`, `K_{d_R^c} = 2 G_{3,R} + 2 G_{2,R}`, `K_{e_R^c} = 2 G_{2,R}` and physical `Yukawa` matrices `Y_f^{phys} = K_{L,f}^{-1/2} Y_{hol} K_{R,f}^{-1/2}` for both `Y_{base}(tau) = Y(tau, 0)` and `S_{ph}(tau) = sum_{w != 0} zeta_5^{-ab} Y_{(1,2)}(tau, w)` (`zero 25th roots`).
   - Verify at `tau_0 = 13/100 + 17/10 i` (`45` digits): exact `T` and `S` invariance of `r_u, r_d, r_e` and `|V_{CKM}|` `< (1/10)^20`; `10`-trial independent random `Haar SU(3)^5` basis-scrambling invariance `< (1/10)^25` (`Guardrail 3`); parameter-free lepton-down separation `|r_{e,23} - r_{d,23}| > 1/2` in both `base_w0` and `phased_sum`.
   - Verify at cusp `y = 6` (`tau = 13/100 + 6 i`, `85` digits, both readings `S` and `tilde_S`): `min_i |V_{ii}| > 999/1000` and `|r_{e,23} / r_{d,23} - 1| > 1/5` in both `base_w0` and `phased_sum`.
   - Verify at cusp `y = 30` (`tau = 13/100 + 30 i`, `180` digits, both readings `S` and `tilde_S`): `1 - min_i |V_{ii}| < (1/10)^12` in both readings, `|r_{e,23} / r_{d,23} - 1| > 3/5` in `S`, and `|r_{e,13} / r_{d,13} - 1| > 3/10` in `tilde_S`.
3. **`P-874(2) / W-L1` Symmetric-Point Forced Null Mode (`tau = i` and `tau = rho`):**
   - At `tau = i` and `tau = rho = -1/2 + i sqrt(3)/2` (`50` digits), verify `sigma_3 / sigma_1 < (1/10)^30` on `S_{ph}`, `Y_{base}`, and all `3` Fock-dressed sectors `Y_u^{phys}, Y_d^{phys}, Y_e^{phys}`, while `sigma_2 / sigma_1` separates leptons from down quarks (`|r_{d,23} - r_{e,23}| > 3/5`).

## 2. Deliverables and Definition of Done

- Both producer (`relays/agy002_found_v2_u2/verify_found_v2_u2.py`) and cold-room referee (`relays/agy002_found_v2_u2_referee/referee_found_v2_u2.py`) pass `AST` zero-float/zero-complex-literal checks, `0` repo imports (`standalone L_2 uniformisation + standalone mpmath quaternion Yukawa`), and matching `SCRIPT_SHA256.txt` / `OUTPUT_SHA256.txt` seals (`A`-only commits).

## 3. Five Planted Fault Controls That Must Fail When Broken

1. **`PFU2-1` (`Omitting zeta_5^{-ab}`):** Dropping `zeta_5^{-ab}` breaks `15`-SV `T`-invariance of `O_1` by `> 1/5`.
2. **`PFU2-2` (`Frame C` Up `25`th Roots):** Frame `C`'s `(1, -4)` up coupling drifts under `T^5` by `> 1/20`.
3. **`PFU2-3` (`Linear Trace Copy Wall`):** Contracting with linear trace `(T_3, T_2)` collapses `|r_e - r_d| < (1/10)^25`.
4. **`PFU2-4` (`Mismatched Colour-Index Contraction`):** Contracting `G_{3,L}` off-diagonally across distinct colour indices (`sum_{c_a != c'_a}`, symmetrized Hermitian) breaks modular `T`/`S` invariance of `r_u` (`max(dT, dS)`) by `> 1/5`.
5. **`PFU2-5` (`Guardrail 3 Basis Non-Invariance`):** Single-matrix left-right overlap `|U_u^dag V_u|` shifts by `> 1/10` under random `Haar` `U_{R,u}`.

## 4. Firewall

Strict `0 of 19`; touches only `relays/`; `0` imports from `frontier/` or other seats; expectations committed first (`0 of 19`).
