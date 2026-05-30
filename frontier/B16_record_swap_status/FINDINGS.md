# B16 -- Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` section 5).

## What Is Forced

If an operation `X in GL(2,Z)` is required to be an involution and to exchange
the primitive shears,

```text
X^2 = I
X L X^-1 = R,
```

then the only possibilities are

```text
X = P  = [[0,1],[1,0]]
X = -P = [[0,-1],[-1,0]].
```

The sign does not change the induced square root of `A` in B14, because
`(-F)^2=F^2=A`.

Similarly, the only bounded `GL(2,Z)` automorphisms of the primitive pair
`{L,R}` are

```text
I, -I, P, -P,
```

with `P` and `-P` swapping the pair.

## What Is Not Forced

A1-A6 in the current conditional uniqueness theorem do not require the
orientation-reversing swap. They restrict updates to the orientation-preserving
mixed closure for the persistent sector. A7 records the residual order choice
`LR` versus `RL`; it does not derive an operation that exchanges them.

Therefore `P` is not currently a theorem of the substrate. It becomes forced
only after adding an exchange-symmetry axiom such as:

```text
The two record labels carry no intrinsic identity before dynamics, so the
substrate admits the involution exchanging them.
```

That axiom is plausible, but it is still an axiom.

## Why This Matters

B13-B14 showed that the trace-map recursion depends on the half-step

```text
F = L P,   F^2=A.
```

B16 shows the exact status of the missing piece:

```text
P is unique up to sign as the primitive-pair exchange symmetry,
but exchange symmetry itself is not derived from A1-A6.
```

This is a useful narrowing of the wall. The missing object is no longer vague:
it is precisely the exchange symmetry of the two-record substrate.

## Minimality Controls

Several weaker-looking requirements were tested.

Too weak:

```text
det(X)=-1 and X^2=I
```

This leaves many orientation-reversing involutions in `GL(2,Z)`.

Still sufficient to force `P` up to sign:

```text
det(X)=-1, X^2=I, and X L X^-1 = R^(+/-1)
det(X)=-1, X^2=I, and X A X^-1 = RL
(L X)^2 = A
```

Each of these gives exactly `X=P` or `X=-P` in the bounded exact search. By
contrast, asking only for an orientation-reversing involutive time-reversal of
`A`,

```text
X A X^-1 = A^-1,
```

leaves many candidates and does not isolate `P`.

The weakest successful formulation currently found is not full philosophical
"exchangeability" but the operational half-step condition:

```text
find X such that (L X)^2 = A.
```

This directly says: after one primitive update, what operation makes the
two-step process equal the persistent sector? The answer is `X=+/-P`.

## Verdict

**`STALLED`**

`P` is conditionally forced by either an exchange-symmetry axiom or the
operational half-step condition `(L X)^2=A`. It is not unconditionally forced by
the current minimal-record axioms alone.
