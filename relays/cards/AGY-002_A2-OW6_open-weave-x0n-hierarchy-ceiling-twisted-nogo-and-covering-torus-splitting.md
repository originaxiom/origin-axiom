# Pre-Registration Card: `AGY-002_A2-OW6` — Hard Wall 1 Complete Verdict: Analytic `X_0(N)` `Im(tau) <= 1` Ceiling, `E[5]` Twisted-Kernel No-Go, and Covering-Torus `E[5] + E[6]` `e != d` Splitting & Hierarchy-vs-CKM Trade-Off (`0 of 19`)

- **Seat:** `AGY-002` (`agy-002/verify`)
- **Card ID:** `A2-OW6`
- **Empirical Firewall:** Strict `0 of 19` (zero empirical inputs, zero PDG numbers, zero `m004` / `G:SE1` / `G:SE2` selection)
- **Prerequisite Custody:** Builds on `A2-OW2` (`b400fc161` / `a31eb8051`), `A2-OW4` (`08315469d` / `1192ed854`), and `A2-OW5` (`b47f02450` / `efeabdbc7`).

## 1. Scientific Objective & Hypotheses Committed Before Run

This card settles Hard Wall 1 (why the base modular curve `X_0(5)` stabilizes at `Im(tau) = 1 / 5`, whether any untuned base `X_0(N)` 1-loop potential can lift `Im(tau) > 1`, how `e != d` splits on the open weave, and what exact flavor wall remains):

1. **Exact Analytic `X_0(N)` `Im(tau) <= 1` Ceiling Theorem (`OW6-A`):**
   - For the fundamental 1-loop torus determinant `V_1(tau) = -ln(Im(tau) |eta(tau)|^4)`:
     - Verify to `50` digits that for every `y > 0` and every `x in R`, `dV_1/dy(x + i y) >= dV_1/dy(i y)` (exact cos-inequality achieved at `x in Z`), `dV_1/dy(i) == 0` (to `< (1 / 10)^45` by exact `S`-duality), and `d^2 V_1 / dy^2(i y) = 1 / y^2 + 16 pi^2 sum_{n>=1} n^2 r^n / (1 - r^n)^2 > 0` strictly for all `y > 0` (verified at `y in {1, 11/10, 3/2, 2, 5}`).
     - **Corollary (Pass bar `OW6-A`):** For every `y > 1` and every `x in R`, `dV_1/dy(x + i y) > 0` strictly. Consequently, **no** non-negative untwisted 1-loop potential `V(tau) = sum_k c_k V_1(d_k tau)` (`c_k >= 0`, integers `d_k >= 1`) on **any** modular curve `X_0(N)` can ever have a stationary point with `Im(tau) > 1`.
     - Cross-check the `S`-dual massive 4D Kaluza-Klein Casimir potential `V_4D(i y; M)` (`M in {1/2, 1, 2, 5}`, confining sign): verify `|dV_4D/dy(i; M)| < (1 / 10)^8` and `dV_4D/dy(i y; M) > 0` strictly at `y in {6/5, 2}` for all four masses.

2. **Twisted `E[5]` Isogeny-Kernel 1-Loop Potential Audit (`OW6-B`):**
   - Using the modular Kronecker second-limit potential `V_{(a,b)}(tau)` summed over the `4`-point `Gamma_0(5)` isogeny kernel `{(0, k / 5) : k = 1..4}` with exact SM `6Y` charges (`3 x 16` fermions, `12` uncharged gauge bosons, `2H` or `1H` Higgs):
     - Verify exact `S`-duality `|V_{(0, 1/5)}(-1 / tau) - V_{(1/5, 0)}(tau)| < (1 / 10)^35` and exact `Gamma_0(5)` invariance `|V_ker(tau / (5 tau + 1)) - V_ker(tau)| < (1 / 10)^30`.
     - **Pass bar `OW6-B`:**
       - **Full SM Fricke-symmetrized runaway no-go:** On `V_ker^{SM}(tau) + V_ker^{SM}(-1 / (5 tau))` (per kernel point), prove exact rational asymptotic cusp slopes `-104 / 5` (`2H`, from `64 / 3 + 5 * (-632 / 75)`) and `-112 / 5` (`1H`, from `68 / 3 + 5 * (-676 / 75)`) — both strictly negative (**deconfining runaway to `-infty`** as `y -> +infty`, matched numerically at `y in {3, 5}` to `< (1 / 10)^6`).
       - **Fermions-only Fricke-symmetrized orbifold lock:** Even dropping the uncharged gauge bosons (`3 x 16` fermions only), the cusp slope is confining (`+24 = 32 + 5 * (-8 / 5) > 0`), **but** the stationary minimum still locks right back to the exact same CP-breaking orbifold pair `tau_*^{+-} = (+-2 + i) / 5` (`Im = 1 / 5`, gradient norm `< (1 / 10)^30`, positive-definite Hessian, strictly deeper than `i / sqrt(5)` by `> 20`), failing to lift `Im(tau) > 1`.

