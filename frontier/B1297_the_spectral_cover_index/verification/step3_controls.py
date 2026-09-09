"""Controls (PREREG §5 b,c): exact geometric rep, m004 Sym^k table vs B1256/B1267, RS cover presentation, H1(C) vs B326."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import d2lib as L
from d2lib import K, OMEGA

REL = L.word_from_snappy("aaabABBAb")            # SnapPy m004: <a,b | aaabABBAb>
MER = L.word_from_snappy("ab"); LON = L.word_from_snappy("aBAbABab")
base = L.Presentation(["a", "b"], [REL])
torus = L.Presentation(["m", "l"], [[("m", 1), ("l", 1), ("m", -1), ("l", -1)]])

# exact geometric rep: Fricke normal form from the trace triple, in the SL2-lift where the relator is +I
A = L.mat([[1 - OMEGA, 1], [-1, 0]])
B = L.mat([[0, -1], [1, OMEGA * (-2)]]); B2 = L.mneg(B)
rho = L.Rep({"a": A, "b": B}); rho2 = L.Rep({"a": A, "b": B2})
print("det A, det B:", L.det2(A), L.det2(B))
print("lift (-A,B):  relator =", rho(REL), " tr ab =", L.tr(rho(MER)), " tr long =", L.tr(rho(LON)))
print("lift (-A,-B): relator =", rho2(REL), " tr ab =", L.tr(rho2(MER)), " tr long =", L.tr(rho2(LON)))
assert L.meq(rho(REL), L.eye(2)) and L.meq(rho2(REL), L.eye(2))
assert L.tr(rho(LON)) == K(-2) and L.tr(rho2(LON)) == K(-2) and L.tr(rho(MER)) == K(2) and L.tr(rho2(MER)) == K(-2)
print("numeric tr a, tr b:", L.tr(A).cx(), L.tr(B).cx(), "  (SnapPy step2: tr a = -1.5+0.866i up to the lift sign, tr b = 1-1.732i)")

print("\n== control: untwisted Sym^k on m004 (B1256/B1267: h^1 = 1,0,1,0,1,0,1 for k=0..6) ==")
table = {}
for lift, Bl in (("(-A,B)", B), ("(-A,-B)", B2)):
    print(" lift", lift)
    for k in range(0, 7):
        mats = {"a": L.sym_power(A, k), "b": L.sym_power(Bl, k)}
        d = L.index_data(base, mats, [MER, LON], torus); v = d["V"]
        table[(lift, k)] = (v["a0"], v["a1"], v["a2"], v["t0"], v["t1"], v["r1"], d["Vstar"]["r1"], d["I"], d["F"], all(d["checks"].values()))
        print(f"  k={k}: a=({v['a0']},{v['a1']},{v['a2']}) t=({v['t0']},{v['t1']},{v['t2']}) r1={v['r1']} r1*={d['Vstar']['r1']}  I={d['I']} F={d['F']} Cc={d['Cc']} ids={all(d['checks'].values())}")
assert [table[("(-A,B)", k)][1] for k in range(7)] == [1, 0, 1, 0, 1, 0, 1]

print("\n== the 3-fold cyclic cover by Reidemeister-Schreier (a->0, b->1 mod 3) ==")
gens, rels, rewrite, t, others = L.rs_cyclic(["a", "b"], [REL], {"a": 0, "b": 1}, 3)
print("generators:", gens)
for R in rels: print("  rel:", L.word_to_snappy(R), " len", len(R))
inv, cls, V, D, keep = L.h1_coordinates(gens, rels)
print("H1(C) invariants (SNF):", inv, "  [B326: Z/4 + Z/4 + Z]"); assert inv == [4, 4, 0]
mC = rewrite(MER * 3); lC = rewrite(LON)
print("m_C =", L.word_to_snappy(mC), "  l_C =", L.word_to_snappy(lC))
print("classes: gens ->", {g: cls([(g, 1)]) for g in gens})
print("[m_C] =", cls(mC), " [l_C] =", cls(lC))
def tau_gen(g):
    if g == "z": return rewrite([("b", 1)] * 3)
    j = int(g[1:]); w = [("b", 1)] * j + [("a", 1)] + [("b", -1)] * j
    return rewrite([("b", 1)] + w + [("b", -1)])
tau_images = {g: tau_gen(g) for g in gens}
print("tau on generators:", {g: L.word_to_snappy(w) for g, w in tau_images.items()})
print("tau on H1 classes:", {g: cls(w) for g, w in tau_images.items()})
# cover rep satisfies the cover relators
def rho_gen(g, Bl):
    if g == "z": return L.mmul(L.mmul(Bl, Bl), Bl)
    j = int(g[1:]); M = A; Bi = L.inv2(Bl)
    for _ in range(j): M = L.mmul(L.mmul(Bl, M), Bi)
    return M
for Bl, name in ((B, "+B"), (B2, "-B")):
    R = L.Rep({g: rho_gen(g, Bl) for g in gens})
    print(f"cover rep (lift {name}) satisfies the 3 relators:", all(L.meq(R(r), L.eye(2)) for r in rels))
print("untwisted sector on C: ", end="")
pres = L.Presentation(gens, rels)
d = L.index_data(pres, {g: [[L.ONE]] for g in gens}, [mC, lC], torus); v = d["V"]
print(f"h^1(C;C) = {v['a1']} (b1 = 1), r1 = {v['r1']}, t0 = {v['t0']} -> half lives, half dies; I = {d['I']}")
json.dump(dict(gens=gens, rels=rels, mC=mC, lC=lC, inv=inv, keep=keep, V=V, D=D, tau=tau_images,
               classes={g: cls([(g, 1)]) for g in gens}, mC_class=cls(mC), lC_class=cls(lC)),
          open("cover_presentation.json", "w"))
print("\nCONTROLS: PASS")
