"""B1742: main's independent reproduction of the web seat's TWO_HIGGS (H_u for up, H_d for down and
leptons, all read S, c = 3) on main's own B1740 instrument (imported, not modified).  F_a's direction (th2^a, th4^a,
i th3^a) (B1730, eps = 1 for a = -2, 6, 22).  Control: H_u = H_d = F_-2 reproduces B1740's stored census row."""
import sys, json, math, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[3]
V40 = ROOT / "frontier" / "B1740_the_non_null_higgs_under_the_standard_models_reading" / "verification"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


CEN = _load("b1740_census", V40 / "census.py")
CMP = _load("b1740_compare", V40 / "compare.py")
SECT = CEN.SECT


def direction(a, t):
    import mpmath as mp
    T = mp.mpc(t.real, t.imag)
    th2 = mp.fsum(mp.exp(1j * mp.pi * T * (n + mp.mpf(1) / 2) ** 2) for n in range(-30, 30))
    th3 = mp.fsum(mp.exp(1j * mp.pi * T * n * n) for n in range(-30, 31))
    th4 = mp.fsum((-1) ** n * mp.exp(1j * mp.pi * T * n * n) for n in range(-30, 31))
    eps = 1j ** ((a + 2) // 2)
    v = [eps * th2 ** a, eps * th4 ** a, 1j * th3 ** a]; m = max(abs(x) for x in v)
    return [complex(x / m) for x in v]


def Smat(v, B): return v[0] * B.QI + v[1] * B.QJ + v[2] * B.QK


def compute2(re_t, im_t, a, b, au, ad, hor, read=("S", "S", "S")):
    """per-sector Higgs: up gets F_au, down and leptons F_ad; readings (up, down, lep) from S / St"""
    M = CEN._modules(); B, col = M["B"], M["col"]
    t = complex(re_t, im_t); w = float(a) * t + float(b)
    L = float(np.interp(im_t, [q[0] for q in col], [q[1] if hor == "L_max" else q[2] for q in col]))
    Hs = {"up": Smat(direction(au, t), B), "down": Smat(direction(ad, t), B), "lep": Smat(direction(ad, t), B)}
    rd = dict(zip(("up", "down", "lep"), read)); out, Y = {}, {}
    for sec, (lf, rf) in SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
        Mw = B.weighted_M(u); S = Hs[sec]
        if rd[sec] == "St": S = B.EPS @ np.conj(S) @ B.EPS.T
        Ym = B.coupling(S, Mw); Y[sec] = Ym
        sv = np.linalg.svd(Ym, compute_uv=False); out[sec] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    Uu = np.linalg.svd(Y["up"])[0][:, ::-1]; Ud = np.linalg.svd(Y["down"])[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    out["ckm"] = [float(abs(V[0, 1])), float(abs(V[1, 2])), float(abs(V[0, 2])), J]
    return out


def targets():
    d = json.loads(CMP.DATA.read_text(encoding="utf-8")); v = d["masses_GeV"]["value"]; C = json.loads(CMP.CKMDATA.read_text(encoding="utf-8"))["ckm_abs"]["value"]
    T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
    return T6, np.concatenate([T6, np.log(np.array([C[0][1], C[1][2], C[0][2]]))])


def readout(r, c=3.0):
    T6, T9 = targets(); s6, s9 = CMP.sigmas()
    six = np.log(np.array(r["up"] + r["down"] + r["lep"])) + np.array([0, 0, 0, 0, math.log(c), -math.log(c)])
    nine = np.concatenate([six, np.log(np.array(r["ckm"][:3]))])
    D = math.exp(six[4] + six[3] - six[2] - six[5])
    return {"six_over_measured": np.exp(six - T6).round(4).tolist(), "worst_six": float(np.exp(np.max(np.abs(six - T6)))),
            "chi2_six": float((((six - T6) / s6) ** 2).sum()), "ckm_over_measured": np.exp(nine[6:] - T9[6:]).round(4).tolist(),
            "worst_nine": float(np.exp(np.max(np.abs(nine - T9)))), "chi2_nine": float((((nine - T9) / s9) ** 2).sum()),
            "Vus_Vcb_Vub": [round(x, 5) for x in r["ckm"][:3]], "J": r["ckm"][3], "D": D}


def control():
    """H_u = H_d = F_-2, every sector S: against B1740's stored row at (line 37, 0.55 + 2.25i), both horocycles"""
    a, b = CEN.lines()[37]; rec = None
    for l in (V40 / "census.jsonl").open(encoding="utf-8"):
        r = json.loads(l)
        if r["line"] == 37 and r["Re_tau"] == 0.55 and r["Im_tau"] == 2.25: rec = r; break
    worst = 0.0
    for h in ("L_max", "L_2"):
        for rd in (("S", "S", "S"), ("St", "S", "S"), ("St", "St", "St")):
            m = compute2(0.55, 2.25, a, b, -2, -2, h, rd)
            for sec, x in zip(("up", "down", "lep"), rd):
                worst = max(worst, max(abs(math.log(p / q)) for p, q in zip(m[sec], rec[f"{sec}|{h}|{x}"])))
            k = rec[f"ckm|{h}|{rd[0]}|{rd[1]}"]
            worst = max(worst, max(abs(math.log(p / q)) for p, q in zip(m["ckm"][:3], k[:3])), abs(m["ckm"][3] - k[3]) / max(abs(k[3]), 1e-30) * 1e-3)
    return {"line": [str(a), str(b)], "max_dln_against_B1740": worst}


if __name__ == "__main__":
    res = {"control": control()}; print("control", res["control"], flush=True)
    F = (Fr(2, 5), Fr(1, 10))
    res["best_six F6|F22"] = readout(compute2(0.5625, 2.6, *F, 6, 22, "L_2"))
    res["best_nine F6|F22"] = readout(compute2(0.0625, 2.7, Fr(2, 5), Fr(7, 10), 6, 22, "L_2"))
    res["best_six_row F22|F6"] = readout(compute2(0.5625, 2.6, *F, 22, 6, "L_2"))
    res["best_six_row F6|F6"] = readout(compute2(0.5625, 2.6, *F, 6, 6, "L_2"))
    res["best_six_row F22|F22"] = readout(compute2(0.5625, 2.6, *F, 22, 22, "L_2"))
    res["best_six_row F6|F22 c=1"] = readout(compute2(0.5625, 2.6, *F, 6, 22, "L_2"), c=1.0)
    q1 = []
    for (a, b, re_t, im_t, h) in ((Fr(2, 5), Fr(1, 10), 0.5625, 2.6, "L_2"), (Fr(2, 5), Fr(3, 10), 0.3, 2.2, "L_max"), (Fr(1, 7), Fr(3, 7), 0.8, 3.1, "L_2"),
                                  (Fr(1, 3), Fr(0), 0.1, 2.5, "L_max"), (Fr(3, 11), Fr(5, 11), 0.45, 2.9, "L_2"), (Fr(0), Fr(1, 2), 0.7, 3.4, "L_max")):
        for ad in (22, 6, -2):
            r = compute2(re_t, im_t, a, b, 6, ad, h)
            q1.append({"line": [str(a), str(b)], "tau": [re_t, im_t], "hor": h, "H_d": ad, "ln(D/9)": readout(r)["D"] and math.log(readout(r)["D"] / 9),
                       "down": r["down"], "lep": r["lep"]})
    res["Q1"] = q1
    sens = []
    for dre, dim in ((0, 0), (0.02, 0), (-0.02, 0), (0, 0.02), (0, -0.02), (-0.02, 0.02), (0.02, -0.02), (-0.02, -0.02), (0.02, 0.02), (-0.02, 0)):
        r = readout(compute2(0.5625 + dre, 2.6 + dim, *F, 6, 22, "L_2"))
        sens.append({"dRe": dre, "dIm": dim, "chi2_six": round(r["chi2_six"], 3), "worst_six": round(r["worst_six"], 4)})
    res["sensitivity"] = sens
    out = pathlib.Path(__file__).resolve().parent / "repro.json"
    out.write_text(json.dumps(res, indent=1, default=str) + "\n")
    for k, v in res.items():
        if k in ("Q1", "sensitivity"):
            for x in v: print(k, x)
        else: print(k, v)
