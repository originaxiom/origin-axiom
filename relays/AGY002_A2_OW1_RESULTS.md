# `AGY-002_A2-OW1` — Open-Flute Gauge-Matter Engine (`Delta(2,3,N)` Without `m004`) and Unblocked `MC:REACH` Census Results (`0 of 19`)

## 1. Check Labels and Tracked Custody (`docs/seats/README.md` § `12`)

- **expectations committed first:**
  - Card commit `62a106f14`: `relays/cards/AGY-002_A2-OW1_open-flute-gauge-matter-engine-and-unblocked-mc-reach-census.md`.
  - Disclosed Errata committed before authoritative `v3`: `8a8ae772c` (`Erratum 1`: `SnapPy` `reverse_orientation()` in-place copy fix) and `060410501` (`Erratum 2`: `SnapPy` unoriented `is_isometric_to` vs oriented `symmetry_group().is_amphicheiral()` + `cusp_maps()[0].det() < 0` catch). Earlier sealed runs `f6cfa58ba`/`60c969a76` (`v1`) and `63d5f6649`/`759796baa` (`v2`) are preserved untouched.
  - Authoritative producer `v3` script seal `16264b8f6` (`relays/a2_ow1_v3/verify_a2_ow1_v3.py`, `SCRIPT_SHA256.txt`) & unread output seal `5f41c72de` (`relays/a2_ow1_v3/verify_a2_ow1_v3_out.json`, `OUTPUT_SHA256.txt`, `all_gates_passed = true`).
- **recomputed independently:**
  - Independent Cold-Room Referee built from Card + Errata alone (zero access to producer files prior to `Commit 4b`), using independent Todd-Coxeter coset enumeration, dual `SnapPy` + `Aut(F_2)` mapping-torus presentations, and dual Fox `J(-1)` SNF + Seifert `|det(V + V^T)|` determinants: script seal `7634a434b` (`relays/a2_ow1_referee/referee_a2_ow1.py`, `SCRIPT_SHA256.txt`) & unread output seal `ccc22f6a1` (`relays/a2_ow1_referee/referee_a2_ow1_out.json`, `OUTPUT_SHA256.txt`, `0` discrepancies across `1095` cross-checked fields).
- **tested against planted errors:**
  - `4 of 4` planted faults caught identically in both `5f41c72de` and `ccc22f6a1` (`PF-OW1-1` rung `N = 2` `S_3` gives `Tr(Y^3) = -6 != 0`, `dim = 4`; `PF-OW1-2` rung `N = 3` `A_4` is non-chiral, `dim = 7`; `PF-OW1-3` odd transposition in `S_5 \ A_5` gives `dim = 16 != 12`; `PF-OW1-4` higher `D_7` gives `dim = 24 != 12`, `fock = 64`).

## 2. Mask-Safe Verification Summary (`0 of 19`)

