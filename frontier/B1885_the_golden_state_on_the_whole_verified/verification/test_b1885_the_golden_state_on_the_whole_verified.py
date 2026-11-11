"""B1885 lock -- the golden state on the whole, the web seat's card verified on main.

What could fail: a check of the committed run other than main's own guess H6; the state not transforming with the character
when recomputed; the stored place not being a critical point, or failing the trace test; the series evaluated where its cut
is not negligible; the arc reading as a design, a selection or a value."""
import importlib.util
import json
import pathlib
from fractions import Fraction

import mpmath as mp
import pytest

HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
_dps = mp.mp.dps
spec = importlib.util.spec_from_file_location("golden_state_on_main_lock", HERE / "golden_state_on_main.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
mp.mp.dps = _dps                      # the script sets its own precision on import; other locks keep theirs
RES = json.loads((HERE / "golden_state_on_main.json").read_text(encoding="utf-8"))
H6 = "H6 main's point agrees with the one the lane reports to 1e-9"


def test_the_committed_run_has_32_checks_and_only_mains_own_guess_fails():
    checks = {k: v for k, v in RES.items() if isinstance(v, bool)}
    assert len(checks) == 32
    assert [k for k, v in checks.items() if not v] == [H6] == RES["failing"]
    run = (HERE / "golden_state_on_main_run.txt").read_text(encoding="utf-8")
    assert "CHECKS: 32, FAILING: 1" in run and "kept as failed" in run
    assert sum(1 for k in checks if k.startswith("A") and "(added)" in k) == 6          # the six added after the first run say so


def test_the_state_transforms_with_the_character_recomputed():
    with mp.workdps(20):
        F5 = m.Field(5)
        assert (F5.ea, F5.eb, F5.eps_norm) == (0, 1, -1) and abs(F5.R - mp.pi / (2 * mp.log((1 + mp.sqrt(5)) / 2))) < mp.mpf(10) ** -17
        f, fc = m.Form(F5, 300), m.Form(F5, 300, cosine=True)
        assert f.c[5] == -1 and f.c[2] == f.c[3] == f.c[7] == 0 and f.c[4] == f.c[9] == 1 and abs(f.c[11] - mp.mpf("-1.11318395792")) < mp.mpf(10) ** -11
        z = mp.mpc("0.137", "0.412")
        for g, chi in (((2, -1, 5, -2), -1), ((1, 0, 5, 1), 1)):
            assert abs(f(m.mob(g, z)) - chi * f(z)) < mp.mpf(10) ** -14 * abs(f(z))
        assert abs(fc(m.mob((2, -1, 5, -2), z)) + fc(z)) > mp.mpf(10) ** -3 * abs(fc(z))       # the control fails, as it must
        assert abs(f(-1 / (5 * z)) + f(z)) < mp.mpf(10) ** -14 * abs(f(z))                     # the sign under the dual involution is -1
        e1 = (2 + mp.mpc(0, 1)) / 5
        assert abs(f(e1)) < mp.mpf(10) ** -14 * abs(f(z))                                      # the forced zero at an elliptic point


def test_the_stored_place_is_a_critical_point_on_the_circle_and_passes_the_trace_test_recomputed():
    x0, y0 = mp.mpf(RES["level_5"]["z_star"][0]), mp.mpf(RES["level_5"]["z_star"][1])
    assert abs(x0 * x0 + y0 * y0 - mp.mpf(1) / 5) < mp.mpf(10) ** -15
    with mp.workdps(20):
        F5 = m.Field(5); f = m.Form(F5, 300)
        peak = f(mp.mpc(x0, y0)) ** 2
        gx = mp.diff(lambda x: f(mp.mpc(x, y0)) ** 2, x0); gy = mp.diff(lambda y: f(mp.mpc(x0, y)) ** 2, y0)
        assert abs(gx) / peak < mp.mpf(10) ** -9 and abs(gy) / peak < mp.mpf(10) ** -9
        hxx = mp.diff(lambda x: f(mp.mpc(x, y0)) ** 2, x0, 2); hyy = mp.diff(lambda y: f(mp.mpc(x0, y)) ** 2, y0, 2)
        want = -2 * (mp.mpf(1) / 4 + F5.R ** 2) / y0 ** 2
        assert hxx < 0 and hyy < 0 and abs((hxx + hyy) / peak - want) < mp.mpf(10) ** -6 * abs(want)
        # at the lane's reported point the gradient is far from zero: it is near the peak and is not the peak
        lx, ly = mp.mpf("0.251539778829130"), mp.mpf("0.369767144294671")
        gl = mp.sqrt(mp.diff(lambda x: f(mp.mpc(x, ly)) ** 2, lx) ** 2 + mp.diff(lambda y: f(mp.mpc(lx, y)) ** 2, ly) ** 2) / peak
        assert mp.mpf("5e-8") < gl < mp.mpf("3e-7")
        assert mp.mpf("1.4e-9") < abs(mp.mpc(lx, ly) - mp.mpc(x0, y0)) < mp.mpf("1.6e-9")


def test_the_series_refuses_a_height_where_its_cut_is_not_negligible():
    with mp.workdps(20):
        f = m.Form(m.Field(5), 60)
        f(mp.mpc("0.2", "0.4"))                                  # 34 terms are enough here
        with pytest.raises(ValueError):
            f(mp.mpc("0.1", "0.01"))                             # here 1353 would be needed: the first run's fault, now refused


def test_the_cell_and_where_the_character_forces_a_zero_by_hand():
    assert Fraction(1, 5) + Fraction(1, 20) == Fraction(1, 2) ** 2          # the two circles meet at a right angle
    assert Fraction(2, 5) ** 2 + Fraction(1, 5) ** 2 == Fraction(1, 5) and (Fraction(2, 5) - Fraction(1, 2)) ** 2 + Fraction(1, 5) ** 2 == Fraction(1, 20)
    order2 = lambda p: [d for d in range(1, p) if (d * d + 1) % p == 0]
    order3 = lambda p: [d for d in range(1, p) if (d * d + d + 1) % p == 0]
    assert order2(5) == [2, 3] and order3(5) == [] and order2(13) == [5, 8] and order3(13) == [3, 9] and order2(17) == [4, 13] and order3(17) == []
    assert [m.legendre(d, 5) for d in order2(5)] == [-1, -1] and [m.legendre(d, 13) for d in order2(13)] == [-1, -1]
    assert [m.legendre(d, 13) for d in order3(13)] == [1, 1] and [m.legendre(d, 17) for d in order2(17)] == [1, 1]
    rows = {(13, o, d): (c, float(v)) for o, d, c, v in RES["level_13"]["elliptic_points"]}
    rows.update({(17, o, d): (c, float(v)) for o, d, c, v in RES["level_17"]["elliptic_points"]})
    assert all(v < 1e-20 for (p, o, d), (c, v) in rows.items() if c == -1) and all(v > 1 for (p, o, d), (c, v) in rows.items() if c == 1)
    assert len(rows) == 6 and RES["level_5"]["cell"]["negative"] == 0 and RES["level_5"]["cell"]["positive"] == RES["level_5"]["cell"]["points"] > 10000


def test_the_arc_says_what_it_is_and_is_not():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("It selects nothing and derives no value", "It is not main's design", "\"Lowest\" and \"simple\" are not verified on main", "A grid is not a proof",
              "One clause of P-776 is no longer kept", "compared with no value of τ on record, and no frame is evaluated at it", "Main's own expectation H6 fails as written",
              "The place depends on the measure", "## Seen first", "## Disclosed", "0 of 19"):
        assert s in f, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1885" and v["claim_one_line"].endswith("0 of 19.") and v["weave_or_thread"].startswith("weave")
    assert "selects nothing" in v["claim_one_line"] and "not main's design" in v["claim_one_line"]
