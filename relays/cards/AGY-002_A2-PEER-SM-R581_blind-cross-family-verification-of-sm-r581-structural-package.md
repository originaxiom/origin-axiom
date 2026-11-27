# SCOPE CARD — Card A2-PEER-SM-R581: Blind Cross-Family Independent Verification of `SM-R581` (`P-581`, `I-9`, `1,199` Census Manifolds & `(Z_6, Y, 3/8)` Structural Package) (seat code: `fam3-v1-high-03`, `0 of 19`)

- **card id:** A2-PEER-SM-R581 (pre-registration; blind cross-family `fam3-v1-high-03` second computation of `fam1-v1-unset-04`'s `P-885` card `SM-R581` on `origin/sm/cards @ 1c5b13d0a` that carries `second computation: none`)
- **seat code:** `fam3-v1-high-03`
- **date:** 2026-11-27
- **touches:** `P-581`, `I-9`
- **imports:** orientable one-cusped hyperbolic census presentations with `<= 6` ideal tetrahedra (`1,199` manifolds, independently extracted directly from SnapPy 3.3.2 `OrientableCuspedCensus(cusps=1, tets=2..6)` into `relays/a2_peer_sm_r581/a2_r581_snappy_presentations.json`, zero files copied from `sm/cards`)
- **premises on main (zero trial arcs):** `B727`, `B861`, `B862`, `B993`, `B996`, `B1160`, `P-581`, `I-9`
- **blindness & custody:** Strictly `0 of 19`. ZERO `origin/sm/cards` scripts, presentations, or outputs (`r581*`, `sm_r581*`) opened prior to committing this Scope Card, the independent verifier script, and its unread sealed outputs.

## Pre-Registered Blind Expectations & Falsification Criteria

1. **Independent Census Presentations (`1,199` Manifolds, `<= 6` Ideal Tetrahedra):**
   - Independently extracted from SnapPy 3.3.2 `OrientableCuspedCensus(cusps=1, tets=2..6)`: `2 + 9 + 52 + 223 + 913 = 1,199` manifolds (`1,041` 2-generator / 1-relator; `158` 3-generator / 2-relator).

2. **Exact Group Tables & Exhaustive Surjection Census (`2T`, `2O`, `2I`, `Z/3`, `(Z/2)^3`):**
   - Build exact multiplication tables and full automorphism groups `Aut(G)` directly from exact algebra:
     * `2T = SL(2, F_3)` (`|2T| = 24`, `|Aut(2T)| = 24`),
     * `2O` over exact `Z[sqrt(2)]/2` quaternions (`|2O| = 48`, `|Aut(2O)| = 48`),
     * `2I = SL(2, F_5)` (`|2I| = 120`, `|Aut(2I)| = 120`).
   - Count exact `Aut(G)`-classes of surjections `pi_1(M) ->> G` across ALL `1,199` manifolds (asserting exact divisibility `raw_surjections % |Aut(G)| == 0` on every manifold):
     * Verify `m004` has **exact `2` `Aut(2T)`-classes** (`48 / 24 = 2`).
     * Verify total manifolds in `K` admitting `pi_1(M) ->> 2T` is **`384 / 1199`** (`0.320267...`), and report exact counts for `2O` and `2I` as well.
   - Verify BOTH stated plants across all `1,199` manifolds:
     * `pi_1(M) ->> Z/3`: holds on **`1,199 / 1,199`** (rate `1`) with exact count `3^d - 1` (`d = dim_{F_3} H_1(M; F_3)`) on every single manifold!
     * `pi_1(M) ->> (Z/2)^3`: fails (`0` surjections) on **`1,041 / 1,041`** two-generator presentations!

3. **Exact Manifold-Independent Post-`E_6` Structural Package (`Z_6`, `Y`, `sin^2 theta_W = 3/8`):**
   - Solve `ker(SU(3) x SU(2) x U(1) -> S(U(3) x U(2)) subset SU(5))` directly -> exact cyclic group `Z_6` of order `6` (element orders `[1, 2, 3, 3, 6, 6]`).
   - Solve exact `SymPy` traceless commutant of `su(3) (+) su(2)` inside `su(5)` -> exact dimension **`1`**, uniquely proportional to **`diag(2, 2, 2, -3, -3)`**.
   - Compute exact `sin^2 theta_W = Tr(T_3^2) / Tr(Q^2)` on the `5` along that unique hypercharge direction -> exact `Fraction(3, 8)`.
   - Confirm `rate(package | 2T) = 1` identically across all `384` `2T`-admitting manifolds (`384 / 1199`).

4. **Controls & Hygiene:** `5/5` independent planted fault controls, `0` AST float literals, `0` JSON float literals, standalone exit-1 control with `0` stderr bytes, `0` refused imports under `T7b Part 1`.
