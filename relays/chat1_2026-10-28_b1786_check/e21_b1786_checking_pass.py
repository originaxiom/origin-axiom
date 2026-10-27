"""e21 -- chat1's checking pass on B1786 (main's ask, accepted 2026-10-27): B1786's sealed cells and main's referee's nulls,
recomputed from main's committed census with this seat's own code.  No module of main's is imported: the seat menu's chi2_six,
the sigmas and B1741's random six-targets are re-implemented from B1741's stated definitions (its compare.py docstring,
sigmas(), chi2_features(), draws()); the line enumeration from B1786's census docstring.  A check, post hoc by nature: no cell,
no grade.
    python3 -B e21_b1786_checking_pass.py MAIN_ROOT [--workers 2] > e21_out.txt
MAIN_ROOT is a checkout of origin/main at 54cfec661 (B1786's FINDINGS); every path below is relative to it.

What main reports (FINDINGS.md, comparison.json, verification/referee/*.txt), for comparison with the output:
  K1  per-line minima of chi2_six (seat) = comparison.json's readout_per_line, on all 588 lines
  K2  class minima: 2/5 at 3.0048102; 1/10 at 919.27; the rest at 103.10 (on 12/25); no other-slope line below 16.75
  K3  P1: 12 of the 30 slope-2/5 lines below 16.75 (order 25: b = 3, 4, 11, 12, 17, 19, 21, 23 over 25; order 30: 1/6, 13/30,
      23/30, 5/6), in equal-valued pairs b <-> 3/5 - b: 6 of 15 independent pairs
  K4  the best row (2/5, 23/30) or its mirror (2/5, 5/6), at 0.269 + 3.037i, L_max, readings (S~, S, S), c = 3; model over
      measured 1.02, 1.16, 1.03, 0.83, 0.98, 0.99
  K5  the random-subset control: 11% of 200 random 30-line subsets (random.Random(1786).sample) reach as low
  K6  seeds 1829-1868 (160 000 targets): 2/5 class as low 8; any class 67; class-choosing 41; prior-chosen 18, conditional
      denominator 78 985
  K7  seeds 2001-2040: 5, 64, 38; prior-chosen 15
  K8  seeds of this seat's choosing, 9001-10250 (5 000 000 targets), against main's 10^7 (seeds 2001-4500): 2/5 4.79e-5; any
      4.18e-4; class-choosing 2.62e-4; prior-chosen 1.13e-4 unconditional and 2.29e-4 conditional (denominator fraction 0.493);
      a target fitting 2/5 at the prior orders as well as the data (<= 3.574) goes on to the event in 13% (107 of 827)
  K9  the mirror w -> -conj(w), tau -> 1 - conj(tau) (b -> -alpha - b): main reports it on 131 712 row pairs to 3e-6
  K10 B1788's statement in B1786's reading: given 5 alpha in Z, ||3 alpha|| = 1/5 iff e_up/e_down = 3/2; and the measured
      ratio ln(m_c/m_t) / ln(m_s/m_b) at M_Z (HZ2021)
"""
import sys, json, math, gzip, random, pathlib
from fractions import Fraction as Fr
import numpy as np
from scipy.spatial import cKDTree
from scipy.stats import beta

ROOT = pathlib.Path(sys.argv[1]).resolve()
NW = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 2
FR = ROOT / "frontier"
V86 = FR / "B1786_the_slope_principle_out_of_sample" / "verification"
HZ = FR / "B1637_fits_on_the_ruled_branch" / "received" / "HZ2021_running_masses_MZ.json"
P49 = FR / "B1749_the_six_at_fresh_apexes" / "verification" / "census.jsonl"
P55 = FR / "B1755_the_six_on_the_lines_of_order_13_to_20" / "verification" / "census.jsonl"
BAR, N_PER_SEED, LC3 = 16.75, 4000, math.log(3)
RD = ("S", "St")
SEAT = [((1, 0, 0), 0.0), ((1, 0, 0), LC3), ((1, 1, 1), 0.0), ((1, 1, 1), LC3)]   # (up, down, lepton) reading, ln c


def lg(x):
    return np.log(np.maximum(np.array(x, dtype=float), 1e-300))


def targets_and_sigmas():
    d = json.loads(HZ.read_text(encoding="utf-8"))["masses_GeV"]; v, e = d["value"], d["sigma"]
    pr = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
    T6 = np.log(np.array([v[a] / v[b] for a, b in pr]))
    s6 = np.array([math.sqrt((e[a] / v[a]) ** 2 + (e[b] / v[b]) ** 2 + 0.10 ** 2) for a, b in pr])
    return T6, s6, v


