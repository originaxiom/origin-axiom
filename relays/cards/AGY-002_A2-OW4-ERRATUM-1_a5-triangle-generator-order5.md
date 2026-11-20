# Erratum 1 to `AGY-002_A2-OW4`: `A_5` Triangle Generator `b` Must Move Point `4`

- **Parent Card:** `relays/cards/AGY-002_A2-OW4_chiral-bowl-rung-selection-and-unique-4d-sakharov-gravity.md` (`def63a893`)
- **Affected Script:** `relays/a2_ow4/verify_a2_ow4.py` (`9ca94f852`, preserved untouched)
- **Cause:** In `build_triangle_group(5)`, both `a = (1, 0, 3, 2, 4)` and `b = (1, 2, 0, 3, 4)` fixed index `4`, so their product `ab` lay in `A_4` with order `3 != 5`, immediately caught by the pre-run generator assertion `perm_order(ab) == N`.
- **Fix in `v2` (`relays/a2_ow4_v2/verify_a2_ow4_v2.py`):** Replace `b` at `N = 5` by the `3`-cycle `(0, 2, 4, 3, 1)` (`1 -> 2 -> 4 -> 1`), so `ord(a) = 2`, `ord(b) = 3`, `ord(ab) = 5` (`0 -> 1 -> 3 -> 2 -> 4 -> 0`), generating the full `60`-element group `A_5`. Zero change to any Card `A2-OW4` hypothesis or pass bar. `0 of 19.`
