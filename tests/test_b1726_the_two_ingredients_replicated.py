"""B1726 -- the two ingredients, replicated (P-293), sealed 8024632e1, PROVED as sealed for its question (R1-R5 hold, R6 and
R7 fail as expected, C1 holds). Live: the best six- and nine-rows re-derived from their stored census rows and the pinned
data. Stored: the cells, the fractions, the control. Seal: the instruments' hashes and the census's."""
import hashlib, json, math, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1726_the_two_ingredients_replicated"
ROOT = A.parents[1]
CENSUS_SHA = "d67432f0dc252e911514f211eb29844fd0bfcc5a270c00188312607435b0478d"


def _stored():
    return json.loads((A / "verification" / "comparison.json").read_text(encoding="utf-8"))


def test_the_cells_stored():
    c = _stored(); k = c["cells"]
    assert k["R1_six_within_2_seat"] and k["R2_six_specific_seat"] and k["R3_six_specific_cov"] and k["R4_six_specific_free"]
    assert k["R5_nine_specific_seat"] and not k["R6_J_within_3_at_best_nine_seat"] and not k["R7_D_within_3_sigma_at_best_six_seat"]
    assert k["C1_control"] and c["points"] == 23940 and c["rows"] == 47880 and c["seeds"] == list(range(1726, 1746))
    m = c["fraction_as_good_mean"]
    assert abs(m["six|seat"] - 0.0011875) < 1e-9 and abs(m["six|cov"] - 0.0041) < 1e-9 and abs(m["six|free"] - 0.0092375) < 1e-9
    assert abs(m["nine|seat"] - 0.0057875) < 1e-9 and abs(m["nine|cov"] - 0.016625) < 1e-9
    per = c["fraction_as_good_per_seed"]
    assert sum(per[s]["six|seat"] > 0.01 for s in per) == 0 and sum(per[s]["six|free"] > 0.01 for s in per) == 5
    assert sum(per[s]["nine|cov"] > 0.01 for s in per) == 20
    assert c["control"]["against_B1725"] < 1e-9 and c["control"]["T_covariance"] < 1e-6


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
        assert abs(math.exp(six[4] + six[3] - six[2] - six[5]) - b["D"]) < 1e-9


def test_the_seal():
    hashes = (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    for name in ("census.py", "compare.py"):
        assert hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest() in hashes
    assert hashlib.sha256((A / "verification" / "census.jsonl").read_bytes()).hexdigest() == CENSUS_SHA
