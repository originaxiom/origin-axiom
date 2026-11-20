# Pre-Registration Card `A2-OW1` — Open-Flute Gauge-Matter Engine (`Delta(2,3,N)` Ladder Without `m004`) and Unblocked `MC:REACH` Thread & Knot Census (`0 of 19`)

## 1. Purpose and Open-Weave Scope

This card drops the two hand-picked thread selections `G:SE1` (torsion-free first homology) and `G:SE2` (orientability) and executes two data-free (`0 of 19`) structural tests:

1. **Open-Weave Intrinsic Engine (`Delta(2,3,N)` Finite Ladder, Zero Thread Selected):**
   Test whether the full gauge-and-matter algebra previously derived on `m004`'s irregular cover `8^3_4` (`Gate F-U1`: `24`-operator Weyl identity, `Berezin`-`CAR` `Cl(10)` Fock space, chiral `16` fermions, centralizer `SU(3) x SU(2) x U(1) / Z_6` of dimension `12`, anomaly cancellation, and doublet-triplet splitting) emerges directly from the open weave's own finite quotient ladder `Gamma / <<T^N>> = Delta(2, 3, N)` (`N in {2, 3, 4, 5}`) without selecting any knot or thread.
2. **Unblocked `MC:REACH` Census (All Punctured-Torus Threads and All Prime Knots to Crossing `8`):**
   Compute without cherry-picking which punctured-torus bundles (both orientable `det = +1` and non-orientable `det = -1`, including `m000`, `m003`, `m004`, and all primitive hyperbolic words up to length `6` in `{L, R}` with signs and orientation reversal) and which of all `35` prime knots in `S^3` through `8` crossings (`3_1` through `8_21`) admit surjective `D_p` covers (`p in {3, 5, 7, 11, 13}`), trivial cusp longitude in `D_5`, surjective `2T = SL(2, F_3)` covers, and surjective `A_5 = PSL(2, F_5)` covers, alongside exact homology torsion, orientability, chirality / Chern-Simons sign, and hyperbolic volume.

All computations are strictly data-free (`0 of 19`, zero empirical constants, zero `frontier/` imports, zero float or complex `AST` literals in Python source).

## 2. Exact Pre-Registered Tasks and Pass Bars

### Task `OW1-A`: Open-Weave Finite Ladder `Delta(2, 3, N)` (`N in {2, 3, 4, 5}`) and All Transitive Faithful Permutation Actions

- Construct `Delta(2, 3, N) = <s, u | s^2 = u^3 = (s u)^N = 1>` explicitly as finite permutation groups for `N = 2, 3, 4, 5` and verify the spherical finiteness bound `1/2 + 1/3 + 1/N > 1` holds if and only if `N in {2, 3, 4, 5}` (exact orders `6, 12, 24, 60`, while `N = 6` is infinite Euclidean).
- For each `N in {2, 3, 4, 5}`, enumerate all core-free subgroup classes giving faithful transitive permutation actions of degree `d <= 12`, and for every conjugacy class of involutions `P` in `Delta(2, 3, N)`, record its cycle partition, eigenvalue multiplicity `(a, b)` on `C^d` (`+1` with multiplicity `a`, `-1` with multiplicity `b`, `a + b = d`), centralizer `C_{su(d)}(P) = s(u(a) + u(b))` of real dimension `a^2 + b^2 - 1`, and the `Berezin`-`CAR` chiral exterior half `Lambda^{even}(C^d)` (`dim = 2^(d-1)`) under hypercharge generator `Y_raw = diag((-b)^a, (+a)^b)` (reduced by `gcd(a, b)`).
- Test exact chirality (`Y` spectrum NOT invariant under `Y -> -Y`), exact cancellation of all `4` anomalies (`Tr(Y)`, `Tr(Y^3)`, `Tr(SU(a)^2 Y)`, `Tr(SU(b)^2 Y)`), exact global kernel order `|K|` of `SU(a) x SU(b) x U(1)` acting on `Lambda^{even}(C^d)`, and collar-odd scalar doublet/triplet splitting.
- **Pre-Registered Bar `OW1-A`:**
  1. Among all finite rungs `N in {2, 3, 4, 5}` and all faithful transitive actions of degree `d <= 12`, verify whether the minimal faithful action of the top finite rung `Delta(2, 3, 5) = A_5` on `d = 5` cosets `A_5 / A_4` is the **unique** action yielding a chiral, anomaly-free `16`-dimensional `Lambda^{even}` with `dim C_{su(d)}(P) = 12` (`SU(3) x SU(2) x U(1)`), global kernel `Z_6`, exact `6Y` multiset `[-4^3, -3^2, 0, +1^6, +2^3, +6]`, and collar-odd scalar splitting to `2` doublets / `0` triplets.
  2. Inside `A_5` on `5` points, verify that `A_5` has a unique conjugacy class of maximal dihedral subgroups `D_5` (order `10`, index `6`), that every involution `P in A_5` has forced even cycle type `[1, 2, 2]` (`a = 3, b = 2`), and that the `24` nonzero Weyl-Heisenberg operators built from `(Z, P)` in `D_5` satisfy `-(1/2) sum_{v != 0} D(v) = (1/2) I_5 - (5/2) P = diag(-2, -2, -2, +3, +3)` in the `P`-eigenbasis both algebraically mod `Phi_5` and numerically to `< (1/10)^50` (`60`-digit `mpmath`).

### Task `OW1-B`: Unblocked Punctured-Torus Bundle Census (No `G:SE1`, No `G:SE2`)

