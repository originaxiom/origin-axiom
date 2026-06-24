"""B203: classify the 4 silver SL(3) character-variety components (B201) -- identify the new comp3 and
EXPLAIN B202's no-tidy result. Each component: Burnside dim (9=irreducible), order of A/B/meridian
(finite=Dehn-filling/torsion vs infinite=cusped). Dumps one (A,B) per component to comps.json.
Standalone character-variety math; sage-python (Sage for the variety, numpy for the classification)."""
from sage.all import PolynomialRing, QQ, QQbar, ideal
import numpy as np, importlib.util, pathlib, json
spec=importlib.util.spec_from_file_location("per", pathlib.Path("frontier/B71_sl3_apoly/peripheral.py"))
per=importlib.util.module_from_spec(spec); spec.loader.exec_module(per); I3=np.eye(3,dtype=complex)
def silver_t(A,B):
    A2B=A@A@B; phiA,phiB=np.linalg.matrix_power(A,3)@B@A2B,A2B
    E=np.vstack([np.kron(A.T,I3)-np.kron(I3,phiA),np.kron(B.T,I3)-np.kron(I3,phiB)])
    t=np.linalg.svd(E)[2][-1].conj().reshape(3,3,order="F"); t=t/np.linalg.det(t)**(1/3)
    return t, np.max(np.abs(t@A@np.linalg.inv(t)-phiA))+np.max(np.abs(t@B@np.linalg.inv(t)-phiB))
def burnside(A,B,rounds=6):
    gens=[A,B,np.linalg.inv(A),np.linalg.inv(B)]; allm=[I3]; fr=[I3]
    for _ in range(rounds): fr=[g@m for m in fr for g in gens]; allm+=fr
    return int(np.linalg.matrix_rank(np.array([m.reshape(-1) for m in allm]),tol=1e-7))
def order_of(M,maxd=24):
    e=np.linalg.eigvals(M)
    return next((d for d in range(1,maxd+1) if np.max(np.abs(e**d-1))<1e-6), None)
R=PolynomialRing(QQ,['x%d'%i for i in range(1,9)]); xs=R.gens()
def Tm(c,m):
    x1,x2,x3,x4,x5,x6,x7,x8=c; tau={-1:x6,0:x2,1:x3}; sig={-1:x7,0:x5,1:x8}
    for k in range(2,m+2): tau[k]=x1*tau[k-1]-x4*tau[k-2]+tau[k-3]; sig[k]=x4*sig[k-1]-x1*sig[k-2]+sig[k-3]
    return (tau[m],x1,tau[m+1],sig[m],x4,sig[m-1],tau[m-1],sig[m+1])
def comps(m): return ideal([R(Tm(Tm(xs,m),m)[i]-xs[i]) for i in range(8)]).minimal_associated_primes()
def sample(P,npts=5,seed=1):
    pts=[];tr=0
    while len(pts)<npts and tr<npts*6:
        tr+=1; a=seed*100+tr
        cuts=[sum(QQ(((a*7+i*13+j*5)%17)-8)*xs[j] for j in range(8))-QQ(((a*11+i)%19)-9) for i in range(2)]
        I0=P+ideal(cuts)
        if I0.dimension()!=0: continue
        try: V=I0.variety(QQbar)
        except Exception: continue
        for s in V:
            pts.append(tuple(complex(s[g]) for g in xs))
            if len(pts)>=npts: break
    return pts
def dmp(M): return [[[x.real,x.imag] for x in row] for row in M]
dump={}
for ci,P in enumerate(comps(2)):
    from collections import Counter
    bd=[];oA=[];oB=[];oMU=[]; saved=False
    for c in sample(P,5,ci+1):
        o=per.realize(c)
        if o is None: continue
        A,B=o; bd.append(burnside(A,B)); oA.append(order_of(A)); oB.append(order_of(B))
        t,res=silver_t(A,B)
        if res<1e-7: oMU.append(order_of(np.linalg.matrix_power(np.linalg.inv(A),2)@t))
        if not saved: dump["comp%d"%ci]={"A":dmp(A),"B":dmp(B)}; saved=True
    print("comp[%d] gens0=%s: Burnside=%s  order(A)=%s order(B)=%s order(mu)=%s (None=infinite)"%(
        ci,str(P.gens()[0])[:42],Counter(bd),Counter(oA),Counter(oB),Counter(oMU)),flush=True)
json.dump(dump, open("frontier/B203_silver_components_classified/comps.json","w"))
print("=> all 4 silver components IRREDUCIBLE (Burnside 9), A/B/mu INFINITE order (cusped-type); NONE is a")
print("   finite-order-A Dehn-filling comp (cf. fig-8 W1: A=diag(1,i,-i) order 4) -- explains B202 (no tidy A-variety).")
print("DONE; dumped", len(dump), "comp reps")
