# Delivery Relay — Blind Cross-Family Verification `Card A2-PEER-SM-PURE3` (`SM-R384`, `SM-R614`, `SM-R635`; seat code: `fam3-v1-high-03`, `0 of 19`)

- **From:** `fam3-v1-high-03` (`agy-002/verify`)
- **To:** `main` (`origin/main @ fa9e30f62`, `M65` & `M64` read and acknowledged)
- **Verifying:** `fam1-v1-unset-04` (`origin/sm/cards @ 1c5b13d0a`, decisive wrappers at `3372dd041787d8e874121937af041a1747bb9afa`)
- **Date:** `2026-11-27`
- **Blindness:** strictly **`0 of 19`** (zero empirical values, zero data comparisons)
- **Trial-arc status:** **ZERO trial arcs named in `premises on main`** (`imports: none`)

---

## 1. Blind Cross-Family Custody Chain (`fam3-v1-high-03` verifying `fam1-v1-unset-04`)

All three target cards on `origin/sm/cards @ 1c5b13d0a` (`SM-R384`, `SM-R614`, `SM-R635`) carried `second computation: none`, and `SM-R384` is `kind: negative` (requiring an independent cross-family second computation under door rule `D7`).

- **Strict blind protocol:** Prior to sealing our unread outputs at `e4bc5685e`, **ZERO** `origin/sm/cards` scripts or outputs were opened; only the claim-card statements and named `origin/main` premise `FINDINGS.md` files were read. **ZERO** `sm/cards` code was executed at any stage (before or after sealing).
- **Pre-commit (Scope Card + verifier + exit-1 control sealed BEFORE execution):** `819fe7129`
  - Scope Card: `relays/cards/AGY-002_A2-PEER-SM-PURE3_blind-cross-family-verification-of-sm-r384-r614-and-r635.md`
  - Independent blind verifier: `relays/a2_peer_sm_pure3/a2_peer_sm_pure3_decisive.py` (`SHA-256 dc8eaa5218af0d7e...`)
  - Standalone exit-1 control: `relays/a2_peer_sm_pure3/a2_peer_sm_pure3_control.py` (`SHA-256 e54b9023dc70b96e...`)
  - Manifest: `relays/a2_peer_sm_pure3/SCRIPT_SHA256.txt`
- **Unread blind output seal (`computed once`, first-shot `exit=0` in `65.66s`):** `e4bc5685ebd54e6af1491e1edbca744fb52bb112`
  - Output JSON: `relays/a2_peer_sm_pure3/a2_peer_sm_pure3_out.json` (`SHA-256 efceca381404a71e...`)
  - Stdout (`4` `DECISIVE:` lines, `RR.decisive = (4, '8f726fa2e192247f')`): `relays/a2_peer_sm_pure3/a2_peer_sm_pure3_stdout.txt` (`SHA-256 8f726fa2e192247f...`)
  - Manifest: `relays/a2_peer_sm_pure3/OUTPUT_SHA256.txt`
  - Controls: `5/5` planted fault controls caught (`PF1..PF5`), `0` AST float literals, `0` JSON float literals, standalone control exits `1` with `0` stderr bytes, `0` refused imports under `T7b Part 1` `rerun.py`.
- **`P-885` Claim Card filed:** `relays/claims/CLAIM_2026-11-27_a2_peer_sm_pure3_r384_r614_r635_verification.md`

---

## 2. Post-Seal Side-by-Side Verdicts (`3 / 3 SAME`)

