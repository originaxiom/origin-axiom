# Card `AGY-002_FOUND-V2-U1` — Dihedral Cover `8^3_4`, `Berezin`-`CAR` `4D` Collar Action (`A-FOCK-APS`), & `Kawamura` Doublet–Triplet Splitting (`0 of 19`)

## 1. Package and Question

Resolving the `4` remaining bits of `Postulate D` (`B1952`, `B1955`, `P-863(a,c)`) from a single `4D` amphicheiral collar action `A-FOCK-APS` over the unique irregular dihedral cover `8^3_4` of `m004` (`4_1`), under strict `0 of 19` firewall, `Guardrails 1-6`, and `100%` mask-safe rational/integer prose:

1. **Unique Irregular Dihedral Cover & Weyl-Hypercharge Identity (`B1955` + `B1953` Joined Symbolically):**
   - From `pi_1(m004) = <x, y | w x = y w>` (`w = x^{-1} y x y^{-1}`, `Alexander` determinant `5`), prove over all odd `n` in `{3, 5, ..., 31}` (`including 15 and 25`) that surjective dihedral homomorphisms `pi_1(m004) ->> D_n` exist **uniquely at `n = 5`** (`exact count 4`).
   - Verify via exact `SL_2(Z[zeta_6])` `Riley` representation that the canonical longitude `lambda = y x^{-1} y^{-1} x^2 y^{-1} x^{-1} y` commutes identically with meridian `x` (`tr = -2`), acts trivially (`I_5`) on the `5` coset sheets `W_5 = C^5`, while `x` acts as the involution `P` with eigenvalues `+1^3, -1^2` (`splitting the cusp into 3 peripheral orbits of degrees 1, 2, 2`).
   - Verify that `Centralizer_{S_5}(D_5)` is trivial (`order 1`), while `Centralizer_{S_5}(Z_5)` over the double cover has order `5` (`shift X`), generating the `24` orthonormal `sl(5)` Weyl operators `D(a, b) = zeta_5^(3 a b) X^a Z^b` (`X Z = zeta_5^{-1} Z X`, `Tr(D(v) P) = 1`), and prove in the `P`-eigenbasis `W_3^+ (+) W_2^-` that `q_{W_5} = -(1/2) sum_{v != 0} D(v) == diag(-2, -2, -2, +3, +3)` identically (`exact 6Y`).
2. **`Berezin`-`CAR` Fock Algebra, `4D` Collar `APS` Chirality, `Kawamura` Gauge Projection, & Doublet–Triplet Splitting:**
   - Explicitly construct the `32 x 32` `Jordan`-`Wigner` `CAR` operators `c_a, c_a^dag` on `Lambda^*(W_5)` (`{c_a, c_b^dag} = delta_{ab} I_{32}`), verify the exact Grassmann `Berezin` Gaussian identity `int d(bar psi) d(psi) exp(bar psi M psi) == det(M)` on explicit `5 x 5` matrices, and prove that `4D` collar `APS` boundary chirality `gamma_5 (-1)^F = +1` correlates left-handed `4D` `Weyl` chirality uniquely with `Lambda^{even}(W_5) = 16_+`.
   - From all `24` explicit `su(5)` generators, prove `dim C_{su(5)}(P) == 12` (`su(3)_c (+) su(2)_L (+) u(1)_Y`), global kernel `Z_6` (`order 6` inside `SU(3) x SU(2) x U(1)`), exact `6Y` spectrum `[-4^3, -3^2, 0, +1^6, +2^3, +6]` on `Lambda^{even}(W_5)`, and exact vanishing of all `4` `SM` anomaly sums (`Tr Y == 0`, `Tr Y^3 == 0`, `Tr_{SU(3)^2} Y == 0`, `Tr_{SU(2)^2} Y == 0`).
   - Prove `Kawamura` doublet–triplet splitting on a collar-odd fundamental scalar `Phi_s(-s) = -P Phi_s(s)`: `P Phi_s = -Phi_s` leaves `2` weak-doublet zero modes (`dim(W_2^-) = 2`) and `0` colour-triplet zero modes (`dim(W_3^+ cap ker(P + I_5)) = 0`).

## 2. Deliverables and Definition of Done

- Both producer (`relays/agy002_found_v2_u1/verify_found_v2_u1.py`) and cold-room referee (`relays/agy002_found_v2_u1_referee/referee_found_v2_u1.py`) pass `AST` zero-float/zero-complex-literal checks, `0` repo imports, and matching `SCRIPT_SHA256.txt` / `OUTPUT_SHA256.txt` seals (`A`-only commits).
- Every exact algebraic identity holds symbolically (`exact == 0`) and numerically to `< (1/10)^35` (`50`-digit `mpmath`).

## 3. Five Planted Fault Controls That Must Fail When Broken

1. **`PFU1-1` (`Trefoil 3_1` Anomaly Control):** `<x, y | x y x = y x y>` yields `D_3` (`P_3 = (+1^2, -1)`), where traceless `q_{W_3} = diag(-1, -1, +2)` on `Lambda^{even}(W_3)` gives non-zero cubic anomaly `Tr(Y^3) = -6 != 0`.
2. **`PFU1-2` (`Bronze Rival p = 13` Gauge Dimension Control):** `P_{13} = (+1^7, -1^6)` yields `dim C_{su(13)}(P_{13}) = 84 != 12`.
3. **`PFU1-3` (`Level-25 Dihedral Cover Absence`):** Surjective homomorphisms `pi_1(m004) ->> D_{25}` have exact count `0`.
4. **`PFU1-4` (`Collar-Even Scalar Parity Reversal`):** Imposing `P Phi_s = +Phi_s` leaves `3` colour triplets and `0` weak doublets.
5. **`PFU1-5` (`Dropping (-1)^F = +1`):** Retaining all `32` states of `Lambda^*(W_5)` yields a vector-like `Y <-> -Y` spectrum (`0` net chirality).

## 4. Firewall

Strict `0 of 19` compliance; touches only `relays/`; expectations committed first (`0 of 19`).
