# R039 — 2T versus A4 is exactly a finite spin-lift torsor, and A6 selects its point

Source state: `codex/seat-r001@f024f0f8`. Verdict: **exact central-extension
and covering-group theorem**, with a strict fence against identifying it with
tangent or four-dimensional Lorentz spin.

## The result hidden behind R037

Use the central extension

```text
1 -> C2 -> 2T=SL(2,3) -> A4 -> 1,
```

which is the restriction of `Spin(3)=SU(2) -> SO(3)` to the tetrahedral
rotation group. R037 proved that exactly one of m004's two `2T` quotient
classes extends over its nonorientable Gieseking parent m000. R039 now projects
every map through the center and computes the full lift square:

```text
                         restriction
Surj(m000,A4): 24 maps  ------------->  Surj(m004,A4): 24 maps
       one Aut(A4) orbit                 one Aut(A4) orbit
                         BIJECTION

each A4 map: 2 lifts to 2T          each A4 map: 2 lifts to 2T
the two restrict to one map         exactly one extends over m000
```

Thus the `A4` quotient data pass through A6 unchanged. The information lost at
the cover is exactly the central lift bit: the two parent lifts differ by the
orientation character, which vanishes on the orientation subgroup. Conversely,
the cover has its own nonzero `H^1(m004;C2)` twist, and that second lift does
not extend.

At the level of finite representations, the phrase **“2T versus A4 is a spin
lift” is now literal rather than analogical**. Every one of the 24 `A4` maps
has exactly two lifts through the finite `Spin(3)` preimage, and the
nonorientable parent selects one.

## The cohomological square

For either group, lifts of a fixed `A4` representation—when nonempty—form a
torsor under `H^1(-;C2)`. Both torsors here have two elements. Restriction does
two different things:

```text
H^1(m000;C2) -> H^1(m004;C2)
orientation bit |-> 0,
```

so the two parent `2T` lifts collapse to the same cover lift, while the other
cover lift has no parent. This explains R037's apparently asymmetric `48 ->
24 subset of 48` without any count-based identification.

For each fixed `A4` representative, the finite lift set is therefore a
two-point `H^1(m004;C2)` torsor with an extension-selected point. B1141's
geometric `SL(2,C)` holonomy lifts have the same *abstract* description. After
separately choosing those two selected points and identifying the two `C2`
actions, there is a unique equivariant bijection between the underlying
pointed sets. R039 does **not** make that comparison canonical: it supplies no
typed map between the finite representation problem and B1141's semilinear
geometric/beat extension. The programme has one `Aut(A4)` quotient class, not
a preferred target framing among its 24 representative maps.

## What is still not identified

The abstract pointed-set bijection is not an intertwiner between the two
representations. The finite `A4` quotient is not thereby the geometric
projective holonomy, the tangent frame bundle, the internal E6 `A1`, or a
four-dimensional Lorentz frame. The typed finite-to-geometric comparison left
open by R021, and R034's two physical identification debts, therefore remain
open.

The smallest missing map is now precise: exhibit a representation-level
intertwiner or functor from the relevant geometric/tangent lift to this finite
tetrahedral quotient, then show that it carries B1141's selected lift to
R039's extendable lift. Merely observing that both are pointed two-torsors is
not enough for physical spin or chirality.

## Reproduce

```text
python3 certificates/r039_a4_2t_lift_torsor/a4_2t_lift_torsor.py
```

The certificate uses only the Python standard library and runs from any cwd.
