import snappy, warnings; warnings.filterwarnings("ignore")
from snappy import Manifold
from collections import Counter

def mirror(M):
    N=M.copy(); N.reverse_orientation(); return N

def amph_sym(M):
    "orientation-aware test A: SymmetryGroup.is_amphicheiral()"
    try: return M.symmetry_group().is_amphicheiral()
    except Exception: return None

def amph_iso(M):
    "orientation-aware test B: an isometry to the mirror whose cusp maps have det +1"
    try:
        isos=M.is_isometric_to(mirror(M), return_isometries=True)
    except Exception:
        return None
    if isos in (False,None) or len(isos)==0: return False
    for I in isos:
        try: cm=I.cusp_maps()
        except Exception: return None
        dets={m[0,0]*m[1,1]-m[0,1]*m[1,0] for m in cm}
        if dets=={1}: return True
    return False

print("=== CONTROLS (classical facts) ===")
for nm,expected in [('m004',True),('m003',True),('m015',False),('m009',True),('m006',False),('4_1',True),('5_2',False)]:
    try:
        M=Manifold(nm); print(f"  {nm}: symgrp_amph={amph_sym(M)} iso_amph={amph_iso(M)} (classical: amphichiral={expected})")
    except Exception as e: print(" ",nm,e)

print("\n=== the 87 covers of m004 to degree 10 ===")
M=Manifold('m004'); allc=[]
for d in range(2,11):
    for c in M.covers(d): allc.append((d,c))
print("  covers:",len(allc))
rows=[]
for d,c in allc:
    cc=Manifold(c)
    a=amph_sym(cc); b=amph_iso(cc)
    rows.append((d,cc.num_cusps(),a,b))
agree=sum(1 for d,n,a,b in rows if a==b)
print("  two tests agree on:",agree,"of",len(rows))
print("  by test A (symmetry group): amphichiral",sum(1 for r in rows if r[2] is True),
      " chiral",sum(1 for r in rows if r[2] is False), " undet",sum(1 for r in rows if r[2] is None))
print("  by test B (oriented isometry): amphichiral",sum(1 for r in rows if r[3] is True),
      " chiral",sum(1 for r in rows if r[3] is False)," undet",sum(1 for r in rows if r[3] is None))
# cyclic + regular covers
cyc=[]
for d in range(2,11):
    cs=M.covers(d,cover_type='cyclic')
    cyc += [(d,c) for c in cs]
print("  cyclic covers to degree 10:",len(cyc))
reg=[]
for d in range(2,11):
    try: reg += [(d,c) for c in M.covers(d,cover_type='normal')]
    except Exception: pass
print("  normal/regular covers to degree 10:",len(reg))
amph_rows=[r for r in rows if r[2] is True]
print("  amphichiral count (test A):",len(amph_rows)," -> chiral:",len(rows)-len(amph_rows))
print("  cusp distribution of chiral ones:",dict(Counter(r[1] for r in rows if r[2] is False)))
print("  cusp distribution of amphichiral ones:",dict(Counter(r[1] for r in rows if r[2] is True)))
one_cusp_chiral=[r for r in rows if r[1]==1 and r[2] is False]
print("  one-cusped chiral covers:",len(one_cusp_chiral))
multi_chiral=[r for r in rows if r[1]>1 and r[2] is False]
print("  multi-cusped chiral covers:",len(multi_chiral))
