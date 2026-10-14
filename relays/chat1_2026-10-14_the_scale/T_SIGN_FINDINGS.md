# T-SIGN: the CP bit of an amphichiral thread is the sign of its monodromy, so the positivity ruling chooses bit 0

chat1, 2026-10-14.
- **Sealed** at `50352be3a` (sha256 258718ef…). The script `t_sign.py` was committed before its one run; its output is
  `t_sign_run.txt` and `t_sign.json`.
- **Every cell held as sealed. 0 of 19.**

| | prediction | prior | outcome |
|---|---|---|---|
| N0 (control) | b+-LR = m003 at CS = ±π²/2; all minus bundles build, orientable and geometric | 95% | **HOLDS.** m003 at 4.934802 = π²/2 |
| N1 | every swap-symmetric word of length ≤ 14 has CS(b+-W) = ±π²/2 (bit ¼) | 75% | **HOLDS, 120 of 120** |
| N2 | for every word of length ≤ 10, CS(b+-W) − CS(b++W) ≡ π²/2 (mod π²) | 45% | **HOLDS, 224 of 224** |

The post hoc read-out from T-ROOT's data covers the plus side (`post_hoc_cp_bit.json`): to length 18, all 514
swap-symmetric plus threads sit at CS = 0, none at ¼, and no chiral thread sits at 0 or ¼.

**Read-out.** Vol(b+-W) = Vol(b++W) on every word checked: the sign changes the Chern–Simons invariant, not the volume.

## What it shows

- **[MATH, to the lengths checked]** Amphichirality forces the Chern–Simons bit into {0, ¼} (B1224). On the threads that
  bit is exactly the sign of the monodromy: 0 for +W, ¼ for −W.
  - More generally, flipping the sign shifts CS by exactly ¼, on every word checked.
  - One reason the shift can only be 0 or ¼: the bundle of W² double-covers both the +W and the −W bundles. That is a
    reason, not a proof.
- **The positivity ruling (GM5d, the owner's) is therefore exactly the choice of CP bit 0** on every amphichiral thread.
  - B1226's ¼ example, m003, is the minus thread b+-LR, which the ruling keeps outside the weave.
- **[READING; I-18 UNEARNED]** If the CS 2-torsion is θ̄'s bit (θ̄ ∈ {0, π}), the weave's own positivity sets θ̄'s bit
  to 0 on its amphichiral threads.
  - This answers L192's question ("does the object's ℤ/2 fix the CP-conservation bit") on the weave, conditionally on
    I-18. It says nothing about θ̄'s continuous value.

## Fence

- b±W bundles: N1 to length 14, N2 to length 10; the plus side to length 18 post hoc.
- Not proved for all lengths.
- I-18, the bit-to-θ̄ identification, is untouched. **0 of 19.**
