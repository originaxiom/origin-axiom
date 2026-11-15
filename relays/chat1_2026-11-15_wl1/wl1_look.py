#!/usr/bin/env python3
"""W-L1, the look (card W-L1, 82c94361d; values 4a9b788d6). The big run's version-3 statistic, bar and calibration
(B1940's big_run_look_v3.py, re-typed here, not imported), applied to one declared option, frame C at (tau = i, the
mark), with the two end-shifted options reported beside it.

    MAIN_CHECKOUT=<a checkout of main> python3 -I -u wl1_look.py

Inputs, each pinned by sha256: this seat's LOOK_VALUES.json; the two data files the big run pins (B1637's received
HZ2021_running_masses_MZ.json; B1612's data.json).
Governing: chi2_7 on the seven claimed rows below the 1 % tail of chi2(7) after five options (the big run's four and this
one), every row within a factor 3, and both calibrations (chi2_7 and the worst factor; B1720's random-target law, 4,000
draws, seed 20261115) below 1 %. Outcome PASS, PATTERN MATCH or FAIL as version 3 defines them. Reported: P-341's six
and nine (the lepton rows as frame C gives them, the down rows), and the same statistics for the two end-shifted
options, each calibrated alone. Writes wl1_look_output.json and prints a summary.
"""
import hashlib, json, math, os, random
import numpy as np
from scipy.stats import chi2

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN = os.environ.get("MAIN_CHECKOUT")
VALUES = os.path.join(HERE, "LOOK_VALUES.json")
VALUES_SHA = "976f52f2428a1dcaf97ae8f12f36182c81e32f5815b38afed36a1994aab069bf"
DATA_REL = ("frontier", "B1637_fits_on_the_ruled_branch", "received", "HZ2021_running_masses_MZ.json")
SHA = "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
CKM_REL = ("frontier", "B1612_the_mixing_patterns_the_weave_fixes", "verification", "data.json")
CKMSHA = "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
POSITIONS = ["up m2/m3", "up m1/m3", "down m2/m3", "down m1/m3", "|V12|", "|V23|", "|V13|"]
GOV = "tau=i, mark, canonical end"
REP = ["end -0.3 (reported)", "end +0.3 (reported)"]
ALLOW = 0.10
BAR7 = float(chi2.ppf(1 - 0.01 / 5, 7))
BAR6, BAR9 = 16.75, 21.67
FACTOR = 3.0
P_CAL = 0.01
N_CAL, SEED = 4000, 20261115
SETS = {"seven": [0, 1, 2, 3, 6, 7, 8], "six": [0, 1, 2, 3, 4, 5], "nine": list(range(9))}


def nine_from_option(vals):
    up2, up1, dn2, dn1, v12, v23, v13 = vals
    return [up2, up1, dn2, dn1, dn2, dn1, v12, v23, v13]


def targets(data_path, ckm_path):
    d = json.load(open(data_path, encoding="utf-8"))
    v, s = d["masses_GeV"]["value"], d["masses_GeV"]["sigma"]
    meas = lambda a, b: (v[a] / v[b], math.sqrt((s[a] / v[a]) ** 2 + (s[b] / v[b]) ** 2 + ALLOW ** 2))
    T = [meas("c", "t"), meas("u", "t"), meas("s", "b"), meas("d", "b"), meas("mu", "tau"), meas("e", "tau")]
    ck = json.load(open(ckm_path, encoding="utf-8"))["ckm_abs"]
    for i, j in ((0, 1), (1, 2), (0, 2)):
        T.append((ck["value"][i][j], math.sqrt((ck["sigma"][i][j] / ck["value"][i][j]) ** 2 + ALLOW ** 2)))
    return np.log([t[0] for t in T]), np.array([t[1] for t in T])


def stats(M, tl, sig):
    out = {}
    for name, idx in SETS.items():
        D = M[:, idx] - tl[idx]
        out["chi2_" + name] = np.sum((D / sig[idx]) ** 2, axis=1)
        out["worst_factor_" + name] = np.exp(np.max(np.abs(D), axis=1))
    return out


def random_nine(rng):
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


