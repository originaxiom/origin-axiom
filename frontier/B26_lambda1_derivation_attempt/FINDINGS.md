# B26 -- Findings

> Logged observation, not a claim.

## What was tested

The proposed derivation of `lambda=1` from the period-3 orbit of the Fibonacci
trace map:

```text
T(x,y,z) = (z, x, 2xz-y)
```

## Exact result

The claimed characteristic polynomial is correct for the derivative of `T^3` at
`(0,0,c)`:

```text
char(DT^3) = (t+1)(t^2 - (4c^2-2)t + 1)
```

Matching the `A` sector requires:

```text
4c^2 - 2 = 3
c^2 = 5/4
I = c^2 - 1 = 1/4
lambda = 1
```

under positive-coupling convention.

## Correction

`(0,0,c)` is not a literal period-3 orbit under the signed trace map:

```text
T^3(0,0,c) = (0,0,-c)
T^6(0,0,c) = (0,0,c)
```

The literal `T^6` return has quadratic factor:

```text
t^2 - (16c^4+2)t + 1
```

At `c^2=5/4`, this is `t^2-27t+1`, not `t^2-3t+1`.

## Verdict

**`STALLED`**

The computation strengthens the motivation for `lambda=1`: it is the unique
surface where the projective half-return linearization reproduces the `A`
quadratic sector. It does not yet derive `lambda=1` from the existing core,
because the projective half-return self-similarity criterion is an additional
selection rule.
