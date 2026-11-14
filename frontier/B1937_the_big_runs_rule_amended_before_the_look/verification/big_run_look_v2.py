"""THE BIG RUN's comparison, version 2 (main, 2026-11-14, before the look). It amends B1932's rule after the web seat's
cold read W-F18; its rule is BIG_RUN_RULE_v2.md beside it. B1932's big_run_look.py (version 1) stays sealed and is run
beside this one; version 2 governs.

It reads B1932's committed values (pinned by sha256) and the two data files pinned by B1720's compare.py. For each of the
four declared options it computes:
  - GOVERNING, on frame C's seven claimed rows: chi2_7 (P-341's statistic) and the worst factor (B1720's coarse cell);
  - REPORTED, as P-341 binds: chi2_six and chi2_nine at compare.py's rows, with the lepton rows as frame C gives them
    (at level 5 the leptons are the down quarks transposed, B1934: the same ratios), and their coarse cells.
It calibrates the best of the four, for every statistic, against B1720's random targets, and writes
big_run_output_v2.json. Nothing is fitted; no option is chosen after the output is read; every passing option is listed.
    python3 -B big_run_look_v2.py"""
import hashlib, json, math, pathlib, random
import numpy as np
from scipy.stats import chi2
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
VALUES = ROOT / "frontier" / "B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options" / "verification" / "BIG_RUN_VALUES.json"
VALUES_SHA = "df1c9bee002ecf5eeb7f1f360e497a5c091bf092cdbaa499352ea3201d02b536"
DATA = ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
SHA = "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
CKMDATA = ROOT / "frontier" / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json"
CKMSHA = "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
POSITIONS = ["up m2/m3", "up m1/m3", "down m2/m3", "down m1/m3", "|V12|", "|V23|", "|V13|"]
OPTIONS = ["W-|a (move count)", "W-|b (area)", "W+|a (move count)", "W+|b (area)"]
ALLOW = 0.10                                          # P-341 / B1720 compare.py
BAR7 = float(chi2.ppf(1 - 0.01 / len(OPTIONS), 7))    # governing: the 1 % tail of chi2(7) after four options, 22.04
BAR6, BAR9 = 16.75, 21.67                             # P-341's bars as written (reported)
FACTOR = 3.0                                          # B1720's coarse cells: every row within a factor 3
P_CAL = 0.01
N_CAL, SEED = 4000, 20261115
# the rows of each statistic, as indices into the nine targets
# (c/t, u/t, s/b, d/b, mu/tau, e/tau, |V_us|, |V_cb|, |V_ub|): compare.py's order, then the three moduli
SETS = {"seven": [0, 1, 2, 3, 6, 7, 8], "six": [0, 1, 2, 3, 4, 5], "nine": list(range(9))}


def nine_from_option(vals):
    """An option's seven values as the nine rows. The lepton rows are the down rows: at level 5 the lepton coupling is
    the down coupling transposed (B1934), the same reading in both Higgs worlds, so its singular-value ratios are the
    down ratios. Frame C does not claim them (the scoreboard, frame C's status, 2026-11-14 08:40)."""
    up2, up1, dn2, dn1, v12, v23, v13 = vals
    return [up2, up1, dn2, dn1, dn2, dn1, v12, v23, v13]


def targets(data_path, ckm_path):
    d = json.loads(pathlib.Path(data_path).read_text(encoding="utf-8")); v, s = d["masses_GeV"]["value"], d["masses_GeV"]["sigma"]
    meas = lambda a, b: (v[a] / v[b], math.sqrt((s[a] / v[a]) ** 2 + (s[b] / v[b]) ** 2 + ALLOW ** 2))
    T = [meas("c", "t"), meas("u", "t"), meas("s", "b"), meas("d", "b"), meas("mu", "tau"), meas("e", "tau")]
    ck = json.loads(pathlib.Path(ckm_path).read_text(encoding="utf-8"))["ckm_abs"]
    for i, j in ((0, 1), (1, 2), (0, 2)):                 # B1735's sigma: the data's, with 0.10 in quadrature
        T.append((ck["value"][i][j], math.sqrt((ck["sigma"][i][j] / ck["value"][i][j]) ** 2 + ALLOW ** 2)))
    return np.log([t[0] for t in T]), np.array([t[1] for t in T])


def stats(M, tl, sig):
    """For a matrix of options' log values (rows = options, columns = the nine), each statistic per option."""
    out = {}
    for name, idx in SETS.items():
        D = M[:, idx] - tl[idx]
        out["chi2_" + name] = np.sum((D / sig[idx]) ** 2, axis=1)
        out["worst_factor_" + name] = np.exp(np.max(np.abs(D), axis=1))
    return out


