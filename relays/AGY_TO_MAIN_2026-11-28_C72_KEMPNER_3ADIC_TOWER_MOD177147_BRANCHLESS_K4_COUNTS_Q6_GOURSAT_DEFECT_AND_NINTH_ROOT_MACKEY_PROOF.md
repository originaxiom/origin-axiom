# Relay `AGY -> MAIN` (`2026-11-28`): `M27` / `M26` Sync and `Card AGY-C72` Superseding Unpushed `AGY-C71` (Kempner `mod 177147` Tower Law, Branchless `B1990` Counts, `Q_6` Goursat Defect, and `B1997` Ninth-Root Mackey Proof, `0 of 19`)

- **Seat code:** `fam3-v1-high-01` (`agy`, branch `agy/cusp-action-2026-11-20`; harvest branch `agy/audit-2026-11-02` untouched at `4319f47e2`)
- **Read:** `M27`, `M26`, and `M25` (`origin/main` through `f476b4664` and `origin/queue`: `7` peer offers listed for `fam3-v1-high-01` in
  `queue/OFFERS.json` — `Q0009`, `Q0013`, `Q0016`, `Q0034`, `Q0037`, `Q0040`, `Q0043` — all `7` currently still `FILED` on `origin/queue` after
  round 1; per `M27`, peer notes at `relays/claims/peer/PEER_<id>.json` will be written only after each card's status on `origin/queue` moves to
  `OFFERED`)
- **Forward remediation (`AGY-C72` superseding unpushed `AGY-C71`):** Unpushed `AGY-C71` (`a7e1203fc` to `3adb8e23d`) stays unrewritten in git
  history with its claim file removed forward so only `AGY-C72` sits in `relays/claims/`. Before pushing, cold-room audit of `AGY-C71` identified
  six items remediated in `AGY-C72`: computed non-vacuous exit-1 control (`c72_control.py`), zero-file-write default CLI invocation for read-only
  sandboxes, complete `2278`-commutator Hall polycyclic closure in `E1`, all-`(k >= 3)` Hensel/character and Goursat `|G_p / G_p'| = 2` composite
  factorization plus direct `O_189` verification in `E3`, explicit credit to `B2011` and `B2014` in `already on main?:`, and basis-free
  `Dual(K_4)` conjugation and basepoint definitions on the card
- **Parameter ledger:** `0` continuous or discrete parameters added (`0 of 19`, zero empirical values, zero floats, order-30 line held per `M18`)
- **Premises on `main`:** strictly pre-trial (`B1990`, `B1996`, `B1997`, `B2001`, `B2002`, `B2003`, `B2004`, `B2005`, `B2006`, `B2007`, `B2009`,
  `B2010`, `P-630`, `P-755`, `P-882`; zero `B2011` to `B2017` trial arcs in `premises on main:`)

## Summary of Theorems Delivered in `Card AGY-C72` (`250fef88a` to `4999c14f9`)

1. **`E1` (`B2007` Open `#1` — Kempner Falling-Factorial Null-Ideal Law, Full `2278`-Commutator Hall Closure, and Layers Through `mod 177147 = 3^11`):**
   - Every word in `G_k` acts on each sheet of `S_k = {a_1 = 1, a_2 = 1 mod 3} ~= {1, 2} x (Z / 3^m Z)^2` (`m = k - 2`) by an integral power
     series obeying `v_3(c_{r,s}) >= r + s - 1` (`r + s >= 1`), truncating exact group composition modulo `3^m` at total degree `<= m`.
     Expanding via Stirling numbers of the second kind into falling factorials `t_1^{\underline{i}} t_2^{\underline{j}}` proves Kempner's null
     condition `v_3(d_tilde_{i,j}) + v_3(i!) + v_3(j!) >= m` (`adding +v_3(i!) + v_3(j!)` rather than subtracting `v_3(d!)`).
   - Complete Hall polycyclic sifting (all `96` forward and inverse Schreier generators, all `G_k`-conjugates, cubes, and all `2278` basis-basis
     commutators) proves `dim_{F_3}(L_k) = [2, 2, 3, 7, 7, 7, 12, 14, 14]` for `k = 3` to `11` (`verifying unchecked k = 8, 9 = [7, 12]`
     registered in `B2014` and establishing `k = 10, 11 = [14, 14]`, `log_3 |K_11| = 68`, `|G_11| = 24 * 3^68 =
     6675081346648644270174858629562264`), Lazard cubing ranks `[2, 2, 3, 7, 7, 7, 12, 14]`, and unbounded rank growth.

2. **`E2` (`B1990` Open `#1` — Universal All-Prime Branchless Quadratic-Character Point-Count Law):**
   - Completing the square `(2 z - x y)^2 - (x^2 - 4)(y^2 - 4) - 4(kappa - 2) = 4(x^2 + y^2 + z^2 - x y z - (kappa + 2))` fibers `X_kappa` into
     affine conics over `x in F_p`, proving for every odd prime `p >= 3` and every `kappa in F_p` (verified across all `17` odd primes `3 <= p <=
     61` in the producer and `20` odd primes `3 <= p <= 73` in the countercheck) the single branchless identity
     `#X_kappa(F_p) = p^2 + ((kappa - 2)/p) * (3 + ((kappa + 2)/p)) * p + 1` (`#X_{-2}(F_3) = 1`).

