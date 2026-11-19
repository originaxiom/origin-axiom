"""p156 -- independent check of B1606's premises (debt P-156).
CLAIMS AS STATED (B1606 / B1655 / SM seat W22):
 (i)  index = dimLambda+ - 3 is odd, never 0, for conditions the moves keep: values -3,-1,+1,+3; it is +-3 when the
      end condition keeps the parity grading.
 (ii) index = dim Lambda+ - 3 (Riemann-Roch, taken as stated by the seat).
 (iii) the M_{1,2} identification.
EXPECTED: moves-only group on C^6 has commutant 2, invariant subspaces dims 0,2,4,6 ; with grading irreducible so 0,6 only;
 -1 in group so all even dims. (ii) I can only test arithmetic consistency, not Riemann-Roch. (iii) not computable beyond
 chi facts.
METHOD (own construction, not the seat's): rho(a)=i, rho(b)=j (Q8). Block p (a nonzero parity character chi_p of F2->Z2^2)
 carries W_p = chi_p (x) rho on C^2. For an automorphism phi find g with g rho(x) g^-1 = rho(phi x) (solved linearly), and
 build the 6x6 lift as the block-monomial matrix with g in block (p, q) where chi_q o phi = chi_p (the parity permutation).
 Verify numerically that it is a genuine intertwiner W -> W o phi.  No u_p twists are used (they are a block-diagonal
 change of basis, shown here to give the same group up to conjugation).
"""
import numpy as np, itertools, json
np.set_printoptions(precision=4, suppress=True, linewidth=150)
I2=np.eye(2,dtype=complex)
qi=np.array([[1j,0],[0,-1j]]); qj=np.array([[0,1],[-1,0]],dtype=complex); qk=qi@qj
rho={'a':qi,'b':qj}
# words: dict letter -> word as list of (letter, +-1)
PHI={'L':{'a':[('a',1)],'b':[('a',1),('b',1)]},
     'R':{'a':[('a',1),('b',1)],'b':[('b',1)]},
     'S':{'a':[('a',-1)],'b':[('b',-1)]}}   # sign move a->a^-1,b->b^-1
def rho_word(w):
    M=I2.copy()
    for l,e in w:
        M=M@(rho[l] if e==1 else np.linalg.inv(rho[l]))
    return M
def ab_count(w): # parity (exponent sums mod 2)
    return (sum(1 for l,e in w if l=='a')%2, sum(1 for l,e in w if l=='b')%2)
PAR=[(1,0),(0,1),(1,1)]
def chi(p,l): return -1 if p[0 if l=='a' else 1]==1 else 1
def Wgen(p,l): return chi(p,l)*rho[l]
def find_g(phi):
    # solve g rho(x) = rho(phi x) g for x=a,b
    rows=[]
    for x in 'ab':
        R=rho[x]; Rp=rho_word(PHI[phi][x])
        rows.append(np.kron(R.T,np.eye(2))-np.kron(np.eye(2),Rp))  # vec (row-major? use column-major)
    # use column-major vec: vec(AXB)=(B^T kron A)vec(X): g R - Rp g =0 -> (R^T kron I - I kron Rp) vec g
    A=np.vstack(rows); u,s,vh=np.linalg.svd(A)
    null=[vh[i].conj() for i in range(len(s)) if s[i]<1e-9]
    assert len(null)==1,len(null)
    g=null[0].reshape(2,2,order='F'); g=g/np.sqrt(abs(np.linalg.det(g)))
    d=np.linalg.det(g); g=g/np.sqrt(d) if abs(d-1)>1e-9 else g
    assert np.allclose(g.conj().T@g,I2) and abs(np.linalg.det(g)-1)<1e-9
    assert all(np.allclose(g@rho[x],rho_word(PHI[phi][x])@g) for x in 'ab')
    return g
G={m:find_g(m) for m in PHI}
def parity_image(phi,p): # chi_p o phi as a parity: value on a,b
    return tuple(0 if np.prod([chi(p,l) for l,e in PHI[phi][x]])==1 else 1 for x in 'ab')
def Wfull(x): # W(x) on C^6
    M=np.zeros((6,6),complex)
    for i,p in enumerate(PAR): M[2*i:2*i+2,2*i:2*i+2]=Wgen(p,x)
    return M
