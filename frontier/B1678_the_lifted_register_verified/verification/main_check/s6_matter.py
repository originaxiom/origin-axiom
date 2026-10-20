from lib import *
import random, numpy as np
random.seed(5);np.random.seed(5)
p0=(0,0)
Q0,_=compl(p0)
Qs={p:compl(p)[0] for p in P}
def m0rep(e):
    return Q0.conj().T@Dmat_cochain(p0,e)@Q0
Qp={(1,0):qj,(0,1):qi,(1,1):qk}
# F: C^3 (x) M0 -> V : e_p (x) [z] -> [Q_p z] in V_p
Fm=np.zeros((6,6),dtype=complex)
for ip,p in enumerate(P):
    for k in range(2):
        z=Q0[:,k]; za,zb=z[:2],z[2:]
        w=np.concatenate([Qp[p]@za,Qp[p]@zb])
        coords=Qs[p].conj().T@w   # class coords
        # check it's within complement-projection (no coboundary loss): residual should be a coboundary
        Fm[2*ip:2*ip+2,2*ip+k]=0  # placeholder
        Fm[2*ip:2*ip+2,2*ip+k]=coords
Finv=np.linalg.inv(Fm)
def nearest_kron(M):
    # M (6x6) as kron(N(3x3),m(2x2)): reshape
    R=M.reshape(3,2,3,2).transpose(0,2,1,3).reshape(9,4)
    u,s,vh=np.linalg.svd(R);return s
worst=0
for t in range(60):
    n=random.randint(1,6);e=(ID,np.eye(2,dtype=complex))
    for _ in range(n): e=Emul(e,GENS[random.choice(list(GENS))])
    Mv=Finv@Vrep(e)@Fm
    s=nearest_kron(Mv); worst=max(worst,s[1]/s[0])
print("max second/first singular value of reshaped F^-1 D_V F (0 => exact Kronecker):",worst)
# M0 characters
print("M0 action: generators commute & diagonalizable?")
Ms=[m0rep(GENS[n]) for n in ['L','Lb','R','Rb']]
print(" max commutator norm",max(np.abs(a@b-b@a).max() for a in Ms for b in Ms))
w,v=np.linalg.eig(Ms[0]+0.37*Ms[2]+0.11*Ms[1]+0.53*Ms[3])
for n,Mm in zip(['L','Lb','R','Rb'],Ms):
    d=np.linalg.inv(v)@Mm@v;print(" ",n,"diag chars",np.round(np.diag(d),4)," offdiag",abs(d[0,1])+abs(d[1,0]))
# e = Delta^2 J_c^-1
Delta=(L@Ri@L, gL@np.linalg.inv(gR)@gL)
c=(1,-2,-1,2)
Jcinv=(Aut(red(inv(c)+(1,)+c),red(inv(c)+(2,)+c)),np.linalg.inv(rho(c)))
e=Emul(Emul(Delta,Delta),Jcinv)
print("e=Delta^2 Jc^-1: g=",np.round(e[1],6).tolist())
d=np.linalg.inv(v)@m0rep(e)@v;print(" M0 chars of e:",np.round(np.diag(d),5),"offdiag",abs(d[0,1])+abs(d[1,0]))
# Y tensor
eps=np.array([[0,1],[-1,0]],dtype=complex)
C=[qj,qi,qk]
def Y(S,M): return np.array([[np.sum((C[a].T@eps@S@C[b])*M) for b in range(3)] for a in range(3)])
def rnd(): return np.random.randn(2,2)+1j*np.random.randn(2,2)
S,M=rnd(),rnd()
print("det Y = 4 detS detM tr(eps S M^T):",abs(np.linalg.det(Y(S,M))-4*np.linalg.det(S)*np.linalg.det(M)*np.trace(eps@S@M.T)))
err=0
for t in range(50):
    g=rnd(); g=g/np.sqrt(np.linalg.det(g))   # SL(2,C)
    Op=np.zeros((3,3),dtype=complex)
    # g C_b g^-1 = sum_a C_a O_ab : solve via trace form tr(C_a C_a')=-2 delta
    for a in range(3):
        for b in range(3):
            Op[a,b]=-np.trace(C[a]@g@C[b]@np.linalg.inv(g))/2
    err=max(err,np.abs(Y(g@S@np.linalg.inv(g),g@M@g.T)-Op@Y(S,M)@Op.T).max())
print("Y(S',M')=O Y O^T err over 50 SL2C:",err)
S0=np.array([[1,0],[0,0]],dtype=complex);M0=S0@np.linalg.inv(eps)
Y0=Y(S0,M0);print("Y0=",np.round(Y0,4).tolist(),"rank",np.linalg.matrix_rank(Y0),"trace",np.trace(Y0))
# 24 octahedral rotations: signed perm matrices det +1
rots=[]
for pm in itertools.permutations(range(3)):
    for sg in itertools.product([1,-1],repeat=3):
        Mx=np.zeros((3,3));
        for i in range(3): Mx[i,pm[i]]=sg[i]
        if abs(np.linalg.det(Mx)-1)<1e-9: rots.append(Mx)
avg=sum(O@Y0@O.T for O in rots)/len(rots)
print("#rots",len(rots)," avg=",np.round(avg,5).tolist())
Y1=Y(np.eye(2,dtype=complex),np.linalg.inv(eps));print("Y(I,eps^-1)=",np.round(Y1,4).tolist())
