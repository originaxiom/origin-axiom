import numpy as np
# Fibonacci word via substitution a->ab, b->a   (w_{k+1}=w_k w_{k-1})
W={1:'a',2:'ab'}
for k in range(3,26): W[k]=W[k-1]+W[k-2]
def Mword(word,E,lam,va=1.0,vb=0.0):
    M=np.eye(2)
    for ch in word:
        V=lam*(va if ch=='a' else vb)
        M=np.array([[E-V,-1.0],[1.0,0.0]])@M     # gives M(uv)=M(v)M(u) => M_{k+1}=M_{k-1}M_k
    return M

print("=== A) TRACE-MAP DYNAMICS = the map whose invariant is kappa ===")
lam=1.0; E=0.7
Ms={k:Mword(W[k],E,lam) for k in range(1,9)}
# recursion M_{k+1}=M_{k-1} M_k ?
rec_ok=all(np.allclose(Ms[k+1],Ms[k-1]@Ms[k]) for k in range(2,8))
print(f"  matrix recursion  M_(k+1)=M_(k-1) M_k : {rec_ok}")
x={k:np.trace(Ms[k])/2 for k in range(1,9)}        # half-traces
tracemap_ok=all(abs(x[k+1]-(2*x[k]*x[k-1]-x[k-2]))<1e-9 for k in range(3,8))
print(f"  half-trace Fibonacci trace map  x_(k+1)=2 x_k x_(k-1) - x_(k-2) : {tracemap_ok}")

print("\n=== B) SUTO INVARIANT  and the bridge  kappa = 2 + lambda^2 ===")
def Ihalf(a,b,c): return a*a+b*b+c*c-2*a*b*c-1     # Suto invariant (half-traces)
print("  lambda | I=(half-trace invariant), several E and k  -> should equal lambda^2/4, const in E,k | kappa=2+4I")
for lam in [0.5,1.0,2.0,3.0]:
    vals=[]
    for E in [-1.3,0.0,0.55,1.2,2.1]:
        Ms={k:Mword(W[k],E,lam) for k in (5,6,7,8,9)}
        xx={k:np.trace(Ms[k])/2 for k in Ms}
        for k in (6,7,8):
            vals.append(Ihalf(xx[k-1],xx[k],xx[k+1]))
    vals=np.array(vals)
    print(f"   lam={lam}:  I = {vals.mean():.5f} ± {vals.std():.1e}   lambda^2/4 = {lam*lam/4:.5f}   kappa=2+4I = {2+4*vals.mean():.4f}   2+lam^2={2+lam*lam:.4f}")

print("\n=== C) SPECTRUM from the trace map: |sigma_k| = measure{E: |tr M_k(E)|<=2}  (Cantor set => ->0) ===")
def measure(k,lam,NE=400000):
    Es=np.linspace(-(2+lam)-0.05,(2+lam)+0.05,NE)
    tr=np.empty(NE)
    # vectorized transfer-matrix product over the word
    a=np.ones(NE); b=np.zeros(NE); c=np.zeros(NE); d=np.ones(NE)  # M=I as (a b;c d)
    for ch in W[k]:
        V=lam*(1.0 if ch=='a' else 0.0)
        # A=[[E-V,-1],[1,0]]; M_new=A@M
        na=(Es-V)*a - c; nb=(Es-V)*b - d; nc=a.copy(); nd=b.copy()
        a,b,c,d=na,nb,nc,nd
    tr=a+d
    inside=np.abs(tr)<=2.0
    return inside.mean()*(Es[-1]-Es[0]), int(np.sum(np.diff(inside.astype(int))==1))
print("  k (period F_{k+1}) | lambda=0(periodic) | lambda=0.5 | lambda=1 | lambda=2")
for k in [5,7,9,11,13,15]:
    row=[]
    for lam in [0.0,0.5,1.0,2.0]:
        m,nb=measure(k,lam); row.append(f"{m:.3f}")
    print(f"   k={k:2d} (F={len(W[k])}): "+"   ".join(f"{l}={r}" for l,r in zip(['λ0','λ.5','λ1','λ2'],row)))
print("\n  (λ=0 stays ~4 = full band [-2,2]; λ>0 measures shrink toward 0 = zero-measure Cantor set, Suto's theorem)")
