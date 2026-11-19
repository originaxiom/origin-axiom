"""W28 independent check. Claims as stated (SM seat W28; row): 
 C1 six local solutions: 2O acts (order 48); decomposes 2 + 4 = spin1/2 + spin3/2 (chars tr g, tr^3-2tr g), vector-spinor.
 C2 two middle conditions (dims 2,4; index -1,+1) break flavour U(3) to a phase (stabiliser = scalars).
 C3 index sets: moves {-3,-1,1,3}; flavour {-3,0,3}; moves+flavour {-3,3}; locality {-3,3}; grading {-3..3}; moves+grading {-3,3}.
 C4 Q8 = <iZ,iY> (Pauli group's SU(2) lift), parities = Z,Y,X axes, eigenbases mutually unbiased.
 C5 lifts L,R generate 2O = normaliser of Q8, order 48, image = 24 cube rotations = Clifford <H,S> image; PSL(2,Z/4) ~ S4;
    moves act through PSL(2,Z/4); SU(2)_1 data S,T relations; dictionary M unique for T and for anti-semion.
 Expectation: all hold as predicted."""
import numpy as np, itertools, sympy as sp
np.set_printoptions(precision=4, suppress=True)
tol=1e-9
X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1]).astype(complex);I2=np.eye(2,dtype=complex)
rho={'a':1j*Z,'b':1j*Y}
def nullspace(A):
    u,s,vh=np.linalg.svd(A); r=int((s>1e-9).sum()); return vh[r:].conj()
def solve_conj(images):  # find g with g rho(x) = img(x) g
    rows=[np.kron(I2,rho_x.T) - np.kron(img,I2) for rho_x,img in images]  # vec row-major: (g rho)=kron(I,rho^T) vec g ; (img g)=kron(img,I) vec g
    ns=nullspace(np.vstack(rows)); 
    return ns
def lift(img):
    ns=solve_conj([(rho['a'],img['a']),(rho['b'],img['b'])]); assert len(ns)==1,len(ns)
    g=ns[0].reshape(2,2); g=g/np.sqrt(np.linalg.det(g)); 
    assert np.allclose(g@g.conj().T,I2); return g
ra,rb=rho['a'],rho['b']
MV={'L':{'a':ra,'b':ra@rb},'R':{'a':ra@rb,'b':rb},'P':{'a':rb,'b':ra},'-I':{'a':np.linalg.inv(ra),'b':np.linalg.inv(rb)}}
g={k:lift(v) for k,v in MV.items()}
print("lifts found by solving g rho(x) g^-1 = rho(phi x): unique up to scalar; det=1 normalised")
for k in g: print(k,np.round(g[k],4).tolist())
def eq_up_sign(A,B): return np.allclose(A,B,atol=tol) or np.allclose(A,-B,atol=tol)
print("g_L ~ (1+iZ)/sqrt2:",eq_up_sign(g['L'],(I2+1j*Z)/np.sqrt(2)),"; g_R ~ (1-iY)/sqrt2:",eq_up_sign(g['R'],(I2-1j*Y)/np.sqrt(2)),
      "; g_P ~ i(Z+Y)/sqrt2:",eq_up_sign(g['P'],1j*(Z+Y)/np.sqrt(2)),"; g_-I ~ iX:",eq_up_sign(g['-I'],1j*X))
# parities
PAR=[(1,0),(0,1),(1,1)]
def chi(p,x): return (-1)**(p[0] if x=='a' else p[1])
# word exponent vector mod 2 of image of generator under move: parities act via chi_p(phi(x))
EX={'L':{'a':(1,0),'b':(1,1)},'R':{'a':(1,1),'b':(0,1)},'P':{'a':(0,1),'b':(1,0)},'-I':{'a':(1,0),'b':(0,1)}}
def chi_img(p,m,x): e=EX[m][x]; return (-1)**(p[0]*e[0]+p[1]*e[1]) if False else chi(p,'a')**e[0]*chi(p,'b')**e[1]
def pmap(m,p):
    q=(0 if chi_img(p,m,'a')==1 else 1, 0 if chi_img(p,m,'b')==1 else 1); return PAR.index(q)
