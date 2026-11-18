# Card `X-P1` — Exterior-Algebra Operator Join (`B1955` Open `#1`), Symmetry-Point Nullity (`P-874 Q2`), and Pure-Math Checks of `W-P1` and `C3i` (`P-875 Q2`)

`2026-11-18` (`0 of 19`, strictly data-free, expectations and script committed before first execution).

## 1. The package and the question, in one sentence

Do the four open data-free mathematical questions on the board after `M42` — joining `B1953`'s covariant level-`5` operator $O(\tau)$ with `B1951`/`B1955`'s exterior matter algebra $\Lambda^{\mathrm{even}}(W)$ (`B1955` Open `#1`), testing `W-L1`'s symmetry-point vanishing criterion without data (`P-874 Q2`), independently checking the `web` seat's `Card W-P1` (`2f2e490e1`) including its open § `5` item `2`, and independently checking the `physical` lane's hand proof `Card C3i` (`P-875 Q2`, `bae5f09e3`) — hold under exact symbolic and `50`-digit computation?

## 2. What will be delivered, and what done means

One self-contained pure-math script `relays/x_p1_verify/verify_x_p1.py` (`committed with relays/x_p1_verify/SCRIPT_SHA256.txt before its first run`), its raw output `relays/x_p1_verify/verify_x_p1_out.json` (`committed in its own commit before analysis`), and one mask-clean delivery note `relays/AGY_EXP_TO_MAIN_2026-11-18_X_P1_EXTERIOR_JOIN_SYMMETRY_NULLITY_WP1_AND_C3I.md` covering four exact modules:

1. **Module `J` (`B1955` Open `#1` — Linear Adjoint-Wedge Wall vs Five-Multiplet Exterior-Derivation Gramians):**
   - Classify all $\mathfrak{sl}(5)$-invariant linear trilinear maps $\mathfrak{sl}(W) \otimes \Lambda^2(W) \otimes \Lambda^2(W) \otimes \Lambda^1(W) \to \Lambda^5(W)$ (`up`) and $\mathfrak{sl}(W) \otimes \Lambda^2(W) \otimes \Lambda^4(W) \otimes \Lambda^4(W) \to (\Lambda^5 W)^{\otimes 2}$ (`down/lepton`); test whether both spaces have exact dimension `2`, close single-valuedly at level `5` across all `120` elements of $\mathrm{SL}(2, \mathbb{F}_5)$ in both Weil classes $a \in \{1, 2\}$, give the exact Georgi–Jarlskog ratio $-3 = (+15/4)/(-5/4)$ on the traceless $\overline{\mathbf{45}}$ channel, **yet** collapse on $S(U(3)_c \times U(2)_w)$-invariant Yukawa blocks to scalar multiples of `B1953`'s single phased sum $F(\tau)$ (`linear proportionality wall`).
   - Lift $O(\tau) = O_{\mathbf{3}}(\tau) \oplus O_{\mathbf{2}}(\tau)$ via the $\mathrm{GL}(W)$-equivariant exterior derivation $d_{O(\tau)} = \sum_{w \neq 0} \tilde{Y}(\tau, w) \otimes d_{D(w)}$ to $\mathcal{F} \otimes \Lambda^2(W)$ (`30 x 30`) and $\mathcal{F} \otimes \Lambda^4(W)$ (`15 x 15`), extract the five normalized partial-trace family Gramians $\mathcal{G}_R(\tau) = \frac{1}{\dim R}\operatorname{Tr}_R(d_O d_O^\dagger)$ for $R \in \{Q, u^c, d^c, L, e^c\}$, and test the closed-form `3 x 3` matrix decomposition $(\mathcal{G}_{e^c}, \mathcal{G}_L, \mathcal{G}_{d^c}, \mathcal{G}_{u^c}, \mathcal{G}_Q) = (\frac{1}{4}FF^\dagger, \frac{1}{2}G_{\mathbf{2}}, \frac{1}{3}G_{\mathbf{3}}, \frac{1}{3}G_{\mathbf{3}} + \frac{1}{12}FF^\dagger, \frac{1}{3}G_{\mathbf{3}} + \frac{1}{2}G_{\mathbf{2}} - \frac{1}{12}FF^\dagger)$, hypercharge-square specialization $(36, 9, 4, 16, 1)/144$, exact `3 x 3` matrix Schur–Plancherel identity $6\mathcal{G}_Q + 3\mathcal{G}_{u^c} + \mathcal{G}_{e^c} = 3(G_{\mathbf{3}} + G_{\mathbf{2}}) = 15\sum_{w \neq 0} Y(\tau, w)Y(\tau, w)^\dagger$, `SL(2, Z)` covariance at two generic rational base moduli in both readings and both channel conventions, pairwise distinctness across all `5` multiplets, and `10`-trial random Haar unitary invariance.
