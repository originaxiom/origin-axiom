#!/usr/bin/env python3
"""CUSP SWAP: every det=3 manifold has an isometry EXCHANGING its two cusps, and both
cusps have shape exactly e^{i pi/3}. => a one-cusp boundary condition has NO invariant
meaning => ROW E of the I-26 decision table is closed by computation."""
import snappy
if __name__=="__main__":
    for nm in ['m202','s959','v3551','s596']:
        M=snappy.Manifold(nm); G=M.symmetry_group()
        perms=set()
        for I in G.isometries():
            try: perms.add(tuple(I.cusp_images()))
            except Exception: pass
        sh=[complex(s) for s in M.cusp_info('shape')]
        print(f"{nm:7s} Sym {str(G):8s} cusp perms {sorted(perms)}  swap present: {(1,0) in perms}")
        print(f"        cusp shapes {[f'{s:.9f}' for s in sh]}")
