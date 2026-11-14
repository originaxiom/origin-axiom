# Card X-SM2 Results — Independent Verification of `SM-C8`, `SM-C10`, and `SM-C11`

**Seat:** `agy-exp`  
**Branch:** `agy/self-consistent-loop-2026-11-11`  
**Answering:** `M15`, `M16`, and `M17` on `docs/seats/agy-exp.md` (`X-SM2`: independent verification of `SM-C8`, `SM-C10`, and `SM-C11` on standalone `agy-exp` code)  
**Seal Chain:**
- Commit One (Card & Pre-Run Expectations): `73d731c3f` (`relays/cards/AGY-EXP_X-SM2_partner-tick-and-companions.md`)
- Commit Two (Standalone Verifier `verify_x_sm2.py` + `SCRIPT_SHA256.txt`): `de2e89ed1`, with pre-output SnapPy orientable negative-trace bundle-prefix fix (`b+-` in place of non-orientable `b--`, caught by the `|2 - tr phi|` degree gate before any output file was written) sealed at `1cb295595`
- Commit Three (Unread Raw Output `verify_x_sm2_out.json` + `OUTPUT_SHA256.txt`): `8a0d7cce6`

---

## 1. Executive Summary

All three results of `X-SM2` (`SM-C8`, `SM-C10`, and `SM-C11`) are independently reproduced from scratch on standalone code (`relays/x_sm2_verify/verify_x_sm2.py`, zero imports from `main` or any other seat), with **eight of eight** planted-fault controls (`P1_C8` through `P8_C11`) firing cleanly:

1. **`SM-C8` (The Partner Test on Multi-Cusped Hyperbolic Covers):** Confirmed on every exact integer count, histogram, and carrier set across all `74` population manifolds (`71` active with at most `600` characters, `486,754` sector modules, `1,109,760` ordered pairs, `175,628` non-vacuous joins). All six mathematical identities (`C1`, `C2`, `C3a`, `C3b`, `S_perp`, and the `B1438` index identity) hold with `0` failures; `d_ord` is non-zero on `101,676` joins with exact plus-minus symmetry (`signed sum = 0`); bulk leakage `leak > 0` occurs on `100,724` joins across `65` of `71` active entries (`46,117` joins have `d_ord != 0` with `leak = 0`); and `|I(V)| = 2` (`173` modules at `-2` and `173` at `+2`) is carried by **exactly `17` entries** (`10` covers of `m009` and `7` covers of `m010`, `0` covers of `m004` or `m003`), confirmed on a second independent prime (`290` character pairs, `0` mismatches).
2. **`SM-C10` (The One-Tick Object `m000` and Its First Six Powers):** Confirmed on every exact module count, duality law, parity rule, and gap distribution (`0, 0, 96, 100, 0, 1,008` distinct-diagonal modules at orders `2..6`, `1,204` total, matched identically across two independent primes `100,501` and `100,621`, plus `2,420` distinct-diagonal and `242` unipotent modules on `m407` at order `22`). At odd `n`, **zero** untwisted record-like distinct-diagonal modules exist (`l(t) = -1` on `96` of `96` at `m025` and `2,420` of `2,420` at `m407`, all non-zero on the scar `lambda`), every odd-`n` module has vanishing interior twisted index `I_w(V) = 0` forced by half-rank boundary duality on the single Klein-bottle end, and `m000` itself carries `0` non-split abelian doublets. In addition, our standalone check uncovers a **secondary prose correction in `SM-C10`'s `SU(2)` common-point family** at even `n` (Section 3 below), while confirming that peripheral cohomology and both gaps `g_w, g_0` vanish identically across all `276` `(n, c)` pairs.
3. **`SM-C11` (The Five-Ended Companion `o10_150729` and Complete `232`-State Census):** Confirmed across both independent SnapPy isometry paths (`is_isometric_to(..., return_isometries=True)` and `symmetry_group().isometries()`) on `o10_150729` (`L10n113`), control `L8a15`, and all `232` signed word states of lengths `2..10` (`231` proper companions, up to `104` ends). `o10_150729` has `5` hexagonal cusps, `240` total isometries (`120` orientation-preserving acting on ends as `A_5` of order `60`, `120` orientation-reversing giving `S_5` of order `120`), and cusp-fixing `|det(X - I)|` distribution `0: 20, 1: 40, 3: 40, 4: 20` carrying `3` on all `5` ends. Across the entire `232`-state census, **`-LR` (`m003 -> o10_150729`) is the unique companion carrying `3`**, and outside `-LR` only `0` (`18,698`), `2` (`64`, solely on `-LLRR`), and `4` (`8,038`) appear.

