"""Referee analysis (B1786): the class-choosing null from classmin_<seed>.npy."""
import sys, pathlib, json
import numpy as np
from scipy.stats import beta
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import null
D = pathlib.Path(__file__).resolve().parent
f = np.load(D / "features.npz"); cl = list(f["classes"]); i25 = cl.index("2/5")
data = null.classmin(f["T6"][None, :])[:, 0]
obs = data[i25]; BAR = 16.75
srt = np.sort(data)
print("data: 2/5 min %.10f; next class %s at %.3f" % (obs, cl[int(np.argsort(data)[1])], srt[1]))


def cp(k, n): return beta.ppf(0.975, k + 1, n - k) if k < n else 1.0


def load(lo, hi):
    return np.concatenate([np.load(D / "classmin" / ("classmin_%d.npy" % s)) for s in range(lo, hi + 1)], axis=1)


def report(name, M):
    n = M.shape[1]; s = np.sort(M, axis=0); arg = np.argmin(M, axis=0)
    ev = {
        "2/5 class as low (the sealed cell's first conjunct)": M[i25] <= obs + 1e-9,
        "ANY class as low (class-choosing, specificity only)": s[0] <= obs + 1e-9,
        "CLASS-CHOOSING NULL: some class <= obs AND every other class >= 16.75": (s[0] <= obs + 1e-9) & (s[1] >= BAR),
        "  same, every other class >= the data's runner-up %.1f" % srt[1]: (s[0] <= obs + 1e-9) & (s[1] >= srt[1]),
        "  2/5 chosen: 2/5 <= obs AND every other class >= 16.75": (M[i25] <= obs + 1e-9) & (np.delete(M, i25, 0).min(0) >= BAR),
    }
    print("\n== %s: %d targets" % (name, n))
    for k, e in ev.items():
        h = int(e.sum()); r = cp(h, n)
        print("%-78s hits %4d  frac %.3e  r(97.5%%) %.3e  m*r: 41 -> %.4f, 73 -> %.4f" % (k, h, h / n, r, 41 * r, 73 * r))
    hit = s[0] <= obs + 1e-9
    u, c = np.unique(arg[hit], return_counts=True)
    print("   classes carrying the 'any class' hits:", {cl[a]: int(b) for a, b in zip(u, c)})
    print("   of the any-class hits, runner-up class min: median %.1f, fraction >= 16.75: %.3f" % (np.median(s[1][hit]) if hit.any() else np.nan, np.mean(s[1][hit] >= BAR) if hit.any() else np.nan))
    return ev


if __name__ == "__main__":
    report("validation, sealed seeds 1829-1868 (expect 8 and 67)", load(1829, 1868))
    report("fresh seeds 2001-2040 (160 000)", load(2001, 2040))
    report("fresh seeds 2001-2200 (800 000)", load(2001, 2200))