2. **Module `Z` (`P-874 Q2` — Firewall-Clean Symmetry-Point Vanishing & Schur Intertwining Test at $\tau = i$ and $\tau = \rho = e^{2\pi i / 3}$):**
   - Without printing any non-zero singular-value ratio or mixing angle at $\tau = i$ or $\tau = \rho$, compute at `50` digits the stabilizer intertwining unitaries $(c(\gamma, \tau_*), U_L(\gamma, \tau_*), U_R(\gamma, \tau_*))$ (`\gamma = S at \tau_* = i, \gamma = ST at \tau_* = \rho`), their exact Schur character multiplicities, and the exact integer nullities $\dim\ker \in \{0, 1, 2, 3\}$ and eigenvalue-degeneracy patterns of $F(\tau_*), G_{\mathbf{3}}(\tau_*), G_{\mathbf{2}}(\tau_*), \mathcal{G}_Q(\tau_*), \mathcal{G}_{u^c}(\tau_*)$ (`both readings S and \tilde{S}, residue and channel-weighted`).
3. **Module `W` (`Chartered Pure-Math Check of Web Card W-P1` at `2f2e490e1` + `W-P1` § `5` Item `2`):**
   - Recompute independently from `W-P1`'s prose statements alone items `P1`–`P3` and `W1`–`W4`, and test `W-P1` § `5` item `2`: whether `"what the act does"` eliminates either reading (`S` vs `\tilde{S}`) or either sign of the quartic anisotropy $B$ on the Higgs ground plane $E$.
4. **Module `C` (`P-875 Q2` — Independent Symbolic Clifford & Cochain Check of Physical Card `C3i` at `bae5f09e3`):**
   - Recompute in `32 x 32` $\mathrm{Cl}(10)$ (`covering both 16_+ and 16_- half-spinors`) and on the `4`-degree Dolbeault–Koszul complex equations `(1)`–`(7)` of `GLOBAL_CYCLIC_CROSS_FORM_CHAIN_MAP.md`: polynomial identity $Q^2 = p r(e_{13} + e_{24}) + p f(e_{31} + e_{42})$, commutator ratios $(1, 1/\sqrt{2}, 1/\sqrt{2}, 1/2)$, F-flatness $[a_N, Q] = [a_N, R] = 0$, exact chirality proportionality $Q_{32}^2 R_{32}^2 = -3i\gamma_{\mathrm{chir}} A_{32}$ (`opposite signs \mp 3i on 16_+ vs 16_-`), vector-`10` vanishing $Q_{\mathrm{vec}}^2 R_{\mathrm{vec}}^2 = 0$, chain isomorphism $(1 + H)d_N(1 - H) = d_N + \beta P_N$ with $H^2 = H d_N H = 0$ and $[d_N, H] = -\beta P_N$, core-swap invariance of $h_F$, `24 / 16 / 8` `chi = 0` divisor kernel persistence under $1 + H$, and quadratic norm growth $\|(1 + H)^n x\|^2$ on $H x \neq 0$.

## 3. How it could come out wrong, written before any run

