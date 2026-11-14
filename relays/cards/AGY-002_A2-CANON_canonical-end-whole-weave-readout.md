# Card A2-CANON: Independent Second Computation of the Whole-Weave Read-Out with `B1927`'s Canonical Length-Two Horocycle End `L_2(tau)` (`M27` & `M30`)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Messages:** `M27` (item two) and `M30` (*after Review 82; independent of `agy-exp`'s `X-CANON`*)
- **Blind Commitment Note:** Committed **prior** to opening `B1927` or `B1928` files or any `agy-exp` branch files.
- **Firewall:** Strictly one hundred percent data-free (`zero` measured values imported or compared).

---

## 1. Mathematical Structure & Locked Pre-Computation Expectations

1. **Exact Modular Invariance of the Pointwise Canonical End (`L_inv(tau) := L_2(tau) + (1/2) log Im(tau)`):**
   - Because `B1667`'s length-two horocycle end satisfies `L_2((a tau + b) / (c tau + d)) = L_2(tau) + log|c tau + d|` while `Im((a tau + b) / (c tau + d)) = Im(tau) / |c tau + d|^2`, the combination
     `L_coord(tau) = L_2(tau) + (1/2) log Im(tau)`
     cancels `log|c tau + d|` identically (`+log|c tau + d| - log|c tau + d| = 0`) and is a **strictly `SL_2(Z)`-invariant, real-analytic function** across the upper half-plane (smooth across the boundary arc `|tau| = 1`, unlike the maximal-horoball / systole `y_FD` corner).
   - Furthermore, under `S . tau = -1 / tau` and `J * tau = (conj(tau) + 1) / conj(tau)`, `L_coord(-1 / tau) = L_coord(tau)` and `L_coord(J * tau) = L_coord(tau)` identically.

2. **Exact Finite-`n` Mark–Twin Equality Under Pointwise `L_2(tau)` (`R_n(mark) == R_n(twin)`):**
   - Because our reverse-swap modular-`S` geodesic bijection `w <-> w^* = swap_{L<->R}(reverse(w))` maps `tau_{w^*}(s) = -1 / tau_w(-s)` pointwise along every closed geodesic and `L_coord(-1 / tau) = L_coord(tau)` holds pointwise (not just at constant `L_coord`), **the exact population averages on the mark `(2/5, 4/5)` and on the twin `(1/5, 2/5)` MUST be strictly equal (`< 10^-12` numerically) at EVERY word length `n >= 2` (`n = 8, 10, 12, 14, 16, 18`)**, and paired samples at `n = 22, 28` will show zero systematic mark-minus-twin drift within paired jackknife standard error.

3. **Strict Channel Positivity (`0.0%` Clamping) & Settling Diagnosis (`n = 8..18` Exact Populations + `n = 22, 28` Large Samples):**
   - Every active channel norm under `L_2(tau)` must remain **strictly positive (`0.0%` clamping)** along all closed geodesics and into cusps (because `L_2(tau)` grows as `+(1/2) log y` in cusps, cancelling `F_u`'s `-pi log y` degeneration just as the systole end did, while staying real-analytic across `|tau| = 1`).
   - Computing **zero-sampling-error exhaustive populations** across `n = 8, 10, 12, 14, 16, 18` together with large without-replacement samples at `n = 22` and `n = 28` (in **both** charge-consistent Higgs worlds of `P-847` / `B1656`'s twenty-four-component frame, plus `B1928`'s twenty-four-point order-five path-measure / hyperbolic-area benchmarks) will definitively separate **deterministic finite-`n` drift** `|R_{18} - R_{16}|` from **finite-sample Monte Carlo variance** at `n = 16 -> 22 -> 28`.
   - **What counts as agreement vs disagreement:**
     - `SAME` on settling if deterministic population steps `|R_{n+2} - R_n|` decay monotonically through `n = 18` (`max |R_{18} - R_{16}| < 10^-2`) and `n = 22` vs `n = 28` agrees within sampling noise (`median |z| ~ 1`, `< 10%` above `2 sigma` on large without-replacement samples), demonstrating that `B1927`'s looser `21% > 2 sigma` figure at one output was sampling variance (and/or finite `n = 16 -> 22` tail step on a small sample) rather than non-convergence.
     - `DIFFERENT` if exact populations through `n = 18` and large `n = 22, 28` samples reveal slow `O(1/n)` drift exceeding `2 sigma` at `N >= 800` words or any channel-norm clamping.

4. **Planted Controls (`CTL-CANON-1..3`):**
   - `CTL-CANON-1`: Omitting the `+(1/2) log Im(tau)` covariant lift on `L_2(tau)` (using bare `L_2(tau)` after pullback or without `SL_2(Z)` covariance) breaks modular invariance along closed geodesics (`> 10^-2`);
   - `CTL-CANON-2`: Second-derivative smoothness test across `|tau| = 1` (`tau(t) = e^{i(pi/3)} + ...` / radial crossing `|tau| = 1`) catches the `C^0` kink of `log y_FD` while passing real-analytic `L_2(tau)`;
   - `CTL-CANON-3`: Unpaired vs paired mark-twin jackknife variance control and reverse-swap word pairing check (`< 10^-12`).

0 of 19.