3. **Topological Covering-Torus Lift `m in {8, 24, 40}`, Open-Weave Regime-4b `E[5] + E[6]` `e != d` Splitting, `10`-Trial Haar Gate, & Exact Hierarchy-vs-CKM Trade-Off (`OW6-C`):**
   - At `tau_m = m * (2 + i) / 5` for the three topological covering-torus levels `m in {8, 24, 40}` (`ord(T_L) = 8`, `ord(c_T) = 24`, `lcm(5, 8) = 40`), evaluate `(Y_u, Y_d, Y_e)` using exact mod-`Z^2`-reduced torsion coordinates `(q_L w, q_R w)` with SM hypercharges `u: (1, -4)`, `d: (1, 2)`, `e: (-3, 6)`:
   - **Pass bar `OW6-C`:**
     - **Taped-flute `E[5]` (`t = 3`) exact `e = d` degeneracy:** On properly reduced `E[5]` alone, `max(|r23_e - r23_d|, |r12_e - r12_d|) < (1 / 10)^35` across all `m in {8, 24, 40}`.
     - **Open-weave `E[5] + E[6]` Regime-4b zero-parameter splitting (`w_3 = lambda(3, +1)^(-4)`, `w_4 = 4 * lambda(4, +1)^(-4)` from `A2-OW5`):** Adding `E[6]` (`t = 4`, `Smith = (1, 6)`) automatically breaks `e = d` degeneracy (`rel 23-split > 45 / 100` at `m = 8`, `> 97 / 100` at `m = 24`, `> 99 / 100` at `m = 40`) while keeping nonzero `J_CP` at all three covering points (`|J_CP(m=8)| > 3 / 10000`, `|J_CP(m=24)| > (1 / 10)^17`, `|J_CP(m=40)| > (1 / 10)^29`).
     - **Mandatory Guardrail 3 (`10`-trial `45`-dps Haar basis-scrambling gate):** Independent random Haar `U(3)` rotations `(U_L, U_{R,u}, U_{R,d}, U_{R,e})` leave all singular-value ratios `(u, d, e)`, `|V_CKM|`, `J_CP`, and `J_det_norm` invariant to `< (1 / 10)^30` (`<< (1 / 10)^12`) at all three covering levels `m in {8, 24, 40}`.
     - **Honest Hierarchy-vs-CKM/CP Trade-Off Certification:** Quantify explicitly that along the single-modulus covering ray `m * (2 + i) / 5`: `m = 8` achieves sizable mixing/CP (`|V_us| > 9 / 100`, `|J_CP| > 3 / 10000`) but shallow masses (`m_2 / m_3 > 1 / 10` in all sectors), whereas `m = 24` and `m = 40` achieve multi-decade mass hierarchies (`m_1 / m_3 < (1 / 10)^5` at `m = 24`, `< (1 / 10)^10` at `m = 40`) but exponentially suppressed mixing/CP (`|V_us| < 1 / 100` at `m = 24`, `< 2 / 1000` at `m = 40`; `|J_CP| < (1 / 10)^15` at `m = 24`, `< (1 / 10)^27` at `m = 40`).

4. **Planted-Fault Self-Checks (`OW6-D`, `4 / 4`):**
   - `PF-OW6-1`: Flipping the Berezin sign (`-V_1`) yields `d(-V_1)/dy < 0` at `y = 2` (`caught`).
   - `PF-OW6-2`: Omitting mod-`Z^2` reduction on `E[5]` wrap-around coordinates `(-3 a / 5, 6 a / 5)` at `m = 8` falsely breaks `e = d` degeneracy by `> 1 / 10` (`caught`).
   - `PF-OW6-3`: Setting `w_4 = 0` (`E[5]` only) collapses `e != d` splitting to `< (1 / 10)^35` (`caught`).
   - `PF-OW6-4`: Evaluating `E[5]` at `m = 5` (`tau = 2 + i`, `Re(tau) in Z`) collapses `|J_CP| < (1 / 10)^35` (`caught`).

## 2. Guardrails & Cold-Room Protocol

- Strict `0` float/complex AST literals and `0` `frontier/` imports; `A`-only `SHA-256` manifests; independent Cold-Room Referee built solely from this card using disjoint implementations (e.g., independent Dedekind eta / Eisenstein `E_2` derivative for `OW6-A`, independent Jacobi `theta_1` Kronecker formula for `OW6-B`, and independent `L_2` + Yukawa + Haar evaluator for `OW6-C`). `0 of 19.`
