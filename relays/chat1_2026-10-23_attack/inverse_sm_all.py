#!/usr/bin/env python3
"""INVERSE SM, ALL ROWS (POST HOC reconnaissance, labelled; committed before its run, its output committed before it is
read).  inverse_higgs.py optimised only the 160 (point, horocycle) rows that its null-Higgs screen ranked best, a screen
built for equal readings; this script removes that bias for the Standard Model's reading.  On every point and both
horocycles of the stored grid (2 560 rows): the lowest chi2_nine over a free Higgs direction h, the up quarks seeing
conj h and the down quarks and leptons h (c = 3), by inverse_higgs.solve() from twelve starts (DR, F_6, F_-2, h2, h3 and
F_22, each as is and conjugated) and the six-only minimum from the nine's optimum.  Two worker processes.
    python3 -B inverse_sm_all.py --grid two_higgs      # writes inverse_sm_all_<grid>.json"""
import importlib.util, json, math, sys, time, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
_argv = sys.argv; sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("ih", HERE / "inverse_higgs.py"); ih = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ih)
sys.argv = _argv
STARTS = ["dR", "F_6", "F_-2", "h2", "h3", "F_22"]
G = {}


def init(gname):
    st = np.load(HERE / f"channel_store_{gname}.npz"); G["U"], G["H"] = st["U"], st["H"]
    G["I"] = json.loads((HERE / f"channel_store_{gname}_index.json").read_text())


def one(args):
    p, ih_ = args
    U, H, I = G["U"], G["H"], G["I"]
    Uh = U[p, :, ih_]; Hp = H[p]; D = I["dirs"]
    starts = [ih.unvec(Hp[D.index(d)]) for d in STARTS] + [ih.unvec(np.conj(Hp[D.index(d)])) for d in STARTS]
    best, dirs = ih.solve("SM", Uh, starts)
    hu, hd = dirs(best[1]); L, J, Dd = ih.nine(Uh, hu, hd)
    b6, _ = ih.solve("SM", Uh, [best[1]], six_only=True)
    return {"point": I["tasks"][p], "line": I["lines"][I["tasks"][p][0]], "hor": I["hors"][ih_],
            "min chi2_nine": round(best[0], 3), "chi2_six there": round(float(np.sum(((L[:6] - ih.T6) / ih.SIG[:6]) ** 2)), 3),
            "model/data": [round(float(q), 4) for q in np.exp(L - ih.T9)], "min chi2_six": round(b6[0], 3),
            "h": ih.decomp(hd)}


def main():
    from multiprocessing import Pool
    gname = sys.argv[sys.argv.index("--grid") + 1]
    init(gname)
    jobs = [(p, h) for p in range(len(G["I"]["tasks"])) for h in range(len(G["I"]["hors"]))]
    rows = []; t0 = time.time()
    with Pool(2, initializer=init, initargs=(gname,)) as P:
        for n, r in enumerate(P.imap(one, jobs, chunksize=8)):
            rows.append(r)
            if n % 200 == 0:
                print(f"{n + 1} of {len(jobs)}, {time.time() - t0:.0f} s", flush=True)
    vals = np.array([r["min chi2_nine"] for r in rows])
    out = {"grid": gname, "rows": len(rows), "lowest min chi2_nine": float(vals.min()),
           "quantiles of min chi2_nine (0, 1, 5, 50%)": [float(np.quantile(vals, q)) for q in (0, 0.01, 0.05, 0.5)],
           "rows below 21.67, 100, 500": [int((vals < b).sum()) for b in (21.67, 100, 500)],
           "the 15 lowest rows": sorted(rows, key=lambda r: r["min chi2_nine"])[:15],
           "lowest min chi2_six": min(r["min chi2_six"] for r in rows)}
    (HERE / f"inverse_sm_all_{gname}.json").write_text(json.dumps(out, indent=1, default=float) + "\n")
    print("written", flush=True)


if __name__ == "__main__":
    main()
