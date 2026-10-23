"""B1735 -- the precision bar on the two-ingredient censuses (post hoc, labelled; PROVED as computed).  Live: the minimum
chi2_six over B1726's 47 880 rows under the seat's menu (3.0946, at the order-10 line (2/5, 1/10), tau = 0.35 + 3.05i)
and over B1734's 380 rows (42.31), from the committed censuses through calib_chi2's own features.  Stored: the
calibration fractions, W138's labelled menu reproduced (3.365%), the control's exact recomputation."""
import importlib.util, json, pathlib, sys
import numpy as np
V = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1735_the_precision_bar_on_the_two_ingredient_censuses" / "verification"


def _calib():
    sys.path.insert(0, str(V))
    spec = importlib.util.spec_from_file_location("b1735_calib", V / "calib_chi2.py"); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_the_chi2_minima_live():
    c = _calib()
    for name, want in (("B1726", 3.0945633), ("B1734", 42.3106320)):
        mod = c.check.mod(name); F = c.features(mod, "seat")
        got = float(c.min_chi2(F, mod.arrays()["T6"][None, :])[0])
        assert abs(got - want) < 1e-6, (name, got)


def test_the_stored_cells():
    d = json.loads((V / "calib_chi2.json").read_text(encoding="utf-8"))
    assert d["B1726"]["seat"]["chi2_six_min"] < 16.75 and d["B1726"]["seat"]["fraction_mean"] < 0.001
    assert d["B1726"]["covfree"]["fraction_mean"] < 0.011 and d["B1734"]["seat"]["chi2_six_min"] > 40
    assert d["B1726"]["chi2_nine_seat"]["chi2_nine_min"] > 100 and d["B1734"]["chi2_nine_seat"]["chi2_nine_min"] > 400
    a = json.loads((V / "check.json").read_text(encoding="utf-8"))
    assert abs(a["B1726"]["covfree_six"]["mean"] - 0.03365) < 1e-9 and abs(a["B1726"]["covfree_six"]["best_factor"] - 1.2016458) < 1e-6
    k = json.loads((V / "control.json").read_text(encoding="utf-8"))
    assert k["fresh_vs_stored_max_abs_log"] == 0.0 and abs(k["chi2_six"] - 3.0945633) < 1e-6 and k["line"] == "2/5,1/10"
    assert max(abs(np.array(k["pulls"]))) < 1.32 and min(k["ckm_model_over_measured"]) > 4
