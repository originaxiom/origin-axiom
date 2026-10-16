"""W98: W95 by trace (the owner's P-180 ruling). The rule (W98_RULE.md, 065b73f8f) was committed before this script.

  T1  the threads: 245 classes in the layers 3 <= t <= 40, each of automorph trace t; the Lyndon words of length <= 12
      with both letters and trace <= 40 are, by rotation, exactly the words of the classes of length <= 12
  T2  convergence: every class and every layer, ln(m1/m3), ln(m2/m3) between the two node counts below 1e-6
  T3  the cross-check with W95: every class in both runs that W95 sized correctly agrees to 1e-8; every D <= 300 whose
      classes lie in the layers, rebuilt from the saved matrices, agrees with W95's D-trace to 1e-8 where that converged
  T4  the law in t: over 20 <= t <= 40 both slopes against t negative, the first steeper
  T5  kappa at t = 40 in [1.3, 1.7]
  T6  no layer within W66's allowance of any sector (Sigma z^2 <= 5.991)
  read-outs: the layers' masses and kappa; the threads' masses; the nearest layer per sector; W95's under-sized classes

The instrument is W95's (the_traces_by_discriminant.py, imported): W72's units, no hypercharge line, the matrices at the
reduced point by their series, 80 digits. One repair: the node counts ceil(30 P (1 + H)) and ceil(37.5 P (1 + H)) use
H = sqrt(D) / (2 m), m the least of a, c and b - a - c over the class's Zagier cycle (its least represented value).

Run: python3 the_traces_by_trace.py  ->  the_traces_by_trace.json beside it (4 processes).
"""
import json
import math
import multiprocessing as mpr
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_traces_by_discriminant as W  # noqa: E402

OUT = HERE / "the_traces_by_trace.json"
W95 = HERE / "the_traces_by_discriminant.json"
TMAX, T_SLOPE = 40, 20


def cycle_min(cyc):
    return min(min(a, c, b - a - c) for (a, b, c), _ in cyc)


def layer_classes():
    out = []
    for t in range(3, TMAX + 1):
        disc = t * t - 4
        for u in range(1, math.isqrt(disc) + 1):
            if disc % (u * u):
                continue
            D = disc // (u * u)
            if D < 5 or D % 4 not in (0, 1) or math.isqrt(D) ** 2 == D:
                continue
            for cyc in W.zagier_cycles(D):
                rec = W.class_record(D, cyc)
                if rec["automorph trace"] != t:
                    continue
                m = cycle_min(cyc)
                rec.update({"t": t, "m": m, "H_true": math.sqrt(D) / (2 * m)})
                out.append(rec)
    return out


def mstr(M):
    return [[[mp.nstr(mp.re(M[i, k]), 45), mp.nstr(mp.im(M[i, k]), 45)] for k in range(3)] for i in range(3)]


def zscore(ratios, r_calc, data):
    v, sg = data
    out = {}
    for sec, (f1, f2, f3) in {"up": ("u", "c", "t"), "down": ("d", "s", "b"), "lepton": ("e", "mu", "tau")}.items():
        r = [math.log(v[f1] / v[f3]), math.log(v[f2] / v[f3])]
        rd = [math.hypot(sg[f1] / v[f1], sg[f3] / v[f3]), math.hypot(sg[f2] / v[f2], sg[f3] / v[f3])]
        z = [(ratios[j] - r[j]) / math.sqrt(r_calc ** 2 + rd[j] ** 2 + 0.10 ** 2) for j in range(2)]
        out[sec] = (z[0] ** 2 + z[1] ** 2, r)
    return out


