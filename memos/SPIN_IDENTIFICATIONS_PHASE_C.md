# R034 — two spin theorems, two missing physical maps

Source state: `origin/main@864c6b75` (B1232). Verdict: **two legacy
identifications are UNEARNED** under B1231's own map-and-action rule. This is a
scope correction, not a retraction of the exact spin-lift or theta computations.

## 1. The beat-selected internal lift is not yet 4d spacetime spin

B1112 and B1141 establish a precise topological/algebraic object: m004 has two
`SL(2,C)` lifts of its projective holonomy, and the beat extension closes over
exactly one. B1145 then proves that the same selected lift closes on the odd
internal `A1` stratum's 27. Its exact operator acts as

```text
Omega^2 = A_27,
Omega A_27 Omega^-1 = A_27,
Omega B_27 Omega^-1 = rho_27(beat(B)).
```

An exact internal action is exhibited. The physical cross-map and action required
by the headline are not. B1145 says so explicitly:
the `A1` is internal to `E6`, not the 4d Lorentz group; its odd weights are not
Weyl spinors; there is no Pin structure, Dirac operator, index, 4d chirality, or
three-generation theorem. B1140's separate spacetime branch uses two Lorentz
`su(2)` factors, and no physical cross-map between those factors and the internal
`A1` is exhibited.

Therefore the identification

```text
beat-selected internal A1 lift  ==  physical 4d Lorentz spin
```

has no exhibited map or action and is **UNEARNED**, while all of B1145's exact
internal algebra remains proved.

The smallest earning result is a specified 4d filling or suspension, its
tangent `Spin(3,1)` or `Pin(3,1)` lift, and an equivariant faithful map from the
internal doublet to a Lorentz spin representation. Chirality or generations
additionally require a Dirac operator and an index.

## 2. A boundary theta polarization is not yet the selected bulk spin class

B359--B363 compute exact/numerical facts about explicitly constructed boundary
theta lifts and show that the seam is two-sided. B364 supplies the decisive
control: both the triangular half-characteristic family and the square integral
family are `T`-stable with their respective multipliers. Thus `T`-stability
selects neither.

B366 later proves that the seam-bearing theta class is forced **within its stated
level-15 geometric-quantization premise**. That closes the choice of boundary
polarization at that tier; it does not construct a map to B1141's bulk spin class.
B1218 correctly records the remaining consequence: a boundary theta-characteristic
and B1141's 3-manifold spin structure are **not identified**. Both being affine
`Z/2` choices, or both carrying the word “spin,” is not a map.

So the identification

```text
boundary theta polarization  ==  beat-selected bulk/observer spin
```

is also **UNEARNED**, without weakening any seam table or theta identity.

The smallest earning result is the typed tangent-frame restriction/extension
map between the bulk spin torsor and the boundary spin torsor, followed by an
exact computation of the boundary image of `chi_beat`. A further observer claim
still needs the 4d Lorentz Spin/Pin construction above.

## Ledger disposition proposed

| row | identification | map | acts | status |
|---|---|---:|---:|---|
| I-8 | odd internal A1 lift = physical 4d spacetime spin | no | no | **UNEARNED** |
| I-9 | boundary theta-characteristic = bulk/observer physical spin | no | no | **UNEARNED** |

These are legacy discoveries from pre-B1231 arcs. Per R033, registering them
requires a deliberate dated baseline migration; hiding them to keep the seed
count green would invert the purpose of the ratchet.

## Reproduce

```text
python3 certificates/r034_spin_identifications/spin_identification_audit.py
```
