# B15 -- Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` section 5).

## What Survived

The diagonal linearization family of the naive proxy `V=T-id` is exact:

```text
char(J_V(c)) = (mu+2)(mu^2 + (1-2c)mu + (1-2c)).
```

This gives three clean algebraic checkpoints:

```text
c=0     -> (mu+2)(mu^2+mu+1)      discriminant -3
c=1/2   -> (mu+2)mu^2             discriminant 0
c=1     -> (mu+2)(mu^2-mu-1)      discriminant 5
```

So the Eisenstein and golden quadratics are real endpoint signatures of this
linearization family. However, the only diagonal fixed points of the trace map
are `c=0` and `c=1`. The midpoint `c=1/2` is a linearization checkpoint, not a
trace-map fixed point.

The discrete trace map preserves the Fricke-Vogt invariant exactly:

```text
I(T(x,y,z)) - I(x,y,z) = 0.
```

The naive continuum proxy fails this control. At `(3/2,1,3/2)`, which lies on
`I=0`,

```text
dI/dt along V=T-id = -5/4.
```

This supports the limited statement that the full discrete map carries structure
not retained by the simplest continuum proxy.

## What Did Not Survive

The proposed Fibonacci coupling `lambda=sqrt(5)` at `(1,1,3/2)` does not follow
under the invariant normalization used here. Direct calculation from the usual
Fibonacci initial line

```text
x=(E-lambda)/2, y=E/2, z=1
```

gives

```text
I=lambda^2/4.
```

Since `I(1,1,3/2)=1/4`, this yields `lambda=1`, not `sqrt(5)`. The `sqrt(5)`
value requires a shifted formula `I=lambda^2/4-1`; that is a convention mismatch
with the current invariant. This route is not accepted as a result.

The phase labels

```text
I=-1 -> nothing
I=0 -> awareness
I=1/4 -> existence
```

are interpretive names for invariant surfaces, not derived semantics. The exact
fact is only that the discrete trace map cannot move an orbit between different
`I`-surfaces.

## Verdict

**`STALLED`**

The endpoint number-field algebra and discrete invariant control are real. The
dictionary to awareness, physical coupling, and phase semantics is not derived;
one proposed `sqrt(5)` coupling is rejected under the current normalization.
