"""B422 -- does the Z/2 (mirror/class-group) connect the golden line and Mercedes plane?"""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(HERE, "..", "B367_value_map", "step0_tables.json")))
o2 = 12
# golden slot line: (1,2) rows 6,14 as Z12 vectors (the s-component); Mercedes: (2,3) cols 0,2,4
def v12_row_12(a):
    v=[Fr(0)]*o2
    for k,val in T["1,2"].items():
        aa,b=map(int,k.split(","))
        if aa==a: v[b]=Fr(val[3])
    return v
def v12_col_23(b):
    v=[Fr(0)]*o2
    for k,val in T["2,3"].items():
        a,bb=map(int,k.split(","))
        if bb==b: v[a]=Fr(val[3])
    return v
g6=v12_row_12(6)                     # golden line (rows 6,14 antipodal per B400)
M=[v12_col_23(b) for b in (0,2,4)]   # Mercedes plane
def dot(u,v): return sum(x*y for x,y in zip(u,v))
# Q1: the mirror image of the golden line: b -> -b mod 12
def mirror(v): return [v[(-i)%o2] for i in range(o2)]
g6m=mirror(g6)
# overlap of g6 and g6m with the Mercedes plane (project onto span M)
def plane_overlap(w, basis):
    # gram-based: |proj|^2 / |w|^2 via the basis
    import itertools
    # build normal equations (basis^T basis) c = basis^T w
    n=len(basis)
    G=[[dot(basis[i],basis[j]) for j in range(n)] for i in range(n)]
    rhs=[dot(basis[i],w) for i in range(n)]
    # solve (exact)
    A=[row[:]+[rhs[i]] for i,row in enumerate(G)]
    for c in range(n):
        piv=next((r for r in range(c,n) if A[r][c]!=0),None)
        if piv is None: continue
        A[c],A[piv]=A[piv],A[c]; pv=A[c][c]; A[c]=[x/pv for x in A[c]]
        for r in range(n):
            if r!=c and A[r][c]!=0:
                f=A[r][c]; A[r]=[A[r][k]-f*A[c][k] for k in range(n+1)]
    coeffs=[A[i][n] for i in range(n)]
    proj=[sum(coeffs[i]*basis[i][k] for i in range(n)) for k in range(o2)]
    return dot(proj,proj), dot(w,w)
p_g, n_g = plane_overlap(g6, M)
p_gm, n_gm = plane_overlap(g6m, M)
print(f"golden line overlap with Mercedes plane: |proj|^2={p_g}, |g|^2={n_g}  -> cos^2={float(p_g/n_g) if n_g else 0:.4f}")
print(f"MIRRORED golden line overlap with Mercedes: |proj|^2={p_gm}, |g|^2={n_gm} -> cos^2={float(p_gm/n_gm) if n_gm else 0:.4f}")
frame = (p_g != 0 or p_gm != 0)
print("Z/2 connects golden and Mercedes (non-orthogonal):", frame)
res=dict(golden_overlap=str(p_g), golden_mirror_overlap=str(p_gm),
         golden_norm=str(n_g), frame_exists=bool(frame),
         verdict=("FRAME: the Z/2 connects the sectors -- content wall evaded" if frame
                  else "NO FRAME: orthogonality preserved under Z/2 -- content wall holds; frame is external"))
print("VERDICT:", res["verdict"])
json.dump(res, open("mirror_frame.json","w"), indent=1)
print("DONE")
