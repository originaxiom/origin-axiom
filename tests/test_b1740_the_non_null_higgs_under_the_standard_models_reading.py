"""B1740 -- the non-null Higgs under the Standard Model's reading (P-345), sealed bf0a9a330, NEGATIVE as sealed for its
question (V1 holds; R1-R7, P1-P4 fail; C1, C2 hold).  Live: the alignment and the lost hierarchy recomputed from the
stored census rows (median |V_ud| under up S~, down S above 0.9; the best six-row's factor 131.7).  Stored: the cells
and fractions.  Seal: the hashes."""
import hashlib, json, math, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1740_the_non_null_higgs_under_the_standard_models_reading"
ROOT = A.parents[1]


def _c():
    return json.loads((A / "verification" / "comparison.json").read_text(encoding="utf-8"))


def test_the_cells_stored():
    c = _c(); k = c["cells"]
    assert k["V1_median_Vud_above_0.9_under_the_SM_reading"] and k["C1_control"] and k["C2_control_chi2_reproduces_B1735"]
    for name in ("R1_six_within_2_seat", "R2_six_specific_seat", "R3_six_specific_cov", "R4_six_specific_free", "R5_nine_specific_seat",
                 "R6_J_within_3_at_best_nine_seat", "R7_D_within_3_sigma_at_best_six_seat", "P1_chi2_six_below_16.75_seat",
                 "P2_chi2_six_specific_seat", "P3_chi2_nine_below_21.67_seat", "P4_chi2_nine_below_21.67_SM_reading"):
        assert not k[name], name
    assert c["chi2"]["six|seat"]["min"] > 3000 and c["fraction_as_good_mean"]["six|seat"] > 0.3
    assert c["seeds"] == list(range(1740, 1760)) and c["points"] == 23940


def test_alignment_and_lost_hierarchy_live():
    d = json.loads((ROOT / "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json").read_text(encoding="utf-8"))["masses_GeV"]["value"]
    T = np.array([d["c"] / d["t"], d["u"] / d["t"], d["s"] / d["b"], d["d"] / d["b"], d["mu"] / d["tau"], d["e"] / d["tau"]])
    vud, best = [], None
    for l in (A / "verification" / "census.jsonl").read_text(encoding="utf-8").splitlines():
        r = json.loads(l)
        for h in ("L_max", "L_2"):
            us, cb, ub, _ = r[f"ckm|{h}|St|S"]
            vud.append(math.sqrt(max(0.0, 1 - us * us - ub * ub)))
        if r["line"] == 37 and r["Re_tau"] == 0.55 and r["Im_tau"] == 2.25: best = r
    assert np.median(vud) > 0.99
    m = np.array(best["up|L_2|St"] + best["down|L_2|S"] + best["lep|L_2|S"]) / T
    assert abs(m[0] - 131.73) < 0.05 and abs(m[2] - 25.52) < 0.05


def test_the_seal():
    h = (A / "ARTIFACT_HASHES.txt").read_text(encoding="utf-8")
    for name in ("census.py", "compare.py"):
        assert hashlib.sha256((A / "verification" / name).read_bytes()).hexdigest() in h
