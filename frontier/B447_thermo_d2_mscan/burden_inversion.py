"""B447 burden-inversion session on the C_peak_T flag.

Declared bounded F (cap: K<=4): peak_T of the C(T) of the K-point Gauss
quadrature of the spectral measure (DOS). The 2K moments are exact class
arithmetic (substitution letter statistics). Parameter-free; out-of-sample
at V=0.5 and V=2.0 (nothing fitted).
"""
import numpy as np, math, sys
sys.path.insert(0,'.')
from harness import *

Tg=np.logspace(-2,1,2400)

def high_peak_of(Evals, weights=None):
    E=np.asarray(Evals,float)
    w=np.ones(len(E))/len(E) if weights is None else np.asarray(weights,float)
    E0=E-E.min()
    best=None; C=[]
    for T in Tg:
        b=np.exp(-E0/T); Z=(w*b).sum()
        e1=(w*E0*b).sum()/Z; e2=(w*E0*E0*b).sum()/Z
        C.append((e2-e1*e1)/T/T)
    C=np.array(C)
    for i in range(1,len(Tg)-1):
        if C[i]>C[i-1] and C[i]>C[i+1]:
            lt=np.log(Tg[i-1:i+2]); a=np.polyfit(lt,C[i-1:i+2],2)
            t=float(np.exp(-a[1]/(2*a[0])))
            if best is None or t>best: best=t
    return best

def gauss_quadrature_dos(E, K):
    """K-point Gauss quadrature of the DOS via Lanczos on diag(E), start=uniform."""
    N=len(E)
    v=np.ones(N)/math.sqrt(N)
    a=[]; b=[]
    V=[v]
    w=E*v
    a.append(float(v@w))
    w=w-a[0]*v
    for k in range(1,K):
        bk=float(np.linalg.norm(w)); b.append(bk)
        v2=w/bk; V.append(v2)
        w=E*v2 - bk*V[k-1]
        ak=float(v2@w); a.append(ak)
        w=w-ak*v2
        # full reorthogonalization (small K, cheap, stable)
        for u in V:
            w=w-(u@w)*u
    J=np.diag(a)+np.diag(b,1)+np.diag(b,-1)
    nodes,vecs=np.linalg.eigh(J)
    weights=vecs[0,:]**2
    return nodes,weights

print("== burden-inversion: measured peak vs K-point moment-surrogate peak ==")
for V in (0.5,1.0,2.0):
    print(f"-- V={V} --")
    meas=[]; surr={K:[] for K in (2,3,4)}
    for m in MS:
        E=spectrum(metallic_word(m,1500),V)
        meas.append(high_peak_of(E))
        for K in (2,3,4):
            nd,wt=gauss_quadrature_dos(E,K)
            surr[K].append(high_peak_of(nd,wt))
    print(f"  measured : {[round(x,4) for x in meas]}")
    cm=classify(meas)
    print(f"    classifier(measured): e1/med={cm['e1_over_med']}")
    for K in (2,3,4):
        resid=[ms-su for ms,su in zip(meas,surr[K])]
        cr=classify(resid)
        cs=classify(surr[K])
        print(f"  K={K} surrogate: {[round(x,4) for x in surr[K]]}")
        print(f"    surrogate reproduces golden offset? classifier(surrogate): e1/med={cs['e1_over_med']}"
              f"   residual (meas-surr): {[round(r,4) for r in resid]}  classifier(residual): e1/med={cr['e1_over_med']} flag={cr['flag']}")