- Enumerate the complete list of conjugacy classes of primitive hyperbolic punctured-torus monodromies up to word length `6` in positive `{L, R}` across all three branches:
  - Branch `+`: orientable `M in SL(2, Z)`, `tr(M) >= 3` (including `m004 = +LR`, `+LLR`, `+LLLR`, `+LLRR`, ...).
  - Branch `-`: orientable `-M in SL(2, Z)`, `tr(-M) <= -3` (including `m003 = -LR`, `-LLR`, `-LLLR`, ...), lifted to `Aut^+(F_2)` by the exact commutator-preserving involution `phi_S^2: (a, b) -> (b a^-1 b^-1, b a b^-1 a^-1 b^-1)`.
  - Branch `P`: non-orientable `M * P in GL(2, Z)` with `det = -1` (including `m000 = L P`, `L^2 P`, `L^3 P`, `L^2 R P`, ...), using `phi_P: (a, b) -> (b, a)` (`phi_P([a,b]) = [a,b]^-1`).
- For every thread `M_phi` in all three branches, compute directly from the exact `3`-generator mapping-torus presentation `<a, b, t | t a t^-1 = phi(a), t b t^-1 = phi(b)>` (and cross-check homology torsion and volume against `SnapPy` `Manifold` construction from the bundle monodromy):
  - First homology torsion `|det(M - I)|`, orientability `det(M)`, exact `D_p` surjection class counts for `p in {3, 5, 7, 11, 13}` (modulo `Aut(D_p)`), whether the cusp puncture commutator `[a, b]` maps to the identity in every `D_5` surjection, exact `2T = SL(2, F_3)` surjection class counts (modulo `Aut(2T)`), and exact `A_5 = PSL(2, F_5)` surjection class counts (modulo `Aut(A_5)`).
  - Report explicitly and honestly how `m000`, `m003`, `m004`, and every other thread perform on `D_5`, `2T`, `A_5`, trivial boundary `[a, b]`, volume, and chirality (`SnapPy` `is_isometric_to(reverse_orientation())` for orientable bundles).
- **Pre-Registered Bar `OW1-B`:** Exact agreement (`0` mismatches) between direct presentation `H_1` torsion and `SnapPy` abelianization on all tested threads, complete exhaustive `D_p` (`p in {3, 5, 7, 11, 13}`), `2T`, and `A_5` counts with zero omissions, and explicit verdict on whether `m004` is unique or shares the `D_5` / `2T` survival set with `m000`, `m003`, or longer threads.

### Task `OW1-C`: Unblocked `MC:REACH` Census of All `35` Prime Knots Through `8` Crossings in `S^3`

- Load all `35` prime knots in `S^3` with crossing number `3 <= c <= 8` (`3_1`, `4_1`, `5_1..5_2`, `6_1..6_3`, `7_1..7_7`, `8_1..8_21`) via `SnapPy`.
- For every knot `K`, compute directly from its `SnapPy` fundamental-group presentation and peripheral meridian/longitude words:
  - Exact knot determinant `|Delta_K(-1)|` (via exact integer Smith normal form of the `2`-fold branched cover / Fox Jacobian at `t = -1`).
  - Hyperbolic volume (`0` if non-hyperbolic / torus) and amphichirality / chirality (`M.is_isometric_to(M.reverse_orientation())` plus Chern-Simons invariant for hyperbolic knots).
  - Exact count of `D_p` surjection classes for `p in {3, 5, 7, 11, 13}`, exact image of the canonical longitude `lambda` in every `D_5` surjection, exact `2T = SL(2, F_3)` surjection class count, and exact `A_5 = PSL(2, F_5)` surjection class count.
- **Pre-Registered Bar `OW1-C`:** `35 / 35` prime knots computed with exact determinant cross-checked against `D_p` divisibility (`D_p` surjection exists if and only if `p | |Delta_K(-1)|` for every `2`-bridge/cyclic-torsion case, checked directly from `pi_1`), exact enumeration of all knots passing `D_5` (with trivial longitude -> `Gate F-U1` gauge/matter engine), all passing `2T`, all passing both `D_5` and `2T`, and explicit identification of any **chiral** hyperbolic knots in that survivor set.

### Task `OW1-D`: Four Planted Faults (`PF-OW1-1` through `PF-OW1-4`)

1. `PF-OW1-1`: Rung `N = 2` (`S_3`, `d = 3`, `a = 2, b = 1`) must fail anomaly cancellation (`Tr(Y^3) != 0`).
2. `PF-OW1-2`: Rung `N = 3` (`A_4`, `d = 4`, `a = 2, b = 2`) must fail chirality (self-conjugate `Y <-> -Y`) and give `dim = 7 != 12`.
3. `PF-OW1-3`: Odd permutation outside `A_5` (`S_5 \ A_5` transposition `[1, 1, 1, 2]`, `a = 4, b = 1`) must fail `SU(3) x SU(2) x U(1)` (`dim = 16 != 12`, wrong hypercharge spectrum).
4. `PF-OW1-4`: Higher odd dihedral `D_7` (`d = 7`, `a = 4, b = 3`) must fail `SU(3) x SU(2) x U(1)` (`dim = 24 != 12`).

## 3. Custody and Cold-Room Discipline

- Producer script sealed pre-run in `relays/a2_ow1/verify_a2_ow1.py` with `relays/a2_ow1/SCRIPT_SHA256.txt` (`A`-only).
- Output `relays/a2_ow1/verify_a2_ow1_out.json` and `relays/a2_ow1/OUTPUT_SHA256.txt` (`A`-only) committed unread before inspection.
- Independent Cold-Room Referee subagent built from this Card alone (never reading `verify_a2_ow1.py` or its output) seals `relays/a2_ow1_referee/referee_a2_ow1.py`, runs independently, and commits unread output + `SHA-256` manifest.
- Results relay `relays/AGY002_A2_OW1_RESULTS.md` reports Producer vs Cold-Room Referee honestly without post-hoc retargeting. `0 of 19.`
