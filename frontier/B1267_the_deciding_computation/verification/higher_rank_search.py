import numpy as np
from scipy.optimize import least_squares
inv=np.linalg.inv
def word(w,D):
    n=D['a'].shape[0]; M=np.eye(n,dtype=complex)
    for c in w: M=M@D[c]
    return M
def solve_rep(n,pa,pb,seed):
    k=n*n
    def resid(v):
        A=(v[0:k]+1j*v[k:2*k]).reshape(n,n); B=(v[2*k:3*k]+1j*v[3*k:4*k]).reshape(n,n); T=(v[4*k:5*k]+1j*v[5*k:6*k]).reshape(n,n)
        D={'a':A,'b':B}
        try:
            f=[np.linalg.det(A)-1,np.linalg.det(B)-1,np.linalg.det(T)-1]
            out=np.concatenate([np.array(f),(T@A-word(pa,D)@T).reshape(-1),(T@B-word(pb,D)@T).reshape(-1)])
            o=np.concatenate([out.real,out.imag]); return o if np.all(np.isfinite(o)) else np.ones(len(o))*9
        except Exception: return np.ones(2*(3+2*k))*9
    r=least_squares(resid,np.random.default_rng(seed).standard_normal(6*k)*0.8,max_nfev=2500,xtol=1e-13,ftol=1e-13)
    if np.max(np.abs(r.fun))>1e-9: return None
    A=(r.x[0:k]+1j*r.x[k:2*k]).reshape(n,n); B=(r.x[2*k:3*k]+1j*r.x[3*k:4*k]).reshape(n,n); T=(r.x[4*k:5*k]+1j*r.x[5*k:6*k]).reshape(n,n)
    words=[np.eye(n)]; cur=[np.eye(n)]
    for _ in range(2*n):
        nxt=[M@X for M in cur for X in (A,B)]
        words+=nxt; cur=nxt
        if np.linalg.matrix_rank(np.array([w.reshape(-1) for w in words]),tol=1e-7)==n*n: break
    if np.linalg.matrix_rank(np.array([w.reshape(-1) for w in words]),tol=1e-7)<n*n: return None
    return A,B,T
def h1(A,B,T,pa,pb):
    n=A.shape[0]; In=np.eye(n,dtype=complex)
    D={'a':A,'b':B,'t':T,'A':inv(A),'B':inv(B),'T':inv(T)}
    def fox(w,g):
        tot=np.zeros((n,n),dtype=complex); P0=np.eye(n,dtype=complex)
        for ch in w:
            if ch==g: tot=tot+P0
            elif ch==g.upper(): tot=tot-P0@D[ch]
            P0=P0@D[ch]
        return tot
    rev=lambda w:"".join(c.upper() if c.islower() else c.lower() for c in reversed(w))
    rels=["t"+"a"+"T"+rev(pa),"t"+"b"+"T"+rev(pb)]
    res=max(np.max(np.abs(word(r,D)-In)) for r in rels)
    d1=np.block([[fox(r,g) for g in ('a','b','t')] for r in rels])
    d0=np.vstack([D['a']-In,D['b']-In,D['t']-In])
    rk=lambda M,tol=1e-7:int((np.linalg.svd(M,compute_uv=False)>tol).sum())
    return (3*n-rk(d1))-rk(d0), res
print("HIGHER-RANK NON-SELF-DUAL SEARCH on m004 (rigidity was the rank-3 obstruction)\n",flush=True)
print(f"{'n':>2} {'reps':>5} {'non-self-dual':>14} {'h1!=0':>6}  (h1V,h1V*) seen                INDEX",flush=True)
for n in (2,3,4,5,6):
    got=nsd=live=0; pairs=set(); idx=set()
    for pa,pb in (("aab","ab"),("aba","ab")):
        for seed in range(25):
            R=solve_rep(n,pa,pb,seed)
            if R is None: continue
            A,B,T=R; got+=1
            if not (abs(np.trace(A)-np.trace(inv(A)))<1e-6 and abs(np.trace(B)-np.trace(inv(B)))<1e-6): nsd+=1
            hV,res=h1(A,B,T,pa,pb); hD,_=h1(inv(A).T,inv(B).T,inv(T).T,pa,pb)
            if res>1e-6: continue
            if hV!=0: live+=1
            pairs.add((hV,hD)); idx.add(hV-hD)
            if got>=10: break
        if got>=10: break
    print(f"{n:>2} {got:>5} {nsd:>14} {live:>6}  {sorted(pairs)}  {sorted(idx)}",flush=True)
print("\nlooking for: NON-SELF-DUAL and h1 != 0 -> a live index test",flush=True)
