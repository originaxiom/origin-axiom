from lib import *
from s2_group192 import closure, blk, Uleft
import numpy as np
def elements(mats,limit=5000):
    n=mats[0].shape[0];I=np.eye(n,dtype=complex)
    def key(M): return tuple(np.round(M.flatten(),5).view(float).round(4)+0.0)
    seen={key(I):I};fr=[I]
    while fr:
        new=[]
        for M in fr:
            for G in mats:
                N=M@G;k=key(N)
                if k not in seen: seen[k]=N;new.append(N)
        fr=new
    return list(seen.values())
def comm_dim(els,n):
    # dim of {X: gX=Xg for gens} via averaging: dim commutant = <chi,chi>
    return np.mean([abs(np.trace(g))**2 for g in els])
es=[GENS[n] for n in ['L','Lb','R','Rb']]
Vs=[Uleft(e) for e in es]; Ws=[Wrep(e) for e in es]
for lab,m in [("V",Vs),("W",Ws),("V+W",[blk(v,w) for v,w in zip(Vs,Ws)])]:
    els=elements(m); print(lab,"order",len(els),"<chi,chi> (=dim commutant)",round(comm_dim(els,0),4))
# parity signs on W present in W image?
Pa=np.kron(np.diag([-1,1,-1]) if False else np.diag([1,-1,-1]),np.eye(2))
# W-frame parity operator for chi_p(a): p ordering P=[(1,0),(0,1),(1,1)] -> chi(a)=-1,+1,-1
Pa=np.kron(np.diag([-1,1,-1]),np.eye(2)); Pb=np.kron(np.diag([1,-1,-1]),np.eye(2))
els=elements(Ws)
def inset(M,els): return any(np.abs(M-E).max()<1e-8 for E in els)
print("P_a in W image:",inset(Pa,els),"P_b:",inset(Pb,els),"; +-P_a:",inset(-Pa,els))
# Q8 inner lifts on W
for h,name in [((1,),'a'),((2,),'b')]:
    Jh=(Aut(red(h+(1,)+inv(h)),red(h+(2,)+inv(h))),rho(h))
    Aj=Wrep(Jh); print("A_J_%s = I3 (x) rho? "%name,np.abs(Aj-np.kron(np.eye(3),rho(h))).max()<1e-12)
