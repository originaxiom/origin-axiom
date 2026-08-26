# R006 — exact E6/27 invariant census and beat covariance

## Claim

For the locked algebraic 27 of E6:

```text
dim Sym^d(27*)^E6 for d=1,2,3,4 = 0,0,1,0
dim (27 tensor 27 tensor 27)^E6 = 1
selected A2^3 ordered / symmetric trilinear dimensions = 9 / 4
```

The unique symmetric cubic is rational in the locked crystal basis, has 45 nonzero normalized
coefficients, is killed by all 72 root generators, and obeys

```text
C(Omega u, Omega v, Omega w) = gal(C(u,v,w))
```

for the specifically fixed linearization `Omega=exp(q rho(E)) o gal`.

## Independent computation

`tensor_invariant_counts.py` is a new exact computation over `fractions.Fraction`.  It constructs
the full 270-element weight-zero ordered basis and computes sparse rational ranks:

```text
full E6: rank 269 -> one ordered invariant
selected A2^3: rank 261 -> nine ordered invariants
selected A2^3 symmetric: rank 41 on 45 -> four invariants
```

The degree-one, degree-two and degree-four symmetric weight-zero bases are empty; degree three has
45 monomials and exact rank 44.

`jordan_beat.py` is the independently authored outside-bench computation, vendored with the exact
locked E6 sources it consumes.  It supplies the full cubic coefficients and semilinear covariance
cross-check.  Both certificates run from any current directory with Python 3 and SymPy; every file
lookup is relative to `__file__`.

## Provenance

| file | SHA-256 |
|---|---|
| `jordan_beat.py` | `c11315c7678f15e4635a8e9a96be717d9d2b684a725ea32975f0f613cffd4cdd` |
| `tensor_invariant_counts.py` | `e5ec514e1a47afd8204b7591c1feaaa62f1d7e9bc64a0efa716a1991d3e49334` |
| `twisted_double.py` | `4a0fb415c7681e052681ab4c1a703d666751776d8fb883edf5ccda44a5cfeba6` |
| `paper/verify/check_charge_bracket.py` | `5facb27879bd0ea76c7378f6432867be9019a9e6a4ba796e34040d31bb51f9f2` |

The vendored `jordan_beat.py` is blob `d8b9b7c1122cbaf367774a6cf5f45b093d6b43a6` from outside commit
`51e8920bc355c40589628ea7a36a4eb1c5cb352b`.  The two locked support files come from Golden commit
`15b3366937af19e643a54d564883253f013fc651`.  The vendored charge-bracket file differs from its
upstream SHA `4f10df9f55bd58bfb814f8b4428ff55bc710d4e49713876797b5c35f5990455f` only by removal of one
trailing space so the repository whitespace gate remains clean.

## Fence

This is finite-dimensional representation theory.  It gives invariant multiplicities and a
coupling-shaped tensor, not a compactification, zero-mode cup product, physical Yukawa value,
fermion mass or mixing angle.

The covariance scalar is also not invariant under an unfixed phase of the semilinear lift:
`Omega -> lambda Omega` sends the cubic scalar to `lambda^3` times its old value.  The printed
scalar one is exact only for the named locked linearization.
