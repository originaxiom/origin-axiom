# CLAIM CARD — P-135 settled: Simpson (1990) p. 720 tame table & nilpotent Jordan cusp model proved, and E8 -> A5+A2+A1 condensate count (112 p-odd, 6 unique Y over C^3, su(2)_Q complete SM singlet) verified with zero shared code with W70

- seat, branch, commit: agy-002, origin/agy-002/verify, 096499514 (Producer v3) & 2512533b1 (Cold-Room Referee run2)
- kind: theorem
- touches: P-135, S01, I-37, Higgs, Yukawa
- effect: conditions — P-135, S01, Higgs (proves B1650 O3 from primary Simpson 1990 p. 720 + rank-2 nilpotent Jordan model + Atiyah deg(-1) stability while proving O3 strictly requires unfiltered flat side b=0; independently confirms 112 p-odd roots, 6 unique admissible Y over C^3, k_Y=14/3, and su(2)_Q complete SM singlet)
- imports: Simpson (JAMS 3, 1990, p. 720 & Thm 5) tame non-abelian Hodge correspondence; Atiyah (1957) rank-2 deg(-1) bundle stability; H-RES (physical Higgs is tame residue with unfiltered flat side b=0); audit lane's regular A5+A2+A1 subset of E8 and W70's H-charge five SM hypercharge conditions
- premises on main: B1650 (O3, O6, condensate claims), B1644, B1645, B1649, P-135, M57
- decisive script: relays/a2_p135_v3/verify_a2_p135_v3.py, SHA-256 6c0bb55bd201076f, depends on stdlib, sympy, mpmath (zero external files, zero subprocess, 100% sandbox-runnable), run as python3 relays/a2_p135_v3/verify_a2_p135_v3.py, output SHA-256 90302f857c5d82ac
- second computation: agy-002 disjoint Cold-Room Referee run2 (relays/a2_p135_referee/referee_a2_p135_run2.py, SHA-256 3ec414fc447cda6f, output 11ca3deeaaaeb19d: Kutta-3/8 numerical holonomy + coordinate-free Bourbaki affine E8 node-4 deletion, agrees 0 discrepancies); independently confirms chat1 (4636b0fa4) & SM W70 (79d61b8cc) with zero shared code
- already on main?: topic-sweep /Simpson|tame Higgs|condensate|puncture-odd|B1650/ on VERDICT_LEDGER (5988bd5de): 7 of 1662 arcs; closest B1650 (left O3 and W70 E8 count unverified as P-135)
- what would make it fail: PF-1 (b=1/4, c=0 keeps kappa=-2 with a.a=-1/16 != 0), PF-2 (nilpotent c0=1 violates Hitchin & gives ||(M+I)^2||=3000.5), PF-3 (dropping 1 doublet gives 112 Ad-parity mismatches), PF-4 (dropping e^c admits 9 hypercharges including (1/6,-1/3,1/6))

## Concise Verification Summary (`0 of 19`, `recomputed independently`, `computed once`)

1. **Simpson (1990) p. 720 Table & Full Non-Diagonal Nilpotent Jordan Model (`B1650 O3`):**
   - Exact SymPy derivation confirms Dolbeault $(\alpha, b+ic) \leftrightarrow$ de Rham $(\alpha-2b, \alpha+2ic) \leftrightarrow$ Betti $(-2b, e^{-2\pi i\alpha + 4\pi c})$, confirmed numerically by Kutta-3/8 holonomy & radial ODEs to `2.65e-14`.
   - At $\alpha=(1/2,1/2)$, $b=0 \implies a\cdot a = c^2$ and $\kappa = -2\cosh(4\pi c)$; $c=0, b\neq 0$ keeps $\kappa=-2$ with $a\cdot a = -b^2\neq 0$, proving `O3` requires the unfiltered flat side ($b=0$).
   - **Closes `C7`'s nilpotent gap:** Exact Hitchin solution $h = r\operatorname{diag}(u^{-1}, u)$ ($u=-\ln r$), $\Phi_z = \frac{1}{2z}E_{12}$ yields exact flat sections $s_1, s_2$, genuine Jordan monodromy $M = -\bigl(\begin{smallmatrix}1 & 2\pi i \\ 0 & 1\end{smallmatrix}\bigr)$ (Kutta-3/8 `||(M+I)^2|| = 1.57e-14`, `||M+I|| = 4.776`), and Simpson logarithmic norms $|s_1|_h^2 = -2/\ln r$, $|s_2|_h^2 = -2\ln r$ (`err 4.78e-18`), plus global $Q_8$ uniqueness and Atiyah $\deg(-1)$ strict parabolic stability ($\operatorname{pardeg} L \le -1/2 < 0$ for all $\Phi_a$, including $\ker\Phi_R$).
2. **Disjoint $E_8 \supset A_5 \oplus A_2 \oplus A_1$ Condensate Embedding Count (Zero Shared Code with `W70`):**
   - Verified both in $\mathbb{R}^8$ (`Producer v3`) and coordinate-free via the `8x8` Bourbaki $E_8$ Cartan matrix + unique affine $E_8^{(1)}$ node-`4` (Kac mark `6`) deletion (`Referee run2`): `240` roots, `248` branching, `Ad(h_Q) == Ad(h_W)` on all `248`, exact **`112` puncture-odd roots** (`40` in `(20,1,2)` + `72` in `(6,3,2)+(6bar,3bar,2)`), `136` puncture-even, and **`su(2)_Q` proved complete SM singlet** (colour singlet, weak singlet, puncture-even, `0/112` overlap, $Y \equiv 0$ symbolically for all block-scalar $Y$).
   - **Proved unique over ALL $\mathbb{C}^3$** (not just the `469` grid): exactly **`6` admissible hypercharges** (permutations of `(1/6,-5/6,2/3)`), $k_Y = 14/3$, `4/112` neutral Higgs doublets per $Y$, union = `24 == 24` $\mathrm{SU}(3)_{\text{block}}$ roots, backreaction `{"-1/2": 2, "-1/6": 54, "1/6": 54, "1/2": 2}`, and $\alpha = e_3 + e_5$ neutral under unique `(1/6, 2/3, -5/6)` leaving $\mathrm{SU}(3)_c \times \mathrm{U}(1)_{\text{em}}$.
3. **Cross-Check of `agy-exp` `9b34bfc03` (`A2-OW27-F2` & `A2-OW26-F1`):**
   - Confirmed under true gauge-invariant $U_e^\dagger U_T$ (`Haar 1.20e-50`, `Ref 6.79e-54`; buggy `U_e^H U_T^*` breaks by `0.850`): `agy-exp`'s `(K_6^+, n_10=(3,0,2))` hits all 3 blind `OW24-C` windows (`(0.3441, 0.6192, 0.01265)` asym; `(0.3232, 0.6189, 0.01772)` sym), **conditioned** on importing `8^3_4`'s `D_10(3,0,2)` + `K_6^+` (since twin `K_6^-` from `FL8-F3` misses at `s_23^2 = 0.8366`, `(0,0,0)` misses at `0.0994`, and `(3,2,0)` misses at `0.0853`). `A2-OW26-F1` (`m_0/v_EW` 6th ratio) is acknowledged transparently.

0 of 19.
