import json, math, sys
import numpy as np
from mpmath import mp, mpf, sqrt
from scipy.stats import spearmanr
mp.dps = 50
S = sys.argv[1]
C = f"{S}/committed/chat1_2026-10-14_selection"
ll = json.load(open(f"{C}/lagrange_law.json"))
rows = ll["readouts"]["per thread"]
thr = json.load(open(f"{S}/relays/chat1_2026-10-14_the_scale/t_root_threads.json"))
def runs(w):
    # cyclic run lengths starting at a letter change
    n = len(w); k = next(i for i in range(n) if w[i] != w[i-1])
    v = w[k:] + w[:k]; out = []; c = 1
    for i in range(1, n):
        if v[i] == v[i-1]: c += 1
        else: out.append(c); c = 1
    out.append(c); return out
def cf(seq):  # [a0; a1, a2, ...] for a long finite list
    x = mpf(seq[-1])
    for a in reversed(seq[:-1]): x = a + 1/x
    return x
def lagrange(w):
    a = runs(w); m = len(a); best = mpf(0)
    for i in range(m):
        fwd = [a[(i + j) % m] for j in range(400)]
        bwd = [a[(i - 1 - j) % m] for j in range(400)]
        val = cf(fwd) + 1/cf(bwd)
        best = max(best, val)
    return best
worst = 0; worst_w = None; below = 0
for w, r in rows.items():
    Lv = lagrange(w); yt = float(Lv/2)
    d = yt - r["y_max"]
    if d < -1e-12: below += 1
    if abs(d) > worst: worst, worst_w = abs(d), w
print("max |exact L/2 - sampled y_max| over 69 words:", worst, worst_w, " cases sampled > exact:", below)
adm = [w for w in rows if rows[w]["admitted"]]
print("admitted:", len(adm), "excluded:", sorted(set(rows) - set(adm)))
print("max |L/2 - y| over admitted:", max(abs(float(lagrange(w)/2) - rows[w]["y_max"]) for w in adm))
# heaviest weights
hv = min(rows[w]["heaviest state's weights (F_i, F+, F-)"][1] for w in adm)
hv_all = min(rows[w]["heaviest state's weights (F_i, F+, F-)"][1] for w in rows)
print("min heaviest-state F+ weight: admitted %.6f, all %.6f" % (hv, hv_all))
new = [w for w in adm if len(w) >= 6]
print("new admitted", len(new), "distinct m2/m3 values (rel 1e-6):", len({round(math.log(rows[w]['m2/m3']), 5) for w in new}))
high = [w for w in adm if rows[w]["y_max"] > 2]
print("n high (y>2)", len(high), "max m2/m3 among them", max(rows[w]["m2/m3"] for w in high))
low = [w for w in adm if rows[w]["y_max"] < 1.5]
print("Markov (y<1.5):", sorted((rows[w]["m2/m3"], w) for w in low))
# refit with exact Lagrange/2 instead of sampled y
y = np.array([rows[w]["y_max"] for w in adm]); ye = np.array([float(lagrange(w)/2) for w in adm]); l2 = np.log([rows[w]["m2/m3"] for w in adm])
A = np.vstack([np.ones_like(y), y]).T; Ae = np.vstack([np.ones_like(ye), ye]).T
print("fit sampled:", np.linalg.lstsq(A, l2, rcond=None)[0], " fit exact:", np.linalg.lstsq(Ae, l2, rcond=None)[0])
yn = np.array([rows[w]["y_max"] for w in new]); yne = np.array([float(lagrange(w)/2) for w in new]); l2n = np.log([rows[w]["m2/m3"] for w in new])
print("LL2 RMS sampled %.4f exact %.4f" % (np.sqrt(np.mean((l2n - (7.1069 - 7.2941*yn))**2)), np.sqrt(np.mean((l2n - (7.1069 - 7.2941*yne))**2))))
print("Spearman sampled %.4f exact %.4f" % (spearmanr(y, l2).correlation, spearmanr(ye, l2).correlation))
# markov table check: CS values
for w in ["LLRLLRR","LLRRLRR","LLRLRLR","LRLRLRR","LLRLLRLR","LRLRRLRR","LLRRLR","LLRLRR","LLRRLRLR","LLRLRLRR","LLRLRRLR"]:
    print(w, "L=%.4f" % float(lagrange(w)), "y=%.5f" % rows[w]["y_max"], "Vol %.4f CS %+.4f" % tuple(thr[w]), "m2/m3 %.4g m1/m3 %.3g" % (rows[w]["m2/m3"], rows[w]["m1/m3"]))
ro = ll["readouts"]
print("residual corr", ro["residual correlations (Spearman)"])
print("fits", ro["fit all admitted: ln m2/m3"], ro["fit all admitted: ln m1/m3"], ro["RMS of the all-admitted fit (m2/m3)"])
print("LLRLRLR residual vs all-admitted fit: %.3f ; vs sealed fit: %.3f" % (math.log(rows['LLRLRLR']['m2/m3']) - (ro['fit all admitted: ln m2/m3'][0] + ro['fit all admitted: ln m2/m3'][1]*rows['LLRLRLR']['y_max']), math.log(rows['LLRLRLR']['m2/m3']) - (7.1069 - 7.2941*rows['LLRLRLR']['y_max'])))
c = ro['fit all admitted: ln m2/m3']
res = {w: math.log(rows[w]['m2/m3']) - (c[0] + c[1]*rows[w]['y_max']) for w in adm}
print("largest residuals (all-admitted fit):", sorted(res.items(), key=lambda kv: -abs(kv[1]))[:6])
res_s = {w: math.log(rows[w]['m2/m3']) - (7.1069 - 7.2941*rows[w]['y_max']) for w in new}
print("largest residuals (sealed fit, new):", sorted(res_s.items(), key=lambda kv: -abs(kv[1]))[:6])
print("span e-folds", math.log(max(rows[w]['m2/m3'] for w in adm)/min(rows[w]['m2/m3'] for w in adm)))
# data mapped through all-admitted fit
for nm, val in (("up", 0.0036847735647212647), ("down", 0.018724903134906656), ("lepton", 0.05887328180682186)):
    yy = (math.log(val) - c[0])/c[1]; print(nm, "y %.4f Lagrange %.4f" % (yy, 2*yy))
