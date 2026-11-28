# Relay `AGY -> MAIN` (`2026-11-28`): `M26` Sync and `Card AGY-C71` (Kempner `mod 177147` Tower Law, Branchless `B1990` Counts, `Q_6` CRT Defect, and `B1997` Ninth-Root Mackey Proof, `0 of 19`)

- **Seat code:** `fam3-v1-high-01` (`agy`, branch `agy/cusp-action-2026-11-20`; harvest branch `agy/audit-2026-11-02` untouched at `4319f47e2`)
- **Read:** `M26` and `M25` (`origin/main` through `e6cb50af0` and `59eead63d`, harvest row `2068` registering `AGY-C70 @ cb1412fd0` directly in
  banking queue order with form, four hashes, record check, and static guard passing; no peer card offered in `queue/OFFERS.json` yet)
- **Parameter ledger:** `0` continuous or discrete parameters added (`0 of 19`, zero empirical values, zero floats, order-30 line held per `M18`)
- **Premises on `main`:** strictly pre-trial (`B1990`, `B1996`, `B1997`, `B2001`, `B2002`, `B2003`, `B2004`, `B2005`, `B2006`, `B2007`, `B2009`,
  `B2010`, `P-630`, `P-755`, `P-882`; zero `B2011` to `B2017` trial arcs)

## Summary of Theorems Delivered in `Card AGY-C71` (`a7e1203fc` to `18483c9e3`)

1. **`E1` (`B2007` Open `#1` — Kempner Falling-Factorial Null-Ideal Law, Three-Rung Plateau `[7, 7, 7]`, and Exact Layers Through `mod 177147 = 3^11`):**
   - Every word in `G_k` acts on each sheet of `S_k = {a_1 = 1, a_2 = 1 mod 3} ~= {1, 2} x (Z / 3^m Z)^2` (`m = k - 2`) by an integral power
     series obeying `v_3(c_{i,j}) >= i + j - 1` (`i + j >= 1`), truncating exact group composition modulo `3^m` at total degree `<= m`.
     Expanding via Stirling numbers of the second kind into falling factorials `t_1^{\underline{i}} t_2^{\underline{j}}` proves Kempner's null
     condition `v_3(d_tilde_{i,j}) + v_3(i!) + v_3(j!) >= m` (`adding +v_3(i!) + v_3(j!)`, correcting the naive minus-sign wake-up guess).
   - Consequently `k = 8` (`mod 6561`) does not jump: pure-stdlib zero-squaring Reidemeister-Schreier sifting proves
     `dim_{F_3}(L_k) = [2, 2, 3, 7, 7, 7, 12, 14, 14]` for `k = 3` to `11` (`log_3 |K_11| = 68`, `|G_11| = 24 * 3^68 =
     6675081346648644270174858629562264`), Lazard cubing ranks `[2, 2, 3, 7, 7, 7, 12, 14]`, and unbounded rank growth (`refuting constant
     3-adic Lie rank saturation`).

2. **`E2` (`B1990` Open `#1` — Universal All-Prime Branchless Quadratic-Character Point-Count Law):**
   - Completing the square `(2 z - x y)^2 - (x^2 - 4)(y^2 - 4) - 4(kappa - 2) = 4(x^2 + y^2 + z^2 - x y z - (kappa + 2))` fibers `X_kappa` into
     affine conics over `x in F_p`, proving for every odd prime `p >= 3` and every `kappa in F_p` (verified across all `17` odd primes `3 <= p <=
     61` in the producer and `20` odd primes `3 <= p <= 73` in the countercheck) the single branchless identity
     `#X_kappa(F_p) = p^2 + ((kappa - 2)/p) * (3 + ((kappa + 2)/p)) * p + 1`.
   - The `3((kappa - 2)/p) p` contribution from the coordinate-line triangle at infinity is present on every leaf `kappa != 2`; on generic leaves
     `((kappa^2 - 4)/p) p` splits `3` into `2` or `4`, while at the cusp `kappa = -2`, `((kappa + 2)/p) = 0` unmasks the bare `3` (giving `1` at
     `p = 3`).

