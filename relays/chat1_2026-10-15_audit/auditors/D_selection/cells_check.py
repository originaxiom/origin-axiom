import json, math
import numpy as np
from scipy.stats import spearmanr
P = "<repo>/relays/chat1_2026-10-14_step3/weights_cells.json"
d = json.load(open(P))
per = d["per thread"]
C = lambda M: np.array([[complex(*z) for z in row] for row in M])
def isqrt(K):
    ev, U = np.linalg.eigh(K); return U @ np.diag(ev ** -0.5) @ U.conj().T, ev
def masses(KL, KR, Y):
    AL, evL = isqrt(KL); AR, evR = isqrt(KR)
    s = np.sort(np.linalg.svd(AL @ Y @ AR.T, compute_uv=False))
    return s, evL, evR
worst = 0
rows = {}
for w, t in per.items():
    rows[w] = {"y": t["y_max"]}
    for cell in ("C1", "C2", "C3"):
        c = t[cell]; m = c["matrices (N = 384)"]
        s, evL, evR = masses(C(m["K_L"]), C(m["K_R"]), C(m["Y"]))
        r = (s[1] / s[2], s[0] / s[2])
        if c["admitted"]:
            worst = max(worst, abs(r[0] - c["m2/m3"]) / c["m2/m3"])
        rows[w][cell] = dict(m23=c["m2/m3"], m13=c["m1/m3"], m12=c["m1/m2"], adm=c["admitted"], re=r)
print("recomputed m2/m3 from stored matrices, worst rel dev on admitted:", worst)
band = lambda x: 0.002 <= x <= 0.07
for cell in ("C1", "C2", "C3"):
    adm = [w for w in rows if rows[w][cell]["adm"]]
    inb = [w for w in adm if band(rows[w][cell]["m23"])]
    print(f"--- {cell}: admitted {len(adm)}, in band {len(inb)}")
    if cell != "C3":
        mb = min(inb, key=lambda w: rows[w][cell]["m12"]); ma = min(adm, key=lambda w: rows[w][cell]["m12"])
        print("  least m1/m2 in band: %.4f on %s (m2/m3 %.4g)" % (rows[mb][cell]["m12"], mb, rows[mb][cell]["m23"]))
        print("  least m1/m2 anywhere: %.4f on %s (m2/m3 %.3g)" % (rows[ma][cell]["m12"], ma, rows[ma][cell]["m23"]))
        print("  max m1/m2 anywhere: %.4f" % max(rows[w][cell]["m12"] for w in adm))
        print("  m1/m2 in band range: %.4f .. %.4f" % (min(rows[w][cell]["m12"] for w in inb), max(rows[w][cell]["m12"] for w in inb)))
    top = sorted(adm, key=lambda w: -rows[w][cell]["m23"])[:6]
    print("  largest m2/m3:", [(w, round(rows[w][cell]["m23"], 4)) for w in top])
    print("  root m2/m3 rank (1 = largest):", 1 + sorted(adm, key=lambda w: -rows[w][cell]["m23"]).index("LR"))
    rho = spearmanr([rows[w]["y"] for w in adm], [math.log(rows[w][cell]["m23"]) for w in adm]).correlation
    print("  Spearman(y, ln m2/m3) = %.4f" % rho)
# C3: the threads below y = 1.75
low = sorted([w for w in rows if rows[w]["C3"]["adm"] and rows[w]["y"] < 1.75], key=lambda w: rows[w]["y"])
print("C3 below y=1.75:", [(w, round(rows[w]["y"], 3), round(rows[w]["C3"]["m23"], 4)) for w in low])
print("C3 max m1/m3 on admitted:", max(rows[w]["C3"]["m13"] for w in rows if rows[w]["C3"]["adm"]))
