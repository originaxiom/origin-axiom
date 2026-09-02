#!/usr/bin/env python3
"""B1240 fast recomputations: R42 (m=12 class counts), R44 (B549 = E7 Perron eigenvector), R43 (Vol(4_1) digits;
B955 surjections by brute force), R50 (the 8-row V4 table with the orientation-aware detector)."""
import json, itertools, math
import numpy as np, mpmath as mp, snappy
out = {}

# ---- R42: reduced indefinite binary quadratic forms of discriminant D = m^2+4, proper (SL2Z) vs full (GL2Z) classes
def reduced_forms(D):
    """Gauss-reduced indefinite forms (a,b,c), b^2-4ac=D, D>0 non-square: |sqrt(D)-2|a|| < b < sqrt(D)."""
    s = math.isqrt(D); assert s*s != D
    forms = []
    for b in range(1, s + 1):
        if (b - D) % 2: continue
        ac = (b*b - D) // 4                      # = a*c < 0
        for a in range(1, s + 1):
            if ac % a: continue
            for aa in (a, -a):
                c = ac // aa
                if abs(math.sqrt(D) - 2*abs(aa)) < b < math.sqrt(D) and math.gcd(math.gcd(abs(aa), b), abs(c)) == 1:
                    forms.append((aa, b, c))          # PRIMITIVE forms only (first draft counted 2*(disc 37) at D=148)
    return sorted(set(forms))
def rho(f):
    """right neighbour: (a,b,c) -> (c, b', a') with b' = -b mod 2c in the reduced window."""
    a, b, c = f; D = b*b - 4*a*c; s = math.sqrt(D)
    # choose b' ≡ -b (mod 2|c|) with sqrt(D)-2|c| < b' < sqrt(D)
    m = 2*abs(c); b2 = (-b) % m
    while b2 < s - m: b2 += m
    while b2 > s: b2 -= m
    a2 = (b2*b2 - D) // (4*c)
    return (c, b2, a2)
def classes(D, gl=False):
    forms = reduced_forms(D); seen = set(); cyc = []
    for f in forms:
        if f in seen: continue
        cycle = []; g = f
        while g not in seen:
            seen.add(g); cycle.append(g); g = rho(g)
        cyc.append(frozenset(cycle))
    if not gl: return len(cyc)
    # improper equivalence: (a,b,c) ~ (a,-b,c) ~ (c,b,a) (reflection); merge cycles meeting under (a,b,c)->(c,b,a)
    key = {c: i for i, cy in enumerate(cyc) for c in cy}
    parent = list(range(len(cyc)))
    def find(i):
        while parent[i] != i: i = parent[i]
        return i
    for cy in cyc:
        for (a, b, c) in cy:
            g = (c, b, a)
            if g in key: parent[find(key[g])] = find(key[(a, b, c)])
    return len({find(i) for i in range(len(cyc))})
r42 = {m: {"D": m*m+4, "SL": classes(m*m+4), "GL": classes(m*m+4, gl=True)} for m in range(1, 13)}
print("R42 class counts (own enumeration):", {m: (v["SL"], v["GL"]) for m, v in r42.items()})
# PARI cross-check via snappy's pari
from snappy import pari
r42_pari = {m: int(pari(f"qfbclassno({m*m+4})")) for m in range(1, 13)}
print("R42 PARI qfbclassno (narrow/proper):", r42_pari)
out["R42"] = {"own": r42, "pari_proper": r42_pari}

