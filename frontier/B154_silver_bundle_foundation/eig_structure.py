# Eigenvalue structure of the degree=rank sub-locus: meridian mu=A^-m t, longitude lam=[A,B], [A,B]=+-mu^k.
# Print eig(mu)=M, eig(lam)=L, check L=M^k, and test whether M_i are roots of unity (|M|=1, and M^N=1).
import numpy as np
# --- figure-eight construction (m=1): B=A^-2 t A t^-1, star=0, mu=A^-1 t ---
def fig_Bfrom(A,t): return np.linalg.inv(A@A)@t@A@np.linalg.inv(t)
def fig_star(A,t):
    Ai=np.linalg.inv(A); A2i=np.linalg.inv(A@A); return t@A2i@t@A - Ai@t@A@t
# --- silver construction (m=2): F1: tB^2=A^-1tA, F2: tB=A^2Bt, mu=A^-2 t ---
def silver_resid(A,B,t):
    Ai=np.linalg.inv(A); return np.concatenate([(t@B@B-Ai@t@A).reshape(-1),(t@B-A@A@B@t).reshape(-1)])
def newton_fig(A,rng,iters=300):
    n=A.shape[0]; t=rng.standard_normal((n,n))+1j*rng.standard_normal((n,n))
    for _ in range(iters):
        g=np.concatenate([fig_star(A,t).reshape(-1),[np.linalg.det(t)-1]]); 
        if np.max(np.abs(g))<1e-12: break
        if np.max(np.abs(g))>1e6: return None
        h=1e-7; tf=t.reshape(-1); J=np.zeros((g.size,n*n),complex)
        for k in range(n*n):
            tp=tf.copy(); tp[k]+=h; gp=np.concatenate([fig_star(A,tp.reshape(n,n)).reshape(-1),[np.linalg.det(tp.reshape(n,n))-1]]); J[:,k]=(gp-g)/h
        try: st,*_=np.linalg.lstsq(J,g,rcond=None)
        except: return None
        t=(tf-st).reshape(n,n)
    return t if np.max(np.abs(fig_star(A,t)))<1e-9 else None
def newton_silver(A,rng,iters=200):
    n=A.shape[0]; x=rng.standard_normal(2*n*n)+1j*rng.standard_normal(2*n*n); sp=lambda x:(x[:n*n].reshape(n,n),x[n*n:].reshape(n,n))
    for _ in range(iters):
        B,t=sp(x); g=np.concatenate([silver_resid(A,B,t),[np.linalg.det(B)-1,np.linalg.det(t)-1]])
        if np.max(np.abs(g))<1e-12: break
        if np.max(np.abs(g))>1e6: return None
        h=1e-7; J=np.zeros((g.size,2*n*n),complex)
        for k in range(2*n*n):
            xp=x.copy(); xp[k]+=h; Bp,tp=sp(xp); gp=np.concatenate([silver_resid(A,Bp,tp),[np.linalg.det(Bp)-1,np.linalg.det(tp)-1]]); J[:,k]=(gp-g)/h
        try: st,*_=np.linalg.lstsq(J,g,rcond=None)
        except: return None
        x=x-st
    B,t=sp(x); return (B,t) if np.max(np.abs(silver_resid(A,B,t)))<1e-9 else None
def root_of_unity_order(z,maxN=24):
    if abs(abs(z)-1)>1e-6: return None
    for N in range(1,maxN+1):
        if abs(z**N-1)<1e-6: return N
    return ">24"
def report(tag,A,B,t,m,kguess):
    mu=np.linalg.matrix_power(np.linalg.inv(A),m)@t; lam=A@B@np.linalg.inv(A)@np.linalg.inv(B)
    M=np.linalg.eigvals(mu); L=np.linalg.eigvals(lam)
    err=np.max(np.abs(np.sort_complex(L)-np.sort_complex(M**kguess)))
    print(f"  {tag}: k={kguess}  ||L-M^k||={err:.1e}")
    print(f"     |M|={np.round(np.abs(M),4)}  argM/2pi={np.round(np.angle(M)/(2*np.pi),4)}  ord(M)={[root_of_unity_order(z) for z in M]}")
    print(f"     |L|={np.round(np.abs(L),4)}  ord(L)={[root_of_unity_order(z) for z in L]}")
w=np.exp(2j*np.pi/3); i_=1j
print("=== meridian/longitude eigenvalue structure on the degree=rank sub-locus ===")
# figure-eight cases
for name,sp,kg in [("FIG {1,i,-i} o4",[1,i_,-i_],3),("FIG {1,w,w2} o3",[1,w,w**2],4)]:
    A=np.diag(np.array(sp,dtype=complex)); rng=np.random.default_rng(0)
    for s in range(150):
        t=newton_fig(A,rng)
        if t is None or np.linalg.cond(t)>1e4: continue
        B=fig_Bfrom(A,t); lam=A@B@np.linalg.inv(A)@np.linalg.inv(B); mu=np.linalg.inv(A)@t
        if np.max(np.abs(lam-np.linalg.matrix_power(mu,kg)))<1e-6: report(name,A,B,t,1,kg); break
# silver cases
for name,sp,kg in [("SILVER {1,w,w2} o3",[1,w,w**2],4),("SILVER {1,i,-i} o4",[1,i_,-i_],2)]:
    A=np.diag(np.array(sp,dtype=complex)); rng=np.random.default_rng(0)
    for s in range(200):
        r=newton_silver(A,rng)
        if r is None: continue
        B,t=r
        if np.linalg.cond(t)>1e4: continue
        lam=A@B@np.linalg.inv(A)@np.linalg.inv(B); mu=np.linalg.inv(A@A)@t
        if np.max(np.abs(lam-np.linalg.matrix_power(mu,kg)))<1e-6: report(name,A,B,t,2,kg); break
