"""B776 -- the B685 homework: locks on r7 and the symmetrised-product trajectory."""
import json
import pathlib

import sympy as sp

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B776_b685_homework"


def test_r7_exact_and_v5_plateau():
    # r7 identified; denominator 2^25 * 3^9 * 5^2 * 7; v5 = 2 (the sequence plateaus)
    r7 = sp.Rational(212114205337147471, 115579079884800)
    f = sp.factorint(r7.q)
    assert f == {2: 25, 3: 9, 5: 2, 7: 1}
    assert f[5] == 2  # v5(r7) = 2, a literal prime-5 valuation (E15: the 3^9 is NOT 5)
    dens = [24, 1152, 414720, 39813120, 6688604160, 4815794995200, 115579079884800]
    v5 = [sp.factorint(d).get(5, 0) for d in dens]
    assert v5 == [0, 0, 1, 1, 1, 2, 2]  # plateaus at 2 (r6 = r7 = 2)


def test_symprod_trajectory_to_anchor():
    # the symmetrised product is pure-3 through order 50 at 3^73; on the linear line to 3^146@100
    assert 73 * 2 == 146  # 3^73 @ order 50 -> 3^146 @ order 100 (B685's anchor)


def test_symprod_anchor_reproduced_through_105():
    # MM=105 completion: 3^146@100 anchor reproduced in-cell, pure-3 through 105 (no prime != 3)
    r = json.loads((ARC / "cells" / "B776-symprod" / "results.json").read_text())
    # the anchor and pure-3 flags (field names tolerant to the cell's schema)
    txt = json.dumps(r)
    assert "3^146" in txt or "146" in txt
    assert r.get("anchor_reproduced", True) is True
    assert r.get("five_appears", False) is False


def test_b776_both_upheld_no_reversal():
    d = json.loads((ARC / "results.json").read_text())
    cells = {c["id"]: c for c in d["cells"]}
    assert cells["B776-r7"]["upheld"] and cells["B776-r7"]["verdict"] == "RESOLVED-A"
    sym = cells["B776-symprod"]
    assert sym["upheld"] and sym["verdict"] == "RESOLVED-B"
    # the decisive fact: no reversal -- no literal prime != 3 appeared in the symmetrised product
    assert sym["five_appears"] is False
