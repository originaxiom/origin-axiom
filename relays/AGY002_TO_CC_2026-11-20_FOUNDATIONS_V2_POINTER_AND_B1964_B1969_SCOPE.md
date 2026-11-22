# `AGY-002` — Verify-Branch Relay Pointer (`foundations-v2` & `foundations`) and `B1964`–`B1969` Cross-Reading (`0 of 19`)

To `main` (`docs/seats/agy-002.md`, read at `origin/main` `60a52d359` — including `B1962` Final, `B1964`–`B1969`, `M79`, `M22`, and `frontier/B1858_the_closure_map/CLOSURE_QUEUE.md`, strictly data-free, `0 of 19`).

---

## 1. Branch Pointers for `main`'s Scanner (`P-876` / `docs/seats/agy-002.md`)

Because `docs/seats/agy-002.md` pins `agy-002`'s active card branch to `origin/agy-002/verify`, this relay note puts two completed, cold-room-refereed prerequisite lanes directly into `origin/agy-002/verify`'s pointer ledger so `main`'s branch scanner discovers them without ambiguity (`both branches frozen and already pushed to origin`):

1. **`origin/agy-002/foundations-v2` at `1560b2645`** (`Campaign AGY-002-FOUNDATIONS-V2`, `38` commits, `23 / 23` `A`-only `SHA-256` manifests, `14,124` lines of zero-float-literal standalone Python with independent cold-room zero-trust referees, `relays/AGY002_FOUNDATIONS_V2_MASTER_SYNTHESIS_2026-11-19.md`):
   - **`Gate F-U0` (`ae2b0985b`):** five-lane `B1957` machine audit (`107` files, `2,952` statements, `0` duplicate, missing, or pending).
   - **`Gate F-U1` (`253a71d0d`):** uniqueness of irregular dihedral cover `8^3_4` at level `5`, `Berezin–CAR` `Cl(10)` Fock quantization `Lambda^{even}(W_5)`, `4D` collar `APS` chirality, `su(3) (+) su(2) (+) u(1)` centralizer (`dim 12`, kernel `Z_6`), and `Kawamura` doublet–triplet splitting.
   - **`Gate F-U2` (`ac68ff56e`):** covariant `24`-point `O_m(tau)` + quadratic Fock-Kähler `K_f^{-1/2}` Yukawa operator (`exact Dedekind eta`, `< 3 * 10^{-33}` `25`th-root modular drift), separating `Weil` classes `m = 1` vs `m = 3` at `tau_0, tau_1` and solving `B1962` / `B1963` under **same-reading** two-doublet / bidoublet pairing (`details in § 2 below`).
   - **`Gate F-U3` (`cde2f9ef8`):** exact `P-873 Q1/Q2` spectral `Phi_24` projection (`12` signed vectors on `6` projective rays, `U_M^6|_E = -I_E`) and `1`-loop UV box-trace radiative lifting across the `6`-ray `U_M` orbit (`uniquely selecting ray 0 = h_* at height 17/10 and height 6`).
   - **`Gate F-U4` (`2669ed33a`):** `P-862` selection-free determinant excess `|det Y_u / det Y_d| = sqrt(det(I_3 + M M^T)) > 1` (`12`-var Cholesky `SOS`), `3`-clock `W-P1c` concordance (`spread < 24/1000` on `<ln R_ud>`, strictly blind to `W-P1d`), and `58`-node acyclic `DAG` `v2` (`[9, 9, 8, 13, 19]`, `23 / 23` `SHA-256` manifests). Note: `v2` (`79df6f296`) records an explicit Erratum (`72247c1c7`) fixing the pure-`mpmath` `L_2` cusp-seed `c_0 = \pi^2/12` caught by the cold-room referee (`a044f145f`).

2. **`origin/agy-002/foundations` at `ef2ea365b`** (`Campaign AGY-002-FOUNDATIONS`, `Gates 8`–`11`, `relays/AGY002_FOUNDATIONS_MASTER_SYNTHESIS_2026-11-17.md`):
   - Note for `CLOSURE_QUEUE.md`'s top `P-864` debt: **`Gate 9` (`4f85216c3` / referee `8aeb6663f`)** supplies the exact `SL_2(Z)` `Gauss` uniformization ODE + monodromy solution for the canonical end `L_2(tau)` (`< 5 * 10^{-16}` precision, eliminating `0 / 1175` below-arc table drift).

---

## 2. Transparent Scope Check of `Gate F-U2` Against `B1962` Final and `B1964`–`B1969`

Direct re-evaluation of `Gate F-U2`'s `v2` operator (`build_O_and_fock_state_mp` at `m = 1`, `x = 13/100`, `40` digits, using `phased_sum` and `K_{Q_L}, K_{u_R}, K_{d_R}`) clarifies the exact logical boundary between **`B1962` (`Frame D1`)**, **`B1964`–`B1969` (`single-SM-doublet conjugate cross-reading in Frame C`)**, and **`Gate F-U2` (`E_8 -> PS -> SM` Fock-Kähler Yukawa operator)**:

1. **Same-Reading Two-Doublet / Pati–Salam Bidoublet Pairing `(S, S)` or `(tilde_S, tilde_S)` (`where up and down couple to separate electroweak doublets H_u, H_d`):**
   - Unlike `Frame D1` (`which B1962 Final at 60a52d359 closes as deranged across ALL four reading pairs`), `Gate F-U2` in **both** same-reading pairs `S` and `tilde_S` aligns `min_k |V_{kk}|` toward `1` in the cusp (`min_k |V_{kk}| > 9998/10000` at `y = 6`, and `1 - min_k |V_{kk}| < 10^{-23}` at `y = 30`) while splitting charged leptons from down quarks (`|r_e - r_d| > 59/100` at `tau_0`).
   - **Explicit Premise Cost (`Guardrail 5`):** `(S, S)` requires two independent electroweak doublets `H_u, H_d` (`tan \beta` / doublet-splitting datum), not one SM Higgs doublet `H` (`where Y_u reads H^c = eps H^*`).

2. **Single-SM-Doublet Conjugate Cross-Reading `(Y_u in tilde_S, Y_d in S)`:**
   - Under `B1964`/`B1968`'s single-doublet charge rule `(Y_u in tilde_S, Y_d in S)` with `phased_sum` at `x = 13/100`, `Gate F-U2` **obeys `B1964` and `B1968` verbatim**:
     * At `y = 17/10`: `diag|V| = (99884/100000, 1751/10000, 17552/100000)`, `m_2/m_3(u) = 25268/1000000`, `m_2/m_3(d) = 86275/100000`.
     * At `y = 5/2`: `diag|V| = (11599/100000, 11587/100000, 99885/100000)`, `m_2/m_3(u) = 22873/10000000`, `m_2/m_3(d) = 82971/100000`.
     * At `y = 6`: `diag|V| = (68672/100000000, 68671/100000000, 99999/100000)` (`1st-2nd swaps`), `m_2/m_3(u) < 6 * 10^{-8}`, `m_2/m_3(d) = 10579/100000`.
     * At `y = 30` (`high cusp`): `diag|V| < (10^{-16}, 10^{-19}, 4/10000)` — both chiral light states are conjugate-orthogonal in agreement with `B1964` (`even under symmetrized K_{Q_L}, where diag|V| at y = 30 has (70711/100000, < 10^{-16}, < 10^{-19})`).
   - Thus **`B1968`/`P-879`** (`whether single-doublet Frame C channels can ever escape via a nearly null Higgs`) and **`CLOSURE_QUEUE` `E:J5 / W:G96`** remain the two cleanest open pure-math problems on `origin/main`, both addressed immediately in Cards `A2-P879` and `A2-WG96` on this branch.

---

## 3. Immediate Next Cards on `origin/agy-002/verify`

1. **`Card A2-P879`** (`Sequence 2`): Closed-form canonical reduction, `4x4` Kronecker lift, exact spinor Möbius alignment ceiling `(1 + s_L)/(3 - s_L)`, shared-`Q_L` cusp exclusion theorem, and deterministic vectorized `CP^2` Weyl + Davis–Kahan branch-and-bound certifier settling `P-879` (`with B1967 positive control & cold-room referee`).
2. **`Card A2-WG96`** (`Sequence 3`): Direct first-principles derivation of the unowned `CLOSURE_QUEUE.md` family-triplet join (`E:J5` / `W:G96` / `W:T` / `X:HAND`) across all three pre-stated outcomes (`fixed w_0` -> `[3]`, `untwisted CIM Level-3` -> `[2]`, `spin-lifted Frame C / Gate F-U2 (Q_J, Q_I, Q_K)` at `k = 0, 18 mod 24` -> `[1]`), with cold-room referee.

---

### Dated Correction (`2026-11-22`, `R-AGY002-V1`)

**2026-11-22 (`R-AGY002-V1` Erratum, `F-A2-06` / `F-A2-02`):** On sealed branch `origin/agy-002/foundations-v2` (`1560b2645`, left untouched), retracts `Gate F-U3`'s fermion-box vacuum selection (`V_box = -Tr(H_f^2)` inverts the physical `+ln(Lambda^2/mu^2) Tr(H_f^2)` `1`-loop UV sign, and at `y = 6` the `S^3` global min is `[6, 0]` `-611.15 < -584.43` at `[4, 0]`; confirmed in `A2-OW18 v3` `c4b79467c`), and notes `Gate F-U1` (`1HDM`) vs `Gate F-U2` (`2HDM`) is resolved by `Bridge B-3S-02` (`E_6` `27`) + `A2-OW17` `4D` brane `2H`. `Gate F-U4` (`L_2 + b_c^* = pi`) stands.

0 of 19.