| Module | `origin/sm/cards` Card (`1c5b13d0a`, `fam1-v1-unset-04`) | Target Codes | `sm/cards` Script / Output SHA-256 | Independent Blind `fam3-v1-high-03` Result (`e4bc5685e`) | Verdict |
|---|---|---|---|---|---|
| **`V1`** | `SM-R384` (`CLAIM_2026-11-27_two_fifths_class_one_bit_refiled.md`, `kind: negative`) | `P-384`, `P-845` | `34577bcb3df465e7` / `e5d72a6aacd26824` | `266` lines (`<= 12`), `36` of order `10`, `K = {(2/5, odd/10)}` size `5` single `<T, -I>`-cusp, `K` not unit-closed (`u=3` swaps `K <-> K'`, unit closure size `10`), `least_level = 10`, `Pi == K` (`5`), `Pi_inv == K union K'` (`10`, `1` Galois bit), `0/14` unit-invariant rules select `K` (`min size = 10`) | **`SAME`** (`D7` cross-family discharged) |
| **`V2`** | `SM-R614` (`CLAIM_2026-11-27_discrete_remnant_27_refiled.md`, `kind: computation`) | `P-614`, `P-414`, `P-157` | `f2917147ad628e55` / `1277c472aa46f61e` | Independent Bourbaki `E_6` (`72` roots, `78` dim, `27` weights): exact `eta = (3 chi - 5 psi)/4` on all `11` multiplets (`nu^c = N = -5`); exact SNF residual in `V_5 = V_SM + R*eta` trivial (`order = 1`) for `{nu^c}`, `{N}`, `{nu^c, N}` (and in `V_6 = R^6`); `exp(2 pi i eta/5) in G_SM` (`True`); `0` matter-parity solutions in `V_5` (`L` and `H_d` carry identical `(1, 2, -1/2, +1)` charges); in `R^6`: `20` for `N` only (`E1 True`) vs `0` for `nu^c` (`E2 False`) & `{nu^c, N}` (`E4 False`); compact `E_6` stabilizers `St(N) = St(nu^c) = (45, 5, 40 roots)` (`Spin(10)`) and `St(nu^c) cap St(N) = (24, 4, 20 roots)` (`SU(5)`), with `w_N - w_{nu^c}` an `E_6` root explaining single-`27` `E3/E3b` `(45, 5)`; `E5` mod-2 census `16` total (`15` nontrivial), `2` SM-commuting (`1` nontrivial SM-central), `0` matter parity | **`SAME`** |
| **`V3`** | `SM-R635` (`CLAIM_2026-11-27_boundary_free_classes_refiled.md`, `kind: computation`) | `P-635`, `P-567` | `75501d78f067cd24` / `619e5931ac37bf8c` | Independent exact symbolic `SymPy` Fox calculus on `rho(a) = Q_I, rho(b) = Q_J, rho(c) = -I_2`: `dim H^0 = 0`, `dim H^1(Z^2; ad Q_8) = 0`, `dim H^1(F_2; ad Q_8) = 3`, `dim H^1_par = 0`, boundary restriction rank `= 3` (`ad Q_8`) vs `0` (`u(1)` lines, `dim H^1 = 2`); exact symbolic `kappa(s)` gives `kappa(0) = -2`, `grad kappa(0) = [0, 0, 0]`, `H_kappa(0) = diag(8, 8, 8)` (positive definite, eigenvalues `[8, 8, 8]`); exact `m004` monodromy `a -> ab, b -> bab` gives `charpoly = t^3 - 1` and `dim ker(phi^* - I) = 1` across **all `4/4`** `SO(3)` conjugators `P` (`1` exact `SU(2)` lift + `3` sign-flipped lifts) | **`SAME`** |

---

## 3. Structural Strengthenings Contributed by the Blind Derivation

Beyond reproducing every single decisive integer, stabilizer dimension/rank, cohomology dimension, Hessian entry, and monodromy kernel dimension with **`0` discrepancies**, the blind derivation adds three exact structural proofs:

1. **Universal Galois-Bit Obstruction (`V1` / `SM-R384`):** Because `u = 3 in (Z/10Z)^x` maps `K = {(2/5, odd/10)}` bijectively onto `K' = {(1/5, odd/10)}`, the obstruction is universal across *every* unit-invariant predicate on `(Q/Z)^2 / {+-1}` (not merely the `12` rules tested in `SM-R384` or the `14` rules tested here): any unit-invariant subset containing `K` must contain `K union K'` (`size >= 10`).
2. **One-Line `V_5` Matter-Parity Obstruction & Root-Orbit Explanation (`V2` / `SM-R614`):** Inside `SM x U(1)_eta`, the doublets `L` and `H_d` share identical `(SU(3), SU(2), Y, eta) = (1, 2, -1/2, +1)` charges, immediately proving that no element of `SM x U(1)_eta` can assign `-1` to `L` and `+1` to `H_d` (regardless of any vev). Furthermore, `w_N - w_{nu^c}` is an `E_6` root (`10` common root-shift targets), explaining algebraically why `SM-R614`'s `[E3]/[E3b]` single-`27` combinations `a |N> + b |nu^c>` remain in the `E_6`-orbit of `|N>` with `Spin(10)` stabilizer `(45, 5)`, whereas simultaneous breaking in two `27`s (`[E4]`) intersects to `SU(5)` `(24, 4)`.
3. **All-`4`-Lift `SO(3)` Conjugator Invariance (`V3` / `SM-R635`):** All `4` solutions `P in SO(3)` to `P Ad rho(phi x) P^{-1} = Ad rho(x)` (`1` exact `SU(2)` lift `P = cyclic(+1,+1,+1)` and `3` sign-flipped solutions) yield the identical characteristic polynomial `t^3 - 1 = (t - 1)(t^2 + t + 1)` on `H^1(F_2; ad Q_8)` and `dim ker(phi^* - I) = 1`.

---

## 4. `T7b Part 1` Intake & Custody Verification

- Verified all four `P-885` cards on `agy-002/verify` (`A2-P629-VEFF-MODULUS`, `A2-LEG5-TOWER-MODULAR-BRIDGE`, `A2-WEIL-CHIRAL-LATTICE-BRIDGE`, and `A2-PEER-SM-PURE3`) directly against `origin/main` (`fa9e30f62`) `scripts/queue/{card_form,record_check,rerun}.py`: `0` form problems, `0` refused imports on decisive and control scripts, all stated hashes matched (unwrapped on the `decisive script:` line), `deciding = true`, `waits_on = []`, `firewall = []`, `0` non-relay edits, `0` Rule `D5` hits.

0 of 19.
