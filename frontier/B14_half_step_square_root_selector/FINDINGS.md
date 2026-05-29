# B14 -- Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` section 5).

## Exact Algebra

For the selected core

```text
A = LR = [[2,1],[1,1]],
```

the record swap

```text
P = [[0,1],[1,0]]
```

conjugates `L` to `R`, and

```text
F = L P = [[1,1],[1,0]]
F^2 = A.
```

The square root is unique up to sign inside `GL(2,Z)`: if `X^2=A`, then
`X=F` or `X=-F`.

The proof is short. Any integer square root `X` has eigenvalues square-rooting
the eigenvalues of `A`, so `det(X)=-1` and `tr(X)=+/-1`; the `det=+1` square-root
choices would have non-integer trace `+/-sqrt(5)`. Cayley-Hamilton gives

```text
X^2 - tr(X) X - I = 0,
```

so `A = X^2 = tr(X) X + I`, hence

```text
X = tr(X)(A-I).
```

This yields exactly `F` and `-F`.

## General Mixed Closures

For

```text
B(a,b)=L_a R_b = [[1+ab,a],[b,1]],
```

the same argument gives `tr(X)^2=ab` for an orientation-reversing square root.
Writing `s=sqrt(ab)`, the only possible root is

```text
X = (B(a,b)-I)/s = [[s, a/s], [b/s, 0]].
```

For positive integers, integrality forces `a=b=s`. Therefore

```text
B(a,b) has an integer orientation-reversing square root
iff a=b.
```

In that case,

```text
B(k,k) = (L_k P)^2.
```

So the half-step requirement is a symmetry selector: it selects balanced
closures. Combined with the existing torsion-free/minimality selection
`ab=1`, it gives `k=1` and hence `F`.

## What This Changes

B13's trace-map result should not be read as "the direct monodromy contains
itself." The more precise structure is:

```text
two-record swap symmetry P
    -> primitive half-step F = L P
    -> F^2 = A
    -> symmetric-square trace lift of F contains the A-sector
```

That is mathematically cleaner and less inflated.

## Verdict

**`STALLED`**

The half-step is forced once the record-swap `P` is admitted as a symmetry of the
two-record substrate. But whether `P` is part of the allowed pre-dynamical
structure or an inserted operation is not derived here.