# units u_p: chi_p rho = u rho u^-1
U={}
for p in PAR:
    ns=solve_conj([(rho['a'],chi(p,'a')*rho['a']),(rho['b'],chi(p,'b')*rho['b'])]); assert len(ns)==1
    u=ns[0].reshape(2,2); u=u/np.sqrt(np.linalg.det(u)); U[p]=u
print("u_p ~ axis: (1,0)->Y?",[eq_up_sign(U[(1,0)],1j*Y) ,eq_up_sign(U[(0,1)],1j*Z),eq_up_sign(U[(1,1)],1j*X)] )
def six(m):
    M=np.zeros((6,6),complex)
    for ip,p in enumerate(PAR):
        iq=pmap(m,p); M[2*iq:2*iq+2,2*ip:2*ip+2]=np.linalg.inv(U[PAR[iq]])@g[m]@U[p]
    return M
def sixB(m): # block form Pi (x) G
    M=np.zeros((6,6),complex)
    for ip,p in enumerate(PAR):
        iq=pmap(m,p); M[2*iq:2*iq+2,2*ip:2*ip+2]=g[m]
    return M
Bm=np.zeros((6,6),complex)
for i,p in enumerate(PAR): Bm[2*i:2*i+2,2*i:2*i+2]=U[p]
MS={m:six(m) for m in g}
# W = sum chi_p rho on six; check lifts intertwine W: M W(x) M^-1 = W(phi x)
def W(x): 
    M=np.zeros((6,6),complex)
    for i,p in enumerate(PAR): M[2*i:2*i+2,2*i:2*i+2]=chi(p,x)*rho[x]
    return M
Wa,Wb=W('a'),W('b')
def Wword(m,x): # W(phi(x)) = chi(..)rho(image)
    return Wa if False else None
for m in ['L','R']:
    Mm=MS[m]
    lhsa=Mm@Wa@np.linalg.inv(Mm); lhsb=Mm@Wb@np.linalg.inv(Mm)
    ea=EX[m]['a'];eb=EX[m]['b']
    def Wpow(e): 
        A=np.eye(6,dtype=complex)
        if e[0]: A=A@Wa
        if e[1]: A=A@Wb
        return A
    # careful: image words: L: b->ab ; R: a->ab ; P swaps; ordered a then b
    print(m,"intertwines W (up to the convention phi or phi^-1):",np.allclose(lhsa,Wpow(ea),atol=tol) and np.allclose(lhsb,Wpow(eb),atol=tol),
          "| or inverse-direction:", np.allclose(np.linalg.inv(Mm)@Wa@Mm,Wpow(ea),atol=tol) and np.allclose(np.linalg.inv(Mm)@Wb@Mm,Wpow(eb),atol=tol))
print("E1: B^-1 (Pi(x)G) B equals twisted lift (L,R):",[np.allclose(np.linalg.inv(Bm)@sixB(m)@Bm,MS[m],atol=tol) for m in 'LR'])
# group on C^6 paired with SU(2) 2x2
def gen_group(gens6,gens2):
    G=[(np.eye(6,dtype=complex),np.eye(2,dtype=complex))];fr=[G[0]]
    while fr:
        A,a=fr.pop()
        for h6,h2 in zip(gens6,gens2):
            N=(A@h6,a@h2)
            if not any(np.allclose(N[0],E[0],atol=1e-8) for E in G):
                G.append(N);fr.append(N)
                assert len(G)<2000
    return G
G=gen_group([MS['L'],MS['R']],[g['L'],g['R']])
print("C1: |<M_L,M_R>| =",len(G))
G2=[a for _,a in G]; 
n2=1; 
S2=[]
for a in G2:
    if not any(np.allclose(a,b,atol=1e-8) for b in S2): S2.append(a)
