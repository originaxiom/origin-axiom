import json, math
P = "<repo>/relays/"
th = json.load(open(P + "chat1_2026-10-14_the_scale/t_root_fixed_threads.json"))
print("vol(L^n R):", [(n, round(th["L" * n + "R"][0], 4)) for n in range(1, 18)])
print("max over L^n R:", max(th["L" * n + "R"][0] for n in range(1, 18)), " LLRR:", th["LLRR"][0])
ll = json.load(open(P + "chat1_2026-10-14_selection/lagrange_law.json"))["readouts"]["per thread"]
k0 = next(iter(ll)); print("lagrange_law per-thread keys:", list(ll[k0].keys()))
adm = [w for w, r in ll.items() if r["admitted"]]
key = [k for k in ll[k0] if "weights" in k]
if key:
    k = key[0]
    print("min heaviest-state weight on F+ over admitted:", min(ll[w][k][1] for w in adm))
# band weights at c = 6 using the 59 admitted C1 values (lengths <= 8), rest 'uncomputed'
meta = json.load(open(P + "chat1_2026-10-14_the_scale/t_root_fixed.json"))
Ln = {int(a): b for a, b in meta["L_of_n"].items()}
canon = lambda s: min(s[i:] + s[:i] for i in range(len(s)))
def wt(word, s):
    n = len(word)
    return {"A": 2.0 ** -n, "B": 3.0 ** -n, "C": 1.0 / (n * (n - 1) * Ln[n])}[s]
for c in (6.0, 24.0):
    for s in "ABC":
        ws = {k: wt(k, s) * math.exp(-c * v[0] / (6 * math.pi)) for k, v in th.items()}
        Z = sum(ws.values())
        root = ws["LR"] / Z
        inband = sum(ws[w] for w in adm if 3e-3 < ll[w]["m2/m3"] < 0.06 and w in ws) / Z
        steeper = sum(ws[w] for w in adm if ll[w]["m2/m3"] <= 3e-3 and w in ws) / Z
        milder = sum(ws[w] for w in adm if ll[w]["m2/m3"] >= 0.06 and w != "LR" and w in ws) / Z
        notadm = sum(ws[w] for w in ll if not ll[w]["admitted"] and w in ws) / Z
        longer = sum(v for k, v in ws.items() if len(k) > 8) / Z
        print(f"c={c} {s}: root {root:.3f}  C1-band(3e-3..0.06) {inband:.3f}  steeper {steeper:.3f}  other milder {milder:.3f}  len<=8 not admitted {notadm:.3f}  length>8 {longer:.3f}")
