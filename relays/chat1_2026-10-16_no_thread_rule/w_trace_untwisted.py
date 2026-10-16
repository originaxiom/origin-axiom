"""W-trace, untwisted (chat1; the no-thread rule's own check; no data, no charge, no twist).

For every primitive thread of trace t = 3 .. TMAX, the untwisted thread frame's cycle integrals with the sealed
instrument (tlow2.py, unchanged): the norm cells K32, KM12, K72 and the Yukawa integrals Y1, Y2x, Y3x at zero twist
(v = R, W72's units and Higgs). The layer's cells are the sums over its threads, K_t = sum K_gamma and Y_t = sum Y_gamma
(each cycle integral is over one period in hyperbolic arc length, so it depends only on the closed geodesic). Read out,
per layer and cell:
  - the share of the layer's integrals carried by its deepest pair (L^(t-2)R and its mirror), as Frobenius-norm ratios;
  - the layer's singular values (untwisted: some cells are rank two by Jacobi, R.R = 0);
  - the deepest pair's own singular values, for comparison;
  - the integrals per unit length (K_t divided by the layer's total length), the quantity that would tend to the
    surface frame if the layers equidistributed without the cusp taking over.
Per thread as well, with its primitive discriminant, so the discriminant indexing can be formed from the same numbers.
Closure: tlow2's probe compares the Y integrand at the period's first point with the point one period on, relative to
its size there. On LRR's three rotations and LLR's rotation LRL that first point is an image of omega, where Y3x
vanishes, so the probe reads 0/0 (about 2). At a generic start every thread closes (closure_at_generic_start.py), so
every thread enters the layer sums; the probe's value is recorded as a diagnostic only.
No datum enters: no mass is compared with anything measured.

Usage: python3 -B w_trace_untwisted.py <forms.pkl> [TMAX] > w_trace_untwisted_run.txt  (writes w_trace_untwisted.json)
"""
import json, math, os, pickle, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
TU = os.path.normpath(os.path.join(HERE, "..", "chat1_2026-10-15_route", "twisted_units"))
sys.path.insert(0, TU)
import flint
import mpmath as mp
import tlow2 as T2

TMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 12
NPTS_PER_PERIOD, NPTS_CHECK = 30.0, 37.5           # points per unit of length, doubled until converged
ZERO = {"Q": 0, "u": 0, "d": 0, "L": 0, "e": 0, "H": 0}
DPS = 60


def lyndon(n, alphabet="LR"):
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == k - 1: w.pop()


def threads_by_trace(tmax):
    out = {}
    for w in lyndon(tmax - 1):
        if "L" in w and "R" in w:
            a, b, c, d = T2.matrix(w)
            if a + d <= tmax:
                out.setdefault(a + d, []).append(w)
    return out


def prim_disc(w):
    a, b, c, d = T2.matrix(w)
    f = math.gcd(math.gcd(c, d - a), b)
    return ((a + d) ** 2 - 4) // (f * f)


def to_mp(M):
    return mp.matrix([[mp.mpc(mp.mpf(x.real.mid().str(DPS + 10, radius=False)), mp.mpf(x.imag.mid().str(DPS + 10, radius=False)))
                       for x in row] for row in M])


def integrals(F_by_prec, P, word, npp):
    rot, M, rho, k, height = T2.thread_geometry(word)
    bits = T2.bits_for(height)
    flint.ctx.prec = 800
    F = T2.Forms(P).prepare()
    flint.ctx.prec = bits
    a, b, c, d = M
    Pl = 2 * math.acosh((a + d) / 2)
    conf = T2.configuration(F, word, (1, 0), 1, {"Z": ZERO}, int(round(Pl * npp)), readings=("minimal",))
    K = {key: to_mp(v) for key, v in conf["Kmn"].items()}
    Y = {key: to_mp(v) for key, v in conf["mn"][(0, 0)].items()}
    return {"K": K, "Y": Y, "length": Pl, "height": height, "bits": bits, "closure": max(conf["closure"].values()),
            "beta": F.beta}


def frob(M):
    return mp.sqrt(sum(abs(M[i, j]) ** 2 for i in range(M.rows) for j in range(M.cols)))


def cell_masses(K, Y, beta):
    mp.mp.dps = DPS
    res = T2.cells_for(K["K32"], K["K32"], K["KM12"], K["K72"], Y, beta, "minimal", mp)
    out = {}
    for cell, d in res.items():
        if d is None:
            out[cell] = None; continue
        s = [float(x) for x in d["s"]]
        out[cell] = {"s": s, "ln s1/s3": (math.log(s[0] / s[2]) if s[0] > 0 else None),
                     "ln s2/s3": math.log(s[1] / s[2]), "rank3": s[0] > 1e-30 * s[2]}
    return out


