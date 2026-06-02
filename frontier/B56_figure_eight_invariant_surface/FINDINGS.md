# B56 Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Verdict

```text
DEAD
```

The hoped-for bridge -- that the figure-eight knot sits on the self-evidencing
surface `I = 1/4`, linking it to the `c=1` Eisenstein structure -- has no
support.

## Exact Results

**Diagonal representations miss `I = 1/4`.** On the diagonal locus `x=y=z=w`, the
cubic `w^3 - 2w^2 - 2w + 1 = (w+1)(w^2 - 3w + 1)` has roots `w in {-1, phi^2, phi^-2}`.
The Fricke-Vogt invariant `I = 3w^2 - 2w^3 - 1` evaluates to

```text
w = -1     : I = 4
w = phi^2  : I = -17/2 - 7 sqrt(5)/2
w = phi^-2 : I = -17/2 + 7 sqrt(5)/2
```

None equals `1/4`. The two irrational values multiply to the clean integer `11`
(`(-17/2)^2 - (7 sqrt5/2)^2 = 11`) -- ordinary `Q(sqrt 5)` algebra, not a
structural relation to `1/4`.

**The Eisenstein resemblance is a cyclotomic coincidence.** The figure-eight
ideal tetrahedron shape solves `z^2 - z + 1 = 0` (root `e^{i pi/3}`, discriminant
`-3`, trace field `Q(sqrt -3)`) -- a complex point, disjoint from the real
diagonal locus above. The `c=1` symmetric-sector factor (B55) is the same
polynomial only because `Phi_6 = t^2 - t + 1` is the simplest discriminant `-3`
cyclotomic. Same polynomial, unrelated origins.

## Scope Guard

The separate fact that the `c=1` twins' discriminant pair `(-3, 5)` matches the
factors of the figure-eight gluing equation `z^2(z-1)^2 = (z^2-z+1)(z^2-z-1)`
(claim P12) is **not** affected. That gluing-equation echo stands as a recorded
structural observation; only the holonomy / `I=1/4` bridge is dead.

## Impact

B56 is a clean boundary for PC12 and for the quarantined self-evidencing path
(`paths/E21`): it removes a tempting but unsupported figure-eight bridge, so the
`c=1` Eisenstein structure is kept as exact trace-map algebra without a knot-
theoretic over-reading. No claim is promoted; the figure-eight remains connected
to the core only through the already-proven P9/P12 facts.