# ---- R44: B549's seven numbers = Perron eigenvector of the E7 Dynkin adjacency matrix
E7 = np.zeros((7, 7)); edges = [(0,1),(1,2),(2,3),(3,4),(4,5),(2,6)]   # Bourbaki: 1-3-4-5-6-7 chain with 2 attached to 4; relabel
# Use the standard E7 diagram: chain 1-2-3-4-5-6 with node 7 attached to node 3
E7 = np.zeros((7, 7))
for i, j in [(0,1),(1,2),(2,3),(3,4),(4,5),(2,6)]: E7[i,j] = E7[j,i] = 1
w, V = np.linalg.eigh(E7); v = V[:, np.argmax(w)]; v = np.abs(v) / np.abs(v).min()
b549 = [1, 1.285575, 1.879385, 1.969616, 2.532089, 2.879385, 3.701666]
print("R44 E7 Perron eigenvector /min:", sorted(np.round(v, 6)), " banked B549:", b549, " Perron root:", round(w.max(), 6))
out["R44"] = {"perron_vector_sorted": [float(x) for x in sorted(v)], "b549": b549, "match": bool(np.allclose(sorted(v), b549, atol=2e-6))}

# ---- R43: Vol(4_1) digits
mp.mp.dps = 40
L = lambda t: -mp.quad(lambda u: mp.log(abs(2*mp.sin(u))), [0, t])
vol = 6*L(mp.pi/3); print("R43 Vol(4_1) = 6*Lambda(pi/3) =", mp.nstr(vol, 35))
out["R43_vol41_35dps"] = mp.nstr(vol, 35)
# B955: pi_1(m004) -> A4, D5, S5 surjections by brute force over S_n pairs
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import SymmetricGroup, AlternatingGroup, DihedralGroup
G = snappy.Manifold("4_1").fundamental_group(); gens = G.generators(); rels = G.relators()
print("R43 pi_1(m004):", gens, rels)
def word_to_perm(word, imgs):
    p = Permutation(list(range(imgs[0].size)))
    for ch in word:
        g = imgs[ord(ch.lower()) - 97]
        p = p * (g if ch.islower() else ~g)
    return p
def surjects(target, n):
    Sn = list(SymmetricGroup(n).generate()); found = 0
    for a in Sn:
        for b in Sn:
            if all(word_to_perm(r, [a, b]).is_Identity for r in rels):
                H = PermutationGroup([a, b])
                if H.order() == target.order() and H.is_subgroup(target) and target.is_subgroup(H): return True
    return False
out["B955"] = {"A4": surjects(AlternatingGroup(4), 4), "D5": surjects(DihedralGroup(5), 5), "S5": surjects(SymmetricGroup(5), 5)}
print("R43 B955 surjections (brute force over S_n^2):", out["B955"])

# ---- R50: the V4 table with the orientation-aware detector
rows = {}
for name in ["m004", "m003", "m025", "b++RRLL", "m009", "m010", "b++RRL", "b++RLL"]:
    M = snappy.Manifold(name); sg = M.symmetry_group()
    rows[name] = {"vol": round(float(M.volume()), 6), "sym_order": sg.order(), "amphicheiral": bool(sg.is_amphicheiral())}
print("R50 V4 table:", rows)
out["R50"] = rows
json.dump(out, open(__file__.replace(".py", ".json"), "w"), indent=1, default=str)

# ---- verdict: every recomputed fact against its pre-registered expectation
checks = {
    "R42 own SL == PARI for all m<=11": all(out["R42"]["own"][m]["SL"] == out["R42"]["pari_proper"][m] for m in range(1, 12)),
    "R42 m=12: own (SL,GL)=(3,2), PARI 3": (out["R42"]["own"][12]["SL"], out["R42"]["own"][12]["GL"], out["R42"]["pari_proper"][12]) == (3, 2, 3),
    "R43 Vol(4_1) 35 dps prefix": out["R43_vol41_35dps"].startswith("2.02988321281930725004240510854904"),
    "R44 B549 seven numbers == E7 adjacency Perron vector": out["R44"]["match"] is True,
    "B955 surjections all True": all(out["B955"].values()),
    "R50 four amphicheiral of eight": sorted(k for k, v in out["R50"].items() if v["amphicheiral"]) == sorted(["m004", "m003", "m025", "b++RRLL"]),
}
for k, v in checks.items(): print(("  OK   " if v else "  FAIL ") + k)
print("REPRODUCES" if all(checks.values()) else "DIFF")
