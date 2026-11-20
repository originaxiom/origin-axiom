# Pre-Registration Card `A2-OW2` — Open-Flute 1-Loop Effective Action Across All Finite Rungs (`N = 1..5`) and Controls (`N = 6..13`): Spontaneous Mirror / CP Breaking (`0 of 19`)

## 1. Purpose and Open-Weave Hypothesis

Dropping `G:SE1`, `G:SE2`, and any hand-picked thread `m004`, consider the canonical Fricke-symmetric 1-loop Euclidean effective potential of a net-fermionic (`n_F > n_B`) field theory on the moduli space `X_0(N) = Gamma_0(N) \ H` of cyclic `N`-isogenous torus pairs `(E_tau, E_{N tau})`:

`V_N(tau) = -pi * ln(Im(tau) * sqrt(N) * |eta(tau) * eta(N * tau)|^2) = (pi / 2) * [-ln(y |eta(tau)|^4) - ln(N y |eta(N tau)|^4)]`

Notice `V_N(tau)` is strictly defined from the zeta-regularized Laplacian determinants of the `N`-isogenous torus pair with **zero** target coordinates embedded, **zero** thread selected, and exact mirror / CP invariance `V_N(-conj(tau)) = V_N(tau)` plus Fricke invariance `V_N(-1 / (N tau)) = V_N(tau)`.

