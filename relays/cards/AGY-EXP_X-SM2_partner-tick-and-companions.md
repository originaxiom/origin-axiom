# Card X-SM2 — Independent Recomputation of SM-C8 (Partner Test), SM-C10 (Twisted Duality on the Tick Family), and SM-C11 (Five-Ended Companion and Length-10 Census)

**Seat:** `agy-exp`
**Date:** `2026-11-14`
**Authorizing directive:** `docs/seats/agy-exp.md`, messages `M16` (`2a43ad52d`) and `M17` (`9ec085124`)
**Targets read (prose `.md` files only; `zero` `.py` or `.json` files read; `zero` imports from `main` or any seat):**
- `SM-C8`: `relays/SM_C8_THE_PARTNER_TEST.md`, `relays/cards/SM_C8_the-partner-test.md`, and `relays/SM_LITERATURE_NOTE_1.md` at `2e1b88a7d` (with background context from `B1441`).
- `SM-C10`: `relays/SM_C10_THE_ONE_TICK_OBJECT.md` and `relays/cards/SM_C10_the-one-tick-object.md` at `2e1b88a7d`.
- `SM-C11` (`P-333`): `relays/SM_C11_THE_FIVE_ENDED_COMPANION.md` and `relays/cards/SM_C11_the-five-ended-companion-in-F-CI.md` at `2e1b88a7d` (with background context from `B1454`, `B1491`, `B1492`).

---

## 1. What Will Be Computed on Our Own Code

### Part 1 — `SM-C8`: The Partner Test on `B1441` Tier 1
1. **Population rebuilt independently from `SnapPy`:** All connected covers of degrees `2` through `6` with at least `2` cusps of `m004`, `m003`, `m009`, and `m010` (`69` covers), together with the `5` named manifolds `m202`, `s959`, `o10_150726`, `m129`, and `m125` (`74` manifolds total; `71` active entries having at most `600` characters in $\operatorname{Hom}(H_1(P), \mu_N)$ at $N = \max(\text{torsion exponent}, 2)$, and `3` entries skipped above `600` characters).
2. **Modules and exact two-prime finite-field Fox calculus:** On each active entry $P$, construct all non-split rank-`2` upper-triangular modules $V(\ell, \alpha) = \bigl(\begin{smallmatrix}\alpha & z\beta \\ 0 & \beta\end{smallmatrix}\bigr)$ ($\beta = \alpha/\ell$, $\ell \neq 1$ with $h^1(P; \ell) \ge 1$, $\alpha \neq 1$, $\beta \neq 1$), where $z$ runs over a deterministic basis of $H^1(P; \ell)$ plus `2` deterministic non-collinear linear combinations whenever $h^1(P; \ell) \ge 2$, evaluated in exact arithmetic over $\mathbb{F}_p$ ($p \equiv 1 \pmod N$), with an independent second prime $p_2 \equiv 1 \pmod N$ cross-checking every $|I| = 2$ carrier and sampled modules per entry (`zero` floating-point SVD thresholds).
3. **Quantities and duality controls at every non-vacuous join $(P, V, T_i)$ ($h^1(T_i; V) > 0$):**
   - `C1`: $\dim A_V + \dim A_{V^*} = h^1(\partial P; V)$;
   - `C2`: $[h^1(V^*) - h^0(V^*)] - [h^1(V) - h^0(V)] = \dim A_{V^*} - h^0(\partial P; V^*)$ and equality with $I(V) = n(V) - n(V^*)$;
   - `C3a` and `C3b`: $\dim S_i + \dim S_i^* = h^1(T_i; V)$ and $D_{\mathrm{ord}} = n(V \mid 0\text{ elsewhere}, S_i) - n(V^* \mid 0\text{ elsewhere}, S_i^*) = d_i + \ell_i$, where $d_i = \dim S_i - h^0(\partial P; V) + h^0(V) - h^0(V^*)$ and the open-end leak is $\ell_i = n(V^* \mid \text{free elsewhere}, S_i^*) - n(V^* \mid 0\text{ elsewhere}, S_i^*)$;
   - Original split-torus $D = n(V \mid \text{sub}) - n(V \mid \text{quotient})$ wherever $V|_{T_i}$ splits; all counts reported both on all `71` entries and excluding `m129` and `m125`.

