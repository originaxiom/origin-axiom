"""CHECK 3 (agy Theorem 21 Part A; P-355 owed item; P-593 'Theorem 18C on the 40 half-lift points').  Data-free.
MAIN's code only (residues, cA, weighted_M, coupling, UNITS, QI/QJ/QK; main's line convention w = p1 tau - p2).

The 40 beta-half-lifts of S297: 24 of order 10, (p/5, odd/10) without (0, 1/2); 16 of order 8, (p/4, odd/8).
Claims tested:
 (R) residues: order 10: (R1, Rj, Ri, Rk)^e = lam10 (+R1, +Rj, -Ri, +Rk)^d, lam10 = exp(2 pi i p(2q+1)/5);
               order 8 : (R1, Rj, Ri, Rk)^e = lam8 (+R1, -Rj, +Ri, -Rk)^d, lam8 = -exp(-i pi p(2q+1)/2).
     (c_s is sector-blind, check 1, so the channel vectors u_s = sqrt(2 pi L + c_s) R_s obey the same law.)
 (Y) main's coupling (linear in M): for ANY Higgs S = a0 1 + h_i QI + h_j QJ + h_k QK, the lepton spectrum equals the
     down spectrum of the reflected Higgs: order 10: S -> (a0, -h_i, h_j, h_k); order 8: S -> (a0, h_i, -h_j, -h_k).
     Matrix form searched over the eight sign diagonals D: Y_e(S) = mu D Y_d(Sigma S)^T D (order 10, transposed) or
     Y_e(S) = mu D Y_d(Sigma S) D (order 8, plain).
 (Q) corollary: a Higgs with no QI component and a0 = 0 gives identical spectra on all 40 (S297); with a0 != 0 the
     order-8 reflection (h_j, h_k) -> -(h_j, h_k) is not a symmetry, so an order-8 point with h_i = 0, a0 != 0 splits.
 Controls: four non-half-lift points (the same tests must fail), and the unreflected Higgs (must split when h_i != 0).
"""
import cmath, itertools, json, math, pathlib
import numpy as np
import mainB

B = mainB.B()
HERE = pathlib.Path(__file__).resolve().parent
rng = np.random.default_rng(355)
L = 2.36
KEYS = ["1", "j", "i", "k"]


def sector_data(p1, p2, t):
    w = B.line_w(p1, p2, t); out = {}
    for sec in ("down", "lepton"):
        ql, qr = mainB.SECTORS[sec]; x, y = B.sector_twists(w, t, ql, qr); out[sec] = B.residues(x, y, t)
    x, y = B.sector_twists(w, t, 1, 2); c = B.cA(x, y, t, out["down"])
    return out, c


def Y_of(S, R, c):
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    return B.coupling(S, B.weighted_M(u))


def S_of(a0, hi, hj, hk):
    return a0 * B.UNITS["1"] + hi * B.QI + hj * B.QJ + hk * B.QK


def sv(Y):
    return np.sort(np.linalg.svd(Y, compute_uv=False))


DIAGS = [np.diag(s) for s in itertools.product((1, -1), repeat=3)]


def matrix_form(Ye, Yd_ref, transpose):
    best = (1e9, None, None)
    M = Yd_ref.T if transpose else Yd_ref
    for D in DIAGS:
        Z = D @ M @ D; mu = np.vdot(Z.ravel(), Ye.ravel()) / np.vdot(Z.ravel(), Z.ravel())
        err = float(np.max(np.abs(Ye - mu * Z)) / np.max(np.abs(Ye)))
        if err < best[0]:
            best = (err, np.diag(D).tolist(), complex(mu))
    return best


