"""B1734 -- the thread rule with the two ingredients (P-312), sealed afc60475c, PROVED as sealed for its question (R1-R4
hold, R5-R7 fail, C1 holds). Live: the best six-row re-derived from its stored census row and the pinned data, and its
double ratio D = 9 exactly (an order-5 line). Stored: the cells, the fractions, the control. Seal: the hashes."""
import hashlib, json, math, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1734_the_thread_rule_with_the_two_ingredients"
ROOT = A.parents[1]


def _stored():
    return json.loads((A / "verification" / "comparison.json").read_text(encoding="utf-8"))


def test_the_cells_stored():
    c = _stored(); k = c["cells"]
    assert k["R1_six_within_2_seat"] and k["R2_six_specific_seat"] and k["R3_six_specific_cov"] and k["R4_six_specific_free"]
    assert not k["R5_nine_specific_seat"] and not k["R6_J_within_3_at_best_nine_seat"] and not k["R7_D_within_3_sigma_at_best_six_seat"]
    assert k["C1_control"] and c["points"] == 190 and c["rows"] == 380 and c["seeds"] == list(range(1734, 1754))
    m = c["fraction_as_good_mean"]
    assert m["six|seat"] < 0.002 and m["six|cov"] < 0.006 and m["six|free"] < 0.007 and m["nine|seat"] > 0.06
    per = c["fraction_as_good_per_seed"]
    assert all(per[s]["six|seat"] <= 0.01 and per[s]["six|cov"] <= 0.01 for s in per)
    assert abs(c["best_six"]["seat"]["best_factor"] - 1.614) < 1e-3 and c["best_six"]["seat"]["thread"] == "LLLLLRR"


def test_the_best_six_row_live():
    v = json.loads((ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))["masses_GeV"]["value"]
    t6 = np.log([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]])
    b = _stored()["best_six"]["seat"]
    rows = json.loads((A / "verification" / "census.json").read_text(encoding="utf-8"))["rows"]
    r = [x for x in rows if x["word"] == b["thread"] and x["a"] + "," + x["b"] == b["line"]][0]
    h = b["horocycle"]; ru, rd, rl = b["readings"]
    six = np.log(r["up|%s|%s" % (h, ru)] + r["down|%s|%s" % (h, rd)] + r["lep|%s|%s" % (h, rl)])
    six[4] += math.log(3.0); six[5] -= math.log(3.0)
    assert abs(math.exp(np.abs(six - t6).max()) - b["best_factor"]) < 1e-9
    assert abs(math.exp(six[4] + six[3] - six[2] - six[5]) - 9.0) < 1e-9 and r["order"] == 5


def test_the_seal():
    hashes = (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    for name in ("census.py", "compare.py"):
        assert hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest() in hashes
