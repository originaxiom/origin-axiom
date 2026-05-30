# Probe B13 -- Trace map character variety and nested self-reference

> **Speculative frontier work.** Everything here is a logged observation, not a
> claim (`../../GOVERNANCE.md` section 5). Nothing in this directory is promoted
> to `CLAIMS.md`. The relevant open targets remain O1-O4.

## The Question

The previous frontier work left a concrete open target in B2: the monodromy
action on boundary `A`-polynomial coordinates was falsified, but the *fiber*
character variety remained open. For a punctured torus, the fiber group is free
on two generators, and its trace coordinates are

```text
x = tr(a), y = tr(b), z = tr(ab).
```

The standard Fibonacci/Fricke trace map is

```text
T(x,y,z) = (z, x, 2xz - y),
```

with Fricke-Vogt invariant

```text
I(x,y,z) = x^2 + y^2 + z^2 - 2xyz - 1.
```

This probe asks whether that trace-map system gives a calculated continuation of
the `A = LR` spine, and where the interpretation stalls.

## What The Probe Checks

`probe.py` checks only exact algebra:

- the Jacobian of `T` at `(1,1,1)` has characteristic polynomial
  `(t+1)(t^2-3t+1)`;
- the quadratic factor is represented on an invariant rank-2 lattice by a
  `GL(2,Z)` conjugate of `A`;
- the full block basis has determinant `5`, matching the discriminant already
  present in the core;
- the Fricke-Vogt invariant is exactly preserved by the trace map;
- the Cayley cubic `I=0` has four singular points forming a regular tetrahedron;
- the Hessian at `(1,1,1)` has eigenvalues `-2, 4, 4`;
- the local Jacobian family with `x=z=1+eps` keeps the `-1` parity eigenvalue
  exact while splitting the two golden modes;
- the iterate spectrum gives the arithmetic tower `2N log(phi)`;
- the linear proxy `J-I` has eigenvalues `phi, -1/phi, -2`;
- `det(J)=-1`, `det(J^2)=1`, and the absolute eigenvalue product is `1`.
- genericity controls for the symmetric-square lift of nearby `GL(2,Z)` matrices.

## Caveats

The exact result is algebra on a character variety. The following readings are
not earned by the computation:

- `3+1` spacetime: the three trace coordinates are not spatial coordinates, and
  iteration count is not physical time without a dictionary.
- Particle masses: logarithms of trace-map multipliers are spectral rates, not
  observed particle masses.
- Gauge protection: the `-1` eigenvalue is protected in a chosen local Jacobian
  family, not in a derived physical gauge theory.
- Kasner or BKL gravity: determinant and shear analogies are structural, not
  Einstein equations.
- Awareness or self-modeling: the invariant can be described operationally as a
  conserved classifier of the trace-map dynamics; no claim about consciousness
  or phenomenal awareness is made.
- Direct self-containment: the `A` sector appears for the primitive
  orientation-reversing Fibonacci half-step `F` whose square is `A`; the direct
  monodromy `A` gives an `A^2` sector in the symmetric-square trace lift.

## Verdict

`STALLED` at the interpretation dictionary. The trace-map algebra is exact and
nontrivial, and it does contain the `A` quadratic as a lattice-conjugate
rank-2 sector. But converting trace coordinates, eigenvalue rates, or conserved
invariants into physical spacetime, matter, gravity, or awareness requires an
additional dictionary that is not derived here.
