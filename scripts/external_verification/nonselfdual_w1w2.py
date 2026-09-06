"""THE DECIDING COMPUTATION named by B1260: h^1(M;V) vs h^1(M;V*) on B71's non-self-dual SL(3) components W1/W2.
Knot group as mapping torus: <a,b,t | t a t^-1 = phi(a), t b t^-1 = phi(b)>, phi: a->a^2 b, b->ab (B71 convention, w=a).
Peripheral: meridian mu = a^-1 t (B71), longitude lambda = [a,b] (fiber boundary).
Fox calculus, left-module convention; ranks by SVD gap (double precision; realizations from B71 are ~1e-9 accurate)."""
import sys, pathlib, numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))   # repo root
from frontier.B71_sl3_apoly import peripheral as per   # B71's realize / monodromy (own scripts of the repo, reused as the rep SOURCE only)

GENS = ['a','b','t']
PHI = {'a': ['a','a','b'], 'b': ['a','b']}
def inv(w): return [c.swapcase() for c in reversed(w)]
RELS = [ ['t','a','T'] + inv(PHI['a']),  ['t','b','T'] + inv(PHI['b']) ]
MU  = ['A','t']          # w^-1 t with w = a
LAM = ['a','b','A','B']  # [a,b]

def fox(word, x):
    terms=[]; prefix=[]
    for c in word:
        if c==x: terms.append((+1, list(prefix)))
        elif c==x.upper(): terms.append((-1, list(prefix)+[c]))
        prefix.append(c)
    return terms

def mat_word(rho, word):
    n=rho['a'].shape[0]; M=np.eye(n, dtype=complex)
    for c in word: M = M @ rho[c]
    return M

def full(ra, rb, rt):
    return {'a':ra,'b':rb,'t':rt,'A':np.linalg.inv(ra),'B':np.linalg.inv(rb),'T':np.linalg.inv(rt)}

def groupring(rho, terms, n):
    M=np.zeros((n,n),dtype=complex)
    for s,w in terms: M += s*mat_word(rho,w)
    return M

def rank(M, tol=1e-6, report=False):
    if M.size==0: return 0
    s=np.linalg.svd(M, compute_uv=False)
    r=int((s>tol*max(1.0, s[0] if len(s) else 1.0)).sum())
    if report: return r, s
    return r

def cochain(rho, gens, rels, n):
    I=np.eye(n)
    d0=np.vstack([rho[g]-I for g in gens])
    d1=np.block([[groupring(rho, fox(r,g), n) for g in gens] for r in rels])
    return d0,d1

def h1(rho, gens, rels, n):
    d0,d1=cochain(rho,gens,rels,n)
    z=np.max(np.abs(d1@d0))
    return (len(gens)*n - rank(d1)) - rank(d0), z

def cocycle_value(rho, f, word, n):
    val=np.zeros((n,1),dtype=complex); pref=[]
    for c in word:
        fc = f[c] if c.islower() else -(rho[c] @ f[c.lower()])
        val = val + mat_word(rho,pref) @ fc
        pref.append(c)
    return val

def kernel_basis(M, tol=1e-6):
    U,s,Vh=np.linalg.svd(M)
    n=M.shape[1]; k=int((s>tol*max(1.0,s[0])).sum()) if len(s) else 0
    return [Vh.conj().T[:,i:i+1] for i in range(k,n)]

def report(ra, rb, rt, label):
    n=ra.shape[0]; out={}
    for tag,(xa,xb,xt) in [('V',(ra,rb,rt)),('V*',(np.linalg.inv(ra).T,np.linalg.inv(rb).T,np.linalg.inv(rt).T))]:
        rho=full(xa,xb,xt)
        hv,z=h1(rho,GENS,RELS,n)
        mu=mat_word(rho,MU); lam=mat_word(rho,LAM)
        comm=np.max(np.abs(mu@lam-lam@mu))
        rhoT={'a':mu,'b':lam,'A':np.linalg.inv(mu),'B':np.linalg.inv(lam)}
        hT,_=h1(rhoT,['a','b'],[['a','b','A','B']],n)
        d0T,_=cochain(rhoT,['a','b'],[['a','b','A','B']],n)
        h0T=n-rank(d0T)
        d0,d1=cochain(rho,GENS,RELS,n)
        Z=kernel_basis(d1)
        cols=[]
        for zv in Z:
            f={'a':zv[0:n],'b':zv[n:2*n],'t':zv[2*n:3*n]}
            cols.append(np.vstack([cocycle_value(rho,f,MU,n), cocycle_value(rho,f,LAM,n)]))
        resmat=np.hstack(cols+[d0T]) if cols else d0T
        rres=rank(resmat)-rank(d0T)
        out[tag]=dict(h1=hv,h1T=hT,h0T=h0T,rres=rres,d1d0=z,comm=comm)
    N=out['V']['h1']-out['V*']['h1']
    lemma = (N == out['V']['rres']-out['V']['h0T'])
    print(f"  {label:44s} h1(V)={out['V']['h1']} h1(V*)={out['V*']['h1']} N={N:+d} | h0(dM;V)={out['V']['h0T']} h0(dM;V*)={out['V*']['h0T']} h1(dM;V)={out['V']['h1T']} | res rank V={out['V']['rres']} V*={out['V*']['rres']} | lemma {'OK' if lemma else 'VIOLATED'} | |d1d0|={out['V']['d1d0']:.1e} |[mu,lam]|={out['V']['comm']:.1e}")
    return N, out


