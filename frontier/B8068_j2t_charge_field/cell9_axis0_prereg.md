# AXIS 0 PREREGISTRATION — the field over which the pure spinors live

**Sealed 2026-08-17, committed BEFORE the run.** Rule 1 of the loop: the session's
docstring-only seals are why several results needed re-litigating.

## THE DEFECT BEING REPAIRED

`cell8_density.py` carries `except Exception: pass`. Primes where the pipeline failed were
silently dropped. In 36 reported primes `#roots(mu) in {1,3}` and **never 0** — impossible for
an `S3` cubic, where 0 roots has density 1/3. So the sample is almost certainly biased: primes
with no root give no idempotents, no `so(10)`, and were dropped without a trace.

## DECLARED BEFORE COMPUTE

Let `N` = all primes tested, `S` = skipped, `R` = reported, `X` = split (2 pure points).

1. **The skip count must be reported.** If `|S|/|N|` is near 1/3 and the skipped primes are
   exactly those with `#roots(mu) = 0`, the bias is confirmed and the earlier density is
   conditional, not absolute.
2. **The conditional density prediction.** If the pure spinors exist exactly when `mu` splits
   completely, then among primes with at least one root the density is
   `(1/6)/(1/6 + 1/2) = 1/4 = 0.250`. Observed was `0.222`.
3. **The predicate test.** `X` must equal `{p : #roots(mu) = 3}` with **zero** misses and
   **zero** extras, over the full unbiased sample.

## THE TWO OUTCOMES, both live

- **CONFIRMED** -> the pure spinors are defined over the **splitting field of the object's own
  charge cubic**. Since `disc K = 6237 > 0` and `K` is totally real, that field is **totally
  real**, so the pure spinors are **real** and `SO(10) -> SU(5)` closes over R.
- **REFUTED** -> the predicate fails somewhere; the field is something else and gets identified
  from scratch, with density measured before any name is attached.

## WHAT WOULD MAKE THIS A FALSE POSITIVE

The near-miss earlier in this session named `Q(sqrt 77)` from **one** split prime. `77` and
`6237` are the same square class, so that was one coincidence printed twice. **A predicate that
matches on a biased sample proves nothing.** Only the unbiased sweep counts.

## INDEPENDENT CROSS-CHECK, required before the result is claimed

Splitting statistics alone are not proof. The pure-spinor quadric must also be computed
**exactly** over `Q(sqrt-3, theta)` and factored. The two methods must agree, or neither is
reported.
