# Probe B26 -- `lambda=1` derivation attempt

> **Speculative frontier work.** Logged observations only. Nothing here is a
> claim.

## Question

Can `lambda=1` in the Fibonacci Hamiltonian be derived from the half-step
kernel, or is it an additional self-dual coupling choice?

## Result

There is a real and nontrivial projective selector:

```text
T(x,y,z) = (z, x, 2xz-y)
T^3(0,0,c) = (0,0,-c)
char(DT^3 at (0,0,c)) = (t+1)(t^2 - (4c^2-2)t + 1)
```

The `A` polynomial `t^2-3t+1` appears in this projective half-return
linearization if and only if:

```text
4c^2 - 2 = 3
c^2 = 5/4
I = c^2 - 1 = 1/4
lambda^2/4 = 1/4
lambda = 1    (positive coupling convention)
```

## Caveat

This is not a literal period-3 orbit of the signed trace map. It is a
sign-flipping half-return:

```text
(0,0,c) -> (c,0,0) -> (0,c,0) -> (0,0,-c)
```

The literal return is period 6, and the `T^6` multiplier does **not** contain
`A`'s characteristic polynomial at `I=1/4`.

Therefore `lambda=1` is selected by an additional projective/sign-quotient
self-reference criterion. That criterion is natural in the trace/character
setting, but it has not yet been derived from A1-A7 plus exchange symmetry.

## Lucas Hierarchy

The same projective half-return criterion does not only select `lambda=1`.
Matching the half-return quadratic to the characteristic polynomial of `F^n` for
even `n` gives:

```text
char(F^n) = t^2 - L_n t + 1
4c^2 - 2 = L_n
I = c^2 - 1 = (L_n - 2)/4
lambda^2 = 4I = L_n - 2
```

For `n=2,4,6,8,10,...`:

```text
lambda^2 = 1, 5, 16, 45, 121, ...
```

The ratios converge to `phi^2`. This is exact algebra under the same projective
selector; it is not yet a physical spectrum or a derivation of the selector.

## Full-Return Control

The literal full return `T^6(0,0,c)=(0,0,c)` gives:

```text
char(DT^6) = (t-1)(t^2 - (16c^4+2)t + 1)
```

Matching `A` then solves `c^2=1/4` over real `c`, hence `I=-3/4` and
`lambda^2=-3` under the B25 convention. Therefore the full-return criterion does
**not** select the B25 `lambda=1` surface. The half-return/projective distinction
is load-bearing.

## Verdict

`STALLED`, strengthened from B25:

```text
lambda=1 is the first member of an exact Lucas hierarchy selected by projective
half-return self-similarity, but the projective criterion itself remains an
added rule.
```

So the status remains **MOTIVATED**, not **DERIVED**.
