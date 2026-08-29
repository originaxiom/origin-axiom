# R028 — exact toric chart and line-bundle frames

## Verdict

The 36 affine charts used by the height-308 computation now have deterministic
ray orders, common Laurent-coordinate maps, line-bundle transition monomials
and residue-orientation signs. This closes a convention gap between R026's
determinant formula, R027's marked top trace and the old Sage unit-ideal data.

The gap was load-bearing. The old code stores raw four-variable Cox
polynomials and chooses three chart-orbit representatives with
`next(iter(set))`. Raw chart polynomials are not common Laurent functions, and
the representative choice is not stable across runs. Moreover, exactly half
the chart ray frames have negative orientation. Transporting polynomials
without these factors can produce a plausible but sign-wrong residue row.

R028 does not yet serialize the height-308 `Phi` coefficients or construct
the characteristic-zero Bezout multipliers required for refinement collapse.

## Exact lattice and chart action

In the source convention, the order-twelve action on the ray lattice and its
contragredient monomial action are

```text
ZETA_N = [[0,0,0,-1], [0,0,1,1], [1,0,0,0], [0,1,0,0]],
A_M    = [[0,0,1,-1], [0,0,1,0], [1,0,0,0], [0,1,0,0]].
```

They satisfy `<A_M u,ZETA_N v>=<u,v>`. Applying `ZETA_N` to monomial
exponents instead is retained as a failing control. On the twelve rays the
exact permutation is

```text
(6,7,8,9,10,11,1,2,3,4,5,0).
```

Number the product chart with factor-cone starts `(i,j)` by `6*i+j`. Its
induced action is

```text
(i,j) -> (j+1 mod 6,i),
```

of order twelve. The three chart orbits all have length twelve. Replacing the
unordered-set representatives by the smallest chart in each orbit pins them
as

```text
(0,1,2).
```

## Affine coordinates and orientations

The Sage routine defines its variables by `tuple(sorted(cone))`, where it
sorts the four ray **vectors**, not their global integer labels. If

```text
V_sigma=[v_1 v_2 v_3 v_4],
```

then the common torus coordinates are

```text
y_i=t^(row_i(V_sigma^-1)).
```

Every `V_sigma` is unimodular. The three deterministic representatives give

```text
chart 0: y=(t4,t3,t2,t1),
chart 1: y=(t3^-1,t3*t4,t2,t1),
chart 2: y=((t3*t4)^-1,t4,t2,t1).
```

The ordered-ray determinant is positive precisely when the two cone starts
are both in `{0,1,2}` or both in `{3,4,5}`. Hence the exact census is

```text
det(V_sigma)=+1 on 18 charts,
det(V_sigma)=-1 on 18 charts.
```

This sign belongs in any local canonical-form or residue comparison. The
certificate rejects both global-ray-ID sorting and an all-positive orientation
convention.

## Line-bundle frames

For `D=sum_r a_r D_r`, define on a chart

```text
q_(D,sigma)(y)=product_(v_i in sigma) y_i^a_i,
ell_(D,sigma)=q_(D,sigma)^(-1).
```

Here `ell` is the Cartier/rational line-bundle frame; `q_D^-1` is not being
called a nowhere-vanishing polynomial function on the whole affine chart.

For every lattice point `u`, the raw polynomial monomial made by the existing
`chart_monomial` routine satisfies exactly

```text
product_i y_i^(<u,v_i>+a_i) = q_(D,sigma)(y) * t^u.
```

R028 verifies this on every one of the 36 charts for all 49 anticanonical
points and all `12 x 35` component points. Therefore a raw local coefficient
`p_(D,sigma)` converts to the common Laurent rational function as

```text
p_(D,sigma)(y(t)) / q_(D,sigma)(y(t)).
```

For `H=-K_Z`, `q_H=product_i y_i`. For a component of
`Phi:B=sum O(D_c)->O(H)`, the relevant frame is

```text
q_(H-D_c)=q_H/y_(i_c)  if ray c lies in sigma,
q_(H-D_c)=q_H          otherwise.
```

If `p_(c,sigma)` is the raw local `Phi_c`, then

```text
Phi(e_(D_c,sigma)) = p_(c,sigma) e_(H,sigma),
s_(c,sigma)=e_Dc/Phi_c has common coefficient q_(H-D_c)/p_(c,sigma).
```

Those are the coefficients that must be used in the four transition
differences of R026. The common temptation to use `1/p_c` alone drops the
line-bundle frame.

## Two defects isolated in the old exploratory script

The unit-ideal result itself remains useful, but two accompanying checks must
not be read more broadly:

- `next(iter(orbit))` makes chart representatives dependent on set iteration;
  R028 replaces it by fixed representatives `0,1,2`.
- `Phi_a*Phi_b-Phi_b*Phi_a=0` is commutativity in a polynomial ring, not a
  cross-chart gluing or frame-transition check.

The next artifact must serialize exact `Q(zeta_12)` coefficients for the 49
hypersurface terms, the 35 first-component `Phi` terms, and explicit Bezout
multipliers on the three fixed representatives. Transport to the other 33
charts must use the action and frame factors certified here.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python3 certificates/r028_toric_chart_frames/toric_chart_frames.py
```