**Pre-Registered Falsifiable Question (`0 of 19`):**
Across the open weave's exact finite quotient ladder `N in {1, 2, 3, 4, 5}` (where `Delta(2, 3, N)` is finite iff `N <= 5`), which rungs preserve mirror / CP symmetry at the global minimum of `V_N(tau)` modulo `Gamma_0(N)`, and is `N = 5` (the unique chiral anomaly-free top finite rung from Card `A2-OW1`) the **first** and **only** finite rung where nature's own 1-loop effective action spontaneously breaks mirror / CP symmetry? Furthermore, how does this compare to non-finite control rungs `N in {6, 7, 8, 9, 10, 11, 13}` and to the algebraic condition `-1` being a square modulo `N` (`B1876` `H11` and Shimura's order-`2` elliptic point count `nu_2(N)`)?

## 2. Exact Pre-Registered Tasks and Pass Bars

### Task `OW2-A`: Exact Euclidean 1-Loop Berezin Sign Theorem and Kronecker Limit Verification

- Verify explicitly on a positive-definite `5 x 5` Hermitian matrix `A` that bosonic Gaussian integration gives `Z_B = 1 / det(A)` (`V_B = +ln det(A)`), whereas Grassmann Berezin integration (computed directly by exact `2^5`-basis exterior expansion and permutation signs) gives `Z_F = +det(A)` (`V_F = -ln det(A)`).
- Independently verify the Kronecker first limit identity `ln det'(-Delta_tau) = ln(4 pi^2 y |eta(tau)|^4)` via direct Chowla-Selberg / Bessel `K`-series evaluation of the real-analytic Eisenstein derivative `-E'(tau, 0)` at multiple test points `tau` to `< (1/10)^35`, establishing that `V_eff(tau) = -(n_F - n_B) / 2 * ln(y |eta(tau)|^4)` is confining (`V_eff -> +infty` at every cusp, strictly subharmonic `Delta_hyp V_N = +pi > 0`) **if and only if `n_F > n_B`** (fermions outnumber bosons, as in the `3`-generation chiral `16` spectrum `n_F = 96 > n_B` from Card `A2-OW1`).

### Task `OW2-B`: Certified Global Minimization Over `100%` of `X_0(N)` for All Five Open Rungs `N in {1, 2, 3, 4, 5}`

- Verify exact `Gamma_0(N)`, Fricke `W_N(tau) = -1 / (N tau)`, and mirror `tau -> -conj(tau)` invariance of `V_N(tau)` on random interior points to `< (1/10)^50` (`65`-digit `mpmath`), and verify the exact Wirtinger gradient `dV_N / dtau = i pi / (2 y) - (i pi^2 / 12) (E_2(tau) + N E_2(N tau))` and exact `2 x 2` real Hessian (`tr H = 4 pi / y^2`? Note exact `Delta_hyp V_N = y^2 (V_xx + V_yy) = +pi`, so `V_xx + V_yy = pi / y^2`!) against finite differences to `< (1/10)^14`.
- Construct the exact coset decomposition `Gamma_0(N) \ SL(2, Z)` of index `mu(N) = 1, 3, 4, 6, 6` for `N = 1, 2, 3, 4, 5` covering `100%` of `X_0(N)`.
- For each `N in {1, 2, 3, 4, 5}`:
  1. Prove an analytic cusp cutoff `Y_cut(N)` strictly eliminating all coset tails `y > Y_cut(N)` (showing `V_N(gamma_k z) > V_min(N)` rigorously from exact cusp widths and `|eta|` bounds).
  2. Run a certified global Lipschitz + Taylor-Hessian branch-and-bound certifier over **100%** of all `mu(N)` coset domains `[-1/2, 1/2] x [sqrt(3)/2, Y_cut(N)]`, rigorously pruning every box outside tiny verified convex balls `B(tau_*, r_ball)` around the global minima where `lambda_min(H(tau_*)) - L_3 * r_ball > 0`.
  3. Refine every global minimum `tau_*` to `55`-digit `mpmath` precision (`|grad V_N(tau_*)| < (1/10)^50`).
  4. Decide **exact CP conservation vs spontaneous CP breaking** via the exhaustive finite-integer congruence solver for `exists gamma in Gamma_0(N)` with `gamma(-conj(tau_*)) = tau_*` (checking BOTH `CP mod Gamma_0(N)` AND whether Fricke `W_N` exchanges conjugate vacua!).
- **Pre-Registered Bar `OW2-B`:** `0` uncertified surviving boxes outside verified positive-definite minimum balls across all `5` rungs `N = 1, 2, 3, 4, 5`; exact `50`-digit stationarity (`< (1/10)^50`) and positive-definite Hessian at every global minimum; exact decidable `Gamma_0(N)` CP-orbit classification reported honestly for every rung.

### Task `OW2-C`: Control Survey on Non-Finite Rungs `N in {6, 7, 8, 9, 10, 11, 13}` and Algebraic Bridge (`H11` / Shimura `nu_2(N)`)

- Compute the exact global minima of `V_N(tau)` (via full coset grid across all `mu(N)` cosets + Newton polish to `50` digits, verifying `|grad| < (1/10)^45` and `lambda_min(H) > 0`), the exact number of `Gamma_0(N)`-distinct global minima, `CP mod Gamma_0(N)`, and Fricke `W_N` pairing for all `7` control rungs `N in {6, 7, 8, 9, 10, 11, 13}`.
- Compute across all `N in {1..13}`: (i) whether `-1` is a square modulo `N` (`B1876` `H11` condition), (ii) Shimura's exact elliptic point counts `nu_2(N)` and `nu_3(N)`, and (iii) whether `V_N`'s global minimum breaks `CP mod Gamma_0(N)`. Report the exact correspondence honestly without post-hoc retargeting.

### Task `OW2-D`: Physical CP Observable and `10`-Trial Haar Basis-Scrambling Gate at `tau_*^{+-} = (+-2 + i) / 5`

- Construct the open boundary-torus `Gate F-U2` `24`-point Yukawa operator `O_1(tau)` directly on the `W:T` triplet basis `(Q_J, Q_I, Q_K)` (zero `m004` required), evaluating the `(S, S)` sector pair (`u` and `d` charges `(1/5, -4/5)` and `(1/5, +2/5)`) at `m * tau_*^{+-}` for canonical weave multiples `m in {1, 5, 8, 15, 24}` (`8 = ord(T_L|_{W:T})`, `24 = ord(c_T)`).
- Compute singular values, CKM-type mixing moduli `|V_ij|`, and the Jarlskog CP invariant `J_CP = Im(V_11 V_22 conj(V_12) conj(V_21))` to `65`-digit precision, checking:
  1. Exact mirror-vacuum antisymmetry `J_CP(m * tau_*^-) == -J_CP(m * tau_*^+)` to `< (1/10)^50`.
  2. Strict nonzero physical CP violation `|J_CP| > 0` at coprime weave orders `m in {8, 24}` (and exact `0` at `m in {5, 15}` where `Re(m * tau_*^{+-}) in Z`).
  3. **Mandatory `Guardrail 3` Haar Unitary Basis-Scrambling Test:** Apply `10` independent random Haar unitary transformations `Y_u -> U_L Y_u U_{R,u}^dag`, `Y_d -> U_L Y_d U_{R,d}^dag` (`U_L, U_{R,u}, U_{R,d} in U(3)`) at `m = 8` and `m = 24` and assert invariance of all singular-value ratios, `|V_ij|`, and `J_CP` to `< (1/10)^12`.

### Task `OW2-E`: Four Planted Faults (`PF-OW2-1` through `PF-OW2-4`)

1. `PF-OW2-1`: Bosonic sign flip `-V_5(tau)` (`n_F - n_B < 0`) must have negative hyperbolic Laplacian (`-pi < 0`) and diverge monotonically toward `-infty` as `y -> infty`.
2. `PF-OW2-2`: Mirror-line stationary point `tau = i / sqrt(5)` on `X_0(5)` must fail strict minimum check (`det H < 0`, saddle point).
3. `PF-OW2-3`: Target-injected potential `V_cheat(tau) = |tau - (2 + i) / 5|^2` (`Guardrail 1`) must fail `Gamma_0(5)` invariance under `T: tau -> tau + 1` and `gamma_5: tau -> tau / (5 tau + 1)`.
4. `PF-OW2-4`: Unphysical single-matrix left-right overlap `V_u^dag U_u` (`Guardrail 3`) must fail the `10`-trial Haar unitary basis-scrambling invariance check (`max drift > 1/10`).

## 3. Custody and Cold-Room Discipline

- Producer script sealed pre-run in `relays/a2_ow2/verify_a2_ow2.py` with `relays/a2_ow2/SCRIPT_SHA256.txt` (`A`-only).
- Output `relays/a2_ow2/verify_a2_ow2_out.json` and `relays/a2_ow2/OUTPUT_SHA256.txt` (`A`-only) committed unread before inspection.
- Independent Cold-Room Referee subagent built from this Card alone (never reading `verify_a2_ow2.py` or its output) seals `relays/a2_ow2_referee/referee_a2_ow2.py`, runs independently, and commits unread output + `SHA-256` manifest.
- Results relay `relays/AGY002_A2_OW2_RESULTS.md` reports Producer vs Cold-Room Referee honestly. `0 of 19.`