def monodromy_generic(A_, B_, tol=1e-6):
    """own solver: X with X A X^-1 = phi(A), X B X^-1 = phi(B); tries both B71 word conventions; returns (X, res, convention)."""
    n=A_.shape[0]; I=np.eye(n)
    for conv,(PA,PB) in {"a->a^2b,b->ab (w=a)":(A_@A_@B_, A_@B_), "a->aba,b->ab (w=aba)":(A_@B_@A_, A_@B_)}.items():
        E=np.vstack([np.kron(I,A_.T)-np.kron(PA,I), np.kron(I,B_.T)-np.kron(PB,I)])
        U,s,Vh=np.linalg.svd(E)
        X=Vh.conj().T[:,-1].reshape(n,n)          # row-major vec
        d=np.linalg.det(X)
        if abs(d)<1e-12: continue
        X=X/d**(1.0/n)
        res=np.max(np.abs(X@A_@np.linalg.inv(X)-PA))+np.max(np.abs(X@B_@np.linalg.inv(X)-PB))
        if res<tol: return X,res,conv
    return None,None,None

def sym2(g):
    a,b,c,d=g[0,0],g[0,1],g[1,0],g[1,1]
    return np.array([[a*a, 2*a*b, b*b],[a*c, a*d+b*c, b*d],[c*c, 2*c*d, d*d]],dtype=complex)

print("=== validation: the geometric fiber holonomy = the Anosov fixed character (x,y,z)=(zbar,z,z), z=(3+sqrt(-3))/2 ===")
zc=(3+1j*np.sqrt(3))/2; x_,y_,z_=np.conj(zc),zc,zc
lam_=(x_+np.sqrt(x_*x_-4))/2
a2=np.array([[lam_,0],[0,1/lam_]],dtype=complex)
# b: tr b = y, tr(ab) = z, det 1, b12 = 1
b11=(z_-y_/lam_)/(lam_-1/lam_); b22=y_-b11; b12=1.0; b21=(b11*b22-1)/b12
b2=np.array([[b11,b12],[b21,b22]],dtype=complex)
comm2=a2@b2@np.linalg.inv(a2)@np.linalg.inv(b2)
print(f"  tr a={np.trace(a2):.4f} tr b={np.trace(b2):.4f} tr ab={np.trace(a2@b2):.4f} tr[a,b]={np.trace(comm2):.4f} (parabolic cusp: -2)")
for name,(A_,B_) in [("Sym^1 (the SL2 fiber holonomy)",(a2,b2)),("Sym^2 (geometric SL3, self-dual)",(sym2(a2),sym2(b2)))]:
    t_,res,conv=monodromy_generic(A_,B_)
    if t_ is None: print("  monodromy not found for",name); continue
    print(f"  monodromy residual {res:.1e} [{conv}]")
    assert conv.startswith('a->a^2b'), 'convention mismatch with RELS/MU'
    for zeta in ([1, np.exp(2j*np.pi/3)] if A_.shape[0]==3 else [1,-1]):
        report(A_,B_,zeta*t_, f"{name}, t*={zeta:.2f}")

print("\n=== W1 / W2 / V0 at generic (p,q): expect N=0 trivially when the cusp has no fixed vectors ===")
rng=np.random.default_rng(1)
for name,fn in [("W1",per.W1),("W2",per.W2),("V0",per.V0)]:
    for k in range(3):
        p=complex(rng.standard_normal(),rng.standard_normal()); q=complex(rng.standard_normal(),rng.standard_normal())
        out=per.realize(fn(p,q))
        if out is None: print("  realize failed",name,p,q); continue
        A_,B_=out; t_,res,conv=monodromy_generic(A_,B_)
        if t_ is None or not conv.startswith('a->a^2b'): print("  no monodromy in convention 1",name,conv); continue
        report(A_,B_,t_, f"{name} p={p:.2f} q={q:.2f}")

