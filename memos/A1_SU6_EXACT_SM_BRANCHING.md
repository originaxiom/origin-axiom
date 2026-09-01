# R035 — the lifted A1 branch carries the exact joint SM-shaped 27

Source state: `origin/main@864c6b75` (B1232). Verdict: **exact positive
representation-theory compatibility**, with strict physical and selection fences.

## The recovered computation

B1098 proves that the minimal `A1` holonomy stratum has centralizer `su(6)`,
rank five: the Standard Model algebra plus one extra `u(1)` can fit. B1112 later
refers in one line to F2's `MATCH-UP-TO-FRAME`, but the result is not explained
there. R035 supplies a branch-local, dependency-free primary certificate for the
full joint representation statement.

Fix the standard mixed-dual branching

```text
27 | SU(6) x SU(2)_E = (Lambda^2 6, 1) + (bar(6), 2_E),
```

where `SU(2)_E` is the minimal `A1` used by the holonomy and the unbroken gauge
algebra is its `SU(6)` centralizer. Embed inside that centralizer

```text
6 = (3,1)_{-1/3} + (1,2)_{1/2} + (1,1)_0.
```

The generator is therefore

```text
Y_6 = diag(-1/3,-1/3,-1/3, 1/2,1/2, 0),
```

which is traceless. Exact exterior-power branching gives

```text
Lambda^2 6
 = (bar3,1)_{-2/3} + (3,2)_{1/6} + (3,1)_{-1/3}
   + (1,1)_1 + (1,2)_{1/2},

bar6 x 2_E
 = 2(bar3,1)_{1/3} + 2(1,2)_{-1/2} + 2(1,1)_0.
```

Their direct sum is exactly the standard joint E6-GUT refinement of B1102's
charge multiset, with the color/weak assignment fixed independently in B1139:

```text
(3,2)_{1/6}
+ (bar3,1)_{-2/3}
+ 2(bar3,1)_{1/3}
+ (3,1)_{-1/3}
+ 2(1,2)_{-1/2}
+ (1,2)_{1/2}
+ (1,1)_1
+ 2(1,1)_0.
```

This is stronger than an eight-value histogram: color representation, weak
multiplet, charge, and multiplicity all agree, dimension `27` exactly.

## Exhaustiveness and bite within the standard block embedding

The `(bar6,2_E)` summand forces `-a`, `-b`, and `-c` to occur in the target's
respective `(bar3,1)`, `(1,2)`, and singlet charge supports. Exhausting those
finite sets under `3a+2b+c=0` leaves two triples; exactly one gives the full
joint target:

```text
(a,b,c)=(-1/3,1/2,0).
```

The control matters. The different triple

```text
(-1/6,1/2,-1/2)
```

reproduces the same charge histogram but assigns charges to the wrong color/weak
multiplets. A charge census alone would accept a false bridge. R035 rejects it.

There is also an abstract second match if the holonomy `SU(2)_E` itself is
called weak. That `SU(2)` is not in the unbroken centralizer and does not commute
with the nonabelian holonomy, so it is not an unbroken gauge embedding. Taking a
diagonal with an internal weak `SU(2)` does not repair this: `2 x 2 = 1 + 3`
produces a weak triplet absent from the target.

## The branch map changes

The two live E6 landings now have complementary verdicts:

| landing | exact strength | exact obstruction/debt |
|---|---|---|
| A2 / `su(3)+su(3)` | projective, rank four; exact hypercharge values | no color-commuting hypercharge direction (B1102/B1109) |
| A1 / `su(6)` | beat-compatible lifted 27; exact full joint SM-shaped 27 (R035) | rank five leaves one extra `u(1)`; the physical spin/matter map is unearned (R034) |

So the banked A2 no-go must not be globalized to all E6 strata. The A1 route is a
real representation-theoretic escape and the forgotten F2 mention was pointing in
the correct direction.

## What this does not derive

- It does not select the A1 stratum from the 20 nilpotent classes.
- Matching the known SM target identifies `Y_6`; it is a compatibility theorem,
  not an object-side prediction of hypercharge.
- `S(U3 x U2 x U1)` has two block-scalar directions. `Y_6` is one and an extra
  `u(1)` remains unbroken.
- B1145 supplies an internally compatible beat lift, but R034 shows that the map
  to 4d Lorentz spin is still unearned.
- No physical matter functor, chiral Dirac index, three-generation theorem,
  dynamics, normalization, mass, or mixing value follows.
- The conjugate `27bar` reverses the charges; the amphichiral object does not
  thereby select a physical hand.

## Reproduce

```text
python3 certificates/r035_a1_su6_sm_branching/a1_su6_sm_branching.py
```
