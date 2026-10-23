"""B1742: (A) the seat's TWO_HIGGS grid on main's instrument -- ten alpha = 2/5 lines x Re tau 0.0625..0.9375 (8) x
Im tau 2.0..3.5 (16) x both horocycles, the six off-diagonal pairs (H_u, H_d) from {F_6, F_-2, F_22}, all read S, c = 3:
min chi2_six, min chi2_nine (main's sigma), the rows below 16.75; (B) the D = 9 mechanism: a Higgs with no QI component."""
import sys, json, math, pathlib
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import repro as R

MENU = (6, -2, 22)
PAIRS = [(u, d) for u in MENU for d in MENU if u != d]
LINES = [(Fr(2, 5), Fr(k, 10)) for k in range(10)]
RES = [0.0625 + 0.125 * i for i in range(8)]
IMS = [round(2.0 + 0.1 * j, 10) for j in range(16)]


def channels(re_t, im_t, a, b):
    M = R.CEN._modules(); B, col = M["B"], M["col"]
    t = complex(re_t, im_t); w = float(a) * t + float(b); out = {}
    for sec, (lf, rf) in R.SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); Rr = B.residues(x, yy, t); c = B.cA(x, yy, t, Rr)
        for hor, ix in (("L_max", 1), ("L_2", 2)):
            L = float(np.interp(im_t, [q[0] for q in col], [q[ix] for q in col]))
            u = {s: (math.sqrt(2 * math.pi * L + c[s]) * Rr[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
            out[(sec, hor)] = B.weighted_M(u)
    return out


def rows(M, t, hs):
    B = R.CEN._modules()["B"]; res = []
    for hor in ("L_max", "L_2"):
        for au, ad in PAIRS:
            Yu = B.coupling(hs[au], M[("up", hor)]); Yd = B.coupling(hs[ad], M[("down", hor)]); Ye = B.coupling(hs[ad], M[("lep", hor)])
            r = {}
            for k, Y in (("up", Yu), ("down", Yd), ("lep", Ye)):
                sv = np.linalg.svd(Y, compute_uv=False); r[k] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
            Uu = np.linalg.svd(Yu)[0][:, ::-1]; Ud = np.linalg.svd(Yd)[0][:, ::-1]; V = np.conj(Uu.T) @ Ud
            r["ckm"] = [float(abs(V[0, 1])), float(abs(V[1, 2])), float(abs(V[0, 2])), float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))]
            res.append((hor, au, ad, r))
    return res


def point(task):
    k, re_t, im_t = task
    a, b = LINES[k]; t = complex(re_t, im_t); B = R.CEN._modules()["B"]
    M = channels(re_t, im_t, a, b); hs = {x: R.Smat(R.direction(x, t), B) for x in MENU}
    out = []
    for hor, au, ad, r in rows(M, t, hs):
        ro = R.readout(r)
        out.append({"line": k, "Re": re_t, "Im": im_t, "hor": hor, "pair": [au, ad], "chi2_six": ro["chi2_six"], "chi2_nine": ro["chi2_nine"],
                    "worst_six": ro["worst_six"], "worst_nine": ro["worst_nine"], "D": ro["D"], "ckm_over": ro["ckm_over_measured"], "J": ro["J"]})
    return out


def mechanism():
    """D with a Higgs (vi, vj, vk): vi = 0 exactly vs small, on alpha = 2/5 lines with k odd and even, and off them"""
    B = R.CEN._modules()["B"]; out = []
    rng = np.random.default_rng(7)
    for (a, b, re_t, im_t) in ((Fr(2, 5), Fr(1, 10), 0.5625, 2.6), (Fr(2, 5), Fr(2, 10), 0.3, 2.9), (Fr(2, 5), Fr(7, 10), 0.8, 2.3), (Fr(1, 7), Fr(3, 7), 0.8, 3.1)):
        M = channels(re_t, im_t, a, b)
        for vi in (0.0, 1e-8, 1e-4, 1e-2):
            for trial in range(2):
                vj, vk = rng.normal(size=2) + 1j * rng.normal(size=2)
                S = R.Smat([vi, vj, vk], B); r = {}
                for sec in ("down", "lep"):
                    sv = np.linalg.svd(B.coupling(S, M[(sec, "L_2")]), compute_uv=False); r[sec] = [sv[1] / sv[0], sv[2] / sv[0]]
                lnD9 = math.log((r["lep"][0] / r["lep"][1]) / (r["down"][0] / r["down"][1]))
                out.append({"line": [str(a), str(b)], "tau": [re_t, im_t], "vi": vi, "trial": trial, "ln(D/9)": lnD9,
                            "down_eq_lep_max_dln": max(abs(math.log(p / q)) for p, q in zip(r["down"], r["lep"]))})
    return out


if __name__ == "__main__":
    from multiprocessing import Pool
    HERE = pathlib.Path(__file__).resolve().parent
    mech = mechanism()
    for m in mech: print("mech", m, flush=True)
    tasks = [(k, r, y) for k in range(10) for r in RES for y in IMS]
    allr = []
    with Pool(8) as P:
        for i, o in enumerate(P.imap_unordered(point, tasks, chunksize=4)):
            allr += o
            if i % 160 == 0: print("points", i, flush=True)
    (HERE / "scan.json").write_text(json.dumps({"mechanism": mech, "rows": allr}) + "\n")
    best6 = min(allr, key=lambda r: r["chi2_six"]); best9 = min(allr, key=lambda r: r["chi2_nine"])
    below = [r for r in allr if r["chi2_six"] < 16.75]
    print("rows", len(allr))
    print("min chi2_six", best6)
    print("min chi2_nine", best9)
    print("rows below 16.75:", len(below), "pairs", sorted({tuple(r["pair"]) for r in below}), "Im", sorted({r["Im"] for r in below}), "hor", sorted({r["hor"] for r in below}),
          "lines", sorted({r["line"] for r in below}), "chi2 range", (round(min(r["chi2_six"] for r in below), 3), round(max(r["chi2_six"] for r in below), 3)) if below else None)
    for p in PAIRS:
        rp = [r for r in allr if tuple(r["pair"]) == p]
        print("pair", p, "min worst_six %.3f" % min(r["worst_six"] for r in rp), "min chi2_six %.2f" % min(r["chi2_six"] for r in rp), "min chi2_nine %.1f" % min(r["chi2_nine"] for r in rp))
    D22 = [abs(math.log(r["D"] / 9)) for r in allr if r["pair"][1] == 22]
    print("H_d = F_22: max |ln(D/9)| over the grid %.2e" % max(D22))
    print("both coarse bars (six within 2.0, nine within 2.5):", sum(1 for r in allr if r["worst_six"] <= 2.0 and r["worst_nine"] <= 2.5))
