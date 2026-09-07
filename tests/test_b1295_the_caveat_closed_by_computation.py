"""B1295 -- THE CAVEAT CLOSED BY COMPUTATION: the three D4 computations reproduce by RUNNING, and the banked numbers are pinned."""
import json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1295_the_caveat_closed_by_computation"
VER = ARC / "verification"


def _run(args, cwd):
    r = subprocess.run([sys.executable] + [str(a) for a in args], capture_output=True, text=True, cwd=str(cwd))
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    return r.stdout


def test_D4c_the_cover_scan_reproduces_by_RUNNING(tmp_path):
    # the script writes cover_scan.json into its cwd: run it in a scratch dir so the shipped JSON stays the banked one
    out = _run([VER / "cover_scan.py"], tmp_path)
    assert out.rstrip().splitlines()[-1].startswith("VERDICT: NEGATIVE"), out[-600:]
    j = json.loads((tmp_path / "cover_scan.json").read_text(encoding="utf-8"))
    assert j["verdict"] == "NEGATIVE" and j["failures"] == []
    assert j["covers"] == 87 and j["multi_cusped"] == 64
    assert set(j["values"]) <= {"0", "4"}
    assert j["isometries_total"] == 968 and j["cusp_fixing_pairs"] == 1376
    assert j["cusp_shapes"]["hexagonal"] == 16 and sum(j["cusp_shapes"].values()) == 201


def test_D4b_the_census_engine_reproduces_by_RUNNING_through_Y3(tmp_path):
    out = _run([VER / "census_fixed_points.py", "--nmax", "3", "--out", tmp_path / "census.json"], VER)
    assert out.rstrip().endswith("SELFTEST: PASS (29/29)"), out[-600:]
    j = json.loads((tmp_path / "census.json").read_text(encoding="utf-8"))
    names = [r["name"] for r in j["results"]]
    assert names == ["Y_1", "Y_2", "Y_3", "Y_0"]
    for r in j["results"][:3]:
        assert r["is_QHS"] and r["counts_rev"] == [2] and r["counts_pres"] == [0] and r["consistent"]
        assert r["n_aut"] == r["n_snappy"]
    y0 = j["results"][3]
    assert not y0["is_QHS"] and y0["H1_closed"] == "Z" and y0["counts_rev"] == [0, 4]   # the control fires


def test_the_divisor_law_holds_on_the_shipped_coefficients_by_RUNNING():
    out = _run([VER / "divisor_law.py", VER / "cusp_coefficient.json", "coefficients_final", "200", "5e-3"], VER)
    line = [l for l in out.splitlines() if l.startswith("modes tested")][0]
    assert "modes tested (N(nu) <= 200): 184" in line and "failures (|obs - S| > 0.005): 0" in line, line
    assert "<-- FAIL" not in out


def _cc():
    return json.loads((VER / "cusp_coefficient.json").read_text(encoding="utf-8"))


def test_D4a_the_coefficient_is_not_zero_and_the_branch_is_decided():
    j = _cc()
    assert j["FAIL"] == []
    c0 = j["c0"]
    assert abs(c0["value_imag"] - (-4.2609826349)) < 1e-7 and c0["error_bar"] < 1e-7
    re, im = j["c_02_seat_pm20"]                    # the SM seat's c_(+-2,0) in their (k along lambda, l along mu) indexing
    assert abs(re) < 1e-10 and abs(im - c0["value_imag"]) < 1e-12
    fin = j["solve"]["(10.0, 0.45, 3200)"]
    assert fin["rank"] == fin["n_unknown"] == 1076 and fin["resid_rms"] < 1e-9
    for t, p in j["partition"].items():             # two annuli each, at every height: chi(d+M) = 0
        assert p["plus"]["components"] == 2 and p["minus"]["components"] == 2, t
        assert p["plus"]["chi_total"] == 0 and p["minus"]["chi_total"] == 0, t
    assert 0.05 < j["mixed_over_leading_at_t1"] < 0.10    # (+-2,+-1) is 7.6 % of the leading mode, not a near-tie
    van = {tuple(v["nu"]) for v in j["allowed_but_vanishing"]}
    assert van == {(0, -2), (3, -1), (3, -2)} and all(v["S"] == 0.0 for v in j["allowed_but_vanishing"])


def test_the_divisor_law_is_a_preregistered_conjecture_and_c0_is_open():
    j = _cc()
    d = j["divisor_law"]
    assert d["status"] == "CONJECTURE" and d["n_tested"] == 184 and d["n_fail"] == 0 and d["n_predicted_zeros"] == 68
    assert d["preregistered"]["verdict"] == "PASS" and d["preregistered"]["n_out"] == 88
    assert d["preregistered"]["eps_in"] < 1e-6 and d["preregistered"]["worst_out"] < 5e-3
    assert j["c0_identify"]["verdict"] == "OPEN" and j["c0_identify"]["hits"] == []
    lo = json.loads((VER / "law_outofsample.json").read_text(encoding="utf-8"))
    assert lo["verdict"] == "PASS" and lo["n_out"] == 88


def test_D4b_the_banked_census_is_two_or_nothing_on_all_nine_closings():
    j = json.loads((VER / "census_fixed_points.json").read_text(encoding="utf-8"))
    assert j["verdict"] == "PASS" and len(j["checks"]) == 71
    rows = {r["name"]: r for r in j["results"]}
    H1 = {"Y_1": "0", "Y_2": "Z/5", "Y_3": "Z/4 + Z/4", "Y_4": "Z/3 + Z/15", "Y_5": "Z/11 + Z/11",
          "Y_6": "Z/8 + Z/40", "Y_7": "Z/29 + Z/29", "Y_8": "Z/21 + Z/105", "Y_9": "Z/76 + Z/76"}
    for n in range(1, 10):
        r = rows[f"Y_{n}"]
        assert r["tets"] == 2 * n and r["n_aut"] == r["n_snappy"] == 8 * n and r["n_rev"] == 4 * n
        assert r["is_QHS"] and r["H1_closed"] == H1[f"Y_{n}"]
        assert r["counts_rev"] == [2] and r["counts_pres"] == [0] and r["consistent"]
    assert rows["Y_0"]["counts_rev"] == [0, 4] and rows["Y_0"]["H1_closed"] == "Z"
    assert sum(rows[f"Y_{n}"]["n_aut"] for n in range(1, 10)) == 360


def test_the_verdict_is_PROVED_with_no_new_law_and_no_identification():
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1295" and v["verdict"] == "PROVED" and v["creates_law"] is False and v["law_id"] is None
    assert v["identifications"] == [] and "B1294" in v["depends_on"]
    for s in ("-4.260982635", "88/88", "CONJECTURE", "{0: 882, 4: 494}", "16 of the 201 cusps", "I-26 stays UNEARNED"):
        assert s in v["claim_one_line"], s
