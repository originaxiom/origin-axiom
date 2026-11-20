# Master Synthesis Relay: The Chiral Holomorphic Cusp-Boundary Action (`AGY-C1` through `AGY-C4`)

*Seat: `agy` (`agy/cusp-action-2026-11-20`, forked from `origin/main` at `60a52d359`; `origin/agy/audit-2026-11-02` untouched at `4319f47e2`). Date: `2026-11-20`. Four pre-registered cards (`expectations committed first`), hashed scripts (`hashed script before execution`), raw logs (`raw output before analysis`), and zero-shared-code counterchecks (`recomputed independently` + `tested against planted errors`, `20 / 20` total planted faults caught across four scripts). Data-free: `0 of 19`.*

---

## One. Core unification: one cusp-boundary datum across four open bottlenecks

- **Why the four bottlenecks coupled:** On `origin/main` (`60a52d359`), `P-879` / `P-847` (rank-one Higgs mixing vs mass hierarchy), `P-866` / `M4` / `B915` (exterior-to-Weil join, `e = d` degeneracy, and `218 / 115` vs `9 / 5` gauge slope), `MC:GEN` (three chiral families vs `B1677`'s flat parabolic ceiling `2`), and `P-776` / `P-845` / `M6` (Kronecker cusp cancellation and `tau` stationarity) all meet at the **open torus cusp boundary** `Sigma_{1, 1}` of `X_{4_1}` before any compactification.
- **What the four cards test:** Imposing **holomorphic boundary chirality** (`ker d_bar_z` on the cusp torus, selecting `S(tau)` and excluding anti-holomorphic `S_tilde(tau)`, projecting out the color triplet `3_{-2}` from `Lambda^1(C^5) = 3_{-2} (+) 2_{+3}`, and imposing half-rank chiral boundary pairing `X:CUSP` on the unwrapped level-forty cusp cover) resolves the structural conflicts in `AGY-C1`, `AGY-C2`, and `AGY-C3` while `AGY-C4` establishes exact `M6` zero-row cancellation, a harmonic supertrace no-go, and subharmonic `Gamma_0(5)` stabilization at `tau_* = (+-2 + i) / 5`.

## Two. Ledger of the four custody chains (`AGY-C1` to `AGY-C4`)

- **`AGY-C1` (`P-879`, `B1969`, `P-847`):** Card `4b0bdf464`, producer `32b1b266e`, raw output `2c583ecbd`, countercheck `97ec73da3` (`5 / 5` plants caught), relay `b7e932dad`.
- **`AGY-C2` (`P-866`, `M4`, `B915`):** Card `ce676bb63`, producer `6ac571494` (passed first run with zero mends), raw output `9abf3e865`, countercheck `b25a7ae64` (`5 / 5` plants caught), relay `8c49a0d85`.
- **`AGY-C3` (`MC:GEN`, `B1677`, `X:CUSP`):** Card `dc31dda2b`, producer `14a52d371`, raw output `fa8880747`, countercheck `4c3162c75` (`5 / 5` plants caught), relay `7cdf9a39e`.
- **`AGY-C4` (`P-776`, `P-845`, `M6`):** Card `ccfcfe7f7`, producer `ecbdd2017`, raw output `8119b11be`, countercheck `3d07391fd` (`5 / 5` plants caught, zero finite differences), relay `2ed4e28de`.

## Three. Exact theorems and certified results (in words and exact rationals)

- **Closed-form resolution of `B1969` (`AGY-C1`, `pure math / invariant`):** In the Takagi basis `{e_+, e_-, e_3}` of `h = c_+ e_- + c_- e_+` (`2 c_+ c_- = r`), `Y(h; mu_+ e_+ + mu_- e_-, 0)` is monomial; at `r = 1 / 2000`, `w_u = w_d = 0`, `u_d = e_+ + (4 / 1000) e_-`, `u_u = (1 / 80000) e_+ + e_-` achieves `|V_CKM| = I_3` and full three-generation hierarchy (`m_2 / m_3 <= 1 / 100`, `m_1 / m_2 <= 1 / 10`) in both sectors, with exact threshold near `r_max = 1 / 1000` (`closed at r = 1001 / 1000000`).
- **Spinor pairing obstruction for `P-879` (`AGY-C1`):** Under `Sym^two(C^two)` contraction at `(h . h = 0, det M_w = 0)`, `sup |V_tb| = (1 + sqrt(1 minus gamma^two)) / (3 minus sqrt(1 minus gamma^two))` (`1 / 3` at `gamma = 1`; `|V_tb| >= 9 / 10` requires `gamma <= 6 sqrt(2) / 19`). Shared `Q_L` (`q_L = 1`) forces `gamma_res = 1` across all `2016` grid points and `0` continuous-`h` counterexamples under a `CP^two` Lipschitz–Weyl–Davis–Kahan branch-and-bound certifier on `12` Frame `C` points.
- **Shared holomorphic `(S, S)` two-doublet escape for `P-847` (`AGY-C1`):** Excluding anti-holomorphic `S_tilde` so `(H_u, H_d)` both couple through holomorphic `(S, S)` converts `gamma -> 1` from a rank-one obstruction into exact asymptotic CKM alignment (`|V_CKM| -> I_3` at large `y`) while preserving `B1945`'s exact three-generation exponents `(1 / 10, 3 / 5)` and `(3 / 10, 1 / 2)` (up) and `(1 / 5, 11 / 20)` (down), independent of `L`.
- **Linear `sl(W)^+` no-go and quadratic / order-fifteen `(B minus L)` splits (`AGY-C2`, `pure math / invariant`):** `dim (sl(W)^+)^{G_SM} = 1` (spanned by `6 Y`), so every linear `G_SM`-invariant exterior derivation of `B1953`'s `O(tau)` collapses to a scalar multiple of `F(tau)` (`leaving e and d identical`), while `(10, 6)` in `E_8` contains `0` `(15, 2, 2)` doublets. Sesquilinear `G_SM` invariants on `sl(W)^+` have dimension `3` (splitting normalised `H_3 / 3` vs `H_2 / 2` Weil Gramians by asymptotic ratio `3` without level `25`), and order-`15` twists break `(minus 3, 6) == (2, 1) mod 5` via quark denominator `3`.
- **Exact `9 / 5` two-doublet gauge slope (`AGY-C2`, `pure math / invariant`):** General `(n_H, n_T)` matter from `Lambda^1(C^5) = 3_{-2} (+) 2_{+3}` gives `(b_1 minus b_2) / (b_2 minus b_3) = (220 minus 2 n_H + 2 n_T) / (110 + 5 n_H minus 5 n_T) = 9 / 5` at holomorphy-forced `(n_H, n_T) = (2, 0)` (verified against Machacek–Vaughn two-loop rationals, reverting to `218 / 115` or `2` if `3_{-2}` survives).
- **Parabolic Milnor–Wood ceiling `2` (`AGY-C3`, `pure math / invariant`):** Every flat `U(3)` commutator `U_inf = [U_alpha, U_beta]` in `SU(3)` on `Sigma_{1, 1}` satisfies `N_par = sum theta_j = (3 minus d_inf minus eta(B_inf)) / 2` in `{0, 1, 2}` (never `3`). Across all `20 = |Aut(D_10)|` dihedral surjections of `4_1`, peripheral longitude acts as `I_16` on `Lambda^even(C^5)` while base `T` (`|G_T| = 96`, `ord(U_T) = 8`) has `theta = (0, 1 / 2, 1 / 2)` (`d_inf = 1 < 3`).
- **Unwrapped `48`-state cusp boundary and `3` families (`AGY-C3`):** On the level-`8` / level-`40` cusp-unwrapping cover (`|SL(2, Z / 40 Z)| = 46080`), peripheral longitude unwraps to `U_inf = I_48`, boundary Dirac reflection `Gamma^r` has signature `(48, 48)`, and one chiral Lagrangian `X:CUSP` selects `3` anomaly-free `16`-state chiral families at `0` `U(1)` flux.
- **`M6` zero-row cancellation and harmonic saddle no-go (`AGY-C4`):** Level-five twists satisfy `4 B_two(0) + 10 B_two(1 / 5) + 10 B_two(2 / 5) = 0`, `csc^two(pi / 5) + csc^two(2 pi / 5) = 4` (catching the card's hand-estimate `2`), `sum_{v != 0} G_v(tau) = minus 2 log(5)`, and `M6` zero-row bose-fermi cancellation of `+pi^two y / sin^two(pi b)`, while every zero-sum `G_v` or `F_u` supertrace is harmonic (`tr Hess = 0 => det Hess <= 0`).
- **Subharmonic `Gamma_0(5)` global minimum at `tau_* = (+-2 + i) / 5` (`AGY-C4`):** The base-plus-cover potential `V_{Gamma_0(5)}(tau) = minus pi log(y sqrt(5) |eta(tau) eta(5 tau)|^two)` has an imaginary-axis Fricke **saddle** at `tau = i / sqrt(5)` and its **strict global minimum** at `tau_* = (+-2 + i) / 5` (`tr Hess = 25 pi > 0`, `det Hess > 0`, `Re(tau_*) = +-2 / 5 != 0`, priced honestly with non-zero discrete potential-specification bits under Guardrail one).

## Four. Open premises left for `main` (honest boundary accounting)

- **Premise `X:HOL` (`AGY-C1`, `AGY-C2`):** Deriving holomorphic boundary chirality (`excluding S_tilde` and projecting out `3_{-2}` at the cusp) from the bulk `11D` / `7D` action rather than imposing it as a chiral boundary condition.
- **Premise `X:CUSP` and cover multiplicity (`AGY-C3`):** Deriving the specific half-rank chiral boundary condition on `C^3 (x) Lambda^even(C^5)` and reconciling cover deck multiplicity when passing to the level-forty finite cover.
- **Discrete potential-sign / cover-weight specification (`AGY-C4`):** Deriving the net bosonic-minus-fermionic sign and `Gamma_0(5)` base-plus-cover determinant weight from the full bulk+cusp field content (`priced with non-zero discrete specification bits until derived`), and testing in a future data-free study how `tau_* = (+-2 + i) / 5` interacts with finite-height Yukawa hierarchies.

## Five. Verification commands for `main`

- Check all four pre-committed script hashes: `shasum -a 256 -c relays/agy_2026-11-20_c1/SCRIPT_SHA256.txt relays/agy_2026-11-20_c2/SCRIPT_SHA256.txt relays/agy_2026-11-20_c3/SCRIPT_SHA256.txt relays/agy_2026-11-20_c4/SCRIPT_SHA256.txt`.
- Run all four zero-shared-code counterchecks (`20 / 20` planted faults caught, `0 of 19`): `for k in c1 c2 c3 c4; do PYTHONDONTWRITEBYTECODE=1 python3 relays/agy_2026-11-20_${k}/${k}_countercheck.py || break; done`.

0 of 19.
