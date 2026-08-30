# R031 — the normalized toric trace has minimum support four

## Verdict

R027's cyclic eight-triangle trace is convenient for symmetry, but it is not
the smallest representative of the normalized dual class.  Exhaustion of the
twenty eligible triangles on the six-chart `dP6` cover gives the exact minimum

```text
(1/4) * [012 + 023 + 034 + 045].
```

No normalized dual trace exists on one, two or three triangles.  The sparse
trace is homologous to R027's cyclic trace and has the same pairing with the
marked top cocycle.  Its Eilenberg--Zilber product on `dP6 x dP6` has 96
nonzero four-simplices rather than 384.  The pending height-308 residue
contraction is therefore four times smaller without changing its value.

This is a chain-representative optimization, not a Yukawa result.  It does not
construct the connecting cochain, evaluate an entry or select a Higgs line.

## Exact factor calculation

R027's canonical-weight complex has twenty degree-two basis triangles.  A
dual trace vector `t` must satisfy

```text
t^T delta_1 = 0,        <t,tau> = 1.
```

The certificate solves these rational linear systems for every support of
size one through four.  It rejects respectively

```text
C(20,1)=20, C(20,2)=190, C(20,3)=1140
```

supports before the displayed four-triangle solution appears.  Thus support
four is minimal, not merely the first representative found by a heuristic.
The trace annihilates every degree-one coboundary and pairs with R027's
all-ones cocycle `tau` as one.

The difference between this trace and R027's cyclic eight-triangle trace is
solved explicitly in `im(delta_2^T)`.  Hence the two are the same normalized
dual homology class.  Deleting one of the four triangles is retained as a
negative control and breaks the cycle equations or the normalization.

## Product trace

Taking the signed six-shuffle cross product of the four supported triangles
in each factor gives

```text
4 * 4 * 6 = 96
```

nonzero product four-simplices.  The certificate checks the product boundary
is zero in R027's canonical-weight subcomplex and its Alexander--Whitney
pairing with `tau x tau` is exactly one.  Because the factor traces are
homologous and the shuffle cross product is a chain map, this is the same
functional as R027's 384-simplex product trace.

## Computational consequence

The direct R030/R026 contraction now needs only the five faces of these 96
four-simplices.  The cover-specific part can be computed once as a universal
trace kernel and reused for all eighteen entries.  What remains load-bearing
is still the full common-frame determinant factor from the frozen `A_7`,
`B_6` and `B_2` representatives and a characteristic-zero/base-change
argument for any nonzero modular row.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  certificates/r031_sparse_toric_trace/sparse_toric_trace.py
```

The certificate uses only Python 3 and R027 through file-relative paths.
