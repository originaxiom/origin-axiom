# Probe B19 -- Exchange/half-step axiom audit

> **Speculative frontier work.** Logged observations only. Nothing here is a
> claim.

## Question

Which condition is the weakest successful way to force the swap `P`?

## Result

In bounded exact `GL(2,Z)` searches, these conditions isolate `P` up to sign:

```text
X^2 = I and X L X^-1 = R
X^2 = I and X A X^-1 = RL
(L X)^2 = A
```

Plain `X L X^-1=R`, plain order-conjugacy, plain orientation-reversing
involution, and generic time-reversal of `A` are too weak. The operational
half-step condition `(L X)^2=A` is the best current formulation because it
avoids relying on philosophical exchangeability language.

## Verdict

`STALLED`: `P` is forced by a half-step condition, but the need for a half-step is
still an added structural requirement.