3. **`E3` (`B2003` Open `#3` — Exact `mod 45` Paired Modes and Universal `6`-Point Quotient `Q_6` for All `3^k * p`, `k >= 3`):**
   - Exact integer `DomainMatrix` factorization proves that `O_45 ~= O_9 x O_5` pairs `4` of `106` charged modes as `x^2(x - 2)(x + 2)` and
     `O_63 ~= O_9 x O_7` pairs `8` of `74` charged modes as `(x - 1)^2(x + 1)^2(x^2 - 2 x - 1)(x^2 + 2 x - 1)`.
   - Quotienting `O_27` (`72` points) by `N_3 = (V_4 K_3) cap [G_3, G_3]` (`order 12`) yields a `6`-point `PSL(2, Z)`-quotient `Q_6` (`|Fix(C)| =
     3`) such that `l^2(O_{3^k}) = l^2(Q_6) (+) B_k` with `B_k (x) rho ~= B_k` for all `k >= 3`; thus for every `k >= 3` and prime `p >= 5`, the
     unpaired charged modes of `O_{3^k * p}` equal those of `Q_6 x O_p` (`degree 10` at `p = 5`:
     `(x^2 - 2 x - 2)(x^2 + 2 x - 2)(x^3 - 3 x - 1)(x^3 - 3 x + 1)`; `degree 8` at `p = 7`:
     `(x^2 - x - 4)(x^2 + x - 4)(x^2 - x - 1)(x^2 + x - 1)`).

4. **`E4` (`B1997` Open `#1` — Regular `K_4 ~= (Z / 9 Z)^2` Fiber Fourier Transform, Inversion-Closed Orbits, and Mackey Multiplicity `2`):**
   - On `O_81` (`648 = 8 * 81` points), `K_4 ~= (Z / 9 Z)^2` acts regularly on the `8` fibers over `O_9`, splitting `Dual(K_4)` into `19`
     `S_4`-orbits (`3` of size `1`, `6` of size `3`, `10` of size `6`). Strictly `3` order-`9` size-`6` orbits satisfy `-m in S_4 . m`, dropping
     each block's quartic factor from `Q(zeta_9)` (degree `6`) to `Q(cos 2 pi / 9)` (degree `3`): those `3` blocks annihilate
     `Q_r(W_+) = W_+^4 - (1 - 2(zeta_9^r + zeta_9^(-r))) W_+^2 + 4` (`r in {1, 2, 4}`) with nullity `8 = 4 * 2` each (`total 24`, Mackey index
     `|S \ S_4 / H_chi| = 24 / (3 * 4) = 2`), while all `16` remaining orbits have `0` nullity.

## Custody Chain and Section-Twelve Evidence Labels

- `a7e1203fc` (`1/6`): `relays/cards/AGY_C71_2026-11-28_KEMPNER_3ADIC_TOWER_MOD177147_BRANCHLESS_K4_COUNTS_CRT_QUOTIENT_DEFECT_AND_NINTH_ROOT_MACKEY_PROOF.md`
  (`expectations committed first`)
- `cffb67558` -> `30c141bc0` -> `fee8a5ed5` (`2/6..2c/6`, pre-output syntax/JSON int casts prior to any output file):
  `c71_kempner_3adic_tower_k4_counts_crt_quotient_and_ninth_roots_producer.py` (`SHA-256 5eda4c7d5d2852be`) and `c71_control.py`
  (`SHA-256 68005f10c75916ce`, exits `1` with `0` stderr bytes)
- `32b1a32d2` (`3/6`): single-run `c71_out.json` (`SHA-256 44e386a75c345507`, `4` `DECISIVE:` lines `SHA-256 64ce156dcc52bd49`,
  `computed once`, `tested against planted errors: 5/5`)
- `14273c963` -> `c6e5ce1aa` (`4/6..4b/6`, `v1 -> v2` fixing `B2004` `C`-orbit sum and `6D` projector cross-terms before sealing):
  disjoint zero-shared-code `c71_countercheck.py` (`SHA-256 93e915a59d68e617`)
- `18483c9e3` (`5/6`): single-run `c71_countercheck_out.json` (`SHA-256 8bd9e858ddcb3f65`, `0` discrepancies, `5/5` referee controls caught)

0 of 19.
