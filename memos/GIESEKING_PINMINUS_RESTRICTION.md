# R021 — Gieseking Pin-minus restriction

## Narrow theorem

Let `N = m000` be the nonorientable Gieseking manifold and let
`p: M = m004 -> N` be its orientable double cover. Under the convention that a
Riemannian Pin-minus structure has obstruction `w2(TN) + w1(TN)^2`, `N` has exactly two
Pin-minus structures and `M` has exactly two spin structures. Both Pin-minus structures restrict
to the same, deliberately unnamed, spin structure on `M`.

The standalone standard-library certificate is
`certificates/r021_gieseking_pinminus/gieseking_pinminus_restriction.py`. It has no repository or
working-directory dependency. Its captured output is `outputs/r021_gieseking_pinminus.txt`.

## Exact derivation

For the checked extension presentation, abelianization gives

```text
H1(M; Z) = Z<a=b>
H1(N; Z) = Z<t>, with a=b=2t.
```

The relation matrix for `N`, on `(a,b,t)`, is

```text
[1 -1  0]
[1  0 -2].
```

It has rank two and its `(a,b)` minor is one, so its Smith form is `diag(1,1)`: there
is one free class and no torsion. Thus both `H^1(N; F2)` and `H^1(M; F2)` are `F2`.

A compact core of `N` is a once-punctured-torus mapping torus, so `chi(N)=0`. Its boundary is
nonempty, hence `b3=0`; with `b0=b1=1`, Euler characteristic gives `b2=0` and therefore
`H^2(N; F2)=0`. The Pin-minus obstruction vanishes. This also agrees with the general
three-manifold Wu-class identity in the stated convention.

Let `u(t)=1` generate `H^1(N; F2)`. The cover inclusion sends `a` and `b` to `2t`, so

```text
p^*u(a) = p^*u(b) = u(2t) = 0.
```

Therefore `p^*=0`. Pin-minus and spin structures are affine torsors over these cohomology groups.
For any Pin-minus basepoint `P`, set `s=res(P)`. Then

```text
res(P) = s
res(P+u) = s.
```

The image consists of one spin structure; the other spin structure is not the restriction of a
Pin-minus structure on `N`.

## Non-identification fence

This theorem intentionally does not identify `s` with a separately named sign lift used in B1141.
The affine calculation fixes differences, not the origin of the spin torsor. Naming the image
requires an explicit Riemannian tangent-frame `Pin^-(3)` lift and a comparison of its restricted
`Spin(3)` lift with the two named hyperbolic-holonomy lifts.

Four objects remain distinct:

- a tangent Pin-minus structure lifts the `O(3)` tangent-frame bundle;
- `t` is a representative in the Gieseking fundamental-group/deck extension, not the central
  kernel of a Pin bundle;
- the central sign in an internal `2T` representation is internal finite-representation data;
- a semilinear holonomy matrix is extended holonomy data, not by itself a tangent Pin certificate.

## Residual and falsifier

The only residual is the named-image comparison. An explicit frame-lift certificate restricting to
the opposite named holonomy lift would falsify any claim that the theorem selects the B1141 label;
it would not alter the counts or the zero linear restriction map. A nonzero `p^*`, a nonzero
Pin-minus obstruction or a different mod-two torsor rank would falsify the narrow theorem.

Primary source trail: outside-campaign A4 at `0fe97f9070384d9a5a98c625b1b70131de2556f1`
and its later arithmetic certificate `outside_bench/certificates/a4_pin.py` at
`fd91324c2c3d0c840540c9d0368654686b846f30`. R021 adds the missing obstruction and affine-scope
derivation without inheriting the source's named-spin conclusion.
