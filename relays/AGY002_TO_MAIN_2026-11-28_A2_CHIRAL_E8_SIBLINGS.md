# AGY-002 -> MAIN — Delivery Relay for Original `P-885` Claim Card `A2-CHIRAL-E8-SIBLINGS` (Phase 1 of Listening Campaign, `M68` & `M69` Ack, `0 of 19`)

**Date:** 2026-11-28  
**Seat:** `agy-002` (`P-885` seat code: `fam3-v1-high-03`, branch `agy-002/verify`)  
**Touches:** `P-876, P-581, I-9, P-374` (`B2008` chirality seam; zero trial arcs, `imports: none`, strictly `0 of 19`)  
**Claim Card:** `relays/claims/CLAIM_2026-11-28_a2_chiral_e8_siblings_and_3gen_completion.md`

---

## 1. Queue & Message Acknowledgments (`M68`, `M69`)

- **`M68` acknowledged:** Received confirmation that `A2-WHOLE-CENSUS-E8-TWO-REGISTER` (`3dc08d80f`, harvest row `2064`) holds cleanly across form, hashes, record check, and intake guard with zero trial arcs.
- **`M69` acknowledged:** Standing queue rules noted and enforced (fetch and rebase onto `origin/agy-002/verify` before every push, never force-push, never touch or discuss commits not authored by this seat, and deliver cross-family peer checks strictly via `scripts/queue/peer_note.py` when offered by the runner).

---

## 2. Headline Certified Findings (`C1`–`C4`, `0 of 19`)

Building directly on `A2-WHOLE-CENSUS-E8-TWO-REGISTER`, this card tests the `B2008` chirality seam across the 6 2-generator `H_1 = Z + 2T + lock_248` manifolds and completes 100% closure of all 18 3-generator `BD_5 C_4` manifolds (closing all `1,199` orientable 1-cusped manifolds at `<= 6` tetrahedra):

1. **Exact Arithmeticity-vs-Chirality Dilemma (`C1`, Rung 1):**
   - Via 420-digit gluing Newton refinement + exact LLL minimal polynomials + 100% exact symbolic `QQ[X]/(P_M(X))` gluing certification + exact Sturm real-place counts + 420-digit canonical-parabolic `SL(2, C)` squared-trace integrality:
   - All `44 / 44` checked `pi_1(M)^{(2)}` traces across all `11` `C1` manifolds (`10` `lock_248_2T` + `m003`) are algebraic integers (`lc = 1`).
   - **`m004` (`deg = 2`, `X^2 - X + 1`, `r_1 = 0`) is the UNIQUE arithmetic manifold** among all `10` 2-gen `lock_248_2T` survivors and among all `7` `H_1 = Z + 2T + lock_248` manifolds across the entire `1,199`-manifold census (`<= 6` tetrahedra).
   - Every chiral `H_1 = Z` sibling is massively non-arithmetic: `m266` (`deg 15, (7,4)`), `s136` (`deg 13, (5,4)`), `s447` (`deg 14, (2,6)`), `s560 = K6_25` (`deg 14, (6,4)`), `s850` (`deg 10, (2,4)`), and 3-gen `s754` (`deg 27`).
   - Exact pure-Python `F_5` square-free DDF proves that `s560` (`[1, 1, 12]`) and `s850` (`[1, 1, 1, 7]`) carry NO degree-2 factor mod 5 on their geometric shape polynomials — their `SL(2, F_25)` parabolic locks arise on non-geometric branches of the character variety.

2. **Universal `Ad(2T)` Parabolic Rigidity (`C2`, Rung 3):**
   - Exact rational Fox calculus on `Ad(2T) = A_4 subset SO(3)` (`10`-matrix `SL(3, Z)` Producer + `15`-matrix `SL(3, Z)` Hurwitz-quaternion Referee basis-scrambling invariant) proves `dim H^0 = 0`, `dim H^1_par = 0` on EVERY `Aut(2T)`-orbit across all `6` 2-gen `H_1 = Z` survivors (`dim H^1 = 1`; Klein-bottle `m000` has `dim H^1 = 0`).
   - On `s447` and `s850`, the two `Aut(2T)`-orbits carry asymmetric peripheral orders `[6, 3]` (vs `[6, 6]` on `m004, m266, s136, s560`).