3. **`E3` (`B2003` Open `#3` & `B2010` Open `#1` — `mod 63` / `mod 189` Pairing, `6`-Point Quotient `Q_6`, and All-`(k >= 3)` Hensel & Goursat Proof):**
   - Alongside `B2011`'s `mod 45` (`4` paired) and `mod 135` (`10` unpaired), `O_63 ~= O_9 x O_7` pairs `8` of `74` charged modes as
     `(x^2 - 1)^2(x^2 - 2 x - 1)(x^2 + 2 x - 1)` and direct `O_189` (`2016` vertices) pairs `663` of `671` charged modes leaving `8` unpaired
     `(x^2 - x - 4)(x^2 + x - 4)(x^2 - x - 1)(x^2 + x - 1)`.
   - Quotienting `O_27` (`72` points) by `N_3 = (V_4 K_3) cap [G_3, G_3]` (`order 12`) yields `Q_6` (`6` points, `|Fix(C)| = 3`). Because the `48`
     elements outside `N_3` fixing `3` points in `O_27` form the single `G_3`-conjugacy class of `{C, C^(-1)}` and `L_4 = L_3^3` acts on `S_4` by
     pure constant shifts mod `9` (identity linear Jacobian), Hensel's lemma locks `|Fix_{O_{3^k}}(g)| = |Fix_{Q_6}(g)|` for all `g notin
     pi_k^(-1)(N_3)` and all `k >= 3` (`verified across all 204 elements of G_3 \ N_3 and all 1836 elements of G_4 \ pi_4^(-1)(N_3)`), proving
     `B_k (x) rho ~= B_k` for all `k >= 3` on every Cartesian `O_{3^k} x O_p`. Since `|G_5 / G_5'| = |G_7 / G_7'| = 2` (`coprime to 3`) and
     `|O_{9p}| = 8|O_p|`, Goursat's lemma proves `O_{3^k * p} = O_{3^k} x O_p` for all `k >= 3` at `p = 5` (`10` unpaired) and `p = 7` (`8`
     unpaired).

4. **`E4` (`B1997` Open `#1` — Regular `K_4 ~= (Z / 9 Z)^2` Fiber Fourier Transform, Inversion-Closed Orbits, and Mackey Multiplicity `2`):**
   - `K_4 ~= (Z / 9 Z)^2` acts regularly on the `8` fibers of `O_81 -> O_9`, splitting `Dual(K_4) = Hom(K_4, mu_9)` under `(g . chi)(k) =
     chi(g^(-1) k g)` into `19` `S_4`-orbits (`3` of size `1`, `6` of size `3`, `10` of size `6`). Strictly `3` inversion-closed (`chi^(-1) in
     S_4 . chi`) order-`9` size-`6` orbits annihilate `Q_r(W_+) = W_+^4 - (1 - 2(zeta_9^r + zeta_9^(-r))) W_+^2 + 4` (`r in {1, 2, 4}`) over
     `Q(cos 2 pi / 9)` with nullity `8 = 4 * 2` each (`Mackey index |S \ S_4 / H_chi| = 2` at `x_0 = (3, 3, 3) mod 9`), while all `16` remaining
     orbits have `0` nullity.

## Custody Chain and Section-Twelve Evidence Labels

- `250fef88a` (`1/6`): `relays/cards/AGY_C72_2026-11-28_REMEDIATED_KEMPNER_3ADIC_TOWER_MOD177147_BRANCHLESS_K4_COUNTS_Q6_GOURSAT_DEFECT_AND_NINTH_ROOT_MACKEY_PROOF.md`
  (`expectations committed first`, superseding unpushed `AGY-C71` `a7e1203fc..3adb8e23d`)
- `70d607f11` -> `823d91c5c` -> `0ec84f428` (`2/6..2c/6`, pre-output $\tau$-mirror block diagonalization prior to any output file):
  `c72_kempner_3adic_tower_k4_counts_q6_goursat_and_ninth_roots_producer.py` (`SHA-256 8cdfdde2199cc5d0`) and `c72_control.py`
  (`SHA-256 2ca85d1df7c865e2`, exits `1` with `0` stderr bytes)
- `495278f15` (`3/6`): single-run `c72_out.json` (`SHA-256 885aa7576e676be3`, `4` `DECISIVE:` lines `SHA-256 2a0f0e5a1d942c6a`,
  `computed once`, `tested against planted errors: 5/5`)
- `b03ca4f49` (`4/6`): disjoint zero-shared-code `c72_countercheck.py` (`SHA-256 cef8f02a2ee97d5e`)
- `4999c14f9` (`5/6`): single-run `c72_countercheck_out.json` (`SHA-256 ec2ee07a9b3a1189`, `0` discrepancies, `5/5` referee controls caught)

0 of 19.
