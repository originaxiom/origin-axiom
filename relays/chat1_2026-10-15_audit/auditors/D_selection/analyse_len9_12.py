import json, math
import numpy as np
from scipy.stats import spearmanr
d = json.load(open("<scratch>/audit_D/len9_12.json"))
ll = json.load(open("<repo>/relays/chat1_2026-10-14_selection/lagrange_law.json"))["readouts"]["per thread"]
print("controls (m2/m3, m1/m3) vs lagrange_law.json:")
for w, (a, b) in d["control"].items():
    print("  ", w, a, b, "| rel dev", abs(a - ll[w]["m2/m3"]) / ll[w]["m2/m3"], abs(b - ll[w]["m1/m3"]) / ll[w]["m1/m3"])
rows = d["rows"]
adm = [w for w, r in rows.items() if r["adm"]]
print("words 9..12:", len(rows), " admitted:", len(adm))
res = {w: math.log(rows[w]["m23"]) - (7.1069 - 7.2941 * rows[w]["y"]) for w in adm}
r = np.array(list(res.values()))
print("sealed fit on admitted 9..12: RMS %.3f  mean residual %+.3f  max %+.3f  min %+.3f" % (np.sqrt(np.mean(r**2)), r.mean(), r.max(), r.min()))
for n in range(9, 13):
    rn = np.array([res[w] for w in adm if len(w) == n])
    print("  length %d: n %d  RMS %.3f  mean %+.3f" % (n, len(rn), np.sqrt(np.mean(rn**2)), rn.mean()))
syl = [sum(1 for i in range(len(w)) if w[i] != w[i - 1]) for w in adm]
print("Spearman(residual, syllables) = %.3f" % spearmanr([res[w] for w in adm], syl).correlation)
print("share of admitted with |residual| > 1:", np.mean(np.abs(r) > 1))
band = [w for w in adm if 0.002 <= rows[w]["m23"] <= 0.07]
m12 = {w: rows[w]["m13"] / rows[w]["m23"] for w in adm}
wb = min(band, key=lambda w: m12[w])
print("C1 at lengths 9..12: in band %d; least m1/m2 in band %.4f on %s (m2/m3 %.4f); least anywhere %.4f" % (len(band), m12[wb], wb, rows[wb]["m23"], min(m12.values())))
print("largest m2/m3 at 9..12:", sorted(((round(rows[w]["m23"], 4), w) for w in adm), reverse=True)[:4])
