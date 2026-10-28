"""R71-1 draft read-outs: per arc, the class-choosing nulls from kd_<arc>_*.npz (candidates' per-line minima) and
feat_<arc>.npz (the data's per-line minima, line table), with THE_BAR's r (exact 97.5% Clopper-Pearson upper end) and m*r.
    python3 -B analyse.py ARC KDFILE [KDFILE ...]"""
import sys, pathlib
from fractions import Fraction as Fr
import numpy as np
from scipy.stats import beta
HERE = pathlib.Path(__file__).resolve().parent
BAR = 16.75
MS = {"b1749": (33, 35, 59), "b1753_all": (39, 41, 68, 70), "b1753_48": (39, 41, 68, 70), "b1753_part": (39, 41, 68, 70)}


def r975(h, n): return float(beta.ppf(0.975, h + 1, n - h)) if h < n else 1.0


def main():
    args = sys.argv[1:]; obs_override = None
    if "--obs" in args:
        i = args.index("--obs"); obs_override = float(args[i + 1]); del args[i:i + 2]
    arc = args[0]; files = args[1:]
    f = np.load(HERE / ("feat_%s.npz" % arc)); dmin = f["data_line_min"]
    alpha = [str(a) for a in f["alpha"]]; order = [int(o) for o in f["order"]]
    obs = 3.573708662392164 if arc == "b1749" else 2.739034460748371
    if obs_override is not None: obs = obs_override
    n = 0; P = []; seeds = []
    for p in files:
        k = np.load(HERE / p); n += int(k["n"]); P.append(k["plm"]); seeds += list(k["seeds"])
    assert len(seeds) == len(set(seeds))
    M = np.concatenate(P, axis=1)                         # 266 x candidates
    present = np.isfinite(dmin)
    lo = M <= obs + 1e-9
    ms = MS[arc]

    def line(label, h):
        r = r975(h, n)
        return "%-66s hits %6d  frac %.4e  r97.5 %.4e  " % (label, h, h / n, r) + "  ".join("m*r(%d) %.4f" % (m, m * r) for m in ms)

    def part_min(Mx, labels):
        keys = sorted(set(labels[i] for i in range(266) if present[i]), key=lambda s: Fr(s) if isinstance(s, str) else s)
        out = np.stack([Mx[[i for i in range(266) if present[i] and labels[i] == k]].min(0) for k in keys])
        return keys, out

    print("== %s: %d targets (seeds %d-%d, %d seeds), %d candidates; obs %.9f; lines present %d" % (arc, n, min(seeds), max(seeds), len(seeds), M.shape[1], obs, present.sum()))
    print("data: all-lines min %.6f" % np.nanmin(np.where(present, dmin, np.nan)))
    print(line("ALL LINES (= ANY CLASS of any partition of the lines present) <= obs", int(lo.any(0).sum())))
    # slope partition
    for name, labels in (("slope", alpha), ("order", [str(o) for o in order])):
        keys, CM = part_min(M, labels)
        dk, dCM = part_min(dmin[:, None], labels)
        srt = np.sort(CM, axis=0)
        dbest = int(np.argmin(dCM[:, 0])); dsrt = np.sort(dCM[:, 0])
        print("-- partition by %s: %d classes; data's best class %s (%.4f), data's runner-up class %.4f; data classes below %.2f: %s" % (
            name, len(keys), keys[dbest], dCM[dbest, 0], dsrt[1], BAR, [(keys[i], round(float(dCM[i, 0]), 3)) for i in range(len(keys)) if dCM[i, 0] < BAR]))
        anyc = (CM <= obs + 1e-9).any(0)
        strict = anyc & (srt[1] >= BAR)
        print(line("  ANY %s class <= obs" % name, int(anyc.sum())))
        print(line("  STRICT: some %s class <= obs AND every other >= 16.75" % name, int(strict.sum())))
        if name == "slope" and "2/5" in keys:
            i25 = keys.index("2/5"); o = np.delete(CM, i25, axis=0).min(0)
            print(line("  the 2/5 slope class <= obs", int((CM[i25] <= obs + 1e-9).sum())))
            print(line("  the 2/5 slope class <= obs AND every other slope >= 16.75", int(((CM[i25] <= obs + 1e-9) & (o >= BAR)).sum())))
        if name == "order" and arc == "b1749":
            pass
    # the order-divisibility family D_d (overlapping), d = 1..12
    fam = {d: np.array([present[i] and order[i] % d == 0 for i in range(266)]) for d in range(1, 13)}
    Dm = {d: M[fam[d]].min(0) if fam[d].any() else np.full(M.shape[1], np.inf) for d in fam}
    Dc = {d: M[present & ~fam[d]].min(0) if (present & ~fam[d]).any() else np.full(M.shape[1], np.inf) for d in fam}
    dD = {d: float(dmin[fam[d]].min()) if fam[d].any() else np.inf for d in fam}
    dDc = {d: float(dmin[present & ~fam[d]].min()) if (present & ~fam[d]).any() else np.inf for d in fam}
    print("-- the order-divisibility family D_d (d | order): lines per d %s" % {d: int(fam[d].sum()) for d in fam})
    print("   data min on D_d: %s" % {d: round(dD[d], 3) for d in fam})
    print("   data min off D_d: %s" % {d: round(dDc[d], 3) for d in fam})
    any_fam = np.zeros(M.shape[1], bool); any_fam2 = np.zeros(M.shape[1], bool); strict_fam = np.zeros(M.shape[1], bool)
    for d in fam:
        hit = Dm[d] <= obs + 1e-9
        any_fam |= hit
        if d >= 2:
            any_fam2 |= hit; strict_fam |= hit & (Dc[d] >= BAR)
    print(line("  ANY D_d (d = 1..12) <= obs", int(any_fam.sum())))
    print(line("  ANY D_d (d = 2..12) <= obs (the trivial line dropped)", int(any_fam2.sum())))
    print(line("  STRICT: some D_d (d >= 2) <= obs AND every line off D_d >= 16.75", int(strict_fam.sum())))
    print(line("  D_5 <= obs (the sealed class, fresh targets)", int((Dm[5] <= obs + 1e-9).sum())))
    print(line("  D_5 <= obs AND every line off D_5 >= 16.75", int(((Dm[5] <= obs + 1e-9) & (Dc[5] >= BAR)).sum())))
    print(line("  D_10 <= obs (order 10 alone)", int((Dm[10] <= obs + 1e-9).sum())))
    # which line carries the any-class hits
    best_line = np.argmin(M[:, lo.any(0)], axis=0)
    from collections import Counter
    cs = Counter(alpha[i] for i in best_line); co = Counter(order[i] for i in best_line)
    print("  all-lines hits by best line's slope (top 12): %s" % cs.most_common(12))
    print("  all-lines hits by best line's order: %s" % sorted(co.items()))
    print("analyse exit 0")


if __name__ == "__main__":
    main()
