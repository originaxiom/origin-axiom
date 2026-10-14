"""Audit checks (inline ones, saved): SnapPy symmetry/census names; the two-ratio curve from lagrange_law.json;
F+ weight minimum; Gueritaud-Futer and max-run bounds on T-ROOT's 31,040 threads. argv: t_root_threads.json lagrange_law.json"""
import json, math, sys, warnings
warnings.filterwarnings("ignore")
import numpy as np
import snappy
thr = json.load(open(sys.argv[1])); ll = json.load(open(sys.argv[2]))
for w in ["LR", "LLR", "LLRR", "LLLR", "LLRLR"]:
    M = snappy.Manifold("b++" + w); G = M.symmetry_group()
    print(w, round(float(M.volume()), 10), [str(x) for x in M.identify()][:1], str(G), G.order(), "amphichiral", G.is_amphicheiral())
r = ll["readouts"]; pt = r["per thread"]; adm = [w for w, q in pt.items() if q["admitted"]]
a2, b2 = r["fit all admitted: ln m2/m3"]; a1, b1 = r["fit all admitted: ln m1/m3"]
sl = b1 / b2; ic = a1 - sl * a2
x = np.array([math.log(pt[w]["m2/m3"]) for w in adm]); y = np.array([math.log(pt[w]["m1/m3"]) for w in adm])
print("curve (height eliminated): intercept %.4f slope %.4f rms %.4f; OLS of y on x: %s" % (ic, sl, np.sqrt(np.mean((y - ic - sl * x) ** 2)), np.polyfit(x, y, 1).round(4)))
for name, (m2, m1) in {"up": (0.0037, 7.3e-6), "lepton": (0.0589, 2.8e-4), "LLRR(LR)^7": (0.0595, 3.1e-3)}.items():
    print("  %s: curve m1/m3 %.3g, factor %.2f" % (name, math.exp(ic + sl * math.log(m2)), math.exp(ic + sl * math.log(m2)) / m1))
k = "heaviest state's weights (F_i, F+, F-)"
print("min F+ weight over admitted:", min((pt[w][k][1], w) for w in adm))
v3, v8 = 1.0149416064096536, 3.663862376708876
def runs(w):
    k = 0
    while w[k] == w[k - 1]: k += 1
    u = w[k:] + w[:k]; rl, cur, n = [], u[0], 0
    for ch in u:
        if ch == cur: n += 1
        else: rl.append(n); cur, n = ch, 1
    rl.append(n); return rl
ratio = [thr[w][0] / (len(runs(w)) // 2) for w in thr]
print("Vol/syllables in [2v3, 2v8):", min(ratio), max(ratio), all(2 * v3 - 1e-9 <= q < 2 * v8 for q in ratio))
