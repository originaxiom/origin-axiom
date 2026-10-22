"""B1723: the golden valley against the six measured ratios and PDG's CKM moduli, with the calibrations sealed in (as
B1712, B1713, B1720; seed 1723).  Rows: (valley point, line, horocycle, up reading).
    python3 -B compare.py      # writes comparison.json beside itself
Importing computes nothing."""
import hashlib, json, math, random, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
DATA = ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
SHA = "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
CKMDATA = ROOT / "frontier" / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json"
CKMSHA = "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
ALLOW = 0.10
N = 4000


def logs(x): return [math.log(max(z, 1e-300)) for z in x]


def best(Mat, target):
    w = np.exp(np.max(np.abs(Mat - target), axis=1)); i = int(np.argmin(w)); return float(w[i]), i


def r_masses(rng):
    tg = []
    for _s in range(3):
        while True:
            r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
            if r1 < r2: break
        tg += [r2, r1]
    return tg


def r_ckm(rng):
    while True:
        a, b, c = 10 ** rng.uniform(-1.5, -0.2), 10 ** rng.uniform(-2.5, -0.7), 10 ** rng.uniform(-3.5, -1.5)
        if c < b < a: return [a, b, c]


def calib(Mat, obs, draw):
    hits, samples = 0, []
    for _ in range(N):
        b, _i = best(Mat, np.log(np.array(draw()))); samples.append(b); hits += b <= obs + 1e-12
    return {"N": N, "fraction_fit_as_well": hits / N, "median": float(np.median(samples)), "q01": float(np.quantile(samples, 0.01))}


def order(line): return math.lcm(Fr(line[0]).denominator, Fr(line[1]).denominator)


def main():
    assert hashlib.sha256(DATA.read_bytes()).hexdigest() == SHA and hashlib.sha256(CKMDATA.read_bytes()).hexdigest() == CKMSHA
    d = json.loads(DATA.read_text(encoding="utf-8")); v, s = d["masses_GeV"]["value"], d["masses_GeV"]["sigma"]
    meas = lambda a, b: (v[a] / v[b], math.sqrt((s[a] / v[a]) ** 2 + (s[b] / v[b]) ** 2 + ALLOW ** 2))
    TGT = [meas("c", "t"), meas("u", "t"), meas("s", "b"), meas("d", "b"), meas("mu", "tau"), meas("e", "tau")]
    C = json.loads(CKMDATA.read_text(encoding="utf-8"))["ckm_abs"]["value"]; VTGT = [C[0][1], C[1][2], C[0][2]]
    G = json.loads((HERE / "the_golden_valley.json").read_text(encoding="utf-8"))
    lab, A, MX, JT = [], [], [], []
    for p in G["rows"]:
        for hor in ("L_max", "L_2"):
            for rd in ("S", "St", "conjS"):
                vals = p["up|%s|%s" % (hor, rd)] + p["down|%s|S" % hor] + p["lep|%s|S" % hor]
                ck = p["ckm|%s|%s" % (hor, rd)]
                lab.append((p["point"], p["line"], hor, rd)); A.append(logs(vals)); MX.append(logs(vals) + logs(ck[:3])); JT.append(ck[3])
    A, MX = np.array(A), np.array(MX)
    t6 = np.log(np.array([x[0] for x in TGT])); sig = np.array([x[1] for x in TGT]); t3 = np.log(np.array(VTGT))
    rng = random.Random(1723)
    wA, iA = best(A, t6); chi = np.sum(((A - t6) / sig) ** 2, axis=1); ic = int(np.argmin(chi)); calA = calib(A, wA, lambda: r_masses(rng))
    w3, i3 = best(MX[:, 6:], t3); calK = calib(MX[:, 6:], w3, lambda: r_ckm(rng))
    t9 = np.concatenate([t6, t3]); w9, i9 = best(MX, t9); calJ = calib(MX, w9, lambda: r_masses(rng) + r_ckm(rng))
    def at(i):
        l = lab[i]; return {"point": G["points"][l[0]], "line": G["lines"][l[1]], "order": order(G["lines"][l[1]]), "horocycle": l[2], "up_reading": l[3]}
    per_order = {}
    for i, l in enumerate(lab):
        wv = float(np.exp(np.max(np.abs(A[i] - t6)))); n_ord = order(G["lines"][l[1]])
        if n_ord not in per_order or wv < per_order[n_ord]["best_worst"]: per_order[n_ord] = dict(at(i), best_worst=wv)
    out = {"data_sha256": SHA, "ckm_data_sha256": CKMSHA, "rows": len(lab), "points": len(G["points"]), "lines": len(G["lines"]),
           "masses": dict(at(iA), worst_factor=wA, chi2_there=float(chi[iA]), model_over_measured=np.exp(A[iA] - t6).tolist()),
           "best_chi2": dict(at(ic), chi2=float(chi[ic])), "calibration_masses": calA,
           "mixing": dict(at(i3), worst_factor=w3, moduli=np.exp(MX[i3, 6:]).tolist(), J=JT[i3]), "calibration_mixing": calK,
           "nine": dict(at(i9), worst_factor=w9), "calibration_nine": calJ,
           "per_order": {str(k): per_order[k] for k in sorted(per_order)},
           "T1_six_within_factor_3": wA <= 3.0, "T2_specific_p_below_0.01": calA["fraction_fit_as_well"] <= 0.01, "T3_chi2_below_16.75": float(chi[ic]) < 16.75,
           "K1_three_within_factor_3": w3 <= 3.0, "K2_specific_p_below_0.01": calK["fraction_fit_as_well"] <= 0.01,
           "K3_nine_within_factor_3": w9 <= 3.0, "K4_specific_p_below_0.01": calJ["fraction_fit_as_well"] <= 0.01,
           "C1_control": G["C1_control"],
           "C1_holds": len(G["C1_control"]) >= 12 and max(c["T"] for c in G["C1_control"]) < 1e-6 and max(c["S"] for c in G["C1_control"]) < 1e-6}
    json.dump(out, open(HERE / "comparison.json", "w"), indent=1)
    print("T1", out["T1_six_within_factor_3"], "T2", out["T2_specific_p_below_0.01"], "T3", out["T3_chi2_below_16.75"])
    print("K1", out["K1_three_within_factor_3"], "K2", out["K2_specific_p_below_0.01"], "K3", out["K3_nine_within_factor_3"], "K4", out["K4_specific_p_below_0.01"], "C1", out["C1_holds"])


if __name__ == "__main__":
    main()
