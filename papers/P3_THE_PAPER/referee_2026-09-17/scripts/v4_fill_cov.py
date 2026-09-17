import snappy, warnings, math, itertools; warnings.filterwarnings("ignore")
from snappy import Manifold
from collections import Counter

def mirror(M):
    N=M.copy(); N.reverse_orientation(); return N
M=Manifold('m004')
print("m004 amphichiral (isometric to mirror):", M.is_isometric_to(mirror(M)))
print("m004 Alexander poly: skipped (needs Sage); classical value t^2-3t+1")
print("m004 symmetry group:", M.symmetry_group(), " order:", M.symmetry_group().order())
sg=M.symmetry_group()
print("  is_amphicheiral:", sg.is_amphicheiral())

print("\n=== FILLINGS: |p| <= 8, q <= 8 grid ===")
slopes=[(p,q) for p in range(-8,9) for q in range(-8,9) if math.gcd(abs(p),abs(q))==1 and (p,q)!=(0,0)]
# the paper says "the |p|,q <= 8 grid" with mirror pairs m004(p,q)=m004(-p,q); take q>=1 plus (1,0)
grid=[(p,q) for p in range(-8,9) for q in range(0,9) if math.gcd(abs(p),abs(q))==1 and not (q==0 and p!=1)]
print("  slopes in grid (q>=0, gcd=1, q=0 -> (1,0)):", len(grid))
hyp=[];nonhyp=[]
for (p,q) in grid:
    N=Manifold('m004'); N.dehn_fill((p,q)); st=N.solution_type()
    (hyp if st=='all tetrahedra positively oriented' else nonhyp).append((p,q))
print("  hyperbolic:",len(hyp)," non-hyperbolic:",len(nonhyp), sorted(nonhyp))

print("\n=== EXCEPTIONAL SLOPES of m004 (all slopes, not just grid) ===")
exc=[]
for p in range(-12,13):
    for q in range(0,13):
        if math.gcd(abs(p),abs(q))!=1: continue
        if q==0 and p!=1: continue
        N=Manifold('m004'); N.dehn_fill((p,q))
        if N.solution_type()!='all tetrahedra positively oriented': exc.append((p,q))
print("  exceptional slopes found:", sorted(exc), "count:", len(exc))

print("\n=== COVERS to degree 10 ===")
allc=[]
for d in range(2,11):
    for c in M.covers(d): allc.append((d,c))
print("  total covers to degree 10:", len(allc), " by degree:", dict(Counter(d for d,_ in allc)))
print("  total cusps:", sum(c.num_cusps() for _,c in allc))
print("  cusp-count distribution:", dict(Counter(c.num_cusps() for _,c in allc)))
chiral=0; amphi=0; amphi_list=[]
for d,c in allc:
    cc=Manifold(c); cc.set_peripheral_curves('fillings') if False else None
    try:
        am = cc.is_isometric_to(mirror(cc))
    except Exception as e:
        am = None
    if am is True: amphi+=1; amphi_list.append((d,c.num_cusps()))
    elif am is False: chiral+=1
print("  amphichiral:",amphi," chiral:",chiral," undetermined:",len(allc)-amphi-chiral)
print("  amphichiral covers (degree,cusps):", amphi_list)
one_cusped=[(d,c) for d,c in allc if c.num_cusps()==1]
print("  one-cusped covers:", len(one_cusped))
