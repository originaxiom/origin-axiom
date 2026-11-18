"""B1788, added 2026-11-18 for register row P-444 (data-free; no measured value is read).

B1785's FINDINGS said its three-height window fits have residual <= 0.07 everywhere; 585 of the 15,888 do not (corrected
there on 2026-10-29).  The row left two questions, answered here on B1785's own exponents.json and with this arc's own
40-digit instrument (highprec/run_high.py, tag p444, seven lines at heights 8, 10, 12, 14):
 Q1  where the 585 fits sit, and B1788's comparison with B1785's window (section 2) and B1785's medians with them left out;
 Q2  whether 'the exponents depend on the slope alone' holds on them: as window fits, and as leading exponents at height.
Reads exponents.json and highprec/high_p444.jsonl; computes nothing new at height (the run is made separately)."""
import json, math, pathlib, statistics as st
from fractions import Fraction as Fr
from collections import Counter, defaultdict
import tropical as T, classify as C, domain as D
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
BAD = 0.07

if __name__ == "__main__":
    d = json.load(open(ROOT / "frontier/B1785_the_slope_sets_the_exponents/verification/exponents.json")); keys = [k for k in d[0] if "|" in k]
    P = {rd: T.polys(rd) for rd in ("S", "St")}
    bad = [(r["alpha"], r["b"], k, r[k]["exponent"], r[k]["resid"]) for r in d for k in keys if r[k]["resid"] > BAD]; top = max(bad, key=lambda x: x[4])
    print("Q1: %d lines, %d fits each, %d in all; residual above %.2f: %d (m1/m3: %d); above 1: %d (the leptons' m1/m3: %d); the largest %.2f at (%s, %s) %s" % (
        len(d), len(keys), len(d) * len(keys), BAD, len(bad), sum(x[2].endswith("m1/m3") for x in bad), sum(x[4] > 1 for x in bad), sum(x[4] > 1 and x[2].startswith("lep") and x[2].endswith("m1/m3") for x in bad), top[4], top[0], top[1], top[2]))
    where = Counter(); tal = Counter(); agree_bad = Counter()
    for r in d:
        a, b = Fr(r["alpha"]), Fr(r["b"])
        for sec, (lf, rf) in T.SECTORS.items():
            ql, qr = T.SIXY[lf], T.SIXY[rf]; mu = T.E(ql * a, qr * a)
            w = "the torsion degeneracy (m1 = 0 exactly, B1716)" if C.torsion_deg(a, b, ql, qr) else ("a theta constant zero" if (D.zero_theta(a, b, ql) or D.zero_theta(a, b, qr)) else "the closed form's domain")
            for rd in ("S", "St"):
                e2, e3 = T.predict(P[rd], mu)
                for nm, pe in (("m2/m3", e2), ("m1/m3", e3)):
                    for hor in ("L_max", "L_2"):
                        f = r["%s|%s|%s|%s" % (sec, hor, rd, nm)]; isbad = f["resid"] > BAD; ok = abs(f["exponent"] - float(pe)) <= 0.05
                        if isbad: where[(w, nm)] += 1; agree_bad[(w.startswith("the closed"), ok)] += 1
                        if hor == "L_max" and w.startswith("the closed"): tal[(nm, "all", ok)] += 1; tal[(nm, "left in" if not isbad else "left out", ok)] += 1
    for k in sorted(where): print("Q1: of the %d, in %s, %s: %d" % (len(bad), k[0], k[1], where[k]))
    for nm in ("m2/m3", "m1/m3"):
        A, G = tal[(nm, "all", True)], tal[(nm, "left in", True)]; nA, nG = A + tal[(nm, "all", False)], G + tal[(nm, "left in", False)]
        print("Q1: B1788's comparison in B1785's window (L_max, the domain), %s: agreement within 0.05 on %d of %d (%.1f%%); with the bad fits left out %d of %d (%.1f%%); the bad fits there: %d agree, %d differ" % (nm, A, nA, 100 * A / nA, G, nG, 100 * G / nG, tal[(nm, "left out", True)], tal[(nm, "left out", False)]))
    by = defaultdict(list)
    for r in d:
        for k in keys: by[(r["alpha"], k)].append((r["b"], r[k]["exponent"], r[k]["resid"]))
    for a in ("2/5", "1/10"):
        print("Q1: B1785's medians on the slope %s, all fits against the good fits only: %s" % (a, ", ".join("%s %.3f / %.3f" % (k.replace("|L_max", ""), st.median(e for _, e, _ in by[(a, k)]), st.median([e for _, e, rs in by[(a, k)] if rs <= BAD])) for k in ("up|L_max|St|m2/m3", "down|L_max|S|m2/m3", "up|L_max|St|m1/m3", "down|L_max|S|m1/m3", "lep|L_max|S|m1/m3"))))
    key = "up|L_max|St|m2/m3"; sp = sorted(((max(e for _, e, _ in v) - min(e for _, e, _ in v), a, sum(x[2] > BAD for x in v)) for (a, k), v in by.items() if k == key and len(v) > 1), reverse=True)
    print("Q2: B1785's own statement (the up sector's m2/m3 in the seat's reading varies over the offsets by at most 0.042, 0.25 at the slope 1/4): the two largest spreads are %.3f at %s and %.3f at %s, with every fit counted; %d fits of this key are bad (on the slopes %s) and the statement holds with them in" % (sp[0][0], sp[0][1], sp[1][0], sp[1][1], sum(x[2] for x in sp), sorted(x[1] for x in sp if x[2])))
    dev = []; alone = 0
    for (a, k), v in by.items():
        g = [e for _, e, rs in v if rs <= BAD]; bd = [e for _, e, rs in v if rs > BAD]
        if bd and not g: alone += len(bd)
        elif bd: dev += [abs(e - st.median(g)) for e in bd]
    print("Q2: as window fits: of the %d bad fits, %d have a good fit on the same slope and key; %d of those lie within 0.05 of that slope's good median and %d lie more than 0.25 from it. On them the window's number does not depend on the slope alone" % (len(bad), len(dev), sum(x <= 0.05 for x in dev), sum(x > 0.25 for x in dev)))
    print("Q2: in the closed form's domain, %d of the bad fits agree with the closed form within 0.05 and %d differ; outside it (the degeneracy) all %d differ, where no exponent exists" % (agree_bad[(True, True)], agree_bad[(True, False)], agree_bad[(False, False)] + agree_bad[(False, True)]))
    rows = [json.loads(l) for l in open(HERE / "highprec" / "high_p444.jsonl")]; cases = []; worst = (0, None); nb = 0
    for a, b, sec in dict.fromkeys((r["a"], r["b"], r["sec"]) for r in rows):
        rs = sorted([r for r in rows if (r["a"], r["b"], r["sec"]) == (a, b, sec)], key=lambda r: r["y"]); ys = [r["y"] for r in rs]
        lf, rf = T.SECTORS[sec]; mu = T.E(T.SIXY[lf] * Fr(a), T.SIXY[rf] * Fr(a)); rec = next(r for r in d if (r["alpha"], r["b"]) == (a, b))
        for rd in ("S", "St"):
            e2, e3 = T.predict(P[rd], mu)
            for idx, nm, pe in ((0, "m2/m3", e2), (1, "m1/m3", e3)):
                v = [math.log(float(r[rd][idx])) for r in rs]; loc = [-(v[n + 1] - v[n]) / (2 * math.pi * (ys[n + 1] - ys[n])) for n in range(len(ys) - 1)]; f = rec["%s|L_max|%s|%s" % (sec, rd, nm)]
                if f["resid"] > BAD:
                    nb += 1; print("Q2: at 40 digits, (%s, %s) %s %s %s: window fit %.3f (residual %.2f); closed form %s = %.4f; local exponents between heights 8, 10, 12, 14: %s" % (a, b, sec, rd, nm, f["exponent"], f["resid"], pe, float(pe), ", ".join("%.4f" % x for x in loc)))
                gap = abs(loc[-1] - float(pe)); cases.append((gap, abs(loc[-1] - float(pe)) <= abs(loc[0] - float(pe)) + 1e-4))
                if gap > worst[0]: worst = (gap, (a, b, sec, rd, nm, pe))
    print("Q2: on the %d lines run, all %d (reading, ratio) cases: the last local exponent is within %.4f of the closed form (the largest gap is at %s, a line of closed value %s, where a logarithmic prefactor is known, B1788 section 2); it is no further from it than the first in %d of %d; the bad fits among them: %d" % (len(set((r["a"], r["b"], r["sec"]) for r in rows)), len(cases), worst[0], worst[1][:5], worst[1][5], sum(c[1] for c in cases), len(cases), nb))