def Wphi(phi,x): # W(phi(x))
    M=np.zeros((6,6),complex)
    for i,p in enumerate(PAR):
        B=I2.copy()
        for l,e in PHI[phi][x]:
            B=B@(Wgen(p,l) if e==1 else np.linalg.inv(Wgen(p,l)))
        M[2*i:2*i+2,2*i:2*i+2]=B
    return M
def lift(phi,c=(1,1,1),direction=+1):
    M=np.zeros((6,6),complex)
    for ip,p in enumerate(PAR):
        q=parity_image(phi,p); iq=PAR.index(q)
        if direction==+1: M[2*ip:2*ip+2,2*iq:2*iq+2]=c[ip]*G[phi]
        else:             M[2*iq:2*iq+2,2*ip:2*ip+2]=c[ip]*G[phi]
    return M
for phi in PHI:
    for d in (+1,-1):
        A=lift(phi,direction=d)
        ok1=all(np.allclose(A@Wfull(x),Wphi(phi,x)@A) for x in 'ab')
        ok2=all(np.allclose(A@Wphi(phi,x),Wfull(x)@A) for x in 'ab')
        print(f"lift {phi} dir {d:+d}: unitary={np.allclose(A.conj().T@A,np.eye(6))}  A W(x)=W(phi x)A: {ok1} ; A W(phi x)=W(x) A: {ok2}")
print("parity permutations: L",[PAR.index(parity_image('L',p)) for p in PAR],"R",[PAR.index(parity_image('R',p)) for p in PAR])
def key(M): return tuple(np.round(M.flatten().view(float),5)+0.0)
def group(gens,cap=4000):
    I=np.eye(6,dtype=complex); seen={key(I):I}; fr=[I]
    while fr:
        M=fr.pop()
        for g in gens:
            N=M@g; k=key(N)
            if k not in seen:
                seen[k]=N; fr.append(N)
                if len(seen)>cap: raise RuntimeError('big')
    return list(seen.values())
def commutant_basis(gens):
    A=np.vstack([np.kron(np.eye(6),g)-np.kron(g.T,np.eye(6)) for g in gens])
    u,s,vh=np.linalg.svd(A); n=int(sum(x<1e-8 for x in s))
    return [vh[-1-i].conj().reshape(6,6,order='F') for i in range(n)]
def classify(gens,seed=0):
    """commutant dim, isotypic dims from a generic hermitian commutant element, whether commutant is commutative"""
    B=commutant_basis(gens); n=len(B)
    rng=np.random.default_rng(seed)
    X=sum(rng.normal()*b+rng.normal()*b.conj().T for b in B)
    X=X+X.conj().T
    w,v=np.linalg.eigh(X); groups=[]; 
    i=0
    while i<6:
        j=i
        while j+1<6 and abs(w[j+1]-w[i])<1e-7: j+=1
        groups.append((j-i+1,v[:,i:j+1])); i=j+1
    comm=all(np.allclose(a@b,b@a) for a in B for b in B)
    inv=all(np.allclose(g@S@np.linalg.pinv(S) @ np.eye(6) if False else (np.linalg.matrix_rank(np.hstack([g@S,S]),tol=1e-7)==S.shape[1]),True) for g in gens for _,S in groups)
    return n,[d for d,_ in groups],comm,inv,groups
GL,GR,GS=lift('L'),lift('R'),lift('S')
grading=[np.diag(np.repeat([1 if k==j else -1 for k in range(3)],2)).astype(complex) for j in range(3)]
print("\n== (i) moves only: L,R lifts ==")
Gm=group([GL,GR]); n,dims,comm,inv,groups=classify([GL,GR])
print("order",len(Gm),"commutant dim",n,"isotypic dims",dims,"commutative",comm,"pieces invariant",inv)
subs=sorted({sum(c) for r in range(len(dims)+1) for c in itertools.combinations(dims,r)})
print("invariant-subspace dims (sums of the multiplicity-free pieces)",subs,"indices dim-3:",[d-3 for d in subs])
print("-1 in group:",any(np.allclose(g,-np.eye(6)) for g in Gm))
# pieces: identify symmetric piece
for d,S in groups:
    # is the piece = vectors (v,v,v)? check
    sym=np.vstack([np.eye(2)]*3)
    print(" piece dim",d,"equals {(v,v,v)}:",np.linalg.matrix_rank(np.hstack([S,sym]),tol=1e-7)==d==2)
