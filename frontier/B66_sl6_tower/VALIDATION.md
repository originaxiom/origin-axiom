# B66 validation -- stress-testing mult(|k|=3) = 2 for SL(6)

Post-merge validation of the B66 key result (the |k|=3 multiplicity is **2**, so
`max(n-d,1)=3` is refuted). Four independent checks. Numerical, high-precision;
not a symbolic proof. Scripts: `validate.py` (Task 1), `second_m.py` (Task 3),
`gauge.py` (Tasks 4+2).

## Summary

**mult(|k|=3) = 2 is robust across every axis we varied** -- two word sets, two
base-point seeds, three values of `m`, and the method exactly recovers the known
SL(3)/SL(4)/SL(5) tower (SL(3),(4) are proven over `Z[m]` in B63/B65). The one
thing that is *not* available is a fully exact rational matrix (Task 2): the
rep-perturbation Jacobian is intrinsically gauge-dependent at the singular fixed
point, so the canonical exact route remains the ambient `SL(6,C)` trace ring (B58).

## Task 1 -- the identical pipeline on SL(3..6)

The same pipeline (automatic QR-pivot inverse-word selection -> `DT(eps)=DX.pinv(Dx)`
high-precision extrapolation -> Dickson identification), run per `n`:

```text
n   dim   words (len)   mult(|k|=3)   expected
3    8     8  (<=4)          1            1     OK
4   15    15  (<=4)          1            1     OK
5   24    24  (<=4)          2            2     OK   <- load-bearing
6   35    35  (<=5)          2            2     OK
```

SL(5)=2 is recovered under the **same** gauge-handling that SL(6) uses -- so the
SL(6) result is not an artifact of the method silently failing on hard cases. The
words here are **auto-selected** (a different set than the hardcoded `SL6_WORDS` of
the original B66 run), so SL(6)=2 also survives a word-set change.

## Task 3 -- a second and third `m` (breaks any m=1 root coincidence)

Same word set, substitution `phi_m(a)=a^m b`, catalog `char(M^3)=t^2-L_3(m)t-1`.
The isolated big root tracks `L_3(m)` and the count stays 2:

```text
m=1:  char(M^3) big root  4.236   (L_3=4)    mult(|k|=3) = 2   [B66]
m=2:  char(M^3) big root 14.071   (L_3=14)   mult(|k|=3) = 2   (char(M^3) x1, char(-M^3) x1)
m=3:  char(M^3) big root 36.028   (L_3=36)   mult(|k|=3) = 2   (char(M^3) x1, char(-M^3) x1)
```

(`14.0710678 = 7+sqrt(50)`, `36.0277564 = 18+sqrt(327)` -- exactly the metallic
`char(M^3)` roots.) The |k|=3 multiplicity is an `m`-independent 2, not a golden-
ratio accident.

## Task 4 -- the gauge subspace

The fixed-line rank-loss makes the `eps->0` pinv limit gauge-dependent in ~8-9
directions (B62). The principled, non-circular test of "gauge" is base-point
dependence: compute the 35x35 Jacobian at seed 20 and seed 24.

**(a) The |k|=3 eigenvalues are seed-STABLE** -- they sit on the catalog roots at
both base points:

```text
root          seed 20          seed 24          |diff|
+4.236068     +4.23606829      +4.23606797      3.2e-07
-4.236068     -4.23604330      -4.23606707      2.4e-05
+0.236068     +0.23624690      +0.23606131      1.9e-04
-0.236068     -0.23606735      -0.23606798      6.3e-07
```

**(b) The 8 gauge modes are seed-UNSTABLE** -- they scatter wildly (one moves
`21.1 -> 17.3`; several go complex<->real):

```text
+21.115 -> 17.334  (diff 3.8)     1.463+-0.853j -> 1.618  (diff 0.87)
 -2.939 -> -2.618  (diff 0.32)   -0.747+-0.564j -> -0.618 (diff 0.58)
 +2.411 -> +2.618  (diff 0.21)    +0.326 -> +0.272        (diff 0.05)
```

So |k|=3 modes are ~10^3-10^5 times less base-point-sensitive than gauge modes.

**(c) Condition numbers** `kappa = ||v_i|| ||w_i||` (basis-independent sensitivity):
the |k|=3 modes are well-conditioned (`kappa in [15, 108]`), the gauge modes reach
`kappa ~ 4.8e3`. (Honest caveat: `kappa` alone does not perfectly separate -- a few
catalog modes also reach `kappa ~ 5e3` -- so seed-stability in (a)/(b) is the
decisive discriminator, with `kappa` corroborating.)

**(d) mult(|k|=3) on the clean (27-dim catalog) complement = 2.**

## Task 2 -- exact arithmetic over Q (the honest negative)

Forming an exact rational 35x35 matrix would remove the conditioning ambiguity
*if such a canonical matrix existed*. It does not: the numerical Jacobian is
strongly base-point dependent,

```text
||dt0(seed 20) - dt0(seed 24)||_max = 7.3e3      (only 245/1225 entries seed-stable to 1e-6)
```

The pinv amplifies floating-point error without bound in the ~8 gauge directions,
so there is no single rational matrix to reconstruct (unlike SL(4), which is
gauge-clean and *was* reconstructed exactly over `Z[m]` in B65). The intrinsic
character-variety Jacobian *is* canonical, but computing it exactly is the ambient
`SL(6,C)` Procesi trace ring -- B58, still open. So:

- **Exact over Q is not achievable for n=6 by this method** (the gauge degeneracy
  is intrinsic, not a precision artifact).
- The |k|=3 eigenvalues are nonetheless the **seed-stable, well-conditioned**
  content (Task 4a), and the method is **calibrated against the exactly-proven
  SL(3)/SL(4)** cases (Task 1), so the numerical mult(|k|=3) = 2 stands on strong
  evidence even though a from-first-principles proof for n>=5 awaits B58.

## Verdict

mult(|k|=3) = 2 for SL(6) (2 word sets x 2 seeds x 3 `m` values, plus exact
SL(3)/SL(4)/SL(5) recovery). `max(n-d,1)=3` is refuted. A fully exact proof needs
the trace ring (B58).
