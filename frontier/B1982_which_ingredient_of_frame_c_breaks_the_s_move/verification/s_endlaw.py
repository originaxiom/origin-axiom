"""B1982 correction (main, 2026-11-25; data-free): frame C under the S move with the record's end law L(-1/tau) = L(tau) +
log|tau| (B1667; B1724; B1921), and V3 (a0 dropped) under the same law; V1 (no norm) as the control. See ../CORRECTION_CARD.md.
    python3 -B s_endlaw.py > s_endlaw_run.txt"""
import sys, pathlib, math, time
from multiprocessing import Pool
sys.path.insert(0, str(next((pathlib.Path(__file__).resolve().parents[2]).glob("B1980_*")) / "verification"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import duality_cov as D
import ablate as AB
mp = D.mp
def outputs(arg):
    x, y, a, b, L, vname = arg
    return AB.outputs((x, y, a, b, L, vname))
if __name__ == "__main__":
    t0 = time.time(); res = {}
    with Pool(6) as pool:
        for vname in ("V0", "V3", "V1"):
            r = []
            for (y, yp) in ((1.25, 0.8), (1.5, 1 / 1.5), (2.5, 0.4)):
                Ls = D.L_code("0", y); Lp = Ls + math.log(y)
                src = dict(zip(D.P96, pool.map(outputs, [("0", y, a, b, Ls, vname) for (a, b) in D.P96], chunksize=8)))
                par = dict(zip(D.E30, pool.map(outputs, [("0", yp, a, b, Lp, vname) for (a, b) in D.E30], chunksize=8)))
                big, med = D.match(src, par); r.append(big)
                print("%s, the end law L(i/y) = L(iy) + log y: S move %.4f against %.4f (L %.6f, %.6f): largest d %.1e, median %.1e  [%.0f s]" % (vname, y, yp, Ls, Lp, big, med, time.time() - t0), flush=True)
            res[vname] = r
    print("SUMMARY L1: frame C (V0) passes S with the record's end law: %s %s" % (all(x < 1e-8 for x in res["V0"]), ["%.1e" % x for x in res["V0"]]))
    print("SUMMARY V3 (a0 dropped) passes: %s %s" % (all(x < 1e-8 for x in res["V3"]), ["%.1e" % x for x in res["V3"]]))
    print("SUMMARY L2: V1 (no norm) fails as before: %s %s" % (all(x > 1e-2 for x in res["V1"]), ["%.1e" % x for x in res["V1"]]))
