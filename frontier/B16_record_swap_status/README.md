# Probe B16 -- Status of the record-swap symmetry

> **Speculative frontier work.** Everything here is a logged observation, not a
> claim (`../../GOVERNANCE.md` section 5). Nothing in this directory is promoted
> to `CLAIMS.md`.

## The Question

B14 reduced the half-step question to the status of the record-swap matrix

```text
P = [[0,1],[1,0]].
```

If `P` is an allowed pre-dynamical symmetry of the two-record substrate, then
the half-step `F=L P` is forced up to sign and `F^2=A`. If `P` is not forced,
then the trace-map recursion still rests on an inserted exchange operation.

This probe tests what the current axioms do and do not force.

## Result

The current conditional uniqueness theorem uses A1-A6 plus residual order choice
A7. Those axioms select the persistent sector `A=LR` up to `LR/RL`, but they do
not include the orientation-reversing record swap as an allowed update.

Inside `GL(2,Z)`, the involutions that conjugate `L` to `R` are exactly

```text
P  = [[0,1],[1,0]]
-P = [[0,-1],[-1,0]].
```

Thus `P` is unique up to sign **if** one asks for an involutive symmetry that
exchanges the two primitive shears. But that exchange requirement is an
additional axiom, not a consequence of A1-A6.

## Interpretation

This is the cleanest current status:

```text
A1-A6 force A up to order.
Adding exchange symmetry forces P up to sign.
A plus P forces F=L P up to sign.
F's trace lift contains the A-sector.
```

The remaining open question is whether exchange symmetry should be counted as
part of the two-record substrate before orientation-preserving dynamics begin,
or as an inserted operation.

## Verdict

`STALLED` at exchange symmetry. `P` is unique once the exchange-symmetry problem
is asked, but the existing axioms do not force asking it.
