"""B1302 Q2: the two-cusp index on m202 for Sym^2 rho (x) psi over the cusp-trivial characters of H1 = Z^2 (exact over Q(zeta_12))."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "B1297_the_spectral_cover_index", "verification"))
import d2lib as L, d2multi as D
from d2lib import K, ONE, ZERO, Z12, OMEGA, I_
ex = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "m202_exact.json")))
def parse(s):  # "(c0 + c1*z + ...)" back to K -- rebuild from the exact search instead (deterministic): rerun the small search is slow; store as coefficients
    raise NotImplementedError
# rebuild A, B exactly from the printed forms: A = [[-2 z^2, -1 - z^2], [z^2, z^2]], B = [[-z^2, z^2], [-1 + z^2, 0]]
z2 = Z12 * Z12
A = L.mat([[z2 * (-2), K(-1) - z2], [z2, z2]]); B = L.mat([[-z2, z2], [K(-1) + z2, ZERO]])
rel = ex["rel"]; RELS = [L.word_from_snappy(rel)]; CUSPS = [[L.word_from_snappy(w) for w in pc] for pc in ex["cusps"]]
gens = ["a", "b"]; pres = L.Presentation(gens, RELS); rho = L.Rep({"a": A, "b": B})
assert L.meq(rho(RELS[0]), L.eye(2)) and L.det2(A) == ONE and L.det2(B) == ONE
# H1 = Z^2 with a, b as basis (relator has zero exponent sums)
inv, cls, V, Dg, keep = L.h1_coordinates(gens, RELS); print("H1(m202) invariants:", inv, " classes:", {g: cls([(g, 1)]) for g in gens})
cusp_classes = [(cls(m), cls(l)) for m, l in CUSPS]; print("cusp classes (m, l) per cusp:", cusp_classes)
# characters trivial on every peripheral class: psi(a) = x, psi(b) = y with x^p y^q = 1 for every cusp class (p, q); the sublattice L spanned by the cusp classes
import itertools
lat = [c for pair in cusp_classes for c in pair]
# Smith form of the 2 x k lattice matrix -> index
Dm, U, Vm = L.smith([[c[0] for c in lat], [c[1] for c in lat]], len(lat))
diag = [Dm[i][i] for i in range(2)]; print("peripheral sublattice: elementary divisors", diag, " index", diag[0] * diag[1] if all(diag) else "infinite")
# cusp-trivial characters: Hom(Z^2 / L, C*) has |Z^2/L| elements; enumerate via the SNF: chi = exp(2 pi i (e1 c1/d1 + e2 c2/d2)) in the SNF basis
d1, d2 = diag
def char_vals(e1, e2):
    # coordinates of a, b in the SNF basis: row k of U gives ... use U: U * Lmat * V = D ; classes in Z^2 map by U to SNF coords
    out = {}
    for g, vec in (("a", (1, 0)), ("b", (0, 1))):
        c = [sum(U[i][j] * vec[j] for j in range(2)) for i in range(2)]
        k = (e1 * c[0] * (12 // d1) + e2 * c[1] * (12 // d2)) % 12 if (12 % d1 == 0 and 12 % d2 == 0) else None
        assert k is not None, "orders not dividing 12: need a larger field"
        v = ONE
        for _ in range(k): v = v * Z12
        out[g] = v
    return out
sectors = []
for e1 in range(d1):
    for e2 in range(d2):
        chi = char_vals(e1, e2)
        ok = all(all((chi["a"] ** 0 if False else True) for _ in [0]) for _ in [0])
        # check cusp-triviality exactly
        triv = True
        for m, l in CUSPS:
            for w in (m, l):
                v = ONE
                for g, e in w: v = v * (chi[g] if e == 1 else chi[g].inv())
                triv &= (v == ONE)
        assert triv, "character not cusp-trivial"
        mats = {g: L.mscale(L.sym_power(rho([(g, 1)]), 2), chi[g]) for g in gens}
        d = D.index_multi(pres, mats, CUSPS); v = d["V"]
        sectors.append(dict(e=(e1, e2), a=(v["a0"], v["a1"], v["a2"]), t=(v["t0"], v["t1"], v["t2"]), r1=v["r1"], r1s=d["Vstar"]["r1"], I=d["I"], F=d["F"], ids=all(d["checks"].values())))
        print(f"psi = ({e1},{e2}): a={sectors[-1]['a']} t={sectors[-1]['t']} r1={v['r1']} r1*={d['Vstar']['r1']} I={d['I']:+d} F={d['F']:+d} ids={sectors[-1]['ids']}")
# controls: untwisted k = 0 and k = 2 (psi = 1 is included above); k = 0:
d0 = D.index_multi(pres, {g: [[ONE]] for g in gens}, CUSPS); v = d0["V"]
print(f"untwisted k=0: h1(m202;C) = {v['a1']} (b1 = 2), t0 = {v['t0']}, r1 = {v['r1']} (half lives, half dies: r1 = t0 = 2), I = {d0['I']}")
nz = [s for s in sectors if s["I"] != 0]
print(f"Q2: cusp-trivial twists {len(sectors)}, nonzero indices {len(nz)}, identities all {all(s['ids'] for s in sectors)}; k=0 control r1 = t0 = 2: {v['r1'] == 2 and v['t0'] == 2}")
json.dump(dict(inv=inv, cusp_classes=cusp_classes, divisors=diag, sectors=sectors, k0=dict(a1=v["a1"], t0=v["t0"], r1=v["r1"], I=d0["I"])), open("b1302_index.json", "w"))
print("Q2:", "PASS" if not nz and all(s["ids"] for s in sectors) and v["r1"] == 2 and v["t0"] == 2 else "FAIL")
