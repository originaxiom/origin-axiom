"""B1732 -- the two ingredients with the Higgs PF1-W fixes (P-307), sealed 65e6abfce, NEGATIVE as sealed for its question
(R1 holds; R2-R5 fail; R6 holds at a non-specific row; R7 fails; C1 holds). Live: the best six- and nine-rows re-derived
from their stored census rows and the pinned data. Stored: the cells, the fractions, the control. Seal: the hashes."""
import hashlib, json, math, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1732_the_two_ingredients_with_the_fixed_higgs"
ROOT = A.parents[1]
CENSUS_SHA = "26b660bbb6e1effc2be75835e3a5ccd74369ce9a2d5f33019277a5120d24b685"


def _stored():
    return json.loads((A / "verification" / "comparison.json").read_text(encoding="utf-8"))


def test_the_cells_stored():
    c = _stored(); k = c["cells"]
    assert k["R1_six_within_2_seat"] and not k["R2_six_specific_seat"] and not k["R3_six_specific_cov"]
    assert not k["R4_six_specific_free"] and not k["R5_nine_specific_seat"] and k["R6_J_within_3_at_best_nine_seat"]
    assert not k["R7_D_within_3_sigma_at_best_six_seat"] and k["C1_control"]
    assert c["points"] == 23940 and c["rows"] == 47880 and c["seeds"] == list(range(1732, 1752))
    m = c["fraction_as_good_mean"]
    assert abs(m["six|seat"] - 0.070625) < 1e-9 and abs(m["six|cov"] - 0.020825) < 1e-9 and abs(m["nine|seat"] - 0.3578) < 1e-9
    per = c["fraction_as_good_per_seed"]
    assert all(per[s]["six|seat"] > 0.01 and per[s]["six|cov"] > 0.01 for s in per)
    assert c["control"]["F6_invariant"] < 1e-10 and c["control"]["T_covariance"] < 1e-6 and c["control"]["against_B1725"] < 1e-9


def test_the_best_rows_live():
    v = json.loads((ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))["masses_GeV"]["value"]
    C = json.loads((ROOT / "frontier" / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json").read_text(encoding="utf-8"))["ckm_abs"]["value"]
    t6 = np.log([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]])
    t3 = np.log([C[0][1], C[1][2], C[0][2]])
    c = _stored(); want = {(b["line"], b["Re_tau"], b["Im_tau"]): b for b in (c["best_six"]["seat"], c["best_nine"]["seat"])}
    rows = {}
    for l in (A / "verification" / "census.jsonl").read_text(encoding="utf-8").splitlines():
        r = json.loads(l); key = (r["line"], r["Re_tau"], r["Im_tau"])
        if key in want: rows[key] = r
    assert len(rows) == 2
    for nine, b in ((False, c["best_six"]["seat"]), (True, c["best_nine"]["seat"])):
        r = rows[(b["line"], b["Re_tau"], b["Im_tau"])]; h = b["horocycle"]; ru, rd, rl = b["readings"]
        six = np.log(r["up|%s|%s" % (h, ru)] + r["down|%s|%s" % (h, rd)] + r["lep|%s|%s" % (h, rl)])
        six[4] += math.log(b["lepton_factor"]); six[5] -= math.log(b["lepton_factor"])
        err = np.abs(six - t6)
        if nine:
            err = np.concatenate([err, np.abs(np.log(r["ckm|%s|%s|%s" % (h, ru, rd)][:3]) - t3)])
            assert abs(r["ckm|%s|%s|%s" % (h, ru, rd)][3] - b["J"]) < 1e-15
        assert abs(math.exp(err.max()) - b["best_factor"]) < 1e-9


def test_the_seal():
    hashes = (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    for name in ("census.py", "compare.py"):
        assert hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest() in hashes
    assert hashlib.sha256((A / "verification" / "census.jsonl").read_bytes()).hexdigest() == CENSUS_SHA
