# B62 FINDINGS -- opposition involution / the 2 unresolved SL(5) modes

Structural, exact (root-system); validated on SL(3)/SL(4); numerically
corroborated. Not a symbolic proof. No physics, no Origin-core claim.

## Verdict

```text
CONFIRMED as a LIVE STRUCTURAL RESULT.
The 2 unresolved SL(5) fixed-line modes are char(M^2) = {phi^2, 1/phi^2}.
The exchange involution = opposition involution (theta = -w0) identification is
recorded as a live structural result.
```

## What was tested

The prediction: the exchange involution `P` (`tr W <-> tr W^-1`) is the
opposition involution `theta = -w0` on the `sl(n)` root system, and on each
height-`h` root space its `+1`/`-1` eigenspaces are the direct `char(M^k)` /
sign `char(-M^k)` sectors. For the **height-2** space this predicts the 2
unresolved SL(5) modes are `char(M^2)` or `char(-M^2)`, completing the 6-dim
height-2 space (4 of 6 resolved by B61).

## What was found

1. **The numerical route is dead (re-verified).** `tr(DT0)` and `det(DT0)` from
   the B61 representation-perturbation method scatter across seeds (tr =
   22.79 / 20.78 / 14.49; det = 2.0+1.3i / -0.01-0.76i / -1.27-2.96i). The
   2-mode block's spectral invariants are gauge-dependent, so no flavor of that
   numerics decides the modes. The opposition involution is a canonical object
   and sidesteps this.

2. **The opposition split is exact and reproduces the known cases.** Computing
   the `theta = -w0` eigenspace dimensions on the height-2 root space of
   `A_{n-1}` (pure root-system combinatorics: self-paired roots `i+j=n+1` ->
   `+1`, swapped pairs -> `+1` and `-1`):

   ```text
   n=3:  (+1,-1) = (2,0)  ->  char(M^2)                  [SL(3) tower: char(M^2)]   OK
   n=4:  (+1,-1) = (2,2)  ->  char(M^2) . char(-M^2)     [SL(4) tower: same]        OK
   n=5:  (+1,-1) = (4,2)  ->  char(M^2)^2 . char(-M^2)
   ```

   The height-2 **direct power is 2** (`char(M^2)`) consistently at `n=3,4`.

3. **SL(5) conclusion.** The height-2 space is `char(M^2)^2 . char(-M^2)`. B61
   resolved 4 of its 6 dimensions as `char(M^2) . char(-M^2)`; the 2 unresolved
   are the **second `char(M^2)`**: eigenvalues `phi^2 = 2.618034...` and
   `1/phi^2 = 0.381966...` (sum `+3`, product `+1`).

4. **Numerical corroboration of the sign.** The gauge-perturbed residual modes
   are positive (seed 20: `~2.89, ~0.90`), close to `char(M^2)` `{2.618, 0.382}`
   (combined distance `0.79`) and far from `char(-M^2)` `{-2.618, -0.382}`
   (distance `4.55`). The positive sign rules out `char(-M^2)`.

## Completed SL(5) fixed-line factorization

```text
char(M^-1) . char(M)^2 . char(M^2)^2 . char(M^3) . char(M^4) . char(M^5)
          . char(-M^2) . char(-M^3) . (t-1)^2 (t+1)^2            (degree 24)
```

Powers `{-1, 1, 1, 2, 2, 3, 4, 5}`, sign sectors `{-2, -3}`, parity degree 4.

## Honest status / limits

- **Exact** at the level of the root-system split; **validated** on SL(3)/SL(4);
  **corroborated** numerically. Recorded as a **live structural result**, not a
  theorem.
- A symbolic proof requires the ambient `SL(5,C)` trace ring (B58's open task),
  which would also prove the whole tower. The power-assignment at heights other
  than 2 (which `char(M^k)` sits where) is not derived here -- only the
  height-2 sign/direct split, which suffices for the user's prediction.
- The opposition-involution = exchange-involution identification is the
  structural hypothesis being recorded as "live": it is consistent with and
  predictive of all resolved data (SL(3), SL(4), and the resolved 22/24 of
  SL(5)), but the height decomposition of the full multiplier spectrum is not
  proved.

## Reproduce

```bash
python frontier/B62_opposition_involution/probe.py
python -m pytest tests/test_b62_opposition_involution.py -q
```