print("distinct 2x2 elements of <g_L,g_R>:",len(S2),"(= pairs, so M determines g:",len(S2)==len(G),")")
def order(A):
    P=A.copy();n=1
    while not np.allclose(P,np.eye(len(A)),atol=1e-8): P=P@A;n+=1
    return n
from collections import Counter
print("order profile 2x2 group:",sorted(Counter(order(a) for a in S2).items()),"expected 2O: {1:1,2:1,3:8,4:18,6:8,8:12}")
print("contains -1 as -I6:",any(np.allclose(A,-np.eye(6),atol=1e-8) for A,_ in G))
def comm_basis(mats,n):
    rows=[np.kron(np.eye(n),A)-np.kron(A.T,np.eye(n)) for A in mats]
    ns=nullspace(np.vstack(rows)); return [v.reshape(n,n) for v in ns]   # row-major vec: (X A)->kron(I,A^T)? check below
def comm_basis2(mats,n):
    # X A = A X  <=> (I⊗A^T - A⊗I) vec_r(X)=0 for row-major vec
    rows=[np.kron(np.eye(n),A.T)-np.kron(A,np.eye(n)) for A in mats]
    ns=nullspace(np.vstack(rows)); return [v.reshape(n,n) for v in ns]
def clumps(S,n=6,seed=3):
    """S closed under adjoint (we add adjoints). returns (commutant dim, list of irreducible dims by clump, subset-sum dims)"""
    S=list(S)+[A.conj().T for A in S]
    C=comm_basis2(S,n); 
    rng=np.random.default_rng(seed); Xr=np.zeros((n,n),complex)
    for c in C:
        H1=c+c.conj().T;H2=1j*(c-c.conj().T)
        Xr+=rng.normal()*H1+rng.normal()*H2
    for c in C: assert all(np.allclose(c@A,A@c,atol=1e-8) for A in S)
    ev=np.linalg.eigvalsh((Xr+Xr.conj().T)/2); 
    groups=[];ev=sorted(ev)
    cur=[ev[0]]
    for e in ev[1:]:
        if abs(e-cur[-1])<1e-6: cur.append(e)
        else: groups.append(len(cur));cur=[e]
    groups.append(len(cur))
    # clump sizes = irreducible dims d_i, one clump per copy; subset sums of clumps
    subs=sorted({sum(c) for r in range(len(groups)+1) for c in itertools.combinations(groups,r)})
    return len(C),sorted(groups),subs,C
def idx(S): return [d-3 for d in S]
cm,gr,sb,Cm=clumps([MS['L'],MS['R']])
print("moves: commutant dim",cm,"clump dims",gr,"kept dims",sb,"indices",idx(sb))
# projections onto V2,V4: eigenspaces of generic hermitian commutant element
def eigspaces(C,n=6,seed=5):
    rng=np.random.default_rng(seed);Xr=np.zeros((n,n),complex)
    for c in C: Xr+=rng.normal()*(c+c.conj().T)+rng.normal()*1j*(c-c.conj().T)
    w,v=np.linalg.eigh(Xr);out=[];cur=[0]
    for i in range(1,n):
        if abs(w[i]-w[cur[-1]])<1e-6: cur.append(i)
        else: out.append(v[:,cur]);cur=[i]
    out.append(v[:,cur]);return out
sp_=eigspaces(Cm); sp_.sort(key=lambda a:a.shape[1]); V2c,V4c=sp_
print("pieces dims",V2c.shape[1],V4c.shape[1])
ch2=[];ch4=[];t2=[]
for A,a in G:
    ch2.append(np.trace(V2c.conj().T@A@V2c)); ch4.append(np.trace(V4c.conj().T@A@V4c)); t2.append(np.trace(a))
