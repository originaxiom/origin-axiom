# B32 -- Findings

> Logged observation, not a claim.

## Dependency Audit

The current exact chain is:

```text
A1-A6 -> A
exchange/half-step -> F=LP, F^2=A
trace functoriality -> T(x,y,z)=(z,x,2xz-y)
central-sign quotient -> projective period-3 return
```

This chain still does not select `I=1/4`. Selection requires one more rule:

```text
S1: the primitive projective return linearization must contain the original A
    quadratic sector t^2-3t+1.
```

With S1:

```text
I=1/4, lambda/h=1
```

Without S1:

```text
I=c^2-1 remains free.
```

## Verdict

**`STALLED`**

The missing object is now isolated: S1, the `A`-sector self-similarity selector.
It is not derived by the current A1-A7 plus exchange package.
