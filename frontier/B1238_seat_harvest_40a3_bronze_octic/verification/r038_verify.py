"""Independent check of codex R038: stabilizer dims/ranks of v = bar(e6) (x) s+ in the (bar6, 2) of su(6)+su(2),
the U(1)_H charges of 27 = Lambda^2 6 + (bar6,2), and the moment-map norms (D-terms) of the lone VEV."""
import numpy as np, itertools
rng=np.random.default_rng(1)
def su_basis(n):
    B=[]
    for i in range(n):
        for j in range(i+1,n):
            E=np.zeros((n,n),complex); E[i,j]=1; E[j,i]=-1; B.append(E)           # real antisymmetric
            E=np.zeros((n,n),complex); E[i,j]=1j; E[j,i]=1j; B.append(E)          # imaginary symmetric
    for i in range(n-1):
        E=np.zeros((n,n),complex); E[i,i]=1j; E[i+1,i+1]=-1j; B.append(E)         # traceless diagonal
    return B                                                                       # anti-hermitian, dim n^2-1
s6=su_basis(6); s2=su_basis(2); assert len(s6)==35 and len(s2)==3
# (bar6, 2): X in su(6) acts on bar6 by -X^T ; Y in su(2) acts on 2 by Y
e6=np.zeros(6,complex); e6[5]=1; sp=np.array([1,0],complex)
v=np.kron(e6,sp)                                # bar(e6) (x) s+
def act(X,Y): return np.kron(-X.T,np.eye(2))+np.kron(np.eye(6),Y)
def stab(basis_pairs):
    M=np.array([act(X,Y)@v for X,Y in basis_pairs]).T          # 12 x dim, complex
    Mr=np.vstack([M.real,M.imag])                              # the algebra is REAL: kernel over R
    _,s,vh=np.linalg.svd(Mr); null=vh[np.sum(s>1e-9):]
    return null
def rank_of(null, basis_pairs):
    # rank = dim of centralizer of a generic element inside the algebra (for a compact reductive algebra)
    mats=[sum(c*np.kron(X,np.eye(1)) for c,(X,Y) in zip(row,basis_pairs)) for row in null]  # su(6) parts
    mats2=[sum(c*Y for c,(X,Y) in zip(row,basis_pairs)) for row in null]
    g=rng.standard_normal(len(null)); Xg=sum(a*m for a,m in zip(g,mats)); Yg=sum(a*m for a,m in zip(g,mats2))
    C=np.array([np.concatenate([(Xg@m-m@Xg).ravel(),(Yg@m2-m2@Yg).ravel()]) for m,m2 in zip(mats,mats2)]).T
    return len(null)-np.linalg.matrix_rank(C,tol=1e-8)
pairs6=[(X,np.zeros((2,2))) for X in s6]
pairs62=pairs6+[(np.zeros((6,6)),Y) for Y in s2]
n6=stab(pairs6); n62=stab(pairs62)
print("stabilizer in su(6) alone: dim", len(n6), "rank", rank_of(n6,pairs6), "  (SU(5): 24, 4)")
print("stabilizer in su(6)+su(2): dim", len(n62), "rank", rank_of(n62,pairs62), "  (u(5): 25, 5)")
# the diagonal generator (2Y+5X, -5T_E) annihilates v; pure X does not
Yc=np.diag([-1/3,-1/3,-1/3,1/2,1/2,0]); Xc=np.diag([1/3,1/3,1/3,0,0,-1]); TE=np.diag([1,-1])
print("|(2Y+5X,-5T_E).v| =", np.linalg.norm(act(1j*(2*Yc+5*Xc),1j*(-5*TE))@v), "  |X.v| =", np.linalg.norm(act(1j*Xc,np.zeros((2,2)))@v), "  |Y.v| =", np.linalg.norm(act(1j*Yc,np.zeros((2,2)))@v))
# U(1)_H charges on the 27: Lambda^2 6 with H = 2Y+5X = diag(1,1,1,1,1,-5); (bar6,2) with -H^T (x) 1 + 1 (x) (-5 T_E)
H=2*Yc+5*Xc; h=np.diag(H).real
lam2=sorted(round(h[i]+h[j],6) for i,j in itertools.combinations(range(6),2))
from collections import Counter
print("Lambda^2 6 charges:", dict(Counter(lam2)))
te=np.diag(-5*TE)
b62=sorted(round(-h[i]+te[k],6) for i in range(6) for k in range(2))
print("(bar6,2) charges:", dict(Counter(b62)))
# moment maps of the lone VEV: traceless projections
V=v.reshape(6,2)                       # v as a 6x2 matrix (bar6 index, 2 index)
mu6=V@V.conj().T; mu6=mu6-np.trace(mu6)/6*np.eye(6)
mu2=V.T@V.conj(); mu2=mu2-np.trace(mu2)/2*np.eye(2)
print("||mu_su(6)||^2 =", round(np.trace(mu6@mu6.conj().T).real,6), "  ||mu_su(2)||^2 =", round(np.trace(mu2@mu2.conj().T).real,6))
# SM embedding inside the SU(5): 6 = (3,1)_{-1/3} + (1,2)_{1/2} + (1,1)_0 -- the SM generators lie in the first five coords
print("Y is supported on coords 1..5 and annihilates v:", abs(Yc[5,5])<1e-12 and np.linalg.norm(act(1j*Yc,np.zeros((2,2)))@v)<1e-12)
