# `AGY-002_CLOSURE-G5` — Gate 5 Results (`0 of 19`)

## 1. Check Labels and Tracked Evidence (`docs/seats/README.md` § 12)

- **expectations committed first:**
  - Card commit `772755b2c`: `relays/cards/AGY-002_CLOSURE-G5_covariant-frame-d1-ckm-bl-holonomy-and-weil-connection.md`
  - First script seal `1f410c48e`: `relays/agy002_closure_g5/verify_closure_g5.py`, `relays/agy002_closure_g5/SCRIPT_SHA256.txt`
  - First output seal `431181218` (committed unread): `relays/agy002_closure_g5/verify_closure_g5_out.json`, `relays/agy002_closure_g5/OUTPUT_SHA256.txt`
- **recomputed independently:**
  - Cold-room second script seal `0b6d75eed` (built from `hep-th/0404229` and the card alone via `2D` torus quadrature and `80`-digit `mpmath`, without reading or importing `verify_closure_g5.py`): `relays/agy002_closure_g5_referee/referee_closure_g5.py`, `relays/agy002_closure_g5_referee/SCRIPT_SHA256.txt`
  - Cold-room second output seal `2decb3d7a` (committed unread): `relays/agy002_closure_g5_referee/referee_closure_g5_out.json`, `relays/agy002_closure_g5_referee/OUTPUT_SHA256.txt`
- **tested against planted errors:**
  - `5 of 5` planted cases caught in `431181218` (`PF5.1` mixed `(e_2, e_0)` `|V_tb| = 0 < 1/100`; `PF5.2` `tau/4` shift `> 5/100 > 1/100`; `PF5.3` odd-`Delta` single-sheet `Gramian` error `> 2 > 1/50`; `PF5.4` unflavoured `6`-mode `Higgs` trace anisotropy `< (1/10)^15 < (1/10)^13`; `PF5.5` naive linear orbit sum `T`-drift `> 7/100 > 1/1000`);
  - `5 of 5` planted cases caught independently in `2decb3d7a` (`PF5.1` `0 < 1/100`; `PF5.2` `> 36/100 > 1/100`; `PF5.3` `> 49/100 > 1/50`; `PF5.4` `< 2 * (1/10)^15`; `PF5.5` `> 1 > 1/1000`).

## 2. Mask-Safe Rational Verification Summary & Cold-Room Refinements (`0 of 19`)

| Check | First Computation (`431181218`) | Cold-Room Second Computation (`2decb3d7a`) | Sealed Rational Bar |
|---|---|---|---|
| `AST` source lock & `SHA-256` custody | `0` float literals, `0` complex literals, `0` repo imports | `0` float literals, `0` complex literals, `2 / 2` producer `SHA-256` matched | Exact (`0`) |
| `E[3] \ {0}` analyticity (`zero 1/(pi m_x^2) poles`) | `max_jump < 2 * (1/10)^4`, `min ||Y||_F > 3 > 1` | Quadrature & theta `< 5 * (1/10)^5`, `min ||Y||_F > 3 > 1` | `< (1/10)^3`, `> 1` |
| `Pati-Salam` `3(B-L)` `CKM` alignment (`288` points) | `24/24` (`N=5`), `72/72` (`N=10`), `192/192` (`N=15`) with `1 - |V_tb| < (1/10)^14`; perturbed `Haar` `< 5 * (1/10)^14` | `288/288` with `1 - |V_tb| < (1/10)^15`; `80`-digit `mpmath` proves `min(s_1 - s_2) > 0` (`100%` `Haar`-invariant); perturbed `Haar` `< (1/10)^14` | `< (1/10)^12` |
| Pure `6Y` cusp `CKM` (`P-861`) + `Guardrail 3` check | Unshifted theta on `e_0`: `4` aligned (`a = 0`), `20` deranged (`PARTIAL`) | Reproduces `(4, 20)` in unshifted theta, and proves exact `s_1(Y_u) = s_2(Y_u)` `2`-fold degeneracy at even `5a`: `15/24` basis-invariantly orthogonal (`|V_tb| = 0`), `9/24` `2D`-subspace degenerate (`0/24` aligned `> 99/100` when lifted covariantly by `v_6(tau)`, `Haar` `< (1/10)^15`) | Exact diagnosis |
| `[B-L, Gamma_bid] = 0`, `(1/3)`-periodicity, & `e-d` split | Exact `0` commutator; `(1/3)` shift `< 2 * (1/10)^16`; `y = 4` pointwise `3(B-L)` factor `> 28 > 10`; `6Y + 3(B-L)` orbit split `> (1/10)^4` | `32 x 32` `Clifford` exact `0`; `(1/3)` shift `< (1/10)^15`; `45`-digit pure multisets `< (1/10)^35`; pointwise `3(B-L)` factor `> 28` (`y = 4`) and `> 800 > 100` (`y = 8`); `6Y + 3(B-L)` split `> (10)^7` | `< (1/10)^13` / split |
| `Weil` `zeta`-independence, cocycle, & `E^*[5]` `Gramian` | `zeta`-diff `< 5 * (1/10)^15`, cocycle `< 3 * (1/10)^15`, even-`Delta` `T/S` `< 7 * (1/10)^15`, anisotropy `> 3/10 > 1/100`, `9`-sheet `Schur` `< 3 * (1/10)^15` | `zeta`-diff `< 4 * (1/10)^15`, cocycle `< 2 * (1/10)^14`, even-`Delta` `T/S` `< 3 * (1/10)^15`, anisotropy `> 5/100 > 1/100`, `9`-sheet `Schur` `< (1/10)^15` | `< (1/10)^13` |

