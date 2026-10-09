# B1630 — THE TICK'S POINT: the principle's tick passes through τ = i, not ω; at i the weave's residual symmetry fixes the clock's line and swaps the two letter lines, so every mass spectrum is one value apart and two equal (never three distinct), the single on the clock's line — the 1 + 2 the rule's word gave outside the weave, now from the weave's own symmetry; the clock's line mixes only with itself

**Verdict: PROVED** (Z0, Z1, Z2 and Z4 hold as sealed. Z3 holds after a disclosed post-seal repair: the sealed run tested
only basis vectors of two-dimensional eigenspaces). cc (main), 2026-10-09. Sealed `87d769c7a` before the run. A READING,
"given τ = i"; adopting τ = i would be the owner's to decide. No data. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /tau = i|τ = i|the point i|elliptic point|stabiliser of i/: 1 of 1401 arcs on main match (PROVED 1)`
— B1617, B1618, B1620 part B, B1621, B1629 and the SM seat's §41.2. **Literature:** modular forms at the elliptic point i.

## 1. The computation (`weave_at_i.py`, sealed, unchanged; the sealed run in `verification/sealed_run/`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **Z0** | the tick's axis through i, not ω | 98% | **HOLDS, exactly** — LR's axis is the circle \|z − ½\|² = 5/4 (center ½ in this convention), which contains i (¼ + 1 = 5/4) and not ω (1 + ¾ ≠ 5/4) |
| **Z1** | S fixes i; the residual group at i finite, preserving T | 95% | **HOLDS** — S = R L⁻¹ R (H₁ matrix [[0, −1], [1, 0]]) fixes i; with ι and the inner lifts it generates a group of order 32 on V |
| **Z2** | S fixes exactly the clock's line (−, −) and swaps the two letter lines | 80% | **HOLDS** — S is monomial on the parity lines, swaps (−, +) ↔ (+, −) and fixes (−, −); T's commutant under the residual group has dimension 2 (T = a line ⊕ an irreducible plane) |
| **Z3** | no spectrum with three distinct values, under any tensor or phase; a 1 + 2 single on the clock's line | 75% | **HOLDS, after repair (§2).** As sealed, every basis vector numpy returned gave "a pair and a single", but several S-eigenspaces are two-dimensional and the sealed code tested no generic element; its single-line check (diagonal matrices only) never fired |
| **Z4** | S of finite order on T | 95% | **HOLDS** — order 8, eigen-turns ⅜, ⅜, ⅞ |

## 2. The repair (`post_seal_generic.py`, written after the sealed run; disclosed)

For every tensor, ι cell and S-eigenspace, 12 random complex combinations (three seeds) were classified. The odd
singular value's line was located basis-independently, from the eigenvector of M M† at that value against the parity
lines.

| tensor | cells (ι, S-turn, dim) | spectra of generic couplings | the single's line |
|---|---|---|---|
| T̄ ⊗ T | (+1, 0, 2), (+1, ½, 1) | all "a pair and a single" | the clock's line (overlap 0.999995) |
| T ⊗ T | (−1, ¼, 1), (−1, ¾, 2) | all "a pair and a single" | the clock's line (−, −) |
| Sym² T | (−1, ¼, 1), (−1, ¾, 2) | all "a pair and a single" | the clock's line (−, −) |

## 3. What it says

- **The principle's tick picks out i** among the two distinguished points: its axis passes through i, not through ω,
  the point of the retired postulate.
- **At i, the weave's own residual symmetry fixes the clock's line and swaps the two letter lines.** So every mass
  spectrum, under every tensor and every weight, is one value apart and two equal, never three distinct, and the single
  value sits on the clock's line. That is the same 1 + 2 split the rule's word gave outside the weave (B1620 part B):
  **two of the principle's forced data single out one line.**
- **The mixing keeps the clock's line apart.** Every sector is diagonal in the parity lines (T-TAU-ONLY-PERMUTATION), so the clock's line maps to the clock's line and the pair's plane to itself. With two equal masses the rotation inside the pair is undetermined, a U(2) freedom the independent check made explicit. So the basis-independent statement is that the line is kept, not that the mixing is a permutation.
- So τ = i gives a leading-order shape, one apart and two together, as in the neutrinos' two close masses. It gives
  neither three distinct masses nor a value. 0 of 19.

## 4. Disclosed

- Z3's sealed run tested only the basis vectors `eig` returned. The repair tests generic couplings, and the conclusion
  is the sealed prediction's.
- Z0 was not blind (B1629's tops and the seat's §41.2 were seen).
- **Independent check (B1631):** a verifier agent rebuilt the claims from the group's closed form without main's code.
  - (0) is exact (|ω − ½|² = 7/4 ≠ 5/4).
  - (1) and (2) hold: no "three distinct" in about 14 000 generic samples, with controls that do fail without the
    constraints. The analytic reason is that S sends diag(d₁, d₂, d₃) to ε(d₂, d₁, d₃).
  - (3) holds: the odd value's eigenvector is the axis S fixes, which Z2 computed to be the clock's line.
  - (4) holds in the stated form: the line is kept, and the mixing inside the pair is free.
  - ι acts on T as −i, consistent with S² = −I and with the record's sector labels.

## 5. Files

`verification/weave_at_i.py` (sealed, unchanged), `weave_at_i.json`, `sealed_run/`; `post_seal_generic.py` and its outputs.
Test: `tests/test_b1630_the_ticks_point.py`.