def main():
    t00 = time.time()
    out = {"rule": "W98_RULE.md (065b73f8f)", "status": "one run", "instrument": "W95's, imported", "dps": W.DPS,
           "t range": [3, TMAX]}
    units, info = W.build_units()
    W.UNITS = units
    W.LO = min(min(u) for u in units.values())
    W.HI = max(max(u) for u in units.values())
    info["build seconds"] = round(time.time() - t00, 1)
    out["units"] = info
    mp.mp.dps = W.DPS

    # T1
    classes = layer_classes()
    bad = [c for c in classes if W.word_disc(c["word"]) != (c["D"], c["t"])]
    short = sorted(W.rot_min(c["word"]) for c in classes if c["length"] <= 12)
    lyn = sorted(w for w in W.lyndon_words(12) if "L" in w and "R" in w and W.word_disc(w)[1] <= TMAX)
    out["T1"] = {"classes": len(classes), "word disc or trace mismatches": len(bad), "short classes": len(short),
                 "Lyndon words": len(lyn), "duplicates": len(short) - len(set(short)),
                 "holds": bool(len(classes) == 245 and not bad and short == lyn)}
    print("T1", out["T1"]["holds"], len(classes), flush=True)

    # the cycle integrals
    tasks = [((i, W.DPS), c["word"], c["D"], c["m"], W.DPS, (("n1", 30), ("n2", mp.mpf("37.5"))))
             for i, c in enumerate(classes)]
    tasks.sort(key=lambda a: -float(2 * mp.acosh(mp.mpf(classes[a[0][0]]["t"]) / 2)
                                    * (1 + classes[a[0][0]]["H_true"])))
    res = {}
    with mpr.get_context("fork").Pool(4, initializer=W.worker_init, initargs=(W.UNITS, W.LO, W.HI)) as pool:
        for key, r, P, H, sec in pool.imap_unordered(W.cycle_integral, tasks):
            for lab in r:
                r[lab]["K"], r[lab]["Y"] = mp.matrix(r[lab]["K"]), mp.matrix(r[lab]["Y"])
            res[key[0]] = (r, P, H, sec)
            print("done", key, sec, flush=True)
    mp.mp.dps = W.DPS

    # per class
    t2 = mp.mpf(0)
    for i, c in enumerate(classes):
        r, P, H, sec = res[i]
        m1, _ = W.masses(r["n1"]["K"], r["n1"]["Y"])
        m2, emin = W.masses(r["n2"]["K"], r["n2"]["Y"])
        if m1 is None or m2 is None:
            c.update({"K singular": True, "seconds": sec})
            t2 = mp.inf
            continue
        l1, l2 = W.ratios(m1), W.ratios(m2)
        d = max(abs(l2[0] - l1[0]), abs(l2[1] - l1[1]))
        t2 = max(t2, d)
        c.update({"P": P, "npts": [r["n1"]["N"], r["n2"]["N"]], "ln m1/m3": W.s(l2[0]), "ln m2/m3": W.s(l2[1]),
                  "m1/m3": float(m2[0] / m2[2]), "m2/m3": float(m2[1] / m2[2]), "r_calc": float(d), "seconds": sec,
                  "K (n2)": mstr(r["n2"]["K"]), "Y (n2)": mstr(r["n2"]["Y"])})
        if c["length"] > 200:
            c["word"] = c["word"][:200] + "..."

    # the layers
    hz = json.loads(W.HZ.read_text(encoding="utf-8"))["masses_GeV"]
    data = (hz["value"], hz["sigma"])
    layers, t6 = {}, True
    for t in range(3, TMAX + 1):
        idx = [i for i, c in enumerate(classes) if c["t"] == t]
        if not idx:
            continue
        tot = {lab: [sum((res[i][0][lab]["K"] for i in idx), mp.zeros(3, 3)),
                     sum((res[i][0][lab]["Y"] for i in idx), mp.zeros(3, 3))] for lab in ("n1", "n2")}
        m1, _ = W.masses(*tot["n1"])
        m2, _ = W.masses(*tot["n2"])
        if m1 is None or m2 is None:
            layers[str(t)] = {"classes": len(idx), "K singular": True}
            t2 = mp.inf
            continue
        l1, l2 = W.ratios(m1), W.ratios(m2)
        d = max(abs(l2[0] - l1[0]), abs(l2[1] - l1[1]))
        t2 = max(t2, d)
        top = max(idx, key=lambda i: classes[i]["H_true"])
        z = zscore([float(l2[0]), float(l2[1])], float(d), data)
        t6 = t6 and all(v[0] > 5.991 for v in z.values())
        layers[str(t)] = {"classes": len(idx), "discriminants": sorted({classes[i]["D"] for i in idx}),
                          "ln m1/m3": W.s(l2[0]), "ln m2/m3": W.s(l2[1]), "m1/m3": float(m2[0] / m2[2]),
                          "m2/m3": float(m2[1] / m2[2]), "kappa": float(l2[0] / l2[1]), "r_calc": float(d),
                          "highest thread": {"D": classes[top]["D"], "form": classes[top]["form"],
                                             "ln m1/m3": classes[top].get("ln m1/m3"),
                                             "ln m2/m3": classes[top].get("ln m2/m3")},
                          "Sigma z^2": {k: v[0] for k, v in z.items()}}
    out["T2"] = {"largest change": W.s(t2, 5), "holds": bool(t2 < mp.mpf(10) ** -6)}

    # T3: the cross-check with W95
    w95 = json.loads(W95.read_text(encoding="utf-8"))
    w95c = {(c["D"], tuple(c["form"])): c for c in w95["classes"]}
    worst_ok, under = 0.0, []
    for c in classes:
        o = w95c.get((c["D"], tuple(c["form"])))
        if o is None or "ln m1/m3" not in c or "ln m1/m3" not in o:
            continue
        dd = max(abs(float(c["ln m1/m3"]) - float(o["ln m1/m3"])), abs(float(c["ln m2/m3"]) - float(o["ln m2/m3"])))
        if o["H"] >= c["H_true"] * (1 - 1e-12):
            worst_ok = max(worst_ok, dd)
        else:
            under.append({"D": c["D"], "form": c["form"], "W95 H": o["H"], "H_true": c["H_true"],
                          "W95 r_calc": o["r_calc"], "|W95 - W98|": dd})
    rebuilt, worst_d = [], 0.0
    for D, row in w95["D-traces"].items():
        idx = [i for i, c in enumerate(classes) if c["D"] == int(D)]
        if not idx or "ln m1/m3" not in row or row["r_calc"] > 1e-8:
            continue
        if len(idx) != row["classes"]:
            rebuilt.append({"D": int(D), "missing classes": row["classes"] - len(idx)})
            continue
        K = sum((res[i][0]["n2"]["K"] for i in idx), mp.zeros(3, 3))
        Y = sum((res[i][0]["n2"]["Y"] for i in idx), mp.zeros(3, 3))
        lr = W.ratios(W.masses(K, Y)[0])
        dd = max(abs(float(lr[0]) - float(row["ln m1/m3"])), abs(float(lr[1]) - float(row["ln m2/m3"])))
        worst_d = max(worst_d, dd)
        rebuilt.append({"D": int(D), "|rebuilt - W95|": dd})
    out["T3"] = {"classes compared (W95 sized correctly), largest difference": worst_ok,
                 "discriminant sums rebuilt": sum(1 for x in rebuilt if "|rebuilt - W95|" in x),
                 "largest rebuilt difference": worst_d, "rebuilt with missing classes": [x for x in rebuilt
                                                                                         if "missing classes" in x],
                 "W95's under-sized classes (read-out)": under,
                 "holds": bool(worst_ok < 1e-8 and worst_d < 1e-8 and not any("missing classes" in x
                                                                               for x in rebuilt))}

    # T4, T5, T6
    pts = [(int(t), float(r["ln m1/m3"]), float(r["ln m2/m3"])) for t, r in layers.items()
           if "ln m1/m3" in r and int(t) >= T_SLOPE]
    slopes = []
    for j in (1, 2):
        X = [p[0] for p in pts]
        Yv = [p[j] for p in pts]
        mx, my = sum(X) / len(X), sum(Yv) / len(Yv)
        slopes.append(sum((a - mx) * (b - my) for a, b in zip(X, Yv)) / sum((a - mx) ** 2 for a in X))
    out["T4"] = {"slopes against t, 20 <= t <= 40": slopes, "holds": bool(slopes[0] < slopes[1] < 0)}
    k40 = layers.get(str(TMAX), {}).get("kappa")
    out["T5"] = {"kappa at t = 40": k40, "holds": bool(k40 is not None and 1.3 <= k40 <= 1.7)}
    out["T6"] = {"holds": bool(t6)}

    # read-outs
    near = {}
    for sec in ("up", "down", "lepton"):
        best = min((t for t, r in layers.items() if "ln m1/m3" in r), key=lambda t: layers[t]["Sigma z^2"][sec])
        r = zscore([float(layers[best]["ln m1/m3"]), float(layers[best]["ln m2/m3"])], 0.0, data)[sec][1]
        near[sec] = {"layer": int(best), "Sigma z^2": layers[best]["Sigma z^2"][sec], "data": r}
    out["read-outs"] = {"nearest layer per sector": near}
    out["layers"] = layers
    out["classes"] = classes
    out["cells"] = {k: out[k]["holds"] for k in ("T1", "T2", "T3", "T4", "T5", "T6")}
    out["seconds"] = round(time.time() - t00, 1)
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(out["cells"], out["seconds"], "s")


if __name__ == "__main__":
    main()
