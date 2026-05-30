# B39 -- Findings

> Logged observation, not a claim.

## Result

The tangent return quadratic can be represented by a companion matrix:

```text
M_mu = [[0,-1],[1,mu]]
```

This preserves the standard integer lattice only when `mu` is integer.

Since:

```text
mu = 4c^2 - 2
```

integrality restricts `c^2` to:

```text
c^2 = (m+2)/4,  m in Z
```

There is an infinite discrete family. The projective quotient alone does not
choose `m=3`; minimality or torsion-one closure must still be added.

## Verdict

**`STALLED`**

No canonical tangent lattice is derived from the quotient alone.
