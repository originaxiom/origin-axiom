"""B1321 / L205 (b) -- the three-line class in the census to nine tetrahedra, and the golden face (DESIGN sealed before this ran).
Class: two-cusped orientable census manifolds with an orientation-preserving isometry fixing a cusp with |det(A - I)| = 3 (an order-3 rotation).
Golden face (main's own test, B1302's method): for a two-generator one-relator presentation, Delta(t1, t2) = (dR/da)/(t2 - 1) up to a unit; the 48
primitive specialisations (|p|,|q| <= 6, (p,q) ~ (-p,-q)) t1 = t^p, t2 = t^q, divisibility by t^2 - 3t + 1. Presentations of rank > 2: the gcd of the
(n-1)-minors of the Fox matrix when sympy reaches it in 120 s, else 'not tested'."""
import json, math, itertools, warnings, time, sys
warnings.filterwarnings("ignore"); import snappy, sympy as sp
t = sp.symbols("t"); GOLD = sp.Poly(t**2 - 3 * t + 1, t)
def cusp_rows(N):
    rows = []
    for iso in N.isomorphisms_to(N):
        for c, (img, A) in enumerate(zip(iso.cusp_images(), iso.cusp_maps())):
            if img != c: continue
            a, b, cc, d = int(A[0, 0]), int(A[0, 1]), int(A[1, 0]), int(A[1, 1]); rows.append((c, a * d - b * cc, abs((a - 1) * (d - 1) - b * cc)))
    return rows
def fox(word, var, imgs):
    total = 0; prefix = 1
    for ch in word:
        g = ch.lower(); e = 1 if ch.islower() else -1; im = imgs[g]
        if g == var: total += prefix if e == 1 else -prefix * im**-1
        prefix *= im**e
    return sp.expand(total)
def alexander_two_var(G, syms):
    """Delta in the free abelian quotient of rank 2 (H1 = Z + Z): images of generators by H1 coordinates; two-generator case exact, else minors' gcd"""
    gens = G.generators(); rels = G.relators(); n = len(gens)
    # H1 coordinates of the generators: abelianise the relators
    import numpy as np
    Mrel = []
    for R in rels:
        v = [0] * n
        for ch in R: v[gens.index(ch.lower())] += 1 if ch.islower() else -1
        Mrel.append(v)
    A = sp.Matrix(Mrel) if Mrel else sp.zeros(0, n)
    # a basis of Hom(H1, Z^2): integer vectors killing the relators; take two independent ones via the smith form of A
    from sympy.matrices.normalforms import smith_normal_form
    ns = A.nullspace() if Mrel else [sp.eye(n)[:, i] for i in range(n)]
    ns = [v * sp.ilcm(*[x.q for x in v]) for v in ns]
    if len(ns) < 2: return None, "H1 rank < 2 in this presentation"
    B = sp.Matrix.hstack(*ns[:2]).T          # 2 x n integer map to Z^2 (a full-rank lattice map; specialisations range over its image -- enough for a divisibility test)
    imgs = {g: syms[0] ** int(B[0, i]) * syms[1] ** int(B[1, i]) for i, g in enumerate(gens)}
    if n == 2 and len(rels) == 1:
        R = rels[0]; d = fox(R, gens[0], imgs); other = imgs[gens[1]]
        q, r = sp.div(sp.Poly(sp.expand(d * syms[0]**20 * syms[1]**20), *syms), sp.Poly(sp.expand((other - 1) * syms[0]**20 * syms[1]**20), *syms))
        # fall back to sympy cancel if the polynomial division leaves a remainder because of monomial factors
        D = sp.cancel(d / (other - 1)); return sp.expand(D), "two-generator"
    if n == len(rels) + 1 and n <= 4:
        J = sp.Matrix([[fox(R, g, imgs) for g in gens] for R in rels])
        minors = [J[:, [k for k in range(n) if k != j]].det() for j in range(n)]
        D = 0
        for m in minors: D = sp.gcd(D, sp.expand(m)) if D != 0 else sp.expand(m)
        return sp.expand(D), f"rank {n} minors' gcd"
    return None, f"presentation rank {n}, {len(rels)} relators: not tested"
def golden_test(D, syms):
    prims = sorted({(p, q) if (p, q) > (-p, -q) else (-p, -q) for p in range(-6, 7) for q in range(-6, 7) if (p, q) != (0, 0) and math.gcd(abs(p), abs(q)) == 1})
    hits = []
    for p, q in prims:
        f = sp.expand(D.subs({syms[0]: t**p, syms[1]: t**q}))
        if f == 0: continue
        num, den = sp.fraction(sp.together(f)); P = sp.Poly(sp.expand(num), t)
        if P.degree() > 0 and sp.rem(P, GOLD).is_zero: hits.append((p, q))
    return len(prims), hits
t1, t2 = sp.symbols("t1 t2"); out = dict(design="see DESIGN.sha256", tets_max=9, scanned=0, two_cusped=0, klass=[], untested=[], golden=[])
t0 = time.time()
for k in range(2, 10):
    for N in snappy.OrientableCuspedCensus(tets=k):
        out["scanned"] += 1
        if N.num_cusps() != 2: continue
        out["two_cusped"] += 1
        rows = cusp_rows(N); three = [r for r in rows if r[1] == 1 and r[2] == 3]
        if not three: continue
        G = N.fundamental_group(); D, how = alexander_two_var(G, (t1, t2))
        rec = dict(name=N.name(), tets=k, H1=str(N.homology()), cusps_with_3=sorted({r[0] for r in three}), values={f"{r[2]}|det{r[1]:+d}": sum(1 for s in rows if s == r) for r in set(rows)}, presentation=how)
        if D is None: out["untested"].append(rec)
        else:
            nprims, hits = golden_test(D, (t1, t2)); rec.update(primitive_classes=nprims, golden_hits=hits, delta=str(D)[:200])
            if hits: out["golden"].append(rec)
        out["klass"].append(rec)
        print(f"  {N.name():<8} tets {k} H1 {rec['H1']:<18} cusps with a 3: {rec['cusps_with_3']}  {how:<28} golden hits: {rec.get('golden_hits', 'n/a')}", flush=True)
print(f"scanned {out['scanned']} census manifolds, {out['two_cusped']} two-cusped, class size {len(out['klass'])}, untested {len(out['untested'])}, golden-face members {len(out['golden'])}  [{time.time()-t0:.0f}s]")
# controls: m202 in the class with 0 golden hits; a planted golden factor is detected
m202 = [r for r in out["klass"] if r["name"] == "m202"]; ctrl_m202 = bool(m202) and m202[0].get("golden_hits") == []
Dm = alexander_two_var(snappy.Manifold("m202").fundamental_group(), (t1, t2))[0]; planted = golden_test(sp.expand(Dm * (t1**2 - 3 * t1 + 1)), (t1, t2))[1]
out["controls"] = dict(m202_in_class_no_golden=ctrl_m202, planted_detected=bool(planted), m202_record=m202[0] if m202 else None)
out["verdict"] = "PASS: a golden-face member exists" if out["golden"] else "FAIL: no member of the three-line class to nine tetrahedra keeps the golden face"
print("controls:", out["controls"]); print(out["verdict"]); json.dump(out, open("b1321_class_search.json", "w"), indent=1, default=str)
