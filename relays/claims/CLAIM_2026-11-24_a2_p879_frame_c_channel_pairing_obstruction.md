# CLAIM CARD — Card A2-P879: Exact Frame C channel-pairing obstruction (spinor Mobius law sup |V33| = (1+s_L)/(3-s_L), order-5 zero law w_u = 0, shared-Q_L rank-1 residue s_L^res = 0, & global CP^2 interval exclusion) (0 of 19)

- seat, branch, commit: agy-002, origin/agy-002/verify, 10437a80b (Producer v5) & 01466ab8a (Cold-Room Referee v3)
- kind: theorem
- touches: A02, A03, A04, A05, A09, P-879, mixing, CKM, Higgs, mass
- effect: conditions — A04, A05, P-879, mixing, CKM (closes P-879 analytically and by deterministic CP^2 interval certification: near-null alignment >= 9/10 requires left-spinor misalignment s_L >= 17/19, whereas Frame C's shared q_L = 1 forces s_L^res = 0 identically and keeps full-weight s_L < 2/5 -> 0 asymptotically across all heights Im tau -> oo)
- imports: none beyond Frame C's banked four-channel coupling (B1656, B1736, B1838, B1945) and Theorem 90 horoball channel weights (B1927, B1940)
- premises on main: B1656, B1736, B1838, B1927, B1940, B1966, B1967, B1968, B1969, B1971, B1972, P-879
- decisive script: relays/a2_p879_v5/verify_a2_p879_v5.py, SHA-256 8db5e4f770a6b5dd, depends on stdlib, sympy, mpmath, numpy (zero external files, zero subprocess, 100% sandbox-runnable), run as python3 relays/a2_p879_v5/verify_a2_p879_v5.py, output SHA-256 1c764eb437db06a1
- second computation: agy-002 disjoint Cold-Room Referee v3 (relays/a2_p879_referee_v3/referee_a2_p879_v3.py, SHA-256 67e521a3eae26588, output 52413e29b185edfb: independent RK4 Weierstrass L_2 + 316-pt CP^2 certifier, agrees 9/9); main B1971 (5988bd5de, dated correction) independently confirmed T1, T4(a), and T4(b)
- already on main?: topic-sweep /B1966|B1967|B1968|B1969|B1971|P-879/ on VERDICT_LEDGER (27a9353e5): 5 arcs; closest B1968, B1971, B1972 (B1972 names A2-P879 as #1 open Tier-A item)
- what would make it fail: B1967's 16-rational counterexample witness (s_L = 0.9537 > 17/19) must remain UNPRUNED by the CP^2 certifier (verified: 310,250 boxes Producer / 9,712 boxes Referee survive) + 5/5 planted controls PF1..PF5 & 10-trial Haar U(3)^3 invariance (< 9e-14)

## Summary of Certified Theorems (`T1–T5`, `0 of 19`, `mended expectations` per Errata 1–4)

- **`T1` (Canonical `2x2` Null Reduction & Exact Proof of `B1966 E4`):** Unitary $h_0$-frame collapses $Y(h_0; u, w)$ to $A = \bigl(\begin{smallmatrix}2(u\cdot\bar{h}_0) & u\cdot e_3 + i w \\ u\cdot e_3 - i w & -(u\cdot h_0)\end{smallmatrix}\bigr)$ with $\det A + (w^2 + u\cdot u) = 0$ identically (`< 3e-15`).
- **`T2–T3` (Exact Spinor Möbius Law):** Maximizing $|V_{33}^{(0)}|$ over unit Higgs spinors at $r = |h\cdot h| = 0$ yields $\sup_{\|\xi\|=1} |V_{33}^{(0)}| = \frac{1 + s_L}{3 - s_L}$, forcing $s_L \ge 17/19$ for $|V_{33}| \ge 9/10$ (ceiling $1/3$ at $s_L = 0$; `B1967` escapes at $s_L = 0.9537$).
- **`T4` (Order-5 Zero Law & Shared-$Q_L$ Asymptotic Exclusion):** Up $(1,-4)$ forces $w_u = 0$ identically on all `24` order-5 points; shared $q_L = 1$ forces $s_L^{\text{res}} = 0$ across all `36` torsion points (`< 6e-16`), and full-weight $\max s_L$ peaks at `0.3881 < 2/5` (`y=2`) and falls monotonically to `< 1/1000` by `y = 30`, closing the near-null corridor for all heights $\operatorname{Im}\tau \to \infty$.
- **`T5` (Deterministic Global `CP^2` Certifier):** Proves `0` surviving counterexample boxes across `192` Producer / `316` Referee grid points + `72` / `48` $L_2 \pm 1/50$ perturbations while keeping `B1967`'s witness unpruned.

0 of 19.
