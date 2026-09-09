"""THE TABLE (PREREG §3-4): I(C; Sym^2(rho_geo|K) (x) psi) for the 16 family characters, exact over Q(zeta_12), plus controls."""
import os, sys, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import d2lib as L
from d2lib import K, OMEGA, I_, ONE

A = L.mat([[1 - OMEGA, 1], [-1, 0]]); B = L.mat([[0, -1], [1, OMEGA * (-2)]])
cp = json.load(open("cover_presentation.json"))
gens = cp["gens"]; rels = [[tuple(x) for x in R] for R in cp["rels"]]
mC = [tuple(x) for x in cp["mC"]]; lC = [tuple(x) for x in cp["lC"]]
pres = L.Presentation(gens, rels)
torus = L.Presentation(["m", "l"], [[("m", 1), ("l", 1), ("m", -1), ("l", -1)]])
inv, cls, V, D, keep = L.h1_coordinates(gens, rels)
print("H1(C) =", inv, " classes:", {g: cls([(g, 1)]) for g in gens}, " [m_C] =", cls(mC), " [l_C] =", cls(lC))
assert cls(mC) == (0, 0, 1) and cls(lC) == (0, 0, 0)

def rho_gen(g, Bl):
    if g == "z": return L.mmul(L.mmul(Bl, Bl), Bl)
    j = int(g[1:]); M = A; Bi = L.inv2(Bl)
    for _ in range(j): M = L.mmul(L.mmul(Bl, M), Bi)
    return M
def character(pq, zval):
    p, q = pq; out = {}
    for g in gens:
        c1, c2, c3 = cls([(g, 1)]); val = ONE
        for _ in range((p * c1 + q * c2) % 4): val = val * I_
        for _ in range(abs(c3)): val = val * (zval if c3 > 0 else zval.inv())
        out[g] = val
    return out
def is_char(chi):
    for R in rels:
        v = ONE
        for g, e in R: v = v * (chi[g] if e == 1 else chi[g].inv())
        if v != ONE: return False
    return True
def float_ranks(mats):
    Vr = L.Rep(mats); d0, d1 = L.cochain_maps(pres, Vr)
    return (np.linalg.matrix_rank(np.array(L.to_cx(d0)), tol=1e-9), np.linalg.matrix_rank(np.array(L.to_cx(d1)), tol=1e-9))
def sector(k, pq, zval=ONE, Bl=B):
    chi = character(pq, zval); assert is_char(chi), ("not a character", pq)
    mats = {g: L.mscale(L.sym_power(rho_gen(g, Bl), k), chi[g]) for g in gens}
    d = L.index_data(pres, mats, [mC, lC], torus); v, w = d["V"], d["Vstar"]
    n = k + 1; rd0 = n - v["a0"]; rd1 = n * len(gens) - (v["a1"] + rd0)
    fr = float_ranks(mats)
    return dict(k=k, pq=pq, a=(v["a0"], v["a1"], v["a2"]), astar=(w["a0"], w["a1"], w["a2"]), t=(v["t0"], v["t1"], v["t2"]),
                r1=v["r1"], r1s=w["r1"], I=d["I"], F=d["F"], Cc=d["Cc"], ids=all(d["checks"].values()), float_ok=(fr == (rd0, rd1)))

rows = []
print("\n== THE TABLE: Sym^2(rho_geo|K) (x) psi,  psi(z) = 1,  psi|Tors = i^(p c1 + q c2) ==")
print(" (p,q) | a=(a0,a1,a2)  a*        t=(t0,t1,t2) | r1 r1* |  I  F  Cc | identities float")
for p in range(4):
    for q in range(4):
        s = sector(2, (p, q)); rows.append(s)
        print(f" ({p},{q}) | a={s['a']} a*={s['astar']} t={s['t']} | {s['r1']}  {s['r1s']}  | {s['I']:+d} {s['F']:+d} {s['Cc']:+d} | {s['ids']} {s['float_ok']}")
nz = [s for s in rows if s["I"] != 0]
print("nonzero indices among the 16:", len(nz), "  all identities:", all(s["ids"] for s in rows), "  all float ranks agree:", all(s["float_ok"] for s in rows))
same = all(sector(2, s["pq"], Bl=L.mneg(B))["I"] == s["I"] for s in rows)
print("lift independence (Sym^2 with the other lift -B gives the same table):", same)

print("\n== controls ==")
print(" k=0 (characters alone):")
k0 = {}
for p in range(4):
    for q in range(4):
        s = sector(0, (p, q)); k0[(p, q)] = (s["a"], s["t"], s["r1"], s["I"], s["F"], s["ids"], s["float_ok"])
print("  psi = 1      :", k0[(0, 0)]); print("  psi != 1 set :", sorted(set(v for k, v in k0.items() if k != (0, 0))))
print(" k=1 (rho_geo (x) psi; both lifts; expect t0 = 0 => I = 0):")
for Bl, name in ((B, "+B"), (L.mneg(B), "-B")):
    out = set()
    for p in range(4):
        for q in range(4):
            s = sector(1, (p, q), Bl=Bl); out.add((s["a"], s["t"], s["r1"], s["I"], s["ids"]))
    print(f"  lift {name}: set of (a, t, r1, I, ids) =", sorted(out))
print(" free-part twists psi(z) in {i, -1, -i} (not family characters; expect t0 = 0 => I = 0):")
for zval, zn in ((I_, "i"), (K(-1), "-1"), (I_ * I_ * I_, "-i")):
    out = set()
    for p in range(4):
        for q in range(4):
            s = sector(2, (p, q), zval=zval); out.add((s["a"], s["t"], s["r1"], s["I"], s["ids"]))
    print(f"  psi(z)={zn:2s}: set of (a, t, r1, I, ids) =", sorted(out))
print(" k=4 (a further even sector), untwisted and three twists:")
for pq in ((0, 0), (1, 0), (0, 1), (1, 1)):
    s = sector(4, pq); print(f"  k=4 {pq}: a={s['a']} a*={s['astar']} t={s['t']} r1={s['r1']} r1*={s['r1s']} I={s['I']:+d} ids={s['ids']} float={s['float_ok']}")
json.dump(dict(table=[dict(pq=s["pq"], a=s["a"], astar=s["astar"], t=s["t"], r1=s["r1"], r1s=s["r1s"], I=s["I"], F=s["F"], Cc=s["Cc"],
                           ids=s["ids"], float_ok=s["float_ok"]) for s in rows], nonzero=len(nz), lift_independent=same),
          open("table.json", "w"), indent=1)
print("\nTABLE: nonzero =", len(nz))
