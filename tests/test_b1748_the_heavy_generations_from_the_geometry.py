"""B1748 -- the heavy generations from the geometry alone (P-362), sealed 3bf82d0ca, NEGATIVE as sealed for its question (R1, P1,
L2 hold; R2, P2, L1 fail; C1 holds).  Live: the best
row's chi2_heavy recomputed from its stored census row and the pinned data.  Stored: the cells and fractions.  Seal: the hashes."""
import hashlib, json, math, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1748_the_heavy_generations_from_the_geometry"
ROOT = A.parents[1]


def _c():
    return json.loads((A / "verification" / "comparison.json").read_text(encoding="utf-8"))


def test_the_cells_stored():
    c = _c(); k = c["cells"]
    assert k["R1_heavy_within_1.25_Lmax"] and k["P1_chi2_heavy_below_bar_Lmax"] and k["L2_Lmax_more_specific_than_L2"] and k["C1_control"]
    assert not (k["R2_coarse_specific_Lmax"] or k["P2_precision_specific_Lmax"] or k["L1_L2_misses_the_bar"])
    M, L = c["L_max"], c["L_2"]
    assert abs(M["min_chi2_heavy"] - 1.1636) < 1e-3 and abs(M["fraction_chi2_mean"] - 0.0154) < 1e-4 and M["rows_below_bar"] == 82
    assert abs(L["min_chi2_heavy"] - 3.1261) < 1e-3 and abs(L["fraction_chi2_mean"] - 0.0739) < 1e-4
    assert c["seeds"] == list(range(1748, 1768)) and c["rows"] == 26068 and abs(c["bar_chi2_4"] - 13.277) < 1e-9


def test_the_best_row_live():
    d = json.loads((ROOT / "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))["masses_GeV"]
    C = json.loads((ROOT / "frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json").read_text(encoding="utf-8"))["ckm_abs"]
    v, e = d["value"], d["sigma"]
    T = np.log([v["c"] / v["t"], v["s"] / v["b"], v["mu"] / v["tau"], C["value"][1][2]])
    rel = [math.hypot(e["c"] / v["c"], e["t"] / v["t"]), math.hypot(e["s"] / v["s"], e["b"] / v["b"]), math.hypot(e["mu"] / v["mu"], e["tau"] / v["tau"]), C["sigma"][1][2] / C["value"][1][2]]
    sg = np.sqrt(np.array(rel) ** 2 + 0.01)
    b = _c()["L_max"]["best_by_chi2"]; assert b["line"] == 88 and b["null line"] == "nbar" and b["lepton_factor"] == 3.0
    for l in (A / "verification" / "census.jsonl").read_text(encoding="utf-8").splitlines():
        r = json.loads(l)
        if r["line"] == b["line"] and r["Re_tau"] == b["Re_tau"] and r["Im_tau"] == b["Im_tau"]: break
    f = np.log(r["L_max|" + b["null line"]]); f[2] += math.log(b["lepton_factor"])
    assert abs(float((((f - T) / sg) ** 2).sum()) - b["chi2_heavy"]) < 1e-9


def test_the_seal():
    h = (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    for name in ("census.py", "compare.py"):
        assert hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest() in h
