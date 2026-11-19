# `AGY-002_FOUND-V2-U1` — Gate `F-U1` Results (Dihedral Cover `8^3_4`, `Berezin`-`CAR` `4D` Collar Action `A-FOCK-APS`, & `Kawamura` Doublet–Triplet Splitting, `0 of 19`)

## 1. Check Labels and Tracked Evidence (`docs/seats/README.md` § `12`)

- **expectations committed first:**
  - Card commit `0d22d097c`: `relays/cards/AGY-002_FOUND-V2-U1_dihedral-cover-berezin-aps-collar-action-and-doublet-triplet-splitting.md` (`and erratum card 6f480b986`: `relays/cards/AGY-002_FOUND-V2-U1-ERRATUM_cyclotomic-reduction.md`).
  - First producer seal `b7ee77877` (`unread output b28c44d89`): `relays/agy002_found_v2_u1/verify_found_v2_u1.py` (`passed all 50-digit numerical checks to < (1/10)^50, Section 2, and all 5 planted faults, with 2 SymPy booleans unreduced on exp(2*I*pi/5)`).
  - Companion cyclotomic `Phi_5` erratum seal `9d19c1166` & unread output `e6838845b`: `relays/agy002_found_v2_u1_v2/verify_found_v2_u1_v2.py`, `relays/agy002_found_v2_u1_v2/verify_found_v2_u1_v2_out.json` (`original sealed files untouched`).
- **recomputed independently:**
  - Cold-room referee script seal `455a17311` (`built from the Card alone without reading verify_found_v2_u1*, using Seifert matrix unimodular SNF, Fox free-differential Jacobian, exhaustive (2n)^2 dihedral search, exterior bitmask inversion parity, 945-matching combinatorial Pfaffian, and 1024-dim Cl(10) gamma algebra`) & unread output `b8c58533b`: `relays/agy002_found_v2_u1_referee/referee_found_v2_u1.py`, `relays/agy002_found_v2_u1_referee/referee_found_v2_u1_out.json`.
- **tested against planted errors:**
  - `5 of 5` planted cases caught identically in `b28c44d89`, `e6838845b`, and `b8c58533b` (`PFU1-1` trefoil `3_1` `det = 3` gives `Tr(Y^3) = -6 != 0`; `PFU1-2` bronze rival `p = 13` gives `dim C_{su(13)}(P_{13}) = 84 != 12`; `PFU1-3` level-`25` dihedral homomorphism `pi_1(m004) ->> D_{25}` count `0`; `PFU1-4` collar-even scalar parity `P Phi_s = +Phi_s` leaves `3` colour triplets and `0` weak doublets; `PFU1-5` full `32D` `Lambda^*(W_5)` without `(-1)^F = +1` is vector-like under `Y <-> -Y`).

## 2. Mask-Safe Rational Verification Summary (`0 of 19`)

| Check | Producer `v2` (`e6838845b`) | Cold-Room Referee (`b8c58533b`) | Sealed Rational Bar |
|---|---|---|---|
| `AST` source & `SHA-256` custody | `0` float literals, `0` complex literals, `0` repo imports, `SCRIPT_SHA256` matched | `0` float literals, `0` complex literals, `0` disallowed imports, `4 / 4` prior + self `SHA-256` matched | Exact (`0` mismatches) |
| Unique dihedral cover `8^3_4` & `Riley` longitude | `4` surjective maps at `n = 5` only (`0` at odd `n != 5` in `3..31`), `Riley` `lambda` commutes with `X` (`tr = -2`), orbits `[1, 2, 2]`, `Cent(D_5) = 1`, `Cent(Z_5) = 5` | Exhaustive `(2n)^2` search `20` total (`4` pinned) at `n = 5` only (`0` elsewhere), unimodular `SNF` `[1, 5]`, `Fox` `\|J(-1)\| = 5`, `Cent(D_5) = 1`, `Cent(Z_5) = 5` | Unique at `n = 5` |
| `24` `Weyl` operators & `6Y` identity | Orthonormal `< (1/10)^50`, `Tr(D P) = 1` `< (1/10)^50`, `-(1/2) sum D(v) = (1/2) I_5 - (5/2) P == diag(-2,-2,-2,+3,+3)` exact mod `Phi_5` (`< (1/10)^50`) | Exact & `60`-digit `mpmath` (`< (1/10)^60`), exact `Phi_5` reduction matching `diag(-2,-2,-2,+3,+3)` | Exact & `< (1/10)^35` |
| `Berezin`-`CAR`, `APS`, `G_{SM}`, & doublet-triplet | `0` `CAR` errors, `Berezin == det` exact, `16 + 16` `APS` split, `dim C_{su(5)}(P) = 12`, kernel `Z_6`, `6Y` `[-4^3,-3^2,0,+1^6,+2^3,+6]`, `4` anomalies `== 0`, `2` doublets / `0` triplets | Exterior wedge + `Cl(10)` gamma volume `(-1)^F`, `945`-matching Pfaffian `== det^2`, `dim 12`, `Z_6` (`6` elements), `6Y` `[-4^3,-3^2,0,+1^6,+2^3,+6]`, `4` anomalies `== 0`, `2` doublets / `0` triplets | Exact (`0` deviations) |

## 3. Theorems Locked in Gate `F-U1` (`Resolving Postulate D's 4 Bits into A-FOCK-APS`)

1. **Unique Irregular Cover `8^3_4` & Analytic-Algebraic `6Y` Identity:** `m004` (`4_1`) admits a surjective dihedral cover uniquely at `p = 5` (`0` at `p != 5`, `0` at level `25`), splitting the cusp into peripheral orbits `[1, 2, 2]` with `P = (+1^3, -1^2)` and trivial longitude `I_5`, while the double-cover rotation centralizer `X` and clock `Z` satisfy `q_{W_5} = -(1/2) sum_{v != 0} D(v) = (1/2) I_5 - (5/2) P == diag(-2, -2, -2, +3, +3)` in the `P`-eigenbasis.
2. **Unified `4D` Collar Action `A-FOCK-APS` (`P-863(a,c)`):** Grassmann `Berezin` path integration over the `5`-sheeted `m004` cover bundle generates `Cl(10) = End(Lambda^*(W_5))` identically (`not an ad-hoc assumption`); `4D` amphicheiral collar `APS` boundary conditions (`gamma_5 (-1)^F = +1`) lock `4D` left-handed chirality to `Lambda^{even}(W_5) = 16_+`; `Kawamura` meridian holonomy `P` projects `su(5) -> C_{su(5)}(P) = su(3)_c (+) su(2)_L (+) u(1)_Y` (`dim 12`, global kernel `Z_6`) with exact anomaly-free `6Y` charges `[-4^3, -3^2, 0, +1^6, +2^3, +6]` and projects a collar-odd scalar strictly onto the `2` weak-doublet zero modes (`0` colour triplets). Gate `F-U1` is locked. `0 of 19.`
