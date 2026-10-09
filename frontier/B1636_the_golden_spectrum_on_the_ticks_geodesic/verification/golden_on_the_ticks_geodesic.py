#!/usr/bin/env python3
"""B1636 -- THE GOLDEN SPECTRUM ON THE TICK'S GEODESIC.  B1635's post-seal read-out (unpredicted): on the tick's closed
geodesic (the axis of LR, |tau - 1/2| = sqrt5/2, through i) the weave's lowest symmetric coupling (O+ at k = 1, one-
dimensional) had normalized masses (1, 0.618033989, 0.381966011) at 13 of 13 points; at i, (1, 1/phi, 1/phi^2) to 1e-16.
Is it exact along the whole geodesic, is it special to the tick, and why?  Uses B1635's sealed instrument's functions.
 G1  O+ k = 1 at 60 points of the tick's geodesic (t in [0.25, pi - 0.25]; Im tau >= 0.27, where the theta series and the
     division by eta^18 keep full precision) and at LR-images of three of them: the largest
     deviation of the normalized masses from (1, 1/phi, 1/phi^2).
 G2  the zero-diagonal sum rule m1 = m2 + m3 for every O+ coupling (k = 1, 3, 5, 7; generic members) at 12 random tau:
     the largest |m1 - m2 - m3| / m1.
 G3  the mechanism read-out: along the tick's geodesic, the moduli of O+ k = 1's three entries (normalized by the
     largest) and the theta ratios |u2/u4|, |u3/u2|.
 G4  the controls: the spread (max - min of the normalized middle mass) of O+ k = 1 along the axes of L^2 R, L R^2,
     L^2 R^2, L^3 R, L R L R^2 (closed geodesics of the weave), and along the reflection lines Re tau = 0, |tau| = 1,
     Re tau = 1/2.
 G5  the spread along the tick's geodesic of O+ k = 3, D k = 5, D k = 7, and generic members of O+ k = 5, of D (+) O+ at
     k = 5 and of O+ k = 9.
Writes golden_on_the_ticks_geodesic.json."""
import json, pathlib, os, importlib.util, math
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("c", FRONTIER / "B1635_couplings_on_the_ruled_branch" / "verification" / "couplings_on_the_ruled_branch.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
inv = np.linalg.inv
PHI = (1 + 5 ** 0.5) / 2
GOLD = np.array([1.0, 1 / PHI, 1 / PHI ** 2])
Lm = np.array([[1, 1], [0, 1]]); Rm = np.array([[1, 0], [1, 1]])


def mob(M, t):
    return (M[0, 0] * t + M[0, 1]) / (M[1, 0] * t + M[1, 1])


def axis(M, ts):
    a, b, cc, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    cen = (a - d) / (2 * cc); rad = math.sqrt((a + d) ** 2 - 4) / (2 * abs(cc))
    return [complex(cen + rad * math.cos(t), rad * math.sin(t)) for t in ts]


def piece(k, name):
    full, mons, _ = c.equivariant_space(k + 9, lambda A: inv(A).T, lambda A: inv(A))
    hol = c.cusp_condition(full, mons, 6)
    if name == "sym": return np.concatenate([c.restrict_piece(hol, "D"), c.restrict_piece(hol, "O+")]), mons
    return c.restrict_piece(hol, name), mons


def masses(b, mons, t):
    return np.linalg.svd(c.evaluate(b, mons, t, 18), compute_uv=False)


def norm_masses(b, mons, t):
    s = masses(b, mons, t); return s / s[0]


def generic(pb, seed):
    rng = np.random.default_rng(seed); z = rng.normal(size=pb.shape[0]) + 1j * rng.normal(size=pb.shape[0])
    return np.einsum("n,nrcm->rcm", z / np.linalg.norm(z), pb)


def spread(b, mons, pts):
    mids = [float(norm_masses(b, mons, t)[1]) for t in pts]
    return {"min_middle": round(min(mids), 12), "max_middle": round(max(mids), 12), "spread": float(max(mids) - min(mids))}


def main():
    out = {}
    O1, mons1 = piece(1, "O+"); b1 = O1[0]
    LR = Lm @ Rm
    ts = np.linspace(0.25, math.pi - 0.25, 60)
    tick = axis(LR, ts)
    imgs = [mob(LR, t) for t in tick[10:13]] + [mob(inv(LR).round().astype(int), t) for t in tick[40:43]]
    dev = [float(np.max(np.abs(norm_masses(b1, mons1, t) - GOLD))) for t in tick + imgs]
    out["G1"] = {"points": len(tick) + len(imgs), "max_deviation_from_golden": max(dev),
                 "images_on_the_axis": [round(abs(t - 0.5) - 5 ** 0.5 / 2, 12) for t in imgs]}
    rng = np.random.default_rng(1636)
    taus = [complex(rng.uniform(-0.5, 0.5), rng.uniform(0.6, 2.0)) for _ in range(12)]
    worst = 0.0
    for k in (1, 3, 5, 7):
        pb, mons = piece(k, "O+")
        for sd in range(3):
            b = generic(pb, sd)
            for t in taus:
                s = masses(b, mons, t); worst = max(worst, abs(s[0] - s[1] - s[2]) / s[0])
    out["G2_sum_rule_worst_relative"] = worst
    g3 = []
    for t in tick[::6]:
        Y = c.evaluate(b1, mons1, t, 18); A = np.abs(Y) / np.abs(Y).max()
        u, _ = c.u_eta(t)
        g3.append({"tau": [round(t.real, 6), round(t.imag, 6)], "abs_entries_12_13_23": [round(float(A[0, 1]), 9), round(float(A[0, 2]), 9), round(float(A[1, 2]), 9)],
                   "abs_u2_over_u4": round(abs(u[0] / u[2]), 9), "abs_u3_over_u2": round(abs(u[1] / u[0]), 9)})
    out["G3_mechanism_readout"] = g3
    geos = {"L^2 R": Lm @ Lm @ Rm, "L R^2": Lm @ Rm @ Rm, "L^2 R^2": Lm @ Lm @ Rm @ Rm, "L^3 R": Lm @ Lm @ Lm @ Rm, "L R L R^2": Lm @ Rm @ Lm @ Rm @ Rm}
    g4 = {name: spread(b1, mons1, axis(M, ts[::3])) for name, M in geos.items()}
    g4["tick LR (reference)"] = spread(b1, mons1, axis(LR, ts[::3]))
    ys = np.linspace(0.6, 3.0, 20)
    g4["Re tau = 0"] = spread(b1, mons1, [complex(0, y) for y in ys])
    g4["|tau| = 1"] = spread(b1, mons1, [complex(math.cos(a), math.sin(a)) for a in np.linspace(math.pi / 3, 2 * math.pi / 3, 20)])
    g4["Re tau = 1/2"] = spread(b1, mons1, [complex(0.5, y) for y in ys])
    out["G4_controls_spread_of_O+k1"] = g4
    g5 = {}
    for label, (k, name, seed) in {"O+ k=3": (3, "O+", None), "D k=5": (5, "D", None), "D k=7": (7, "D", None),
                                   "O+ k=5 generic": (5, "O+", 0), "sym k=5 generic": (5, "sym", 0), "O+ k=9 generic": (9, "O+", 0)}.items():
        pb, mons = piece(k, name)
        b = pb[0] if seed is None else generic(pb, seed)
        g5[label] = spread(b, mons, axis(LR, ts[::3]))
    out["G5_other_couplings_on_the_tick"] = g5
    json.dump(out, open(HERE / "golden_on_the_ticks_geodesic.json", "w"), indent=1, default=str)
    print(json.dumps(out, indent=1, default=str)[:6000])


if __name__ == "__main__":
    main()