ch2=np.array(ch2);ch4=np.array(ch4);t2=np.array(t2)
print("V2 char == tr g (spin 1/2) all 48:",np.allclose(ch2,t2,atol=1e-7),"| V4 char == tr^3-2tr (spin 3/2):",np.allclose(ch4,t2**3-2*t2,atol=1e-7))
print("norms <chi,chi>: V2",np.round((abs(ch2)**2).sum()/48,6),"V4",np.round((abs(ch4)**2).sum()/48,6),"; <chi2,chi4>",np.round(abs((ch2.conj()*ch4).sum()/48),6))
print("spin 3/2 char test on spectrum: 6x6 eigenvalues multiset {l,l*,l,l*,l^3,l*^3} for all:",
 all(sorted(np.round(np.angle(np.linalg.eigvals(A)),5).tolist())==sorted(np.round(np.angle(np.array([l,l.conjugate(),l,l.conjugate(),l**3,(l**3).conjugate()])),5).tolist()) 
     for A,a in G for l in [np.linalg.eigvals(a)[0]]))
# is V2 the diagonal in Pi(x)G basis?
GB=gen_group([sixB('L'),sixB('R')],[g['L'],g['R']])
cmB,grB,sbB,CB=clumps([sixB('L'),sixB('R')])
spB=eigspaces(CB);spB.sort(key=lambda a:a.shape[1]);V2B,V4B=spB
diag=np.zeros((6,2),complex);diag[0::2,0]=1;diag[1::2,1]=1
sumz=[np.array([1,0,-1,0,0,0],complex),np.array([0,1,0,-1,0,0],complex),np.array([1,0,0,0,-1,0],complex),np.array([0,1,0,0,0,-1],complex)]
def same(Sub,vecs):
    Q,_=np.linalg.qr(Sub); return all(np.allclose(Q@(Q.conj().T@v),v,atol=1e-8) for v in vecs)
print("in Pi(x)G basis: V2 = {(v,v,v)}:",same(V2B,[diag[:,0],diag[:,1]]),"V4 = {v1+v2+v3=0}:",same(V4B,sumz),"|group order",len(GB))
# flavour
Cw=comm_basis2([Wa,Wb],6); print("flavour algebra (commutant of W(a),W(b)) dim:",len(Cw))
# lifts normalise it
def in_span(Mx,basis):
    A=np.array([b.flatten() for b in basis]).T; v=Mx.flatten(); c,res,rk,_=np.linalg.lstsq(A,v,rcond=None); return np.allclose(A@c,v,atol=1e-8)
print("lifts normalise flavour algebra:",all(in_span(MS[m]@b@np.linalg.inv(MS[m]),Cw) for m in 'LR' for b in Cw))
cf,grf,sbf,_=clumps(Cw); print("flavour alone: commutant dim",cf,"clumps",grf,"dims",sbf,"indices",idx(sbf))
cmf,grmf,sbmf,_=clumps([MS['L'],MS['R']]+Cw); print("moves+flavour: dims",sbmf,"indices",idx(sbmf))
# E4 stabiliser in flavour algebra of V2, V4
def stab(V):
    Q,_=np.linalg.qr(V); P=Q@Q.conj().T; N=np.eye(6)-P
    rows=[ (N@c@Q).flatten() for c in Cw]; A=np.array(rows).T   # want sum x_i c_i with N c Q=0
    return len(nullspace(A))
