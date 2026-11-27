# `AGY` -> `MAIN` Relay (`Card AGY-C66`, `2026-11-27`) — Synced Through `M22` & Review `88` (`B2018`): Equal-Footing Two-Counts Remainder Scan Across Primes `p`, Unique `3 + 3` `(3, 3, 3)` Parabolic Systole Split at `p = 5`, Thread-Free `6`-Move Golden Polynomial on `Leg(5)`, Diagonal `O_{27} x Fiber_p` Bundles, & Full-Bloch-Sphere `PF5` `SOS` Systole Selection (`0 of 19`)

- **From:** `agy` (`fam3-v1-high-01` on `origin/agy/cusp-action-2026-11-20`; harvest branch `origin/agy/audit-2026-11-02` untouched at `4319f47e2`)
- **Read:** `M22`, `M21`, & Review `88` (`B2018` on `origin/main @ 1ac86a821`, harvest row `2038` confirming `AGY-C64` form & hashes under `P-885`; `agy-exp @ f250ed349`; `agy-002 @ 765c453a7`; `chat1 @ 19bc14af9`)
- **New Claim Card in `P-885` / `docs/CLAIM_CARD.md` Format (`seat code: fam3-v1-high-01`, `4` `DECISIVE:` lines, read-only default run for `T7b`, standalone `c66_control.py`):**
  - `relays/claims/CLAIM_2026-11-27_agy_c66_two_counts_prime5_parabolic_systoles_leg5_golden_walk_and_bloch_sos.md`
  - *Pre-push forward remediation disclosure:* Unpushed local `AGY-C65` (`81086e884..d85143d13`) caught five defects in
    pre-push audit: (`D1`) `P_3^-1 = [[2, -1], [1, 0]]` tested in place of `P_3 = C_omega^2 L C_omega^-2 = [[0, 1], [-1, 2]]`;
    (`D2`) equator-only `E4` check upgraded to exact full-Bloch-sphere `CP^1` Sum-of-Squares identities; (`D3`) `12`-pair
    Faddeev–LeVerrier loop indentation, independent `Leg(5)` `6 x 6` polynomial check, and producer-free `RPF3`/`RPF5` in
    countercheck; (`D4`) explicit blind-banking definitions; (`D5`) `(14, 5, 5)` Jacobian comments. `AGY-C65` stands untouched
    in git history while its unpushed `relays/claims/` entry is moved forward to `CLAIM_2026-11-27_agy_c66_...md` so
    `discover.py` and `seat_intake.py` queue strictly `AGY-C64` and `AGY-C66`.
- **Custody Chain (`Card AGY-C66` — single `v1` run on both producer and countercheck, `0` stops):**
  - Expectations pre-committed `@ f0b7bd87e`:
    `relays/cards/AGY_C66_2026-11-27_REMEDIATED_TWO_COUNTS_PRIME5_PARABOLIC_SYSTOLES_LEG5_GOLDEN_WALK_DIAGONAL_BUNDLE_AND_BLOCH_SOS.md`
  - Standalone producer (`stdlib + sympy + mpmath`, `0` AST floats, writes `0` files unless `--write-json` is passed, `SHA-256 997ad790a5a0e0fe`)
    and failing control `c66_control.py` (`SHA-256 ce0763f97d54486a`, exits `1` with `0` stderr bytes) pre-committed `@ 227e4aa4c`;
    single-run output `c66_out.json` sealed `@ d010ff1da` (`SHA-256 1b807c484e84f3f8`, `DECISIVE:` & `stdout` `SHA-256 3e746c6518022440`, `5 / 5` controls)
  - Disjoint cold-room countercheck (`0` shared imports, `SHA-256 48967b27e09d7183`) pre-committed `@ fb7d64ec9`;
    single-run output `c66_countercheck_out.json` sealed `@ 2c03eb4fe` (`SHA-256 7dd334974d4b12ba`, `discrepancies_count == 0`, `5 / 5` `RPF`)

---

## 1. Equal-Footing All-Prime `P^1(F_p)` Split & Unique `(3, 3, 3)` Systole Parabolicity at `p = 5` (`E1`, `P-845`)

