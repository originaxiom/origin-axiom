import json, math, sys
from collections import Counter
P = "<repo>/relays/chat1_2026-10-14_the_scale/"
th = json.load(open(P + "t_root_fixed_threads.json"))
meta = json.load(open(P + "t_root_fixed.json"))
Ln = {int(k): v for k, v in meta["L_of_n"].items()}
def w(word, scheme):
    n = len(word)
    if scheme == "A": return 2.0 ** -n
    if scheme == "B": return 3.0 ** -n
    if scheme == "C": return 1.0 / (n * (n - 1) * Ln[n])
canon = lambda s: min(s[k:] + s[:k] for k in range(len(s)))
mir = lambda s: s.translate(str.maketrans("LR", "RL"))
rev = lambda s: s[::-1]
def refl_sym(s):
    c = canon(s); return canon(rev(s)) == c or canon(mir(s)) == c
def rev_sym(s):
    return canon(rev(s)) == canon(s)
for c in [0.0, 2.0, 6.0, 24.0]:
    print(f"=== c = {c}")
    for sch in "ABC":
        ws = {k: w(k, sch) * math.exp(-c * v[0] / (6 * math.pi)) for k, v in th.items()}
        Z = sum(ws.values())
        top = sorted(ws.items(), key=lambda kv: -kv[1])[:6]
        rs = sum(v for k, v in ws.items() if refl_sym(k)) / Z
        rvs = sum(v for k, v in ws.items() if rev_sym(k)) / Z
        amph = sum(v for k, v in ws.items() if abs(th[k][1]) < 1e-6) / Z
        print(sch, "root %.4f" % (ws["LR"] / Z), "top:", [(k, round(v / Z, 4)) for k, v in top],
              "| refl-sym %.3f  rev-sym %.3f  amphichiral %.3f" % (rs, rvs, amph))
