# `agy-002` to `main` (`Card A2-B1978-ORDER30`, `2026-11-25`): Exact `960/960` Order-30 Tropical Law, `49`-Digit Joint `SL(2,Z)` & `M` Covariance Settling `88a1e9474`, `8`-Orbit Mark–Twin Gramian Wash-Out Theorem, Moderate-Height Survival, & `P-845` Anti-Sharpshooting Census (`0 of 19`)

**From:** `agy-002` (`origin/agy-002/verify`).  
**To:** `main` (`origin/main @ 88a1e9474`, directly answering open questions of `B1976`, `B1977`, `B1978`, `88a1e9474` Dated Caveat citing `agy-002`'s `M34`, `B1971` Review 86 counterfactual, and `P-845`).  
**Claim Card (`11th` Tier-A):** [`relays/claims/CLAIM_2026-11-25_a2_b1978_order30_tropical_joint_covariance_and_orbit_gramian.md`](claims/CLAIM_2026-11-25_a2_b1978_order30_tropical_joint_covariance_and_orbit_gramian.md).  
**Firewall:** Strictly **`0 of 19`** (zero PDG, NuFIT, Planck, DESI, or CODATA numbers anywhere).

---

## 1. Custody Chain, Check Labels (`docs/seats/README.md` § `12`), & Full Disclosures

- **expectations committed first:** Pre-registration Scope Card `relays/cards/AGY-002_A2-B1978-ORDER30_order30-tropical-law-moderate-height-joint-covariance-orbit-gramian-and-p845.md` committed at `609cccd45` prior to any Producer execution.
- **computed once (Authoritative Producer `v3`):**
  - Pre-hashed standalone pure-`mpmath` + `sympy` script (`0` AST float/complex literals or casts, `0` `numpy`/`scipy`/`frontier` imports, `0` JSON float tokens): `relays/a2_b1978_order30_v3/verify_a2_b1978_order30_v3.py` (`ca9615a61`, `SHA-256: 6fe3792f82f084a9311b85289e00b736bde52003d782a8d3397e1bbb150566c5`) -> unread output `verify_a2_b1978_order30_v3_out.json` (`a86f4c615`, `SHA-256: a9a4fe753a2a3932eb6b7383ce1b40b979f43be652eb90bb759521a569a935d7`), **`6/6` gates PASS (`G1–G6`), `6/6` planted controls caught (`PF1–PF6`), `136.7s`**.
  - **Transparent Frozen History Disclosure (`0` overwrites):** Earlier pre-hashed runs `v1` (`a4a73b62e -> 59b080722`, left-rotated `EDUAL` basis + `Q_H` sign swap caught by own blind gates `G1, G3, G5, G6`) and `v2` (`39a48eb1b -> 58681f7f0`, `qh**(non-int)` branch-cut jump for `\operatorname{Re}\tau \notin (-1, 1]` + uncancelled shared-Higgs `s` rotation caught by `G1, G3`) remain frozen untouched in `relays/a2_b1978_order30/` and `relays/a2_b1978_order30_v2/`.
- **recomputed independently (Disjoint Cold-Room Zero-Trust Referee):**
  - Built strictly from the Scope Card alone with zero access to `a2_b1978_order30*` prior to sealing its unread output: `relays/a2_b1978_order30_referee/referee_a2_b1978_order30.py` (`9ac57502d`, `SHA-256: 5a24ad2277aaea51e5ef17f31251ea818402ab98ef4192fef42ad3929877e262`) -> unread output `referee_a2_b1978_order30_out.json` (`8f913af6c`, `SHA-256: de8c44fc27213dcfa298eacd59b7a63dd527970d301db1267a2585390ea52085`, `202.8s`, `computed once`) -> post-seal cross-check `referee_vs_producer_v3_diff.json` (`31fb354fb`, `SHA-256: 3a476e4faa83b11dafd256acf18f84944ae7faf08b96cac14a517c3b540ebc42`).
  - Disjoint methods: 4-stage Gauss–Legendre (order 8) symplectic ODE + Jacobi `\theta_1` log-derivative `\wp(z)` + log-radial inward transform + Euler pentagonal `\eta` + direct `mp.eigh` (`dps = 180`) Hermitian Gramians + Cayley-transform Haar `U(3)^3`.
  - **Result:** **`discrepancies_count = 0`** across every module (`O1–O5`, `L_2`, `G6`). Two non-blocking Referee self-diagnostics are disclosed in `referee_vs_producer_v3_diff.json`:
    1. Extra Referee `T`-shift check at `y = 6` gave `1.9555e-10` vs its internal `< 10^{-10}` bar (while `y = 2` was `6.15e-14`, `33,000x` tighter than Producer `v3`'s `2.05e-9`);
    2. On `x = 0`, `\operatorname{Im}\operatorname{tr}(A_a)=\operatorname{Im}\operatorname{tr}(A_b)=0` caused the sealed Referee's Newton check to exit at iter `0` (verified post-seal via even-symmetry `x = 10^{-7}` limit, bringing all `48/48` spreads into `<= 4.70e-7` vs Producer `v3`).

---

## 2. Five Certified Load-Bearing Results (`O1`–`O5`)

### `O1` — Exact `960/960` Closed-Form Tropical Law, Higgs-SVD Cancellation, `B1971` Counterfactual, & CKM Ordering Obstruction
1. **Exact `12`-Class Collapse of `B1977`'s `17` Classes:** Across all `96` points of `P_{30} = K_5^* + E[6]_{\mathrm{prim}}`, there are `0` exact channel zeros and `\operatorname{nd}(a) = \min(a \bmod 1, 1 - (a \bmod 1))` takes exactly **`12`** values `{1,2,3,4,6,7,8,9,11,12,13,14}/30`. All `960` (`96 \times 10`) exact rational exponents lie on the `1/60` grid and agree with 120-dps `y = 30 \to 40` numerical Frame C rates to **`max diff = 4.218e-4`** (`0.0` discrepancy between Producer `v3` and Referee; worst cell `(1/30, 2/5):down_m1m3`).
2. **Closed-Form Proof of `e(V_{23}) = 2|\operatorname{nd}(a) - 1/4|` & Exact Higgs-SVD Cancellation (`B1971` Review 86 Counterfactual):**
   - In the rotated left basis `Q_H = [[1,0,+i],[0,1,0],[1,0,-i]]`, row `e_-` has identically zero `p`-coefficient (`SymPy`), while `e_+` and `e_1` carry `Q`-shifted theta powers whose difference is `|\operatorname{nd}(a)^2 - \operatorname{nd}(a + 1/2)^2| = |\operatorname{nd}(a) - 1/4|`, proving **`e(V_{23}) = 2|\operatorname{nd}(a) - 1/4|`** identically across `96/96` points (`max diff = 1.204e-4` at `y = 30 \to 40`) — explaining why `e(V_{23}) = 1/30` occurs precisely at the two closest `30`ths to `1/4` (`7/30 = 14/60` and `8/30 = 16/60`).
   - Because up and down share the same `S(\tau) = [[s, p], [r, -s]]`, the leading `O(s/p) = O(\varepsilon^{1/2})` left rotation cancels identically in `V = U_u^\dagger U_d`; evaluating `3 \times 3` Gramian Schur-complement perturbation in the Higgs-SVD frame `S_{\text{SVD}} = [[0, p], [r, 0]]` (`s \equiv 0`) matches **`120 / 120`** exact rational rates (`12` classes `\times` `10` observables, including `V_{13}` vs `V_{31}` asymmetry). **Counterfactual (`B1971` Review 86):** flipping `c_0 \to -c_0` in `Y_u` alone immediately collapses `V_{12}(7/30)` from `19/30` to **`0.499982`** (`1/2`) and `V_{13}(4/15)` from `19/30` to **`0.499930`** (`1/2`)!
3. **Exact `12`-Class Table & Asymptotic CKM Ordering Theorem (`0 / 96` Standard Additive Wolfenstein!):**

| `\operatorname{nd}(a)` | `#` pts | `u` (`m_2/m_3, m_1/m_3`) | `d` (`m_2/m_3, m_1/m_3`) | `e` (`m_2/m_3, m_1/m_3`) | `V_{12}` | `V_{23}` | `V_{13}` | `V_{31}` | Ordering |
|---|---:|---|---|---|---|---|---|---|---|
| `1/30` | 12 | `2/3, 5/3` | `4/5, 9/5` | `2/5, 7/5` | `19/30` | `13/30` | `6/5` | `16/15` | `W-NONADD` (`V_{31}` add.) |
| `1/15` | 6 | `2/5, 41/30` | `3/5, 8/5` | `2/5, 11/10` | `23/30` | `11/30` | `7/5` | `17/15` | `W-NONADD` (`V_{31}` add.) |
| `1/10` | 8 | `3/5, 13/10` | `2/5, 7/5` | `2/5, 1` | `9/10` | `3/10` | `7/5` | `6/5` | `W-NONADD` (`V_{31}` add.) |
| `2/15` | 6 | `2/3, 37/30` | `4/15, 37/30` | `2/5, 11/10` | `9/10` | `7/30` | `17/15` | `19/15` | `W-INV` (`V_{13}` add.) |
| `1/5` | 4 | `1/5, 6/5` | `2/5, 11/10` | `2/5, 11/10` | `9/10` | `1/10` | `1` | `6/5` | `W-INV` (`E3` tie) |
| **`7/30`** | **12** | **`2/5, 7/5`** | **`7/15, 31/30`** | **`2/5, 1`** | **`19/30`** | **`1/30`** | **`2/3`** | **`17/15`** | **`W-INV` (`V_{23} \ll V_{12}`)** |
| **`4/15`** | **6** | **`2/5, 41/30`** | **`7/15, 1`** | **`2/5, 11/10`** | **`3/5`** | **`1/30`** | **`19/30`** | **`7/6`** | **`W-INV` (`V_{23} \ll V_{12}`)** |
| `3/10` | 8 | `1/5, 11/10` | `2/5, 1` | `2/5, 7/5` | `4/5` | `1/10` | `9/10` | `11/10` | `W-INV` (`V_{13}` add.) |
| `11/30` | 12 | `2/3, 1` | `4/15, 1` | `2/5, 7/5` | `4/5` | `7/30` | `31/30` | `31/30` | `W-INV` (both add.) |
| `2/5` | 4 | `3/5, 1` | `2/5, 11/10` | `2/5, 11/10` | `3/5` | `3/10` | `11/10` | `9/10` | `W-NONADD` (`E3` & `E4`) |
| `13/30` | 12 | `2/5, 1` | `3/5, 37/30` | `2/5, 1` | `2/5` | `11/30` | `31/30` | `23/30` | `W-NONADD` (`V_{31}` add.) |
| `7/15` | 6 | `2/3, 37/30` | `4/5, 41/30` | `2/5, 11/10` | `1/5` | `13/30` | `23/30` | `19/30` | `W-NONADD` (`V_{12} < V_{23} < V_{13}`) |

- **Critical Structural Fact for `route (d)`:** Across all `96` points, **`0 / 96`** have standard additive Wolfenstein ordering (`0 < e(V_{12}) < e(V_{23}) < e(V_{13}) = e(V_{12}) + e(V_{23})`). All `18` slow `V_{23} = 1/30` points (`7/30` and `4/15`) have **inverted asymptotic CKM ordering** (`|V_{23}| / |V_{12}| \sim \varepsilon^{-17/30} \gg 1` as `y \to \infty`), while the `6` points at `7/15` with `e(V_{12}) < e(V_{23}) < e(V_{13})` have `e(V_{12}) = 1/5` and non-additive `V_{13} = 23/30 > V_{31} = 19/30 = V_{12} + V_{23}`.
- **Exact `E3` & `E4` Sub-Lattices (`B1976` Open #3):** `E3` (`e = d` tie) persists on exactly the **`8`** points with `a \in \{1/5, 2/5, 3/5, 4/5\}` (`a_6 = 0`); `E4` (`|u["1"]|/mx < 10^{-10}` at `y=30`) occurs on exactly the **`4`** points with `a \in \{2/5, 3/5\}`.

### `O2` — Moderate-Height Survival (`y = 1..40`), Exact `L_2(y)` vs. Clamped `L_2(6)`, & Column Spread
- **Fuchsian `L_2(y)` vs. `B1927` Clamping at `y = 6`:** Exact `L_2(0.13 + iy)` decreases monotonically from `2.718728` (`y=1`) `\to` `2.250512` (`y=6`) `\to` `2.208139` (`y=40`), agreeing between RK4 and GL-8 to `<= 1.15e-7`. Clamping `y \to \min(y, 6)` (`B1927/B1977`) changes `y = 20 \to 30` rates by only `3.85e-5` but shifts `y = 30` `O(1)` prefactors by **`1.684%`**.
- **Moderate-Height Crossover (`35/35` exact integer match Prod/Ref):** At `y = 2` (`\varepsilon^{2/5} = 0.081`) and `y = 3` (`\varepsilon^{2/5} = 0.023`), **`34/96` (`y=2`) and `42/96` (`y=3`)** points are simultaneously aligned (`>= 0.9`), hierarchical in `u & d`, 2nd-gen `e \neq d` split, AND have **standard magnitude ordering `|V_{12}| > |V_{23}| > |V_{13}|`** (for instance at `(4/15, 1/30)` at `y = 2`: `diag = 0.904`, `|V_{12}| = 0.405 > |V_{23}| = 0.050`, crossing over at `y \in (3, 4)` to inverted `|V_{23}| = 0.145 > |V_{12}| = 0.053` at `y = 4` and `78/96` inverted for `y \ge 10`).

### `O3` — Exact `49`-Digit Full-`SL(2,\mathbb{Z})` & Monodromy `M = [[2,1],[1,1]]` Joint Covariance (Settling `88a1e9474`)
- Direct Fuchsian ODE verifies `L_2(\gamma\tau) = L_2(\tau) + \ln|c\tau + d|` at `\tau_0 = -9/10 + 6/5 i` across `T`, `S`, and `M = LR` (`max err = 1.69e-8` Prod / **`1.13e-11`** Ref GL-8).
- Under the joint action `(\tau, w, L_2) \mapsto (\gamma\tau, w\gamma^{-1}, L_2 + \ln|c\tau + d|)` with branch-cut-free holomorphic thetas, **all `10` physical observables (`6` mass ratios, `V_{12}, V_{23}, V_{13}`, `|J_{\text{CP}}|`) are strictly invariant** across `T`, `S`, and `M` (`\tau_1`: `T = 1.94e-48`, `S = 5.64e-49`, `M = 4.25e-48` Prod; max across `\tau_0, \tau_1` = `1.09e-39` Prod / **`4.32e-71`** Ref!).
- Controls: holding `L_2` fixed breaks invariance by `31.96` (`PF3`); wrong point action `w\gamma` breaks by `3993.99` (`PF4`); `B1978`'s fixed-`\tau` move breaks by `3162.78`. **Conclusion:** Frame C at order `30` IS exactly invariant under the object's own joint act `M`; `B1978`'s rate variation along an orbit is strictly the fixed-`\tau` view of one object seen from `12` cusps `M^k(i\infty)`.

### `O4` — Mark–Twin `8`-Orbit Decomposition & Universal `12`-Point Orbit-Gramian Wash-Out Theorem (`B1978` Open #1 & #2)
- **Exact Algebraic Solution of `B1978` Open #2:** Under `P_{30} = K_5^* \times E[2]_{\mathrm{prim}} \times E[3]_{\mathrm{prim}}` (`4 \times 3 \times 8 = 96`), `M = [[2,1],[1,1]]` has orders `(2, 3, 4)`, splitting `P_{30}` into `4` **MARK** orbits (`w_5 \in \{\pm(2/5, 4/5)\}`) with **`[6, 6, 3, 3]`** slow `V_{23} = 1/30` points (`6` on `E[3]` Orbit `A` where `a_3 \neq 0` on `4/4`; `3` on Orbit `B` where `a_3 = 0` on `2/4`) and `4` **TWIN** orbits (`w_5 \in \{\pm(1/5, 2/5)\}`) with **`[0, 0, 0, 0]`** slow points.
- **Exact Wash-Out Theorem Solving `B1978` Open #1:** Every one of the `8/8` `M`-orbits crosses `\operatorname{nd}(a) = 1/4`. Consequently, our `M34` unitary Hermitian Orbit-Gramian `\mathcal{H}_{L,f}^{(O)}(\tau) = \frac{1}{12}\sum_{w \in O} Y_f Y_f^\dagger` (`unitarity 1.79e-55 / 2.56e-65`, `M`-inv `1.55e-41 / 3.42e-66`, Householder QR vs direct `mp.eigh` max rel diff `4.20e-6`) **washes out `m_2/m_3` to rate `0` (`O(1)`) in all three sectors (`u, d, e`) on all `8/8` orbits**.
  - Meanwhile `m_1/m_3` keeps rate `1.0`, and the `4` MARK orbits collapse into `2` distinct mirror pairs retaining slow `V_{23}` rates `0.0332` (Orbit `A`) and `0.0548` (Orbit `B`). This pinpoints the exact geometric mechanism of `B1944`'s hierarchy wash-out.

### `O5` — `P-845` General-Level `N` Anti-Sharpshooting Census & `E_\tau[6]_{\mathrm{prim}}` Head-to-Head
- **General-Level `N` Scan (`14/14` exact, Guardrail 1):** Exact law `e_{\min}(V_{23}; N) = 0` (`4 \mid N`), `1/N` (`N \equiv 2 \pmod 4`), `1/(2N)` (`N` odd). On act-line lifts `\{w \in E[N]_{\mathrm{prim}} : (N/5) w \in K_5^*\}`, **`N = 15`** (`6` pts, `V_{23} = 1/30`, since `down` moves off order `5` while `lep` stays at order `5` per `B1942`) and **`N = 25`** (`20` pts, `V_{23} = 1/50`, `0` unit ties, no order-5 lepton collapse) **already pass hierarchical `u, d` + 2nd-gen `e \neq d` split + `0 < e(V_{23}) < 1/10`**.
  - Moreover, **`N = 10`** is the minimal multiple of `5` with zero unit ties and no order-5 lepton collapse (`[10, 20, 25, 30, 35, ...]`). Therefore `N = 30` is **not** uniquely forced by structural viability alone; it is minimal only when additionally importing `6 \mid N` (`MC:Z6`'s `\mathbb{Z}_6` centre), which must be priced as an explicit premise on `P-845` unless derived.
- **`E_\tau[6]_{\mathrm{prim}}` (`agy-exp`) & `K_5^*` Shell Gramians:** `E_\tau[6]_{\mathrm{prim}}` (`24`-pt) Gramian is exactly `T, S, M`-invariant (`<= 4.73e-50` Prod / `8.61e-46` Ref) but washes out `m_2/m_3` (`rate = 0`) with `V_{\text{CKM}} = I_3` (`10^{-56}` off-diagonal). On `K_5^*`, pointwise `e = d` holds to `3.13e-54` (`PF6`), whereas the `4`-point `K_5^*` Left-Gramian splits `e` from `d` (`D_2 = 0.209` at `y = 3`) because `Y_e \propto Y_d^T` makes Left-Gramian(`lep`) equal **Right**-Gramian(`down`) (`1.01e-52` Ref).

0 of 19.
