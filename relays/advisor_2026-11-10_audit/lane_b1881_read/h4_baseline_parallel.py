#!/usr/bin/env python3
"""The control of h4_baseline.py, run in several processes.  Written AFTER that script was committed and started.

Why: in one process the lane's function takes 36 seconds a point (its solver for the cusp radii takes 15 of them), so
the committed loop over 320 points would have run for three hours.  It was stopped after its first point, which
reproduced the lane's 2 of 96.  This driver changes nothing that is measured: the points, the function, the bar, the
seed and the expectations are those of h4_baseline.py, which it imports; only the loop is replaced by a pool.

    python3 -B h4_baseline_parallel.py CLONE_AT_THE_LANES_TIP [workers]"""
import sys, json, math, time, hashlib, pathlib, importlib.util
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location("h4_baseline", HERE / "h4_baseline.py"); B = importlib.util.module_from_spec(sp); sp.loader.exec_module(B)
M = None


def bar(tau):
    """as in h4_baseline.py: (how many of the 96 clear both bands, how many clear the lower floor alone, the reduced height)"""
    try:
        r = M.evaluate_fr_fib_structural_census_at_tau("control", complex(tau), [1, 2])
        return int(r["passing_H4_joint_count"]), int(r["passing_S_DECADE_count"]), float(r["tau_sl2z_reduced"][1])
    except Exception as exc:
        return None, None, repr(exc)[:80]


def main():
    global M
    from multiprocessing import get_context
    clone = pathlib.Path(sys.argv[1]).resolve(); path = clone / B.ARC; workers = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    assert hashlib.sha256(path.read_bytes()).hexdigest() == B.SCRIPT_SHA, "not the lane's sealed script"
    spm = importlib.util.spec_from_file_location("lane_b1881", path); M = importlib.util.module_from_spec(spm)
    sys.modules["lane_b1881"] = M; spm.loader.exec_module(M); M.load_main_instruments()
    lines = []

    def log(x):
        print(x, flush=True); lines.append(x)
    # the points, exactly as h4_baseline.py makes them
    lo, hi = math.atan(0.5), math.pi / 2
    thetas = [lo + (k + 0.5) / B.N_CIRCLE * (hi - lo) for k in range(B.N_CIRCLE)]
    circ_tau = [complex(math.cos(th), math.sin(th)) / math.sqrt(5) for th in thetas]
    rng = np.random.default_rng(B.SEED); area_tau = []
    while len(area_tau) < B.N_AREA:
        x = rng.uniform(0.0, 0.5); yb = float(M.fplus5_y_bottom(np.array([x]))[0]); w = 1.0 / yb - 1.0 / B.Y_CUT
        if rng.uniform(0.0, 5.0 - 1.0 / B.Y_CUT) > w: continue
        y = 1.0 / rng.uniform(1.0 / B.Y_CUT, 1.0 / yb); area_tau.append(complex(x, y))
    log("a control on the lane's H4: how often does an unselected point clear the same bar? (the lane's function, unchanged; %d processes)" % workers)
    t0 = time.time()
    with get_context("fork").Pool(workers) as P:
        res = P.map(bar, [B.PEAK] + circ_tau + area_tau, chunksize=1)
    j, s, h = res[0]; circ = [(th, tau) + r for th, tau, r in zip(thetas, circ_tau, res[1:1 + B.N_CIRCLE])]
    area = [(tau,) + r for tau, r in zip(area_tau, res[1 + B.N_CIRCLE:])]
    log("X0  the lane's point %.9f + %.9fi: %s of 96 clear both bands (the lane reports 2); reduced height %s" % (B.PEAK.real, B.PEAK.imag, j, h))
    okc = [c for c in circ if c[2] is not None]; pc = sum(c[2] >= 1 for c in okc)
    log("X1  the circle: %d points evenly in angle, %d evaluated; %d clear the bar (%.1f%%); mean number of the 96 that clear it %.2f" % (
        B.N_CIRCLE, len(okc), pc, 100.0 * pc / max(len(okc), 1), float(np.mean([c[2] for c in okc])) if okc else float("nan")))
    for a in range(0, B.N_CIRCLE, 12):
        seg = [c for c in circ[a:a + 12] if c[2] is not None]
        if seg:
            log("       angle %5.1f to %5.1f degrees, reduced height %.3f to %.3f: %2d of %2d clear the bar" % (
                math.degrees(circ[a][0]), math.degrees(circ[min(a + 11, B.N_CIRCLE - 1)][0]), min(c[4] for c in seg), max(c[4] for c in seg),
                sum(c[2] >= 1 for c in seg), len(seg)))
    med = float(np.median([c[4] for c in okc])) if okc else float("nan")
    up = [c for c in okc if c[4] > med]; dn = [c for c in okc if c[4] <= med]
    log("X3  the circle by the height of the reduced point: upper half %d of %d clear the bar, lower half %d of %d" % (
        sum(c[2] >= 1 for c in up), len(up), sum(c[2] >= 1 for c in dn), len(dn)))
    oka = [c for c in area if c[1] is not None]; pa = sum(c[1] >= 1 for c in oka)
    log("X2  the domain: %d points evenly in hyperbolic area below height %.0f (seed %d), %d evaluated; %d clear the bar (%.1f%%); mean number of the 96 that clear it %.2f" % (
        B.N_AREA, B.Y_CUT, B.SEED, len(oka), pa, 100.0 * pa / max(len(oka), 1), float(np.mean([c[1] for c in oka])) if oka else float("nan")))
    for a, b in ((1.0, 1.5), (1.5, 2.0), (2.0, 2.5), (2.5, 3.5), (3.5, 99.0)):
        seg = [c for c in oka if a <= c[3] < b]
        if seg: log("       reduced height %.1f to %s: %3d of %3d clear the bar" % (a, ("%.1f" % b) if b < 99 else "above", sum(c[1] >= 1 for c in seg), len(seg)))
    bad = [c for c in circ if c[2] is None] + [c for c in area if c[1] is None]
    log("points the lane's function could not evaluate: %d%s" % (len(bad), "".join("\n       %s" % (c[-1],) for c in bad[:5])))
    json.dump({"peak": [j, s, h], "circle": [[c[0], c[1].real, c[1].imag, c[2], c[3], c[4]] for c in circ],
               "area": [[c[0].real, c[0].imag, c[1], c[2], c[3]] for c in area]}, open(HERE / "h4_baseline.json", "w"), indent=0)
    log("total %.0f s in %d processes" % (time.time() - t0, workers)); log("control exit 0")
    (HERE / "h4_baseline_out.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
