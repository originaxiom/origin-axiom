# B17 -- Findings

> Logged observation, not a claim.

## Result

Same-record repetition does not produce the first hyperbolic persistent sector:

```text
L^n and R^n are parabolic for n>0.
```

The original determinant, torsion-free, and minimal-trace filters select `LR`
and `RL` at length 2. When `P` is added to the alphabet, many longer spellings
reduce to the same selected sectors because `P^2=I` and `P L P=R`.

The half-step spelling

```text
L P L P = A
```

is therefore not a new uniqueness theorem under the old filters. It is the
unique solution to a new operational question:

```text
After one primitive update L, what X makes (L X)^2=A?
```

The answer is `X=±P`.

## Verdict

**`STALLED`**

The carried-over A1-A6 filters select `A` already. Alternation explains the
half-step structure but requires the half-step question as an added condition.
