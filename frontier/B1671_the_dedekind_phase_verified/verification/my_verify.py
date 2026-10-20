# independent verification (own code): sympy identity, numeric covariance-based form spaces, N10, phase law
import numpy as np, sympy as sp, mpmath as mp, itertools, time
np.set_printoptions(precision=6)
T0=time.time()
# ---- (c1) symbolic identity, by an independent route: characteristic polynomial of H=Y Y^dagger, with Y complex symmetric zero-diag
a,b,c=sp.symbols('a b c'); ar,ai,br,bi,cr,ci=sp.symbols('ar ai br bi cr ci',real=True)
A=ar+sp.I*ai; B=br+sp.I*bi; C=cr+sp.I*ci
Y=sp.Matrix([[0,C,B],[C,0,A],[B,A,0]]); H=Y*Y.H
lam=sp.symbols('lam'); cp=sp.expand((H-lam*sp.eye(3)).det())
co=sp.Poly(cp,lam).all_coeffs()  # -lam^3 + e1 lam^2 - e2 lam + e3
e1=sp.expand(-co[1]*-1) if False else sp.expand(co[1]*-1*-1)
e1=sp.expand(co[1]); e2=sp.expand(-co[2]); e3=sp.expand(-co[3]) 
# cp = -lam^3 + e1 lam^2 - e2 lam + e3  => co=[-1,e1,-e2,e3]
print("char poly lead coeff",co[0]); e1=sp.expand(co[1]); e2=sp.expand(-co[2]); 
print("e1^2-4e2 =",sp.simplify(sp.expand(e1**2-4*e2)))
# and the equivalence: 16*Area^2-like product (s1+s2+s3)(-s1+s2+s3)(s1-s2+s3)(s1+s2-s3) = 4 e2 - e1^2 for s_i^2=lam_i
s1,s2,s3=sp.symbols('s1 s2 s3',positive=True)
ex=sp.expand((s1+s2+s3)*(-s1+s2+s3)*(s1-s2+s3)*(s1+s2-s3)-(4*(s1**2*s2**2+s1**2*s3**2+s2**2*s3**2)-(s1**2+s2**2+s3**2)**2))
print("Heron-type identity residual:",ex)
# zero-diag nonzero-case: det Y = 2abc
print("det Y =",sp.simplify(Y.det()-2*A*B*C))
# ---- numeric theta, eta
def thetas(tau,N=40):
    mp.mp.dps=30
    E=lambda x: mp.exp(1j*mp.pi*tau*x)   # q^x without branch ambiguity
    t2=2*sum(E((n+mp.mpf(1)/2)**2) for n in range(0,N)); t3=1+2*sum(E(n*n) for n in range(1,N)); t4=1+2*sum((-1)**n*E(n*n) for n in range(1,N))
    return t2,t3,t4
def eta(tau):
    q=mp.exp(2j*mp.pi*tau); return mp.exp(2j*mp.pi*tau/24)*mp.nprod(lambda k:1-q**k,[1,200])
def XYZ(tau):
    t2,t3,t4=thetas(tau); return t2**2,t3**2,t4**2
# check Jacobi theta2 t3 t4 = 2 eta^3 and det Y1 = 8 eta^6 with Y1 = [[0,Z,Y],[Z,0,X],[Y,X,0]]
for tau in [mp.mpc(0.13,1.21),mp.mpc(-0.31,0.95),mp.mpc(0.45,2.0)]:
    X,Yv,Z=XYZ(tau); M=mp.matrix([[0,Z,Yv],[Z,0,X],[Yv,X,0]])
    print("tau",tau,"det Y1/eta^6 =",mp.nstr(mp.det(M)/eta(tau)**6,15))
