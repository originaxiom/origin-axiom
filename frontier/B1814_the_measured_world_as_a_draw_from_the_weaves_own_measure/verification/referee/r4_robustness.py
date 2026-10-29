"""Referee R4: how robust are the decisive outcomes to the census's finite sample and to the unforced mixture's
configuration seed?  Uses R3's independent implementation (r3_independent.py).  (a) 100 random half-splits of each arm's
4 000 draws; (b) 200 subsamples of 3 000 of the 4 000 without replacement; (c) 100 other seeds for the unforced mixture's
per-draw configuration (the sealed seed is 18142).  For each: p_nn(A1 unforced) [D1], p_nn(A1 by hand) [D1h], p_F(A1
unforced) and p_F(A0 unforced) [D2], p_nn(A0 unforced) [D2's read-out].  Also: the horocycle-by-hand read-out's random-
hierarchy shares (L_max vs L_2), D2 by p_nn's r, and D1 at floor 1e-8 with r on 4 seeds."""
import json, math, random, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import r3_independent as R

t6, s6, t9, s9 = R.target(); arms = R.load_census(); cf0 = R.cfg_seq()


def cells(rsA0, rsA1, cfA0, cfA1):
    A1u = R.Typ(R.model(rsA1, cfA1), s6); A1h = R.Typ(R.model(rsA1, cfA1, fixed=(1, 0, 0), c=3), s6); A0u = R.Typ(R.model(rsA0, cfA0), s6)
    return {"D1 p_nn A1u": float(A1u.pnn(t6)[0][0]), "D1h p_nn A1h": float(A1h.pnn(t6)[0][0]), "p_F A1u": float(A1u.pF(t6)[0][0]),
            "p_F A0u": float(A0u.pF(t6)[0][0]), "p_nn A0u": float(A0u.pnn(t6)[0][0])}


def summarize(L):
    out = {}
    for k in L[0]:
        v = np.array([x[k] for x in L])
        out[k] = {"mean": float(v.mean()), "sd": float(v.std()), "min": float(v.min()), "q05": float(np.quantile(v, 0.05)),
                  "median": float(np.median(v)), "q95": float(np.quantile(v, 0.95)), "max": float(v.max()), "share > 0.05": float(np.mean(v > 0.05))}
    out["D1 holds"] = float(np.mean([x["D1 p_nn A1u"] > 0.05 for x in L])); out["D1h holds"] = float(np.mean([x["D1h p_nn A1h"] > 0.05 for x in L]))
    out["D2 holds"] = float(np.mean([x["p_F A1u"] > 0.05 and x["p_F A0u"] <= 0.05 for x in L]))
    out["D2 by p_nn holds"] = float(np.mean([x["D1 p_nn A1u"] > 0.05 and x["p_nn A0u"] <= 0.05 for x in L]))
    return out


if __name__ == "__main__":
    out = {"sealed": cells(arms["A0"], arms["A1"], cf0, cf0)}
    print("sealed", out["sealed"], flush=True)
    rng = np.random.default_rng(814)
    halves = []
    for _ in range(100):
        p0 = rng.permutation(4000); p1 = rng.permutation(4000)
        for part in (slice(0, 2000), slice(2000, 4000)):
            i0, i1 = np.sort(p0[part]), np.sort(p1[part])
            halves.append(cells([arms["A0"][i] for i in i0], [arms["A1"][i] for i in i1], [cf0[i] for i in i0], [cf0[i] for i in i1]))
    out["halves (200 = 100 splits x 2)"] = summarize(halves); print("halves", json.dumps(out["halves (200 = 100 splits x 2)"]), flush=True)
    subs = []
    for _ in range(200):
        i0, i1 = np.sort(rng.choice(4000, 3000, replace=False)), np.sort(rng.choice(4000, 3000, replace=False))
        subs.append(cells([arms["A0"][i] for i in i0], [arms["A1"][i] for i in i1], [cf0[i] for i in i0], [cf0[i] for i in i1]))
    out["subsamples 3000 of 4000 (200)"] = summarize(subs); print("subs", json.dumps(out["subsamples 3000 of 4000 (200)"]), flush=True)
    cseeds = []
    for s in range(1, 101):
        cf = R.cfg_seq(seed=s); cseeds.append(cells(arms["A0"], arms["A1"], cf, cf))
    out["configuration seeds 1-100"] = summarize(cseeds); print("cfseeds", json.dumps(out["configuration seeds 1-100"]), flush=True)
    # the horocycle by hand: data and random hierarchies (seeds 1741-1744, 4 000 each)
    hb = {}
    for h, name in ((0, "L_max"), (1, "L_2")):
        ty = R.Typ(R.model(arms["A1"], cf0, fixed=(1, 0, 0), c=3, horo=h), s6)
        sh = [float(np.mean(ty.pnn(R.rand_hier(s))[0] > 0.05)) for s in range(1741, 1745)]
        shF = [float(np.mean(ty.pF(R.rand_hier(s))[0] > 0.05)) for s in range(1741, 1745)]
        hb[name] = {"data p_nn": float(ty.pnn(t6)[0][0]), "data p_F": float(ty.pF(t6)[0][0]), "random hierarchies typical by p_nn": float(np.mean(sh)),
                    "by p_F": float(np.mean(shF)), "q95": ty.q95(), "d_data": float(ty.pnn(t6)[1][0])}
    out["horocycle by hand"] = hb; print("horo", hb, flush=True)
    # floor 1e-8: D1, D2 legs with r on seeds 1741-1744
    fl = {}
    for floor in (1e-16, 1e-12, 1e-8):
        A1u = R.Typ(R.model(arms["A1"], cf0, floor=floor), s6); A0u = R.Typ(R.model(arms["A0"], cf0, floor=floor), s6)
        a = [(A1u.pnn(R.rand_hier(s))[0], A0u.pnn(R.rand_hier(s))[0], A1u.pF(R.rand_hier(s))[0], A0u.pF(R.rand_hier(s))[0]) for s in range(1741, 1745)]
        fl["%g" % floor] = {"n A1u": A1u.n, "D1 p_nn": float(A1u.pnn(t6)[0][0]), "q95 A1u": A1u.q95(), "d_data A1u": float(A1u.pnn(t6)[1][0]),
                            "r D1": float(np.mean([np.mean(x[0] > 0.05) for x in a])),
                            "p_nn A0u": float(A0u.pnn(t6)[0][0]), "p_F A1u": float(A1u.pF(t6)[0][0]), "p_F A0u": float(A0u.pF(t6)[0][0]),
                            "r D2 (p_F)": float(np.mean([np.mean((x[2] > 0.05) & (x[3] <= 0.05)) for x in a])),
                            "r D2 by p_nn": float(np.mean([np.mean((x[0] > 0.05) & (x[1] <= 0.05)) for x in a]))}
    out["floors"] = fl; print("floors", json.dumps(fl), flush=True)
    (HERE / "r4_out.json").write_text(json.dumps(out, indent=1))
