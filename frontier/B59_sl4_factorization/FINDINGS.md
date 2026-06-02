# B59 Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Verdict

```text
RESOLVED (numerical): the SL(4) tower prediction is REFUTED in specifics;
the actual fixed-line factorization is determined.
```

This resolves the `NEEDS-EXPERTISE` that B58 recorded -- numerically, with the
method validated against SL(3) ground truth.

## The Result

The SL(4) Fibonacci fixed-line Jacobian (15x15) has spectrum factoring as

```text
char(M^-1) . char(M) . char(M^2) . char(M^3) . char(M^4) . char(-M^2) . (t-1)^2 (t+1)
```

- **5 clean `char(M^k)`**, powers `k = -1, 1, 2, 3, 4`. The powers climb beyond
  SL(3)'s `{-1, 2, 3}` (now including `M^4`), so part of the tower intuition is
  right: higher rank reaches higher `M`-powers.
- **1 sign sector `char(-M^2) = t^2 + 3t + 1`** (eigenvalues `-phi^2, -phi^-2`).
  This has **no SL(3) analog** -- a genuinely new feature at SL(4).
- **a degree-3 parity block `(t-1)^2 (t+1)`** (eigenvalues `1, 1, -1`), not the
  predicted degree-1 parity.

## Why The Prediction Is Refuted

The PC12 "Open Prediction" stated: parity block + `(n^2-1-parity)/2` degree-2
`char(M^k)` factors, i.e. for `n=4`: 1 + 7 char(M^k). The computation shows:

```text
predicted:  1 (parity)  + 7 char(M^k)                         = 15
actual:     3 (parity)  + 5 char(M^k) + 2 (char(-M^2))        = 15
```

The count of `char(M^k)` is 5, not 7; a sign sector appears; the parity block is
degree 3. The clean `(n^2-1-parity)/2` formula does not hold.

## Method And Status

Computed by extrapolating the ambient Jacobian
`DT(eps) = D[tr W_i(AB,A)] . pinv(D[tr W_j(A,B)])` to `eps=0` along
`A=exp(eps P), B=exp(eps Q)`. The same procedure reproduces B55's SL(3) `c=3`
spectrum to ~4 digits (`max match 0.0000`), which is the credibility anchor;
the SL(4) spectrum matches the factorization above to `max match 0.0101`.

This is **numerical (~3-4 digits), method-validated -- not a symbolic proof.**
A symbolic confirmation needs the ambient SL(4,C) trace ring (B58's open task);
B59 fixes the target that build must reproduce. No physics, no Origin-core claim.
