"""B1697 -- the scan for misses. Live: the unit-free weight-7/2 section a0 = D2R - E4 R/48 is holomorphic at the cusp while R
and DR carry the unit (the bite: t = 0, i.e. D2R alone, keeps it); LR's sign-fixed lines are the four order-5 points.
Stored: a0's m2/m3 -> 1/2 along tau = iy; the candidate taus; the silver cusp shape."""
import importlib.util, io, contextlib, json, pathlib
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1697_the_scan_for_misses" / "verification"


def _m():
    spec = importlib.util.spec_from_file_location("b1697_scan", A / "the_scan.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


def test_the_unit_free_section_and_the_order5_lines_live():
    m = _m(); o = m.out
    assert o["a0_holomorphic_at_the_cusp"] and o["a0_orders_on_(e_i,e_j,e_k)"] == [1, 3, 3]
    assert min(o["R_orders"]) < 0 and min(o["DR_orders"]) < 0
    d2r = m.B[2]; assert min(c.ord() for c in d2r) < 0                      # the bite: D2R alone keeps the unit
    assert o["det_LR_minus_I"] == -1 and o["det_LR_plus_I"] == 5 and o["lines_fixed_by_LR"] == [[0, 0]]
    assert o["order5_lines_fixed_up_to_sign"] == [["1/5", "2/5"], ["2/5", "4/5"], ["3/5", "1/5"], ["4/5", "3/5"]]


def test_stored():
    d = json.loads((A / "the_scan.json").read_text(encoding="utf-8"))
    assert all(abs(v - 0.5) < 0.02 for k, v in d["a0_m2/m3_along_i_y"].items() if float(k) >= 2)
    assert d["candidate_taus_m2/m3_large_L"]["omega"]["a0"] < 1e-30
    assert abs(d["cusp_shapes_snappy"]["LLRR"][1] - 0.5) < 1e-12
