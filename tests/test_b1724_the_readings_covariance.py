"""B1724 -- the readings' covariance (P-297), PROVED. Live: rho(T) on S's components is e^{i pi/4}(1 + R_{-90}); one T
comparison per reading (S and S~ covariant, S* not). Stored: every transformation's table, the Gamma(2) result, and the
consequences (every sealed calibration reproduced exactly; no verdict turns on S*). S* is covariant exactly under
Gamma^0(2) = <R, T^2>: it passes R, T^2 and S T^2 S and fails T, T^3, S and T S."""
import json, math, pathlib, sys, importlib.util
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1724_the_readings_covariance"


def _load(name):
    spec = importlib.util.spec_from_file_location("b1724_" + name, A / "verification" / (name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_mechanism_live():
    m = _load("covariance")
    a = m.part_a()
    assert a["third_tau_check"] < 1e-12 and a["M_is_e_ipi4_times_R_minus90"] < 1e-12
    assert all(abs(x - 0.125) < 1e-12 for x in a["phase_i_over_2pi"])
    assert [round(x, 9) for x in a["eigenphases_over_2pi"]] == [0.375, 0.875]


def test_one_T_comparison_live():
    m = _load("covariance")
    t = m.TAUS[0]; a, b = m.LINES[4]; L = m.L_col(t.imag)
    d = m.compare(m.frame(t, a, b, L), m.frame(t + 1, a, b - a, L))
    assert d["S"] < 1e-6 and d["St"] < 1e-6 and d["conjS"] > 0.1
    assert d["ckm St|S"] < 1e-6 and d["ckm St|conjS"] > 1e-3


def test_the_tables_stored():
    s = json.loads((A / "verification" / "covariance.json").read_text(encoding="utf-8"))["summary"]
    for g in ("T^1", "T^2", "T^3", "S", "ST^2S", "TS", "R"):
        assert s[g]["S"] < 1e-6 and s[g]["St"] < 1e-6
        assert all(v < 1e-6 for k, v in s[g].items() if k.startswith("ckm") and "conjS" not in k)
    for g in ("T^1", "T^3", "S", "TS"):
        assert s[g]["conjS"] > 1.0
    for g in ("T^2", "ST^2S", "R"):
        assert s[g]["conjS"] < 1e-6 and all(v < 1e-6 for v in s[g].values())


def test_the_consequences_stored():
    c = json.loads((A / "verification" / "consequences.json").read_text(encoding="utf-8"))
    assert len(c) == 10 and all(v["reproduced"] for v in c.values())
    assert abs(c["B1720|masses"]["covariant_readings"]["fraction_fit_as_well"] - 0.01475) < 1e-9
    assert c["B1720|masses"]["covariant_readings"]["fraction_fit_as_well"] > 0.01           # T2 still fails
    for k, new in (("B1713|mixing", 1.174), ("B1720|mixing", 1.225), ("B1723|mixing", 1.851)):
        assert abs(c[k]["covariant_readings"]["best_factor"] - new) < 0.001
        assert c[k]["covariant_readings"]["fraction_fit_as_well"] > 0.01
    for k in ("B1712|masses", "B1713|masses", "B1720|masses", "B1723|masses"):
        assert abs(c[k]["covariant_readings"]["best_factor"] - c[k]["stored"]["best"]) < 1e-9 * c[k]["stored"]["best"]