print("dim{A in flavour algebra: A V ⊂ V}: V2",stab(V2c),"V4",stab(V4c),"(1 = scalars)")
# also check scalars are exactly the stabiliser: identity in span
# grading
proj=[np.diag(np.repeat([1.0 if k==j else 0.0 for k in range(3)],2)).astype(complex) for j in range(3)]
cg,grg,sbg,_=clumps(proj); print("grading alone: dims",sbg,"indices",idx(sbg))
cmg,_,sbmg,_=clumps([MS['L'],MS['R']]+proj); print("moves+grading: dims",sbmg,"indices",idx(sbmg))
# locality: W([a,b]) = -1
comm=Wa@Wb@np.linalg.inv(Wa)@np.linalg.inv(Wb); print("W([a,b]) = -1 on six:",np.allclose(comm,-np.eye(6)))
mu=[np.eye(6)[:,[i]]@np.eye(6)[[j],:] for i in range(6) for j in range(6)]
cl,_,sbl,_=clumps([comm],6) if False else (None,None,None,None)
# commutant of -1 is all M6: invariant under all of M6:
cl,grl,sbl,_=clumps(mu); print("locality (invariant under all of M6): dims",sbl,"indices",idx(sbl))
# with sign move
G3=gen_group([MS['L'],MS['R'],MS['-I']],[g['L'],g['R'],g['-I']]); print("with -I lift order",len(G3))
# ---------- Part II
print("\n== Part II")
Q8=[I2]
for gen in [1j*Z,1j*Y]:
    pass
Q=[I2]
fr=[I2]
while fr:
    A=fr.pop()
    for h in [1j*Z,1j*Y]:
        N=A@h
        if not any(np.allclose(N,E) for E in Q): Q.append(N);fr.append(N)
print("<iZ,iY> order",len(Q),"; iZ*iY == iX:",np.allclose(1j*Z@(1j*Y),1j*X),"; Q8 = Pauli group ∩ SU(2); full Pauli group <X,Y,Z> order:",end=" ")
P=[I2];fr=[I2]
while fr:
    A=fr.pop()
    for h in [X,Y,Z]:
        N=A@h
        if not any(np.allclose(N,E) for E in P): P.append(N);fr.append(N)
print(len(P),"(Q8 is index 2 in it; mod phases both are Z2^2)")
def eigb(A): w,v=np.linalg.eigh(A); return v
EB={'X':eigb(X),'Y':eigb(Y),'Z':eigb(Z)}
print("MUB overlaps |<e|f>|^2:",{(a,b):np.round(abs(EB[a].conj().T@EB[b])**2,6).tolist() for a,b in [('X','Y'),('Y','Z'),('X','Z')]})
# Q8 normaliser / Aut
def Ad(Um): s=[X,Y,Z]; return np.array([[0.5*np.trace(s[i]@Um@s[j]@Um.conj().T).real for j in range(3)] for i in range(3)])
def inQ(A): return any(np.allclose(A,E,atol=1e-8) for E in Q)
print("all 48 normalise Q8:",all(inQ(a@q@np.linalg.inv(a)) for a in S2 for q in Q))
# Aut(Q8) by brute force
els=Q; gensQ=[1j*Z,1j*Y]
def idxQ(A): return [i for i,E in enumerate(els) if np.allclose(A,E)][0]
aut=0
for im in itertools.product(els,repeat=2):
    # build hom
    try:
        mp={idxQ(I2):I2}; fr=[I2]; ok=True
        # BFS words
        words={idxQ(I2):(I2,I2)}
        fr=[(I2,I2)]
        while fr and ok:
            A,B=fr.pop()
            for h,hi in zip(gensQ,im):
                Nn=(A@h,B@hi);k=idxQ(Nn[0])
                if k in words:
                    if not np.allclose(words[k][1],Nn[1]): ok=False;break
                else: words[k]=Nn;fr.append(Nn)
        if ok and len(words)==8 and len({idxQ(w[1]) for w in words.values()})==8: aut+=1
    except Exception: pass
