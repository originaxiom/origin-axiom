"""Referee re-implementation of B1741's chi2_six (seat menu) from its stated definitions, no import of B1741's code."""
import json, math, sys
from fractions import Fraction as Fr
R = str(next(q for q in __import__("pathlib").Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())) + "/"
CEN = R + "frontier/B1792_the_offset_recurrence_at_order_60/verification/census.jsonl"
d = json.load(open(R + "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"))["masses_GeV"]
v, e = d["value"], d["sigma"]
pr = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
T = [math.log(v[a] / v[b]) for a, b in pr]
S = [math.sqrt((e[a] / v[a]) ** 2 + (e[b] / v[b]) ** 2 + 0.01) for a, b in pr]
SEAT = [("St", "S", "S"), ("St", "St", "St")]
L3 = math.log(3)
def chi_parts(r, h, cfg, c):
    u, dn, l = cfg
    m = [math.log(max(x, 1e-300)) for x in r[f"up|{h}|{u}"] + r[f"down|{h}|{dn}"] + r[f"lep|{h}|{l}"]]
    k = L3 if c == 3 else 0.0
    m[4] += k; m[5] -= k
    return [((m[i] - T[i]) / S[i]) ** 2 for i in range(6)], m
rows = [json.loads(l) for l in open(CEN) if l.strip()]
best = {}
allrows = []
for r in rows:
    for h in ("L_max", "L_2"):
        for cfg in SEAT:
            for c in (1, 3):
                p, m = chi_parts(r, h, cfg, c); x = sum(p)
                rec = (x, r["b"], r["apex"], r["Re_tau"], r["Im_tau"], h, cfg, c, p, m)
                allrows.append(rec)
                if r["b"] not in best or x < best[r["b"]][0]: best[r["b"]] = rec
import pickle
pickle.dump(allrows, open(str(__import__("pathlib").Path(__file__).resolve().parent) + "/allrows.pkl", "wb"))
cmp = json.load(open(R + "frontier/B1792_the_offset_recurrence_at_order_60/verification/comparison.json"))["readout_per_line"]
mine = {v_["b"]: v_["chi2_six_seat"] for v_ in cmp.values()}
PRED = {"1/60", "7/60", "29/60", "7/12", "41/60", "47/60", "49/60", "11/12"}
print("T", [round(t, 4) for t in T]); print("S", [round(s, 4) for s in S])
for b in sorted(best, key=lambda s: Fr(s)):
    x = best[b]
    print("%-6s %s mine %.6f theirs %.6f diff %.1e | apex %3d Re %.4f Im %.4f %s %s c=%d parts %s" % (b, "P" if b in PRED else " ", x[0], mine[b], abs(x[0] - mine[b]), x[2], x[3], x[4], x[5], "/".join(x[6]), x[7], [round(q, 2) for q in x[8]]))
