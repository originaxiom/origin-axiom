# Card `AGY-002_CLOSURE-G5` — Covariant Frame `D1` `CIM (3, 3, -6)` `CKM` Alignment, `Pati-Salam` `3(B-L)` Holonomy Separation, and `Weil` Cocycle / `Gramian` Laws (`0 of 19`)

## 1. Package and Question

Closing `P-861`, `B1947`, `B1948` Step `2`, `P-860(a, b, d)`, and `P-845` inside the pole-free closed-fibre `CIM (3, 3, -6)` triple overlap (`I_L + I_R + I_H = 3 + 3 - 6 = 0`) under strict `0 of 19` firewall and `Guardrails 1-6`:
1. In genuine triple-overlap Frame `D1`, is cusp `CKM` mixing `|V_tb|` `ALIGNED`, `DERANGED`, or `PARTIAL` under pure hypercharge `6Y` vs `SU(2)_R`-symmetric `Pati-Salam` `3(B-L)` holonomy above `M_PS`, and is `CIM (3, 3, -6)` completely free of the `1 / (pi m_x^2)` `3`-torsion poles?
2. Why do local `SO(10)` `10_vec` Clebsch-Gordan vertices fail to split `Y_e` from `Y_d^T`, why does the `k = 0` cusp `Higgs` slice of `CIM (3, 3, -6)` possess an exact `(1/3) Lambda_tau` spectral periodicity, and how do `Pati-Salam` `(6Y, 3(B-L))` holonomies separate leptons from down quarks pointwise and orbit-wise across Levels `5`, `10`, and `15`?
3. What is the exact `SL(2, Z)` `Weil` transport and `Heisenberg` cocycle law of `CIM (3, 3, -6)`, when does the single-sheet `E^*[5]` `Hermitian` `Gramian` preserve exact `T` and `S` covariance (`even` vs `odd` `Delta`), and what distinguishes flavoured covariant `Higgs` contraction from both `9`-sheet `E[3]` `Schur-Heisenberg` collapse and unflavoured `6`-mode `Higgs` tracing (`B1727`)?

## 2. Deliverables and Definition of Done

1. **Pole-Free `E[3]` Continuity & Exact `CIM (3, 3, -6)` `CKM` Alignment Theorem (`P-861`, `B1947`, `P-860(d)`):**
   - Verify continuous analyticity across all `8` non-zero `3`-torsion points `w in E[3] \ {0}` (`max ||Y(w + eps) - Y(w)|| < (1/10)^3` at `eps = (1/10)^6`, `min ||Y(w)||_F > 1`, zero `m_x` pole masking).
   - At cusp height `y = 8` on the unique `q^0` cusp `Higgs` zero mode `e_0`: prove pure `6Y` (`(Delta_up, Delta_dn) = (+5, -1)`) yields **exact `PARTIAL (4 / 24)` alignment** (`4` meridian points `a = 0` have `|V_tb| > 99/100`; all `20` non-meridian points `a != 0` have `|V_tb| < 1/1000`), whereas `SU(2)_R`-symmetric `Pati-Salam` `3(B-L)` holonomy (`(Delta_up, Delta_dn) = (+2, +2)`) yields **`100% ALIGNED` `|V_tb| > 1 - (1/10)^12` across all `24 / 24` Level-`5`, `72 / 72` Level-`10`, and `192 / 192` Level-`15` primitive points**, with small `SU(2)_R` breaking + subleading `Higgs` mode admixture smoothly generating `0 < |V_cb|, |V_td| < 1/10` and `|V_tb| > 99/100`. Verify `10`-trial `U(3)^6` `Haar` scrambling `< (1/10)^13`.
2. **Local `10_vec` Commutant No-Go, `(1/3)`-Periodicity Theorem, & `Pati-Salam` Lepton-Down Split (`P-845`, `B1948` Step `2`):**
   - Verify `[B-L, Gamma_bidoublet] = 0` identically on `(1, 2, 2) subset 10_vec` (`local vertex cannot split Y_e from Y_d^T`).
   - Prove `Y_cim(tau; xi)[:, :, 0]` has singular-value shifts `{1/6, 3/6, 5/6}` invariant under `xi -> xi + 1/3` and `xi -> xi + tau/3` (`< (1/10)^14`), explaining why `s_1 / s_3` whole-orbit multisets match (`< (1/10)^13`) for pure `6Y` and pure `3(B-L)` while splitting **pointwise** by `> 100` in ratio at Level `5` under `3(B-L)` (`w = (1/5, 2/5)`) and splitting **orbit-wise** (`max |s_1/s_3(dn) - s_1/s_3(lep)| > (1/10)^4` at `y = 4`) across **all** Levels `5`, `10`, and `15` under combined `6Y + 3(B-L)` (`(Delta_dn, Delta_lep) = (+1, -15)`).
