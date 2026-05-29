# B31 -- Findings

> Logged observation, not a claim.

## Result

The projective period-3 return exists for every `c`:

```text
T^3(0,0,c) = (0,0,-c)
```

Therefore primitive projective return alone does not select an invariant
surface.

The derivative of the signed lift at the half-return is:

```text
char(DT^3) = (t+1)(t^2 - (4c^2-2)t + 1)
```

Adding the extra rule "the quadratic sector must equal the original `A`
polynomial `t^2-3t+1`" uniquely gives:

```text
c^2=5/4, I=1/4, lambda/h=1
```

## Verdict

**`STALLED`**

`lambda/h=1` is derived only conditional on the extra `A`-sector matching rule.
The primitive projective return by itself leaves a full one-parameter family.
