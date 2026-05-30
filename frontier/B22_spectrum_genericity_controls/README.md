# Probe B22 -- Spectrum genericity controls

> **Speculative frontier work.** Logged observations only. Nothing here is a
> claim.

## Question

Is the `-1` parity sector special to the half-step `F=L P`, or generic for
orientation-reversing trace lifts?

## Result

For any `M in GL(2,Z)`, the symmetric-square trace lift has characteristic
polynomial

```text
(t-det M)(t^2 - (tr(M)^2 - 2 det(M))t + det(M)^2).
```

Therefore every orientation-reversing map has a `-1` sector. The `-1` sector is
generic. What is special to the half-step is the `A` quadratic, which occurs
only for `det=-1` and `tr=±1`.

## Verdict

`STALLED`: the special particle/gauge reading of the `-1` sector is rejected;
the special surviving object is the minimal orientation-reversing `A` sector.
