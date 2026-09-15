#!/usr/bin/env python3
"""I-26: every convention for d+M computed. None promoted.
Formula (B1290, banked): net chirality = chi(M, d+M) = chi(M) - chi(d+M).
chi(M) = 0 for every cusped hyperbolic 3-manifold, so net = -chi(d+M)."""
import snappy
def data(nm):
    M=snappy.Manifold(nm); G=M.fundamental_group()
    ng,nr=len(G.generators()),len(G.relators()); chiM=1-ng+nr
    S=M.symmetry_group(); isos=S.isometries()
    def o(k):
        cur=k
        for j in range(2,25):
            cur=S.multiply_elements(cur,k)
            if cur==0: return j
        return None
    th=[k for k in range(1,len(isos)) if o(k)==3]
    fp=[abs(int((m[0,0]-1)*(m[1,1]-1)-m[0,1]*m[1,0])) for m in isos[th[0]].cusp_maps()] if th \
       else [0]*M.num_cusps()
    return M.num_cusps(), chiM, fp
CONV=[("A  truncate, d+M = whole cusp torus",           lambda nc,fp: 0),
      ("B  truncate, d+M = annular subsurface",         lambda nc,fp: 0),
      ("C  cylindrical end, d+M empty (L^2 index)",     lambda nc,fp: 0),
      ("D  truncate, torus minus order-3 fixed discs",  lambda nc,fp: -sum(fp)),
      ("E  same but ONE distinguished cusp",            lambda nc,fp: -fp[0]),
      ("F  d+M = one disc per cusp",                    lambda nc,fp: nc)]
objs=[(nm,)+data(nm) for nm in ['m004','m202','s959']]
print(f"{'convention':44s}" + "".join(f"{o[0]:>9s}" for o in objs))
for lab,f in CONV:
    print(f"{lab:44s}" + "".join(f"{o[2]-f(o[1],o[3]):>9d}" for o in objs))
print("\nA,B,C are the standard readings and all give ZERO.")
print("E is the ONLY row giving 3, and it is unmotivated: see README section 3.")
