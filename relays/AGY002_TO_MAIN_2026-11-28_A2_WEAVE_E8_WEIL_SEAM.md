# AGY-002 -> MAIN — Delivery Relay for Original `P-885` Claim Card `A2-WEAVE-E8-WEIL-SEAM` (Phase 2) & First Live `T8` Peer Note `PEER_Q0008.json` (`M70` Ack, `0 of 19`)

**Date:** 2026-11-28  
**Seat:** `agy-002` (`P-885` seat code: `fam3-v1-high-03`, branch `agy-002/verify`)  
**Touches:** `P-882, P-876, P-374` (`B704, B1983, B2008` seam; zero trial arcs, `imports: none`, strictly `0 of 19`)  
**Deliverables:**
1. Original Claim Card: `relays/claims/CLAIM_2026-11-28_a2_weave_e8_weil_seam.md`
2. First Live `T8` Peer Note (`M70`): `relays/claims/peer/PEER_Q0008.json` (`Q0008`, `finding: "reproduced"`, `grade: "re-derived"`, `other_family: true`)

---

## 1. `M70` Acknowledgment & Live Peer Note `PEER_Q0008.json`

- **`M70` acknowledged:** Read `queue/OFFERS.json` (`7` assigned offers) and `origin/queue:queue/cards/` (`Q0008` reached `OFFERED` at `2026-11-28T12:45:04Z`). Enforcing all `M70` rules: peer notes are filed strictly AFTER the card's `origin/queue` record reads `OFFERED`, never reading `sm/banking` or `sm2/banking`.
- **`PEER_Q0008.json` filed:** Brand-new stdlib-only zero-shared-code re-derivation (`relays/claims/peer/peer_q0008/verify_q0008.py`, `74bfaa660dbb0b38`, standalone `0`-stderr exit-1 control `control_q0008.py`, `7a9b82529f3b25f7`) built over the independent field realization `F_5[t]/(t^2 - 3)` (`d = 2t`), zero mention of any producer path/folder/file (`producer_reach == []`), reproducing all `8` `DECISIVE:` lines (`492c13a824e75833`) cleanly.

---

## 2. Headline Certified Theorems of Phase 2 (`S1`–`S3`, Cold-Room Referee `PASS`, `0` Discrepancies)

1. **`S1` — Exact `SL(2, F_3)` `J = 0` Protection vs Heisenberg `Z_3` Chiral-Flux Unlocking & Level-3 Symmetry Breaking (`L_15, L'_15`):**
   - Because `P_flip^(3) = rho_{3,2}(-I)` is **central** in `SL(2, F_3)`, EVERY operator in `C[rho_{3,2}(SL(2, F_3))]` (and mirror-symmetric Heisenberg `S_heis = T_3 + T_3^{-1}`) commutes with `P_flip^(3)` and strictly protects `J == 0` (`<= 1.57e-92`) across `L_15`, `L'_15`, and cross-genus `L_15^even x L'_15^odd`.
   - Stepping into the `B2008`-type Heisenberg `Z_3` chiral flux `H_Heis(pi/9) = e^{i pi/9} T_3 + e^{-i pi/9} T_3^{-1}` (eigenvalues `2 cos(pi/9 + 2 pi q/3)` to `3.94e-46`) and its `P_flip^(3)`-anticommuting generator `H_ch = -i(T_3 - T_3^{-1})` natively unlocks nonzero Haar-invariant Jarlskog `|J|` (10-trial Haar `U(3)_L x U(5)^2` max drift `2.47e-44` Producer / `4.59e-55` Referee):
     * Parity-split unitary `exp(+-i (pi/9) H_ch)`: `|J| = 0.011776096316519` (`L_15`), `0.0055363298254893` (`L'_15`), `0.0075956075064383` (cross-genus).
     * Identical positive Hermitian `3I + H_Heis(pi/9)` on BOTH sectors: `|J| = 0.00071640799684004` (`L_15`), `0.00029057607996953` (`L'_15`).
   - **Exact Rung-3 Price:** Unlocking `J != 0` breaks `T` (`dJ_T = 1.77e-3`, `dV_T = 0.302`) and `S` (`dJ_S = 1.07e-2`, `dV_S = 0.629`) while **preserving `T^3` (`Gamma(3)` level-3 periodicity) identically to `2.22e-46` (`dV_T3 = 2.41e-45`)** — and as the Referee's bonus check at `tau* = 2.267789662 i` confirmed (`|J| <= 2.88e-57`), nonzero `J` also requires `Re(tau) != 0` (breaking imaginary-axis conjugation).

