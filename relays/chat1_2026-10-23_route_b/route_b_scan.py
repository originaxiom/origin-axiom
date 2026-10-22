#!/usr/bin/env python3
"""EXPLORATORY, labelled (route (b) of step 1 in chat1's plan; no cell, no seal, no data in the design): a
Georgi-Jarlskog-type Higgs built from the record's own weight-3/2 Higgs space, in main's frame.

The space.  With FK10's unit O(delta) the weight-3/2 sections of rho_T form a three-dimensional space (main's B1700,
exact), with basis
    h1 = DR (= dR, main's Higgs, line orders (1, -1, 3), the only member holomorphic off v+, m2/m3 ~ |q|^(1/2));
    h2 = E4^2 (E4 DR + E6 R / 12) / Delta,     h3 = E4 E6 (D^2R - E4 R / 48) / Delta    (orders (-7, -1, -5)).
All three carry the same multiplier, so any constant combination is covariant in main's frame.

The model.  A Pati-Salam-type Higgs: the (1,2,2) part along h1 with Clebsch 1 in every sector, and a (15,2,2) part
along a second direction s with the B - L Clebsch, 1 for quarks and -3 for leptons:
    S_quarks = S(h1) + kappa S(s),      S_leptons = S(h1) - 3 kappa S(s),
with S(v) = v_i Q_i + v_j Q_j + v_k Q_k as in main's frame.  s runs over h2, h3 and four unit-norm combinations
(h2 + e^{i psi} h3)/sqrt2 at tau (psi = 0, 90, 180, 270 degrees); kappa = rho e^{i phi} |h1(tau)| / |s(tau)|, with
log10 rho = -4.0, -3.9, ..., 1.0 and phi = 0, 15, ..., 345 degrees.  No by-hand factor on any output.
Two readings: S~ = eps S* eps^T for every sector (covariant, B1724), and main's (up S~, down and leptons S).
Everything else is main's B1720 instrument at 3412bf09d, unchanged (imported through two_ingredients_census).

Base points: the ten best six-rows of the sealed two-ingredient census (two_ingredients_after.json, all order-10
alpha = 2/5 lines near Im tau 2.5-2.8) and the tick's d = e line (2/5, 4/5) at 1/2 + i{2.9, 3.0, 3.1, 3.2}.

Controls (written to route_b_controls.json): B1700's line orders for h1, h2, h3; kappa = 0 against the census
instrument; s = h1 leaves every ratio unchanged; T-covariance of the mixed Higgs (tau -> tau + 1, b -> b - a).
    python3 -B route_b_scan.py      # writes route_b_scan.npz, route_b_scan_index.json, route_b_controls.json"""
import contextlib, importlib.util, io, json, math, pathlib
from fractions import Fraction as F
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
SEL = HERE.parent / "chat1_2026-10-22_selection_map"
_spec = importlib.util.spec_from_file_location("tic", SEL / "two_ingredients_census.py")
tic = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(tic)
B, TC, te, mp = tic.B, tic.TC, tic.te, tic.mp
QS = te.S
R, D1, D2 = te.B
e4, e6 = te.e4, te.e6
Delta = (e4 * e4 * e4 - e6 * e6) * QS.c(F(1, 1728))
Dinv = Delta.inv()
H1 = list(D1)
H2 = [Dinv * e4 * e4 * (e4 * D1[i] + e6 * R[i] * QS.c(F(1, 12))) for i in range(3)]
H3 = [Dinv * e4 * e6 * (D2[i] - e4 * R[i] * QS.c(F(1, 48))) for i in range(3)]
I = QS.c(0, 1)


def line_orders(a):
    return [a[0].ord(), (a[1] + I * a[2]).ord(), (a[1] - I * a[2]).ord()]


def at(sec, re_t, im_t):
    return np.array([complex(te.ev(c, mp.mpc(re_t, im_t))) for c in sec])


def S_of(v):
    return v[0] * B.QI + v[1] * B.QJ + v[2] * B.QK


def St(S):
    return B.EPS @ np.conj(S) @ B.EPS.T


def channels(re_t, im_t, a, b):
    t = complex(re_t, im_t); w = a * t + b; M = {}
    for sec, (lf, rf) in TC.SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); Rr = B.residues(x, yy, t); c = B.cA(x, yy, t, Rr)
        for which in ("L_max", "L_2"):
            L = TC.L_of(t.imag, which)
            u = {kk: (math.sqrt(2 * math.pi * L + c[kk]) * Rr[kk] if c[kk] is not None and 2 * math.pi * L + c[kk] > 0 else 0) for kk in B.UNITS}
            M[(sec, which)] = B.weighted_M(u)
    return M


def outputs(M, which, Sq, Sl, model):
    if model == "St_all":
        su, sd, sl = St(Sq), St(Sq), St(Sl)
    else:                                                      # main's readings
        su, sd, sl = St(Sq), Sq, Sl
    Yu, Yd, Yl = B.coupling(su, M[("up", which)]), B.coupling(sd, M[("down", which)]), B.coupling(sl, M[("lep", which)])
    out = []
    for Y in (Yu, Yd, Yl):
        s = np.linalg.svd(Y, compute_uv=False); out += [s[1] / s[0], s[2] / s[0]]
    return out + tic.ckm_left(Yu, Yd)


after = json.loads((SEL / "two_ingredients_after.json").read_text())
seen, BASE = set(), []
for r in after["ten_best_w6"]:
    key = (r["Re"], r["Im"], r["line_value"][1], r["line_value"][2])
    if key not in seen:
        seen.add(key); BASE.append((r["Re"], r["Im"], float(F(r["line_value"][1])), float(F(r["line_value"][2]))))
