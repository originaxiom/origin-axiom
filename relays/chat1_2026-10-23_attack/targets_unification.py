#!/usr/bin/env python3
"""TARGETS AT THE UNIFICATION SCALE (track A-4 of THE_PLAN_AFTER_THE_READING_TEST; data, no model).  The nine (six
in-sector mass ratios, |V_us|, |V_cb|, |V_ub|), D = (m_mu/m_s)(m_d/m_e) and the inter-sector ratio m_b/m_tau at
M_GUT = 2e16 GeV in the MSSM, from the published running values of arXiv:2510.01312v1 ("Updated Running Quark and Lepton
Parameters"), Table 6 (2024 PDG input, M_SUSY = 3 TeV, SUSY threshold corrections eta = 0, "SM quantities":
y_{u,c,t} = y^MSSM sin(beta), y_{d,s,b,e,mu,tau} = y^MSSM cos(beta), CKM angles unchanged), transcribed by hand from the
paper (values and 1-sigma errors as printed; the transcription is the only step), beside the record's M_Z targets
(inverse_higgs.py's pinned files at 3412bf09d).  In-sector ratios do not depend on the sin/cos(beta) normalisation; the
CKM moduli are taken as |V_us| = sin(theta12), |V_cb| = sin(theta23) cos(theta13), |V_ub| = sin(theta13).
    python3 -B targets_unification.py      # writes targets_unification.json"""
import importlib.util, json, math, sys, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
TABLE6 = {   # tan(beta): (value, 1-sigma error) as printed; y_u in 1e-6, y_c 1e-3, y_d 1e-5, y_s 1e-4, y_b 1e-2, y_e 1e-6, y_mu 1e-4, y_tau 1e-2, th23 1e-2, th13 1e-3
    5: {"yu": (2.79, 0.07), "yc": (1.41, 0.03), "yt": (0.5058, 0.0084), "yd": (0.49, 0.01), "ys": (0.97, 0.01), "yb": (0.548, 0.006),
        "ye": (2.0010, 0.0007), "ymu": (4.2154, 0.0016), "ytau": (0.7170, 0.0003), "th12": (0.22702, 0.00082), "th23": (3.862, 0.038), "th13": (3.40, 0.07)},
    10: {"yu": (2.76, 0.07), "yc": (1.39, 0.03), "yt": (0.4947, 0.0079), "yd": (0.49, 0.01), "ys": (0.98, 0.01), "yb": (0.550, 0.006),
         "ye": (2.0095, 0.0008), "ymu": (4.2334, 0.0017), "ytau": (0.7223, 0.0003), "th12": (0.22702, 0.00082), "th23": (3.874, 0.038), "th13": (3.41, 0.07)},
    30: {"yu": (2.76, 0.07), "yc": (1.39, 0.03), "yt": (0.5020, 0.0081), "yd": (0.52, 0.01), "ys": (1.03, 0.02), "yb": (0.600, 0.007),
         "ye": (2.1128, 0.0020), "ymu": (4.4515, 0.0042), "ytau": (0.7889, 0.0008), "th12": (0.22702, 0.00082), "th23": (3.823, 0.038), "th13": (3.37, 0.07)},
    50: {"yu": (2.79, 0.07), "yc": (1.41, 0.03), "yt": (0.5312, 0.0095), "yd": (0.59, 0.01), "ys": (1.18, 0.02), "yb": (0.766, 0.013),
         "ye": (2.4248, 0.0087), "ymu": (5.1104, 0.0183), "ytau": (1.0089, 0.0042), "th12": (0.22702, 0.00082), "th23": (3.679, 0.037), "th13": (3.24, 0.07)},
}
SC = {"yu": 1e-6, "yc": 1e-3, "yt": 1.0, "yd": 1e-5, "ys": 1e-4, "yb": 1e-2, "ye": 1e-6, "ymu": 1e-4, "ytau": 1e-2, "th12": 1.0, "th23": 1e-2, "th13": 1e-3}
NAMES = ["m_c/m_t", "m_u/m_t", "m_s/m_b", "m_d/m_b", "m_mu/m_tau", "m_e/m_tau", "|V_us|", "|V_cb|", "|V_ub|"]


def nine(t):
    v = {k: t[k][0] * SC[k] for k in t}; e = {k: t[k][1] / t[k][0] for k in t}
    s12, s23, s13 = math.sin(v["th12"]), math.sin(v["th23"]), math.sin(v["th13"])
    vals = [v["yc"] / v["yt"], v["yu"] / v["yt"], v["ys"] / v["yb"], v["yd"] / v["yb"], v["ymu"] / v["ytau"], v["ye"] / v["ytau"],
            s12, s23 * math.cos(v["th13"]), s13]
    rel = [math.hypot(e["yc"], e["yt"]), math.hypot(e["yu"], e["yt"]), math.hypot(e["ys"], e["yb"]), math.hypot(e["yd"], e["yb"]),
           math.hypot(e["ymu"], e["ytau"]), math.hypot(e["ye"], e["ytau"]), e["th12"], e["th23"], e["th13"]]
    D = (v["ymu"] / v["ys"]) * (v["yd"] / v["ye"])
    return vals, rel, D, v["yb"] / v["ytau"]


argv = sys.argv; sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("ih", HERE / "inverse_higgs.py"); ih = importlib.util.module_from_spec(spec); spec.loader.exec_module(ih)
sys.argv = argv
mz = np.exp(ih.T9)
out = {"source": "arXiv:2510.01312v1, Table 6 (2024 PDG input, M_SUSY = 3 TeV, eta = 0, M_GUT = 2e16 GeV), transcribed by hand",
       "names": NAMES, "M_Z (the record's pinned targets)": mz.tolist(), "M_Z relative errors": ih.REL.tolist(), "GUT": {}}
for tb, t in TABLE6.items():
    vals, rel, D, btau = nine(t)
    out["GUT"][f"tan beta {tb}"] = {"nine": vals, "relative errors": rel, "GUT / M_Z": [round(a / b, 4) for a, b in zip(vals, mz)],
                                    "D": D, "m_b/m_tau": btau}
(HERE / "targets_unification.json").write_text(json.dumps(out, indent=1) + "\n")
print("written")
