# exact-action form-space solver (own code): dimension table by piece, then N10 on generic members
import numpy as np, sympy as sp, mpmath as mp, time
from math import comb
chit,chis=np.exp(2j*np.pi/24),np.exp(-1j*np.pi/4)
rt=np.diag([1j,1,1])@np.array([[1,0,0],[0,0,1],[0,1,0]]); rs=-1j*np.array([[0,0,1],[0,1,0],[1,0,0]])
rho_t=chit**21*rt; rho_s=chis**21*rs
X_,Y_,Z_=sp.symbols('X Y Z')
def monos(K): return [(a,b,K-a-b) for b in (0,1) for a in range(K-b+1)]
def reduce_poly(expr,K):
    # reduce Y^2 -> X^2+Z^2, return coefficient vector over monos(K)
    p=sp.Poly(sp.expand(expr),X_,Y_,Z_); ms=monos(K); idx={mm:i for i,mm in enumerate(ms)}; v=np.zeros(len(ms),dtype=complex)
    for (a,b,c),co in p.terms():
        m_,r=divmod(b,2)
        for j in range(m_+1):
            v[idx[(a+2*j,r,c+2*(m_-j))]]+=complex(co)*comb(m_,j)
    return v
def action_matrix(sub,K):
    ms=monos(K); n=len(ms); M=np.zeros((n,n),dtype=complex)
    for j,(a,b,c) in enumerate(ms):
        M[:,j]=reduce_poly(sp.sympify(sub[0])**a*sp.sympify(sub[1])**b*sp.sympify(sub[2])**c,K)
    return M  # (P o g) coefficient vector = M @ coefficient vector of P
def svdnull(A,tol=1e-9):
    u,s,vh=np.linalg.svd(A); r=int((s<tol).sum()) if A.shape[0]>=A.shape[1] else A.shape[1]-int((s>tol).sum())
    if A.shape[0]>=A.shape[1]: return vh[A.shape[1]-r:].conj().T, s
    rk=int((s>tol).sum()); return vh[rk:].conj().T, s
def form_space(R_t,R_s,K,phase_t,phase_s):
    n=len(monos(K)); MT=action_matrix((I_*X_ if False else sp.I*X_,Z_,Y_),K); MS=action_matrix((-sp.I*Z_,-sp.I*Y_,-sp.I*X_),K)
    rows=[]
    I9=np.eye(9)
    # unknown C (9 x n) row-major vec; (P_i o g) = C_i . (M c)?  P_i(g theta) = sum_m C_im (monomial_m o g) = (C M^T)_i . monomials
    for M,R,ph in ((MT,R_t,phase_t),(MS,R_s,phase_s)):
        # C M^T - ph R C = 0   ->  vec: kron(I9, M) vec(C) - ph kron(R, I_n) vec(C)  (row-major: (C M^T)_{i,:} = M C_{i,:}^T)
        rows.append(np.kron(I9,M)-ph*np.kron(R,np.eye(n)))
    A=np.vstack(rows)
    N,s=svdnull(A)
    return N,s,n
