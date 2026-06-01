# B52 Findings

## Verdict

```text
STALLED / NEGATIVE CONTROL
```

The simplest three-channel Fibonacci tight-binding construction does not supply
the missing PC12 physics bridge.

## What Was Tested

The model is the standard three-channel nearest-neighbor equation

```text
psi_{n+1} + psi_{n-1} + (W + V_s) psi_n = E psi_n
```

with Fibonacci letter `s in {a,b}`. Its transfer matrix is

```text
T_s(E) = [[E I - W - V_s, -I],
          [I,              0]]
```

This is a `6x6` matrix because a second-order lattice equation needs both
`psi_n` and `psi_{n-1}`.

## Exact Control Results

```text
det(T_a)=det(T_b)=1
T_a and T_b preserve the canonical symplectic form
the position-only 3D subspace is not closed because the -I block is nonzero
the diagonal commuting control decomposes into three independent SL(2) channels
the PC12 third-order trace recursion fails on generic 6x6 transfer matrices
the order-six Cayley-Hamilton recursion holds, as expected for 6x6 matrices
```

## Consequence

The naive bridge has the wrong group and the wrong Cayley-Hamilton order:

```text
PC12: 3x3 SL(3) character-variety recursion
naive 3-channel physics model: 6x6 symplectic doubled-phase transfer recursion
```

This is not a contradiction of PC12. It is a failed dictionary. PC12 stays a
standalone mathematical candidate.

## Next Live Bridge Question

To connect PC12 to physics, a future model would need a first-order
three-component evolution whose physical transfer matrices are genuinely
`SL(3)`, or a principled reduction from the `6x6` symplectic cocycle to an
`SL(3)` character-variety quotient. The standard tight-binding construction
does not provide that reduction.