BASE += [(0.5, y, 0.4, 0.8) for y in (2.9, 3.0, 3.1, 3.2)]
RHO = [10 ** (-4 + 0.1 * k) for k in range(51)]
PHI = [math.radians(15 * k) for k in range(24)]
CANDS = ["h2", "h3", "c0", "c90", "c180", "c270"]
MODELS = ["St_all", "main"]
HORS = ["L_max", "L_2"]

if __name__ == "__main__":
    ctrl = {"line_orders": {"h1": line_orders(H1), "h2": line_orders(H2), "h3": line_orders(H3)},
            "expected_B1700": {"h1": [1, -1, 3], "h2": [-7, -1, -5], "h3": [-7, -1, -5]}}
    data = np.zeros((len(BASE), len(CANDS), len(RHO), len(PHI), len(HORS), len(MODELS), 10))
    norms = []
    for ib, (re_t, im_t, a, b) in enumerate(BASE):
        M = channels(re_t, im_t, a, b)
        v1, v2, v3 = at(H1, re_t, im_t), at(H2, re_t, im_t), at(H3, re_t, im_t)
        n1 = np.linalg.norm(v1)
        u2, u3 = v2 / np.linalg.norm(v2), v3 / np.linalg.norm(v3)
        dirs = {"h2": u2, "h3": u3}
        for ang in (0, 90, 180, 270):
            dirs[f"c{ang}"] = (u2 + np.exp(1j * math.radians(ang)) * u3) / math.sqrt(2)
        norms.append({"base": [re_t, im_t, a, b], "|h1|": float(n1), "|h2|": float(np.linalg.norm(v2)), "|h3|": float(np.linalg.norm(v3))})
        S1 = S_of(v1)
        if ib == 0:                                            # controls at the first base point
            ref = tic.evaluate(re_t, im_t, a, b)
            dev0 = 0.0
            for which in HORS:
                o = outputs(M, which, S1, S1, "St_all")
                vals = ref[f"up|{which}|St"] + ref[f"down|{which}|St"] + ref[f"lep|{which}|St"] + ref[f"ckm|{which}|St|St"][:3]
                dev0 = max(dev0, max(abs(math.log(x / y)) for x, y in zip(o[:9], vals)))
                o = outputs(M, which, S1, S1, "main")
                vals = ref[f"up|{which}|St"] + ref[f"down|{which}|S"] + ref[f"lep|{which}|S"] + ref[f"ckm|{which}|St|S"][:3]
                dev0 = max(dev0, max(abs(math.log(x / y)) for x, y in zip(o[:9], vals)))
            ctrl["kappa0_vs_census_max_abs_log"] = dev0
            devs = 0.0
            for kap in (0.3 + 0.2j, -0.05j, 1.7):
                for which in HORS:
                    for model in MODELS:
                        o0 = outputs(M, which, S1, S1, model)
                        o1 = outputs(M, which, S1 + kap * S1, S1 - 3 * kap * S1, model)
                        devs = max(devs, max(abs(math.log(x / y)) for x, y in zip(o0[:9], o1[:9])))
            ctrl["s_equals_h1_invariance_max_abs_log"] = devs
            Mt = channels(re_t + 1, im_t, a, b - a)
            w1, w2 = at(H1, re_t + 1, im_t), at(H2, re_t + 1, im_t)
            kap = 0.37 * np.exp(0.8j) * n1 / np.linalg.norm(v2)
            covdev = 0.0
            for which in HORS:
                for model in MODELS:
                    o0 = outputs(M, which, S1 + kap * S_of(v2), S1 - 3 * kap * S_of(v2), model)
                    o1 = outputs(Mt, which, S_of(w1) + kap * S_of(w2), S_of(w1) - 3 * kap * S_of(w2), model)
                    covdev = max(covdev, max(abs(math.log(x / y)) for x, y in zip(o0[:9], o1[:9])))
            ctrl["T_covariance_mixed_higgs_max_abs_log"] = covdev
            ctrl["T_covariance_section_ratio_check"] = {"|h1(tau+1)|/|h1(tau)|": float(np.linalg.norm(w1) / n1),
                                                        "|h2(tau+1)|/|h2(tau)|": float(np.linalg.norm(w2) / np.linalg.norm(v2))}
        for ic, cn in enumerate(CANDS):
            s = dirs[cn]
            for ir, rho in enumerate(RHO):
                for ip, phi in enumerate(PHI):
                    kap = rho * np.exp(1j * phi) * n1
                    Sq = S1 + kap * S_of(s); Sl = S1 - 3 * kap * S_of(s)
                    for ih, which in enumerate(HORS):
                        for im_, model in enumerate(MODELS):
                            data[ib, ic, ir, ip, ih, im_] = outputs(M, which, Sq, Sl, model)
        print(f"base {ib + 1}/{len(BASE)} done", flush=True)
    np.savez_compressed(HERE / "route_b_scan.npz", data=data)
    (HERE / "route_b_scan_index.json").write_text(json.dumps({"base": BASE, "cands": CANDS, "rho": RHO, "phi_deg": [15 * k for k in range(24)],
                                                              "hors": HORS, "models": MODELS, "norms": norms,
                                                              "fields": ["up m2/m3", "up m1/m3", "down m2/m3", "down m1/m3", "lep m2/m3", "lep m1/m3", "Vus", "Vcb", "Vub", "J"]}, indent=1) + "\n")
    (HERE / "route_b_controls.json").write_text(json.dumps(ctrl, indent=1, default=str) + "\n")
    print(json.dumps(ctrl, indent=1, default=str))
