#!/usr/bin/env python3
"""B511/D3.1+D3.2 — stationary measure + arcsine test. Streams to d3_results.txt."""
import numpy as np, os, json
HERE=os.path.dirname(os.path.abspath(__file__))
out=open(os.path.join(HERE,"d3_results.txt"),"w")
def log(m): print(m,flush=True); out.write(m+"\n"); out.flush()
def haar(n,rng):
    q=rng.normal(size=(n,4)); q/=np.linalg.norm(q,axis=1,keepdims=True)
    a,b,c,d=q.T
    M=np.zeros((n,2,2),complex)
    M[:,0,0]=a+1j*b; M[:,0,1]=c+1j*d; M[:,1,0]=-c+1j*d; M[:,1,1]=a-1j*b
    return M
def run_measure(seed,n,steps,mix):
    rng=np.random.default_rng(seed)
    A,B=haar(n,rng),haar(n,rng)
    samples=[]
    for t in range(steps):
        r=rng.random(n)
        ev_m=r<mix[0]; ev_d=(r>=mix[0])&(r<mix[0]+mix[1])
        AB=A@B
        Bn=np.where(ev_m[:,None,None], B@A, np.where(ev_d[:,None,None], B@B, A))
        An=np.where(ev_d[:,None,None], A@A, AB)
        A,B=An,Bn
        if t%20==19:
            for Mt in (A,B):
                d=np.sqrt(np.abs(np.linalg.det(Mt))); Mt/=d[:,None,None]
        if t>steps//2 and t%10==9:
            x=np.real(np.trace(A,axis1=1,axis2=2)); y=np.real(np.trace(B,axis1=1,axis2=2))
            z=np.real(np.trace(A@B,axis1=1,axis2=2))
            kap=x*x+y*y+z*z-x*y*z-2
            samples.append(kap)
    return np.concatenate(samples)
log("D3.1 stationary measure (mix M10/D10/F80), 2 seeds x 2 sizes:")
qs=[5,25,50,75,95]
res={}
for seed in (11,42):
    for n,steps in ((1000,4000),(2000,8000)):
        s=run_measure(seed,n,steps,(0.10,0.10))
        res[f"s{seed}_n{n}"]=np.percentile(s,qs).tolist()
        log(f"  seed{seed} n={n} steps={steps}: kappa percentiles {qs} = {np.round(np.percentile(s,qs),4).tolist()}")
log("GATE: the beta-zero at kappa*=0 must appear as the measure's central concentration.")
log("\nD3.2 arcsine test (F80/M20 critical walk): occupation fraction of positive log-increments")
rng=np.random.default_rng(7)
n,steps=1500,4000
A,B=haar(n,rng),haar(n,rng)
S=np.zeros(n); Tpos=np.zeros(n); nM=np.zeros(n)
for t in range(steps):
    ev=rng.random(n)<0.2
    x=np.real(np.trace(A,axis1=1,axis2=2)); y=np.real(np.trace(B,axis1=1,axis2=2))
    z=np.real(np.trace(A@B,axis1=1,axis2=2))
    mult=np.abs(x*x+y*y-x*y*z)
    inc=np.where(ev, np.log(np.maximum(mult,1e-300)), 0.0)
    S+=inc; Tpos+=np.where(ev & (S>0),1,0); nM+=ev
    AB=A@B
    Bn=np.where(ev[:,None,None], B@A, A); A,B=AB,Bn
    if t%20==19:
        for Mt in (A,B):
            d=np.sqrt(np.abs(np.linalg.det(Mt))); Mt/=d[:,None,None]
frac=Tpos/np.maximum(nM,1)
hist,edges=np.histogram(frac,bins=10,range=(0,1))
log(f"  occupation-fraction histogram (10 bins): {hist.tolist()}")
log("  arcsine prediction: U-shaped (peaks at 0 and 1, minimum at 1/2). Uniform or peaked-center = KILL.")
u=hist[0]+hist[-1]; c=hist[4]+hist[5]
log(f"  ends={u} center={c} => {'U-SHAPED (arcsine-consistent)' if u>2*c else 'NOT U-shaped'}")
json.dump({"measure":res,"arcsine_hist":hist.tolist()},open(os.path.join(HERE,"d3_results.json"),"w"))
log("D3 BACKGROUND CELLS COMPLETE")
out.close()