print("\n== (i) moves + parity grading (block sign flips) ==")
Gg=group([GL,GR]+grading); ng,dg,cg,ig,gg=classify([GL,GR]+grading)
print("order",len(Gg),"commutant dim",ng,"isotypic dims",dg)
chi_=np.array([np.trace(g) for g in Gg]); FS=np.mean([np.trace(g@g) for g in Gg])
print("irreducible iff mean|tr|^2=1:",np.mean(abs(chi_)**2),"; Frobenius-Schur mean tr(g^2) =",FS)
for d,S in groups:
    print(" moves-invariant piece of dim",d,"invariant under grading:",all(np.linalg.matrix_rank(np.hstack([g@S,S]),tol=1e-7)==d for g in grading))
print("\n== sign move added to moves ==")
Gms=group([GL,GR,GS]); print("order",len(Gms),"commutant",classify([GL,GR,GS])[0])
print("\n== the seat's u_p twist is a block-diagonal conjugation ==")
U={(1,0):qj,(0,1):qi,(1,1):qk}
Dm=np.zeros((6,6),complex)
for i,p in enumerate(PAR): Dm[2*i:2*i+2,2*i:2*i+2]=U[p]
print("D1 chi_p rho = u_p rho u_p^-1:",all(np.allclose(chi(p,x)*rho[x],U[p]@rho[x]@np.linalg.inv(U[p])) for p in PAR for x in 'ab'))
def six_seat(phi):
    M=np.zeros((6,6),complex)
    for ip,p in enumerate(PAR):
        q=parity_image(phi,p); iq=PAR.index(q)
        M[2*iq:2*iq+2,2*ip:2*ip+2]=np.linalg.inv(U[q])@G[phi]@U[p]
    return M
for phi in 'LR':
    S_=six_seat(phi); print(f" seat's lift {phi} = D^-1 (my lift, direction -1) D :",np.allclose(S_,np.linalg.inv(Dm)@lift(phi,direction=-1)@Dm))
print("\n== robustness: block scalars c_p on the lifts (the lift is fixed only up to such scalars) ==")
from collections import Counter
res=Counter(); detail={}
for cl in itertools.product([1,-1],repeat=3):
    for cr in itertools.product([1,-1],repeat=3):
        gens=[lift('L',cl),lift('R',cr)]
        try: Gx=group(gens,cap=2000); o=len(Gx)
        except RuntimeError: o=-1
        n_,d_,c_,_,_=classify(gens)
        m1=o>0 and any(np.allclose(g,-np.eye(6)) for g in Gx)
        # with grading
        ng_=classify(gens+grading)[0]
        res[(n_,tuple(d_),m1,ng_)]+=1
print("sign choices (64): (commutant, isotypic dims, -1 in group, commutant with grading) -> count")
for k,v in res.items(): print(" ",k,v)
res2=Counter(); roots=[1,1j,-1,-1j]
for cl in itertools.product(roots,repeat=3):
    for cr in itertools.product(roots,repeat=3):
        gens=[lift('L',cl),lift('R',cr)]
        n_,d_,c_,_,_=classify(gens); ng_=classify(gens+grading)[0]
        res2[(n_,tuple(d_),ng_)]+=1
print("4th-root phases (4096): (commutant, isotypic dims, commutant with grading) -> count")
for k,v in res2.items(): print(" ",k,v)
print("\n== (ii) dim Lambda+ - 3: consistency only ==")
print("block-diagonal Lambda: sum_p (dim L_p -1) = dim L -3 ; antisymmetry index(dim)->-index(6-dim):",all((d-3)==-((6-d)-3) for d in range(7)))
print("NOT CHECKED: the Riemann-Roch term -3 = -(1/2)*rank 6 itself (needs the Dirac operator's index theory with a local end condition).")
print("\n== (iii) M_{1,2}: chi facts (also in B1624 w19_check.py) ==")
from fractions import Fraction as Fr
chi_sl=Fr(1,4)+Fr(1,6)-Fr(1,2); chi_f2=Fr(-1)
print("chi(SL2Z)",chi_sl,"chi(F2)*chi(SL2Z)",chi_f2*chi_sl,"chi(M12)=(2-2g-n)chi(M11) n=1:",(2-2-1)*chi_sl, "dim_C",3*1-3+2)