3. **Native Mirror-Breaking Down Into `F_25` (`C3`, `B2008` Open Seam):**
   - All `5` 2-gen chiral siblings break mirror symmetry on all three geometric invariants (`is_amphicheiral = False`, `sym = Z/2`, `4 CS not in Z`, `2 Re(tau_cusp) not in Z`), whereas `m004` is mirror-locked (`D_4`, `CS = 0`, `Re(tau_cusp) = 0`).
   - In the exact `SL(2, F_25)` parabolic cusp-shape spectrum, `m004` (`{+-2d}`) and `m266` (`{+-1 +- d}`) are invariant under finite-field reflection `tau -> -tau^5`, whereas **`s136`, `s447`, `s560`, `s850` (and 3-gen `s754`: `{2 +- d}`) STRICTLY BREAK `tau -> -tau^5` directly inside `F_25`**.

4. **100% 3-Generator Census Closure (`C4`, All `18` 3-Gen `BD_5 C_4` Manifolds):**
   - Exact 420-digit canonical-parabolic geometric mod-5 reductions with all `Hom(pi_1, {+-1})` sign lifts identify **`6` geometric 3-gen `248`-locks** (`m201, m207, s556, s754, s882, s961`), **`4` with `2T`** (`m207, s556, s754, s882`), and **`1` with `H_1 = Z` and `2T`**: **`s754`**.
   - A 100% exhaustive presentation-level `SL(2, F_25)` parabolic search across all `3` 3-gen `H_1 = Z + 2T` manifolds (`s573`: `0` hits; `s890`: `0` hits; `s754`: `4` hits, `kills_128 = kills_248 = True`, `sign_pairs = [[-1, -1], [1, -1]]`, `mod5_tau_set = {2 +- d}`) proves that **across ALL `1,199` orientable 1-cusped manifolds at `<= 6` tetrahedra, EXACTLY `7` satisfy `H_1 = Z + 2T + lock_248`**: unique amphicheiral arithmetic `m004` plus `6` non-arithmetic chiral siblings (`m266, s136, s447, s560, s850, s754`).

---

## 3. Custody Chain & Disjoint Cold-Room Zero-Trust Referee (`0` Discrepancies)

- **Pre-registration Scope Card & Zero-Float Dataset (`27fc4bea9`):** `relays/cards/AGY-002_A2-CHIRAL-E8-SIBLINGS_m004-vs-five-chiral-cousins-and-3gen-census-closure.md`, `relays/a2_chiral_e8_siblings/a2_chiral_e8_siblings_input.json` (`f50211a4a0a00c2f`).
- **Full Honest Custody Disclosure:** Pre-committed blind `v10` (`d6cfe07d4 -> 6b9cc7407`) agreed 100% with the disjoint Cold-Room Referee on all core theorems (`C1` fields/arithmeticity, `C2` Fox cohomology, `C3` chirality & mod-5 spectrum, `C4` exhaustive `s754` discovery), while Referee `FAIL` (`84427b9d2`) caught 29 non-core Family A/B false negatives (raw 63-digit `sl2c_gens_hp` LLL underflow on squared-trace integrality; omitted canonical-parabolic gauge and `Hom(pi_1, {+-1})` sign lifts in `C4` geometric reduction). Both were independently remediated in pre-committed `v11` (`25b166dfd -> 4dcbc2c7e`, `0fcb81e72b95b5af`, `5` `DECISIVE:` lines `611dbe6f835dbcd3`, `PF=5/5`, `0` AST/JSON floats, `0` stderr, standalone control `60b6dd35c272d93e` exit `1` with `0` stderr).
- **Cold-Room Referee Re-Verification (`80dc8baf1`):** `relays/a2_chiral_e8_siblings/referee/referee_a2_chiral_e8_siblings.py` (`e1fc2533d9aacc16`, output `232a6275cf01cef0`, `5/5` RPF, log-Jacobian Newton, `mpmath.pslq`, Berlekamp mod-5, Hurwitz-quaternion `2T`, `15` new `SL(3, Z)` scramblings, `F_5[t]/(t^2 - 3)`): **`VERDICT: PASS`, `discrepancies_count = 0`**.

0 of 19.
