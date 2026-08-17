import sys,os,pathlib,itertools,numpy as np,sympy as sp
from fractions import Fraction
from collections import Counter
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
PRIME=int(sys.argv[1])
src=pathlib.Path(os.path.join(os.path.dirname(os.path.abspath(__file__)),"cell5_spinor_test.py")).read_text()
src=src.split('print("\\nSTABILISER')[0].replace("PRIME = int(sys.argv[1]) if len(sys.argv) > 1 else 1093",f"PRIME = {PRIME}")
exec(compile(src,"c5","exec"))
def basis16(forms):
    S=[(Pm16@vec(embed_form(f,n,TWENTYSEVEN)))%P for f,n in forms]
    ind=[]
    for s in S:
        T=np.array([[int(t)%P for t in u] for u in ind+[s]],dtype=np.int64)
        if rank_mod_p(T)>len(ind): ind.append(s)
    return ind
OM =[(sp.expand(Psi**2),8),(sp.expand(Phi**4),16),(sp.expand(Wp*Psi**2),16)]
OM2=[(sp.expand(Phi**2),8),(sp.expand(Psi**4),16),(sp.expand(Wp*Phi**2),16)]
for name,FS in (("omega",OM),("omega^2",OM2)):
    ind=basis16(FS)
    spec=Counter(); pure=[]
    pts=[(1,t) for t in range(P)]+[(0,1)]
    for (u,v) in pts:
        s=(u*ind[0]+v*ind[1])%P
        if not np.count_nonzero(s): continue
        rows=[[int(t)%P for t in (A_.astype(object)@s)%P] for A_ in ops]
        d=45-rank_mod_p(np.array(rows,dtype=np.int64).T%P)
        spec[d]+=1
        if d==34: pure.append((u,v))
    krs=set()
    for (u,v) in pure:
        s=(u*ind[0]+v*ind[1])%P
        rows=[[int(t)%P for t in (A_.astype(object)@s)%P] for A_ in ops]
        ns2=nullspace(np.array(rows,dtype=np.int64).T%P); els=[]
        for vv in ns2:
            xx={}
            for co,Xb in zip(vv,elts):
                if co%P: xx=E.vadd(xx,E.vmul(Fraction(int(co)%P),Xb))
            els.append(xx)
        K=np.zeros((len(els),len(els)),dtype=np.int64)
        for r1,z1 in enumerate(els):
            for r2,z2 in enumerate(els):
                kv=E.killing_pair(z1,z2); K[r1,r2]=(kv.numerator%P)*pow(kv.denominator%P,P-2,P)%P
        krs.add((len(els),rank_mod_p(K)))
    print(f"  {name:8s}: span {len(ind)}  spectrum {dict(spec)}  pure points {len(pure)} at {pure}  (dim,Killing) {krs}")
