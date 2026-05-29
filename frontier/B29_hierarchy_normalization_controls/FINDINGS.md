# B29 -- Findings

> Logged observation, not a claim.

## Exact Hierarchy

Under the B26 projective half-return criterion, matching `F^n` for even `n`
gives:

```text
char(F^n) = t^2 - L_n t + 1
I = (L_n - 2)/4
(lambda/h)^2 = L_n - 2
```

The first values are:

```text
1, 5, 16, 45, 121, 320, ...
```

The selected quantity is the dimensionless ratio `lambda/h`, not an absolute
coupling `lambda`.

## Full-Return Control

The literal full-return criterion differs:

```text
16 c^4 + 2 = L_n
(lambda/h)^2 = sqrt(L_n - 2) - 4
```

It gives negative or zero values for the first entries and does not reproduce
the B25 `lambda/h=1` surface at `n=2`.

## Spectral Control

Finite Fibonacci Hamiltonian approximants at the first projective hierarchy
values `lambda/h = 1, sqrt(5), 4` pass the same top-gap labeling control. That
confirms the code and the known gap-labeling structure across hierarchy values;
it does not derive a physical spectrum.

## Verdict

**`STALLED`**

The hierarchy and normalization are exact and useful. The missing step is still
the derivation of the projective half-return selector itself.
