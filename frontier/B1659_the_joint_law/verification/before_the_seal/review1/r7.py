import numpy as np
I=1j
qi=np.array([[I,0],[0,-I]]);qj=np.array([[0,1],[-1,0]],dtype=complex);qk=qi@qj
C=[qj,qi,qk];E=qj
def Y(S,M): return np.array([[np.sum((a.T@E@S@b)*M) for b in C] for a in C])
rng=np.random.default_rng(1)
rc=lambda *s: rng.normal(size=s)+1j*rng.normal(size=s)
pol=lambda A,B: np.linalg.det(A+B)-np.linalg.det(A)-np.linalg.det(B)
S=rc(2,2);M=rc(2,2)
print(np.trace(E@S@M.T), pol(S,M@E), pol(S,E@M), pol(S,M@np.linalg.inv(E)))
# with N = M E^{-1}...: detY = 4 detS detM ell ; ell = -pol(S, M E)/? 
# Does Y(S,M) have a symmetry Y(S,M)= T Y(N-version) : test Z(S,N)=Y(S, N E^-1) vs Z(N,S)
Ei=np.linalg.inv(E)
Z=lambda S,N: Y(S,N@Ei)
S=rc(2,2);N=rc(2,2)
print(np.linalg.norm(Z(S,N)-Z(N,S)),np.linalg.norm(Z(S,N)-Z(N,S).T))
# solve linear for T,T' : Z(S,N)=T Z(N,S) T' by alternating over many samples
samp=[(rc(2,2),rc(2,2)) for _ in range(60)]
A_=np.array([Z(a,b).ravel() for a,b in samp]);B_=np.array([Z(b,a).ravel() for a,b in samp])
# Kronecker form: vec(Z)=(T kron T'^T) vec(Z') ; general 9x9 linear map K on vec (relaxation)
K,res,rk,sv=np.linalg.lstsq(B_,A_,rcond=None)
print("general 9x9 linear relax residual",np.linalg.norm(B_@K-A_)/np.linalg.norm(A_), "rank of data",rk)
