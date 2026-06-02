# B57 Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Verdict

```text
PRODUCES-PROOF-MODULE
```

The integer splitting of the antisymmetric fixed-line quartic is classified for
`m = 1..6`, extending B51's `c=3` Diophantine observation to the metallic family.

## Exact Results

The antisymmetric quartic is `chi(t) = t^4 - A(m,c) t^3 + C(m,c) t^2 + A(m,c) t + 1`,
splitting over `Z` as `(t^2 - alpha t - 1)(t^2 - beta t - 1)` iff
`D = A^2 - 4(C+2)` is a perfect square with `A + sqrt(D)` even. Scanning
`c in [-120, 120]`:

```text
m=1: {-11, -9, 1, 3}
m=2: {-3, -1, 1, 3}
m=3: {-3, 0, 1, 3}
m=4: {-1, 1, 3}
m=5: {1, 3}
m=6: {-1, 0, 1, 2, 3}
```

- **Universal:** `c = 1` and `c = 3` split for every `m` (at `c=1` the quartic is
  `(t^2 - 1)(t^2 - m t - 1)`; at `c=3` it is the B51 factorization
  `(t^2 + m t - 1)(t^2 - (m^3 + 3m) t - 1)`).
- **m-dependent extras**, count `[4, 4, 4, 3, 2, 5]` -- varies.

## Killed Speculation

The apparent match between the class number `h(Q(sqrt-15)) = 2` and the two
non-negative splitting points of `m=1` is a **coincidence**. For `m >= 2` the
splitting counts do not track any class number (counts vary 2..5). Recorded as a
negative result; no number-field connection is claimed.

## Impact On PC12

B57 turns PC12's Theorem-4 content (the one part the literature screen flagged as
apparently-new and elementary) from a `c=3`, `m=1` observation into a classified
family across `m`. It remains elementary Diophantine arithmetic -- standalone
trace-map mathematics, no selector, no physics, no new claim.
