"""The limit theorem's prediction, step 2 (written before the run): the integral of F-bar against the path measure, from
F-bar tabulated on the fundamental domain (fiber_grid.json) averaged along many UNCONSTRAINED random geodesics (uniform
letters; F-bar is SL(2,Z)-invariant, so every closed geodesic is a valid thread), set against B1924's read-outs.

EXPECTATIONS: (P1) the interpolation of F-bar is accurate to well below the read-outs' errors (checked against direct
evaluation at random points); (P2) with B1924's constant ends, the ergodic integral agrees with B1924's read-outs at the
mark and at the twin (n = 22, both samples, and n = 28) within their errors: median |z| near 0.67, few above 2. A clear
disagreement refutes the draft claim (DRAFT.md) or one of its hypotheses. Values: the json only."""
import json, math, pathlib, random, sys
import numpy as np
from scipy.interpolate import LinearNDInterpolator, NearestNDInterpolator
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1924_*")) / "verification"))
import thread_average as T

FINE = "--fine" in sys.argv
G = json.loads((HERE / ("fiber_grid_fine.json" if FINE else "fiber_grid.json")).read_text())
KEYS = list(G[0]["F"]["const"].keys())
SHAPES = [len(G[0]["F"]["const"][k]) for k in KEYS]
XY = np.array([g["tau"] for g in G])


def flat(d):
    return np.concatenate([np.array(d[k]) for k in KEYS])


INTERP = {}
for mode in ("const", "canon"):
    V = np.array([flat(g["F"][mode]) for g in G])
    INTERP[mode] = (LinearNDInterpolator(XY, V), NearestNDInterpolator(XY, V))


def fbar_interp(pts, mode):
    lin, near = INTERP[mode]
    v = lin(pts)
    bad = ~np.all(np.isfinite(v), axis=1)
    if bad.any():
        v[bad] = near(pts[bad])
    return v, int(bad.sum())


def reduce_pt(t):
    tr, a, b, _ = T.reduce(t, 0.0, 0.0, {"x": 0.0})
    return tr


def thread(w, per_unit=10):
    beta, betap, ell, g = T.geodesic(w)
    zt = lambda s: complex((beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1))
    nodes = max(32, int(per_unit * abs(ell))); s0 = -ell / 2
    pts = np.array([[r.real, r.imag] for r in (reduce_pt(zt(s0 + ell * j / nodes)) for j in range(nodes))])
    return pts, abs(ell)


def unflat(v):
    out, i = {}, 0
    for k, n in zip(KEYS, SHAPES):
        out[k] = v[i:i + n].tolist(); i += n
    return out


if __name__ == "__main__":
    import fiber_grid as FG
    rng = random.Random(1924)
    # (P1) interpolation accuracy at random points of the domain
    worst = {"const": 0.0, "canon": 0.0}
    for _ in range(8):
        x = rng.uniform(-0.5, 0.5); y = rng.uniform(math.sqrt(1 - x * x) + 0.01, 3.0)
        direct = FG.fbar(complex(x, y))
        for mode in worst:
            v, _ = fbar_interp(np.array([[x, y]]), mode)
            worst[mode] = max(worst[mode], float(np.max(np.abs(v[0] - flat(direct[mode])))))
    print("P1, interpolation against direct evaluation at 8 random points: largest difference const %.1e, canon %.1e" % (worst["const"], worst["canon"]), flush=True)
    # the ergodic integral: unconstrained random words of 40 letters, length-weighted thread averages
    words = []
    while len(words) < 3000:
        w = "".join(rng.choice("LR") for _ in range(40))
        if "L" in w and "R" in w:
            words.append(w)
    out = {"P1": worst}
    for mode in ("const", "canon"):
        A, wts, outside = [], [], 0
        for w in words:
            pts, ell = thread(w)
            v, nb = fbar_interp(pts, mode); outside += nb
            A.append(v.mean(0)); wts.append(ell)
        A = np.array(A); wts = np.array(wts)
        R = (wts[:, None] * A).sum(0) / wts.sum()
        # jackknife in 30 blocks of 100 words
        blocks = np.array_split(np.arange(len(words)), 30); jk = []
        for bl in blocks:
            m = np.ones(len(words), bool); m[bl] = False
            jk.append((wts[m][:, None] * A[m]).sum(0) / wts[m].sum())
        jk = np.array(jk); se = np.sqrt((len(jk) - 1) * np.mean((jk - R) ** 2, 0))
        out[mode] = {"R": unflat(R), "se": unflat(se), "nodes_outside_grid": outside}
        print("%s: the ergodic integral over 3000 unconstrained words of 40 letters; largest sampling error %.1e; nodes outside the grid %d" % (mode, float(se.max()), outside), flush=True)
    (HERE / ("fiber_ergodic_fine.json" if FINE else "fiber_ergodic.json")).write_text(json.dumps(out, indent=1))
    # (P2) against B1924's read-outs with the constant ends
    D = {}
    for f in ("whole_average_3.json", "whole_average_4.json"):
        D.update(json.loads((next((ROOT / "frontier").glob("B1924_*")) / "verification" / f).read_text()))
    Rb, sb = flat(out["const"]["R"]), flat(out["const"]["se"])
    for lab in ("22 mark", "22 twin", "22b mark", "22b twin", "28 mark", "28 twin"):
        z = np.abs(flat(D[lab]["R"]) - Rb) / np.sqrt(flat(D[lab]["se"]) ** 2 + sb ** 2)
        print("P2, the ergodic integral of F-bar against B1924's read-out at %s: median |z| %.2f, share above 2 %.0f%%, largest %.2f"
              % (lab, np.median(z), 100 * np.mean(z > 2), z.max()), flush=True)
    # (P3, added before the canonical-end run had finished, and before its values were read): the same with the canonical end,
    # against the constrained read-outs with the canonical end (audit/canonical_end/canon_readout.json)
    cj = next((ROOT / "frontier").glob("B1927_*")) / "verification" / "canon_readout.json"
    if cj.exists():
        Dc = json.loads(cj.read_text())
        Rc, sc = flat(out["canon"]["R"]), flat(out["canon"]["se"])
        for lab in ("16 mark", "16 twin", "22 mark", "22 twin"):
            if lab in Dc:
                z = np.abs(flat(Dc[lab]["R"]) - Rc) / np.sqrt(flat(Dc[lab]["se"]) ** 2 + sc ** 2)
                print("P3, the ergodic integral of F-bar (canonical end) against the read-out at %s: median |z| %.2f, share above 2 %.0f%%, largest %.2f"
                      % (lab, np.median(z), 100 * np.mean(z > 2), z.max()), flush=True)
