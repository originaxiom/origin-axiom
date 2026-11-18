"""B1957: the web seat's session relay of 2026-09-08, its line on seven manifolds: 'all carry a three-line Z/3; 3
comes from order 3 in every one', and its withdrawal of its own flag (a three-cusped manifold whose symmetry of order 3
acts trivially on one cusp).  Computed on main with SnapPy from the census names; nothing of the seat's is run.
For each manifold: the number of cusps, the order of the symmetry group, and for every symmetry of order 3 the trace
of its action on the homology of each cusp it fixes, with the count sum over fixed cusps of det(A - 1), halved."""
import functools
from collections import Counter
import snappy
print = functools.partial(print, flush=True)
NAMES = ["m202", "otet06_00002", "otet07_00000", "otet10_00005", "otet10_00046", "otet12_00044", "otet12_00045"]

if __name__ == "__main__":
    allok = True
    for name in NAMES:
        M = snappy.Manifold(name); G = M.symmetry_group(); n = G.order(); iso = G.isometries(); ident = next(i for i in range(n) if all(G.multiply_elements(i, j) == j for j in range(n)))
        rows = Counter()
        for i in range(n):
            sq = G.multiply_elements(i, i)
            if i == ident or G.multiply_elements(sq, i) != ident: continue
            imgs = iso[i].cusp_images(); maps = iso[i].cusp_maps(); tr = []; tot = 0
            for c in range(M.num_cusps()):
                if imgs[c] != c: tr.append(None); continue
                A = maps[c]; a, b, cc, d = int(A[0, 0]), int(A[0, 1]), int(A[1, 0]), int(A[1, 1]); assert a * d - b * cc == 1
                tr.append(a + d); tot += (a - 1) * (d - 1) - b * cc
            rows[(tuple(tr), tot / 2)] += 1
        three = [k for k in rows if k[1] == 3]; allok &= bool(three)
        print("%-13s tetrahedra %2d, cusps %d, symmetries %3d; those of order 3, as (traces on the cusps they fix, half the sum of det(A - 1)): %s" % (name, M.num_tetrahedra(), M.num_cusps(), n, {str(k): v for k, v in sorted(rows.items(), key=str)}))
    print("every one of the seven has a symmetry of order 3 whose count is 3: %s" % allok)
