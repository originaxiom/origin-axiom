#!/usr/bin/env python3
"""WEIGHT PENCIL (POST HOC reconnaissance, labelled; committed before its run, its output committed before it is read).
The modular-covariant (Maass-Shimura) derivative of main's R taken in weight w,
    h_w = delta_w(eta^(2w+1) R) / eta^(2w+1) = DR + (w/12) E2* R,      E2* = E2 - 3/(pi Im tau),
is covariant for every w (E2* has weight 2; R.R = 0 and R.DR = 0, so h_w.h_w = DR.DR for every w); w = 0 is main's DR
(the holomorphic Serre derivative), w = -1/2 the Maass derivative of R itself, w = 1 that of the theta squares.  Its e1
admixture grows with w toward the point where its leading null part vanishes (w (1 - 3/(pi y)) = 1 at the cusp).
On the stored channel grid, every pair (w_u, w_d) in {-1, -1/2, 0, 1/2, 1, 3/2, 2}^2, each direction oriented to be
led by h0 (the aligned reading; the leptons with H_d; c = 3): the nine and B1720's chi2 at every point and horocycle.
Also: each h_w's departures from its leading null line at Im tau 2.2, 2.7, 3.2 (data-free).
    python3 -B weight_pencil.py --grid two_higgs      # writes weight_pencil_<grid>.json"""
import contextlib, importlib.util, io, json, math, sys, pathlib
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
_argv = sys.argv; sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("rp", HERE / "record_pairs.py"); rp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rp)
_spec2 = importlib.util.spec_from_file_location("zfc", HERE.parent / "chat1_2026-10-23_zero_free_frame" / "zero_free_census.py")
zfc = importlib.util.module_from_spec(_spec2)
with contextlib.redirect_stdout(io.StringIO()):
    _spec2.loader.exec_module(zfc)
sys.argv = _argv
rbs = zfc.rbs
mp.mp.dps = 30
WS = [-1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]
F1, F2, F3 = rp.F1, np.array([1, 0, 0], dtype=complex), rp.F3


def E2(t):
    q = mp.exp(2j * mp.pi * t)
    return complex(1 - 24 * mp.fsum(n * q ** n / (1 - q ** n) for n in range(1, 80)))


def h_w(w, re_t, im_t, cache={}):
    key = (re_t, im_t)
    if key not in cache:
        t = complex(re_t, im_t)
        cache[key] = (rbs.at(rbs.R, re_t, im_t), rbs.at(rbs.H1, re_t, im_t), E2(t) - 3 / (math.pi * im_t))
    R, DR, e2s = cache[key]
    v = DR + (w / 12) * e2s * R
    v = v / np.linalg.norm(v)
    return v if abs(np.vdot(F3, v)) >= abs(np.vdot(F1, v)) else np.conj(v)


def dep(v):
    c = np.array([np.vdot(F2, v), np.vdot(F3, v), np.vdot(F1, v)])
    lead = 1 if abs(c[1]) >= abs(c[2]) else 2
    return abs(c[0] / c[lead]), abs(c[3 - lead] / c[lead])


def main():
    gname = sys.argv[sys.argv.index("--grid") + 1]
    st = np.load(HERE / f"channel_store_{gname}.npz"); U = st["U"]
    I = json.loads((HERE / f"channel_store_{gname}_index.json").read_text())
    tasks, lines, hors = I["tasks"], I["lines"], I["hors"]
    out = {"grid": gname, "weights": WS, "departures (delta / r^(1/2), eps / r) at Re tau 0.3": {}}
    for w in WS:
        row = {}
        for y in (2.2, 2.7, 3.2):
            r = math.exp(-math.pi * y); d, e = dep(h_w(w, 0.3, y))
            row[str(y)] = [round(d / r ** 0.5, 3), round(e / r, 3), round(d, 4)]
        out["departures (delta / r^(1/2), eps / r) at Re tau 0.3"][str(w)] = row
    best, counts, min6, rows = {}, {}, {}, []
    for p in range(len(tasks)):
        k, re_t, im_t = tasks[p]
        hs = {w: h_w(w, re_t, im_t) for w in WS}
        for ih in range(len(hors)):
            Uh = U[p, :, ih]
            for wu in WS:
                for wd in WS:
                    L, J = rp.nine(Uh, hs[wu], hs[wd])
                    c9 = float(np.sum(((L - rp.T9) / rp.SIG) ** 2)); c6 = float(np.sum(((L[:6] - rp.T6) / rp.SIG[:6]) ** 2))
                    key = f"{wu} | {wd}"
                    rec = {"chi2_nine": c9, "chi2_six": c6, "at": [lines[k], re_t, im_t, hors[ih]],
                           "model/data": [round(float(q), 3) for q in np.exp(L - rp.T9)], "J": J,
                           "D": math.exp((L[4] - L[2]) + (L[3] - L[5]))}
                    counts[key] = counts.get(key, 0) + int(c9 < 21.67)
                    min6[key] = min(min6.get(key, 1e99), c6)
                    if key not in best or c9 < best[key]["chi2_nine"]:
                        best[key] = rec
                    if c9 < 40:
                        rows.append(dict(rec, pair=key))
    for key in best:
        best[key]["rows below 21.67"] = counts[key]; best[key]["lowest chi2_six"] = min6[key]
    out["per pair (w_u | w_d): the lowest chi2_nine and its row; rows below 21.67; the lowest chi2_six"] = dict(sorted(best.items(), key=lambda kv: kv[1]["chi2_nine"]))
    out["rows below chi2_nine 40, the 40 lowest"] = sorted(rows, key=lambda r: r["chi2_nine"])[:40]
    (HERE / f"weight_pencil_{gname}.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
    print("written", flush=True)


if __name__ == "__main__":
    main()
