import json, math, sys
import numpy as np
from scipy.stats import spearmanr
S = sys.argv[1]
d = json.load(open(f"{S}/committed/chat1_2026-10-14_selection/thread_frame.json"))
per = d["readouts"]["per thread"]
print("keys:", list(d.keys()))
print("Q0", d["Q0"])
print("cells", d["cells"])
# per-thread table
for w, r in sorted(per.items(), key=lambda kv: kv[1]["y_max"]):
    K = np.array([[complex(*z) for z in row] for row in r["K"]]); Y = np.array([[complex(*z) for z in row] for row in r["Y"]])
    ev = r["K eigenvalues"]; cond = ev[2]/ev[0]
    wts = r["weights on (F_i, F+, F-) per state (light to heavy)"]
    print(f"{w:6s} rot {r['rotation']:6s} tr {r['trace']:3d} P {r['period']:.4f} y {r['y_max']:.6f} m2/m3 {r['m2/m3']:.6e} m1/m3 {r['m1/m3']:.6e} m1/m2 {r['m1/m2']:.4f} condK {cond:.3e} ImK/max {np.max(np.abs(K.imag))/np.max(np.abs(K)):.1e} ImY/max {np.max(np.abs(Y.imag))/np.max(np.abs(Y)):.1e} heavy F+ {wts[2][1]:.6f} light F+ {wts[0][1]:.2e} Kh {r['Kh']:.4e}")
# mirror pairs
mir = lambda w: w.translate(str.maketrans("LR", "RL")); canon = lambda w: min(w[k:] + w[:k] for k in range(len(w)))
for w in per:
    m = canon(mir(w))
    if m != w and w < m:
        print("mirror", w, m, "rel diff m2/m3 %.2e m1/m3 %.2e" % (abs(per[w]["m2/m3"]-per[m]["m2/m3"])/per[w]["m2/m3"], abs(per[w]["m1/m3"]-per[m]["m1/m3"])/per[w]["m1/m3"]))
words = list(per)
y = np.array([per[w]["y_max"] for w in words]); l2 = np.log([per[w]["m2/m3"] for w in words]); l1 = np.log([per[w]["m1/m3"] for w in words])
A = np.vstack([np.ones_like(y), y]).T
c2 = np.linalg.lstsq(A, l2, rcond=None)[0]; c1 = np.linalg.lstsq(A, l1, rcond=None)[0]
print("12-thread fit ln m2/m3:", c2, "rms", np.sqrt(np.mean((l2 - A@c2)**2)))
print("12-thread fit ln m1/m3:", c1, "rms", np.sqrt(np.mean((l1 - A@c1)**2)))
print("Spearman(y, ln m1/m3)", spearmanr(y, l1).correlation, " Spearman(y, ln m2/m3)", spearmanr(y, l2).correlation)
# adjacent slopes on distinct heights
hs = {}
for w in words: hs.setdefault(round(per[w]["y_max"], 3), []).append(w)
ks = sorted(hs)
for i in range(len(ks)-1):
    a, b = hs[ks[i]][0], hs[ks[i+1]][0]
    s2 = -(math.log(per[b]["m2/m3"]) - math.log(per[a]["m2/m3"]))/(per[b]["y_max"]-per[a]["y_max"])
    s1 = -(math.log(per[b]["m1/m3"]) - math.log(per[a]["m1/m3"]))/(per[b]["y_max"]-per[a]["y_max"])
    print(f"adjacent {a}->{b}: slope m2/m3 {s2:.2f}  m1/m3 {s1:.2f}")
# all pairs slopes
sl2=[];sl1=[]
for i,a in enumerate(words):
    for b in words[i+1:]:
        dy = per[b]["y_max"]-per[a]["y_max"]
        if abs(dy) > 1e-3:
            sl2.append(-(math.log(per[b]["m2/m3"])-math.log(per[a]["m2/m3"]))/dy); sl1.append(-(math.log(per[b]["m1/m3"])-math.log(per[a]["m1/m3"]))/dy)
print("all-pair slopes m2/m3: min %.2f max %.2f ; m1/m3 min %.2f max %.2f" % (min(sl2), max(sl2), min(sl1), max(sl1)))
print("TF1", d["TF1"]); print("TF2", d["TF2"]); print("TF3", d["TF3"]); print("TF4", d["TF4"]["worst relative difference"]); print("TF5", d["TF5"])
ro = d["readouts"]
print("H-end", ro["H-end control (W73's 0.01938, 3.87e-4)"])
hy = ro["hybrid: W72's Y with the root's K"]; print("hybrid", hy["m2/m3"], hy["m1/m3"], hy["m"])
print("data", ro["data"]); print("data line", ro["data line (root vs HZ2021 at M_Z)"])
print("seconds", ro["seconds"])
