# B8068 AXIS 0 — the field of the pure spinors

**Date:** 2026-08-17 · **Seat:** cc3 · **Prereg:** `cell9_axis0_prereg.md`, committed
`de8a055b` **before** compute. **Gate 5:** algebra only.

## THE RESULT

> **Pure spinors exist on the ω-line if and only if μ = x³ − 12x − 5 splits completely.**

- **forward** (μ splits ⟹ pure spinors): **30 primes tested, 30 confirmed, 0
  counterexamples, 0 no-answer** — every prime `≡ 1 mod 3` up to 4000 at which μ splits.
- **reverse** (pure spinors ⟹ μ splits): **zero misses, zero extras** on the unbiased
  sample.
- 56 primes, perfect agreement.

Therefore the pure spinors are defined over the **splitting field of the object's own
charge cubic**, `L = K(√77)`. `K` is totally real and `77 > 0`, so **`L` is totally
real** — the pure spinors are **real**, and `SO(10) → SU(5)` closes over ℝ.

## THE PREREGISTERED BIAS CHECK — CONFIRMED

`cell8_density.py` carried `except Exception: pass`. The prereg predicted the dropped
primes would be exactly the `#roots(μ) = 0` ones. **They were** — `was the drop exactly
the 0-root primes? True`, 12 of 38.

Root-count distribution over the unbiased sample, against `S₃` predictions:

| #roots(μ) | observed | S₃ predicts |
|---|---|---|
| 0 | 0.316 | 1/3 |
| 1 | 0.553 | 1/2 |
| 3 | 0.132 | 1/6 |

Conditional split density `5/26 = 0.192` against the prereg's predicted `0.250` — within
noise at 5 splits.

## WHAT THE BIAS HAD HIDDEN, and why it matters

On the **biased** sample, "μ splits completely" and "77 is a QR" were the same predicate,
and an earlier pass named `ℚ(√77)` from **one** split prime. With the 0-root primes
restored the two predicates come apart: by `S₃`, `L(disc) = +1` iff Frobenius is *even*,
which is **3 roots or 0 roots**. The agreement was an artefact of exactly the class that
had been deleted.

**A limitation stated rather than managed.** On the *answerable* set the two predicates
still coincide — answerable means `≥1` root, and with `≥1` root, 3 roots ⟺ 77 is a QR.
The only primes that separate them are the 0-root primes, and those are precisely where
no `so(10)` exists. **The distinguishing case is unanswerable by construction**, so this
sweep cannot separate the two readings.

It does not matter for the conclusion: both readings give a field inside `L = K(√77)`,
and `L` is totally real either way. The reality of the pure spinors is robust to the
ambiguity.

## STILL OWED

The prereg requires an **exact** cross-check — the pure-spinor quadric computed over
`ℚ(√−3, θ)` and factored — agreeing with the splitting statistics. **Not done.** Until
it is, this is strong evidence (56 primes, perfect agreement) and not proof.

## RUN

```
python3 cell10_unbiased.py 200 700    # full accounting, no silent skips
python3 cell13_forward.py             # forward direction, every splitting prime to 4000
```