### Part 2 — `SM-C10`: Twisted Duality on the Tick Family $M_1, \dots, M_6$
1. **Presentations and `SnapPy` cross-checks:** Build $M_n = \langle x, y, t \mid t x t^{-1} = \varphi^n(x),\, t y t^{-1} = \varphi^n(y)\rangle$ for $\varphi(x) = yx, \varphi(y) = x$ ($n = 1, \dots, 6$), verify $\varphi^n([x, y]) = [x, y]^{(-1)^n}$ in the free group $F_2$, and cross-check against `SnapPy`'s cyclic covers of `b-+R` (`m000`, `m004`, `m025`, `m206`, `m407`, `s961`): orientability (non-orientable iff $n$ is odd), volume $n \cdot \operatorname{vol}(\text{m000})$, $H_1(M_n)$ invariant factors (`1, 1, 4, 5, 11, 16` in the fibre direction), and orientation double covers (`m004` for `m000`, `s961` for `m025`, and $M_{10}$ for `m407`).
2. **Exact Fox cohomology populations (two certified primes):**
   - **Sealed population ($N \in \{2, 3, 4, 5, 6\}$, $\alpha \neq \beta$):** Verify `K1` ($\dim A_V + \dim A_{V^* \otimes w} = h^1(\partial M_n; V)$), `K2` ($[h^1(V^* \otimes w) - h^0(V^* \otimes w)] - [h^1(V) - h^0(V)] = \dim A_{V^* \otimes w} - h^0(\partial M_n; V^* \otimes w)$), transfer `K4` ($h^1(M_n; V) + h^1(M_n; V \otimes w) = h^1(M_{2n}; V|_{M_{2n}})$ at odd $n$), twisted vs untwisted $h^1$ gaps $g_w$ vs $g_0$, and interior class index $n(V) - n(V^* \otimes w)$.
   - **Extended `m407` ($n = 5$) population ($N = 22$):** Both the `2420` distinct-diagonal ($\alpha \neq \beta$) modules and the `242` unipotent ($\alpha = \beta$) doublets (`2662` total).
   - **Common-point `SU(2)` family ($n = 1, \dots, 6$):** $x \mapsto i, y \mapsto j, t \mapsto c \cdot g^n$ across all `46` non-trivial roots of unity $c$ of order dividing $d \in \{2, \dots, 12\}$ (`50`-digit `mpmath` linear algebra).

### Part 3 — `SM-C11` (`P-333`): Five-Ended Companion `o10_150729` and Length-`10` Companion Census
1. **Standalone F-CI cusp-isometry reader (two independent `SnapPy` paths):** From both `M.is_isometric_to(M, return_isometries=True)` and `M.symmetry_group().isometries()`, extract total isometries, orientation sign $\det(X) \in \{+1, -1\}$, induced permutation group on the cusps (order, transitivity, even-permutation check for $A_5$ vs $S_5$), cusp-fixing $|\det(X - I)|$ values over all orientation-preserving isometries, per-cusp presence of $|\det(X - I)| = 3$, and cusp shape hexagonal test modulo $\mathrm{GL}(2, \mathbb{Z})$ on `o10_150729` and published control `L8a15`.
2. **Length-`10` companions' census:** Enumerate all `232` signed word states of lengths `2` through `10` (aperiodic `{L, R}` words with both letters modulo cyclic shift and `{L <-> R}` swap, signs `+` and `-`), construct each state's canonical fixed-point companion cover via the quotient $H_1(M) / \operatorname{im} H_1(\partial M)$ (`degree = cusps = |2 - tr phi|`), and run our standalone F-CI reader across all `232` companions (cross-checking both isometry paths to certify the negative outside `o10_150729`).

---

## 2. Expectations Committed Before Writing or Running Code