def read_rows(path, gz=False):
    op = (lambda p: gzip.open(p, "rt", encoding="utf-8")) if gz else (lambda p: open(p, encoding="utf-8"))
    out = []
    with op(path) as fh:
        for l in fh:
            if not l.strip(): continue
            r = json.loads(l)
            rec = {k: r.get(k) for k in ("line", "alpha", "b", "order", "Re_tau", "Im_tau", "apex")}
            for h in ("L_max", "L_2"):
                rec[h] = np.array([[lg(r["%s|%s|%s" % (s, h, a)]) for a in RD] for s in ("up", "down", "lep")])   # (3, 2, 2)
            out.append(rec)
    return out


def features(rows, s6):
    """per (row, horocycle): the four seat configurations' scaled six (4, n, 6), and the labels"""
    G, lab = [], []
    for r in rows:
        for h in ("L_max", "L_2"):
            G.append(r[h]); lab.append((r["line"], r["alpha"], r["b"], r["Re_tau"], r["Im_tau"], h))
    G = np.array(G)                      # (n, 3 sectors, 2 readings, 2 ratios)
    X = []
    for (a, b, l), k in SEAT:
        X.append(np.concatenate([G[:, 0, a], G[:, 1, b], (G[:, 2, l, 0] + k)[:, None], (G[:, 2, l, 1] - k)[:, None]], axis=1) / s6)
    return np.stack(X), lab, G


def lines_upto(orders):
    """B1726's enumeration as B1786's census docstring states it: gcd(j, k, N) = 1, key = min((a, b), (-a, -b) mod 1)"""
    seen, out = set(), []
    for N in orders:
        for j in range(N):
            for k in range(N):
                if math.gcd(math.gcd(j, k), N) != 1: continue
                a, b = Fr(j, N), Fr(k, N); key = min((a, b), ((-a) % 1, (-b) % 1))
                if key in seen: continue
                seen.add(key); out.append(key)
    return out


def draws(seed, n=N_PER_SEED):
    """B1741's six-targets, re-implemented: per sector r2 = 10^U(-3,-1), r1 = 10^U(-6,-2.5), redrawn until r1 < r2"""
    rng = random.Random(seed); out = []
    for _ in range(n):
        tg = []
        for _s in range(3):
            while True:
                r2 = 10 ** rng.uniform(-3, -1); r1 = 10 ** rng.uniform(-6, -2.5)
                if r1 < r2: break
            tg += [r2, r1]
        out.append(np.log(np.array(tg)))
    return np.array(out)


def cp(k, n):
    return float(beta.ppf(0.975, k + 1, n - k)) if k < n else 1.0


_G = {}


def classmin_exact(t):
    """the 26 class minima of chi2_six (seat) at orders 25/30 for one scaled target, by direct differences"""
    P, st = _G["P_sorted"], _G["starts"]
    d = ((P - t) ** 2).sum(1)
    return np.minimum.reduceat(d, st)


def work(seed):
    T = draws(seed) / _G["s6"]
    dist, _ = _G["tree25"].query(T, k=1, distance_upper_bound=math.sqrt(_G["obs"] + 0.5))
    cand = np.flatnonzero(np.isfinite(dist))
    cm = np.array([classmin_exact(T[j]) for j in cand]).reshape(len(cand), -1)
    pd, pi = _G["treeP"].query(T, k=1)
    pcls = _G["pcid"][pi % _G["nP"]]
    return seed, len(T), cand, cm, pd ** 2, pcls