print("|Aut(Q8)| by brute force:",aut)
cent=[a for a in S2 if all(np.allclose(a@q,q@a,atol=1e-8) for q in Q)]
print("centraliser of Q8 inside 2O:",len(cent),"=> image in Aut(Q8) has order",48//len(cent),"= |Aut| (so 2O is the whole normaliser in SU(2), since centraliser of irreducible Q8 in SU(2) is ±1)")
# Clifford <H,S>
H=np.array([[1,1],[1,-1]],complex)/np.sqrt(2);Sg=np.diag([1,1j])
def rots(gens):
    R=[np.eye(3)];fr=[np.eye(3)]
    while fr:
        A=fr.pop()
        for h in gens:
            N=A@Ad(h)
            if not any(np.allclose(N,E,atol=1e-8) for E in R): R.append(N);fr.append(N)
    return R
RC=rots([H,Sg]); RW=rots([g['L'],g['R']])
print("Clifford <H,S> rotations:",len(RC),"; <g_L,g_R> rotations:",len(RW),"; equal sets:",all(any(np.allclose(a,b,atol=1e-8) for b in RC) for a in RW) and len(RW)==len(RC))
Rall=[np.array(m) for m in [list(itertools.permutations(range(3)))] ] 
cube=[]
for pm in itertools.permutations(range(3)):
    for sg in itertools.product([1,-1],repeat=3):
        M=np.zeros((3,3))
        for i in range(3): M[i,pm[i]]=sg[i]
        if abs(np.linalg.det(M)-1)<1e-9: cube.append(M)
print("cube rotation group size",len(cube),"; Ad(2O) == cube group:",len(RW)==24 and all(any(np.allclose(a,b) for b in cube) for a in RW))
# SU(2)_1
S1=np.array([[1,1],[1,-1]])/np.sqrt(2); T1=np.exp(-2j*np.pi/24)*np.diag([1,1j])
print("S^2=1:",np.allclose(S1@S1,np.eye(2)),"; (ST)^3=S^2:",np.allclose(np.linalg.matrix_power(S1@T1,3),S1@S1))
WA=np.diag(S1[1]/S1[0]); WB=S1@WA@np.linalg.inv(S1)
print("W_A=Z:",np.allclose(WA,Z),"W_B=X:",np.allclose(WB,X),"anticommute:",np.allclose(WA@WB,-WB@WA))
TW=T1@WB@np.linalg.inv(T1); print("T fixes W_A:",np.allclose(T1@WA@np.linalg.inv(T1),WA),"; T W_B T^-1 ∝ W_A W_B:",np.allclose(TW, TW[0,1]/(WA@WB)[0,1]*(WA@WB)) , "ratio",np.round(TW[0,1]/(WA@WB)[0,1],4))
gL,gR=g['L'],g['R']
t=Ad(gL); s_=Ad(gL@np.linalg.inv(gR)@gL)
mp=np.linalg.matrix_power
print("(2,3,4): s^2=1",np.allclose(mp(s_,2),np.eye(3)),"(st)^3=1",np.allclose(mp(s_@t,3),np.eye(3)),"t^4=1",np.allclose(mp(t,4),np.eye(3)),"; t^2 != 1:",not np.allclose(mp(t,2),np.eye(3)))
def count_M(Tm):
    sols=[]
    for M in cube:
        c=[np.allclose(M@Ad(rho['a'])@M.T,Ad(Z)),np.allclose(M@Ad(rho['b'])@M.T,Ad(X)),np.allclose(M@Ad(gL)@M.T,Ad(Tm)),
           np.allclose(M@Ad(gR)@M.T,Ad(S1@np.linalg.inv(Tm)@np.linalg.inv(S1)))]
        if all(c): sols.append(M)
    return sols
s1=count_M(T1); Tbar=np.exp(+2j*np.pi/24)*np.diag([1,-1j]); s2=count_M(Tbar)
print("dictionary M, semion T:",len(s1),[m.astype(int).tolist() for m in s1],"; anti-semion:",len(s2),[m.astype(int).tolist() for m in s2])
# also: search all 24 cube rotations is enough? M preserves axes (shown). fine.
# PSL(2,Z/4)
def mm(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%4 for j in range(2)) for i in range(2))
Lm=((1,1),(0,1));Rm=((1,0),(1,1))
def norm(A): 
    Bm_=tuple(tuple((-x)%4 for x in r) for r in A); return min(A,Bm_)
