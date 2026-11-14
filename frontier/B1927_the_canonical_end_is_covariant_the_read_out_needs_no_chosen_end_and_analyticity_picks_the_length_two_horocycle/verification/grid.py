"""The canonical end (B1667's L_max and L_2) on a grid of the fundamental domain, to read the frame with the end fixed by
the fibre's own geometry instead of a chosen constant (B1924's correction; P-845).

Written before the run. B1667's end is L = log(1/eps), with eps a radius in the flat coordinate z of C/(Z + tau Z), set by
an intrinsic horocycle (the maximal embedded one; or the one of length 2). Under tau -> -1/tau the coordinate scales by
1/|tau|, so L(-1/tau) = L(tau) + log|tau|, the frame's own covariance (B1724, B1921). So L~(tau) = L(tau) + 1/2 log Im tau
- (gamma + log pi) is SL(2,Z)-invariant, though not constant, and the frame read with this end is periodic along every
thread at the thread's own line (B1922's mechanism) with no free continuous end: only the convention (maximal, length 2).
Checks built in: (1) the grid reproduces B1667's sealed values at its own points (to 1e-8); (2) mirror symmetry
L(-conj tau) = L(tau) at two points; (3) the S-covariance L(-1/tau) = L(tau) + log|tau| at one point inside the
instrument's reach. Uses B1667's sealed instrument's functions unchanged; computes only the two ends."""
import json, math, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification"))
import the_canonical_cusp as CC


def ends(tau, c):
    tau = complex(tau); c = complex(c)
    lat, z0, Aa, Ab = CC.monodromy(tau, c)
    P0 = CC.mobius_of(CC.puncture_loop(lat, c, z0, 0.05))
    g, Ra, Rb, RP, lam = CC.normalise(Aa, Ab, P0)
    lam = abs(lam.real)
    mc8 = CC.min_c(Ra, Rb, 8)
    al, be = CC.frobenius(lat, c)
    ib = float(CC.local_B(lat, c, z0, g, lam, al, be, 0.05))
    return (2 * np.pi / lam) * (1.0 / mc8 - ib), np.pi - (2 * np.pi / lam) * ib


def column(x, ys, c_start, tau_start):
    out = []; tau, c = complex(tau_start), complex(c_start)
    for y in ys:
        tgt = complex(x, y)
        c, res = CC.newton_walk(tau, c, tgt); tau = tgt
        if float(np.max(np.abs(res))) > 1e-9:
            out.append({"tau": [x, y], "failed": float(np.max(np.abs(res)))}); break
        lm, l2 = ends(tau, c)
        out.append({"tau": [x, y], "c": [c.real, c.imag], "L_max": float(lm), "L_2": float(l2)})
        print("tau = %.3f + %.3fi: done" % (x, y), flush=True)
    return out


if __name__ == "__main__":
    B = json.loads((ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json").read_text())["points"]
    # (1) reproduce two sealed points
    chk = []
    for p in B[:60]:
        if p.get("where") == "grid" and abs(p["tau"][0] - 0.25) < 1e-9 and p["tau"][1] in (1.5, 3.0):
            lm, l2 = ends(complex(*p["tau"]), complex(*p["c"]))
            chk.append(max(abs(lm - p["L_max"]), abs(l2 - p["L_2"])))
    print("check (1), the sealed values reproduced: largest difference %.1e over %d points" % (max(chk), len(chk)), flush=True)
    seeds = {}
    for p in B:
        if p.get("where") == "grid":
            x = round(p["tau"][0], 3)
            if x not in seeds or p["tau"][1] < seeds[x][0].imag:
                seeds[x] = (complex(*p["tau"]), complex(*p["c"]))
    grid = []
    # capped at 6: the reduced nodes of the read-out's threads reach Im tau 4.5 at n = 16 and 5.6 at n = 22 (measured
    # before this run); the first version went to 10 and stalled at 8, where the instrument is slow
    YS = [1.0, 1.1, 1.25, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0]
    for x in (0.05, 0.15, 0.25, 0.35, 0.45):
        t0, c0 = seeds[x]
        lo = math.sqrt(max(0.0, 1 - x * x)) + 0.02
        ys = sorted(set([round(lo, 3)] + [y for y in YS if y > lo]))
        grid += column(x, ys, c0, t0)
        (HERE / "grid.json").write_text(json.dumps({"grid": grid, "check1": chk}, indent=1))
    # (2) mirror and (3) S-covariance at tau = 0.25 + 1.5i (its image -1/tau = -0.105 + 0.632i, walked from the seed)
    t = complex(0.25, 1.5); p = next(q for q in grid if abs(q["tau"][0] - 0.25) < 1e-9 and abs(q["tau"][1] - 1.5) < 1e-9)
    c = complex(*p["c"])
    cm, _ = CC.newton_walk(t, c, complex(-0.25, 1.5))
    lm_m, l2_m = ends(complex(-0.25, 1.5), cm)
    mirror = max(abs(lm_m - p["L_max"]), abs(l2_m - p["L_2"]))
    ts = -1 / t
    try:
        cs, res = CC.newton_walk(t, c, ts, step=0.02)
        lm_s, l2_s = ends(ts, cs)
        cov = max(abs(lm_s - (p["L_max"] + math.log(abs(t)))), abs(l2_s - (p["L_2"] + math.log(abs(t)))))
    except Exception as e:
        cov = None; print("check (3) could not walk to -1/tau:", type(e).__name__, flush=True)
    print("check (2), mirror: difference %.1e; check (3), S-covariance at 0.25 + 1.5i: %s" % (mirror, "-" if cov is None else "%.1e" % cov), flush=True)
    (HERE / "grid.json").write_text(json.dumps({"grid": grid, "check1": chk, "mirror": mirror, "covariance": cov}, indent=1))
