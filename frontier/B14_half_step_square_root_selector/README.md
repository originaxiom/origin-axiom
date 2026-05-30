# Probe B14 -- Half-step square-root selector

> **Speculative frontier work.** Everything here is a logged observation, not a
> claim (`../../GOVERNANCE.md` section 5). Nothing in this directory is promoted
> to `CLAIMS.md`.

## The Question

B13 showed that the trace-character lift contains the `A` sector most naturally
through the primitive orientation-reversing Fibonacci half-step

```text
F = [[1,1],[1,0]],   F^2 = A = LR.
```

This probe asks whether that half-step is inserted or forced once the
two-record system has already selected the mixed closure `A`.

## Result

Let

```text
L_a = [[1,a],[0,1]],   R_b = [[1,0],[b,1]],
B(a,b) = L_a R_b = [[1+ab,a],[b,1]].
```

If `B(a,b)` has an integer orientation-reversing square root in `GL(2,Z)`, then
`ab` must be a perfect square and the root is

```text
X = (B(a,b)-I) / sqrt(ab).
```

For positive integers, integrality forces `a=b`. Thus the half-step condition
selects the symmetric mixed closures:

```text
B(k,k) = (L_k P)^2,   P = [[0,1],[1,0]].
```

For the already selected core `A=B(1,1)`, the only square roots in `GL(2,Z)` are

```text
F = L P = [[1,1],[1,0]]
-F.
```

## Interpretation

This does not derive `A` from nothing. It says something narrower and useful:
once the record-swap `P` is admitted as a symmetry of the two-record substrate,
the half-step whose square is `A` is unique up to sign.

The half-step criterion also explains why B13's trace lift sees the `A` sector:
the trace lift is naturally a symmetric-square lift of the orientation-reversing
half-step, not of the orientation-preserving monodromy directly.

## Verdict

`STALLED` at the status of the record-swap `P`. The half-step is forced if `P`
is admitted as a substrate symmetry, but `P` is not an orientation-preserving
update under A3. The live question is whether `P` belongs in the allowed
pre-dynamical symmetry layer or remains an inserted choice.
