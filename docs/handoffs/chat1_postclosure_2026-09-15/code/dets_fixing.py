#!/usr/bin/env python3
"""CORRECTED instrument. The bug: cusp_maps() on a CUSP-PERMUTING isometry returns a
map BETWEEN DIFFERENT cusps -- a change of basis, not an automorphism -- so 2-trace is
not a fixed-point count there. Always filter on cusp_images() first."""
import snappy
def dets_fixing(M):
    G=M.symmetry_group(); out=set(); ident=tuple(range(M.num_cusps()))
    for I in G.isometries():
        try:
            if tuple(I.cusp_images())!=ident: continue      # <-- THE FIX
        except Exception: continue
        for m in I.cusp_maps():
            if int(m[0,0]*m[1,1]-m[0,1]*m[1,0])==1:
                out.add(2-int(m[0,0]+m[1,1]))
    return sorted(out)
if __name__=="__main__":
    for nm in ['m004','m003','m202','s959','v3551']:
        print(f"{nm:8s} det(A-I) from cusp-FIXING maps: {dets_fixing(snappy.Manifold(nm))}")