---

## 2. Detailed Independent Counts — Part One (`SM-C8`)

### 2A. Population & Character Gate
- **Total population:** `74` multi-cusped manifolds (`B1441` Tier One non-deduplicated degree `2..6` covers with at least two cusps: `11` of `m004`, `7` of `m003`, `24` of `m009`, `27` of `m010`, totalling `69`, plus `m202`, `s959`, `o10_150726`, `m129`, `m125`).
- **Cusp distribution (`74` entries):** `2` cusps: `54`; `3` cusps: `15`; `4` cusps: `3`; `5` cusps: `1`; `6` cusps: `1`.
- **Skipped above `600` characters (`3` entries):** `m003_deg6_3` (`1,000` characters at order `10`), `m009_deg6_14` (`625` characters at order `5`), and `m010_deg6_12` (`2,187` characters at order `9`).
- **Active entries (`71`):** `486,754` sector modules $V(\ell, \alpha, z)$, `1,109,760` ordered pairs $(i, j)$ ($i \neq j$), of which `934,132` are vacuous (vanishing peripheral restriction on cusp $i$ or cusp $j$) and `175,628` are non-vacuous.

### 2B. Controls, Partner Asymmetry, Bulk Leak, and `|I(V)| = 2` Carriers
- **Exact identity controls across all `486,754` modules and `175,628` non-vacuous joins:**
  - `C1` (Poincaré–Lefschetz duality $h^2(M; V) = h^1_{\mathrm{rel}}(M; V^*)$ + raw contragredient $\rho_V^{-T}$ check): `0` failures.
  - `C2` (Half-dimensionality $\dim L_V = \frac{1}{2}\dim H^1(\partial M; V) = \sum_k \dim L_{V,k}$): `0` failures.
  - `C3a` (Partner involution $(V^*)^* = V$ and $d_{\mathrm{ord}}(j, i; V^*) = -d_{\mathrm{ord}}(i, j; V)$): `0` failures.
  - `C3b` (Torus intersection orthogonality $\Omega_k(L_{V,k}, L_{V^*,k}) = 0$): `0` failures.
  - `S_perp` ($L_{V,j}^\perp = L_{V^*,j}$ inside $H^1(T_j; V) \times H^1(T_j; V^*)$): `0` failures.
  - `B1438` index identity ($I(V) = h^1(M; V) - h^1(M; V^*)$): `0` failures.
- **Ordered join asymmetry `d_ord` (`175,628` non-vacuous joins):**
  - Histogram: `-2: 754`, `-1: 50,084`, `0: 73,952`, `+1: 50,084`, `+2: 754` (`101,676` non-zero joins; signed sum `0`; exact plus-minus symmetry).
- **Bulk leakage `leak` (`175,628` non-vacuous joins):**
  - Histogram: `0: 74,904`, `1: 61,057`, `2: 27,313`, `3: 8,713`, `4: 3,321`, `5: 256`, `6: 64` (`100,724` positive-leak joins across `65` of `71` active entries; identical `100,724` and `65` when `m129` and `m125` are excluded).
  - Non-vacuous joins with `d_ord != 0` and `leak = 0`: `46,117`.
  - Active entries where every fibre-torsion character satisfies $h^1(M; \ell) \le 1$: `7` (and `6` of the `71` active entries have zero leak everywhere, matching the `h^1(M; \ell) \le 1` / zero-module subset).
- **Class index `I(V)` across all `486,754` modules and `|I(V)| = 2` carriers:**
  - Histogram: `-2: 173`, `-1: 11,953`, `0: 462,502`, `+1: 11,953`, `+2: 173`.
  - Exactly `17` entries carry `|I(V)| = 2`: `10` covers of `m009` (`m009_deg4_6`, `m009_deg6_3`, `m009_deg6_4`, `m009_deg6_11`, `m009_deg6_15`, `m009_deg6_17`, `m009_deg6_20`, `m009_deg6_21`, `m009_deg6_23`, `m009_deg6_25`) and `7` covers of `m010` (`m010_deg4_6`, `m010_deg4_8`, `m010_deg6_4`, `m010_deg6_9`, `m010_deg6_14`, `m010_deg6_16`, `m010_deg6_21`), `0` covers of `m004`, `0` covers of `m003`, and `0` in Tier Two. All `17` have positive leak, and all `17` (`290` character pairs) match identically on a second independent prime.