print("\n=== W1 / W2 on the locus where the meridian mu = a^-1 t has eigenvalue 1 (cusp-fixed vectors exist) ===")
from scipy.optimize import fsolve
def mu_of(fn,p,q):
    out=per.realize(fn(p,q))
    if out is None: return None
    A_,B_=out; t_,res,conv=monodromy_generic(A_,B_)
    if t_ is None or not conv.startswith('a->a^2b'): return None
    return A_,B_,t_, np.linalg.inv(A_)@t_
def det_mu_minus_I(fn,p,q):
    r=mu_of(fn,p,q)
    if r is None: return None
    return np.linalg.det(r[3]-np.eye(3))
from scipy.optimize import fsolve, minimize
def realize_near(coords, B0):
    """B71's realization but started from a nearby solution B0 (continuity across the sheet)."""
    x1,x2,x3,x4,x5,x6,x7,x8=(complex(c) for c in coords)
    roots=np.roots([1,-x1,x4,-1]); A=np.diag(roots).astype(complex); Ai=np.diag(1.0/roots).astype(complex)
    def resid(v):
        B=(v[:9]+1j*v[9:]).reshape(3,3); adjB=per._adjugate(B)
        e=np.array([np.trace(B)-x2,np.trace(A@B)-x3,np.trace(Ai@B)-x6,np.trace(adjB)-x5,np.trace(A@adjB)-x7,np.trace(Ai@adjB)-x8,np.linalg.det(B)-1.0,B[0,1]-1.0,B[1,2]-1.0],dtype=complex)
        return np.concatenate([e.real,e.imag])
    sol,info,ier,msg=fsolve(resid,np.concatenate([B0.real.ravel(),B0.imag.ravel()]),full_output=True)
    if ier==1 and np.max(np.abs(resid(sol)))<1e-9: return A,(sol[:9]+1j*sol[9:]).reshape(3,3)
    return None
def periph(A_,B_):
    t_,res,conv=monodromy_generic(A_,B_)
    if t_ is None or not conv.startswith('a->a^2b'): return None
    mu=np.linalg.inv(A_)@t_; lam=A_@B_@np.linalg.inv(A_)@np.linalg.inv(B_)
    return t_,mu,lam
def objective(A_,B_):
    r=periph(A_,B_)
    if r is None: return None
    t_,mu,lam=r
    Sm=np.vstack([np.linalg.matrix_power(mu,3)-np.eye(3), lam-np.eye(3)])   # joint fixed vectors of (zeta*mu for some zeta) and lambda
    return np.linalg.svd(Sm,compute_uv=False)[-1]
for name,fn in [("W1",per.W1),("W2",per.W2)]:
    rng=np.random.default_rng(3); hits=0; attempts=0
    while hits<3 and attempts<8:
        attempts+=1
        p=complex(rng.standard_normal(),rng.standard_normal())
        grid=[]
        for qr in np.linspace(-2.5,2.5,9):
            for qi in np.linspace(-2.5,2.5,9):
                q=complex(qr,qi); out=per.realize(fn(p,q))
                if out is None: continue
                f=objective(*out)
                if f is not None: grid.append((f,q,out[1]))
        grid.sort(key=lambda x:x[0])
        done=False
        for f0,q0,B0 in grid[:4]:
            state={'B':B0}
            def F(v):
                q=complex(v[0],v[1]); out=realize_near(fn(p,q),state['B'])
                if out is None: return 10.0
                state['B']=out[1]; f=objective(*out)
                return 10.0 if f is None else f
            res=minimize(F,[q0.real,q0.imag],method='Nelder-Mead',options={'xatol':1e-12,'fatol':1e-14,'maxiter':600})
            if res.fun<1e-7:
                q=complex(res.x[0],res.x[1]); out=realize_near(fn(p,q),state['B']); A_,B_=out; t_,mu,lam=periph(A_,B_)
                comm=A_@B_@np.linalg.inv(A_)@np.linalg.inv(B_)
                print(f"  [{name}] p={p:.3f} q={q:.5f}  sigma_min={res.fun:.1e}  eig(mu)={np.round(np.linalg.eigvals(mu),3)}  eig(lambda)={np.round(np.linalg.eigvals(lam),3)}  tr[A,B]={np.trace(comm):.3f}")
                for zeta in [1,np.exp(2j*np.pi/3),np.exp(-2j*np.pi/3)]:
                    report(A_,B_,zeta*t_,f"   {name} on the cusp-fixed-vector locus, t*={zeta:.2f}")
                hits+=1; done=True; break
        if not done: print(f"  [{name}] p={p:.3f}: no point of the locus found from 4 starts (best sigma_min {grid[0][0] if grid else 'n/a'})")
