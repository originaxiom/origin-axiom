"""scan.py -- the 3D index of m004 and m003 over the whole saturated lattice of boundary
classes with |x|,|y| <= 4 (half-steps where admissible), to q^32, with the exact
minimal-degree bound recorded for every class so that a series which is 0 on the window
can be told apart from a series whose leading term is beyond the window."""
import json, itertools, sys
from fractions import Fraction as F
import snappy
from idx import index_class, rows, bdry_vector, triples, J_mindeg
from tet_index import s_str, s_trunc

X = 64                       # x-exponent budget => q^32
HALF = 4                     # |x|,|y| <= HALF, in half-steps

def minD(name, cls, box=400, mfd=None):
    """min over the gauge slice of the exact minimal x-degree of the k-term (a LOWER bound
       for the leading degree of I; cancellation can only push the true leading degree up)."""
    M,n,r,E,Mr,Ln = rows(name, mfd)
    v = bdry_vector(n,Mr,Ln,cls)
    free=[i for i in range(n) if i>=r]
    best=None; arg=None
    for kk in itertools.product(range(-box,box+1),repeat=len(free)):
        k=[0]*n
        for idx,i in enumerate(free): k[i]=kk[idx]
        D=2*sum(k)+sum(J_mindeg(*t) for t in triples(E,n,k,v))
        if best is None or D<best: best,arg=D,tuple(kk)
    return best,arg

def admissible(name):
    M,n,r,E,Mr,Ln = rows(name)
    out=[]
    for a in range(-2*HALF,2*HALF+1):
        for b in range(-2*HALF,2*HALF+1):
            x,y=F(a,2),F(b,2)
            try:
                bdry_vector(n,Mr,Ln,((x,y),)); out.append((x,y))
            except AssertionError: pass
    return out

data={}
for name in ["m004","m003"]:
    adm=admissible(name)
    print(f"{name}: {len(adm)} admissible classes with |x|,|y| <= {HALF}", file=sys.stderr)
    d={}
    for (x,y) in adm:
        mD,arg=minD(name,((x,y),))
        Xm = max(X, mD+24)
        s = index_class(name, ((x,y),), Xm)
        lead = min(s) if s else None
        d[f"{x},{y}"]={"minD":mD,"lead":lead,"Xmax":Xm,
                       "ser":{str(k):v for k,v in sorted(s_trunc(s,Xm).items())}}
    data[name]=d
json.dump(data,open("scan.json","w"),indent=0)
print("wrote scan.json", file=sys.stderr)
