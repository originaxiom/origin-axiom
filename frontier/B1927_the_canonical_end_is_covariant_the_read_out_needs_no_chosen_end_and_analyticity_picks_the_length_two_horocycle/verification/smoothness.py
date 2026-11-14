"""Which end convention? The candidate criterion the mathematics can decide (written before the run; the author's
reminder of 2026-11-14).

The maximal-horoball end L_max = (2 pi/lam)(1/min|c_gamma| - Im B) is a MINIMUM over group elements: where the
minimising element changes, L_max has a corner (a jump in its derivative), so it is not real-analytic in tau. The
length-2 end L_2 = pi - (2 pi/lam) Im B involves no minimum and should be real-analytic, like the rest of the frame
(the theta functions, the channel norm's Kronecker limit). EXPECTATION: along paths in the fundamental domain, the two
smallest values of |c_gamma| cross somewhere (their gap touches zero), and at those points L_max's second difference
spikes while L_2's stays smooth. If no crossing occurs on the paths, the criterion does not decide on them. If L_2 also
shows a spike, the criterion fails as stated.
Uses B1667's sealed instrument's functions unchanged. Printed: structure only (crossings, ratios of second differences)."""
import json, math, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification"))
import the_canonical_cusp as CC


def two_smallest(Ra, Rb, maxlen=8):
    gens = [Ra, Rb, np.linalg.inv(Ra), np.linalg.inv(Rb)]; inv = {0: 2, 1: 3, 2: 0, 3: 1}
    vals = []
    frontier = [(np.eye(2, dtype=complex), -1)]
    for _ in range(maxlen):
        nxt = []
        for M, last in frontier:
            for k in range(4):
                if last >= 0 and inv[k] == last:
                    continue
                N = M @ gens[k]
                if abs(N[1, 0]) > 1e-9 * max(1.0, abs(N[0, 0])):
                    vals.append(abs(N[1, 0]))
                nxt.append((N, k))
        frontier = nxt
    vals = np.sort(np.array(vals))
    first = vals[0]
    second = next((v for v in vals if v > first * (1 + 1e-7)), np.inf)
    return first, second


def ends_and_gap(tau, c):
    lat, z0, Aa, Ab = CC.monodromy(tau, c)
    P0 = CC.mobius_of(CC.puncture_loop(lat, c, z0, 0.05))
    g, Ra, Rb, RP, lam = CC.normalise(Aa, Ab, P0)
    lam = abs(lam.real)
    c1, c2 = two_smallest(Ra, Rb, 8)
    al, be = CC.frobenius(lat, c)
    ib = float(CC.local_B(lat, c, z0, g, lam, al, be, 0.05))
    return (2 * np.pi / lam) * (1.0 / c1 - ib), np.pi - (2 * np.pi / lam) * ib, (c2 - c1) / c1


def path(points, c_seed, tau_seed):
    tau, c = complex(tau_seed), complex(c_seed); out = []
    for tgt in points:
        c, res = CC.newton_walk(tau, c, tgt); tau = tgt
        lm, l2, gap = ends_and_gap(tau, c)
        out.append({"tau": [tau.real, tau.imag], "L_max": float(lm), "L_2": float(l2), "gap": float(gap)})
    return out


def second_diff(v):
    v = np.array(v); return np.abs(v[2:] - 2 * v[1:-1] + v[:-2])


if __name__ == "__main__":
    G = json.loads((HERE / "grid.json").read_text())["grid"]
    seed = next(p for p in G if abs(p["tau"][0] - 0.25) < 1e-9 and abs(p["tau"][1] - 1.0) < 1e-6) if any(abs(p["tau"][0] - 0.25) < 1e-9 and abs(p["tau"][1] - 1.0) < 1e-6 for p in G) else min((p for p in G if abs(p["tau"][0] - 0.25) < 1e-9), key=lambda p: p["tau"][1])
    t0, c0 = complex(*seed["tau"]), complex(*seed["c"])
    out = {}
    paths = {"vertical Re 0.25": [complex(0.25, y) for y in np.arange(t0.imag, 3.0001, 0.04)],
             "horizontal Im 1.3": [complex(x, 1.3) for x in np.arange(0.25, -0.0001, -0.02)] + [complex(x, 1.3) for x in np.arange(0.27, 0.5001, 0.02)]}
    for name, pts in paths.items():
        if name.startswith("horizontal"):
            seg1 = path(pts[:13], c0, t0)
            seg2 = path(pts[13:], c0, t0)
            rows = list(reversed(seg1)) + seg2
        else:
            rows = path(pts, c0, t0)
        out[name] = rows
        gaps = np.array([r["gap"] for r in rows])
        d2m, d22 = second_diff([r["L_max"] for r in rows]), second_diff([r["L_2"] for r in rows])
        cross = [i for i in range(1, len(gaps) - 1) if gaps[i] < gaps[i - 1] and gaps[i] < gaps[i + 1] and gaps[i] < 0.02]
        print("%s: %d points; near-crossings of the two smallest |c| (gap below 2%%, local minimum): %d; "
              "second differences: L_max largest/median %.1f, L_2 largest/median %.1f" %
              (name, len(rows), len(cross), d2m.max() / max(np.median(d2m), 1e-300), d22.max() / max(np.median(d22), 1e-300)), flush=True)
        (HERE / "smoothness.json").write_text(json.dumps(out, indent=1))
