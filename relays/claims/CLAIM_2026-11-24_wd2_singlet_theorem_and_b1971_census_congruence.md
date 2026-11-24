# CLAIM CARD — Card A2-B1972-OPEN (Blocks OPEN-2 & OPEN-3): Exact 3-factor det Y(h,s) law, Mark-Twin Singlet Alignment Dichotomy solving W-D2 §3-4, & closed-form congruence solving B1971's order-5 lock and B1963 (12) vs B1971 (8) reconciliation (0 of 19)

- seat, branch, commit: agy-002, origin/agy-002/verify, 5f252be77 (Producer v3, computed once) & 2f9eb0da2 (Cold-Room Referee run2, computed once)
- kind: theorem
- touches: A02, A03, A04, A05, A10, P-847, P-860, P-862, mixing, CKM, lepton factor, Higgs, mass
- effect: conditions — A03, A04, A05, A10, P-860, P-862, mixing, CKM, lepton factor (proves det Y(h,s)=(u.u+w^2)(h.h+s^2)(u.h-ws) and Mark-Twin Singlet Alignment Dichotomy: (S,S,S)+same-sign singlet achieves aligned O(1) 1st-gen lepton-down split ONLY at the twin (1/5,2/5), collapsing exponentially at the mark (2/5,4/5), with 2nd-gen split impossible at both; proves closed-form order-5 congruence & reconciles B1963 12 vs B1971 8)
- imports: none beyond Frame C's banked four-channel coupling (B1656, B1736, B1945) and singlet Higgs coupling H = R + s I_2 (W-D2)
- premises on main: B1656, B1736, B1739, B1943, B1945, B1949, B1963, B1969, B1970, B1971, B1972, P-847, P-860, P-862
- decisive script: relays/a2_b1972_open_v3/verify_a2_b1972_open_v3.py, SHA-256 b2f662a67d9d9039, depends on stdlib, sympy, mpmath (zero external files, zero subprocess, 100% sandbox-runnable), run as python3 relays/a2_b1972_open_v3/verify_a2_b1972_open_v3.py, output SHA-256 80edd2038eb49a0e
- second computation: agy-002 disjoint Cold-Room Referee run2 (relays/a2_b1972_open_referee/referee_a2_b1972_open_run2.py, SHA-256 0b79ecd2b17a4c47, output 7076eb58a199e8c2: direct 2x2 spinor contraction + mp.jtheta(3), agrees 0 discrepancies, max rel diff 2.81e-8); independently verifies chat1 W-D2 §3 (f25ec9069) and main B1971 N1-N5 (5988bd5de)
- already on main?: topic-sweep /W-D2|singlet|B1971|B1963|lepton.*down|null frame/ on VERDICT_LEDGER (27a9353e5): B1963, B1971, B1972 (B1972 names W-D2 §3 as #3 open item; B1971 names order-5 congruence & 12-vs-8 reconciliation as open)
- what would make it fail: PF-2 (opposite-sign singlet collapses |ln D_1| < 1e-45 [obs 4.3e-95]), PF-4 (wrong-sign s breaks W-D2 §3 by > 0.22), PF-5 ((S_tilde,S,S) destroys CKM alignment [min diag < 1e-26]), PF-6 (perturbing h lifts |V_13| by > 10^3x) + Guardrail-3 Haar U(3)^3 invariance (8.96e-77)

## Concise Statement of New Theorems (`0 of 19`, `computed once`)

1. **Exact 3-Factor Determinant Law & Analytic `W-D2 § 3` Window (`OPEN-2`):**
   - From `B1656`'s 2x2 spinor contraction, $Y(h, s; u, w) = u h^T + h u^T - (u\cdot h)I_3 + w[h]_\times - s(w I_3 + [u]_\times)$ obeys $Y(h, s; M^T) = Y(h, -s; M)^T$ identically (proving `W-D2 § 3`'s $Y_{\text{lep}}(R + s\mathbf{1}) = \lambda Y_{\text{down}}(R - s\mathbf{1})^T$, verified to `2.88e-61` / Ref `4.22e-106`) and factorizes identically as:
     $$\det Y(h, s; u, w) = (u\cdot u + w^2)(h\cdot h + s^2)(u\cdot h - w s) \implies \frac{\det Y_{\text{lep}}(h, s)}{\det Y_{\text{down}}(h, s)} = \lambda^3\,\frac{u\cdot h + w s}{u\cdot h - w s}.$$
   - This derives `W-D2 § 3`'s empirical window exponents analytically: $\kappa_* = |u\cdot h|/(|w| c_{\max})$ scales at exact rate $\varepsilon^{+1/10}$ (`0.10000000`) under `S` (`W_-`) and $\varepsilon^{+3/10}$ (`0.300000`) under `S_tilde` (`W_+`).
