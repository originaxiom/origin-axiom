# B52 -- Multichannel Fibonacci Bridge Control

## Question

Does the simplest multichannel Fibonacci tight-binding model produce the PC12
`SL(3)` trace-map recursion as its physical transfer-matrix renormalization?

## Status

```text
STALLED / NEGATIVE CONTROL
PC12 REMAINS MATHEMATICAL
NO PHYSICS CLAIM
```

B52 was opened because the PC12 `SL(3)` trace maps are mathematically stronger
after B51. This probe tests whether that strength already gives a physical
dictionary. It does not.

## Run

```bash
python frontier/B52_multichannel_fibonacci_bridge_control/probe.py
```

## What It Tests

The probe writes the simplest `d=3` channel nearest-neighbor model:

```text
psi_{n+1} + psi_{n-1} + (W + V_s) psi_n = E psi_n,
s in {a,b} following a Fibonacci word.
```

The site transfer matrix is

```text
T_s(E) = [[E I - W - V_s, -I],
          [I,              0]]
```

acting on `(psi_n, psi_{n-1})`, hence it is `6x6`.

## Verdict

For symmetric channel coupling and onsite matrices, the transfer matrices are
determinant-one symplectic matrices in the doubled phase space. They are not
natural `3x3` `SL(3)` transfer matrices. In the commuting diagonal control they
decompose into three independent `2x2` `SL(2)` channels, not one `SL(3)`
channel.

The PC12 third-order Cayley-Hamilton trace recursion fails on the generic
`6x6` transfer matrices. The correct Cayley-Hamilton recursion has order six.

This is useful negative evidence: the missing physics bridge is not the naive
three-channel tight-binding model.