def test_point(p1, p2, order, t, higgs):
    R, c = sector_data(p1, p2, t); Rd, Re = R["down"], R["lepton"]
    if order == 10:
        p, q = round(p1 * 5), round((p2 * 10 - 1) / 2); lam = cmath.exp(2j * math.pi * p * (2 * q + 1) / 5)
        sig = {"1": 1, "j": 1, "i": -1, "k": 1}
    else:
        p, q = round(p1 * 4), round((p2 * 8 - 1) / 2); lam = -cmath.exp(-0.5j * math.pi * p * (2 * q + 1))
        sig = {"1": 1, "j": -1, "i": 1, "k": -1}
    scale = max(abs(Rd[k]) for k in KEYS)
    res_err = max(abs(Re[k] - lam * sig[k] * Rd[k]) for k in KEYS) / scale
    out = {"res_err": res_err}
    ysp, ysp_ctrl, mform = 0.0, 1e9, 0.0
    for (a0, hi, hj, hk) in higgs:
        S = S_of(a0, hi, hj, hk)
        Sr = S_of(a0, -hi, hj, hk) if order == 10 else S_of(a0, hi, -hj, -hk)
        Ye, Ydr, Yd = Y_of(S, Re, c), Y_of(Sr, Rd, c), Y_of(S, Rd, c)
        top = sv(Ye)[-1]
        ysp = max(ysp, float(np.max(np.abs(sv(Ye) - sv(Ydr))) / top))
        ysp_ctrl = min(ysp_ctrl, float(np.max(np.abs(sv(Ye) - sv(Yd))) / top))
        mf = matrix_form(Ye, Ydr, transpose=(order == 10)); mform = max(mform, mf[0]); out["D_mu"] = (mf[1], str(mf[2]))
    out["spec_err_reflected"] = ysp; out["spec_split_unreflected_min"] = ysp_ctrl; out["matrix_form_err"] = mform
    # (Q) QI-free, a0 = 0; and QI-free with a0 != 0
    hj, hk = rng.normal(size=2) + 1j * rng.normal(size=2)
    for tag, a0 in (("qi_free_a0_0", 0.0), ("qi_free_a0_nonzero", 0.37 - 0.21j)):
        S = S_of(a0, 0.0, hj, hk); Ye, Yd = Y_of(S, Re, c), Y_of(S, Rd, c)
        out[tag] = float(np.max(np.abs(sv(Ye) - sv(Yd))) / sv(Ye)[-1])
    return out


higgs = [tuple(complex(*rng.normal(size=2)) for _ in range(4)) for _ in range(3)]
pts10 = [(p / 5, (2 * q + 1) / 10) for p in range(5) for q in range(5) if not (p == 0 and 2 * q + 1 == 5)]
pts8 = [(p / 4, (2 * q + 1) / 8) for p in range(4) for q in range(4)]
ctrl = [((2 / 5), 1 / 5, 10), ((2 / 5), 1 / 7, 10), (0.25, 1 / 6, 8), (0.3, 0.1, 10)]
res = {"order10": {}, "order8": {}, "controls": {}}
for t in (0.23 + 1.85j, 0.61 + 2.7j):
    for (p1, p2) in pts10:
        res["order10"][f"{p1:.2f},{p2:.2f},{t}"] = test_point(p1, p2, 10, t, higgs)
    for (p1, p2) in pts8:
        res["order8"][f"{p1:.2f},{p2:.3f},{t}"] = test_point(p1, p2, 8, t, higgs)
    for (p1, p2, o) in ctrl:
        res["controls"][f"{p1:.2f},{p2:.3f},{t},as{o}"] = test_point(p1, p2, o, t, higgs)
summ = {}
for grp in ("order10", "order8", "controls"):
    v = list(res[grp].values())
    summ[grp] = {"n": len(v), "max_res_err": max(x["res_err"] for x in v), "min_res_err": min(x["res_err"] for x in v),
                 "max_spec_err_reflected": max(x["spec_err_reflected"] for x in v),
                 "min_spec_err_reflected": min(x["spec_err_reflected"] for x in v),
                 "min_split_unreflected": min(x["spec_split_unreflected_min"] for x in v),
                 "max_matrix_form_err": max(x["matrix_form_err"] for x in v),
                 "D_found": sorted(set(str(x["D_mu"][0]) for x in v)),
                 "max_qi_free_a0_0": max(x["qi_free_a0_0"] for x in v),
                 "min_qi_free_a0_nonzero": min(x["qi_free_a0_nonzero"] for x in v),
                 "max_qi_free_a0_nonzero": max(x["qi_free_a0_nonzero"] for x in v)}
    print(grp, summ[grp], flush=True)
(HERE / "check3_t21_half_lifts_out.json").write_text(json.dumps({"summary": summ, "points": res}, indent=1, default=str))
