"""The read-out on the whole with the exact channel weight against frame C as computed (B1928's ergodic integral, its
words, seed, threads and interpolation unchanged; canonical end, horocycle of length 2). The same 3000 words are used for
both grids, so the difference is paired. Prints only differences and sampling errors; the values go to the json.
Firewall: nothing compared with any measured value."""
import json, math, pathlib, random, sys
import numpy as np
from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
V = next((ROOT / "frontier").glob("B1928_*")) / "verification"
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1924_*")) / "verification"))
import thread_average as T
HERE = pathlib.Path(__file__).resolve().parent
CLAIMED = ["up|L_2|St", "down|L_2|S", "ckm|L_2|St|S", "up|L_2|S", "down|L_2|St", "ckm|L_2|S|St"]
NAMES = ["W- up r2", "W- up r1", "W- down r2", "W- down r1", "W- V12", "W- V23", "W- V13", "W+ up r2", "W+ up r1", "W+ down r2", "W+ down r1", "W+ V12", "W+ V23", "W+ V13"]


def build(path):
    G = json.loads(path.read_text()); XY = np.array([g["tau"] for g in G])
    Vv = np.array([np.concatenate([np.array(g["F"]["canon"][k]) for k in CLAIMED]) for g in G])
    return LinearNDInterpolator(XY, Vv), NearestNDInterpolator(XY, Vv)


def interp(I, pts):
    v = I[0](pts); bad = ~np.all(np.isfinite(v), axis=1)
    if bad.any():
        v[bad] = I[1](pts[bad])
    return v


def thread(w, per_unit=10):
    beta, betap, ell, g = T.geodesic(w)
    zt = lambda s: complex((beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1))
    nodes = max(32, int(per_unit * abs(ell))); s0 = -ell / 2
    pts = np.array([[r.real, r.imag] for r in (T.reduce(zt(s0 + ell * j / nodes), 0.0, 0.0, {"x": 0.0})[0] for j in range(nodes))])
    return pts, abs(ell)


if __name__ == "__main__":
    I0 = build(V / "fiber_grid_fine.json"); I1 = build(HERE / "fiber_grid_t90.json")
    rng = random.Random(1924); words = []
    while len(words) < 3000:
        w = "".join(rng.choice("LR") for _ in range(40))
        if "L" in w and "R" in w:
            words.append(w)
    A0, A1, wts = [], [], []
    for w in words:
        pts, ell = thread(w); A0.append(interp(I0, pts).mean(0)); A1.append(interp(I1, pts).mean(0)); wts.append(ell)
    A0, A1, wts = np.array(A0), np.array(A1), np.array(wts)
    R0 = (wts[:, None] * A0).sum(0) / wts.sum(); R1 = (wts[:, None] * A1).sum(0) / wts.sum()
    D = np.log(A1 / A0); Rd = np.log(R1 / R0)
    blocks = np.array_split(np.arange(len(words)), 30); jk0, jkd = [], []
    for bl in blocks:
        m = np.ones(len(words), bool); m[bl] = False
        r0 = (wts[m][:, None] * A0[m]).sum(0) / wts[m].sum(); r1 = (wts[m][:, None] * A1[m]).sum(0) / wts[m].sum()
        jk0.append(r0); jkd.append(np.log(r1 / r0))
    se0 = np.sqrt(29 * np.mean((np.array(jk0) - R0) ** 2, 0)); sed = np.sqrt(29 * np.mean((np.array(jkd) - Rd) ** 2, 0))
    for n, d, s, e in zip(NAMES, Rd, sed, se0 / R0):
        print("%-8s  d ln (exact weight - truncated) %+.4e  +- %.1e   (the read-out's own relative sampling error %.1e)" % (n, d, s, e))
    (HERE / "ergodic_both_worlds.json").write_text(json.dumps({"names": NAMES, "R_truncated": R0.tolist(), "R_exact_weight": R1.tolist(),
                                                       "dln": Rd.tolist(), "dln_se": sed.tolist(), "se_truncated": se0.tolist()}, indent=1))