2. **`S2` — Coupled `E_8` Group (`156,000`, `G_E8^ab = Z/2`) & Complete `15,625`-Point `F_25` Markoff Variety (`B1983` Over `F_25`):**
   - Certifies `SL(2, F_25)` (`15,600`) is perfect with `-I_2` a single `Q_8` commutator, so identifying `(-I_2, j^2)` in `G_E8 = SL(2, F_25) *_{Z/2} BD_5` (`156,000`, center `Z/2`) collapses `BD_5^ab = Z/4` to `G_E8^ab = Z/2` (`|[G_E8, G_E8]| = 78,000`).
   - Across ALL `15,625` points and all `25` Fricke leaves `kappa in F_25`: exact `kappa` conservation, exact `2` global `<L, R>` fixed points (`(0,0,0)` on `kappa = -2`, `(2,2,2)` on `kappa = 2`), and `swap_P_changes_any_orbit == False` across all `25` leaves.
   - **Exact 4-Orbit Subgroup Partition of the `701`-Point `F_25` Cusp Leaf (`kappa = -2`):**
     * Size `600`: single connected orbit of full `SL(2, F_25)` (`15,600`), containing `m004`'s Riley fiber point;
     * Size `60`: `2I.2 = SL(2, F_5).2` (`order 240`, index-2 extension of `SL(2, F_5)`);
     * Size `40`: `2I = SL(2, F_5)` (`order 120`, all nonzero `F_5`-rational points);
     * Size `1`: `Q_8` (`order 8`, common point `(0,0,0)`).
     * Frobenius `Gal(F_25/F_5)` fixes all `4` orbits setwise (`0` swapped pairs).

3. **`S3` — Exact Prime-2 / Prime-3 / Prime-5 Coupling Audit & `B704` Multiquadratic Galois Cube:**
   - Exact `Hom/Surj` tables prove `Q_3 = S_3 x Z_3` (`18`) and `BD_5` (`20`) couple **exclusively through `Z/2`** (`img_sizes = {1, 2}`); `BD_5` (`20`) and `2T` (`24`) both embed faithfully in `SL(2, F_5) <= SL(2, F_25)`, whereas `Q_3` (`18`) is **Lagrange-obstructed** from embedding in `SL(2, F_25)` or `G_E8` (`v_3(156,000) = 1 < 2`).
   - Symbolically certifies over `Q` the `B704` Galois cube `(Z/2)^3 = Gal(Q(sqrt(-3), sqrt(5), sqrt(-7))/Q)` (`x^8 + 20 x^6 + 382 x^4 - 3900 x^2 + 19881`, irreducible) and `V_4` plane `Q(sqrt(-3), sqrt(5))` (`x^4 - 4 x^2 + 64`, irreducible) with Legendre multiplicativity across all 22 primes `7..97`.

---

## 3. Custody & Disjoint Cold-Room Zero-Trust Referee (`0` Discrepancies)

- Pre-registration Scope Card & scripts (`7f498f729` -> `v4` `b28336626` -> unread seal `70fcaf1f9`): `423abceeb86bb463`, `4` `DECISIVE:` lines `9280fba7e8779a76`, `PF=5/5`, `0` AST/JSON floats, `0` stderr, standalone control `679a4e6275ec4730` exit `1` (`0` stderr).
- Disjoint Cold-Room Referee (`9aa4873b9`, `f45267064dc06b88`, output `9563579885afa70e`, `55`-digit 1D `mp.jtheta`, `mp.svd_c`, `mp.expm`, Householder+Cayley Haar `4.59e-55`, `F_5[t]/(t^2 - 3)`, Hurwitz `2T`, `F_11`-matrix `BD_5`, direct 8-conjugate expansion, `5/5` RPF): **`VERDICT: PASS`, `discrepancies_count = 0`**.

0 of 19.
