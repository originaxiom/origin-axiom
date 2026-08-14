"""B900 locks: the exact frame 1-cocycle (root-indexed blocks, diagonal action)."""
import json
import os

import sympy as sp

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B900_frame_cocycle")


def _res():
    with open(os.path.join(ARC, "results.json")) as f:
        return json.load(f)


def test_all_four_label_cubics_have_a_root_in_K():
    rho, x = sp.symbols("rho x")
    MU = 500716339200*rho**3 - 2075673600*rho**2 - 4769856*rho + 2197
    r0 = sp.RootOf(MU, 0)
    cubics = [
        2197*x**3 - 22110326784*x - 21334764552192,
        2197*x**3 - 5527581696*x + 2666845569024,
        2197*x**3 - 6963104474726400*x + 2923811689117777920000,
        2197*x**3 - 1740776118681600*x - 365476461139722240000,
    ]
    for F in cubics:
        assert sp.factor_list(F, x)[1][0][0].as_poly(x).degree() == 3  # irred /Q
        degs = sorted(sp.degree(f, x)
                      for f, _ in sp.factor_list(F, x, extension=r0)[1])
        assert degs == [1, 2]          # exactly one root in K


def test_index_maps_are_bijections_with_the_banked_twists():
    m = _res()["root_index_maps"]
    assert m["vac8"] == [0, 2, 1]
    assert m["oct8"] == [2, 0, 1]
    assert m["vac16"] == [2, 1, 0]
    assert m["oct16"] == [0, 1, 2]
    for k in m:
        assert sorted(m[k]) == [0, 1, 2]


def test_b896_frame1_float_perms_equal_the_exact_twists():
    m = _res()["root_index_maps"]
    b896 = json.load(open(os.path.join(
        os.path.dirname(ARC), "B896_s3_harmonics", "results.json")))
    a1 = b896["alignment"]["1"]
    assert a1["singlet_perm"] == m["vac8"]
    assert a1["octet_perm"] == m["oct8"]