E=((1,0),(0,1))
nodes={norm(E):np.eye(3)};fr=[E]
ok=True
Ad_gens={'L':Ad(gL),'R':Ad(gR)}
while fr:
    A=fr.pop()
    for nm,mt in (('L',Lm),('R',Rm)):
        N=mm(A,mt);k=norm(N);r=nodes[norm(A)]@Ad_gens[nm]
        if k in nodes:
            if not np.allclose(nodes[k],r,atol=1e-8): ok=False
        else: nodes[k]=r;fr.append(N)
print("|PSL(2,Z/4)| from L,R:",len(nodes),"; word->rotation well defined on PSL(2,Z/4):",ok,"; injective onto 24 rotations:",len({tuple(np.round(v,6).flatten()) for v in nodes.values()})==24)
print("SL(2,Z/4) order (all 2x2 det 1 mod 4):",sum(1 for a,b,c,d in itertools.product(range(4),repeat=4) if (a*d-b*c)%4==1))
# PSL(2,Z/4) ~ S4: Sylow-3 conjugation action on 4 subgroups -> injective hom
els=list(nodes.keys())
def pinv(A):
    # inverse in PSL: search
    for B in els:
        if norm(mm(A,B))==norm(E): return B
def pm(A,B): return norm(mm(A,B))
def powr(A,n):
    P=norm(E)
    for _ in range(n): P=pm(P,A)
    return P
ord3=[A for A in els if A!=norm(E) and powr(A,3)==norm(E)]
subs=set()
for A in ord3: subs.add(frozenset([norm(E),A,pm(A,A)]))
subs=list(subs); print("order-3 subgroups:",len(subs))
def conj_action(A):
    perm=[]
    for Sg_ in subs:
        im=frozenset(pm(pm(A,x),pinv(A)) for x in Sg_); perm.append(subs.index(im))
    return tuple(perm)
perms={A:conj_action(A) for A in els}
print("conjugation action on the 4 Sylow-3 subgroups: image size",len(set(perms.values())),"(24 => injective into S4 => PSL(2,Z/4) ≅ S4); homomorphism check:",
      all(tuple(perms[A][perms[B][i]] for i in range(4))==perms[pm(A,B)] or tuple(perms[B][perms[A][i]] for i in range(4))==perms[pm(A,B)] for A in els for B in els))

print("\n== E4 debug / recheck")
def stab2(V):
    Q,_=np.linalg.qr(V); P=Q@Q.conj().T; N=np.eye(6)-P
    A=np.array([(N@c@Q).flatten() for c in Cw]).T
    s=np.linalg.svd(A,compute_uv=False); print(" singular values",np.round(s,4)); return int((s<1e-9).sum())+max(0,A.shape[1]-len(s))
print("V2:",stab2(V2c),"V4:",stab2(V4c))
print("V2 in W-basis: is it of form {sum u_p v (x) e_p}? check via projection norms per block:",[np.round(np.linalg.norm(V2c[2*i:2*i+2],'fro')**2,4) for i in range(3)])
# direct: flavour = 1(x)A in coordinates; test with an explicit block-diag-in-multiplicity basis: A_ex maps (rho_Q (x) C3) -> build from Cw elements and test a diagonal flavour element
import scipy.linalg as sl
# eigen-decomposition of the 3 'flavour projectors' (rank-2 idempotents) inside Cw: elements of Cw of rank 2 commuting
print("Cw ranks:",[np.linalg.matrix_rank(c,tol=1e-8) for c in Cw])
# spectrum test redone with characters of eigenvalue multisets via trace of powers
ok=True
for A,a in G:
    l=np.linalg.eigvals(a); t=l[0]+l[1]
    # char of V2+V4 on powers k: tr(A^k) vs tr(a^k)^3 - tr(a^k)
    for k in (1,2,3):
        tk=np.trace(np.linalg.matrix_power(a,k)); 
        if not np.isclose(np.trace(np.linalg.matrix_power(A,k)),tk**3-tk,atol=1e-7): ok=False
print("tr(M^k) = tr(g^k)^3 - tr(g^k), k=1,2,3, all 48:",ok)