# ---- modular covariance of the triplet T=(X,Y,Z) with rho_u: f(t)=P34 diag(i,1,1)?? check numerically
tau=mp.mpc(0.21,1.1)
f=lambda t: mp.matrix(list(XYZ(t)))
rt=np.diag([1j,1,1])@np.array([[1,0,0],[0,0,1],[0,1,0]]); rs=-1j*np.array([[0,0,1],[0,1,0],[1,0,0]])
ft=np.array([complex(v) for v in f(tau+1)]); f0=np.array([complex(v) for v in f(tau)]); fs=np.array([complex(v) for v in f(-1/tau)])
print("T-covariance err",np.abs(ft-rt@f0).max(),"S-covariance err (weight 1)",np.abs(fs-complex(tau)*(rs@f0)).max())
# character of eta: eta(-1/tau)=sqrt(-i tau) eta ; eta(tau+1)=e^{2 pi i/24} eta
print("eta T:",complex(eta(tau+1)/eta(tau)),np.exp(2j*np.pi/24)," eta S ratio / (tau^{1/2}):",complex(eta(-1/tau)/eta(tau)/mp.sqrt(tau)),np.exp(-1j*np.pi/4))
chit,chis=np.exp(2j*np.pi/24),np.exp(-1j*np.pi/4)
rho_t=chit**21*rt; rho_s=chis**21*rs
print("det rhobar(t)^2 =",np.linalg.det(rho_t.conj())**2," chi_eta(t)^6=",chit**6)
print("det rhobar(s)^2 =",np.linalg.det(rho_s.conj())**2," chi_eta(s)^6=",chis**6)
# ---- own numeric form-space solver: Y(g tau) = (c tau+d)^k (rhobar x rhobar) Y(tau), Y = eta^-18 * sum coef * monomial
def monos(K): return [(a_,b_,K-a_-b_) for b_ in (0,1) for a_ in range(K-b_+1)]
Rt=np.kron(rho_t.conj(),rho_t.conj()); Rs=np.kron(rho_s.conj(),rho_s.conj())
rng=np.random.default_rng(7)
def mvals(tau,ms):
    X,Yv,Z=[complex(v) for v in XYZ(tau)]
    return np.array([X**a_*Yv**b_*Z**c_ for a_,b_,c_ in ms])
def nullspace_covariant(k,Rt,Rs,epow,npts=None):
    K=k+epow//2 if epow else k   # degree: weight k + 9 (eta^18 has weight 9) for epow=18; 
    ms=monos(K); n=len(ms); N=9*n; npts=npts or (N//9*2+30)
    rows=[]
    for _ in range(npts):
        t=mp.mpc(rng.uniform(-.5,.5),rng.uniform(0.9,1.4))
        Fe=lambda tt: (mvals(tt,ms)/complex(eta(tt))**epow if epow else mvals(tt,ms))
        f0=Fe(t); ft=Fe(t+1); fs=Fe(-1/t)
        # unknown coef matrix C (9 x n): Y(tau)=C f0 (vector 9)
        # T: C ft - Rt C f0 = 0 ; S: C fs - tau^k Rs C f0 =0
        # as linear in vec(C) (row-major): C f = kron(I9, f^T) vec(C)
        I9=np.eye(9)
        for (fa,fb,R,fac) in ((ft,f0,Rt,1),(fs,f0,Rs,complex(t)**k)):
            rows.append(np.kron(I9,fa[None,:])-fac*np.kron(R,fb[None,:]))
    A=np.vstack(rows); u,s,vh=np.linalg.svd(A,full_matrices=True)
    return vh,s,ms,n
# eta^18 factor: Y = eta^-18 P(X,Y,Z) with deg P = k+9
def solve(k,Rt_,Rs_,epow,K):
    ms=monos(K); n=len(ms); N=9*n; npts=int(N/9*1.3)+25
    rows=[]
    I9=np.eye(9)
    for _ in range(npts):
        t=mp.mpc(rng.uniform(-.5,.5),rng.uniform(0.92,1.5))
        e=lambda tt: complex(eta(tt))**epow if epow else 1.0
        f0=mvals(t,ms)/e(t); ft=mvals(t+1,ms)/e(t+1); fs=mvals(-1/t,ms)/e(-1/t)
        for (fa,fb,R,fac) in ((ft,f0,Rt_,1),(fs,f0,Rs_,complex(t)**k)):
            rows.append(np.kron(I9,fa[None,:])-fac*np.kron(R,fb[None,:]))
    A=np.vstack(rows); 
    # row scaling
    nr=np.linalg.norm(A,axis=1,keepdims=True); A=A[nr[:,0]>1e-12]; A=A/nr[nr[:,0]>1e-12]
    u,s,vh=np.linalg.svd(A); 
    return s,vh,ms,n
if __name__=="__main__":
    import sys
    k=1; s,vh,ms,n=solve(1,Rt,Rs,18,10)
    print("weight1 (before cusp) smallest singular values:",s[-6:], " count<1e-8:",(s<1e-8).sum(), "of", len(s))