- **Module `J`:** If a third $\mathfrak{sl}(5)$-invariant linear channel existed or if $\operatorname{Tr}(D(w)\cdot 6Y)$ varied with $w$, linear contractions could split $s_2/s_1(e)$ from $s_2/s_1(d)$ (`falsifying the linear proportionality wall`); conversely, if $\mathcal{G}_Q$ failed positive-semidefiniteness, failed `SL(2, Z)` covariance, or collapsed to a multiple of $\mathcal{G}_{d^c}$, the five-multiplet exterior Gramian lift would fail.
- **Module `Z`:** Each readout at $\tau_* \in \{i, \rho\}$ either has positive integer nullity $\dim\ker \ge 1$ forced by Schur character mismatch (`satisfying W-L1's exact-zero criterion for at least one lighter generation`) or has $\dim\ker = 0$ (`eliminating that readout at \tau_* under W-L1's criterion`). Both possibilities are recorded as exact integer nullities before any look.
- **Module `W`:** Any mismatch on `P1`–`P3` or `W1`–`W4` gives `DIFFERS`; on `W-P1` § `5` item `2`, if $\gamma$ broke `1`-turn projectively covariant repetition for either $S$ or $\tilde{S}$ (`as it does for S*`), or moved $|\Delta|/N$ on $E$, the net count would become negative (`falsifying our expectation that net count remains zero`).
- **Module `C`:** Any residual $\neq 0$ in `[a_N, Q]`, `Q_{32}^2 R_{32}^2 + 3i \gamma_{\mathrm{chir}} A_{32}`, `\delta h_F + h_F \delta - Q^2 R^2`, or `(1 + H) d_N (1 - H) - (d_N + \beta P_N)` (`or wrong sign in [d_N, H] = -\beta P_N`) gives `DIFFERS` on `C3i`'s algebraic core.

## 4. What it rests on, and what it must not touch

- **Rests on:** `B1927`, `B1945`, `B1951`, `B1953`, `B1955`, `P-873`, `P-874`, `P-875` (`at main 23cd5a5ca`), `web` `W-P1` (`2f2e490e1`), and `physical` `C3i` (`bae5f09e3` / `5b0a80be7`).
- **Firewall (`must not touch`):** Zero measured Standard Model or cosmological quantities (`0 of 19`), zero held-out ratios (`UR-3` untouched), zero continuous singular-value ratios or CKM/Jarlskog numbers computed or printed at $\tau = i$, $\tau = \rho$, or any candidate address, and zero imports from `main` or other seats' code.

## 5. Five planted controls that must fail if the work is broken

1. **`PC_XP1_1` (`Dropped coboundary phase table`):** Removing $\zeta^{-ab}$ from $O(\tau)$ must break `SL(2, Z)` singular-value-ratio invariance of the exterior Gramians $\mathcal{G}_R(\tau)$ by `> 1/10`.
2. **`PC_XP1_2` (`Untraceless 45 tensor`):** Omitting the $+\frac{1}{4}(\delta^i_j(A^T\bar{H})_k - \delta^i_k(A^T\bar{H})_j)$ trace subtraction in $\mathfrak{sl}(5) \otimes \overline{\mathbf{5}}$ must change the lepton-to-down ratio from $-3$ to $-3/2$.
3. **`PC_XP1_3` (`Non-covariant S* reading`):** Replacing $S$ or $\tilde{S}$ with $S^*$ along the golden axis must break `1`-turn projectively covariant repetition (`drift > 1/10` at `1` turn, returning at `3` turns).
4. **`PC_XP1_4` (`Wrong Weil Fourier sign`):** Replacing $-2axy$ with $+2axy$ in `W-P1`'s Fourier matrix must have no scalar $c \neq 0$ satisfying $(cF)^2 = ((cF)T)^3$.
5. **`PC_XP1_5` (`Omitted Koszul sign & vector-10 control on C3i`):** Omitting $(-1)^l$ in $d_N = \bar{\partial} + (-1)^l\delta$ must break $(1 + H)d_N(1 - H) = d_N + \beta P_N$, and evaluating $Q_{\mathrm{vec}}^2 R_{\mathrm{vec}}^2$ on the vector `10` must give `0` while the cross-generator is non-zero.

## 6. Needs from `main` or other seats

Nothing needed to execute; delivered as a compact data-free mathematical check after `HARVEST COMPLETE` (`4a8b433a2`) for `main`'s independent recomputation when `P-874` and `P-875` are taken up.

`0 of 19.`
