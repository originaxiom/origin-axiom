"""B202 confirmation + rep dump: figure-eight matexp gate (W1 k=3, W2 k=-3, V0 none) + silver: correct
commuting meridian mu=A^-2 t (word A^3BA^2B, B154) but NO tidy [A,B]=c*mu^k on any component. Dumps a
few (A,B,t) reps per case to JSON for the pyenv test."""
from sage.all import PolynomialRing, QQ, QQbar, ideal
import numpy as np, importlib.util, pathlib, json
spec=importlib.util.spec_from_file_location("per", pathlib.Path("frontier/B71_sl3_apoly/peripheral.py"))
per=importlib.util.module_from_spec(spec); spec.loader.exec_module(per); I3=np.eye(3,dtype=complex)
def matexp(comm,mu,kmax=8):
    best=(None,9e9)
    for k in range(-kmax,kmax+1):
        if k==0: continue
        muk=np.linalg.matrix_power(mu,k) if k>0 else np.linalg.matrix_power(np.linalg.inv(mu),-k)
        Mm=comm@np.linalg.inv(muk); off=max(abs(Mm[i,j]) for i in range(3) for j in range(3) if i!=j)
        dsp=max(abs(Mm[i,i]-Mm[0,0]) for i in range(3))
        if off+dsp<best[1]: best=(k,off+dsp)
    return best
def silver_t(A,B):
    A2B=A@A@B; phiA,phiB=np.linalg.matrix_power(A,3)@B@A2B,A2B
    E=np.vstack([np.kron(A.T,I3)-np.kron(I3,phiA),np.kron(B.T,I3)-np.kron(I3,phiB)])
    t=np.linalg.svd(E)[2][-1].conj().reshape(3,3,order="F"); t=t/np.linalg.det(t)**(1/3)
    res=np.max(np.abs(t@A@np.linalg.inv(t)-phiA))+np.max(np.abs(t@B@np.linalg.inv(t)-phiB))
    return t,res
R=PolynomialRing(QQ,['x%d'%i for i in range(1,9)]); xs=R.gens()
def Tm(c,m):
    x1,x2,x3,x4,x5,x6,x7,x8=c; tau={-1:x6,0:x2,1:x3}; sig={-1:x7,0:x5,1:x8}
    for k in range(2,m+2): tau[k]=x1*tau[k-1]-x4*tau[k-2]+tau[k-3]; sig[k]=x4*sig[k-1]-x1*sig[k-2]+sig[k-3]
    return (tau[m],x1,tau[m+1],sig[m],x4,sig[m-1],tau[m-1],sig[m+1])
def comps(m): return ideal([R(Tm(Tm(xs,m),m)[i]-xs[i]) for i in range(8)]).minimal_associated_primes()
def sample(P,npts=6,seed=1):
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
def dump(M): return [[ [m.real,m.imag] for m in row] for row in M]
out={"figure_eight_W1":[], "silver":[]}
print("=== figure-eight gate (matexp) ===")
rng=np.random.default_rng(2)
for _ in range(6):
    c=per.W1(complex(*rng.standard_normal(2)),complex(*rng.standard_normal(2)))
    o=per.realize(c)
    if o is None: continue
    A,B=o; mu=per.meridian(A,B)[0]; comm=A@B@np.linalg.inv(A)@np.linalg.inv(B)
    k,sc=matexp(comm,mu)
    if sc<1e-6 and len(out["figure_eight_W1"])<2:
        out["figure_eight_W1"].append({"A":dump(A),"B":dump(B),"mu":dump(mu)})
    print("  W1 matexp k=%s score=%.1e"%(k,sc))
print("=== silver: commuting meridian mu=A^-2 t, matexp per component ===")
for ci,P in enumerate(comps(2)):
    scores=[]
    for c in sample(P,6,ci+1):
        o=per.realize(c)
        if o is None: continue
        A,B=o; t,res=silver_t(A,B)
        if res>1e-7: continue
        mu=np.linalg.matrix_power(np.linalg.inv(A),2)@t; comm=A@B@np.linalg.inv(A)@np.linalg.inv(B)
        cdev=np.max(np.abs(mu@comm-comm@mu))
        if cdev>1e-5: continue   # require correct commuting meridian
        k,sc=matexp(comm,mu); scores.append(sc)
        if len(out["silver"])<3:
            out["silver"].append({"A":dump(A),"B":dump(B),"t":dump(t),"comp":ci})
    if scores:
        print("  comp[%d]: %d commuting-meridian reps, matexp best-score median=%.2f (>>1e-6 => NO tidy [A,B]=c*mu^k)"%(ci,len(scores),float(np.median(scores))))
    else:
        print("  comp[%d]: no commuting-meridian reps sampled"%ci)
json.dump(out, open("frontier/B202_silver_avariety/reps.json","w"))
print("DONE; dumped", len(out["figure_eight_W1"]),"fig-W1 +",len(out["silver"]),"silver reps")