- **`E1` (`SM-C8` population & theorem identities):** `71` active entries, `486754` non-split modules, `1109760` total joins (`934132` vacuous, `175628` non-vacuous); `C1`, `C2`, `C3a`, `C3b`, and $\dim S_i + \dim S_i^* = h^1(T_i; V)$ hold with `zero` failures across every module and join.
- **`E2` (`SM-C8` relational leak):** Outcome `R_leak` holds — $\ell_i > 0$ on `65` of `71` entries and on all `17` carriers of $|I| = 2$, while $D_{\mathrm{ord}}$ is symmetric under $+ \leftrightarrow -$ (`sum = 0`), confirming that a shared open-end boundary condition carries the order without selecting its sign (unchanged when `m129` and `m125` are excluded).
- **`E3` (`SM-C8` B1441 index histogram scope):** All `17` carriers of $|I| = 2$ match `B1441` (`zero` carriers of $|I| \ge 3$; `m004` and `m003` covers reach at most `1`; `m202` and `s959` carry `0`), and on the `7` entries where every non-trivial $h^1(P; \ell) \le 1$ the full index histogram is basis-independent.
- **`E4` (`SM-C10` sealed population):** `m000`, `m004`, and `m407` carry `0` modules at orders up to `6`; `m025` carries `96`, `m206` carries `100`, and `s961` carries `1008` (`1204` total); `K1`, `K2`, and `K4` hold on `100` percent of modules, with $g_w = g_0$ on all even-$n$ modules and $g_w \neq g_0$ on `6` of `96` modules on `m025`.
- **`E5` (`SM-C10` Klein-bottle parity law & `m407` at $N = 22$):** Every non-split module at odd $n$ satisfies $\ell(t) = -1$ and interior twisted index $n(V) - n(V^* \otimes w) = 0$; at $N = 22$ on `m407`, `K1`, `K2`, and `K4` hold on all `2420` distinct-diagonal modules ($g_w \neq g_0$ on `20`, $g_w = \pm 2$ on `10 + 10`) and on all `242` unipotent doublets ($g_w = \pm 1$ on `11 + 11`).
- **`E6` (`SM-C10` common-point `SU(2)` family):** Peripheral cohomology vanishes (`0`) across all `46` roots $c$ at every $n \in \{1, \dots, 6\}$, $h^1 = 1$ solely at $c = \pm i$, and $g_w = g_0 = 0$ everywhere.
- **`E7` (`SM-C11` Part 1 on `o10_150729`):** `240` isometries (`120` orientation-preserving acting on the `5` ends as $A_5$ of order `60`, extending with the `120` orientation-reversing ones to $S_5$ of order `120`), orientation-preserving cusp-fixing values `{3: 40, 1: 40, 4: 20, 0: 20}` hitting every end `0` through `4` with value `3`, and all `5` cusps hexagonal; control `+LLLR` companion is isometric to `L8a15` (`12` chiral isometries, $S_3$ on `3` ends, cusp-fixing values `{0: 6, 4: 6}`, `zero` threes).
- **`E8` (`SM-C11` Part 2 length-`10` census):** All `232` signed word states (`231` proper companions) satisfy $\text{degree} = \text{cusps} = |2 - \operatorname{tr}\varphi|$ with transitive end action, and **`o10_150729` (`-LR`) is the unique companion to word length `10` carrying $|\det(X - I)| = 3$** (with `2` occurring once on `-LLRR`'s `8`-ended companion and `{0, 4}` everywhere else).

---

## 3. Planted Fault Controls (`8` Controls, All Must Fire)

1. **`P1_C8`:** Replace $V^*$ by $V$ in `C1` and `C2` on `SM-C8`; must fail on a large majority of modules/joins.
2. **`P2_C8`:** Replace $S_i^*$ by a deterministic non-canonical line in $H^1(T_i; V^*)$ when $h^1(T_i; V^*) = 2$; must violate `C3b` ($D_{\mathrm{ord}} = d_i + \ell_i$) on joins.
3. **`P3_C8`:** Assert untwisted half-dimension $2\dim A_V = h^1(\partial P; V)$ on `SM-C8`; must fail wherever $I(V) \neq 0$.
4. **`P4_C10`:** Replace $V^* \otimes w$ by untwisted $V^*$ in `K1` and `K2` on odd-$n$ ticks (`m025` and `m407`); must fail (`24` on `m025`, `220` on `m407`) while changing `0` on even-$n$ ticks.
5. **`P5_C10`:** Replace $w$ by a wrong order-`2` character $w' = w \cdot \chi_2$ on `m025`; must fail `K1`/`K2` (`24` modules).
6. **`P6_C10`:** Omit $w$ in transfer `K4` ($2\,h^1(M_n; V) = h^1(M_{2n}; V)$) on `m025`; must fail (`6` modules).
7. **`P7_C11`:** Replace $|\det(X - I)|$ by $|\det X|$ in `SM-C11`; must evaluate to `1` everywhere and erase the `3` on `o10_150729`.
8. **`P8_C11`:** Build `+LLLR`'s cover from the trivial character subgroup instead of $H_1(M) / \operatorname{im} H_1(\partial M)$; must fail the $|2 - \operatorname{tr}\varphi| = 3$ degree and cusp-count gate.

---

## 4. Firewall

Pure mathematics only (`SnapPy` census manifolds, integer matrices, finite-field Fox calculus, `50`-digit `mpmath` for the `SU(2)` common-point check). `Zero` measured physical quantities appear anywhere.

`0 of 19.`
