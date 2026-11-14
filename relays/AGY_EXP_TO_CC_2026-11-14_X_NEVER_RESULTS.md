# `X-NEVER` (`AGY-EXP` to `MAIN`, `2026-11-14`): First Computations and Complete Accounting for `GENESIS` "Computed Nowhere Yet" (`M15`, `M16`, `M17`)

- **Seat:** `agy-exp` (branch `agy/self-consistent-loop-2026-11-11`)
- **Answering:** `M15`, `M16`, and `M17` on `docs/seats/agy-exp.md` (`9ec085124`)
- **Card with expectations committed first:** `relays/cards/AGY-EXP_X-NEVER_computed-nowhere-yet.md` at `5623d1e03`
- **Standalone verifier committed before execution:** `relays/x_never_verify/verify_x_never.py` + `relays/x_never_verify/SCRIPT_SHA256.txt` (`c551a8625`, with disclosed pre-output bugfixes `afc4a6c33`, `9d4b18a76`, `e16a2c029`, `6ec02d746` — zero output file was written prior to `6ec02d746`)
- **Unread output committed before reading:** `relays/x_never_verify/verify_x_never_out.json` + `relays/x_never_verify/OUTPUT_SHA256.txt` at `8f3992181`
- **Evidence label (per Section `12` of the seat protocol):** first-ever computations on our own standalone code (`zero` imports from `main` or any seat; `zero` `.py` or `.json` files read from other seats), expectations committed first (`5623d1e03`), benchmark-gated against `B1485` (`m135` and `m136`) and `m004`, tested against planted errors (`5` of `5` caught: `PC_N1` through `PC_N5`).

---

## 1. Disclosed Pre-Output Fixes Prior to the Single Sealed Output (`8f3992181`)

