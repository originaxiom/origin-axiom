import numpy as np, math
rng=np.random.default_rng(7)
def dot(X,Y): return np.sum(X*Y,axis=1)
def Gp(X,Y,v): return dot(v,Y)[:,None]*X + dot(v,X)[:,None]*Y - dot(X,Y)[:,None]*v
def inv_sqrt(K):
    e,U=np.linalg.eigh(K); return U@np.diag(e**-0.5)@U.conj().T
def crand(*s): return rng.normal(size=s)+1j*rng.normal(size=s)
N=300; a=crand(N); th=rng.normal(size=N)+0.3j*rng.normal(size=N)
R=a[:,None]*np.stack([np.ones(N),1j*np.cos(th),1j*np.sin(th)],1)
E4=1+0.3*crand(N); h=crand(N,3); c=rng.normal(size=(N,3))*3
X=[crand(N,3),R,crand(N,3)]; Y=[crand(N,3),E4[:,None]*R,crand(N,3)]   # C3/E4 analogue: left R (index 1), right E4 R (index 1)
KL=np.array([[np.sum(dot(X[i],np.conj(X[j]))) for j in range(3)] for i in range(3)])
KR=np.array([[np.sum(dot(Y[i],np.conj(Y[j]))) for j in range(3)] for i in range(3)])
A,B=inv_sqrt(KL),inv_sqrt(KR)
Ym=lambda v: np.array([[np.sum(dot(Gp(X[p],Y[q],v),np.conj(h))) for q in range(3)] for p in range(3)])
MR=A@Ym(R)@B.T; U,s,Vh=np.linalg.svd(MR); o=np.argsort(s); s3=s[o[2]]
u0,v0=U[:,o[0]],Vh[o[0],:].conj(); d=c*R
k_svd=abs(u0.conj()@(A@Ym(d)@B.T)@v0)/s3
closed=abs(np.sum(2*E4*dot(d,R)*dot(R,np.conj(h))))/(math.sqrt(KL[1,1].real)*math.sqrt(KR[1,1].real)*s3)
print('m2/m3',s[o[1]]/s3,' kappa SVD',k_svd,' closed form',closed, ' rel', abs(k_svd-closed)/closed)