def tally(results, name):
    cl, i25, obs = _G["classes"], _G["classes"].index("2/5"), _G["obs"]
    n = sum(r[1] for r in results)
    e1 = e2 = e3 = e4 = 0; dens = 0; fit_t = fit_e = 0; closest = math.inf
    carry = {}
    for seed, nn, cand, cm, pd2, pcls in results:
        present = np.array([_G["pclasses"][c] in _G["cls_set"] for c in pcls])
        dens += int(present.sum())
        for j, row in zip(cand, cm):
            s = np.sort(row); closest = min(closest, float(np.min(np.abs(row - obs))))
            if row[i25] <= obs + 1e-9: e1 += 1
            if s[0] <= obs + 1e-9:
                e2 += 1; c0 = cl[int(np.argmin(row))]; carry[c0] = carry.get(c0, 0) + 1
            if s[0] <= obs + 1e-9 and s[1] >= BAR: e3 += 1
            pc = _G["pclasses"][pcls[j]]
            if pc in _G["cls_set"]:
                ci = cl.index(pc)
                ev = row[ci] <= obs + 1e-9 and np.delete(row, ci).min() >= BAR
                e4 += int(ev)
                if pc == "2/5" and pd2[j] <= _G["prior_obs"] + 1e-9: fit_e += int(ev)
        fit_t += int(np.sum((pd2 <= _G["prior_obs"] + 1e-9) & (np.array([_G["pclasses"][c] for c in pcls]) == "2/5")))
    print("\n== %s: %d targets" % (name, n))
    for lab, k, nn in (("2/5 class as low (the sealed conjunct)", e1, n), ("any class as low", e2, n),
                       ("class-choosing: some class as low, every other >= 16.75", e3, n),
                       ("prior-chosen class, unconditional", e4, n), ("prior-chosen class, conditional on its presence at 25/30", e4, dens)):
        r = cp(k, nn)
        print("  %-62s %6d / %9d = %.3e   r97.5 %.3e   m*r: 41 -> %.4f, 73 -> %.4f" % (lab, k, nn, k / nn, r, 41 * r, 73 * r))
    print("  fraction of targets whose prior class has lines at 25/30: %.4f" % (dens / n))
    print("  any-class hits by carrying class (top 6): %s" % sorted(carry.items(), key=lambda x: -x[1])[:6])
    print("  prior fit as good as the data's (<= %.4f) with prior class 2/5: %d targets; the event follows in %d (%.3f)"
          % (_G["prior_obs"], fit_t, fit_e, fit_e / fit_t if fit_t else float("nan")))
    print("  closest |class minimum - obs| among candidates: %.2e" % closest)


