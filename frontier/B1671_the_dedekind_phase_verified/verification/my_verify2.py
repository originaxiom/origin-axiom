import numpy as np, mpmath as mp, time, json
import my_verify as m
from my_verify import *
NW=40
def ser_theta():
    t3=np.zeros(NW); t4=np.zeros(NW); s2=np.zeros(NW)
    for n in range(-10,11):
        e=2*n*n   # q^{n^2/2} = w^{2 n^2}
        if e<NW: t3[e]+=1; t4[e]+=(-1)**n
    for n in range(0,10):
        e=4*(n*(n+1)//2)   # q^{n(n+1)/2} = w^{4*...}
        if e<NW: s2[e]+=1
    mul=lambda a,b: np.convolve(a,b)[:NW]
    Xs=np.zeros(NW); sq=mul(s2,s2); Xs[1:]=4*sq[:NW-1]
    return Xs,mul(t3,t3),mul(t4,t4),mul
Xs,Ys,Zs,mul=ser_theta()
def pw(b,e):
    r=np.zeros(NW); r[0]=1
    for _ in range(e): r=mul(r,b)
    return r
def mono_ser(a_,b_,c_): return mul(mul(pw(Xs,a_),pw(Ys,b_)),pw(Zs,c_))
def cusp_null(vecs,ms,order=3):
    n=len(ms); S=[mono_ser(*mm)[:order] for mm in ms]  # list of arrays (order,)
    rows=[]
    for i in range(9):
        for p in range(order):
            row=np.zeros(vecs.shape[0]*0+vecs.shape[1],dtype=complex)
            for col in range(vecs.shape[1]):
                v=vecs[i*n:(i+1)*n,col]; row[col]=sum(v[j]*S[j][p] for j in range(n))
            rows.append(row)
    A=np.array(rows); u,s,vh=np.linalg.svd(A); rank=int((s>1e-8*max(1,s[0])).sum())
    return vecs@vh[rank:].conj().T
def nullvecs(k,Rt_,Rs_,epow,K,tol=1e-9):
    s,vh,ms,n=solve(k,Rt_,Rs_,epow,K); r=int((s<tol).sum())
    gap=(s[-r-1] if r<len(s) else None, s[-r] if r>0 else None)
    return vh[len(s)-r:].conj().T, ms, n, r, gap
P=np.zeros((9,9))
for i in range(3):
    for j in range(3): P[3*i+j,3*j+i]=1
Pd=np.diag([1.0 if i==j else 0 for i in range(3) for j in range(3)]); Po=(np.eye(9)+P)/2-Pd; Pa=(np.eye(9)-P)/2
def pieces(V,n):
    out={}
    for nm,Pm in (("D",Pd),("O+",Po),("O-",Pa)):
        if V.shape[1]==0: out[nm]=0; continue
        cols=[(Pm@V[:,c].reshape(9,n)).reshape(-1) for c in range(V.shape[1])]
        s=np.linalg.svd(np.array(cols).T,compute_uv=False); out[nm]=int((s>1e-6).sum())
    return out
res={}
table={}
for k in range(1,12,2):
    t=time.time()
    V,ms,n,r,gap=nullvecs(k,Rt,Rs,18,k+9)
    Vc=cusp_null(V,ms) if r>0 else V
    d=pieces(Vc,n); d['total']=Vc.shape[1]; table[k]=d
    print(f"TT k={k}: pre-cusp null {r} (sv gap {gap}), with cusp {Vc.shape[1]}, pieces {d}  [{time.time()-t:.0f}s]",flush=True)
Rt2=np.kron(rho_t.conj(),rho_t); Rs2=np.kron(rho_s.conj(),rho_s)
table2={}
for k in (0,2,4,6):
    V,ms,n,r,gap=nullvecs(k,Rt2,Rs2,0,k)
    d=pieces(V,n); d['total']=V.shape[1]; table2[k]=d
    print(f"TbT k={k}: null {r} (gap {gap}) pieces {d}",flush=True)
want=dict(D=[0,0,1,1,2,2],Op=[1,1,2,2,3,3],Om=[0,1,1,2,2,3])
ok=all(table[k]['D']==want['D'][i] and table[k]['O+']==want['Op'][i] and table[k]['O-']==want['Om'][i] for i,k in enumerate(range(1,12,2)))
print("B1635 table reproduced by my solver:",ok)
# ---- N10 with my own weight-3 forms and weight-2 Dirac forms
E6=lambda t: 1-504*sum(kk**5*mp.exp(2j*mp.pi*t*kk)/(1-mp.exp(2j*mp.pi*t*kk)) for kk in range(1,80))
def mkform(Vc,ms,n,col): 
    return lambda t: (np.array(mvals(t,ms)) @ Vc[:,col].reshape(9,n).T).reshape(3,3)/complex(eta(t))**18
V3,ms3,n3,r3,_=nullvecs(3,Rt,Rs,18,12); V3c=cusp_null(V3,ms3)
print("weight3 dim",V3c.shape[1])
taus=[mp.mpc(.13,1.21),mp.mpc(-.31,.95),mp.mpc(.45,2.0),mp.mpc(.07,1.3),mp.mpc(-.22,1.6)]
rng2=np.random.default_rng(3)
spreads=[]
for trial in range(3):
    c=rng2.normal(size=V3c.shape[1])+1j*rng2.normal(size=V3c.shape[1]); vec=V3c@c
    F=lambda t: (np.array(mvals(t,ms3))@vec.reshape(9,n3).T).reshape(3,3)/complex(eta(t))**18
    # check covariance of the generic member and symmetric/antisym content
    rat=[np.linalg.det(F(t))/(complex(eta(t))**6*complex(E6(t))) for t in taus]
    spreads.append(max(abs(np.array(rat)/rat[0]-1)))
    print(f" generic weight-3 member {trial}: det/(eta^6 E6) at 5 tau = {np.round(rat,6)} spread {spreads[-1]:.2e}; symmetric? {np.abs(F(taus[0])-F(taus[0]).T).max():.2e}")
# Dirac weight 2 TbT
V2,ms2,n2,r2,_=nullvecs(2,Rt2,Rs2,0,2)
for trial in range(2):
    c=rng2.normal(size=V2.shape[1])+1j*rng2.normal(size=V2.shape[1]); vec=V2@c
    F=lambda t: (np.array(mvals(t,ms2))@vec.reshape(9,n2).T).reshape(3,3)
    rat=[np.linalg.det(F(t))/complex(E6(t)) for t in taus]
    print(f" generic weight-2 Dirac member {trial}: det/E6 = {np.round(rat,6)} spread {max(abs(np.array(rat)/rat[0]-1)):.2e}")
# phase law: theta_bar-related quantity 12 arg eta - pi x
dev=0
for x in np.linspace(-.5,.5,11):
    for y in (1.0,1.5,2.5,3.0):
        d=(12*float(mp.arg(eta(mp.mpc(x,y))))-np.pi*x+np.pi)%(2*np.pi)-np.pi; dev=max(dev,abs(d))
        if y==2.5: pass
    print("x=%.2f  y=1.0 dev %.2e  y=2.5 dev %.2e  (bound 12*2*exp(-2 pi y) = %.2e)"%(x,abs(((12*float(mp.arg(eta(mp.mpc(x,1.0))))-np.pi*x+np.pi)%(2*np.pi))-np.pi),abs(((12*float(mp.arg(eta(mp.mpc(x,2.5))))-np.pi*x+np.pi)%(2*np.pi))-np.pi),12*np.exp(-2*np.pi*2.5)))
print("max dev y>=1:",dev)
# theta_bar definition: arg det(Mu Md) with Mu=cu*Y(tau), Md=cd*Y(tau), Y weight1 => det = 64 cu^3 cd^3 eta^12 (3x3 dets)
x=.23; y=2.7; t=mp.mpc(x,y); X,Yv,Z=XYZ(t)
M=np.array([[0,complex(Z),complex(Yv)],[complex(Z),0,complex(X)],[complex(Yv),complex(X),0]])
print("arg det(Y1)^2 =",np.angle(np.linalg.det(M)**2),"  pi*x =",np.pi*x, " 12 arg eta =",12*float(mp.arg(eta(t))))
