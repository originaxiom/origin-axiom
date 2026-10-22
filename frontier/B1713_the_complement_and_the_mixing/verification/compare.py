"""B1713: the census's complement (orders 1-7) against the six measured ratios, and the mixing (orders 1-12) against PDG's
|V_us|, |V_cb|, |V_ub|, with the calibrations sealed in.  Part A as B1712's compare on the complement's rows.  Part B: the
worst factor over the three moduli (K1), its calibration (K2), the worst factor over the nine (six ratios and three
moduli, K3) and its calibration (K4).  Controls: unitarity (C1) and B1712's ratios reproduced on orders 8-12 (C2).
Read-outs: J, the right-vector convention, the double ratio (y_mu y_d)/(y_s y_e), the best per order.
    python3 -B compare.py      # writes comparison.json beside itself"""
import hashlib, json, math, random, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
DATA = ROOT / "frontier" / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
SHA = "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f"
CKMDATA = ROOT / "frontier" / "B1612_the_mixing_patterns_the_weave_fixes" / "verification" / "data.json"
CKMSHA = "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606"
B1712 = ROOT / "frontier" / "B1712_the_weave_census_of_lines" / "verification" / "the_line_census_masses.json"
ALLOW = 0.10
assert hashlib.sha256(DATA.read_bytes()).hexdigest() == SHA and hashlib.sha256(CKMDATA.read_bytes()).hexdigest() == CKMSHA
d = json.loads(DATA.read_text(encoding="utf-8")); v, s = d["masses_GeV"]["value"], d["masses_GeV"]["sigma"]
def meas(a, b): return v[a] / v[b], math.sqrt((s[a] / v[a]) ** 2 + (s[b] / v[b]) ** 2 + ALLOW ** 2)
TGT = [meas("c", "t"), meas("u", "t"), meas("s", "b"), meas("d", "b"), meas("mu", "tau"), meas("e", "tau")]
DR_DATA = (v["mu"] * v["d"]) / (v["s"] * v["e"])
C = json.loads(CKMDATA.read_text(encoding="utf-8"))["ckm_abs"]["value"]
VTGT = [C[0][1], C[1][2], C[0][2]]                                     # |V_us|, |V_cb|, |V_ub|
G = json.loads((HERE / "the_complement_and_mixing.json").read_text(encoding="utf-8"))
NC = G["n_complement"]
def logs(x): return [math.log(max(z, 1e-300)) for z in x]
labA, A, labB, MX, JT, RT = [], [], [], [], [], []
unit = 0.0
for p in G["rows"]:
    for hor in ("L_max", "L_2"):
        for rd in ("S", "St", "conjS"):
            m = [p["up|%s|%s" % (hor, rd)], p["down|%s|S" % hor], p["lep|%s|S" % hor]]
            vals = [m[0][0], m[0][1], m[1][0], m[1][1], m[2][0], m[2][1]]
            ck = p["ckm|%s|%s" % (hor, rd)]; unit = max(unit, ck[4])
            lab = (p["line"], p["Re_tau"], p["Im_tau"], hor, rd)
            if p["line"] < NC: labA.append(lab); A.append(logs(vals))
            labB.append(lab); MX.append(logs(vals) + logs(ck[:3])); JT.append(ck[3]); RT.append(p["ckm_right|%s|%s" % (hor, rd)])
A, MX = np.array(A), np.array(MX)
t6 = np.log(np.array([x[0] for x in TGT])); sig = np.array([x[1] for x in TGT]); t3 = np.log(np.array(VTGT))
def best(Mat, target):
    w = np.exp(np.max(np.abs(Mat - target), axis=1)); i = int(np.argmin(w)); return float(w[i]), i
rng = random.Random(1713)
def r_masses():
    tg = []
    for _s in range(3):
        while True:
            r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
            if r1 < r2: break
        tg += [r2, r1]
    return tg
def r_ckm():
    while True:
        a, b, c = 10 ** rng.uniform(-1.5, -0.2), 10 ** rng.uniform(-2.5, -0.7), 10 ** rng.uniform(-3.5, -1.5)
        if c < b < a: return [a, b, c]
N = 4000
def calib(Mat, obs, draw):
    hits, samples = 0, []
    for _ in range(N):
        b, _i = best(Mat, np.log(np.array(draw()))); samples.append(b); hits += b <= obs + 1e-12
    return {"N": N, "fraction_fit_as_well": hits / N, "median": float(np.median(samples)), "q01": float(np.quantile(samples, 0.01)), "q05": float(np.quantile(samples, 0.05))}