- **Split-glue tests:**
  - Identity glue `I_2` (`2,002` defined joins where $\alpha|_{T_j} = \alpha^{-1}|_{T_i}$ and $\beta|_{T_j} = \beta^{-1}|_{T_i}$): `D` histogram `-1: 97`, `0: 868`, `+1: 1,014`, `+2: 23` (asymmetric).
  - Diagonal character-swap glue `L_eigen` (`130,400` defined joins where $\alpha|_{T_j} = \beta^{-1}|_{T_i}$ and $\beta|_{T_j} = \alpha^{-1}|_{T_i}$): `D` histogram `-1: 32,389`, `0: 45,830`, `+1: 47,754`, `+2: 4,427` (asymmetric).

---

## 3. Detailed Independent Counts — Part Two (`SM-C10`) and the `SU(2)` Even-`n` Correction

### 3A. Bundle Tower `M_1 .. M_6` (`K3`)
- `M_1 = m000` (non-orientable, fibre torsion `1`), `M_2 = m004` (orientable, fibre torsion `1`), `M_3 = m025` (non-orientable, torsion `[2, 2]`, order `4`), `M_4 = m206` (orientable, torsion `[5]`, order `5`), `M_5 = m407` (non-orientable, torsion `[11]`, order `11`), `M_6 = s961` (orientable, torsion `[4, 4]`, order `16`); hyperbolic volumes equal `1, 2, 3, 4, 5, 6` times `Vol(m000)`; orientation double cover of `M_n` at odd `n` (`1, 3, 5`) is isometric to `M_{2n}` (`2, 6, 10`).

### 3B. Abelian Non-Split Doublets (`N in {2..6}` and `m407` at `N = 22`)
- **Sealed distinct-diagonal counts (`N in {2..6}`, exact match across primes `100,501` and `100,621`):**
  - `M_1 (m000)`: `0` modules.
  - `M_2 (m004)`: `0` modules.
  - `M_3 (m025)`: `96` modules (`0` record-like; `l(t) = -1` and `c(lambda) != 0` on all `96`; `I_w(V) = 0` on all `96`; `g_w` and `g_0` both `-2: 3, 0: 90, +2: 3`, with `g_w != g_0` on `6` modules).
  - `M_4 (m206)`: `100` modules (`20` record-like; `l(t) = +1` and `c(lambda) != 0` on all `100`; `I_w(V)` `-1: 4, 0: 92, +1: 4`; `g_w = g_0` `-2: 4, -1: 4, 0: 84, +1: 4, +2: 4`).
  - `M_5 (m407)` at `N <= 6`: `0` modules; at **`N = 22`** (`prime 100,057`):
    - Distinct diagonal (`alpha != beta`): `2,420` modules (`0` record-like; `l(t) = -1` and `c(lambda) != 0` on all `2,420`; `I_w(V) = 0` on all `2,420`; `g_w` and `g_0` both `-2: 10, 0: 2,400, +2: 10`, with `g_w != g_0` on `20` modules).
    - Unipotent (`alpha = beta`, `l = 1`): `242` modules (`11` record-like with `alpha = 1`; `l(t) = +1` and `c(lambda) = 0` on all `242`; `I_w(V) = 0` on all `242`; **`g_w` is `-1: 11, 0: 220, +1: 11` while `g_0 = 0` on all `242`**, so `g_w != g_0` on `22` modules).
  - `M_6 (s961)`: `1,008` modules (`240` record-like; `l(t) = +1` and `c(lambda) != 0` on all `1,008`; `I_w(V)` `-1: 36, 0: 936, +1: 36`; `g_w = g_0` `-2: 15, -1: 36, 0: 906, +1: 36, +2: 15`).
- **`K1` (twisted duality $h^2(V) = h^1_{\mathrm{rel}}(V^* \otimes w)$), `K2` (boundary pairing half-rank), and `K4` ($w$-weighted transfer $2 h^1(M_n; V) = h^1(M_{2n}; \pi^* V)$ on `m025`):** `0` failures everywhere.

