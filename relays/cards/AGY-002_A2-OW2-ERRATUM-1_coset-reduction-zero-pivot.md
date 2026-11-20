# Erratum 1 to Card `A2-OW2` — `coset_affine_reduction` Zero-Pivot Guard for Coset `S` (`0 of 19`)

## Disclosed Bug in Sealed `v1` (`2a84d5d24`)

In sealed `relays/a2_ow2/verify_a2_ow2.py`, `coset_affine_reduction(gamma, N)` swapped `r0` and `r1` when `abs(r0[0]) < abs(r1[0])` without looping back to check `r1[0] == 0`, triggering `ZeroDivisionError` on coset `S = (0, -1, 1, 0)` where `N * a = 0` (`v1` raised before producing any output file).

## Exact Fix for Companion `v2` (`relays/a2_ow2_v2/verify_a2_ow2_v2.py`)

- Leave `relays/a2_ow2/` completely untouched (`verify_a2_ow2.py` and `SCRIPT_SHA256.txt` preserved as sealed).
- Add `continue` immediately after the swap `if abs(r0[0]) < abs(r1[0]): r0, r1 = [-r1[0], -r1[1]], r0; continue` inside `coset_affine_reduction`, and use raw docstrings `r"""` to eliminate backslash syntax warnings.
- All mathematical definitions, tasks (`OW2-A` through `OW2-E`), and pass bars of Card `A2-OW2` (`d19ced577`) remain completely unchanged. `0 of 19.`
