import json, math, statistics, itertools
import numpy as np
from scipy.stats import spearmanr

D = "<repo>/relays/chat1_2026-10-14_step3/"
p = json.load(open(D + "post_hoc_completions.json"))["per thread"]
s = json.load(open(D + "weights_cells.json"))["per thread"]
words = list(p)
adm = [w for w in words if s[w]["C2"]["admitted"]]

# --- the control's median, several definitions
pairs_adm, pairs_all, thr_adm, thr_all = [], [], [], []
for w in words:
    d = []
    for cell, ks in (("C2", ("m2/m3", "m1/m3")), ("C3", ("m2/m3",))):
        for k in ks:
            d.append(abs(p[w][f"H-ORTH {cell}"][k] - s[w][cell][k]) / abs(s[w][cell][k]))
    (pairs_adm if w in adm else []).extend(d); pairs_all.extend(d)
    (thr_adm if w in adm else []).append(max(d)); thr_all.append(max(d))
print("median: per-thread worst, admitted %.2e | all threads %.2e | (thread, quantity) admitted %.2e | all %.2e" % (
    statistics.median(thr_adm), statistics.median(thr_all), statistics.median(pairs_adm), statistics.median(pairs_all)))
# with C3 m1/m3 too (rank-2 noise) -- not meaningful but check
# --- C1 root and AUDIT row 2
r = s["LR"]["C1"]; print("C1 root", r["m2/m3"], r["m1/m3"], r["m1/m2"])

# --- H-E4 C3 against height
k = "H-E4 C3"
rows = sorted((p[w]["y_max"], p[w][k]["m2/m3"], w, w in adm) for w in words)
print("H-E4 C3 m2/m3 by height (all 69; * = unadmitted):")
seen = set()
for y, v, w, a in rows:
    key = (round(y, 3), round(v, 4))
    if key in seen: continue
    seen.add(key)
    print("   y %.3f  %.4f  %s%s" % (y, v, w, "" if a else " *"))
rho_noroot = spearmanr([p[w]["y_max"] for w in adm if w != "LR"], [math.log(p[w][k]["m2/m3"]) for w in adm if w != "LR"]).correlation
print("Spearman H-E4 C3 admitted without the root: %.3f" % rho_noroot)
for kk in ("H-ORTH C3", "H-E4 C2", "H-ORTH C2"):
    print("Spearman", kk, "without root %.3f" % spearmanr([p[w]["y_max"] for w in adm if w != "LR"],
                                                       [math.log(p[w][kk]["m2/m3"]) for w in adm if w != "LR"]).correlation)

# --- the data and pulls
hz = json.loads(open("<scratch>/referee2/pc_review/hz.json").read())["masses_GeV"]
V, S = hz["value"], hz["sigma"]
def ratio(a, b):
    x = V[a] / V[b]; return x, x * math.hypot(S[a] / V[a], S[b] / V[b])
secs = {"up m2/m3": ratio("c", "t"), "down m2/m3": ratio("s", "b"), "lepton m2/m3": ratio("mu", "tau"),
        "up m1/m2": ratio("u", "c"), "down m1/m2": ratio("d", "s"), "lepton m1/m2": ratio("e", "mu"),
        "up m1/m3": ratio("u", "t"), "down m1/m3": ratio("d", "b"), "lepton m1/m3": ratio("e", "tau")}
for kq, (x, sg) in secs.items():
    print("  %-13s %.5g +- %.2g  (rel %.3f, log-width of the 1-sigma window %.4f)" % (kq, x, sg, sg / x, math.log((x + sg) / (x - sg))))
x, sg = secs["down m2/m3"]
for name, v in (("H-E4", p["LR"]["H-E4 C3"]["m2/m3"]), ("H-ORTH", p["LR"]["H-ORTH C3"]["m2/m3"])):
    print("  pull", name, "%.3f sigma" % ((v - x) / sg))

# --- base rate: analytic, log-uniform prior on [a, 1], m2/m3 windows only
W23 = sum(math.log((x + sg) / (x - sg)) for kq, (x, sg) in secs.items() if kq.endswith("m2/m3"))
print("total log-width of the three m2/m3 windows: %.4f" % W23)
for a in (1e-2, 1e-3, 1e-4):
    pv = W23 / math.log(1 / a)
    print("  log-uniform on [%.0e, 1]: per value %.3f; 5 values %.3f; 4 values %.3f" % (a, pv, 1 - (1 - pv) ** 5, 1 - (1 - pv) ** 4))
# with all ratios of the rank-3 roots too (C1 root, C2 H-ORTH root: m1/m2, m1/m3 as two extra looks each)
W12 = sum(math.log((x + sg) / (x - sg)) for kq, (x, sg) in secs.items() if kq.endswith("m1/m2"))
W13 = sum(math.log((x + sg) / (x - sg)) for kq, (x, sg) in secs.items() if kq.endswith("m1/m3"))
for a in (1e-3, 1e-4):
    L = math.log(1 / a); L13 = math.log(1 / (a * 1e-2))
    miss = (1 - W23 / L) ** 5 * (1 - W12 / L) ** 2 * (1 - W13 / L13) ** 2
    print("  all nine looks (5 m2/m3, 2 m1/m2, 2 m1/m3), prior [%.0e,1] (m1/m3 two decades lower): %.3f" % (a, 1 - miss))

# --- base rate: empirical, the instrument's own admitted m2/m3 values as the prior for a value
vals = []
for w in adm:
    vals.append(s[w]["C1"]["m2/m3"])
    for kk in ("H-ORTH C2", "H-ORTH C3", "H-E4 C2", "H-E4 C3"):
        vals.append(p[w][kk]["m2/m3"])
vals = np.array(vals)
hit = np.zeros(len(vals), bool)
for kq, (x, sg) in secs.items():
    if kq.endswith("m2/m3"):
        hit |= (np.abs(vals - x) <= sg)
pe = hit.mean()
print("empirical per-value hit rate over %d admitted (thread, cell, completion) m2/m3 values: %.3f; five values: %.3f" % (
    len(vals), pe, 1 - (1 - pe) ** 5))
for kk, src in (("C1", "s"), ("H-ORTH C2", "p"), ("H-ORTH C3", "p"), ("H-E4 C2", "p"), ("H-E4 C3", "p")):
    vv = np.array([(s[w]["C1"] if src == "s" else p[w][kk])["m2/m3"] for w in adm])
    hh = np.zeros(len(vv), bool)
    for kq, (x, sg) in secs.items():
        if kq.endswith("m2/m3"):
            hh |= (np.abs(vv - x) <= sg)
    print("   per cell %-10s hit rate %.3f  (range %.4f..%.4f)" % (kk, hh.mean(), vv.min(), vv.max()))
