# R027 — the marked toric top trace for the height-308 evaluator

## Verdict

The ambient trace component of the norm-308 down/lepton Yukawa evaluator is
now explicit. On the source-locked six-cone cover of `dP6`, R027 constructs a
marked generator of

```text
H^2(dP6,K_dP6) = Q
```

and a normalized dual Cech cycle. Its Eilenberg--Zilber cross product is a
384-simplex cycle on the 36-chart cover of `Z=dP6 x dP6`; it evaluates
`H^4(Z,K_Z)` directly and pairs with the marked product generator as one.

This is the trace target required after applying the anticanonical
hypersurface connecting map. It does **not** yet construct that connecting
image for any of the eighteen Yukawa entries. The R026 local cochain still
has to be collapsed to the toric cover, lifted to `Z`, differentiated and
divided by the hypersurface equation `f`.

## Factor complex

Index the six fan rays and maximal cones cyclically by

```text
rays:  (1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1),
cones: sigma_i={i,i+1 mod 6}.
```

For `K=-sum_i D_i`, a character-zero local section on a chart intersection
exists exactly when its common cone contains no ray: the toric inequalities
are `<0,v_i>-1 >= 0` for every common ray and hence fail unless the common-ray
set is empty. The resulting Cech dimensions and exact differential ranks are

```text
dim C^p:       0, 9, 20, 15, 6, 1
rank delta_p:  0, 9, 10,  5, 1
dim H^p:       0, 0,  1,  0, 0, 0.
```

All ranks are obtained by standard-library `Fraction` elimination, with every
`delta^2=0` checked. The cyclically invariant two-cocycle

```text
tau_(i,j,k)=1 for all 0<=i<j<k<=5
```

is not a boundary. A normalized dual two-cycle has support

```text
(1/4) * [013 - 024 + 025 + 034 + 124 - 135 + 145 + 235].
```

It annihilates `im(delta_1)`, pairs with `tau` as one and is literally fixed
by the cyclic chart rotation. The certificate also plants the tempting
`012`-for-`013` replacement and rejects it because it fails the dual-cycle
equations. A genuine boundary-shifted trace is accepted and proved homologous,
so the normalization check is not tied to one coordinate row.

## Product trace on 36 charts

The product trace is represented on the actual lexicographically ordered
product cover `(i,j) -> 6*i+j`, not only asserted through Kunneth. For each
pair of supported factor triangles, R027 sums the six `(2,2)` shuffle paths
with their permutation signs. This gives exactly

```text
8 * 8 * 6 = 384
```

nonzero oriented product four-simplices. Its boundary vanishes in the
canonical-weight subcomplex. Against the Alexander--Whitney product cocycle
`tau x tau`, only the `HHVV` shuffle survives in normalized degree, so the
pairing is exactly

```text
Tr_Z(tau x tau)=1.
```

The order-twelve action exchanges the two factors and rotates one of them.
The factor trace is rotation-invariant and the graded factor-exchange sign is
`(-1)^(2*2)=+1`, hence the marked product orientation is preserved.
This is a statement on the one-dimensional cohomology and its trace. The
particular 384-simplex chain is not asserted to be literally fixed by the
published chart permutation; a transformed representative may differ by a
dual boundary.

## Relation to the hypersurface trace

For the anticanonical hypersurface `Y=(f=0)` in `Z`, the exact sequence

```text
0 -> K_Z --f--> O_Z -> O_Y -> 0
```

gives

```text
delta_f : H^3(Y,O_Y) -> H^4(Z,K_Z).
```

Because a smooth complete toric variety has no higher structure-sheaf
cohomology, and `Z` is the product of two such surfaces, this is an
isomorphism. With the marked orientation, the remaining evaluator is

```text
Tr_Y(c)=Tr_Z(delta_f(c)).
```

If `ctilde` is an ambient lift of a coarse Cech three-cocycle, then
`delta(ctilde)=f*q`; R027 supplies the exact finite functional that extracts
the coefficient of `[q]` in `H^4(K_Z)`. An overall nonzero change of
orientation cannot alter nonvanishing or tensor rank. It also does not supply
the Kähler and matter-metric normalization required for a physical Yukawa.

The input `q` must first be expressed in R027's marked toric-character frame.
Raw four-variable chart polynomials are not already in that frame: conversion
requires the Cox line-bundle monomial and the determinant sign of the ordered
ray matrix on every chart. Half of the 36 lexicographic factor charts have the
opposite local ray orientation. R027 does not silently set those transition
units to one; they are an explicit obligation of the next evaluator cell.

## Remaining obstruction

The available principal-cover unit-ideal computation is over `GF(1009)`.
Its Bezout coefficients cancel the four simple `Phi` denominators formally,
but a characteristic-zero claim requires explicit
`Q(zeta_12)` coefficients or a valid lift theorem with all chart-frame units
tracked. R027 therefore banks the trace **target and functional**, not the
yet-unconstructed characteristic-zero refinement collapse.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python3 certificates/r027_toric_top_trace/toric_top_trace.py
```