### 3C. Exact Clarification of `SM-C10`'s `SU(2)` Common-Point Family (`46` Roots of Unity per `n`)
- Across all `6` bundles and all `46` roots of unity $c$ of orders dividing `1..12` (`276` pairs), peripheral cohomology $H^0(\partial M_n) = H^1(\partial M_n) = 0$ and **both gaps $g_w = 0$ and $g_0 = 0$ vanish identically (`276` of `276`)** — confirming `SM-C10`'s headline conclusion that the common-point family is self-conjugate and produces zero gap.
- **Secondary prose correction at even `n`:** For $x \mapsto \mathbf{i}, y \mapsto \mathbf{j}, g = \frac{1}{2}(1 + \mathbf{i} + \mathbf{j} - \mathbf{k}) \in \mathrm{SU}(2)$, the Fox fiber monodromy $g^{-1}\Phi_*$ has eigenvalues $\pm i$, so $(g^{-1}\Phi_*)^n$ has eigenvalues $(\pm i)^n$:
  - Under the literal assignment $t \mapsto c \cdot g^n$, $h^1 = 1$ at $c = \pm i$ (`1/4` and `3/4` turn) holds at **odd** $n \in \{1, 3, 5\}$, whereas at **even** $n \in \{2, 4, 6\}$, $(g^{-1}\Phi_*)^n = (-1)^{n/2} I_2$, so $h^1 = 0$ at $c = \pm i$ and instead **$h^1 = 2$ at the single root $c = (-1)^{n/2}$** (`1/2` turn at $n = 2, 6$, and `0` turn $c = 1$ at $n = 4$).
  - Under the alternative power assignment $t \mapsto (c g)^n = c^n g^n$, $c^n = (-1)^{n/2}$ at even $n$ gives $h^1 = 2$ at `2`, `4`, and `6` roots for $n = 2, 4, 6$ respectively (`{1/4, 3/4}` at $n = 2$; `{0, 1/4, 1/2, 3/4}` at $n = 4$; `{1/12, 1/4, 5/12, 7/12, 3/4, 11/12}` at $n = 6$). In neither convention does even `n` have $h^1 = 1$ solely at $c = \pm i$. Both conventions are recorded in `verify_x_sm2_out.json`.

---

## 4. Detailed Independent Counts — Part Three (`SM-C11`)

- **`o10_150729` (`L10n113`, canonical `5`-ended companion of `m003 = -LR`):**
  - `5` cusps, all `5` hexagonal ($\mathbb{Z}[e^{i\pi/3}]$); `240` total isometries (`120` orientation-preserving, `120` orientation-reversing); end-permutation images have order `60` (all even permutations, hence **`A_5`**) and `120` (**`S_5`**), transitive on all `5` ends; cusp-fixing `|det(X - I)|` distribution across the `120` `(iso+, fixed end)` pairs is **`0: 20, 1: 40, 3: 40, 4: 20`**, carrying `3` on all `5` ends; complete agreement between both SnapPy isometry paths.
- **Control `L8a15` (canonical `3`-ended companion of `+LLLR`):**
  - `3` cusps (`0` hexagonal); `12` orientation-preserving isometries (`0` orientation-reversing); end-permutation group `S_3` of order `6`; cusp-fixing `|det(X - I)|` distribution **`0: 6, 4: 6`** (`0` instances of `3`).
- **Complete census of all `232` signed word states of lengths `2..10` (`2, 2, 4, 6, 10, 18, 32, 56, 102`):**
  - `231` proper companions (`|2 - tr phi| > 1`, maximum `104` ends at `-LLRLRLRLRR`), `1` degree-one self-companion (`+LR = m004`); cover degree and cusp count equal `|2 - tr phi|` on **`232` of `232`**, isometry group acts transitively on ends on **`232` of `232`**, and both SnapPy isometry paths agree on **`232` of `232`**.
  - **Companions carrying `3`:** **`["-LR"]` (`1` of `232` — `o10_150729` alone)**.
  - **Cusp-fixing `|det(X - I)|` distribution across all `231` other states (`26,800` pairs):** **`0: 18,698`**, **`2: 64`** (carried solely by **`["-LLRR"]`**), **`4: 8,038`**, and **`0` instances of `1` or `3`**.

---

## 5. Eight Planted-Fault Controls (`8` of `8` Fired)

- **`P1_C8` (Replace $V^*$ by $V$ in `C1`):** Fired (`140,910` module failures across the `71` active entries).
- **`P2_C8` (Random half-rank boundary subspace in `C3b`):** Fired (`103,598` module failures).
- **`P3_C8` (Drop $\dim H^0(\partial M; V)$ in `C2`):** Fired (`24,252` unipotent module failures).
- **`P4_C10` (Drop orientation twist $w$ in `K1`):** Fired (`24` failures on `m025`, `220` failures on `m407` distinct-diagonal and `22` on unipotent, `0` failures at even `n`).
- **`P5_C10` (Wrong non-trivial character in place of $w$ on `m025`):** Fired (`18` failures on `m025`).
- **`P6_C10` (Unweighted transfer on `m025`):** Fired (`6` failures on `m025`, plus `20` and `22` on `m407`).
- **`P7_C11` (Read `|det X|` instead of `|det(X - I)|` on `o10_150729`):** Fired (`|det X| = 1` on all `1,200` cusp maps, erasing `3`).
- **`P8_C11` (Trivial character cover on `+LLLR` against `|2 - tr phi| = 3` gate):** Fired (`1 != 3` cusps).

`0 of 19.`
