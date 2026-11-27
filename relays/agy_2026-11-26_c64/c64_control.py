#!/usr/bin/env python3
"""Failing control for Card AGY-C64 (door rule D3: exits 1 with no traceback; 0 of 19).

Imports the sealed AGY-C64 producer module beside this file and runs the exact Z[x]
sector-halving classifier with ONE deliberate mathematical perturbation: the whole's
Category-(a) factor x(x^2 - 9) is replaced by x(x^2 - 4) (q9_const = 4 instead of 9)
across (3, 3, 3) mod 27 and all 18 halving orbits discovered at mod 81.

Exit codes (per P-885 / rerun.py):
  1  control fails as it must: the perturbed run completes cleanly with no crash and
     the decisive Category-(a) counts fail to come out (0 != 6 at mod 81; 'c' != 'a' at mod 27);
  0  control did not fail (decisive Category-(a) counts still came out under q9_const = 4);
  3  control invalid (unexpected exception or incomplete run; a crash never counts as failing).
"""

import os as _os
import sys as _sys
import traceback as _tb


def _crash(et, ev, tb):
    _tb.print_exception(et, ev, tb)
    print("CONTROL INVALID: unexpected exception; a crash is not a failing control")
    _sys.stdout.flush()
    _os._exit(3)


_sys.excepthook = _crash

import ast
import pathlib
import sys

sys.dont_write_bytecode = True

import c64_b2017_mod81_census_b2016_subgroups_mod243_ceiling_and_cusp_producer as prod


MOD81_HALVING_REPS = [
    (3, 9, 9), (9, 9, 24), (9, 9, 30),
    (6, 9, 9), (9, 9, 21), (9, 9, 33),
    (9, 9, 12), (9, 9, 15), (9, 9, 39),
    (3, 3, 3), (3, 3, 30), (3, 3, 33),
    (3, 3, 15), (3, 3, 21), (3, 3, 42),
    (3, 3, 12), (3, 3, 24), (3, 3, 39),
]


def main():
    tree = ast.parse(pathlib.Path(__file__).read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            print("CONTROL INVALID: float or complex literal in control script")
            return 3

    sec27 = prod.build_orbit_and_sectors(27, (3, 3, 3))
    cat27_perturbed = prod.exact_charpolys_zz(sec27, q9_const=4)

    counts81_perturbed = {"a": 0, "a'": 0, "b": 0, "c": 0}
    for rep in MOD81_HALVING_REPS:
        sec81 = prod.build_orbit_and_sectors(81, rep)
        cat = prod.exact_charpolys_zz(sec81, q9_const=4)
        counts81_perturbed[cat] = counts81_perturbed.get(cat, 0) + 1

    # All 12 Category-(a') orbits have |Fix(C)| == 0 (independent of q9_const),
    # verifying the full classifier pipeline executed cleanly to completion.
    if counts81_perturbed["a'"] != 12 or sum(counts81_perturbed.values()) != 18:
        print(f"CONTROL INVALID: incomplete perturbed census counts={counts81_perturbed}")
        return 3

    print(
        f"CONTROL: q9_const=4 (x^2 - 4 in place of x^2 - 9) completed cleanly: "
        f"mod27_(3,3,3)={cat27_perturbed}, mod81_18_orbits={counts81_perturbed}"
    )
    if cat27_perturbed == "a" and counts81_perturbed["a"] == 6:
        print("CONTROL DID NOT FAIL: decisive Category-(a) counts still came out under q9_const=4")
        return 0

    print(
        "CONTROL FAILS: as it must, replacing x^2 - 9 with x^2 - 4 gives "
        f"mod-27 category {cat27_perturbed!r} != 'a' and mod-81 Category-(a) count "
        f"{counts81_perturbed['a']} != 6"
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
