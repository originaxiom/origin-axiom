#!/usr/bin/env python3
"""CS VALIDITY GATE. SnapPy returns cs values for NON-hyperbolic fillings (volume
0.0000000, solution_type 'contains flat tetrahedra'). Those are INVALID.
p=4 returns n/a, which exposes p=0,1,2,3. ALWAYS gate on solution_type.
B286's slope law is UNAFFECTED: all 8 slopes in that run are individually hyperbolic."""
import snappy
def cs_valid(M):
    return M.solution_type()=='all tetrahedra positively oriented'
if __name__=="__main__":
    print("validity gate on m004(p,1):")
    for p in range(0,7):
        M=snappy.Manifold('m004'); M.chern_simons(); M.dehn_fill((p,1))
        try: cs=f"{float(M.chern_simons()):+.9f}"
        except Exception: cs="n/a"
        print(f"  p={p}: {M.solution_type()[:28]:28s} vol {float(M.volume()):10.7f} cs {cs:>14s} "
              f"VALID={cs_valid(M)}")
    print("\nB286 slope law, hyperbolic slopes only:")
    ok=0
    for (p,q) in [(5,1),(7,1),(7,2),(9,1),(5,2),(8,3),(11,2),(13,4)]:
        A=snappy.Manifold('m004'); A.chern_simons(); A.dehn_fill((p,q))
        B=snappy.Manifold('m004'); B.chern_simons(); B.dehn_fill((p,-q))
        if not(cs_valid(A) and cs_valid(B)): continue
        s=(float(A.chern_simons())+float(B.chern_simons()))%1.0; s=min(s,1-s)
        ok+= s<1e-8
        print(f"  ({p},{q}): |sum| mod 1 = {s:.2e}")
    print(f"  law holds {ok}/8")
