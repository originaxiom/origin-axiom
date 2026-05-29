# B30 -- Findings

> Logged observation, not a claim.

## Result

The central-sign quotient is canonical once the state space is taken to be
lift-independent `PSL` trace-character data.

For signs `sa,sb in {+1,-1}`:

```text
S(sa,sb)(x,y,z) = (sa*x, sb*y, sa*sb*z)
```

The invariant quotient coordinates are:

```text
u=x^2, v=y^2, w=z^2, r=xyz,  r^2=uvw
```

The Fibonacci trace map descends polynomially:

```text
(u,v,w,r) -> (w, u, 4uw - 4r + v, 2uw - r)
```

In these quotient coordinates, the B26 sign-flipping half-return becomes a
literal period-3 return:

```text
(0,0,c^2,0) -> (c^2,0,0,0) -> (0,c^2,0,0) -> (0,0,c^2,0)
```

## Verdict

**`STALLED`**

The quotient is canonical conditional on choosing lift-independent `PSL` data.
It still does not select `I=1/4`; every value of `c^2` has the same projective
period-3 return.
