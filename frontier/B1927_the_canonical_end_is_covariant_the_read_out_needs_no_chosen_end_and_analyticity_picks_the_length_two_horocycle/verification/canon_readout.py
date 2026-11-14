"""The read-out on the whole with the CANONICAL end (B1667's geometric end, point by point), instead of a chosen constant.

Written before the run (P-845; B1924's correction). At each node of a thread the modulus is carried into the fundamental
domain with the line (B1724's transport), and the frame is read there with the end L = L_max(tau_FD) or L_2(tau_FD) from
B1667's instrument (interpolated on `grid.json` and B1667's sealed points; mirror-symmetric in Re tau). Because the
canonical end is covariant, its invariant form is a modular function, so the frame read this way repeats along a thread
at its own line with no constant to choose: the two conventions (maximal horoball; horocycle of length 2) are the only
choice left, both carried.
EXPECTATIONS: (E1) periodicity on the golden thread at the mark: outputs at tau and gamma tau equal to 1e-8 (the
interpolation is single-valued on the domain); (E2) the read-out at n = 16 and n = 22 (60 words each, the mark and the
twin) agrees between n within errors, and the twins are not told apart at n = 22 (paired). Not expected either way:
whether it agrees with B1924's constant-end values (it need not; the end is different).
Values: the json only. Printed: structure only. Nothing compared with a measured number."""
import json, math, pathlib, random, sys
import numpy as np
from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1924_*")) / "verification"))
import thread_average as T
import whole_average as WA            # patches the frame with the closed-form channel norm
C = T.C

pts = json.loads((HERE / "grid.json").read_text())["grid"]
pts = [p for p in pts if "L_max" in p]
B = json.loads((ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json").read_text())["points"]
pts += [p for p in B if "L_max" in p]
XY = np.array([(s * p["tau"][0], p["tau"][1]) for p in pts for s in (1, -1)])
LM = np.array([p["L_max"] for p in pts for s in (1, -1)])
L2 = np.array([p["L_2"] for p in pts for s in (1, -1)])
YMAX = float(XY[:, 1].max())
INTERP = {name: (LinearNDInterpolator(XY, V), NearestNDInterpolator(XY, V)) for name, V in (("L_max", LM), ("L_2", L2))}


def canon(t):
    x, y = t.real, t.imag
    yq = min(y, YMAX)
    out = {}
    for name, (lin, near) in INTERP.items():
        v = float(lin(x, yq))
        if not np.isfinite(v):
            v = float(near(x, yq))
        out[name] = v
    out["_extrapolated"] = y > YMAX
    return out


EXTRAP = {"count": 0, "nodes": 0}


def outputs(t):
    tr, a, b, _ = T.reduce(complex(t), T.MARK[0], T.MARK[1], {"L_max": 0.0, "L_2": 0.0})
    L = canon(tr); EXTRAP["nodes"] += 1; EXTRAP["count"] += L.pop("_extrapolated")
    out = C.frame(tr, a, b, L)
    return {k: v for k, v in out.items() if "conjS" not in k}


def thread_mean(w):
    beta, betap, ell, g = T.geodesic(w)
    zt = lambda s: complex((beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1))
    s0 = -ell / 2
    if abs(g(zt(s0)) - zt(s0 + ell)) > 1e-7 * (1 + abs(zt(s0))):
        ell = -ell
    nodes = max(64, int(30 * abs(ell)))
    acc = None
    for j in range(nodes):
        o = outputs(zt(s0 + ell * j / nodes))
        if acc is None:
            acc = {k: np.zeros(len(v)) for k, v in o.items()}
        for k in acc:
            acc[k] += np.array(o[k]) / nodes
    return acc, abs(ell), nodes


def run(words, mark):
    T.MARK = mark
    rows = []
    for w in words:
        A, ell, nodes = thread_mean(w)
        rows.append({"word": w, "length": ell, "A": {k: v.tolist() for k, v in A.items()}})
    keys = rows[0]["A"].keys(); wts = np.array([r["length"] for r in rows])
    R = {k: np.sum([wt * np.array(r["A"][k]) for wt, r in zip(wts, rows)], 0) / wts.sum() for k in keys}
    jk = []
    for i in range(len(rows)):
        m = np.ones(len(rows), bool); m[i] = False
        jk.append({k: np.sum([wt * np.array(r["A"][k]) for wt, r, keep in zip(wts, rows, m) if keep], 0) / wts[m].sum() for k in keys})
    se = {k: np.sqrt((len(rows) - 1) * np.mean([(j[k] - R[k]) ** 2 for j in jk], 0)) for k in keys}
    return rows, R, se


if __name__ == "__main__":
    out = {}
    # (E1) periodicity on the golden thread at the mark
    T.MARK = (0.4, 0.8)
    beta, betap, ell, g = T.geodesic("LR")
    worst = 0.0
    for s in (-0.3, 0.1, 0.4):
        z = complex((beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1))
        o1, o2 = outputs(z), outputs(g(z))
        worst = max(worst, max(float(np.max(np.abs(np.log(np.array(o1[k]) / np.array(o2[k]))))) for k in o1 if min(o1[k]) > 1e-12 and min(o2[k]) > 1e-12))
    print("E1, periodicity at the golden thread's own line with the canonical end: largest |log ratio| %.1e" % worst, flush=True)
    out["E1"] = worst
    for n, seed in ((16, 9161), (22, 9221)):
        rng = random.Random(seed); words = []
        while len(words) < 60:
            w = "".join(rng.choice("LR") for _ in range(n))
            if "L" in w and "R" in w and T.keeps_mark(w):
                words.append(w)
        for name, mark in (("mark", (0.4, 0.8)), ("twin", (0.2, 0.4))):
            rows, R, se = run(words, mark)
            out["%d %s" % (n, name)] = {"rows": rows, "R": {k: v.tolist() for k, v in R.items()}, "se": {k: v.tolist() for k, v in se.items()}}
            print("n = %d, %s: 60 words; largest sampling error %.1e; nodes past the grid's top (end held at its last value): %d of %d"
                  % (n, name, max(float(np.max(v)) for v in se.values()), EXTRAP["count"], EXTRAP["nodes"]), flush=True)
            (HERE / "canon_readout.json").write_text(json.dumps(out, indent=1))
