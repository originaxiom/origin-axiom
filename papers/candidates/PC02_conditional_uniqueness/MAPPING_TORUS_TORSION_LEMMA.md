# Mapping-Torus Torsion Lemma

Status: paper-support lemma for PC02. This does not change C1's status.

## Statement

Let `B` be an integer `2 x 2` matrix with determinant `1`, and let `M_B` be the
mapping torus of the torus homeomorphism induced by `B`:

```text
M_B = T^2 x [0,1] / (x,1) ~ (B x,0).
```

Then:

```text
H1(M_B; Z) = Z plus coker(B - I).
```

If `det(B - I) != 0`, then `coker(B - I)` is finite and has order:

```text
|det(B - I)|.
```

For the mixed closure

```text
B(a,b) = L_a R_b = [[1+ab,a],[b,1]],
```

we have:

```text
det(B(a,b) - I) = -ab,
```

so the torsion order of `H1(M_B; Z)` is `ab` whenever `ab != 0`. Over positive
integers, torsion-free closure therefore forces:

```text
ab = 1,
a = b = 1.
```

## Proof

Use the Wang exact sequence for the fibration:

```text
T^2 -> M_B -> S^1.
```

The relevant low-degree part is:

```text
H1(T^2) --(B_* - I)--> H1(T^2) -> H1(M_B)
  -> H0(T^2) --(B_* - I)--> H0(T^2).
```

Because `T^2` is connected, `H0(T^2; Z) = Z`, and the induced map on `H0` is the
identity. Hence the last map is zero:

```text
B_* - I = 0 on H0(T^2).
```

Exactness gives the short exact sequence:

```text
0 -> coker(B_* - I) -> H1(M_B; Z) -> Z -> 0.
```

Since `Z` is free, this short exact sequence splits. Therefore:

```text
H1(M_B; Z) = Z plus coker(B_* - I).
```

With the column-vector convention used in the project, `B_*` is represented by
`B`, so this is `Z plus coker(B - I)`. With the opposite row-vector convention,
the matrix is `B^T`; the Smith normal forms of a matrix and its transpose are
the same, so the torsion order statement is unchanged.

Now assume `det(B - I) != 0`. Then `B - I` has full rank over `Q`, so
`coker(B - I)` is finite. For a full-rank integer `2 x 2` matrix `A`, the order
of `coker(A)` is `|det A|`; equivalently, this is the product of the diagonal
entries in the Smith normal form of `A`.

Thus:

```text
|torsion H1(M_B; Z)| = |det(B - I)|.
```

For the mixed closure:

```text
B(a,b) - I = [[ab,a],[b,0]],
```

so:

```text
det(B(a,b) - I) = (ab)(0) - ab = -ab.
```

Therefore:

```text
|torsion H1(M_B; Z)| = ab.
```

If `a,b` are positive integers, `ab = 1` if and only if `a = b = 1`. Hence the
torsion-free closure condition selects:

```text
B(1,1) = L R = [[2,1],[1,1]].
```

## Role In PC02

This lemma supplies the paper-grade topology step used by
`docs/UNIQUENESS_THEOREM.md`. It does not prove the axioms A1-A7. It proves only
that, once the mixed closure `B(a,b)` and torsion-free closure condition are
accepted, the torsion filter forces `ab = 1`.

## Review Notes

A reviewer should check:

```text
the Wang sequence is the right convention for this mapping torus
the `B` versus `B^T` convention is harmless for torsion order
the split by `Z` is stated correctly
the use of Smith normal form for the torsion order is standard
the punctured-torus versus torus-bundle language does not alter this lemma's use
```
