import numpy as np
exec(open("v1.py").read().split("# ---- 1.")[0])
gL,gR=W.gL,W.gR; ML,MR=W.ML,W.MR; TB=cp.TB
def blocks_action(m,g):
    A=np.zeros((6,6),dtype=complex)
    for i,u in enumerate(W.PAR):
        j=W.PAR.index(W.act_parity(m,u)); A[2*i:2*i+2,2*j:2*j+2]=g
    return A
Lm={"a":"a","b":"ab"}; Rm={"a":"ab","b":"b"}
St=om.compose(Rm,om.compose({"a":"a","b":"Ab"},Rm))
S6=blocks_action(St,gR@inv(gL)@gR); T6=blocks_action(Lm,gL)
TL=cp.restrict(ML,TB); TR=cp.restrict(MR,TB); ST=TR@inv(TL)@TR; TT=TL
def hom_dim(S1,T1,S2,T2):
    n=S1.shape[0];m=S2.shape[0]
    A=np.vstack([np.kron(S1.T,np.eye(m))-np.kron(np.eye(n),S2),np.kron(T1.T,np.eye(m))-np.kron(np.eye(n),T2)])
    s=np.linalg.svd(A,compute_uv=False); return int(sum(s<1e-9))
print("check S^2 central and (ST)^3=S^2 relation in L6 module:", np.allclose(np.linalg.matrix_power(S6@T6,3),S6@S6,atol=1e-8) or np.allclose(np.linalg.matrix_power(S6@T6,3),np.linalg.matrix_power(S6,2),atol=1e-8))
print("commutant dim of (S6,T6):",hom_dim(S6,T6,S6,T6))
for k in range(24):
    cS=np.exp(-1j*k*np.pi/4); cT=np.exp(1j*k*np.pi/12)
    h=hom_dim(cS*np.kron(ST,gR@inv(gL)@gR),cT*np.kron(TT,gL),S6,T6)
    if h: print("k",k,"Hom dim ((chi^k rho_T) x V2 -> L6) =",h)
# is the (S6,T6) module reproducing the W-module (ML,MR)? compare commutants / traces of random words
import itertools
print("group order of (S6,T6):",None)