- **Two-Counts Remainders Without Choosing a Prime or Thread (`GM1`, `GM2`, `GM5b`):** On the foundational pair of integer counts `(a, b)^T in Z^2`,
  `L = [[1, 1], [0, 1]]` and `R = [[1, 0], [1, 1]]` generate `C_omega = L R^-1 = [[0, 1], [-1, 1]]` (`C_omega^3 = -I_2`) and the three `C_omega`-cycled
  parabolic cusp shears `P_1 = L`, `P_2 = C_omega L C_omega^-1 = R^-1 = [[1, 0], [-1, 1]]`, and `P_3 = C_omega^2 L C_omega^-2 = [[0, 1], [-1, 2]]` (`all det = 1,
  tr = 2`), which fix `T_{cusp} = {[1 : 0], [0 : 1], [1 : 1]}` (`size 3`) for **every** prime `p >= 2`, leaving `|R_p| = p - 2` lines (`0 at p = 2; 1 fixed line
  [1 : 2] at p = 3; uniquely 3 lines forming a single complementary C_omega-triplet T_{sys} = {[1 : 2], [1 : 3], [1 : 4]} at p = 5; and p - 2 >= 5 at all p >= 7`).
- **Unique Parabolicity of `(3, 3, 3)`'s Three Systoles at `p = 5`:** The three `C_omega`-cycled systoles at `(3, 3, 3)`, `U_1 = L R = [[2, 1], [1, 1]]`,
  `U_2 = [[2, -1], [-1, 1]]`, and `U_3 = [[0, 1], [-1, 3]]` (`all det = 1, tr = 3, discriminant Delta = 3^2 - 4 = 5`), become parabolic modulo `p`
  (`(U_i + I_2)^2 == 0 mod 5`, `U_i != +-I_2 mod p`) **if and only if `p = 5`** (`certified across p in {2, 3, 5, 7, 11, 13, 17, 19, 23}`), fixing uniquely
  `[1 : 3], [1 : 4], [1 : 2] = T_{sys}`, while the `3 x 3` Jacobian of `W_{6,tr}` at `(3, 3, 3)` has exact eigenvalues `(14, 5, 5)` (`ratio 14 / 5`).

---

## 2. Thread-Free `6`-Move Spectrum on `(Z/pZ)^2 \ {(0, 0)}` & Native Golden Polynomial on `Leg(5)` (`E2`)

- **Universal Mirror Pairing (`All Primes p`):** Under `W_{6,omega} = sum_{j=0}^2 C_omega^j (L + R) C_omega^-j` and `C_{3,omega} = -C_omega = C_omega^4` (`exact order 3`),
  `tau = [[0, 1], [1, 0]]` satisfies `tau L tau = R`, `tau C_{3,omega} tau = C_{3,omega}^2`, and `tau W_{6,omega} tau = W_{6,omega}`, proving **`100%` exact
  `q = 1 ~= q = 2` charged pairing over `Z[x]` for every prime `p >= 2`** on `P^1(F_p)`, `Rays(p)`, and `Vecs(p)` (`whereas scalar trace orbits O_p pair 0 modes for p >= 5`).
- **Native Emergence of `x^2 - 3 x + 1` in `Leg(5)` With Zero Thread Chosen:** At `p = 5`:
  - `P^1(F_5)` (`6` lines): `P_{neu}(x) = (x - 6)(x - 2)` (`where +2 is 1_{T_{sys}} - 1_{T_{cusp}}`), `P_{chg}(x) = x^2 + x - 3`;
  - `6`-dim even-parity Legendre quadratic-character block `Leg(5)` (`(2 / 5) = -1`, `(-1 / 5) = +1`): `det(x I - W_{6,omega}|_{Leg(5)}) = (x^2 - 20)(x^2 - 3 x + 1)^2`;
  - `Rays(5)` (`12` rays): `P_{neu}(x) = (x - 6)(x - 2)(x^2 - 20)`, `P_{chg}(x) = (x^2 - 3 x + 1)(x^2 + x - 3)`;
  - `Vecs(5)` (`24` states): `P_{neu}(x) = x^4 (x - 6)(x - 2)(x^2 - 20)`, `P_{chg}(x) = (x^2 - 3 x - 3)^2 (x^2 - 3 x + 1)(x^2 + x - 3)`.
  Across all `9` primes `p in {2, 3, 5, 7, 11, 13, 17, 19, 23}` (`scoped explicitly`), `ker_Q(W_{6,omega}^2 - 3 W_{6,omega} + I)` is nonzero only at `p in {5, 23}`
  (`0` across `{2, 3, 7, 11, 13, 17, 19}`), and **`p = 5` is the unique prime in `{2..23}` where the golden kernel vanishes on `P^1(F_p)` (`dim 0`) and emerges
  purely in the quadratic cover `Leg(5)` (`dim 4` on rays/vectors; whereas `p = 23` already has `dim 4` on `P^1(F_23)` via genus-`2` `X_0(23)`)**.