def dr(m): return math.exp(m[4] - m[5]) * math.exp(m[3] - m[2])        # (m_mu/m_e)(m_d/m_s) from the logs of the six
# ---- Part A: the complement's masses
wA, iA = best(A, t6); chiA = np.sum(((A - t6) / sig) ** 2, axis=1); icA = int(np.argmin(chiA))
calA = calib(A, wA, r_masses)
per_line_A = {}
for k in range(NC):
    idx = [i for i, l in enumerate(labA) if l[0] == k]; ww = np.exp(np.max(np.abs(A[idx] - t6), axis=1)); j = idx[int(np.argmin(ww))]
    per_line_A["%s %s %s" % tuple(G["lines"][k])] = {"best_worst": float(np.min(ww)), "at": labA[j][1:]}
# ---- Part B: the mixing on every order 1-12
w3, i3 = best(MX[:, 6:], t3); calK = calib(MX[:, 6:], w3, r_ckm)
t9 = np.concatenate([t6, t3]); w9, i9 = best(MX, t9); calJ = calib(MX, w9, lambda: r_masses() + r_ckm())
per_order = {}
for k, ln in enumerate(G["lines"]):
    idx = [i for i, l in enumerate(labB) if l[0] == k]; ww = np.exp(np.max(np.abs(MX[idx, 6:] - t3), axis=1)); j = idx[int(np.argmin(ww))]
    o = ln[0]
    if o not in per_order or ww.min() < per_order[o]["best_worst_3"]: per_order[o] = {"best_worst_3": float(ww.min()), "line": ln, "at": labB[j][1:]}
Jmax = {}
for i, l in enumerate(labB):
    key = "%s %s %s" % tuple(G["lines"][l[0]]); Jmax[key] = max(Jmax.get(key, 0.0), abs(JT[i]))
# ---- C2: B1712's ratios reproduced on orders 8-12
c2 = None
if B1712.is_file():
    old = {(r["line"], r["Re_tau"], r["Im_tau"]): r for r in json.loads(B1712.read_text(encoding="utf-8"))["rows"]}
    c2 = 0.0
    for p in G["rows"]:
        if p["line"] < NC: continue
        o = old[(p["line"] - NC, p["Re_tau"], p["Im_tau"])]
        for kk, vv in o.items():
            if "|" in kk: c2 = max(c2, max(abs(a - b) / max(abs(b), 1e-300) for a, b in zip(p[kk], vv)))
def at(i, lab): return {"line": G["lines"][lab[i][0]], "Re_tau": lab[i][1], "Im_tau": lab[i][2], "horocycle": lab[i][3], "up_reading": lab[i][4]}
out = {"data_sha256": SHA, "ckm_data_sha256": CKMSHA, "rows_A": len(labA), "rows_B": len(labB),
       "A": {"best_by_worst_factor": dict(at(iA, labA), worst_factor=wA, chi2=float(chiA[iA]), model_ratios=np.exp(A[iA]).tolist(),
                                          targets=[x[0] for x in TGT], double_ratio=dr(A[iA])),
             "best_by_chi2": dict(at(icA, labA), chi2=float(chiA[icA]), worst_factor=float(np.exp(np.max(np.abs(A[icA] - t6))))),
             "per_line": per_line_A, "calibration": calA,
             "H1_within_factor_3": wA <= 3.0, "H2_specific_p_below_0.01": calA["fraction_fit_as_well"] <= 0.01,
             "H3_chi2_below_16.75": float(chiA[icA]) < 16.75},
       "B": {"best_three": dict(at(i3, labB), worst_factor=w3, moduli=np.exp(MX[i3, 6:]).tolist(), J=JT[i3], right_convention=RT[i3]),
             "best_nine": dict(at(i9, labB), worst_factor=w9, model=np.exp(MX[i9]).tolist(), J=JT[i9], double_ratio=dr(MX[i9])),
             "targets_moduli": VTGT, "calibration_three": calK, "calibration_nine": calJ, "per_order": per_order,
             "J_max_abs_by_line": Jmax,
             "K1_three_within_factor_3": w3 <= 3.0, "K2_specific_p_below_0.01": calK["fraction_fit_as_well"] <= 0.01,
             "K3_nine_within_factor_3": w9 <= 3.0, "K4_specific_p_below_0.01": calJ["fraction_fit_as_well"] <= 0.01},
       "C1_unitarity_max": unit, "C1_holds": unit < 1e-10, "C2_B1712_max_rel_diff": c2, "C2_holds": (c2 is not None and c2 < 1e-9),
       "double_ratio_data_HZ2021": DR_DATA}
if __name__ == "__main__":
    json.dump(out, open(HERE / "comparison.json", "w"), indent=1)
    print("A: H1", out["A"]["H1_within_factor_3"], "H2", out["A"]["H2_specific_p_below_0.01"], "H3", out["A"]["H3_chi2_below_16.75"])
    print("B: K1", out["B"]["K1_three_within_factor_3"], "K2", out["B"]["K2_specific_p_below_0.01"], "K3", out["B"]["K3_nine_within_factor_3"], "K4", out["B"]["K4_specific_p_below_0.01"])
    print("C1", out["C1_holds"], "C2", out["C2_holds"])
