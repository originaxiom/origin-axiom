"""Frame C with the exact channel weight (Theorem 90's leading form, N = 2 pi L_2 + c_s - pi |a0_s|^2 e^{-2 L_2}; checked
against the exact horoball norm to about 1e-5, t90_run.txt): F-bar, the frame averaged over the 24 points of order 5,
on B1928's grid, canonical end, horocycle of length 2 only (the L_max keys are copied from B1928's grid unchanged and
are not used). Writes fiber_grid_t90.json in B1928's grid format, so B1928's ergodic integral can read it.
    python3 -B fiber_grid_t90.py [--time]"""
import json, math, pathlib, sys, time
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
V = next((ROOT / "frontier").glob("B1928_*")) / "verification"
sys.path.insert(0, str(V))
import fiber_grid as FG
CR, C = FG.CR, FG.C
Bm = C._modules()["B"]
FAST = Bm.cA                     # B1924's closed-form channel norm, as patched by whole_average
L2_NOW = [None]


def cA_t90(x, yy, t, R, **kw):
    c = FAST(x, yy, t, R)
    a0 = Bm.a0_of(x, yy, t, R)
    return {s: (c[s] - math.pi * abs(a0[s]) ** 2 * math.exp(-2 * L2_NOW[0]) if c[s] is not None and a0[s] is not None else c[s])
            for s in c}


Bm.cA = cA_t90
HERE = pathlib.Path(__file__).resolve().parent


def fbar_t90(t):
    L = CR.canon(t); L.pop("_extrapolated"); L2_NOW[0] = L["L_2"]
    acc = None
    for a, b in FG.POINTS:
        o = {k: np.array(v) for k, v in C.frame(t, a, b, L).items() if "conjS" not in k and "L_2" in k}
        if acc is None:
            acc = {k: v / len(FG.POINTS) for k, v in o.items()}
        else:
            for k in acc:
                acc[k] += o[k] / len(FG.POINTS)
    return {k: v.tolist() for k, v in acc.items()}


if __name__ == "__main__":
    G = json.loads((V / "fiber_grid_fine.json").read_text())
    if "--time" in sys.argv:
        t0 = time.time(); f = fbar_t90(complex(*G[0]["tau"])); print("one point: %.1f s; keys %d" % (time.time() - t0, len(f))); sys.exit()
    out = []; t0 = time.time()
    for i, g in enumerate(G):
        new = fbar_t90(complex(*g["tau"]))
        canon = dict(g["F"]["canon"]); canon.update(new)
        out.append({"tau": g["tau"], "F": {"const": g["F"]["const"], "canon": canon}})
        if i % 50 == 0:
            print("%d/%d  %.0f s" % (i, len(G), time.time() - t0), flush=True)
    (HERE / "fiber_grid_t90.json").write_text(json.dumps(out))
    print("done %.0f s" % (time.time() - t0))
