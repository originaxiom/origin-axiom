# Probe B18 -- Trace-lift functoriality

> **Speculative frontier work.** Logged observations only. Nothing here is a
> claim (`../../GOVERNANCE.md` section 5).

## Question

Is the trace map used in B13 a canonical consequence of the half-step

```text
F = L P,  F^2 = A,
```

or merely an eigenvalue coincidence?

## Computation

For the Fibonacci half-step automorphism

```text
a -> ab
b -> a
```

on the free group on two generators, full trace coordinates

```text
X=tr(a), Y=tr(b), Z=tr(ab)
```

transform as

```text
(X,Y,Z) -> (Z, X, XZ - Y).
```

Passing to half-trace coordinates `X=2x`, `Y=2y`, `Z=2z` gives exactly

```text
T(x,y,z) = (z, x, 2xz - y).
```

Thus the B13 trace map is the `F`-level trace lift. The `A`-level map is `T^2`.

## Verdict

`STALLED` at the physics dictionary, but the canonicality gate passes: the trace
map is the functorial character-variety lift of the half-step `F`.
