# B59 -- SL(4) Fixed-Line Factorization (numerical; resolves B58)

## Question

Test the SL(n) factor-count tower prediction (PC12 "Open Prediction") at `n=4`,
which B58 left as `NEEDS-EXPERTISE`. Predicted: parity block + **7** degree-2
`char(M^k)` factors.

## Status

```text
FRONTIER EVIDENCE (numerical, method-validated)
PC12 SUPPORT
NO CLAIM PROMOTION
```

## Run

```bash
python frontier/B59_sl4_factorization/probe.py
```

## Method (and why it works where B58's shortcut failed)

The ambient fixed-line Jacobian is the linearization of the polynomial trace map
at the all-traces-`n` point. B58 showed it cannot be read off representations
*at* the identity (traces are second-order there). **But at a perturbed
representation** `A=exp(eps P)`, `B=exp(eps Q)` the trace-coordinate differential
is full rank, so

```text
DT(eps) = D[tr W_i(AB,A)] . pinv( D[tr W_j(A,B)] )
```

is the ambient Jacobian at the point `x(eps)`, and `x(eps) -> (n,...,n)` as
`eps -> 0`. Extrapolating `DT(eps)` to `eps=0` gives the fixed-line Jacobian.

**Built-in validation:** on SL(3) (8 coordinates) this reproduces B55's `c=3`
spectrum to ~4 digits (`max match 0.0000`). That ground-truth check is the
credibility anchor for the SL(4) result.

## Result (SL(4), 15 coordinates; numerical ~3 digits)

The fixed-line spectrum factors as

```text
char(M^-1) . char(M) . char(M^2) . char(M^3) . char(M^4) . char(-M^2) . (t-1)^2 (t+1)
```

(max match `0.0101` to this product). That is:

```text
5 clean char(M^k), powers k = -1, 1, 2, 3, 4   (SL(3) had k = -1, 2, 3)
1 sign sector char(-M^2) = t^2+3t+1  (eigenvalues -phi^2, -phi^-2; new at SL(4))
a degree-3 parity block (t-1)^2 (t+1)  (eigenvalues 1, 1, -1)
```

## Verdict

The naive tower prediction (`7 char(M^k) + 1 parity eigenvalue`) is **REFUTED**.
The actual structure is richer: only **5** clean `char(M^k)` (the powers do
climb, now to 4), plus a **sign sector** `char(-M^2)` with no SL(3) analog, plus
a **degree-3** parity block (not degree 1). The `(n^2-1-parity)/2` factor-count
formula does not hold.

This is numerical (~3-4 digits), method-validated against SL(3) ground truth --
**not a symbolic proof.** A symbolic confirmation would require the ambient
SL(4,C) trace ring (B58); B59 determines the answer the symbolic build would have
to reproduce. Standalone trace-map mathematics; no physics, no claim promoted.
