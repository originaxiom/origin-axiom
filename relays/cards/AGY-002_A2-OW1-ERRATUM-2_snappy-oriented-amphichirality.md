# Erratum 2 to Card `A2-OW1` — `SnapPy` Unoriented `is_isometric_to` Catch (`0 of 19`)

## Disclosed Bug in Sealed `v2` (`63d5f6649` / `759796baa`)

In sealed `relays/a2_ow1_v2/verify_a2_ow1_v2.py`, `M.is_isometric_to(M_rev)` returned `True` for every manifold because `SnapPy`'s `is_isometric_to` checks unoriented isometry rather than orientation-preserving isometry (so every manifold is trivially unorientedly isometric to its own orientation reversal, falsely marking chiral manifolds with nonzero Chern-Simons invariant such as `7_4`, `8_21`, `b++LLLRLR`, and `b+-LLLLLR` as amphichiral).

## Exact Fix for Authoritative `v3` (`relays/a2_ow1_v3/verify_a2_ow1_v3.py`)

- Leave `relays/a2_ow1/` and `relays/a2_ow1_v2/` completely untouched.
- Determine amphichirality via both `M.symmetry_group().is_amphicheiral()` and direct orientation-reversing self-isometry check `any(iso.cusp_maps()[0].det() < 0 for iso in M.is_isometric_to(M, return_isometries=True))`, asserting exact agreement (`0` discrepancies across all orientable hyperbolic bundles and hyperbolic prime knots).
- All mathematical definitions and bars of Card `A2-OW1` (`62a106f14`) remain completely unchanged. `0 of 19.`
