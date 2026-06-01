# B51 Findings

## Verdict

```text
PRODUCES-PROOF-MODULE
```

The `c=3` fixed-line factorization is not merely a bounded certificate. With
`m` kept symbolic, the Jacobian commutes with the record-exchange involution and
block diagonalizes into two four-dimensional sectors.

## Exact Result

At `c=3`, the Cayley-Hamilton recurrence

```text
tau_k = 3 tau_{k-1} - 3 tau_{k-2} + tau_{k-3}
```

has characteristic equation `(r-1)^3=0`. The derivative sequences are therefore
polynomials in `k`:

```text
d tau_k / d x1 = k(k^2-1)/2
d tau_k / d x2 = 1-k^2
d tau_k / d x3 = k(k+1)/2
d tau_k / d x4 = -k(k^2-1)/2
d tau_k / d x6 = k(k-1)/2
```

The `sigma` derivatives are obtained by the exchange
`x1<->x4`, `x2<->x5`, `x3<->x8`, `x6<->x7`.

For the resulting symbolic `8x8` Jacobian `J(m)`, the exchange involution
commutes with `J(m)`. In the symmetric/antisymmetric basis the off-diagonal
blocks vanish and the characteristic polynomials are:

```text
symmetric:     (t-1)(t+1)(t^2-(m^2+2)t+1)
antisymmetric: (t^2+mt-1)(t^2-(m^3+3m)t-1)
```

SymPy verifies both polynomial identities by expanding the symbolic difference
to zero.

## Impact On PC12

This upgrades Theorem 1/Theorem 4 proof status for the `c=3` fixed line:
case-by-case checks become a reusable formal proof module. It does not resolve
the remaining global splitting-classification prose tasks for `c>=15` and
`c<=-12`.