def evaluate(vals, tl, sig):
    M = np.log(np.array([nine_from_option(vals)]))
    S = stats(M, tl, sig)
    e = {key: float(S[key][0]) for key in S}
    e["pulls_nine"] = ((M[0] - tl) / sig).tolist()
    e["passes_governing"] = bool(e["chi2_seven"] < BAR7 and e["worst_factor_seven"] <= FACTOR)
    e["meets_coarse_seven"] = bool(e["worst_factor_seven"] <= FACTOR)
    rng = random.Random(SEED)
    hits = {key: 0 for key in S}
    for _ in range(N_CAL):
        R = stats(M, np.log(np.array(random_nine(rng))), sig)
        for key in S:
            hits[key] += float(R[key][0]) <= e[key] + 1e-12
    e["calibration"] = {key: hits[key] / N_CAL for key in S}
    cal_ok = e["calibration"]["chi2_seven"] < P_CAL and e["calibration"]["worst_factor_seven"] < P_CAL
    if e["passes_governing"] and cal_ok:
        e["outcome"] = "PASS"
    elif e["meets_coarse_seven"] and e["calibration"]["worst_factor_seven"] < P_CAL:
        e["outcome"] = "PATTERN MATCH"
    else:
        e["outcome"] = "FAIL"
    e["reported_P341"] = {"chi2_six_below_16.75": bool(e["chi2_six"] < BAR6), "chi2_nine_below_21.67": bool(e["chi2_nine"] < BAR9)}
    return e


def main():
    if MAIN is None:
        raise SystemExit("set MAIN_CHECKOUT")
    data = os.path.join(MAIN, *DATA_REL)
    ckm = os.path.join(MAIN, *CKM_REL)
    assert hashlib.sha256(open(VALUES, "rb").read()).hexdigest() == VALUES_SHA, "the values are not the committed ones"
    assert hashlib.sha256(open(data, "rb").read()).hexdigest() == SHA, "the mass data are not the pinned file"
    assert hashlib.sha256(open(ckm, "rb").read()).hexdigest() == CKMSHA, "the mixing data are not the pinned file"
    V = json.load(open(VALUES))
    assert V["positions"] == POSITIONS
    tl, sig = targets(data, ckm)
    out = {"rule": "card W-L1 (82c94361d): version 3's statistic, bar after five options",
           "bars": {"chi2_seven": BAR7, "chi2_six": BAR6, "chi2_nine": BAR9, "factor": FACTOR, "calibration": P_CAL},
           "calibration": {"N": N_CAL, "seed": SEED, "law": "B1720 compare.py's random targets"},
           "governing": {GOV: evaluate(V["options"][GOV]["values"], tl, sig)},
           "reported": {o: evaluate(V["options"][o]["values"], tl, sig) for o in REP},
           "look_ledger": "36 sealed decisive cells and 32 post-hoc scans (Review 70), six point-based value looks (A9), the big run (B1944), and this look"}
    path = os.path.join(HERE, "wl1_look_output.json")
    open(path, "w").write(json.dumps(out, indent=1))
    g = out["governing"][GOV]
    print("OUTCOME (governing, %s): %s" % (GOV, g["outcome"]))
    print("chi2_7 %.3f (bar %.2f) | worst factor %.3f (bar 3) | calibration chi2_7 %.4f, worst factor %.4f" % (
        g["chi2_seven"], BAR7, g["worst_factor_seven"], g["calibration"]["chi2_seven"], g["calibration"]["worst_factor_seven"]))
    print("pulls (nine rows, compare.py's order):", ["%.2f" % p for p in g["pulls_nine"]])
    print("reported, P-341: chi2_six %.3f, chi2_nine %.3f" % (g["chi2_six"], g["chi2_nine"]))
    for o in REP:
        r = out["reported"][o]
        print("reported %s: outcome %s, chi2_7 %.3f, worst factor %.3f, calibrations %.4f / %.4f" % (
            o, r["outcome"], r["chi2_seven"], r["worst_factor_seven"], r["calibration"]["chi2_seven"], r["calibration"]["worst_factor_seven"]))
    print("written; sha256", hashlib.sha256(open(path, "rb").read()).hexdigest())


if __name__ == "__main__":
    main()
