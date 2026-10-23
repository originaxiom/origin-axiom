"""B1741 -- tau from the thread rule, the line free (P-347), sealed acd2fec77, PROVED as sealed for its question (P1, P2,
R1-R3 hold; P2c, R4-R7, P3, P4 fail; C1, C2 hold).  Live: the best six-row's chi2 recomputed from its stored census row
and the pinned data (14.93, at the apex 3.4 + 2.993i on (2/5, 9/10), L_max, (S~, S, S), c = 3).  Stored: the cells and
fractions.  Seal: the hashes."""
import hashlib, json, math, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1741_tau_from_the_thread_rule_the_line_free"
ROOT = A.parents[1]


def _c():
    return json.loads((A / "verification" / "comparison.json").read_text(encoding="utf-8"))


def test_the_cells_stored():
    c = _c(); k = c["cells"]
    assert k["P1_chi2_six_below_16.75_seat"] and k["P2_chi2_six_specific_seat"] and k["R1_six_within_2_seat"]
    assert k["R2_six_specific_seat"] and k["R3_six_specific_cov"] and k["C1_control"] and k["C2_control_chi2_reproduces_B1735"]
    assert not (k["P2c_chi2_six_specific_cov"] or k["R4_six_specific_free"] or k["R5_nine_specific_seat"] or k["P3_chi2_nine_below_21.67_seat"] or k["P4_chi2_nine_below_21.67_SM_reading"])
    assert abs(c["chi2"]["six|seat"]["min"] - 14.93) < 0.01 and c["chi2"]["six|seat"]["fraction_mean"] < 0.0065
    assert c["seeds"] == list(range(1741, 1761)) and c["points"] == 19950


def test_the_best_row_live():
    d = json.loads((ROOT / "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))["masses_GeV"]
    v, s = d["value"], d["sigma"]
    pr = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
    T = np.log([v[a] / v[b] for a, b in pr]); sg = np.array([math.sqrt((s[a] / v[a]) ** 2 + (s[b] / v[b]) ** 2 + 0.01) for a, b in pr])
    b6 = _c()["best_six"]["seat"]; assert b6["line"] == 153 and abs(b6["Im_tau"] - 2.993325909) < 1e-6 and b6["Re_tau"] == 3.4
    for l in (A / "verification" / "census.jsonl").read_text(encoding="utf-8").splitlines():
        r = json.loads(l)
        if r["line"] == 153 and r["Re_tau"] == 3.4 and abs(r["Im_tau"] - 2.993325909) < 1e-6: break
    six = np.log(r["up|L_max|St"] + r["down|L_max|S"] + r["lep|L_max|S"]) + np.array([0, 0, 0, 0, math.log(3), -math.log(3)])
    assert abs(float((((six - T) / sg) ** 2).sum()) - 14.93) < 0.01


def test_the_seal():
    h = (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    for name in ("census.py", "compare.py"):
        assert hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest() in h
