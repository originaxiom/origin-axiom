# B19 -- Findings

> Logged observation, not a claim.

## Result

The following solution sets coincide in the bounded exact search:

```text
{X : X^2=I and X L X^-1 = R}
{X : X^2=I and X A X^-1 = RL}
{X : (L X)^2 = A}
```

Each gives exactly `P` and `-P`.

The following are too weak:

```text
X L X^-1 = R
X A X^-1 = RL
det(X)=-1 and X^2=I
X A X^-1 = A^-1
```

They leave many candidates.

## Verdict

**`STALLED`**

The weakest successful operational condition currently found is `(L X)^2=A`,
but this condition itself is not derived from A1-A6.
