# R038 — the A1 route contains the exact rank-reducing singlet, but not its physics

Source state: `codex/seat-r001@b9264428`. Verdict: **exact compact-group
stabilizer and branching theorem, conditional physical bridge, plus a SUSY
negative**.

## The algebraic bridge R035 left open

R035 established

```text
27 | SU(6) x SU(2)_E = (Lambda^2 6,1) + (bar6,2_E)
Y = diag(-1/3,-1/3,-1/3,1/2,1/2,0),
```

where `SU(2)_E` is the minimal holonomy `A1` and the unbroken gauge group is
its `SU(6)` centralizer. The two `Y=0` singlets in R035 are precisely the two
components

```text
bar(e_6) tensor s_+,   bar(e_6) tensor s_-.
```

Choose `v=bar(e_6) tensor s_+`. If the `SU(2)_E` factor is correctly treated
as holonomy/multiplicity data and `s_+` is fixed, the compact `SU(6)`
stabilizer of the actual vector is exactly `SU(5)`, not `U(5)`. Thus

```text
SU(6) --<v>--> SU(5),       rank 5 -> 4.
```

The surviving `SU(5)` acts on the first five coordinates and contains the
same `SU(3) x SU(2) x U(1)_Y` used in R035. The candidate is an exact SM
singlet, so the rank-reducing step preserves the embedded SM algebra.

This is the representation-theoretic operation B964 names as missing: a
rank-reducing `27` VEV. It shows that the recovered A1 branch has a perfectly
matched *seat* for that operation. It does not show that the object performs
it.

## The type distinction that prevents a false closure

If one incorrectly promotes `SU(2)_E` to a second four-dimensional gauge
factor and stabilizes the same tensor under the covering product, reciprocal
phases survive. The exact compact preimage stabilizer is

```text
{(diag(A,z),diag(z,z^-1)) : A in U(5), z=det(A)^-1} ~= U(5).
```

The actual `A5 A1` subgroup in `E6` is
`(SU(6) x SU(2)_E)/C2`, because `(-I_6,-I_2)` acts trivially on the `27`.
Consequently the faithful-image stabilizer is globally `U(5)/C2`; its Lie
algebra is `u(5)`, of dimension 25 and rank 5. In R035's charge frame define

```text
X = diag(1/3,1/3,1/3,0,0,-1),
T_E = diag(1,-1).
```

Pure `X` is broken, but the diagonal generator

```text
(2Y+5X, -5 T_E)
```

annihilates `v`. The full-product reading therefore removes only one of six
ranks and leaves a diagonal `U(1)`; it does **not** close to the rank-four SM.
R038's positive rank closure is valid only in the banked A1-centralizer
typing, where `SU(2)_E` is the holonomy rather than an unbroken gauge factor.

## What the 27 becomes

For the full-product `U(5)/C2` control, the local
`su(5) + u(1)_H` weights are exact (no claim of a direct-product global form):

```text
27 -> 10_2 + 5_-4 + bar5_-6 + bar5_4 + 1_0 + 1_10,
```

with the proposed VEV in `1_0`. Forgetting `U(1)_H` gives the familiar

```text
27 -> 10 + 5 + 2 bar5 + 2 singlets.
```

This exposes, but does not yet implement, the usual possible separation into
one chiral `10+bar5`, vectorlike material, and singlets. Which fields are
eaten or become massive depends on an actual scalar sector and couplings;
R038 does not infer a physical generation from the bare branching.

## The exact negative

A single decomposable vector in `(bar6,2_E)` is not D-flat even when only the
`SU(6)` centralizer is gauged. Its `su(6)` trace-free partial projector has
squared norm `5/6`. If `SU(2)_E` is also gauged, its second partial projector
adds another nonzero moment map of squared norm `1/2`:

```text
5/6  in su(6),    1/2 in su(2).
```

The relevant moment maps are therefore nonzero. A conjugate field or additional VEVs are
required for a supersymmetric vacuum, and that completion may change the
stabilizer. This is a theorem-level fence, not a model-building detail.

## What remains unearned

- The object does not select the A1 stratum from the twenty-class menu.
- Nothing proves that either `s_+` component is a four-dimensional scalar
  zero mode rather than internal representation data.
- No potential, vacuum selection, D-flat/F-flat completion, physical matter
  functor, chirality, generation count, or mass spectrum is derived.
- The known SM target was used to identify `Y`; it is not predicted here.
- Treating a component of the mathematical `27` simultaneously as a Higgs
  scalar and as observed fermionic matter would be a type error.

R038 therefore closes the *finite-dimensional group-theory shape* of the A1
rank step while making the remaining physical arrow smaller and more precise:

```text
derive a scalar zero mode + select a D/F-flat rank-one direction.
```

## Reproduce

```text
python3 certificates/r038_a1_rank_reduction/a1_rank_reduction.py
```

The certificate uses only the Python standard library and runs from any cwd.
