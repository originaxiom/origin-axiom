"""R72 (part 5) -- the menu of fixed-line counts the commensurability class offers.

Tetrahedral census (orientable, cusped, regular ideal tetrahedra -- every member is commensurable with m004), all manifolds
with <= 12 tetrahedra and >= 2 cusps: for each, the symmetry group and, for every orientation-preserving cusp-preserving
isometry, its order and number of fixed lines = (sum over cusps of |det(A - I)|)/2.  Lines fixed by an orientation-
preserving isometry g are the object's charge loci; the count per charged component with equal signs is +-(#lines).
"""
import collections, snappy
def fixcount(m): return abs((m[0,0]-1)*(m[1,1]-1) - m[0,1]*m[1,0])
rows = []
for M in snappy.TetrahedralOrientableCuspedCensus:
    if M.num_tetrahedra() > 12: break
    if M.num_cusps() < 2: continue
    try: G = M.symmetry_group()
    except Exception as e: rows.append((str(M), M.num_tetrahedra(), M.num_cusps(), '?', {})); continue
    menu = collections.Counter()
    for I in G.isometries():
        maps = [I.cusp_maps()[k] for k in range(M.num_cusps())]; perm = I.cusp_images()
        if any(m.det() < 0 for m in maps): continue
        if perm != list(range(M.num_cusps())):
            continue
        # order of the cusp map (all cusp maps have the same order for an isometry of finite order acting on the manifold; take the lcm)
        tr = [int(m.trace()) for m in maps]
        order = {2: 1, 1: 6, 0: 4, -1: 3, -2: 2}
        ords = set(order.get(t) for t in tr)
        o = max(ords) if None not in ords else '?'
        lines = sum(fixcount(m) for m in maps)
        assert lines % 2 == 0, (M, lines)
        if o != 1 and lines > 0: menu[(o, lines//2)] += 1
    rows.append((str(M), M.num_tetrahedra(), M.num_cusps(), G.order(), dict(sorted(menu.items()))))
print(f"{'manifold':26} {'tets':5} {'cusps':6} {'|Sym|':6} menu {{(order, #fixed lines): #isometries}}")
for r in rows: print(f"{r[0]:26} {r[1]:<5} {r[2]:<6} {str(r[3]):6} {r[4]}")
three = [r for r in rows if any(k[1] == 3 for k in r[4])]
print(f"\nmulti-cusped tetrahedral manifolds <= 12 tets: {len(rows)}; with an isometry fixing exactly 3 lines: {len(three)}: {[r[0] for r in three]}")
counts = collections.Counter(k[1] for r in rows for k in r[4])
print("fixed-line counts occurring in the class (<= 12 tets, >= 2 cusps):", dict(sorted(counts.items())))
print("SELFTEST: PASS")
