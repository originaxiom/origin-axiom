# B13 -- Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` section 5).

## Exact Results

The punctured-torus trace map

```text
T(x,y,z) = (z, x, 2xz - y)
```

has Jacobian at `(1,1,1)`

```text
J = [[0,0,1],
     [1,0,0],
     [2,-1,2]]
```

with characteristic polynomial

```text
(t + 1)(t^2 - 3t + 1).
```

The quadratic factor is not merely a same-eigenvalues coincidence. On the
rank-2 invariant lattice with basis

```text
b1 = (0, 1, -1),  b2 = (1, 0, 3),
```

the restriction is

```text
M = [[0, 1],
     [-1, 3]],
```

and `M` is `GL(2,Z)`-conjugate to `A = [[2,1],[1,1]]`. Thus the trace-map
linearization contains the `A` quadratic sector in a precise lattice sense. The
full block basis separating the parity line from this rank-2 sector has
determinant `5`.

The Fricke-Vogt invariant

```text
I(x,y,z) = x^2 + y^2 + z^2 - 2xyz - 1
```

is exactly preserved by `T`. Its `I=0` singular set contains the four points

```text
(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1),
```

which form a regular tetrahedron of edge length `2sqrt(2)`. At `(1,1,1)`, the
Hessian has eigenvalues `-2, 4, 4`; the negative direction is the diagonal
`(1,1,1)`.

For the local Jacobian family obtained by setting `x=z=1+eps`, the characteristic
polynomial factors as

```text
(t + 1)(t^2 - (3 + 2eps)t + 1).
```

The parity eigenvalue `-1` is exact throughout this family, while the two golden
modes split at first order:

```text
delta(lambda_phi2)    = 1 + 3sqrt(5)/5
delta(lambda_phi-2)   = 1 - 3sqrt(5)/5
delta(lambda_parity)  = 0.
```

This is a clean algebraic splitting. It is not yet a physical mass splitting.

## Controls

The same calculation also prevents three over-readings:

- The local `x=z=1+eps` family is not a family of trace-map fixed points.
  The trace map fixed points are only `(0,0,0)` and `(1,1,1)`.
- The continuum proxy `J-I` gives eigenvalues `phi, -1/phi, -2`, but this is a
  chosen linearization proxy. A physical continuum generator would require a
  justified time parameter and a branch choice for the `-1` eigenvalue.
- The `A`-sector is a symmetric-square phenomenon of the orientation-reversing
  Fibonacci half-step `F=[[1,1],[1,0]]`, not of the direct orientation-preserving
  monodromy `A=F^2`. The symmetric-square lift has characteristic polynomial

  ```text
  (t-det M)(t^2 - (tr(M)^2 - 2 det(M))t + 1).
  ```

  For `F`, this is `(t+1)(t^2-3t+1)`, so the rank-2 sector is the `A` sector.
  For direct `A`, this is `(t-1)(t^2-7t+1)`, i.e. the rank-2 sector is the
  `A^2` sector. Thus the safe statement is not "the trace map contains itself"
  in an unrestricted sense; it is "the trace-coordinate lift of the primitive
  orientation-reversing half-step contains the `A` sector."

The `A` quadratic appears in such a symmetric-square lift exactly when
`det(M)=-1` and `tr(M)=+/-1` over `GL(2,Z)`. This makes it minimal-discriminant
orientation-reversing structure, not an arbitrary feature of all trace maps.

## Interpretation Boundary

The result is strong as character-variety algebra and weak as physics. It opens
a serious route for studying the fiber character variety that B2 left open, but
it does not derive physical `3+1`, matter content, gravity, or awareness.

The safe statement is:

```text
The trace-map linearization at the Cayley cubic singular point, for the
primitive orientation-reversing Fibonacci half-step, contains the Origin Axiom
A-sector as an exact rank-2 lattice-conjugate sector, together with a parity
sector and an exactly preserved Fricke-Vogt invariant.
```

## Verdict

**`STALLED`**

The exact algebra is real and worth keeping. The bridge from trace coordinates
and invariant surfaces to physical spacetime, particles, gravity, or
self-awareness is still an inserted dictionary.
