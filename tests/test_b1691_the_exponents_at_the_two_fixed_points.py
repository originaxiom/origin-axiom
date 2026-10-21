"""B1691 -- the exponents at the two fixed points (P-227, part 1). Live: the exact identities (R.R = 0, R.DR = 0,
R.D2R = -DR.DR), the Wronskian -(i/8) eta^9, the cusp exponents of a weight-7/2 section (m2/m3 ~ |q|^(1/2),
m1/m3 ~ Im tau |q|), the f2 = 0 stratum (m1 = 0), the control (a constant direction: no 2-3 hierarchy), and W72's h as
eta^6 R; the bite: with B1654's q read as e^{2 pi i tau} instead of the nome the m1 exponent moves to 3/2. Stored: the
census to weight 23/2 at the cusp and at omega."""
import importlib.util, io, contextlib, json, pathlib, sys
from fractions import Fraction as F
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
sys.path.insert(0, str(A))


def _m():
    spec = importlib.util.spec_from_file_location("the_exponents_lock", A / "the_exponents.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


def test_identities_and_the_cusp_live_with_the_bite():
    m = _m()
    c1 = m.out["C1"]
    assert c1["R.R_identically_0"] and c1["R.DR_identically_0"] and c1["R.D2R_plus_DR.DR_identically_0"]
    assert c1["wronskian_over_8eta9_constant"] and c1["wronskian_over_8eta9"] == ["0", "-1/64"]
    a, used = m.section(2, 5)                                   # weight 7/2: E4 R and D2R
    e = m.cusp_exps(a)
    assert 2 in used and e["m2/m3_exponent_in_|q|"] == "1/2" and e["m1/m3_exponent_in_|q|_times_Im_tau"] == "1"
    z, _ = m.section(4, 5, drop=(2,))
    assert m.cusp_exps(z)["m1/m3_exponent_in_|q|_times_Im_tau"] is None    # no D2R component: m1 = 0
    const = m.cusp_exps([m.S.c(3), m.S.c(-2), m.S.c(5)])
    assert const["m2/m3_exponent_in_|q|"] == "0" and const["m1/m3_exponent_in_|q|_times_Im_tau"] == "1/2"
    o = e["orders_x"]                                           # the bite: D read with q = e^{2 pi i tau}
    assert F(2 * (8 + o[1]) - o[3], 16) == F(3, 2) != F(e["m1/m3_exponent_in_|q|_times_Im_tau"])
    assert m.out["C4_h_is_eta6_R"]["equal_to_the_seats"] and m.out["C4_h_is_eta6_R"]["h.h_identically_0"]


def test_the_census_stored():
    d = json.loads((A / "the_exponents.json").read_text(encoding="utf-8"))
    for k in ("7/2", "15/2", "19/2", "23/2"):
        for s in ("seed1", "seed2"):
            r = d["C2_cusp"][k][s]
            assert (r["m2/m3_exponent_in_|q|"], r["m1/m3_exponent_in_|q|_times_Im_tau"]) == ("1/2", "1")
        sl = d["C2b_cusp_direct"][k]
        assert sl["m2/m3_slope_in_|q|"] == [0.5, 0.5] and 0.94 < sl["m1/m3_slope_in_|q|_with_D_law"][0] < 0.96
    w = d["C3_omega"]
    assert w["7/2"]["seed1"]["slope_m2/m3_in_eps"] == [1.0, 1.0, 1.0] and w["11/2"]["seed1"]["slope_m2/m3_in_eps"] == [2.0, 2.0, 2.0]
    assert w["15/2"]["seed1"]["m2/m3_at_omega"].startswith("0.5") and w["23/2"]["seed1"]["slope_lift_factor_in_eps"] == [2.0, 2.0, 2.0]


def test_the_coefficients_are_free_addendum():
    d = json.loads((A / "the_coefficients_are_free.json").read_text(encoding="utf-8"))
    assert d["distinct"] and abs(d["pole_t"][0] + 5 / 288) < 1e-15 and abs(d["zero_t"][0] + 1 / 48) < 1e-15
    assert (d["r"], d["r2"], d["D2R.D2R_x2"], d["DR.DR_x2"]) == (["-1/2", "0"], ["-1/96", "0"], ["-5/576", "0"], ["1/4", "0"])
    assert abs(d["weight_3/2_m2/m3_over_|q|^(1/2)"] - 18) < 1e-12


def test_the_principles_points_addendum():
    d = json.loads((A / "the_principles_points.json").read_text(encoding="utf-8"))
    assert abs(d["m2/m3_at"]["omega"] - 0.5) < 1e-12 and abs(d["m2/m3_at"]["i"] - 0.5) < 1e-12
    lo, hi = d["on_LR_geodesic_min_max"]; assert 0.29 < lo < 0.30 and 0.49 < hi <= 0.5 + 1e-12
    need = d["Im_tau_needed_for_B1693s_values"]
    assert all(y > 5 ** 0.5 / 2 for y in need.values()) and need["up m_c/m_t"] > need["down m_s/m_b"] > need["lepton m_mu/m_tau"]


def test_the_correction_the_lift_at_finite_L():
    d = json.loads((A / "correction" / "the_lift_at_finite_L.json").read_text(encoding="utf-8"))
    for y, row in d.items():
        r = [row[L]["m1/m3"] for L in ("10", "40", "160", "640")]
        assert all(14 < r[i] / r[i + 1] < 18 for i in range(3))           # 1/L^2, not zero at finite L
        assert row["2.5"]["m1/m3"] > 1e-7
    assert abs(d["2.0"]["640"]["m2/m3"] - 0.0339) < 2e-4
