"""B1755 -- the six on the lines of order 13, 14, 15 and 20, sealed 2d6681208, PROVED as sealed for its question (D, the
composite decisive cell, holds; P1, C1, C2 hold).  Live: the best six-row's chi2 on order 15 (5.3303 at 0.5 + 3.0619i on
line 236 = (2/5, 14/15), L_max, (S~, S, S), c = 3) and on order 20 (10.8856 at 0.6053 + 3.0259i on line 365 = (2/5, 7/20))
recomputed from the stored census rows and pinned data, plus the per-line alpha = 2/5 vs unit-twist check.  Seal: the hashes."""
import hashlib, json, math, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1755_the_six_on_the_lines_of_order_13_to_20"
ROOT = A.parents[1]


def _c():
    return json.loads((A / "verification" / "comparison.json").read_text(encoding="utf-8"))


def test_the_cells_stored():
    c = _c(); k = c["cells"]
    assert k["D_DECISIVE_specific_on_15_and_20_at_0.1pc_and_not_on_13_nor_14_at_1pc"]
    assert k["P1_chi2_six_below_16.75_on_15_and_20"] and k["C1_control"] and k["C2_control_chi2_reproduces_B1735"]
    assert k["readout_15_and_20_specific_at_1pc"] and k["readout_15_alone_at_0.1pc"]
    assert not (k["readout_20_alone_at_0.1pc"] or k["readout_13_specific_at_1pc"] or k["readout_14_specific_at_1pc"] or k["readout_nine_below_21.67_on_15_and_20"])
    assert abs(c["chi2"]["15+20"]["six|seat"]["min"] - 5.3303255) < 1e-5 and c["chi2"]["15+20"]["six|seat"]["hits"] == 78
    assert abs(c["chi2"]["15"]["six|seat"]["min"] - 5.3303255) < 1e-5 and c["chi2"]["15"]["six|seat"]["hits"] == 30
    assert abs(c["chi2"]["20"]["six|seat"]["min"] - 10.8855960) < 1e-5 and c["chi2"]["20"]["six|seat"]["hits"] == 243
    assert c["chi2"]["13"]["six|seat"]["fraction_mean"] > 0.049 and c["chi2"]["14"]["six|seat"]["fraction_mean"] > 0.42
    assert c["seeds"] == list(range(1809, 1829)) and c["apexes"] == 125 and c["counts"] == {"13": 84, "14": 72, "15": 96, "20": 144}
    pl = c["readout_per_line"]
    below = [v for v in pl.values() if v["chi2_six_seat"] < 16.75]
    assert len(below) == 8 and all(v["alpha"] == "2/5" for v in below)
    assert min(v["chi2_six_seat"] for v in pl.values() if v["order"] == 15 and v["alpha"] in ("1/15", "4/15")) > 750.0


def test_the_best_rows_live():
    d = json.loads((ROOT / "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))["masses_GeV"]
    v, s = d["value"], d["sigma"]
    pr = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
    T = np.log([v[a] / v[b] for a, b in pr]); sg = np.array([math.sqrt((s[a] / v[a]) ** 2 + (s[b] / v[b]) ** 2 + 0.01) for a, b in pr])
    r15 = r20 = None
    for l in (A / "verification" / "census.jsonl").read_text(encoding="utf-8").splitlines():
        q = json.loads(l)
        if q["line"] == 236 and abs(q["Re_tau"] - 0.5) < 1e-6 and abs(q["Im_tau"] - 3.0618621785) < 1e-6: r15 = q
        if q["line"] == 365 and abs(q["Re_tau"] - 0.6053) < 1e-3 and abs(q["Im_tau"] - 3.0259) < 1e-3: r20 = q
        if r15 is not None and r20 is not None: break
    assert r15 is not None and r20 is not None
    six15 = np.log(r15["up|L_max|St"] + r15["down|L_max|S"] + r15["lep|L_max|S"]) + np.array([0, 0, 0, 0, math.log(3), -math.log(3)])
    six20 = np.log(r20["up|L_max|St"] + r20["down|L_max|S"] + r20["lep|L_max|S"]) + np.array([0, 0, 0, 0, math.log(3), -math.log(3)])
    assert abs(float((((six15 - T) / sg) ** 2).sum()) - 5.3303255) < 1e-5
    assert abs(float((((six20 - T) / sg) ** 2).sum()) - 10.8855960) < 1e-5


def test_the_seal():
    h = (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    for name in ("census.py", "compare.py"):
        assert hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest() in h
