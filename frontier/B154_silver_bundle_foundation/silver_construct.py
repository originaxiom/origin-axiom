"""Phase C step 3 — silver bundle SL(n) construction + degree=rank scan.

Silver bundle relations (R1: tAt^-1=A^3 B A^2 B, R2: tBt^-1=A^2 B) eliminate (R1+R2) to the clean
degree-2 system in (B,t) given A:
    F1:  t B^2 = A^-1 t A        (i.e. B^2 = t^-1 A^-1 t A)
    F2:  t B   = A^2 B t         (i.e. t B t^-1 = A^2 B)
{F1,F2} <=> {R1,R2}  (verified algebraically). Given A=diag(spectrum), Newton-solve (B,t) with
det B=det t=1, check irreducibility (Burnside) and the peripheral relation [A,B] vs (meridian)^k.

Validation: at SL(2), reps on the geometric component must give kappa=tr[A,B]=1/2 z^2+8/z^2-2 (B154).
Then SL(3)/SL(4): scan candidate A-spectra; which admit irreducible silver reps; is there a degree=rank
L=+-M^k relation, and what is k?
"""
from __future__ import annotations
import numpy as np

def silver_resid(A, B, t):
    Ai = np.linalg.inv(A)
    F1 = t @ B @ B - Ai @ t @ A
    F2 = t @ B - A @ A @ B @ t
    return np.concatenate([F1.reshape(-1), F2.reshape(-1)])

def newton_BT(A, rng, iters=600, detpin=True):
    n = A.shape[0]
    x = rng.standard_normal(2*n*n) + 1j*rng.standard_normal(2*n*n)
    def split(x): return x[:n*n].reshape(n,n), x[n*n:].reshape(n,n)
    for _ in range(iters):
        B,t = split(x)
        g = silver_resid(A,B,t)
        if detpin:
            g = np.concatenate([g, [np.linalg.det(B)-1, np.linalg.det(t)-1]])
        if np.max(np.abs(g)) < 1e-12: break
        h=1e-7; J=np.zeros((g.size, 2*n*n), complex)
        for k in range(2*n*n):
            xp=x.copy(); xp[k]+=h
            Bp,tp=split(xp)
            gp=silver_resid(A,Bp,tp)
            if detpin: gp=np.concatenate([gp,[np.linalg.det(Bp)-1,np.linalg.det(tp)-1]])
            J[:,k]=(gp-g)/h
        step,*_=np.linalg.lstsq(J,g,rcond=None); x=x-step
    B,t=split(x)
    return B,t, np.max(np.abs(silver_resid(A,B,t)))

def is_irred(A,B,rounds=6,tol=1e-7):
    n=A.shape[0]; gens=[A,B,np.linalg.inv(A),np.linalg.inv(B)]
    allm=[np.eye(n,dtype=complex)]; fr=[np.eye(n,dtype=complex)]
    for _ in range(rounds):
        fr=[g@m for m in fr for g in gens]; allm+=fr
    return np.linalg.matrix_rank(np.array([m.reshape(-1) for m in allm]),tol=tol)==n*n

def degree_rank(A,B,t):
    lam=A@B@np.linalg.inv(A)@np.linalg.inv(B); L=np.sort_complex(np.linalg.eigvals(lam))
    out={}
    for nm,mu in [('A^-1 t',np.linalg.inv(A)@t),('t',t),('t A^-1',t@np.linalg.inv(A))]:
        dt=np.linalg.det(t); best=(None,9e9)
        for k in range(1,10):
            for s in (1,-1):
                pred=np.sort_complex(s*np.linalg.eigvals(mu)**k/dt)
                err=np.max(np.abs(L-pred))
                if err<best[1]: best=((s,k),err)
        out[nm]=best
    return L,out

# ---------- validation at SL(2) ----------
print("=== SL(2) validation: silver construction must give kappa=1/2 z^2+8/z^2-2 on geometric reps ===")
rng=np.random.default_rng(0); got=0
for s in range(120):
    a = rng.standard_normal()+1j*rng.standard_normal()
    A=np.diag([a,1/a]).astype(complex)
    B,t,res=newton_BT(A,rng)
    if res<1e-9 and abs(np.linalg.det(t))>1e-3 and is_irred(A,B):
        z=np.trace(A@B); kap=np.trace(A@B@np.linalg.inv(A)@np.linalg.inv(B))
        f=0.5*z**2+8/z**2-2
        got+=1
        if got<=4:
            print(f"  rep{got}: res={res:.1e} z=trAB={z:.3f} kappa={kap:.4f} formula(1/2z^2+8/z^2-2)={f:.4f} match={abs(kap-f)<1e-6}")
    if got>=4: break
if not got: print("  (no irreducible SL(2) silver rep found -- construction may need structured seeds)")

# ---------- SL(3) spectrum scan ----------
print("\n=== SL(3) silver: scan candidate A-spectra for irreducible reps + degree=rank ===")
w=np.exp(2j*np.pi/3); i_=1j
specs3 = {
    "{1,1,1}":[1,1,1], "{1,w,w^2}":[1,w,w**2], "{1,i,-i}":[1,i_,-i_],
    "{1,-1,-1}":[1,-1,-1], "{w,w,w}":[w,w,w], "generic":[1.3+.2j,0.7-.1j,1/((1.3+.2j)*(0.7-.1j))],
}
for name,sp in specs3.items():
    sp=np.array(sp,dtype=complex); sp=sp/ (np.prod(sp))**(1/3)  # normalize det 1
    A=np.diag(sp)
    rng=np.random.default_rng(7); nirr=0; best_dr=(None,9e9); examples=0
    for s in range(80):
        B,t,res=newton_BT(A,rng)
        if res<1e-9 and abs(np.linalg.det(t))>1e-3 and np.linalg.cond(t)<1e4 and is_irred(A,B):
            nirr+=1
            L,out=degree_rank(A,B,t)
            for nm,(sk,err) in out.items():
                if err<best_dr[1]: best_dr=((nm,sk),err)
    print(f"  {name:12s}: irreducible reps {nirr}/80; best degree=rank L=s*M^k: {best_dr[0]} err={best_dr[1]:.2e}")
