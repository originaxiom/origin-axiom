"""B1753 -- the six on the five-ality lines, sealed 33b197340, PROVED as sealed for its question (P2, the
decisive cell, holds; P1, C1, C2 hold).  Live: the best six-row's chi2 recomputed from its stored census row and the pinned
data (2.739 at 0.3333 + 3.0368i on (2/5, 1/10), L_max, (S~, S, S), c = 3).  Stored: the cells and fractions.  Seal: the hashes."""
import hashlib, json, math, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1753_the_six_on_the_five_ality_lines"
ROOT = A.parents[1]


def _c():
    return json.loads((A / "verification" / "comparison.json").read_text(encoding="utf-8"))


def test_the_cells_stored():
    c = _c(); k = c["cells"]
    assert k["P2_DECISIVE_chi2_six_specific_seat_0.1pc"] and k["P1_chi2_six_below_16.75_seat"] and k["C1_control"] and k["C2_control_chi2_reproduces_B1735"]
    assert not (k["readout_P3_chi2_nine_below_21.67_seat"] or k["readout_P4_chi2_nine_below_21.67_SM_reading"])
    assert abs(c["chi2"]["six|seat"]["min"] - 2.7390) < 1e-3 and c["chi2"]["six|seat"]["fraction_mean"] < 0.0001
    assert c["seeds"] == list(range(1789, 1809)) and c["points"] == 10704 and c["rows"] == 21408


def test_the_best_row_live():
    d = json.loads((ROOT / "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))["masses_GeV"]
    v, s = d["value"], d["sigma"]
    pr = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
    T = np.log([v[a] / v[b] for a, b in pr]); sg = np.array([math.sqrt((s[a] / v[a]) ** 2 + (s[b] / v[b]) ** 2 + 0.01) for a, b in pr])
    r = None
    for l in (A / "verification" / "census.jsonl").read_text(encoding="utf-8").splitlines():
        q = json.loads(l)
        if q["line"] == 149 and abs(q["Re_tau"] - 0.333333333) < 1e-6 and abs(q["Im_tau"] - 3.0368112) < 1e-6: r = q; break
    assert r is not None
    six = np.log(r["up|L_max|St"] + r["down|L_max|S"] + r["lep|L_max|S"]) + np.array([0, 0, 0, 0, math.log(3), -math.log(3)])
    assert abs(float((((six - T) / sg) ** 2).sum()) - 2.7390) < 1e-3


def test_the_seal():
    h = (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    for name in ("census.py", "compare.py"):
        assert hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest() in h
