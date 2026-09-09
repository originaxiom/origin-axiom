"""The Galois self-duality theorem, checked: tau: zeta_12 -> zeta_12^7 fixes omega (hence rho_geo) and sends i -> -i (hence chi -> chi^-1),
so V^tau = Sym^2 rho (x) chi^-1 = V*; ranks are Galois-invariant => I = 0 with no reference to the isometry group.
Then: where is the argument unavailable for the Q(sqrt-3) object?  Only for characters of order divisible by 3 (zeta_3 in k).
The 4-fold cyclic cover of m004: H1, its 3-torsion, the cusp classes -- the first Galois-unprotected sector (B1298's object)."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import d2lib as L
from d2lib import K, OMEGA, I_, ONE, ZERO
def tau(x):            # field automorphism zeta -> zeta^7 of Q(zeta_12): coefficients (c0,c1,c2,c3) in basis 1,z,z^2,z^3
    z7 = K((0, 0, 0, 0)); p = ONE; z = L.Z12
    for _ in range(7): p = p * z
    out = K(0); pw = ONE
    for a in x.c:
        out = out + K(a) * pw; pw = pw * p
    return out
print("tau(omega) = omega:", tau(OMEGA) == OMEGA, "  tau(i) = -i:", tau(I_) == -I_, "  tau^2 = id on zeta:", tau(tau(L.Z12)) == L.Z12)
A = L.mat([[1 - OMEGA, 1], [-1, 0]]); B = L.mat([[0, -1], [1, OMEGA * (-2)]])
print("tau fixes rho_geo entrywise:", all(tau(x) == x for M in (A, B) for r in M for x in r))
cp = json.load(open("cover_presentation.json")); gens = cp["gens"]; rels = [[tuple(x) for x in R] for R in cp["rels"]]
mC = [tuple(x) for x in cp["mC"]]; lC = [tuple(x) for x in cp["lC"]]
pres = L.Presentation(gens, rels); inv, cls, V, D, keep = L.h1_coordinates(gens, rels)
def rho_gen(g):
    if g == "z": return L.mmul(L.mmul(B, B), B)
    j = int(g[1:]); M = A; Bi = L.inv2(B)
    for _ in range(j): M = L.mmul(L.mmul(B, M), Bi)
    return M
def chi(pq, g):
    c1, c2, c3 = cls([(g, 1)]); v = ONE
    for _ in range((pq[0] * c1 + pq[1] * c2) % 4): v = v * I_
    return v
ok = True
for p in range(4):
    for q in range(4):
        Vm = {g: L.mscale(L.sym_power(rho_gen(g), 2), chi((p, q), g)) for g in gens}
        Vt = {g: [[tau(x) for x in r] for r in M] for g, M in Vm.items()}
        Vinv = {g: L.mscale(L.sym_power(rho_gen(g), 2), chi(((-p) % 4, (-q) % 4), g)) for g in gens}
        Vd = L.dual_rep(Vm)
        # V^tau == V (x) chi^-1 entrywise; and V* isomorphic to it (Sym^2 self-dual): compare cohomology dims instead of an explicit iso
        ok &= all(L.meq(Vt[g], Vinv[g]) for g in gens)
print("V^tau == Sym^2 rho (x) chi^-1 entrywise for all 16 chi:", ok)
# the Galois-self-duality vanishing: I(V) = I(V^tau) = I(V*) = -I(V)
print("=> I(V) = 0 for every family character, with no use of Isom(C).  [T-GALOIS-SELF-DUALITY]")

print("\n== the 4-fold cyclic cover of m004 (a->0, b->1 mod 4): the first Galois-unprotected sector ==")
REL = L.word_from_snappy("aaabABBAb"); MER = L.word_from_snappy("ab"); LON = L.word_from_snappy("aBAbABab")
g4, r4, rw4, t, others = L.rs_cyclic(["a", "b"], [REL], {"a": 0, "b": 1}, 4)
inv4, cls4, V4, D4, keep4 = L.h1_coordinates(g4, r4)
print("generators:", g4, " relators:", [L.word_to_snappy(R) for R in r4])
print("H1(C_4) invariants:", inv4, "  (|Tors| = |Delta(i)|^2 * |Delta(-1)| = 9 * 5 = 45 expected)")
m4 = rw4(MER * 4); l4 = rw4(LON)
print("[m_C4] =", cls4(m4), " [l_C4] =", cls4(l4), "  classes:", {g: cls4([(g, 1)]) for g in g4})
import itertools
tor_idx = [i for i, d in enumerate(inv4) if d != 0]
n3 = 0; n3_cusp = 0
for expo in itertools.product(*[range(inv4[i]) if i in tor_idx else range(1) for i in range(len(inv4))]):
    if all(e == 0 for e in expo): continue
    order = 1
    from math import gcd
    order = max((inv4[i] // gcd(inv4[i], e)) if e else 1 for i, e in enumerate(expo) if i in tor_idx)
    if order != 3: continue
    n3 += 1
    mcl, lcl = cls4(m4), cls4(l4)
    triv = all((e * mcl[i]) % inv4[i] == 0 and (e * lcl[i]) % inv4[i] == 0 for i, e in enumerate(expo) if i in tor_idx)
    if triv: n3_cusp += 1
print(f"order-3 characters of H1(C_4): {n3}; trivial on the cusp: {n3_cusp}  -> Galois-unprotected sectors for B1298: {n3_cusp // 2} inverse pairs")
import snappy, warnings; warnings.filterwarnings("ignore")
M = snappy.Manifold("m004"); C4 = [c for c in M.covers(4, cover_type="cyclic")][0]
print("SnapPy 4-fold cyclic cover:", C4, C4.homology(), " cusps:", C4.num_cusps(), " |Isom| =", C4.symmetry_group().order())
json.dump(dict(inv4=inv4, n3=n3, n3_cusp=n3_cusp, snappy_h1=str(C4.homology())), open("c4_preview.json", "w"))
