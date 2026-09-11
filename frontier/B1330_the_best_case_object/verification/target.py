"""The object the index should be asked of: chiral, in the Q(sqrt-3) class, AND carrying
order-3 cusp-trivial twists. B1324 looked only at m004's own covers."""
import snappy, warnings, itertools, json; warnings.filterwarnings("ignore")
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from fractions import Fraction
SQ3=3.0**0.5; TOL=1e-9; MAXDEN=256
def near_rat(x):
    f=Fraction(x).limit_denominator(MAXDEN); return abs(float(f)-x)<TOL
def in_family(M):
    try: sh=M.tetrahedra_shapes('rect')
    except Exception: return False
    for z in sh:
        z=complex(z)
        if not (near_rat(z.real) and near_rat(z.imag/SQ3)): return False
    return True
def expsum(word,gens):
    v=[0]*len(gens)
    for ch in word:
        if ch.islower(): v[gens.index(ch)]+=1
        else: v[gens.index(ch.lower())]-=1
    return v
def cusp_trivial_order(M):
    """|H_1(M)/<all peripheral curves>| -- the cusp-trivial character group"""
    G=M.fundamental_group(); gens=list(G.generators())
    if not gens: return None
    rows=[expsum(r,gens) for r in G.relators()]
    for pc in G.peripheral_curves():
        for w in pc: rows.append(expsum(w,gens))
    S=smith_normal_form(sp.Matrix(rows))
    if S.cols>S.rank(): return 'INF'
    o=1
    for i in range(min(S.rows,S.cols)):
        d=abs(int(S[i,i]))
        if d==0: return 'INF'
        o*=d
    return o

fam=[]
for M in snappy.OrientableCuspedCensus():
    if in_family(M): fam.append(M.name())
print("Q(sqrt-3) family size:",len(fam))
rows=[]
for nm in fam:
    M=snappy.Manifold(nm)
    try: amph=bool(M.symmetry_group().is_amphicheiral())
    except Exception: amph=None
    o=cusp_trivial_order(M)
    rows.append((nm,M.num_cusps(),amph,o,str(M.homology())))
chiral=[r for r in rows if r[2] is False]
print("chiral members:",len(chiral))
live=[r for r in chiral if isinstance(r[3],int) and r[3]%3==0]
print("CHIRAL + order-3 cusp-trivial characters EXIST:",len(live))
print()
for r in sorted(live,key=lambda x:(x[1],x[0])):
    print(f"   {r[0]:12s} cusps={r[1]}  |cusp-trivial group|={r[3]:4d}  H1={r[4]}")
json.dump(live,open('target.json','w'))
one=[r for r in live if r[1]==1]
print()
print("ONE-CUSPED among them (the index's own domain):",len(one), [r[0] for r in one])
