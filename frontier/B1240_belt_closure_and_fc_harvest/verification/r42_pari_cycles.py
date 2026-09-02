"""R42 recheck at m=12 (D=148): reduced primitive forms and their rho-cycles, rho taken from PARI (qfbred flag 1)."""
import math, os, json
from snappy import pari
def reduced_forms(D):
    s = math.isqrt(D); forms = []
    for b in range(1, s + 1):
        if (b - D) % 2: continue
        ac = (b*b - D) // 4
        for a in range(1, s + 1):
            if ac % a: continue
            for aa in (a, -a):
                c = ac // aa
                if abs(math.sqrt(D) - 2*abs(aa)) < b < math.sqrt(D) and math.gcd(math.gcd(abs(aa), b), abs(c)) == 1:
                    forms.append((aa, b, c))
    return sorted(set(forms))
def pari_rho(f):
    q = pari(f"qfbred(Qfb({f[0]},{f[1]},{f[2]}),1)")
    return tuple(int(x) for x in (q[0], q[1], q[2]))
res = {}
for m in range(1, 13):
    D = m*m + 4; forms = reduced_forms(D); seen = set(); cycles = []
    for f in forms:
        if f in seen: continue
        cyc = []; g = f
        while g not in seen:
            seen.add(g); cyc.append(g); g = pari_rho(g)
            if g not in forms and g not in seen:   # PARI's rho left my reduced set: my reduced set is incomplete/wrong
                cyc.append(("LEFT-SET", g)); break
        cycles.append(cyc)
    # GL2 merge: (a,b,c) ~ (c,b,a) (improper); merge cycles that meet under it
    idx = {}
    for i, cy in enumerate(cycles):
        for g in cy:
            if isinstance(g[0], int): idx[g] = i
    parent = list(range(len(cycles)))
    def find(i):
        while parent[i] != i: i = parent[i]
        return i
    for cy in cycles:
        for g in cy:
            if isinstance(g[0], int) and (g[2], g[1], g[0]) in idx:
                parent[find(idx[g])] = find(idx[(g[2], g[1], g[0])])
    gl = len({find(i) for i in range(len(cycles))})
    h = int(pari(f"qfbclassno({D})"))
    res[m] = {"D": D, "n_reduced": len(forms), "SL_cycles": len(cycles), "GL": gl, "pari_qfbclassno": h,
              "left_set": any(isinstance(g[0], str) for cy in cycles for g in cy)}
    print(m, res[m])
    if m == 12:
        for cy in cycles: print("   cycle:", cy)
json.dump(res, open(__file__.replace(".py", ".json"), "w"), indent=1)
ok = all(r["SL_cycles"] == r["pari_qfbclassno"] and not r["left_set"] for r in res.values()) and \
     (res[12]["n_reduced"], res[12]["SL_cycles"], res[12]["GL"]) == (14, 3, 2)
print("REPRODUCES" if ok else "DIFF")