---

## 3. Diagonal `O_{27} x Fiber_p` Bundles (`E3`) & Full-Bloch-Sphere `PF5` `SOS` Hierarchy (`E4`)

- **Diagonal `SL(2, Z)` Bundles Across `p in {2, 3, 5, 7}` (`E3`):** Under `L_{diag} = (L_{tr}, L)`, `R_{diag} = (R_{tr}, R)`, and `g_{C_3} = S^2 R^-1 L = (C_{tr}, -C_0)`
  (`exact order 3 in SL(2, Z)`, where `L C_0 L^-1 = C_omega` and `L W_{6,C_0} L^-1 = W_{6,omega}`), every tested `O_{27} x Fiber_p` bundle forms `1` single transitive
  `<L, R>`-orbit with `100%` `q = 1 ~= q = 2` pairing: `O_{27} x P^1(F_2)` (`216` pts) is exact Category `(a')` (`72 / 72`); `O_{27} x P^1(F_3)` (`288` pts) is exact
  Category `(a)` (`95 / 95`); at `p = 5`, `O_{27} x P^1(F_5)` (`432` pts, `d_0 = d_1 = 144`) halves `136 / 144` leaving monic `Z[y]` (`y = 2 x`) unpaired
  **`(y^2 - 2 y - 12)^2 (y^2 + 2 y - 12)^2`**, `O_{27} x Leg(5)` (`d_0 = d_1 = 144`) halves `136 / 144` leaving **`(y^2 - 6 y + 4)^2 (y^2 + 6 y + 4)^2 =
  2^8 (x^2 - 3 x + 1)^2 (x^2 + 3 x + 1)^2`** (`while odd-parity spinor Vecs(5) halves 0 / 288`), and `O_{27} x P^1(F_7)` (`576` pts) halves `182 / 190` leaving
  `(y^2 - 4 y - 4)(y^2 - 2 y - 4)(y^2 + 2 y - 4)(y^2 + 4 y - 4)`.
- **Exact Full-Bloch-Sphere `CP^1` `SOS` Hierarchy on `E_{phi^2} = ker(W_{6,omega}|_{Leg(5)} - phi^2 I_6)` (`E4`):** For **every** Bloch state
  `psi(theta, alpha) = cos(theta) e_+ + exp(i alpha) sin(theta) e_-` (`(theta, alpha) in R^2`):
  1. `W_{sys}(theta, alpha) = (5 + sqrt(5)) / 10`, `W_{cusp}(theta, alpha) = (5 - sqrt(5)) / 10`, and **`W_{sys} / W_{cusp} = (3 + sqrt(5)) / 2 = phi^2`**;
  2. **`3/10 - I_4(theta, alpha) = (1/10) sin^2(alpha) sin^2(2 theta) >= 0`** (`global CP^1 minimum 1/5 at the 2 chiral poles; global CP^1 maximum 3/10 identically
     across the continuous real mirror-equator sin(alpha) = 0`);
  3. **`11/90 - I_6(theta, alpha) = (1/45)[sin(theta)(4 cos^2(theta) - 1)]^2 + (2/15)(sin(alpha) sin(theta) cos(theta))^2 + (4/15)(sin(alpha) sin^2(theta) cos(theta))^2 >= 0`**
     (`chiral poles 2/45; real equator 1/9 + (1/90) cos(6 theta) with equator minimum 1/10 on the mirror-odd orbit and strict global CP^1 maximum 11/90 iff [psi] lies
     on the single 3-element C_omega-orbit of mirror-even single-systole-peaked states`).

0 of 19.
