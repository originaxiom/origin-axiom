#!/usr/bin/env python3
"""A control on the agy lane's B1881, cell H4 (branch agy/stage4-sync-2026-11-11, read at b4ddb600b).

H4 fed the lane's read-out point into the frame and asked whether AT LEAST ONE of 96 configurations clears two bands
(the hierarchy between 2.5 and 7.5 decades, and between 1.0 and 4.5 decades, in all three sectors; and |J| above 1e-8).
It found 2 of 96, and the arc's verdict is PROVED.  The card does not say how often a point that no rule selected clears
the same bar.  This script measures that, with the lane's own function, unchanged, loaded from a checkout of its branch.
No measured value is read: the lane's gate is a pair of fixed bands.

    python3 -B h4_baseline.py CLONE_AT_THE_LANES_TIP

THE SEAT'S EXPECTATIONS, written before the run and committed before it:
  X0  the lane's own point reproduces: 2 of 96 clear the bar                                                   95%
  X1  of 120 points spread evenly in angle on the circle |z|^2 = 1/5 between its two forced zeros, at least
      a quarter clear the bar (one configuration or more of the 96)                                            65%
  X2  of 200 points spread evenly in hyperbolic area over the lane's domain, cut at height 3, at least a
      quarter clear the bar                                                                                    60%
  X3  on the circle, the share that clears the bar is greater in the upper half (by the height of the
      reduced point) than in the lower                                                                         75%
HOW IT WILL BE READ.  If a quarter or more of unselected points clear the bar, clearing it says little about the point.
If under 5% do, the lane's point is unusual, and this control says so.  Between the two, it says what was measured.
"""
import sys, json, math, time, pathlib, importlib.util
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ARC = "frontier/B1881_p776_twin_odd_operator_and_whole_subweave_readout/verification/subweave_p776_and_hierarchy.py"
SCRIPT_SHA = "abcb2fb3721580a5de859b9815e776edbabab3598e40cbe892506a1454dec6ad"        # the lane's sealed hash of its script
PEAK = complex(0.251539778829130, 0.369767144294671)                                   # the lane's read-out point, from its findings
N_CIRCLE, N_AREA, Y_CUT, SEED = 120, 200, 3.0, 20261111


def main():
    import hashlib
    clone = pathlib.Path(sys.argv[1]).resolve(); path = clone / ARC
    assert hashlib.sha256(path.read_bytes()).hexdigest() == SCRIPT_SHA, "not the lane's sealed script"
    sp = importlib.util.spec_from_file_location("lane_b1881", path); M = importlib.util.module_from_spec(sp)
    sys.modules["lane_b1881"] = M; sp.loader.exec_module(M)
    lines = []

    def log(x):
        print(x, flush=True); lines.append(x)

    def bar(tau):
        """(how many of the 96 clear both bands, how many clear the lower floor alone, the height of the reduced point)"""
        try:
            r = M.evaluate_fr_fib_structural_census_at_tau("control", complex(tau), [1, 2])
            return int(r["passing_H4_joint_count"]), int(r["passing_S_DECADE_count"]), float(r["tau_sl2z_reduced"][1])
        except Exception as exc:
            return None, None, repr(exc)[:80]

    log("a control on the lane's H4: how often does an unselected point clear the same bar? (the lane's function, unchanged)")
    t0 = time.time(); j, s, h = bar(PEAK)
    log("X0  the lane's point %.9f + %.9fi: %s of 96 clear both bands (the lane reports 2); reduced height %s; %.1f s a point" % (PEAK.real, PEAK.imag, j, h, time.time() - t0))

    # the circle |z|^2 = 1/5 between the forced zeros at angle arctan(1/2) (an elliptic point) and at a right angle (i / sqrt 5)
    lo, hi = math.atan(0.5), math.pi / 2; circ = []
    for k in range(N_CIRCLE):
        th = lo + (k + 0.5) / N_CIRCLE * (hi - lo); tau = complex(math.cos(th), math.sin(th)) / math.sqrt(5)
        circ.append((th, tau) + bar(tau))
    okc = [c for c in circ if c[2] is not None]
    pc = sum(c[2] >= 1 for c in okc)
    log("X1  the circle: %d points evenly in angle, %d evaluated; %d clear the bar (%.1f%%); mean number of the 96 that clear it %.2f" % (
        N_CIRCLE, len(okc), pc, 100.0 * pc / max(len(okc), 1), float(np.mean([c[2] for c in okc])) if okc else float("nan")))
    for a in range(0, N_CIRCLE, 12):
        seg = [c for c in circ[a:a + 12] if c[2] is not None]
        if seg:
            log("       angle %5.1f to %5.1f degrees, reduced height %.3f to %.3f: %2d of %2d clear the bar" % (
                math.degrees(circ[a][0]), math.degrees(circ[min(a + 11, N_CIRCLE - 1)][0]), min(c[4] for c in seg), max(c[4] for c in seg),
                sum(c[2] >= 1 for c in seg), len(seg)))
    med = float(np.median([c[4] for c in okc])) if okc else float("nan")
    up = [c for c in okc if c[4] > med]; dn = [c for c in okc if c[4] <= med]
    log("X3  the circle by the height of the reduced point: upper half %d of %d clear the bar, lower half %d of %d" % (
        sum(c[2] >= 1 for c in up), len(up), sum(c[2] >= 1 for c in dn), len(dn)))

    # evenly in hyperbolic area over the lane's domain (x in [0, 1/2] by its mirror symmetry), below the cut
    rng = np.random.default_rng(SEED); area = []
    while len(area) < N_AREA:
        x = rng.uniform(0.0, 0.5); yb = float(M.fplus5_y_bottom(np.array([x]))[0]); w = 1.0 / yb - 1.0 / Y_CUT
        if rng.uniform(0.0, 5.0 - 1.0 / Y_CUT) > w: continue
        y = 1.0 / rng.uniform(1.0 / Y_CUT, 1.0 / yb); tau = complex(x, y)
        area.append((tau,) + bar(tau))
    oka = [c for c in area if c[1] is not None]
    pa = sum(c[1] >= 1 for c in oka)
    log("X2  the domain: %d points evenly in hyperbolic area below height %.0f (seed %d), %d evaluated; %d clear the bar (%.1f%%); mean number of the 96 that clear it %.2f" % (
        N_AREA, Y_CUT, SEED, len(oka), pa, 100.0 * pa / max(len(oka), 1), float(np.mean([c[1] for c in oka])) if oka else float("nan")))
    for a, b in ((1.0, 1.5), (1.5, 2.0), (2.0, 2.5), (2.5, 3.5), (3.5, 99.0)):
        seg = [c for c in oka if a <= c[3] < b]
        if seg: log("       reduced height %.1f to %s: %3d of %3d clear the bar" % (a, ("%.1f" % b) if b < 99 else "above", sum(c[1] >= 1 for c in seg), len(seg)))
    bad = [c for c in circ if c[2] is None] + [c for c in area if c[1] is None]
    log("points the lane's function could not evaluate: %d" % len(bad))
    json.dump({"peak": [j, s, h], "circle": [[c[0], c[1].real, c[1].imag, c[2], c[3], c[4]] for c in circ],
               "area": [[c[0].real, c[0].imag, c[1], c[2], c[3]] for c in area]}, open(HERE / "h4_baseline.json", "w"), indent=0)
    log("total %.0f s" % (time.time() - t0)); log("control exit 0")
    (HERE / "h4_baseline_out.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
