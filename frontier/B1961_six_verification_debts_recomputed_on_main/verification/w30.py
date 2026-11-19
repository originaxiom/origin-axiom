# CLAIMS (SM seat W30): Q1 puncture -1 order 2 => no order-3 flux in any rep (Sym^n, parity twists);
# Q2 Heisenberg pairs in SU(3) with commutator w form ONE class; L,R,-I keep it; swap P sends to wbar class;
# P with complex conj keeps it; moves act on C^3 via SL(2,F3) order 24, 2+1; with bare -I order 216, commutant 1.
# EXPECT: Q1 holds trivially; Q2 holds in SU(3)/SL3 but NOT in GL3 (scalars free) ; image 24 and 2+1 hold; 216 uncertain.
import numpy as np, itertools, sympy as sp
np.set_printoptions(precision=4,suppress=True)
w=np.exp(2j*np.pi/3)
C=np.diag([1,w,w*w]); S=np.roll(np.eye(3),1,axis=0)  # |k>->|k+1>
inv=np.linalg.inv
comm=lambda A,B:A@B@inv(A)@inv(B)
print("comm(C,S)=w:",np.allclose(comm(C,S),w*np.eye(3)))
# Q1: [a,b]=-1 ; Sym^n of -I and parity twists
import sympy
for n in range(0,9):
    for par in (1,-1):
        M=sympy.Matrix([[-1,0],[0,-1]])
        # Sym^n of -I = (-1)^n I; twist sign par^? (character chi of SL2? -I has chi in {+1,-1} order<=2)
        val=(-1)**n*(par if True else 1)
        assert val in (1,-1)
print("Q1: image of -1 in Sym^n (x) chi has eigenvalue (-1)^n*(+-1) in {+1,-1}, n=0..8: never w. General: g^2=1 => rho(g)^2=1")
# Also: no rep of [a,b]=-1 with comm = w I: det/order
def inter(Ap,Bp,A=C,B=S):
    # solve U A = Ap U, U B = Bp U
    I=np.eye(3)
    M=np.vstack([np.kron(I,A.T)-np.kron(Ap,I) if False else np.kron(A.T,I)-np.kron(I,Ap),
                 np.kron(B.T,I)-np.kron(I,Bp)])  # vec row-major? use column-major below
    # column-major vec: vec(UA)=(A^T kron I)vec(U); vec(Ap U)=(I kron Ap)vec(U)
    u,s,vh=np.linalg.svd(M)
    null=[vh[i].conj() for i in range(9) if s[i]<1e-9]
    Us=[v.reshape(3,3,order='F') for v in null]
    return Us
# Q2 part a: pairs with comm w: A^3 scalar -> in SU(3) A^3=1, B^3=1. nine twists conjugate
ok=True
for i in range(3):
  for j in range(3):
    Us=inter(w**i*C,w**j*S)
    U=Us[0]
    print("twist",i,j,"intertwiner dim",len(Us),"invertible",abs(np.linalg.det(U))>1e-9)
# general SU(3): A^3 commutes with irreducible pair => scalar; also verify any pair with comm w is irreducible: Schur check
# (all such pairs: A^3 scalar c, det A =1 => c^3=1... A eigenvalues = l,wl,w^2 l => det = l^3, A^3 = l^3 =1)
print("SU3: A eigen set closed under w -> {l,wl,w^2 l}, det=l^3=1, so A^3=1; same B => 9 twists, all conjugate (above)")
# GL3 contrast: A=t*C, B=S has comm w, det A=t^3; conj class changes with t
for t in (1,2.0):
    print("GL3 pair (tC,S) comm w:",np.allclose(comm(t*C,S),w*np.eye(3)),"conj to (C,S) intertwiner dim",len(inter(t*C,S)))
# moves
K=np.conj
moves={
 'L':lambda A,B:(A,A@B),'R':lambda A,B:(A@B,B),'-I':lambda A,B:(inv(A),inv(B)),
 'P':lambda A,B:(B,A),'PK':lambda A,B:(K(B),K(A)),'K(plain conj)':lambda A,B:(K(A),K(B))}
