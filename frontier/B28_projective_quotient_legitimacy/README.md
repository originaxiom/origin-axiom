# B28 -- Projective Quotient Legitimacy

Status: `frontier` / `STALLED`.

## Question

B26 selected `lambda/h=1` by using the projective half-return
`T^3(0,0,c)=(0,0,-c)`. Is that sign flip a canonical quotient operation, or an
ad hoc identification?

## Scope

This probe checks the central sign action on `SL(2)` trace coordinates:

```text
S(sa,sb)(x,y,z) = (sa*x, sb*y, sa*sb*z)
```

and verifies equivariance with the Fibonacci half-step trace map:

```text
T(x,y,z) = (z, x, 2xz-y)
```

## Run

```bash
python frontier/B28_projective_quotient_legitimacy/probe.py
```