def main():
    T6, s6, vals = targets_and_sigmas(); t6 = T6 / s6
    _G["s6"] = s6
    rows = read_rows(V86 / "census.jsonl.gz", gz=True)
    X, lab, G = features(rows, s6)
    nrow = X.shape[1]
    d2 = ((X - t6) ** 2).sum(2)                         # (4, n)
    best_row = d2.min(0)
    line = np.array([l[0] for l in lab]); alpha = np.array([str(l[1]) for l in lab])
    print("census: %d rows of (point, horocycle); %d lines; apexes %d" % (nrow, len(set(line)), len({(l[3], l[4]) for l in lab})))
    # K1
    cmp = json.loads((V86 / "comparison.json").read_text(encoding="utf-8")); plb = cmp["readout_per_line"]
    per_line = {int(k): float(best_row[line == int(k)].min()) for k in plb}
    dev = max(abs(per_line[int(k)] - v["chi2_six_seat"]) for k, v in plb.items())
    print("K1 per-line minima vs comparison.json: max |difference| %.2e over %d lines" % (dev, len(plb)))
    # K2
    classes = sorted({str(a) for a in alpha}, key=Fr)
    cmin = {c: float(best_row[alpha == c].min()) for c in classes}
    srt = sorted(cmin.items(), key=lambda x: x[1])
    obs = cmin["2/5"]
    print("K2 class minima: 2/5 %.7f; 1/10 %.2f; least other class %s at %.2f; then %s"
          % (obs, cmin["1/10"], srt[1][0], srt[1][1], ", ".join("%s %.1f" % x for x in srt[2:6])))
    other_below = [(k, v) for k, v in plb.items() if v["alpha"] != "2/5" and per_line[int(k)] < BAR]
    print("   other-slope lines below 16.75: %d; classes present: %d; lines per class: %s"
          % (len(other_below), len(classes), {c: len(set(line[alpha == c])) for c in classes}))
    v110 = sorted(per_line[int(k)] for k, v in plb.items() if v["alpha"] == "1/10")
    print("   the 20 slope-1/10 lines' minima: %.1f to %.1f" % (v110[0], v110[-1]))
    # K3
    l25 = {int(k): (v["b"], v["order"]) for k, v in plb.items() if v["alpha"] == "2/5"}
    below = sorted((Fr(b), o, per_line[k]) for k, (b, o) in l25.items() if per_line[k] < BAR)
    print("K3 slope-2/5 lines below 16.75: %d of %d" % (len(below), len(l25)))
    for o in (25, 30):
        print("   order %d: %s" % (o, ", ".join("%s (%.2f)" % (b, c) for b, oo, c in below if oo == o)))
    byb = {Fr(b): per_line[k] for k, (b, o) in l25.items()}
    pairs = set(); worst = 0.0
    for b in byb:
        m = (Fr(3, 5) - b) % 1
        pairs.add(tuple(sorted((b, m)))); worst = max(worst, abs(byb[b] - byb[m]) / byb[b])
    carrying = {p for p in pairs if byb[p[0]] < BAR}
    print("   mirror pairs b <-> 3/5 - b: %d independent pairs, %d carry the six; max relative difference within a pair %.1e"
          % (len(pairs), len(carrying), worst))
    # K4
    i25 = np.flatnonzero(alpha == "2/5")
    flat = d2[:, i25]; cfg, j = np.unravel_index(np.argmin(flat), flat.shape); i = i25[j]
    tied = np.flatnonzero(np.abs(d2.min(0) - flat.min()) < 1e-6)
    (a_, b_, l_), k_ = SEAT[cfg]
    six = np.concatenate([G[i, 0, a_], G[i, 1, b_], [G[i, 2, l_, 0] + k_, G[i, 2, l_, 1] - k_]])
    print("K4 chi2-best slope-2/5 row: line (2/5, %s) at %.4f + %.4fi, %s, readings (%s, %s, %s), c = %d, chi2 %.6f"
          % (lab[i][2], lab[i][3], lab[i][4], lab[i][5], RD[a_], RD[b_], RD[l_], round(math.exp(k_)), flat.min()))
    print("   model over measured: %s" % ", ".join("%.3f" % x for x in np.exp(six - T6)))
    print("   rows within 1e-6 of it: %s" % [(lab[t][1], lab[t][2], round(lab[t][3], 4), round(lab[t][4], 4), lab[t][5], float(d2[:, t].min())) for t in tied])
    # the coarse measure's pick (the worst factor over the seat menu with c in {1, 3}), as describe() picks it
    wf = []
    for (a, b, l), k in SEAT:
        dd = np.abs(np.concatenate([G[i25, 0, a], G[i25, 1, b], (G[i25, 2, l, 0] + k)[:, None], (G[i25, 2, l, 1] - k)[:, None]], axis=1) - T6)
        wf.append(dd.max(1))
    wf = np.array(wf); cw, jw = np.unravel_index(np.argmin(wf), wf.shape); iw = i25[jw]
    print("   the smallest worst factor on slope 2/5: %.4f at (2/5, %s) %.4f + %.4fi %s (chi2 there %.4f)"
          % (math.exp(wf.min()), lab[iw][2], lab[iw][3], lab[iw][4], lab[iw][5], d2[:, iw].min()))
    # K5
    ids = sorted(int(k) for k in plb); rng = random.Random(1786); low = 0; low_with = 0
    best_lines = {int(k) for k, v in plb.items() if abs(per_line[int(k)] - obs) < 1e-6}
    for _ in range(200):
        s = rng.sample(ids, 30); m = min(per_line[x] for x in s)
        if m <= obs + 1e-9:
            low += 1; low_with += int(bool(best_lines & set(s)))
    p_two = 1 - math.comb(588 - len(best_lines), 30) / math.comb(588, 30)
    p_any25 = 1 - math.comb(558, 30) / math.comb(588, 30)
    print("K5 random 30-line subsets as low: %d of 200 (%.3f); each contains one of the %d tied best lines: %d of %d"
          % (low, low / 200, len(best_lines), low_with, low))
    print("   chance a random 30-line subset contains one of those lines %.4f; contains any slope-2/5 line %.4f" % (p_two, p_any25))
    # K9: the mirror at row level
    key = {}
    for t, l in enumerate(lab):
        key[(Fr(l[1]), Fr(l[2]), round(l[3], 9), round(l[4], 9), l[5])] = t
    npair = 0; mx = {0: 0.0, 1: 0.0}
    for t, l in enumerate(lab):
        a, b = Fr(l[1]), Fr(l[2]); bm = (-a - b) % 1
        kk = min((a, bm), ((-a) % 1, (-bm) % 1))
        u = key.get((kk[0], kk[1], round(1 - l[3], 9), round(l[4], 9), l[5]))
        if u is None: continue
        npair += 1
        for swap in (0, 1):
            g2 = G[u][:, ::-1] if swap else G[u]
            mx[swap] = max(mx[swap], float(np.max(np.abs(G[t] - g2))))
    print("K9 rows with a mirror partner (alpha, -alpha - b) at 1 - conj(tau): %d of %d; max |delta ln| over the 12 ratios: "
          "readings kept %.1e, readings swapped %.1e" % (npair, nrow, mx[0], mx[1]))
    # K10
    nrm = lambda x: abs(x - round(x))
    e2 = lambda a, qL, qR: 0.5 - (nrm(2 * qL * a) + nrm(2 * qR * a)) / 2
    print("K10 given 5 alpha in Z: alpha, ||3 alpha||, (e_up, e_down, e_lep), e_up/e_down")
    for a in (Fr(1, 5), Fr(2, 5), Fr(3, 5), Fr(4, 5)):
        eu, ed, el = e2(a, 1, -4), e2(a, 1, 2), e2(a, -3, -6)
        print("   %s: %s, (%s, %s, %s), %s" % (a, Fr(nrm(3 * a)).limit_denominator(100), Fr(eu).limit_denominator(100),
              Fr(ed).limit_denominator(100), Fr(el).limit_denominator(100), Fr(eu / ed).limit_denominator(100)))
    sol = sorted({a for q in range(1, 121) for p in range(q) for a in [Fr(p, q)]
                  if abs(e2(a, 1, -4) - 0.3) < 1e-12 and abs(e2(a, 1, 2) - 0.2) < 1e-12})
    print("   alpha in [0, 1) with denominator <= 120 giving (e_up, e_down) = (3/10, 1/5): %s" % [str(a) for a in sol])
    rmeas = math.log(vals["c"] / vals["t"]) / math.log(vals["s"] / vals["b"])
    print("   measured ln(m_c/m_t) / ln(m_s/m_b) at M_Z (HZ2021): %.4f; the two values five-ality allows: 1/2 and 3/2" % rmeas)
    # the nulls
    order = np.argsort([classes.index(a) for a in alpha], kind="stable")
    cid_rows = np.array([classes.index(a) for a in alpha])[order]
    P = X[:, order, :]                                  # (4, n, 6), rows grouped by class
    P_sorted = np.concatenate([P[c] for c in range(4)], axis=0)
    cid_all = np.concatenate([cid_rows] * 4)
    o2 = np.argsort(cid_all, kind="stable"); P_sorted = P_sorted[o2]; cid_all = cid_all[o2]
    starts = np.r_[0, np.flatnonzero(np.diff(cid_all)) + 1]
    assert len(starts) == len(classes) == 26
    _G.update(P_sorted=P_sorted, starts=starts, obs=obs, classes=classes, cls_set=set(classes),
              tree25=cKDTree(X.reshape(-1, 6)))
    chk = classmin_exact(t6)
    print("\nnull set-up: data's class minima recomputed through the null's path: 2/5 %.10f (direct %.10f)" % (chk[classes.index("2/5")], obs))
    L26 = lines_upto(range(1, 13))
    assert len(L26) == 266
    pr = read_rows(P49)
    for r in pr: r["alpha"] = str(L26[r["line"]][0]); r["b"] = str(L26[r["line"]][1])
    pr55 = read_rows(P55)
    XP, labP, _ = features(pr + pr55, s6)
    pclasses = sorted({l[1] for l in labP}, key=lambda s: Fr(s))
    pcid = np.array([pclasses.index(l[1]) for l in labP])
    dP = ((XP - t6) ** 2).sum(2).min(0)
    src = np.array([0] * (2 * len(pr)) + [1] * (2 * len(pr55)))
    pmin = {c: float(dP[pcid == i].min()) for i, c in enumerate(pclasses)}
    ps = sorted(pmin.items(), key=lambda x: x[1])
    print("prior lines (B1749 orders 1-12, B1755 orders 13, 14, 15, 20): %d rows, %d classes, %d of them present at 25/30"
          % (len(labP), len(pclasses), len(set(pclasses) & set(classes))))
    print("   data: B1749's minimum %.4f, B1755's %.4f; prior argmin class %s at %.4f, runner-up %s at %.2f"
          % (dP[src == 0].min(), dP[src == 1].min(), ps[0][0], ps[0][1], ps[1][0], ps[1][1]))
    _G.update(treeP=cKDTree(XP.reshape(-1, 6)), pcid=pcid, nP=XP.shape[1], pclasses=pclasses, prior_obs=ps[0][1])
    from multiprocessing import Pool
    with Pool(NW) as Pl:
        for name, lo, hi in (("K6, seeds 1829-1868 (B1786's sealed seeds)", 1829, 1868), ("K7, seeds 2001-2040", 2001, 2040),
                             ("K8, seeds 9001-10250 (this seat's)", 9001, 10250)):
            res = list(Pl.imap_unordered(work, range(lo, hi + 1), chunksize=5))
            tally(res, name)
            sys.stdout.flush()
    print("\ne21 exit 0")


if __name__ == "__main__":
    main()