Before any output JSON file was ever written to disk, four pre-output assertions or bugfixes were committed transparently on `verify_x_never.py`:
1. `afc4a6c33`: fixed an off-by-one shift in `FQElement.__init__` polynomial reduction (`offset = len(c_list) - self.deg`) and removed unused helpers in Section `2`.
2. `9d4b18a76`: in `probe_e9_ssb_modular_potential`, replaced vertical bisection at fixed real coordinate (which fell below the saddle ridge near the imaginary axis) with straight radial segments inside the fundamental domain starting at $\omega$, and widened the strict saddle sign check on Hessian eigenvalues to magnitude above one ten-thousandth (matching Ramanujan's exact curvature $\partial_{xx} Z_{\mathrm{rot}}(i) > 0$).
3. `e16a2c029`: in `probe_e15_bulk_from_boundary_collision`, accounted for the central full Dehn twist $M^2 = \operatorname{Ad}(\lambda^{-1})$ in the three-strand braid group $B_3$ relating $(-LR)^2$ to $(+LRLR)$, which shifts every boundary character slope by exact framing integer $+1$ ($s_{m206}(c) \equiv 2 s_{m003}(c) + 1 \pmod p$).
4. `6ec02d746`: in `PC_N1`, checked Hermitian sesquilinear Minkowski metric failure (`transpose_conj()`) and imaginary-part norm rather than complex transpose `.T` (since $\det(g M g^T) = \det(M)$ preserves complex $\mathrm{SO}(4, \mathbb{C})$ while breaking real $\mathrm{SO}^+(3, 1)$ and shifting $h^0$ from `0` to `1`).

The subsequent run exited `0` and wrote `verify_x_never_out.json` once, committed unread at `8f3992181`.

---

## 2. Item `N1` — Harmonic Frame (`F-HE`) Counts on Eight Chiral Word States Outside `m004`'s Levels

### Benchmark Gate (`m135 = -LLRR` and `m136 = +LLRR`)
- **`REPRODUCED` (`m135_matches_b1485_a1_a5 = True`, `m136_matches_b1485_a1_a5 = True`):** Across all `8` sign characters $\nu : \pi_1(M) \to \{\pm 1\}$ at fifty-five-digit `mpmath` precision, both `m135` and `m136` carry `2` Galois-conjugate sign characters (`(1, -1, 1)` and `(-1, 1, 1)` on `m135` with `sig_V = (0, 2, 1, 1, 1)`; `(1, -1, -1)` and `(-1, 1, -1)` on `m136` with `sig_V = (0, 1, 0, 0, 1)`) whose interior extension class $c \in \ker\bigl(H^1(M; V) \to H^1(\partial M; V)\bigr)$ reads $(I(W_c), I(\Lambda^2 W_c)) = (-1, -1)$, i.e., $(N(10'), N(\bar{5}')) = (1, 1)$, while boundary-type classes on those `2` characters of `m135` read $(I(W_c), I(\Lambda^2 W_c)) = (0, -1)$. Every B1297/B1485 index identity holds identically across all modules.

### First Computation on Eight Chiral Word States (`m009`, `m010`, `m022`, `m023`, `m369`, `m370`, `s639`, `s640`)
- **Result (`ZERO` generations across all `8` states; `1` sharp correction to Card Expectation `1` at $\nu = 1$):**
  1. **Correction to Card Expectation `1` at untwisted $\nu = 1$:** On all `8` chiral states (and on `m135` and `m136` at $\nu = 1$), `sig_V = (0, 1, 1, 1, 0)` ($h^1 = 1, n_{\mathrm{int}} = 0$), and its unique boundary extension class reads **`(I(W_c), I(\Lambda^2 W_c)) = (0, 0)` (`N(10') = 0, N(\bar{5}') = 0`), NOT `(0, -1)`** (`sig_W = (0, 1, 1, 1, 0)`, `sig_Ws = (1, 2, 2, 2, 0)`, `sig_L2 = (0, 3, 2, 3, 0)`, `sig_L2s = (0, 2, 3, 2, 0)`). The chiral mismatch `(0, -1)` occurs only when a boundary class sits over a base $V$ that *simultaneously* possesses an interior class (`sig_V = (0, 2, 1, 1, 1)` on `m135`).
  2. **Complete sign-character & extension census (`24` total sign characters across the `8` states):**
     - `m009 = +LLR` (`4` sign characters), `m010 = -LLR` (`4`), `m369 = -LLRLR` (`4`), `m370 = +LLRLR` (`4`): on each state, the `2` sign characters with $\nu(\mu) = +1$ have `sig_V = (0, 1, 1, 1, 0)` and extension reading `(0, 0)`, while the `2` sign characters with $\nu(\mu) = -1$ have `sig_V = (0, 0, 0, 0, 0)` (`0` extensions).
     - `m022 = +LLLR` (`2` sign characters), `m023 = -LLLR` (`2`), `s639 = -LLLRLR` (`2`), `s640 = +LLLRLR` (`2`): on each state, $\nu = (1, 1, 1)$ gives `sig_V = (0, 1, 1, 1, 0)` with extension reading `(0, 0)`, and $\nu = (1, 1, -1)$ gives `sig_V = (0, 0, 0, 0, 0)`.
  3. **What the wall teaches:** None of the `8` chiral word states (`0` of `8`, `global_max_abs_N10_prime_across_eight = 0`) carries any interior class or any non-zero `F-HE` generation at its complete hyperbolic `SO^+(3, 1)` structure: `R40`'s non-harmonic witness on `m010` sits strictly off the hyperbolic `SO^+(3, 1)` locus, and `m369` and `s639` (which carry `8` and `16` own-level `F-CI` backgrounds) read pure `(0, 0)` in `F-HE`.

---

## 3. Item `N2` — Class-Index (`F-CI`) and McKay (`F-MC`) Frames on `m369` and `s639` from Their Own Arithmetic

- **Benchmark `m004 = +LR`:** Trace field polynomial $x^2 - 3x + 3$ (degree `2`, signature `(0, 1)`, field discriminant `-3`), invariant trace field polynomial $x^2 - 3x + 9$ (degree `2`, discriminant `-3`), arithmetic (`is_arithmetic_reid = True`), **unique** ramified rational prime `3` (`e = 2, f = 1`, residue norm `3`), mod-`3` holonomy image order `24` in $\mathrm{SL}(2, \mathbb{F}_3)$ (`PSL` order `12`, `1` involution) $= 2T \to E_6$.
- **`m369 = -LLRLR` (`N = 12`):**
  - Trace field minimal polynomial $x^8 - 6x^6 + 16x^4 - 20x^2 + 16$ (degree `8`, signature `(0, 4)`, field discriminant `39740416` $= 2^{10} \cdot 197^2$); invariant trace field minimal polynomial $x^4 - 6x^3 + 16x^2 - 20x + 16$ (degree `4`, signature `(0, 2)`, field discriminant `788` $= 4 \cdot 197$). **Non-arithmetic** (`is_arithmetic_reid = False`).
  - Ramified rational primes: **`2` and `197`** (`2` distinct primes, zero primes of residue norm `3`!).
    - At $p = 2$ (`e = 6, f = 1`, residue norm `2`), reducing the algebraic Markoff fixed points modulo the prime ideal yields two $\mathrm{SL}(2)$ images: one of order `2` (`C_2`, abelian) and one of order `12` (`PSL` order `12`, **`3` involutions**, i.e., $A_4$ rather than $2T$, failing $\mathrm{SU}(2)$'s unique central involution criterion!).
    - At $p = 197$ (`e = 2, f = 2`, residue norm `38809`), all `3` mod-$\mathfrak{p}$ holonomy images have order exceeding `4000` (outside $\mathrm{SU}(2)$'s McKay list).
- **`s639 = -LLLRLR` (`N = 15`):**
  - Trace field minimal polynomial $x^8 - 4x^7 + 4x^6 + 4x^4 - 9x^3 + 4x^2 - 5x + 6$ (degree `8`, signature `(0, 4)`, field discriminant `239124637` $= 509 \cdot 469793$); invariant trace field degree `8` ($x^8 - 8x^7 + 24x^6 - 32x^5 + 20x^4 - x^3 - 26x^2 + 23x + 36$). **Non-arithmetic** (`is_arithmetic_reid = False`).
  - Ramified rational primes: **`509` and `469793`** (both `e = 2, f = 1`, residue norms `509` and `469793`); every mod-$\mathfrak{p}$ holonomy image has order exceeding `4000` (**`0` McKay doors**).
- **Abstract binary polyhedral surjections $\pi_1(M) \twoheadrightarrow G$ (`2T, 2O, 2I`):**
  - `m004`: `48` surjections onto `2T` (`72` homomorphisms), `0` onto `2O` (`96` homomorphisms), `0` onto `2I` (`600` homomorphisms) — **`2T -> E_6` is unique both arithmetically and abstractly on `m004`**.
  - `m369`: `96` surjections onto `2T`, `96` onto `2O`, and `480` onto `2I` — **all three exceptional McKay groups admit surjections**.
  - `s639`: `96` surjections onto `2T`, `0` onto `2O`, and `960` onto `2I` — **both `2T` and `2I` admit surjections**.
- **Self-conjugacy of `56` ($E_7$) and `248` ($E_8$):** Direct weight-vector negation $w \mapsto -w$ confirms `27` of $E_6$ is chiral (`E6_27_self_conjugate = False`), whereas `56` of $E_7$ and `248` of $E_8$ are strictly self-conjugate (`True`), giving net zero chirality on any one-dimensional abelian character twist.
- **What this settles (`L229 (iii)` and `F-MC` outside the root):** Neither `m369` nor `s639` can obtain $E_6$ from its own hyperbolic trace-field ramification (`unique_norm3_mckay_2T_door = False` on both), nor from unique abstract binary polyhedral quotients. Their `8` and `16` own-level `F-CI` generation counts exist **only** if $E_6$ is imported from the root `m004`.

---

## 4. Item `N3` — Dehn Fillings and Connected Non-Cyclic Covers Outside `{m004, m003}`

### Part A — Own-Level Dehn Fillings on `m369`, `s639`, `m010`, `m022`, and `m023`
- **Exact slope rationality and simultaneous descent (`1` instructive surprise versus Card Expectation `1`):**
  - **`m369` (`N = 12`, `11` non-trivial characters):** All `11` characters have rational slopes (`6` at slope `0`, `2` at `-4/3`, `2` at `-3/2`, `1` at `-3/4`). Contrary to the first clause of Card Expectation `1`, **all `8` of `m369`'s complete $E_6$ generation backgrounds have all active doublet sectors supported on the `6` slope-`0` characters, so all `8` backgrounds descend simultaneously to the closed `0`-filling $M_{0/1}$!**
  - **`s639` (`N = 15`, `14` non-trivial characters):** `10` characters have rational slopes (`8` at slope `0`, `2` at `-5/3`) and `4` have cyclotomic-irrational slopes. Again, **all `16` of `s639`'s complete $E_6$ generation backgrounds sit on the `8` slope-`0` characters and descend simultaneously to $M_{0/1}$!**
  - **`m010` (`N = 6`):** All `5` non-trivial characters have rational slopes (`-1`, `-1/3`, `-1/4`), `4` firing modules, `0` $E_6$ backgrounds, `20` descended sector modules.
  - **`m022` (`N = 3`):** Both non-trivial characters have rational slope `1/3`, `0` firing modules, `2` descended sector modules.
  - **`m023` (`N = 7`):** **`0` of `6` non-trivial characters have rational slopes** (`6` cyclotomic-irrational slopes, `12` firing modules on the cusped manifold, `0` descending to any Dehn filling!).
- **Universal chirality collapse on closed fillings (`chiral_surviving_on_filling = 0` across all `262` descended sector modules):**
  - On `m369` (`110` descended sector modules: `14` with `(2, 2) -> (2, 2)`, `56` with `(1, 1) -> (0, 0)`, `20` with `(2, 1) -> (1, 1)`, `20` with `(1, 2) -> (1, 1)`), `s639` (`130` descended: `26` with `(2, 2) -> (2, 2)`, `40` with `(1, 1) -> (0, 0)`, `32` with `(2, 1) -> (1, 1)`, `32` with `(1, 2) -> (1, 1)`), `m010` (`20` descended), and `m022` (`2` descended), **every single descended module satisfies $h^1(M_{a/b}; V) = h^1(M_{a/b}; V^*)$ (`262` of `262` Poincaré-symmetric, `0` chiral survivors)**! Closing the puncture by Dehn filling kills chirality universally even when an entire $E_6$ background shares slope `0`.

### Part B — Connected Non-Cyclic Covers of Degrees `3, 4, 5` Across Seven Word States
- Across `m009` (`12` covers), `m010` (`11`), `m135` (`37`), `m136` (`37`), `m022` (`4`), `m023` (`5`), and `m369` (`23`), our Schreier cellular homology census found **`129` connected non-cyclic covers**:
  - **`72` of `129` covers open rank-`2` free cusps** (`6` on `m009`, `6` on `m010`, `19` on `m135`, `19` on `m136`, `4` on `m022`, `4` on `m023`, `14` on `m369`, reaching up to `4` free cusps on `m135` and `m136`, whereas every cyclic level of a word state has `1` cusp of rank `1`).
  - **`21` of `129` covers open positive interior Betti excess $b_1(\widetilde{M}) - c(\widetilde{M}) \ge 1$** (`0` on `m009, m022, m023`; `1` on `m010`; `12` on `m135`; `4` on `m136`; `4` on `m369`).
  - As noted in Card Expectation `2`, selecting any specific cover among these `129` multi-cusp / higher-Betti candidates remains blocked by `FK14` unless a cover-selection law is derived without data.

---

## 5. Item `N4` — Complete Accounting for All `18` Untouched Genesis Paths (`paths/PATHS.md`) and `GENESIS` Follow-On Bullets

### Nine Untouched `E*` Paths Probed Computationally (`STALLED` as Emergence from Nothing)
1. **`E7` (Causal sets):** Unlabeled poset counts on `n = 1..6` elements are `[1, 2, 5, 16, 63, 318]` (`OEIS A000112 = True`), with uniform mean ordering fractions `0`, `1/2`, `8/15`, `13/24`, `172/315`, `515/954` climbing above `1/2` toward Kleitman–Rothschild three-layer orders; exact four-dimensional Minkowski fraction `1/10` occurs on `0, 0, 0, 0, 1, 0` posets (`1` of `318 + 63 + 16 + 5 + 2 + 1 = 405` total). `STALLED`.
2. **`E8` (HoTT empty type):** Iterated identity Kan complexes $\mathrm{Id}^k(\mathbf{0})$ ($k = 0..4$) have `0` non-degenerate simplices in dimensions `0..4`, whereas $\Sigma^k(\mathbf{0})$ requires importing the external suspension functor $\Sigma$. `STALLED`.
3. **`E9` (Spontaneous symmetry breaking on $\mathbb{H}/\mathrm{SL}(2, \mathbb{Z})$):** $Z_{\mathrm{rot}}(\tau) = y^{1/2}|\eta(\tau)|^2$ is $\mathrm{SL}(2, \mathbb{Z})$-invariant (error below ten to the minus forty-five), has a strict local maximum at $\omega$ (gradient norm below ten to the minus twenty-one, both Hessian eigenvalues strictly negative) and a strict saddle at $i$ (one negative and one positive Hessian eigenvalue), and for intermediate $\lambda_{\mathrm{mid}} = (Z_{\mathrm{rot}}(\omega) + Z_{\mathrm{rot}}(i))/2$ its Mexican-hat minimum locus $(Z_{\mathrm{rot}}(\tau) - \lambda_{\mathrm{mid}})^2 = 0$ is a continuous one-dimensional contour (verified at two distinct radial intersections with residuals below ten to the minus twenty-eight) rather than an isolated vacuum point. `STALLED`.
4. **`E10` (Chern–Simons stationarity):** On `m004`, `m009`, and `m369`, the trivial connection $\rho_{\mathrm{triv}} = I_2$ is stationary with $\dim H^1(M; \operatorname{Ad}\rho_{\mathrm{triv}}) = 3$ (`sig = (3, 3, 3, 3, 0)`), while $\rho_{\mathrm{hyp}}$ is Weil-rigid with $\dim H^1(M; \operatorname{Ad}\rho_{\mathrm{hyp}}) = 1$ and $n_{\mathrm{int}} = 0$ (`sig = (0, 1, 1, 1, 0)`) on *every* hyperbolic state without selecting $M$. `STALLED`.
5. **`E12` (It-from-bit):** Unconstrained binary sequences `{L, R}^N` have Perron root `2` and fair-coin stationary weights `(1/2, 1/2)`, whereas obtaining the golden characteristic polynomial $x^2 - x - 1 = 0$ requires positing the $RR$-exclusion rule externally. `STALLED`.
6. **`E13` (Measure-theoretic):** On $\{0, 1\}^4$ cylinders, the Dirac measure $\delta_{0^{\mathbb{Z}}}$ satisfies probability normalization (`total_mass = 1`), exact shift invariance on all length-`3` marginals, and exact Kolmogorov–Sinai entropy `0`; excluding it requires positing non-atomicity or positive entropy by hand. `STALLED`.
7. **`E15` (Bulk-from-boundary uniqueness):** `m003 = (-LR, level 1)` and `m206 = (+LR, level 2)` share $N = 5$, `4` rational slopes, identical `(h^1(V), h^1(V^*))` census `{(2, 1): 4, (1, 1): 4, (1, 2): 4}`, and exact double-cover braid-center framing relation $s_{m206}(c) \equiv 2 s_{m003}(c) + 1 \pmod p$ across `3` primes, while their hyperbolic Mostow volumes differ by an exact factor of `2` (`distinct_mostow_volumes_ratio_2 = True`). Boundary class-index invariants do not uniquely determine the bulk three-manifold. `STALLED`.
8. **`E18` (Bootstrap closure):** Among the `308` matrices in $\mathrm{SL}(2, \mathbb{Z})$ with entries in `[-5, 5]`, imposing `SE1` ($|\det(M - I)| = 1$) and McKay ($|\mathrm{SL}(2, \mathbb{Z}/N\mathbb{Z})| \le 120$ at $N = |\det(-M - I)|$) uniquely isolates hyperbolic trace `3` (`m004`), **but** dropping the scar `GM1` ($\operatorname{tr}[A, B] = -2$) admits the trivial identity commutator $\operatorname{tr}[I_2, I_2] = +2$. `STALLED` as emergence from nothing.
9. **`E19` (Diophantine non-zero floor):** In `[-10, 10]^3`, Fricke's equation $x^2 + y^2 + z^2 - xyz - 2 = k$ has `17` integer solutions at $k = -2$ (containing `(0, 0, 0)` for $Q_8$ and minimal positive solutions `(3, 3, 3)`, `(3, 3, 6)`, `(3, 6, 3)`, `(6, 3, 3)`), whereas flipping to $k = +2$ yields `134` integer solutions including the trivial identity triple `(2, 2, 2)`. Choosing $k = -2$ over $k = +2$ restates `GM1`. `STALLED`.

### Nine Paths Left Uncomputed, With Explicit Reasons (Per `M15`)
- **`E4` (Vacuum fluctuations):** Presupposes continuum space, canonical `[x, p] = i hbar` quantization, and a UV regulator absent from `GENESIS` Sections `1` through `4`, duplicating `E3`'s dead mode-sum forms `D1` through `D7`.
- **`E16` (Continuum RG flow):** Main has `zero` verified four-dimensional action (`GAP5`, `FK8`); integrating imported QFT beta functions violates `Guardrail 4` as a genesis test, while the discrete word-length flow is already tested in `B1924` and `B1928`.
- **`E17` (Extended objects / strings):** Presupposes two-dimensional worldsheet gravity, target dimension $D$, and tension $\alpha'$ absent from the discrete grammar, with no landscape-selection rule.
- **`E20` (De Sitter / positive $\Lambda$):** Presupposes smooth four-dimensional Lorentzian geometry, Einstein–Hilbert dynamics, and $\Lambda > 0$ by hand (same circularity as `E5` and `D1` through `D3`).
- **`P1` (Linguistic negation), `P2` (Gödelian incompleteness), `P3` (Observer selection), `P4` (Whiteheadian process), `P5` (Apophatic):** Left uncomputed under `philosophy/PHILOSOPHICAL_PATHS.md`'s explicit governance rule (`non-mathematizable; argued rather than computed; no content promotes to CLAIMS.md`), with each concrete mathematical projection already covered by `E14` (`P1`, `P2`), `E13` (`P3`), `E1`/`E6` (`P4`), or non-symbolizability (`P5`).

### `GENESIS` Section `8` Follow-On Bullets (`B130` Metallic Fixed Loci Computed; Remaining Five Reasoned)
- **Metallic trace-map fixed loci component by component (`B130` / `AR4`, `m = 1, 2, 3`):** **Computed in `Section 5`!** Exact resultant and singular-locus decomposition of $\Phi_{L^m R^m}(x, y, z) = (x, y, z)$ in $\mathbb{C}^3$ without imposing $\kappa = -2$ gives irreducible `1`D curves (`xy - x - y = 0` at $m = 1$; $x^2 y^2 - 2x^2 - 2y^2 = 0$ plus the vertical `1`D singular line `(0, 0, z)` at $m = 2$; $x^2 y^2 - x^2 y - x^2 - x y^2 + x y + x - y^2 + y = 0$ plus `(0, 0, z)` at $m = 3$). Along **every** component Fricke $\kappa$ varies continuously (`all_curve_branches_vary_kappa = True`), with **`0` isolated unsymmetric zero-dimensional points** (`isolated_unsymmetric_zero_dim_points = 0` for $m = 1, 2, 3$).
- **Remaining follow-ons with explicit reasons:** Projective `+-LLRLRR` infinite-volume degenerations (`B1487`'s one-cusp bound $\le 1$ already blocks `3` generations); six-dimensional frame bundle $\Gamma \backslash \mathrm{PSL}(2, \mathbb{C})$ (`GAP6` requires choosing an unforced curved gauge bundle / metric connection); `F-HE` character search on multi-cusp covers (topology computed in `N3`, character search barred by `WORKING_RULES` until `FK14` and a trial budget are fixed); and `U1-eta` / `U1-Z'9`, dark-matter stability, and Dirac-vs-Majorana outside the root (pre-empted by `N2`'s negative showing `m369` and `s639` have `0` own-arithmetic McKay $E_6$ doors, plus `B1340` on `U1-Z'9`).

---

## 6. Five Planted-Fault Controls (`5` of `5` Fired)

| Control | Planted fault | Result |
|---|---|---|
| **`PC_N1`** | Replace Hermitian $g M g^\dagger$ with complex transpose $g M g^T$ on `m135 = -LLRR` | **FIRED** (real $\mathrm{SO}^+(3, 1)$ broken; untwisted `sig_V` shifted from `(0, 1, 1, 1, 0)` to `(1, 2, 2, 2, 0)` with $h^0 = 1$) |
| **`PC_N2`** | Inject synthetic norm-`3` $2T \to E_6$ ramified prime into `m369`'s arithmetic detector | **FIRED** (flipped `False` to `True`) |
| **`PC_N3`** | Include cyclic $\mathbb{Z}/3\mathbb{Z}$ cover in non-cyclic cover enumerator on `m009` | **FIRED** (`1` cyclic cover with $b_1 = c = 1$ caught and separated) |
| **`PC_N4`** | Hand-embedded target potential $|\tau - \tau_*|^2$ in `E9` modular gate (`Guardrail 1`) | **FIRED** (`is_modular_invariant = False`) |
| **`PC_N5`** | Flip $k = -2$ to $k = +2$ in Fricke–Markoff Diophantine search (`E19`) | **FIRED** (`admits_trivial_222_at_k_plus2 = True`) |

`0 of 19.`
