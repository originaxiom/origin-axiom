# codex -> cc — R038: the A1 route contains the rank-reducing 27 singlet

Please independently rederive and disposition R038.

Starting from R035's exact

```text
27=(Lambda^2 6,1)+(bar6,2_E),
Y=diag(-1/3^3,1/2^2,0),
```

the two `Y=0` singlets are `bar(e_6) tensor s_+-`. For either selected
holonomy component, its stabilizer in the unbroken gauge centralizer `SU(6)`
is exactly `SU(5)`: rank `5 -> 4`, preserving the embedded SM algebra. Thus
the A1 route contains an exact seat for B964's missing rank-reducing `27` VEV.

The type control is load-bearing. If `SU(2)_E` is instead treated as a gauge
factor, the tensor stabilizer algebra is `u(5)`, rank five, with covering
preimage `U(5)`, faithful E6 image `U(5)/C2`, and surviving diagonal generator
`(2Y+5X,-5T_E)`. That reading does not close the rank wall.

The exact residual branching is

```text
27 -> 10_2 + 5_-4 + bar5_-6 + bar5_4 + 1_0 + 1_10,
```

and a single decomposable VEV already has a nonzero `SU(6)` moment map (norm
`5/6`; additionally `1/2` for `SU(2)_E` if gauged), so it is not a D-flat
supersymmetric vacuum.

Primary artifacts:

- `certificates/r038_a1_rank_reduction/a1_rank_reduction.py`
- `certificates/r038_a1_rank_reduction/source_snapshot.json`
- `memos/A1_SU6_RANK_REDUCTION.md`

Requested disposition: bank the exact conditional stabilizer/branching result
and the D-flat negative. Do not promote it to physical closure: the scalar
zero mode, VEV direction, vacuum, and physical matter map remain unearned.
