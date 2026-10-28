"""Step 4 (P-373), data-free: do natural functionals of B1656's frame single out a height Im tau?
On three slope-2/5 lines, at three Re tau, over Im tau 1.5-8 (step 0.25), with B1726's compute() internals (the record's Higgs
DR, the canonical horocycles from B1667's column -- clamped above Im tau 4 as the instrument does), per sector:
  F1 = sum_s c_s (the channel norms), F2 = |det M| (the weighted matrix), and per reading (S, S~):
  F3 = ||Y||_F, F4 = sum of singular values, F5 = sigma_max, F6 = sigma_max * (Im tau)^(w/2) for w = 0..4 (Petersson-like).
Reports, per functional, the interior extrema in Im tau (sign changes of the finite-difference slope) and the monotone runs.
No measured value is read.
    python3 -B functionals.py [--workers 6]"""
import sys, json, math, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
HERE = pathlib.Path(__file__).resolve().parent
LINES = [(Fr(2, 5), Fr(1, 10)), (Fr(2, 5), Fr(23, 30)), (Fr(2, 5), Fr(4, 25))]
RES = (0.1, 0.3, 0.7)
IMS = tuple(round(1.5 + 0.25 * k, 2) for k in range(27))
_C = {}


def census():
    if not _C:
        spec = importlib.util.spec_from_file_location("c26", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); _C["m"] = m
    return _C["m"]


def point(task):
    import mpmath as mp
    (a, b), re_t, im_t = task
    C = census(); M_ = C._modules(); B, te, col = M_["B"], M_["te"], M_["col"]
    t = complex(re_t, im_t); w = float(a) * t + float(b)
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    reading = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T}
    L = float(np.interp(im_t, [q[0] for q in col], [q[1] for q in col]))      # L_max, clamped above 4 as the instrument
    out = {"line": "%s,%s" % (a, b), "re": re_t, "im": im_t, "L_max": L}
    for sec, (lf, rf) in C.SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
        Mw = B.weighted_M(u)
        rec = {"F1_sum_c": float(sum(c[s] for s in B.UNITS if c[s] is not None)), "F2_detM": float(abs(np.linalg.det(Mw)))}
        for rn in ("S", "St"):
            Y = B.coupling(reading[rn], Mw); sv = np.linalg.svd(Y, compute_uv=False)
            rec["F3_frob_" + rn] = float(np.linalg.norm(Y)); rec["F4_nuc_" + rn] = float(sv.sum()); rec["F5_smax_" + rn] = float(sv[0])
        out[sec] = rec
    return out


def extrema(ys, vs):
    """interior extrema of v(y) on the grid: (y, kind) where the finite-difference slope changes sign"""
    d = np.diff(np.log(np.abs(vs) + 1e-300))
    ex = []
    for k in range(1, len(d)):
        if d[k - 1] > 0 and d[k] < 0: ex.append((ys[k], "max"))
        if d[k - 1] < 0 and d[k] > 0: ex.append((ys[k], "min"))
    trend = "up" if d.sum() > 0 else "down"
    return ex, trend


if __name__ == "__main__":
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    tasks = [(ln, r, y) for ln in LINES for r in RES for y in IMS]
    if nw > 1:
        import multiprocessing as mpp
        with mpp.Pool(nw) as P: rows = P.map(point, tasks, chunksize=4)
    else:
        rows = [point(t) for t in tasks]
    json.dump(rows, open(HERE / "functionals.json", "w"), indent=0)
    summary = {}
    for ln in LINES:
        for r in RES:
            sel = sorted([q for q in rows if q["line"] == "%s,%s" % ln and q["re"] == r], key=lambda q: q["im"])
            ys = [q["im"] for q in sel]
            for sec in ("up", "down", "lep"):
                for key in sel[0][sec]:
                    vs = np.array([q[sec][key] for q in sel])
                    ex, tr = extrema(ys, vs)
                    summary["%s,%s|%.1f|%s|%s" % (ln[0], ln[1], r, sec, key)] = {"extrema": ex, "trend": tr,
                        "range": [float(vs.min()), float(vs.max())]}
                if "F5_smax_S" in sel[0][sec]:
                    for wgt in (1, 2, 3, 4):
                        vs = np.array([q[sec]["F5_smax_St" if sec == "up" else "F5_smax_S"] * q["im"] ** (wgt / 2) for q in sel])
                        ex, tr = extrema(ys, vs)
                        summary["%s,%s|%.1f|%s|F6_smax_seat_x_y^%g" % (ln[0], ln[1], r, sec, wgt / 2)] = {"extrema": ex, "trend": tr}
    json.dump(summary, open(HERE / "functionals_summary.json", "w"), indent=1)
    n_ex = {k: v["extrema"] for k, v in summary.items() if v["extrema"]}
    print("functionals with an interior extremum in Im tau 1.5-8:", len(n_ex), "of", len(summary))
    for k, v in list(n_ex.items())[:60]: print("  ", k, v)
    print("functionals exit 0")
