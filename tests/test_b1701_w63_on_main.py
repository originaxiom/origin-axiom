"""B1701 -- W63 on main (P-246). Live: the half bound and m(e_k) = 1/2 at one axis point on main's triplet; on one tied
line the twisted coupling is exactly 0 : 1 : 1 and an untied unit is not. Stored: every one of the 864 tied rows is
0 : 1 : 1; the control."""
import importlib.util, io, contextlib, json, math, pathlib, sys
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1701_w63_on_main"


def _mod():
    argv = sys.argv; sys.argv = ["x"]
    spec = importlib.util.spec_from_file_location("b1701", A / "verification" / "w63_on_main.py")
    m = importlib.util.module_from_spec(spec)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(m)
    finally:
        sys.argv = argv
    return m


def test_live():
    m = _mod()
    R = m.Rvec(2.5j)
    assert abs(m.m_of(np.array([0, 0, 1], dtype=complex), R) - 0.5) < 1e-9
    from fractions import Fraction as Fr
    k = m.LINES.index((Fr(1, 2), Fr(0)))                                   # w = tau/2: p* = (1/2, 0), the unit j
    r = m.point((k, 0.5, 2.2))
    assert all(abs(r[key][0] - 1) < 1e-12 and r[key][1] < 1e-12 for key in r if "|" in key)
    r2 = m.point((k, 0.5, 2.2, "k"))
    assert all(abs(r2[key][0] - 1) > 0.05 for key in r2 if "|" in key)


def test_stored():
    d = json.loads((A / "verification" / "w63_on_main.json").read_text(encoding="utf-8"))
    assert len(d["b"]["lines"]) == 27 and len(d["b"]["rows"]) == 864
    assert d["b"]["max_abs_m2_over_m3_minus_1"] < 1e-14 and d["b"]["max_m1_over_m3"] < 1e-14
    assert d["c"]["min_abs_m2_over_m3_minus_1"] > 0.05 and d["c"]["min_m1_over_m3"] > 1e-5
    for row in d["a"].values():
        assert 0.5 - 1e-12 <= row["min_m_real"] < 0.5 + 1e-6 and row["max_m_isotropic"] < 1e-9