2. **Mark–Twin Singlet Alignment Dichotomy (`Solving W-D2 § 4`'s Two Uncomputed Questions):**
   - In the null basis $(n, \bar{n}, e)$, the leading singlet operator $u_e(\pm i I_3 + [e]_\times)$ equals $\operatorname{diag}(+2i, 0, +i)$ at the **mark `(2/5, 4/5)`** (`w/u_e = +i`) versus $\operatorname{diag}(0, -2i, -i)$ at the **twin `(1/5, 2/5)`** (`w/u_e = -i`).
   - Consequently, combining `(S, S, S)` with a same-sign singlet on down & leptons yields an exact structural selection dichotomy:
     - **Twin `(1/5, 2/5)` (`Q1 = YES`):** Singlet annihilates the light state $n$, preserving CKM alignment (`min |V_{ii}| = 0.9944 -> 0.9999895 -> 0.9999999804` across `y = 10, 20, 30`) and hierarchy (`r_{23} \le 0.00539`) while sustaining an $O(1)$ first-generation split **`|\ln D_1| = 2.206 -> 2.211 -> 2.211`** at $\kappa_* \sim \varepsilon^{1/10}$.
     - **Mark `(2/5, 4/5)` (`Q1 = NO`):** Singlet lifts the light state $n$ by $2\kappa_* \sim \varepsilon^{1/10} \gg m_2 \sim \varepsilon^{2/5}$, swapping the 1–2 states and breaking alignment; keeping `min |V_{ii}| >= 0.99` forces `|\ln D_1|` to collapse as $\varepsilon^{3/10}$ (`0.0263 -> 6.08e-4 -> 4.45e-5`).
     - **Second generation (`Q2 = NO` at both):** Wherever `r_{23} <= 10^{-2}`, `|\ln D_2|` vanishes exponentially (`<= 0.0105 -> 3.09e-4 -> 1.33e-5`).
3. **Closed-Form Proof of `B1971`'s Order-5 Lock & `B1963` (`12`) vs `B1971` (`8`) Reconciliation (`OPEN-3`):**
   - Independently confirms `B1971` `N1–N5` (`max rate err 3.77e-5`, $h\cdot h/(\eta^6/4)$ err `1.16e-76`).
   - Proves from leading theta phases that $u_j/u_k \to i(-1)^{\operatorname{nint}(a_+)+\operatorname{nint}(a_-)}$ and $w/u_e \to +i(-1)^{\operatorname{nint}(a_+ + 1/2)+\operatorname{nint}(a_- + 1/2)}$, so at order 5 all `20` nonzero-$a$ points obey $P_{\text{up}}(a) + P_{\text{dn}}(a) \equiv 1 \pmod 2$ (`24/24` exact predictions `[10, 10, 4]`), while at $a = 1/2$ both sectors satisfy $E_{1i} = 0, E_{jk} = 1/2$ matching the Higgs `e`-rate.
   - Reconciles `B1963` (`12`) vs `B1971` (`8`) to the exact integer: `B1971`'s `max(d_a, d_b) in {8, 10}` (`112` pts) gives `8` unaligned (`4` ord-8 + `4` ord-10 on `a=1/2`, `96` clean across ALL `x in {0, 0.13, 1/4, 1/2}` & `y in {10, 20, 30}`), whereas `B1963`'s `lcm(d_a, d_b) in {8, 10}` (`120` pts) adds `8` points of `max_denom = 5`: `4` on `a = 1/2` (all unaligned $\implies 8 + 4 = \mathbf{12}$) plus `4` on `b = 1/2` (all aligned).

0 of 19.
