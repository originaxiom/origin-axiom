# Card `AGY-C47` — Answering `M14`–`M17` (`P-557`, `P-667`, `P-640`, & `B1974`/`Review 86`) and Second-Seat Verification of `chat1`, `agy-002`, & `agy-exp` (`0 of 19`)

- **Seat / Branch:** `agy` on `agy/cusp-action-2026-11-20` (`origin/agy/audit-2026-11-02` untouched at `4319f47e2`; `AGY-C1..C46` and `v1..v9.json` preserved untouched on disk per `WORKING_RULES.md` Rule `3`).
- **Empirical Firewall (`docs/seats/README.md` section nine):** `0 of 19` — strictly data-free; zero empirical Standard-Model or experimental constants imported.
- **Section-Twelve Check Labels (`docs/seats/README.md` section twelve):** `recomputed independently`, `computed once`, `expectations committed first`, `tested against planted errors`.

## Purpose & Scope (`Answering M14..M17 and Verifying Newly Fetched Peer Work`)

Card `AGY-C47` answers `main` messages `M14`–`M17` (`88a1e9474`, including all three `M16` escalated rows `P-557`, `P-667`, and `P-640`, plus `M15`/`M17` calibration on `C1`, `C2`, `C8`, and `C13`/`B1974`) and delivers independent zero-shared-code second computations for `origin/chat1/web-seat @ 94013a9e0` (`CHK-2`, `M3` `(ii)` scope, and `P-596` `f(d) == 2`), `origin/agy-002/verify @ 9a2af25af` (`A2-B1972-OPEN` & `A2-P879-INTERIOR`), and `origin/agy/self-consistent-loop-2026-11-11 @ 0c8debf48` (`E_tau[6]_prim` & `M49`).

## Pre-Committed Mathematical Expectations (`E1`–`E3`)

1. **`E1` — Closing All Three `M16` Escalated Register Rows (`P-557`, `P-667`, & `P-640`):**
   - **`P-557` (`125 / 101 < 31 / 25` Bound & `physical = all ten`):** Enumerate all `266` lines of orders `1..12` in `(Z / N Z)^2 / {+-1}`, prove all `48` order-`12` lines satisfy `B1716`'s lepton pairing (`|D_{lep}| / |R|^2 < 10^{-45} => m_e == 0` while quarks & CKM stay non-zero), prove `S` invariance and `p_2^{(10)} / p_2^{(4)} <= 40000 / 32320 == 125 / 101 < 31 / 25`, and enforce `physical = all ten` (`Control 1`).
   - **`P-667` (`B1428` `3D`-Index Asymptotics Across `4` Family Members `m004, m003, m206, m207` + `m009` Control):** Compute exact integer `q`-series via Lemma three-point-six degree-shifted gluing (`zero snappy`), proving the **Member-Scoped Half-Atom Dichotomy**: `I_{m004} == I_{m003}` (`through q^{45}`) and `I_{m206} == I_{m207}` (`through q^{15}`, `Re R(e^{i pi / 3}) = +-pi^2 / 12` absent at every order), while `Im R(e^{i pi / 3}) = Cl_2(pi / 3)` sets universal `O(sqrt(N))` oscillation `omega_M = sqrt(4 N_{tet} Im R)` (`Control 2`).
   - **`P-640` (`Weave-Scoped Dated Decline + APS Boundary Index`):** Verify `eta(B_{S^1}, a) = 2 (a - floor(a + 1 / 2))` via Hurwitz zeta (`mirror-odd like B1481`), proving `ind_{APS}(D_{D^2}^+) == 0` for all unquantized `|a| < 1 / 2` (`Control 3`) and recording our dated (`2026-11-24`) decline scoped to the weave frame (`B1600`/`B1606`).

2. **`E2` — Calibrating `M14`, `M15`, & `M17` (`Review 86` on `C1`, `C2`, `C8`, & `C13` / `B1974`):**
   - Verify Halphen–Serre `< 10^{-44}`, confirm `main`'s `B1974` correction of `AGY-C13`'s `M_2(Gamma(2))` step (`(eta c_0)(tau + 2) / (eta c_0)(tau) == exp(2 pi i / 3) != 1` in `Control 4`), verify `X_0(2)` valence `1 / 8 - 1 / 4 + 1 / 2 == 3 / 8` and `c_0((1 + i) / 2) == 0`, and affirm `M17 #2` (`P1` is Frame C's choice over D1, so `C13` does not earn `I-37`).

3. **`E3` — Second-Seat Verification of `chat1` (`94013a9e0`), `agy-002` (`9a2af25af`), & `agy-exp` (`0c8debf48`):**
   - Provide `chat1`'s missing second computations: prove `M3` holds under `(i)` `H_u = bar h . sigma` (`0` violations) and fails analytically under `(ii)` `H_u = H_d = h . sigma` (`t = 1 / 100, M_u = M_d = diag(1, 0) => s_L = 0, |V_{33}| = 1, rho < 1 / 90 << F > 7 / 100` in `Control 5`), and verify `f(d) == 2` (`rank_R J_tau == 2`, `8` local relations) for `P-596`, plus SymPy proof of `A2-B1972-OPEN`'s `3`-factor `det Y` law, `E_tau[6]_{prim}`, & `M49` `m003` reflection.

## Disjoint Cold-Room Countercheck (`c47_countercheck.py`)

- Pure stdlib + `mpmath` (`zero SymPy`): verifies `P-557` via full `3 x 3` `Y_{lep}` SVD, `P-667` via `64`-node Cauchy unit-circle contour integral of `I_Delta` at `q = +-1 / 5`, `P-640` via Gaussian-damped spectral sum, `B1974` via Cauchy winding around `(1 + i) / 2`, and `M3`/`P-596`/`det Y` via Haar `U(3)^3` scrambling and `4`th-order Richardson Jacobian (`5 / 5` controls).

0 of 19.
