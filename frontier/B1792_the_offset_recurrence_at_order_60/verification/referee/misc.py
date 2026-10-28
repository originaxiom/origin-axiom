import pathlib
import pickle, math
from fractions import Fraction as Fr
P = pickle.load(open(str(pathlib.Path(__file__).resolve().parent / "slope25.pkl"), "rb")); rows = P["rows"]; S = P["S"]; T = P["T"]
M = pickle.load(open(str(pathlib.Path(__file__).resolve().parent / "lmin.pkl"), "rb")); lmin = M["lmin"]
strip = sorted({lmin[b][1][:2] for b in lmin if lmin[b][0] < 16.75})
names = ["c/t", "u/t", "s/b", "d/b"]
print("per-ratio |dlog| in reading (St,S), L_max, at the strip apexes: 7/20 -> 1/60 and 7/20 -> 41/60")
for (re, im) in strip:
    r0, r1, r2 = rows[("7/20", re, im)]["L_max"], rows[("1/60", re, im)]["L_max"], rows[("41/60", re, im)]["L_max"]
    q0, q1, q2 = r0["upSt"] + r0["downS"], r1["upSt"] + r1["downS"], r2["upSt"] + r2["downS"]
    print("  Re %.4f: ->1/60 %s | ->41/60 %s | model-target (sigma) 7/20 %s 1/60 %s 41/60 %s" % (re, " ".join("%s %+.2f" % (n, b - a) for n, a, b in zip(names, q0, q1)), " ".join("%+.2f" % (b - a) for a, b in zip(q0, q2)),
          " ".join("%+.1f" % ((a - t) / s) for a, t, s in zip(q0, T, S)), " ".join("%+.1f" % ((a - t) / s) for a, t, s in zip(q1, T, S)), " ".join("%+.1f" % ((a - t) / s) for a, t, s in zip(q2, T, S))))
# mirror: Re -> 1 - Re with b -> 3/5 - b; check row-level equality, and at Re = 0 against the T-shifted partner
apx = sorted({(k[1], k[2]) for k in rows})
res = sorted({a[0] for a in apx}); print("apex Re values not mirror-closed within [0,1):", [r for r in res if round((1 - r) % 1, 9) not in {round(x, 9) for x in res}])
print("Re = 0 apexes:", [a for a in apx if a[0] == 0.0])
def chi(rec):
    best = math.inf
    for h in ("L_max", "L_2"):
        for u, dn, l in (("St", "S", "S"), ("St", "St", "St")):
            m = rec[h]["up" + u] + rec[h]["down" + dn] + rec[h]["lep" + l]
            for k in (0.0, math.log(3)):
                mm = m[:4] + [m[4] + k, m[5] - k]; best = min(best, sum(((mm[i] - T[i]) / S[i]) ** 2 for i in range(6)))
    return best
L60 = sorted({k[0] for k in rows if M["order"][k[0]] == 60}, key=Fr)
worst = 0; worst0 = 0; unp = set()
for b in L60:
    mb = str((Fr(3, 5) - Fr(b)) % 1)
    for (re, im) in apx:
        mre = round((1 - re) % 1, 9)
        if re == 0.0:
            # partner at Re 1 = Re 0 with b' - alpha (T-law)
            mb2 = str((Fr(mb) - Fr(2, 5)) % 1)
            worst0 = max(worst0, abs(chi(rows[(b, re, im)]) - chi(rows[(mb2, 0.0, im)])))
            continue
        if (mb, mre, im) not in rows: unp.add((re, im)); continue
        worst = max(worst, abs(chi(rows[(b, re, im)]) - chi(rows[(mb, mre, im)])))
print("order 60: max |chi(b, Re) - chi(3/5-b, 1-Re)| over non-zero-Re apexes: %.2e; at Re 0 against the T-shifted partner: %.2e" % (worst, worst0))
print("unpaired apexes (Re, Im):", sorted(unp))
cnt = {}
for b in L60:
    bb = min(((chi(rows[(b, re, im)]), (re, im)) for (re, im) in apx))
    cnt[b] = bb
for b in L60: print("  %-6s best %.4f at %s %s" % (b, cnt[b][0], cnt[b][1], "UNPAIRED/Re0" if (cnt[b][1] in unp or cnt[b][1][0] == 0.0) else ""))
# per-line minima without the Re = 0 apexes
for b in ("13/60", "23/60", "43/60", "53/60"):
    m = min(chi(rows[(b, re, im)]) for (re, im) in apx if re != 0.0 and (re, im) not in unp)
    print("  %s min without Re=0 apexes %.4f" % (b, m))
