# B28 -- Findings

> Logged observation, not a claim.

## Result

The B26 sign flip is not arbitrary. For central lift signs
`sa,sb in {+1,-1}`,

```text
S(sa,sb)(x,y,z) = (sa*x, sb*y, sa*sb*z)
```

the Fibonacci trace map is equivariant:

```text
T(S(sa,sb)(p)) = S(sa*sb, sa)(T(p))
```

The Fricke-Vogt invariant is also unchanged under this central sign action.

At the B26 orbit:

```text
T^3(0,0,c) = (0,0,-c)
```

and `(0,0,-c)` is related to `(0,0,c)` by a legitimate central sign action, for
example `S(1,-1)`.

## Control

The global antipodal map `(x,y,z)->(-x,-y,-z)` is not a generic central sign
action and does not preserve the Fricke-Vogt invariant in general. The B26
identification works because the orbit lies on `x=y=0`, where the required sign
flip is exactly a central-lift ambiguity.

## Verdict

**`STALLED`**

The projective/sign quotient used by B26 is legitimate once one passes to
lift-independent `PSL`/central-sign character data. However, the decision to use
that quotient as the selector remains a bridge criterion, not something derived
from A1-A7.
