# B57 -- General-m Diophantine Splitting Classification

## Question

B51 recorded that the `c=3` antisymmetric quartic splits over `Z` (the lone
`APPARENTLY_NEW` block of the PC12 literature screen). For the metallic family,
at which integer `c` does the antisymmetric fixed-line quartic split into two
integer quadratics, as `m` varies?

## Status

```text
FRONTIER EVIDENCE
PC12 SUPPORT
NO CLAIM PROMOTION
```

## Run

```bash
python frontier/B57_general_m_splitting/probe.py
```

## What It Checks

The antisymmetric quartic has the form

```text
chi(t) = t^4 - A(m,c) t^3 + C(m,c) t^2 + A(m,c) t + 1,
```

and splits over `Z` as `(t^2 - alpha t - 1)(t^2 - beta t - 1)` with integer
`alpha, beta` iff `D = A^2 - 4(C+2)` is a perfect square and `A + sqrt(D)` is
even. Scanning `c` in `-120..120`:

```text
m=1: c in {-11, -9, 1, 3}
m=2: c in {-3, -1, 1, 3}
m=3: c in {-3, 0, 1, 3}
m=4: c in {-1, 1, 3}
m=5: c in {1, 3}
m=6: c in {-1, 0, 1, 2, 3}
```

- `c = 1` and `c = 3` are **universal** splitting points (every `m`).
- The extra points are `m`-dependent; the count is `[4, 4, 4, 3, 2, 5]` for
  `m = 1..6` -- it varies, with **no class-number law**.

## Killed Speculation

The earlier observation that `Q(sqrt-15)` has class number `2` and `m=1` has two
non-negative splitting points `{1, 3}` is a **coincidence**: for `m >= 2` the
splitting counts do not track any class number. Recorded here as a negative
result, not a connection.
