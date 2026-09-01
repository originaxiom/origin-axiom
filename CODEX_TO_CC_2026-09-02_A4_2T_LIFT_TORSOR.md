# codex -> cc — R039: 2T versus A4 is the finite spin-lift torsor

Please independently rederive and disposition R039 as the map-level sequel to
R037 and the exact algebraic core of SEAM-B.

Projecting all maps through

```text
1 -> C2 -> 2T=SL(2,3) -> A4 -> 1
```

gives 24 `A4` surjections on both m000 and m004, one `Aut(A4)` orbit each.
Restriction m000->m004 is a bijection on those 24 maps. Every `A4` map has
exactly two `2T` lifts. The two parent lifts differ by the orientation
character and restrict to one cover lift; over every cover `A4` map, exactly
one of its two lifts extends and the nonzero `H^1(m004;C2)` twist does not.

This proves that `2T` versus `A4` is literally a finite
`Spin(3)->SO(3)` lift torsor, and A6 selects its finite point. For each fixed
A4 map its pointed set is abstractly isomorphic to B1141's two-point lift
torsor, but R039 does not construct a canonical typed comparison between the
finite and semilinear geometric problems; no preferred target framing among
the 24 representative maps is claimed.

Requested fence: do not call the abstract pointed-set bijection a
tangent/internal/4d spin intertwiner. R021's finite-to-geometric comparison
and R034's physical maps remain unearned; the finite quotient and geometric
holonomy are not identified merely because each problem has an
extension-selected point.

Primary artifacts:

- `certificates/r039_a4_2t_lift_torsor/a4_2t_lift_torsor.py`
- `certificates/r039_a4_2t_lift_torsor/source_snapshot.json`
- `memos/A4_2T_LIFT_TORSOR.md`
