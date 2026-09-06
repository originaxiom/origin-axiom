"""R72 (part 2) -- m202, the two-cusped tetrahedral manifold, on SnapPy.

 (a) volume ratio to m004, cusp count and shapes; identify() -> otet04_00000 (tetrahedral census, 4 tetrahedra)
 (b) commensurability with m004: shape field Q(sqrt -3) (minimal polynomials of the tetrahedra shapes at high
     precision), integrality of tr a, tr b, tr ab (Fricke: then all traces are integral) => arithmetic, hence
     commensurable with PSL(2, O_3) and with m004.  Also: m202 is not a cover of m004 or m003 of degree <= 6.
 (c) the symmetry group D6 (order 12, all orientation-preserving) and the cusp maps of every isometry;
     |Fix| = |det(A - I)| per cusp: the Z/6 of cusp-preserving isometries has 1, 3, 4 fixed lines for r, r^2, r^3.
 (d) the tetrahedral census up to 8 tetrahedra: every 2-cusped manifold, its symmetry group, and whether some
     orientation-preserving isometry of order 3 fixes 3 points on a cusp (3 lines).
"""
import collections, snappy
from snappy import pari
def fixcount(m): return abs((m[0,0]-1)*(m[1,1]-1) - m[0,1]*m[1,0])
M = snappy.Manifold('m004'); N = snappy.Manifold('m202'); S = snappy.Manifold('m003')
v4 = float(M.volume()); vN = float(N.volume())
print(f"(a) m004: vol {v4:.10f}, cusps {M.num_cusps()}, shapes {[complex(c['shape']) for c in M.cusp_info()]}")
print(f"    m202: vol {vN:.10f}, cusps {N.num_cusps()}, shapes {[complex(c['shape']) for c in N.cusp_info()]}, ratio {vN/v4:.10f}")
print(f"    identify(m202) = {N.identify()}   identify(m004) = {M.identify()}")
assert abs(vN/v4 - 2) < 1e-9 and N.num_cusps() == 2
# (b)
Nh = N.high_precision(); Mh = M.high_precision()
print("(b) shape minimal polynomials: m202", [str(pari(z).algdep(4)) for z in Nh.tetrahedra_shapes('rect')], " m004", [str(pari(z).algdep(4)) for z in Mh.tetrahedra_shapes('rect')])
G = Nh.fundamental_group(); print("    pi_1(m202) =", G.generators(), G.relators())
for w in ['a', 'b', 'ab', 'aab', 'abb', 'abab', 'aabb']:
    tr = G.SL2C(w).trace(); print(f"    tr({w}) = {complex(tr):.6f}   minpoly over Z: {pari(tr).algdep(2)}")
covers = []
for base, nm in ((M, 'm004'), (S, 'm003')):
    for d in range(2, 7):
        for C in base.covers(d):
            if C.num_cusps() == 2 and abs(float(C.volume()) - vN) < 1e-6 and C.is_isometric_to(N): covers.append((nm, d))
print("    m202 as a cover of m004/m003 of degree <= 6:", covers or "none (it is a sibling in the class, not a cover)")
# (c)
Gs = N.symmetry_group(); print(f"(c) Sym(m202) = {Gs}, order {Gs.order()}")
rows = []
for I in Gs.isometries():
    maps = [I.cusp_maps()[k] for k in range(2)]; perm = I.cusp_images()
    dets = [int(m.det()) for m in maps]; trs = [int(m.trace()) for m in maps]
    fixes = [fixcount(m) if perm[k] == k else '-' for k, m in enumerate(maps)]
    rows.append((perm, dets, trs, fixes, [[[int(m[i,j]) for j in range(2)] for i in range(2)] for m in maps]))
print("    perm  dets  traces  |Fix| per cusp   cusp maps")
for r in sorted(rows, key=str): print("   ", r)
assert all(r[1] == [1, 1] for r in rows), "all orientation-preserving"
keep = [r for r in rows if r[0] == [0, 1]]
assert sorted(r[2][0] for r in keep) == [-2, -1, -1, 1, 1, 2], "cusp-preserving subgroup is Z/6"
byorder = {2: [r for r in keep if r[2][0] == 2][0], 1: [r for r in keep if r[2][0] == 1][0], -1: [r for r in keep if r[2][0] == -1][0], -2: [r for r in keep if r[2][0] == -2][0]}
print(f"    Z/6: order-6 element |Fix| = {byorder[1][3]} -> 1 line; order-3 |Fix| = {byorder[-1][3]} -> 3 lines; order-2 |Fix| = {byorder[-2][3]} -> 4 lines")
assert byorder[1][3] == [1, 1] and byorder[-1][3] == [3, 3] and byorder[-2][3] == [4, 4]
# (d)
print("(d) tetrahedral census (orientable, cusped), <= 8 tetrahedra, 2+ cusps:")
for T in snappy.TetrahedralOrientableCuspedCensus:
    if T.num_tetrahedra() > 8: break
    if T.num_cusps() < 2: continue
    Gt = T.symmetry_group(); hits = collections.Counter()
    for I in Gt.isometries():
        maps = [I.cusp_maps()[k] for k in range(T.num_cusps())]; perm = I.cusp_images()
        if any(m.det() < 0 for m in maps): continue
        fixes = tuple(fixcount(m) if perm[k] == k else 'mv' for k, m in enumerate(maps))
        if 3 in [f for f in fixes if f != 'mv']:
            hits[(fixes, sum(f for f in fixes if f != 'mv')//2)] += 1
    sh = [complex(c['shape']) for c in T.cusp_info()]
    print(f"    {str(T):24} tets {T.num_tetrahedra()} cusps {T.num_cusps()} vol/vol(m004) {float(T.volume())/v4:.3f} |Sym| {Gt.order():3} cusp shapes {[f'{z.real:.3f}+{z.imag:.3f}i' for z in sh]}  order-3 with 3 fixed pts (|Fix| per cusp, #lines): {dict(hits) if hits else '-'}")
print("SELFTEST: PASS")