## 3. Theorems Locked in Gate 5

1. **Resolution of `P-861`, `B1947`, & `P-860(d)` (`CKM` Alignment in Genuine `CIM (3, 3, -6)` Frame `D1`):** Closed-fibre `CIM (3, 3, -6)` is analytic across all `8` points of `E[3] \ {0}` (`no propagator poles`). Under pure `6Y`, opposite `T_{3R}` charges give `(Delta_up, Delta_dn) = (+5, -1)`, leaving `15/24` order-`5` points basis-invariantly orthogonal (`|V_tb| = 0`) and `0/24` aligned above `99/100` once `Y_u`'s `2`-fold `k = 0` degeneracy is covariantly lifted (`v_6(tau)`). Above `M_PS`, unbroken `SU(2)_R` forbids `T_{3R}` holonomy splitting and restricts abelian torus holonomy to `3(B-L) subset SU(4)_c`, forcing `(Delta_up, Delta_dn) = (+2, +2)` and **exact `Haar`-invariant `|V_tb| = 1` across `288 / 288` primitive points at Levels `5, 10, 15`**, with small `SU(2)_R` breaking generating hierarchical off-diagonal `CKM` angles.
2. **Resolution of `P-845` & `B1948` Step `2` (`Lepton-Down Separation`):** Local `(1, 2, 2) subset 10_vec` vertices commute identically with `B-L` (`forcing Y_e = Y_d^T`), whereas `3(B-L)` torus holonomy yields `(Delta_dn, Delta_lep) = (+2, -6)`, splitting `s_1 / s_3` pointwise at Level `5` (`> 28` at `y = 4`, `> 800` at `y = 8`) while `Y_cim[:, :, 0]`'s `(1/3) Lambda_tau` periodicity preserves pure whole-orbit multisets until combined with `T_{3R}` (`6Y + 3(B-L)`, splitting whole-orbit multisets at all Levels `5, 10, 15`).
3. **Resolution of `B1945` § `6` & `P-860(a, b)` (`Weil` Cocycle & Single-Sheet `SL(2, Z)` `Gramian`):** In `CIM (3, 3, -6)`, `U_3(T; zeta)` and `U_3(S; zeta)` are `zeta`-independent while lattice wraps induce `exp(+6 i pi alpha)` and `exp(-6 i pi beta)` `Heisenberg` phases. Consequently, single-sheet `E^*[5]` `Gramians` contracted with `v_6(tau) = psi^{(6)}(0; tau, 0)` are `SL(2, Z)`-covariant (`< (1/10)^14`) and anisotropic (`ev_3 - ev_1 > 1/100`) for **even `Delta`** (`3(B-L)`), evading both `9`-sheet `E[3]` `Schur` collapse and `6`-mode unflavoured `Higgs` trace collapse (`B1727`). Gate 5 is locked. `0 of 19.`