| Task / Metric | Producer `v3` (`5f41c72de`) | Cold-Room Referee (`ccc22f6a1`) | Match |
|---|---|---|---|
| `AST` source & `SHA-256` custody | `0` float/complex literals, `0` `frontier/` imports, `A`-only manifests `OK` | `0` float/complex literals, `0` `frontier/` imports, `A`-only manifests `OK` | Exact (`0` mismatches) |
| `OW1-A`: Finite rungs `Delta(2,3,N)` | `N in {2, 3, 4, 5}` (`orders 6, 12, 24, 60`), `N = 6` infinite (`5/6 + 1/6 = 1`) | Identical via Todd-Coxeter + explicit `A_5 ~= PSL(2, F_5)` | Exact |
| `OW1-A`: All `21` faithful `(N, d <= 12, P)` pairs | Unique chiral anomaly-free hit: `N = 5` (`A_5`), `d = 5` (`A_5 / A_4`), `P = [1, 2, 2]`, `(a, b) = (3, 2)`, `dim = 12`, `16` chiral, `0` anomalies, `Z_6` (`|K| = 6`), `2` doublets / `0` triplets | `0` mismatches across all `21` pairs; exact same unique SM hit | Exact (`21 / 21`) |
| `OW1-A`: `A_5` uniqueness & `24`-Weyl / `Cl(10)` `CAR` | `1` index-`5` (`A_4`), `1` index-`6` (`D_5`, ord `10`), `1` involution class (`15`); Weyl id exact mod `Phi_5` and `< (1/10)^50` (`65` dps); `0` `CAR` errors | Identical `A_5` uniqueness; Weyl id exact mod `Phi_5` and `< (1/10)^50` (`60` dps); `0` `CAR` + `0` `Cl(10)` gamma errors | Exact |
| `OW1-B`: Unblocked `50` punctured-torus threads (`21+`, `21-`, `8P`) | `0` `H_1` mismatches; `32` `D_5`, `6` `D_5` all-trivial cusp, `26` `2T`, `34` `A_5`; `6` pass `D_5`-all-triv + `2T` (`4` chiral orientable `s640`/`s001`, `1` amphichiral `m004`, `1` non-orientable `m024`) | `0` mismatches across `650` per-thread fields and `0` mismatches between `SnapPy` and `3`-gen presentations (plus notes `2` mixed-cusp `D_5` threads `b++LLLRR`, `b++LLRRR` with `2T = 0`) | Exact (`650 / 650`) |
| `OW1-C`: All `35` prime knots `3_1..8_21` (`MC:REACH`) | `0` `det` vs `D_p` mismatches; `8` pass `D_5` (all trivial longitude), `15` `2T`, `21` `A_5`; `3` pass both `D_5` and `2T` (`4_1`, `8_18`, `8_21`); `4` chiral hyperbolic pass `D_5` (`7_4`, `8_8`, `8_16`, `8_21`), `1` chiral hyperbolic passes both `D_5` and `2T` (`8_21`, also `A_5 = 3`) | `0` mismatches Fox `J(-1)` SNF vs Seifert `|det(V + V^T)|`, `0` mismatches across `420` per-knot fields (`175/175` `D_p` divisibility checks) | Exact (`420 / 420`) |
| `OW1-D`: Planted faults (`PF-OW1-1..4`) | `4 / 4` caught | `4 / 4` caught | Exact (`4 / 4`) |

## 3. Core Foundational Findings (`0 of 19`)

1. **The Standard Model Gauge-Matter Engine Does NOT Require `m004`, `G:SE1`, or `G:SE2`:** Across all four
   finite quotients of the open weave (`Delta(2,3,N)`, `N = 2, 3, 4, 5`) and all `21` faithful transitive `(N,
   d <= 12, P)` permutation actions, the minimal `5`-point action of the top finite rung `Delta(2,3,5) = A_5`
   on `A_5 / A_4` is the **unique** chiral, anomaly-free action. Every involution `P in A_5` is forced by even
   parity to cycle type `[1, 2, 2]` (`a = 3, b = 2`), and its unique maximal dihedral subgroup `D_5 < A_5`
   (`index 6`, matching `[SL(2, Z) : Gamma_0(5)] = 6`) generates the entire `Gate F-U1` `24`-Weyl `6Y`
   identity, `Cl(10)` `Berezin`-`CAR` `16`, `SU(3) x SU(2) x U(1) / Z_6` (`dim 12`), and doublet-triplet
   splitting directly on the open weave with zero hand-picked knot.
2. **Unblocked `MC:REACH` Refutes `m004`-Uniqueness on Single Threads:** Dropping `G:SE1` and `G:SE2` reveals
   that `m004` (`b++LR`) is **not** unique among either punctured-torus threads or prime knots in `S^3`: `4`
   chiral orientable threads (`b++LLLRLR`, `b++LRLRRR`, `b+-LLLLLR`, `b+-LRRRRR`) and `1` non-orientable
   thread (`b-+LLLLL` = `m024`, which also surjects onto `A_5`) pass `D_5`-trivial-cusp + `2T`, while in `S^3`
   the chiral hyperbolic knot `8_21` (`det = 15`) passes `D_5` (trivial longitude) + `2T` + `A_5`, and `m003`
   (`b+-LR`) + `m000` (`b-+L`) pass `2T` with `D_5 = 0`. `m004` is merely the smallest-volume orientable
   amphichiral representative of an infinite family, whereas the gauge-matter engine itself lives natively on
   the open weave's top finite rung `A_5`. `0 of 19.`
