"""Analyse scan.jsonl: (0) spot-check against the note's functionals.json at shared grid points; (1) the scale-free
functionals the note did not compute (sigma2/sigma1, sigma3/sigma1, inter-sector top ratios, channel differences c_j - c_k,
single channels c_s); (2) the strength below Im tau 1.5; (3) the |eta|-weighted invariant norms of the Higgs alone."""
import json, math, pathlib, collections, itertools
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
rows = [json.loads(l) for l in open(HERE / "scan.jsonl")]
print("rows", len(rows))
key = lambda q: (q["line"], q["re"])
G = collections.defaultdict(list)
for q in rows: G[key(q)].append(q)
for k in G: G[k].sort(key=lambda q: q["im"])


def extrema(ys, vs, tol=0.0):
    v = np.asarray(vs, float); d = np.diff(v); ex = []
    for k in range(1, len(d)):
        if d[k - 1] > tol and d[k] < -tol: ex.append((ys[k], "max"))
        if d[k - 1] < -tol and d[k] > tol: ex.append((ys[k], "min"))
    return ex

# ---- (0) spot-check against the note's outputs
note = json.load(open(pathlib.Path(__file__).resolve().parent.parent / "functionals.json"))
idx = {(q["line"], q["re"], q["im"]): q for q in note}
print("\n(0) spot-check against functionals.json (relative deviations)")
for pt in [("2/5,1/10", 0.3, 3.0), ("2/5,23/30", 0.3, 2.0), ("2/5,4/25", 0.3, 6.0), ("2/5,1/10", 0.3, 1.5)]:
    mine = next(q for q in rows if (q["line"], q["re"], q["im"]) == pt); theirs = idx[pt]; dev = 0.0
    for sec in ("up", "down", "lep"):
        sumc = sum(v for v in mine[sec + "|c"].values() if v is not None)
        pairs = [(sumc, theirs[sec]["F1_sum_c"]), (mine[sec + "|L_max|detM"], theirs[sec]["F2_detM"])]
        for rn in ("S", "St"):
            sv = np.array(mine["%s|L_max|%s" % (sec, rn)])
            pairs += [(np.sqrt((sv ** 2).sum()), theirs[sec]["F3_frob_" + rn]), (sv.sum(), theirs[sec]["F4_nuc_" + rn]), (sv[0], theirs[sec]["F5_smax_" + rn])]
        dev = max(dev, max(abs(a - b) / max(abs(b), 1e-300) for a, b in pairs))
    print("  ", pt, "max rel dev %.2e" % dev)

# ---- (1) scale-free functionals
print("\n(1) scale-free functionals: interior extrema in Im tau 1.0-8.0 (53 heights), per (line, Re tau) series")
fam = collections.defaultdict(lambda: [0, 0, []])
for (ln, re), sel in G.items():
    ys = [q["im"] for q in sel]
    for sec in ("up", "down", "lep"):
        for h in ("L_max", "L_2"):
            for rn in ("S", "St"):
                sv = np.array([q["%s|%s|%s" % (sec, h, rn)] for q in sel])
                for name, v in (("s2/s1", sv[:, 1] / sv[:, 0]), ("s3/s1", sv[:, 2] / sv[:, 0]), ("s1", sv[:, 0]),
                                ("y^0.5 s1", sv[:, 0] * np.sqrt(ys)), ("s3/s2", sv[:, 2] / sv[:, 1])):
                    ex = extrema(ys, np.log(v + 1e-300)); f = fam[name]; f[0] += 1
                    if ex: f[1] += 1; f[2].append((ln, re, sec, h, rn, ex))
        cs = [q[sec + "|c"] for q in sel]
        for s in ("1", "i", "j", "k"):
            if any(c[s] is None for c in cs): continue
            ex = extrema(ys, [c[s] for c in cs]); f = fam["c_" + s]; f[0] += 1
            if ex: f[1] += 1; f[2].append((ln, re, sec, ex))
        for s, t in itertools.combinations(("1", "i", "j", "k"), 2):
            if any(c[s] is None or c[t] is None for c in cs): continue
            ex = extrema(ys, [c[s] - c[t] for c in cs]); f = fam["c_%s-c_%s" % (s, t)]; f[0] += 1
            if ex: f[1] += 1; f[2].append((ln, re, sec, ex))
    for h in ("L_max", "L_2"):
        for ru, rd in (("St", "S"), ("S", "S")):
            v = np.array([q["up|%s|%s" % (h, ru)][0] / q["down|%s|%s" % (h, rd)][0] for q in sel])
            ex = extrema(ys, np.log(v)); f = fam["s1(up)/s1(down)"]; f[0] += 1
            if ex: f[1] += 1; f[2].append((ln, re, h, ru, rd, ex))
for name, (n, k, lst) in fam.items():
    locs = sorted(set(round(e[0], 3) for item in lst for e in item[-1]))
    print("  %-18s %4d series, %4d with an interior extremum; heights %s" % (name, n, k, locs[:25]))
    for item in lst[:6]: print("       ", item)

# ---- (2) the strength below 1.5
print("\n(2) seat strength s1 (up S~, down S, lep S; L_max) monotone over Im tau 1.0-1.5?")
bad = 0
for (ln, re), sel in G.items():
    ys = [q["im"] for q in sel if q["im"] <= 1.5]
    for sec, rn in (("up", "St"), ("down", "S"), ("lep", "S")):
        v = [q["%s|L_max|%s" % (sec, rn)][0] for q in sel if q["im"] <= 1.5]
        if extrema(ys, v) or np.any(np.diff(v) < 0): bad += 1; print("   non-monotone:", ln, re, sec, [round(x, 4) for x in v])
print("   non-monotone series below 1.5:", bad)

# ---- (3) the Higgs alone: y^(3/4)|S| and the invariant family y^((3+m)/4) |eta|^m |S|
print("\n(3) the Higgs alone (line-independent): Petersson y^(3/4)|dR| and y^((3+m)/4)|eta|^m |dR| (all modular-invariant in modulus)")
for re in sorted(set(q["re"] for q in rows)):
    sel = G[("2/5,1/10", re)]; ys = np.array([q["im"] for q in sel]); S = np.array([q["S_frob"] for q in sel]); et = np.array([q["eta"] for q in sel])
    out = []
    for m in (0, 3, 4, 5, 6, 7, 8, 9, 12):
        v = ys ** ((3 + m) / 4) * et ** m * S; ex = extrema(list(ys), np.log(v)); out.append((m, ex[:2] if ex else "monotone " + ("up" if v[-1] > v[0] else "down")))
    print("  Re tau %.2f:" % re, out)
print("  analytic: |dR| ~ e^{pi y/4}, |eta|^m ~ e^{-pi m y/12}: max at y = 3(3+m)/(pi(m-3)) for m > 3 (m=4: %.2f, 5: %.2f, 6: %.2f, 9: %.2f)" % tuple(3 * (3 + m) / (math.pi * (m - 3)) for m in (4, 5, 6, 9)))
print("analyse exit 0")
