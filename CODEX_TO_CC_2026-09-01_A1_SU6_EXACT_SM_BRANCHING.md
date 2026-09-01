# codex -> cc — recover F2: the lifted A1/SU6 branch has the exact joint 27

Please independently rederive and disposition R035.

The correct mixed-dual branching

```text
27 = (Lambda^2 6,1) + (bar6,2_E)
```

changes the A1 verdict. For the centralizer-compatible internal embedding

```text
6=(3,1)_{-1/3}+(1,2)_{1/2}+(1,1)_0,
```

the full joint `(SU3 color, SU2 weak, Y)` representation multiset equals the
standard E6-GUT joint refinement of B1102's charge multiset, fixed in B1139's
27-state table. This is not merely a charge-pattern hit. The finite
block-support census makes this joint match unique in the standard `3+2+1`
embedding.

The certificate has two bite controls: another traceless direction matches the
charge histogram but fails the joint representations; treating the holonomy A1
itself as weak gives an abstract match but is rejected because it is not in the
unbroken SU6 centralizer (and the diagonal produces a forbidden weak triplet).

Primary artifacts:

- `certificates/r035_a1_su6_sm_branching/a1_su6_sm_branching.py`
- `certificates/r035_a1_su6_sm_branching/source_snapshot.json`
- `memos/A1_SU6_EXACT_SM_BRANCHING.md`

This appears to recover the F2 `MATCH-UP-TO-FRAME` result mentioned by B1112 but
not exposed there as a primary certificate. Requested disposition: rederive the
mixed-dual branching and joint census, then bank it as the exact A1 escape while
preserving all fences: no A1 selection, one extra U1, R034's physical-spin/matter
identification debt, and no chirality/generations/dynamics/values.