3. **`Weil` `zeta`-Independence, `Heisenberg` Cocycle, & Even-`Delta` Single-Sheet `SL(2, Z)` `Gramian` Law (`B1945` § `6`, `P-860(a, b)`):**
   - Verify `||U_3(T; zeta) - U_3(T; 0)|| < (1/10)^13` and `||U_3(S; zeta) - U_3(S; 0)|| < (1/10)^13`, and verify the exact `Heisenberg` cocycle `Y(xi + 1) = exp(+6 i pi alpha) Y(xi)`, `Y(xi + tau) = exp(-6 i pi beta) Y(xi)` (`< (1/10)^13`).
   - Prove that single-sheet `E^*[5]` `Gramian` covariance with covariant puncture-`Higgs` `v_6(tau) = psi^{(6)}(0; tau, 0)` fails for odd `Delta` (`pure 6Y`, `err > 1/50`) and holds to `< (1/10)^13` under `T` and `S` for **even `Delta`** (`Pati-Salam 3(B-L)` `Delta in {+2, -6}`), retaining non-degenerate eigenvalues (`ev_3 - ev_1 > 1/100` at `y = 3/2`) whereas both the `9`-sheet `E[3]` `Schur-Heisenberg` orbit and the unflavoured `6`-mode `Higgs` trace collapse to `(Tr G / 3) I_3` (`anisotropy < (1/10)^13`).

## 3. How It Could Come Out Wrong (Falsification Conditions Sealed Before Execution)

- Any `E[3]` discontinuity `>= (1/10)^3`, mismatch on `(4, 20)` pure-`6Y` `CKM` counts, or `3(B-L)` `|V_tb|` deficit `>= (1/10)^12` on any of the `288` primitive points across Levels `5`, `10`, `15`.
- Failure of `(1/3)`-periodicity (`>= (1/10)^14`), failure of pointwise `3(B-L)` or whole-orbit `6Y + 3(B-L)` lepton-down separation, or `U(3)^6` `Haar` drift `>= (1/10)^13`.
- Failure of even-`Delta` `E^*[5]` `Gramian` `T/S` covariance (`>= (1/10)^13`), failure of `Schur` / `Higgs`-trace isotropy (`>= (1/10)^13`), any float/complex literal in source, or failure to catch any of `PF5.1..PF5.5`.

## 4. Five Planted Fault Controls That Must Fail When Broken

1. **`PF5.1` (`Mixed Conjugated Bidoublet Pairing on 3(B-L)`):**Replacing `(e_0, e_0)` with orthogonal `(e_2, e_0)` in `Y_u` vs `Y_d` must break `24 / 24` `CKM` alignment (`min |V_tb| < 1/100`).
2. **`PF5.2` (`Non-Period 1/4 Shift on k = 0 Spectrum`):** Shifting `xi -> xi + 1/4` instead of `xi + 1/3` must break singular-value invariance (`diff > 1/100`).
3. **`PF5.3` (`Odd-Delta Single-Sheet E^*[5] Gramian Non-Covariance`):** Using odd `Delta = -1` (`pure 6Y down`) without double-cover lift must fail single-sheet `E^*[5]` `T/S` covariance (`err > 1/50`).
4. **`PF5.4` (`Unflavoured 6-Mode Higgs Trace Isotropy Collapse — B1727`):** Tracing equally over all `6` `Higgs` modes instead of contracting with `v_6(tau)` must collapse `G_L` to `(Tr G / 3) I_3` (`anisotropy < (1/10)^13`, failing hierarchy).
5. **`PF5.5` (`Naive Un-Transported Linear Orbit Sum Under tau -> tau + 1` — `B1945` § `6`):** Summing `Y(tau; w)` linearly over `E^*[5]` with unit weights must change singular-value ratios under `tau -> tau + 1` (`diff > 1/1000`).

## 5. Dependencies and Firewall Boundaries

Rests on `Cremades-Ibanez-Marchesano` (`2004`), `Pati-Salam` (`1974`), and `Gates 1-4`. Strict `0 of 19` firewall; touches only files under `relays/`. Expectations committed first (`0 of 19`).
