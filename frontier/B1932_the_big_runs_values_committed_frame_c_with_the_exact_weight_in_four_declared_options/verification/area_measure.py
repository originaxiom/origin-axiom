"""Measure (b), the area (Liouville) average of the averaged frame over the modular surface, for both channel weights
(truncated, as in frame C; exact, Theorem 90's form) and both Higgs worlds; canonical end, horocycle of length 2.
<F>_b = (3/pi) * integral over the fundamental domain of F-bar dx dy / y^2.
- below Im tau = 6: B1928's grid (truncated) and fiber_grid_t90.json (exact), linear interpolation, Gauss-Legendre in x
  and in y on [sqrt(1 - x^2), 6];
- above 6: F-bar computed here at heights 6 to 45 (x-averaged over five columns), the end above 6 bracketed two ways:
  (i) held at its height-6 value (the canonical end's own extrapolation), (ii) continued on the trend A + B/y fitted to
  B1667's and B1927's values at heights 3 to 6; beyond 45, F-bar held at its height-45 value (weight 3/(45 pi)).
Prints only the differences (b against a; exact against truncated; the two end brackets); values go to the json.
Firewall: nothing compared with any measured value."""
import json, math, pathlib, sys
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
V = next((ROOT / "frontier").glob("B1928_*")) / "verification"
sys.path.insert(0, str(V))
HERE = pathlib.Path(__file__).resolve().parent
import fiber_grid as FG
import fiber_grid_t90 as G90          # importing patches the channel norm to Theorem 90's form (the exact weight)
CR, C, Bm = FG.CR, FG.C, G90.Bm
KEYS = ["up|L_2|St", "up|L_2|S", "down|L_2|S", "down|L_2|St", "ckm|L_2|St|S", "ckm|L_2|S|St"]


def build(path):
    G = json.loads(path.read_text()); XY = np.array([g["tau"] for g in G])
    Vv = np.array([np.concatenate([np.array(g["F"]["canon"][k]) for k in KEYS]) for g in G])
    return LinearNDInterpolator(XY, Vv), NearestNDInterpolator(XY, Vv)


def ev(I, pts):
    v = I[0](pts); bad = ~np.all(np.isfinite(v), axis=1)
    if bad.any():
        v[bad] = I[1](pts[bad])
    return v


def lower(I, nx=48, ny=48):
    xg, wx = leggauss(nx); yg, wy = leggauss(ny); tot = 0
    for x, w1 in zip(0.5 * xg, 0.5 * wx):
        y0 = math.sqrt(1 - x * x); ys = 0.5 * (6 - y0) * yg + 0.5 * (6 + y0); ws = 0.5 * (6 - y0) * wy
        v = ev(I, np.array([[x, y] for y in ys]))
        tot = tot + w1 * (ws[:, None] / ys[:, None] ** 2 * v).sum(0)
    return tot


def fbar_at(y, L2, exact):
    acc = 0
    for x in (-0.5, -0.25, 0.0, 0.25, 0.5):
        t = complex(x, y); L = CR.canon(t); L.pop("_extrapolated"); L["L_2"] = L2
        G90.L2_NOW[0] = L2
        Bm.cA = G90.cA_t90 if exact else G90.FAST
        o = 0
        for a, b in FG.POINTS:
            f = C.frame(t, a, b, L); o = o + np.concatenate([np.array(f[k]) for k in KEYS]) / len(FG.POINTS)
        acc = acc + o / 5
    return acc


if __name__ == "__main__":
    ys_fit = np.array([3.0, 3.5, 4.0, 4.5, 5.0, 6.0]); L2s = np.array([CR.canon(complex(0.0, y))["L_2"] for y in ys_fit])
    A = np.vstack([np.ones_like(ys_fit), 1 / ys_fit]).T; (a0, b0), *_ = np.linalg.lstsq(A, L2s, rcond=None)
    L2_6 = CR.canon(complex(0.0, 6.0))["L_2"]
    H = [6, 7, 8, 10, 13, 17, 22, 30, 45]
    out = {"keys": KEYS, "trend": [a0, b0], "L2_at_6": L2_6}
    for exact, path in ((False, V / "fiber_grid_fine.json"), (True, HERE / "fiber_grid_t90.json")):
        low = lower(build(path))
        for bracket in ("held", "trend"):
            F = [fbar_at(y, (L2_6 if bracket == "held" else a0 + b0 / y), exact) for y in H]
            tail = sum(0.5 * (F[i] / H[i] ** 2 + F[i + 1] / H[i + 1] ** 2) * (H[i + 1] - H[i]) for i in range(len(H) - 1)) + F[-1] / H[-1]
            Fb = (3 / math.pi) * (low + tail)
            out["%s|%s" % ("exact" if exact else "truncated", bracket)] = Fb.tolist()
            print("%s weight, end above 6 %s: done; tail share of the area weight %.3f" % ("exact" if exact else "truncated", bracket, (3 / math.pi) / 6), flush=True)
    e_h, e_t = np.array(out["exact|held"]), np.array(out["exact|trend"]); t_h = np.array(out["truncated|held"])
    print("max |d ln| between the end's two brackets (exact weight): %.2e" % float(np.max(np.abs(np.log(e_t / e_h)))))
    print("max |d ln| exact against truncated weight (held): %.2e" % float(np.max(np.abs(np.log(e_h / t_h)))))
    (HERE / "area_measure.json").write_text(json.dumps(out, indent=1))
