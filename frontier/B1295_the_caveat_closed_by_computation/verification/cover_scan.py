#!/usr/bin/env python3
"""B1295 / D4(c) -- the degree-<=10 cover scan of m004: NO cusp of the object's own tower carries
an isometry with an isolated fixed-point count other than 0 or 4.

WHY IT MATTERS.  B1291 proved that one cusp forces an even number of arc endpoints (|Fix| even).
The only way to get THREE arc endpoints on a cusp torus is an isometry acting on that torus
with an odd isolated fixed-point count -- a rotation of order 3 or 6 (|det(A - I)| = 3 or 1);
order 4 gives 2, order 2 gives 4, and det(A - I) = 0 covers the parabolic / glide / reflection
cases (empty or 1-dimensional fixed sets).  This scan asks the object's own tower whether such a
cusp exists anywhere among the finite covers of m004 up to degree 10.

WHAT IS COMPUTED.  For every cover N of m004 of degree 2..10 (all conjugacy classes of
subgroups, SnapPy `covers(d)`), every isometry g of N (SnapPy `isomorphisms_to`, both
orientations), every cusp c with g(c) = c: the matrix A of g on H_1(c) and |det(A - I)|.
NEGATIVE = the set of values is a subset of {0, 4}.  Every failure of SnapPy to produce the
isometry group of a cover is recorded, not skipped silently.
"""
import json, time, warnings
from collections import Counter
warnings.filterwarnings("ignore")
import snappy

def reduced_shape(z):
    """SL(2,Z)-reduce a cusp shape to the standard fundamental domain."""
    z = complex(z)
    for _ in range(200):
        z = complex(z.real - round(z.real), z.imag)
        if abs(z) >= 1 - 1e-12: break
        z = -1 / z
    return z
def shape_class(z):
    z = reduced_shape(z)
    if abs(z - 1j) < 1e-6: return "square"
    if abs(z - complex(0.5, 3**0.5 / 2)) < 1e-6 or abs(z - complex(-0.5, 3**0.5 / 2)) < 1e-6: return "hexagonal"
    if abs(z.real) < 1e-6 or abs(abs(z.real) - 0.5) < 1e-6: return "rectangular/rhombic"
    return "generic"

M = snappy.Manifold("m004")
rows, failures, values, shapes = [], [], Counter(), Counter()
t0 = time.time()
for d in range(2, 11):
    covs = M.covers(d)
    for i, N in enumerate(covs):
        nc = N.num_cusps()
        sc = [shape_class(ci['shape']) for ci in N.cusp_info()]
        for k in sc: shapes[k] += 1
        try:
            isos = N.isomorphisms_to(N)
        except Exception as e:
            failures.append(dict(degree=d, index=i, cusps=nc, error=str(e)[:200])); continue
        per_cover = Counter()
        n_fixed_pairs = 0
        for g in isos:
            imgs = g.cusp_images(); maps = g.cusp_maps()
            for c in range(nc):
                if imgs[c] != c: continue
                A = maps[c]
                a, b, cc, dd = int(A[0,0]), int(A[0,1]), int(A[1,0]), int(A[1,1])
                det_AmI = abs((a-1)*(dd-1) - b*cc)
                per_cover[(det_AmI, a*dd - b*cc)] += 1
                values[det_AmI] += 1
                n_fixed_pairs += 1
        rows.append(dict(degree=d, index=i, cusps=nc, cusp_shapes=sc, H1=str(N.homology()), n_isometries=len(isos),
                         n_cusp_fixing_pairs=n_fixed_pairs,
                         det_AmI_by_orientation={f"{k[0]}|det{k[1]:+d}": v for k, v in sorted(per_cover.items())}))
    print(f"degree {d}: {len(covs)} covers done, values so far {dict(values)}, {time.time()-t0:.0f}s", flush=True)

multi = sum(1 for r in rows if r["cusps"] > 1)
verdict = "NEGATIVE" if set(values) <= {0, 4} and not failures else "OPEN"
out = dict(covers=len(rows), multi_cusped=multi, failures=failures, values=dict(values), cusp_shapes=dict(shapes),
           isometries_total=sum(r["n_isometries"] for r in rows),
           cusp_fixing_pairs=sum(r["n_cusp_fixing_pairs"] for r in rows), verdict=verdict, rows=rows)
json.dump(out, open("cover_scan.json", "w"), indent=1)
print(f"covers {len(rows)} ({multi} multi-cusped), isometries {out['isometries_total']}, cusp-fixing pairs "
      f"{out['cusp_fixing_pairs']}, |det(A-I)| values {dict(values)}, failures {len(failures)}")
print(f"cusp shapes over all {sum(shapes.values())} cusps (SL2Z-reduced): {dict(shapes)}  -- order 3/6 needs hexagonal, order 4 needs square")
print("VERDICT:", verdict, "-- no order-3/4/6 cusp rotation in the tower through degree 10" if verdict == "NEGATIVE" else "")
