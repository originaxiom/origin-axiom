# Probe B17 -- Alternation/persistence selector

> **Speculative frontier work.** Logged observations only. Nothing here is a
> claim.

## Question

Does the half-step language strengthen the original uniqueness theorem, or only
refactor the already-selected `A=LR`?

## Result

The original A1-A6 filters already select `LR/RL` at word length 2. Adding `P`
does not make `LPLP` uniquely selected under the same filters; it gives a
half-step factorization of the same selected sector.

What is new is the operational filter:

```text
find X such that (L X)^2 = A.
```

This selects `X=±P`. Thus alternation is a refactorization/half-step selector,
not an independent replacement for the A1-A6 uniqueness theorem.

## Verdict

`STALLED`: alternation clarifies the mechanism but depends on a new half-step
requirement.