for name,f in moves.items():
    dims=[]
    for i in range(3):
      for j in range(3):
        A,B=w**i*C,w**j*S
        Ap,Bp=f(A,B)
        cm=comm(Ap,Bp); sc=cm[0,0]
        isscal=np.allclose(cm,sc*np.eye(3))
        dims.append(len(inter(Ap,Bp)))
    print(name,"new commutator scalar",np.round(sc,4),"(w=%s, wbar=%s)"%(np.round(w,4),np.round(w.conjugate(),4)),"intertwiner dims over 9 twists:",sorted(set(dims)),"count",dims.count(1) )
# also generic SU(3) class check: all pairs in the class are the 9 twists; also check moves on twist-class keep within same-comm class (comm scalar value suffices)
# Image group: lifts of L,R normalised det 1
def lift(f):
    U=inter(*f(C,S))[0]; U=U/abs(np.linalg.det(U))**(1/3)
    d=np.linalg.det(U); U=U/(d**(1/3)); 
    return U
UL=lift(moves['L']); UR=lift(moves['R']); Um=lift(moves['-I'])
print("det UL,UR,U-I:",np.linalg.det(UL),np.linalg.det(UR),np.linalg.det(Um))
def gen(gs,limit=5000):
    key=lambda M:tuple(np.round(M.flatten(),5).tolist())
    els={key(np.eye(3,dtype=complex)):np.eye(3,dtype=complex)}; fr=[np.eye(3,dtype=complex)]
    while fr:
        nf=[]
        for x in fr:
            for g in gs:
                y=x@g
                k=key(y)
                if k not in els: els[k]=y; nf.append(y)
        fr=nf
        if len(els)>limit: return None
    return list(els.values())
def modscal(els):
    seen=set()
    for M in els:
        # normalise phase by first nonzero entry
        f=M.flatten(); a=f[np.argmax(abs(f)>1e-6)]; N=M/a*abs(a)
        seen.add(tuple(np.round(N.flatten(),4).tolist()))
    return len(seen)
def commutant(els):
    I=np.eye(3)
    rows=[np.kron(g.T,I)-np.kron(I,g) for g in els]
    s=np.linalg.svd(np.vstack(rows),compute_uv=False)
    return int(sum(s<1e-8))
def irrep_dims(els):
    # decompose: commutant dim d, sum of squares of multiplicities; plus invariant subspaces by averaging
    return commutant(els)
G=gen([UL,UR]); print("group <UL,UR> (det1 lifts) order",len(G),"mod scalars",modscal(G),"commutant",commutant(G))
# projective: take all products mod scalars check 24
print("phase-free image order (L,R):",modscal(G))
G2=gen([UL,UR,Um]); print("<UL,UR,U-I(det1 lift)> order",len(G2),"mod scalars",modscal(G2),"commutant",commutant(G2))
Pm=np.zeros((3,3));
for k in range(3): Pm[(-k)%3,k]=1
print("bare -I lift k->-k det",np.linalg.det(Pm), "intertwines -I:",np.allclose(Pm@C@inv(Pm),inv(C)) and np.allclose(Pm@S@inv(Pm),inv(S)))
G3=gen([UL,UR,Pm]); print("<UL,UR,bare(k->-k)> order",len(G3) if G3 else None,"mod scalars",modscal(G3) if G3 else None,"commutant",commutant(G3) if G3 else None)
G4=gen([UL,UR,Pm*np.linalg.det(Pm)**0]) 
# 2+1 decomposition for <UL,UR>: invariant subspace
els=G; Mavg=sum(els)/len(els)
# trace-character norm: <chi,chi> over group
chi=np.array([np.trace(g) for g in els]); print("<chi,chi> for <UL,UR>:",np.round(np.mean(abs(chi)**2),4),"(2 for 2+1 non-isomorphic; 1 irreducible)")
# find invariant 1-dim subspace: common eigenvector
M=sum(np.random.randn()*g for g in els)  # random combination in group algebra
ev,V=np.linalg.eig(M); 
inv1=[v for v in V.T if all(np.linalg.matrix_rank(np.c_[g@v,v],tol=1e-7)==1 for g in els)]
print("invariant lines found:",len(inv1))
# also the 24-element group: SL(2,3) check by orders of elements mod scalars
from collections import Counter
def order_mod_scal(M):
    X=M.copy()
    for n in range(1,13):
        if np.allclose(X,X[0,0]*np.eye(3)): return n
        X=X@M
    return None
print("element orders mod scalars (L,R group):",sorted(Counter(order_mod_scal(g) for g in G).items()))
print("dim of the 1-dim summand's action: even/odd functions: k->-k parity")
