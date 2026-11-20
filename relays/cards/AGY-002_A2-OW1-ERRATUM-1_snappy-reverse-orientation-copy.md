# Erratum 1 to Card `A2-OW1` — `SnapPy` In-Place `reverse_orientation()` Copy Fix (`0 of 19`)

## Disclosed Bug in Sealed `v1` (`f6cfa58ba` / `60c969a76`)

In sealed `relays/a2_ow1/verify_a2_ow1.py`, `M.is_isometric_to(M.reverse_orientation())` passed `None` to `is_isometric_to` because `SnapPy`'s `Manifold.reverse_orientation()` mutates the manifold in-place and returns `None`, causing `is_amphichiral` to be caught as `None` (so the chiral-survivor summary lists were empty even though the printed `chern_simons` invariants directly showed chiral manifolds such as `b++LLLRLR`, `b+-LLLLLR`, `7_4`, `8_8`, `8_16`, and `8_21`).

## Exact Fix for Companion `v2` (`relays/a2_ow1_v2/verify_a2_ow1_v2.py`)

- Leave `relays/a2_ow1/` completely untouched.
- Compute amphichirality via `M_rev = M.copy(); M_rev.reverse_orientation(); is_amphi = bool(M.is_isometric_to(M_rev))` on all orientable hyperbolic bundles (`OW1-B`) and all hyperbolic prime knots (`OW1-C`).
- All mathematical definitions, census scope (`50` threads and `35` prime knots), and pass bars of Card `A2-OW1` (`62a106f14`) remain completely unchanged. `0 of 19.`