def random_nine(rng):
    """B1720's law: r_masses for three sectors (r2, r1 per sector, r1 < r2), then r_ckm (c < b < a)."""
    r = []
    for _s in range(3):
        while True:
            r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
            if r1 < r2:
                break
        r += [r2, r1]
    while True:
        a, b, c = 10 ** rng.uniform(-1.5, -0.2), 10 ** rng.uniform(-2.5, -0.7), 10 ** rng.uniform(-3.5, -1.5)
        if c < b < a:
            break
    return r + [a, b, c]


def look(values_path, data_path, ckm_path, out_path):
    V = json.loads(pathlib.Path(values_path).read_text(encoding="utf-8"))
    assert V["positions"] == POSITIONS, "the values file's positions are not the expected ones"
    assert sorted(V["options"]) == sorted(OPTIONS), "the values file's options are not the four declared ones"
    tl, sig = targets(data_path, ckm_path)
    M = np.log(np.array([nine_from_option(V["options"][o]["values"]) for o in OPTIONS]))
    S = stats(M, tl, sig)
    per = {}
    for k, o in enumerate(OPTIONS):
        e = {key: float(S[key][k]) for key in S}
        e["pulls_nine"] = ((M[k] - tl) / sig).tolist()
        e["passes_governing"] = bool(e["chi2_seven"] < BAR7 and e["worst_factor_seven"] <= FACTOR)
        e["meets_coarse_seven"] = bool(e["worst_factor_seven"] <= FACTOR)
        e["reported_P341"] = {"chi2_six_below_16.75": bool(e["chi2_six"] < BAR6), "chi2_nine_below_21.67": bool(e["chi2_nine"] < BAR9),
                              "six_within_factor_3": bool(e["worst_factor_six"] <= FACTOR), "nine_within_factor_3": bool(e["worst_factor_nine"] <= FACTOR)}
        per[o] = e
    best = {key: float(np.min(S[key])) for key in S}
    rng = random.Random(SEED); hits = {key: 0 for key in S}; med = {key: [] for key in S}
    for _ in range(N_CAL):
        R = stats(M, np.log(np.array(random_nine(rng))), sig)
        for key in S:
            b = float(np.min(R[key])); med[key].append(b); hits[key] += b <= best[key] + 1e-12
    cal = {key: {"fraction_as_good_as_the_best_option": hits[key] / N_CAL, "median_best": float(np.median(med[key]))} for key in S}
    passing = [o for o in OPTIONS if per[o]["passes_governing"]]
    coarse = [o for o in OPTIONS if per[o]["meets_coarse_seven"]]
    cal_ok = cal["chi2_seven"]["fraction_as_good_as_the_best_option"] < P_CAL and cal["worst_factor_seven"]["fraction_as_good_as_the_best_option"] < P_CAL
    if passing and cal_ok:
        outcome = "PASS"
    elif coarse and cal["worst_factor_seven"]["fraction_as_good_as_the_best_option"] < P_CAL:
        outcome = "PATTERN MATCH"
    else:
        outcome = "FAIL"
    out = {"rule": "BIG_RUN_RULE_v2.md", "bars": {"chi2_seven": BAR7, "chi2_six": BAR6, "chi2_nine": BAR9, "factor": FACTOR, "calibration": P_CAL},
           "options": per, "best": best, "calibration": {"N": N_CAL, "seed": SEED, "law": "B1720 compare.py's random targets, three sectors and the moduli", "by_statistic": cal},
           "passing_options_none_preferred": passing if outcome == "PASS" else [],
           "outcome_governing_seven": outcome,
           "reported_P341_six_and_nine": {"note": "the lepton rows are the down rows (B1934); frame C does not claim them",
                                          "any_option_chi2_six_below_bar": any(per[o]["reported_P341"]["chi2_six_below_16.75"] for o in OPTIONS),
                                          "any_option_chi2_nine_below_bar": any(per[o]["reported_P341"]["chi2_nine_below_21.67"] for o in OPTIONS),
                                          "calibration_six": cal["chi2_six"], "calibration_nine": cal["chi2_nine"]}}
    pathlib.Path(out_path).write_text(json.dumps(out, indent=1))
    return out


def main():
    assert hashlib.sha256(VALUES.read_bytes()).hexdigest() == VALUES_SHA, "the values are not the committed ones"
    assert hashlib.sha256(DATA.read_bytes()).hexdigest() == SHA and hashlib.sha256(CKMDATA.read_bytes()).hexdigest() == CKMSHA
    look(VALUES, DATA, CKMDATA, HERE / "big_run_output_v2.json")
    print("written; sha256", hashlib.sha256((HERE / "big_run_output_v2.json").read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