if __name__ == "__main__":
    t0 = time.time()
    mp.mp.dps = DPS
    P = pickle.load(open(sys.argv[1], "rb"))
    layers = threads_by_trace(TMAX)
    out = {"status": "W-trace, untwisted; no data", "TMAX": TMAX, "threads": {}, "layers": {}}
    per = {}
    for t in sorted(layers):
        for w in layers[t]:
            npp = NPTS_PER_PERIOD
            while True:                                  # deep threads need more points: double until converged
                r1 = integrals(None, P, w, npp)
                r2 = integrals(None, P, w, npp * NPTS_CHECK / NPTS_PER_PERIOD)
                mp.mp.dps = DPS
                conv = max(float(frob(r1[s][k_] - r2[s][k_]) / frob(r1[s][k_])) for s in ("K", "Y") for k_ in r1[s])
                if conv < 1e-20 or npp >= 16 * NPTS_PER_PERIOD:
                    break
                npp *= 2
            per[w] = r1
            m = cell_masses(r1["K"], r1["Y"], r1["beta"])
            cl = r1["closure"]
            out["threads"][w] = {"trace": t, "primitive discriminant": prim_disc(w), "Psi": w.count("R") - w.count("L"),
                                 "closure probe at the period's first point (diagnostic)": cl,
                                 "points per unit length": npp,
                                 "height": r1["height"], "length": r1["length"], "bits": r1["bits"],
                                 "closure": r1["closure"], "convergence (rel. Frobenius, 30 vs 37.5 per period)": conv,
                                 "trace of K32, KM12, K72": [float(mp.re(sum(r1["K"][k_][i, i] for i in range(r1["K"][k_].rows))))
                                                             for k_ in ("K32", "KM12", "K72")],
                                 "masses": m}
            print(f"t={t:2d} {w:14s} Psi={w.count('R') - w.count('L'):3d} D'={prim_disc(w):4d} h={r1['height']:.3f} bits {r1['bits']} npp {npp:.0f} "
                  f"closure probe {r1['closure']:.1e} conv {conv:.1e} "
                  f"{time.time() - t0:.0f} s", flush=True)
    for t in sorted(layers):
        allw = layers[t]
        ws = list(allw)
        out["layers"][str(t)] = {"threads": allw}
        mp.mp.dps = DPS
        deep = {"L" * (t - 2) + "R", "L" + "R" * (t - 2)} & set(ws)
        if not deep:
            deep = {max(ws, key=lambda w: per[w]["height"])}
        K = {k_: sum((per[w]["K"][k_] for w in ws[1:]), per[ws[0]]["K"][k_]) for k_ in per[ws[0]]["K"]}
        Y = {k_: sum((per[w]["Y"][k_] for w in ws[1:]), per[ws[0]]["Y"][k_]) for k_ in per[ws[0]]["Y"]}
        dl = sorted(deep)
        Kd = {k_: sum((per[w]["K"][k_] for w in dl[1:]), per[dl[0]]["K"][k_]) for k_ in K}
        Yd = {k_: sum((per[w]["Y"][k_] for w in dl[1:]), per[dl[0]]["Y"][k_]) for k_ in Y}
        Ltot = sum(per[w]["length"] for w in ws)
        share = {k_: float(frob(Kd[k_]) / frob(K[k_])) for k_ in K}
        share.update({k_: float(frob(Yd[k_]) / frob(Y[k_])) for k_ in Y})
        rest = [w for w in ws if w not in deep]
        out["layers"][str(t)].update({
            "deepest pair": dl, "total length": Ltot,
            "deepest pair's share (Frobenius)": share,
            "per unit length: trace of K32, KM12, K72": [float(mp.re(sum(K[k_][i, i] for i in range(K[k_].rows)))) / Ltot
                                                         for k_ in ("K32", "KM12", "K72")],
            "layer masses": cell_masses(K, Y, per[ws[0]]["beta"]),
            "deepest pair's masses": cell_masses(Kd, Yd, per[ws[0]]["beta"]),
            "the rest's masses (layer without its deepest pair)": (cell_masses(
                {k_: sum((per[w]["K"][k_] for w in rest[1:]), per[rest[0]]["K"][k_]) for k_ in K},
                {k_: sum((per[w]["Y"][k_] for w in rest[1:]), per[rest[0]]["Y"][k_]) for k_ in Y},
                per[ws[0]]["beta"]) if rest else None)})
        lm = out["layers"][str(t)]["layer masses"]
        print(f"layer t={t:2d}: {len(ws)} threads; deepest pair {dl}; share K32 {share['K32']:.6f} KM12 {share['KM12']:.6f} "
              f"K72 {share['K72']:.6f} Y1 {share['Y1']:.6f}; ln s2/s3 C1 "
              f"{(lm['C1'] or {}).get('ln s2/s3')}", flush=True)
    json.dump(out, open(os.path.join(HERE, "w_trace_untwisted.json"), "w"), indent=1, default=str)
    print(f"written w_trace_untwisted.json; {time.time() - t0:.0f} s")