NW=60
def ser():
    t3=np.zeros(NW); t4=np.zeros(NW); s2=np.zeros(NW)
    for n in range(-12,13):
        e=2*n*n
        if e<NW: t3[e]+=1; t4[e]+=(-1)**n
    for n in range(0,12):
        e=4*(n*(n+1)//2)
        if e<NW: s2[e]+=1
    mul=lambda a,b: np.convolve(a,b)[:NW]
    Xs=np.zeros(NW); Xs[1:]=4*mul(s2,s2)[:NW-1]
    return Xs,mul(t3,t3),mul(t4,t4),mul
Xs,Ys,Zs,mul=ser()
def pw(b,e):
    r=np.zeros(NW); r[0]=1
    for _ in range(e): r=mul(r,b)
    return r
def cusp(N,K,order=3):
    ms=monos(K); n=len(ms); S=np.array([mul(mul(pw(Xs,a),pw(Ys,b)),pw(Zs,c))[:order] for a,b,c in ms])  # n x order
    rows=[]
    for i in range(9):
        for p in range(order):
            rows.append(N[i*n:(i+1)*n,:].T@S[:,p])
    A=np.array(rows); u,s,vh=np.linalg.svd(A); rk=int((s>1e-9).sum())
    return N@vh[rk:].conj().T
Pp=np.zeros((9,9))
for i in range(3):
    for j in range(3): Pp[3*i+j,3*j+i]=1
Pd=np.diag([1.0 if i==j else 0 for i in range(3) for j in range(3)]); Po=(np.eye(9)+Pp)/2-Pd; Pa=(np.eye(9)-Pp)/2
def pieces(V,n):
    out={}
    for nm,Pm in (("D",Pd),("O+",Po),("O-",Pa)):
        if V.shape[1]==0: out[nm]=0; continue
        cols=[(Pm@V[:,c].reshape(9,n)).reshape(-1) for c in range(V.shape[1])]
        s=np.linalg.svd(np.array(cols).T,compute_uv=False); out[nm]=int((s>1e-8).sum())
    return out
if __name__=="__main__":
    Rt=np.kron(rho_t.conj(),rho_t.conj()); Rs=np.kron(rho_s.conj(),rho_s.conj())
    table={}
    spaces={}
    for k in range(1,12,2):
        K=k+9
        N,s,n=form_space(Rt,Rs,K,chit**18,chis**18)
        sv=np.sort(s)
        Nc=cusp(N,K)
        d=pieces(Nc,n); d['total']=Nc.shape[1]; table[k]=d; spaces[k]=(Nc,n)
        print(f"TT k={k}: weakly-hol null {N.shape[1]}, with cusp {Nc.shape[1]}, pieces {d}",flush=True)
    want=dict(D=[0,0,1,1,2,2],Op=[1,1,2,2,3,3],Om=[0,1,1,2,2,3])
    print("B1635 table reproduced:",all(table[k]['D']==want['D'][i] and table[k]['O+']==want['Op'][i] and table[k]['O-']==want['Om'][i] for i,k in enumerate(range(1,12,2))))
    Rt2=np.kron(rho_t.conj(),rho_t); Rs2=np.kron(rho_s.conj(),rho_s)
    for k in (0,2,4,6):
        N,s,n=form_space(Rt2,Rs2,k,1,1) if False else (None,None,None)
    # TbT: eta power 0 -> phases 1
    for k in (0,2,4,6):
        N,s,n=form_space(Rt2,Rs2,k,1,1); d=pieces(N,n); d['total']=N.shape[1]; print(f"TbT k={k}: {d}")
    # ---- N10 on generic members (hi-precision evaluation)
    mp.mp.dps=40
    def thetas(tau,Nn=60):
        E=lambda x: mp.exp(1j*mp.pi*tau*x)
        t2=2*sum(E((n+mp.mpf(1)/2)**2) for n in range(Nn)); t3=1+2*sum(E(n*n) for n in range(1,Nn)); t4=1+2*sum((-1)**n*E(n*n) for n in range(1,Nn))
        return t2**2,t3**2,t4**2
    def eta(tau):
        q=mp.exp(2j*mp.pi*tau); return mp.exp(2j*mp.pi*tau/24)*mp.nprod(lambda k:1-q**k,[1,400])
    def E6(t): return 1-504*mp.nsum(lambda k: k**5*mp.exp(2j*mp.pi*t*k)/(1-mp.exp(2j*mp.pi*t*k)),[1,150])
    taus=[mp.mpc(.13,1.21),mp.mpc(-.31,.95),mp.mpc(.45,2.0),mp.mpc(.07,3.1),mp.mpc(-.22,1.6),mp.mpc(1.3,.7)]
    rng=np.random.default_rng(11)
    def Fmat(vec,K,tau,epow):
        X,Y,Z=thetas(tau); ms=monos(K); n=len(ms)
        mv=[X**a*Y**b*Z**c for a,b,c in ms]
        C=vec.reshape(9,n); out=mp.matrix(3,3)
        for i in range(9):
            out[i//3,i%3]=sum(mp.mpc(C[i,j])*mv[j] for j in range(n))/(eta(tau)**epow if epow else 1)
        return out
    for k,wt,dp in ((1,0,6),(3,0,6),(5,0,6)):
        Nc,n=spaces[k]; K=k+9
        for trial in range(2 if k>1 else 1):
            c=rng.normal(size=Nc.shape[1])+1j*rng.normal(size=Nc.shape[1]); vec=Nc@c
            vals=[]
            for t in taus:
                rat=mp.det(Fmat(vec,K,t,18))/(eta(t)**6*(E6(t)**((k-1)//2) if k==3 else 1))
                vals.append(rat)
            if k==5: 
                # weight-15-... : det weight 3k=15; /eta^6 -> weight 12 level one: show it is a combination of E4^3, Delta (2-dim)
                pass
            ref=vals[0]
            print(f"weight {k} generic member {trial}: det/(eta^6{' E6' if k==3 else ''}) = "+", ".join(mp.nstr(v,8) for v in vals[:4])+f"  spread {mp.nstr(max(abs(v/ref-1) for v in vals[:6]),3)}",flush=True)
    # weight 5: det/eta^6 is a level-one weight-12 form: test it lies in span{E4^3, Delta} using 4 taus -> fit 2 coeffs, residual on the rest
    E4=lambda t: 1+240*mp.nsum(lambda k: k**3*mp.exp(2j*mp.pi*t*k)/(1-mp.exp(2j*mp.pi*t*k)),[1,150])
    Nc,n=spaces[5]; c=rng.normal(size=Nc.shape[1])+1j*rng.normal(size=Nc.shape[1]); vec=Nc@c
    f=lambda t: mp.det(Fmat(vec,14,t,18))/eta(t)**6
    Dl=lambda t: eta(t)**24
    pts=taus
    A=mp.matrix([[E4(t)**3,Dl(t)] for t in pts]); b=mp.matrix([f(t) for t in pts])
    sol=mp.lu_solve(A,b)  # least squares
    print("weight5 det/eta^6 fit to a E4^3 + b Delta: coeffs",mp.nstr(sol[0],6),mp.nstr(sol[1],6),"max rel resid",mp.nstr(max(abs((A*sol-b)[i])/abs(b[i]) for i in range(len(pts))),3))
