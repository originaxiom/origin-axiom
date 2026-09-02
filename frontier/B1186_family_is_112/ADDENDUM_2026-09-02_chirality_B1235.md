# Addendum (2026-09-02) — `amphichirality_failures = []` tested nothing (B1235)

`verification/family_census.py:96` decides amphichirality by `M.is_isometric_to(W)` with W the mirror. SnapPy's
isometry test ignores orientation (`REPRODUCIBILITY.md:73`), so the field is vacuous: every manifold is isometric to
its mirror under it. The 112 membership count is unaffected. The proper test (`symmetry_group().is_amphicheiral()`)
gives **38 amphichiral / 74 chiral**, with 38 of the 74 chiral members CS-silent. Zero B1224 violations. The per-member
table is `frontier/B1235_two_seat_harvest/verification/chirality_112.json`; this arc's JSON is left as banked
(append-only), superseded on that field only.
