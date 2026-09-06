"""Non-self-dual reps of the figure-eight knot group (2-bridge presentation <a,b | a w = w b>, w = b A B a):
(3) pi_1 ->> PSL(2,7) composed with the two 3-dim irreps (Klein's group); (4) a non-semisimple extension of chi_t by the
geometric rep. For each: h^1(V), h^1(V*), cusp data, and the lemma N = rank(res_V) - h^0(dM;V). numpy double precision."""
import itertools, numpy as np, sympy as sp
GENS=['a','b']; W=['b','A','B','a']; REL=['a']+W+['B']+[c.swapcase() for c in reversed(W)]
LAM=list('bABaaBAb')   # longitude word found in verify_core (commutes with a, translation 2 sqrt3 i)
def fox(word,x):
    terms=[]; prefix=[]
    for c in word:
        if c==x: terms.append((+1,list(prefix)))
        elif c==x.upper(): terms.append((-1,list(prefix)+[c]))
        prefix.append(c)
    return terms
def mat_word(rho,word):
    n=rho['a'].shape[0]; M=np.eye(n,dtype=complex)
    for c in word: M=M@rho[c]
    return M
def full(ra,rb): return {'a':ra,'b':rb,'A':np.linalg.inv(ra),'B':np.linalg.inv(rb)}
def groupring(rho,terms,n):
    M=np.zeros((n,n),dtype=complex)
    for s,w in terms: M+=s*mat_word(rho,w)
    return M
def rank(M,tol=1e-8):
    if M.size==0: return 0
    s=np.linalg.svd(M,compute_uv=False); return int((s>tol*max(1.0,s[0])).sum())
def cochain(rho,gens,rels,n):
    d0=np.vstack([rho[g]-np.eye(n) for g in gens])
    d1=np.block([[groupring(rho,fox(r,g),n) for g in gens] for r in rels]); return d0,d1
def h1(rho,gens,rels,n):
    d0,d1=cochain(rho,gens,rels,n); assert np.max(np.abs(d1@d0))<1e-9
    return (len(gens)*n-rank(d1))-rank(d0)
def cocycle_value(rho,f,word,n):
    val=np.zeros((n,1),dtype=complex); pref=[]
    for c in word:
        fc=f[c] if c.islower() else -(rho[c]@f[c.lower()])
        val=val+mat_word(rho,pref)@fc; pref.append(c)
    return val
def kernel_basis(M,tol=1e-8):
    U,s,Vh=np.linalg.svd(M); n=M.shape[1]; k=int((s>tol*max(1.0,s[0])).sum())
    return [Vh.conj().T[:,i:i+1] for i in range(k,n)]
def report(ra,rb,label,mu_word=['a'],lam_word=LAM):
    n=ra.shape[0]; out={}
    for tag,(xa,xb) in [('V',(ra,rb)),('V*',(np.linalg.inv(ra).T,np.linalg.inv(rb).T))]:
        rho=full(xa,xb); hv=h1(rho,GENS,[REL],n)
        mu=mat_word(rho,mu_word); lam=mat_word(rho,lam_word); assert np.max(np.abs(mu@lam-lam@mu))<1e-9
        rhoT={'a':mu,'b':lam,'A':np.linalg.inv(mu),'B':np.linalg.inv(lam)}; relT=[['a','b','A','B']]
        hT=h1(rhoT,GENS,relT,n); d0T,_=cochain(rhoT,GENS,relT,n); h0T=n-rank(d0T)
        d0,d1=cochain(rho,GENS,[REL],n); Z=kernel_basis(d1); cols=[]
        for zv in Z:
            f={'a':zv[0:n],'b':zv[n:2*n]}
            cols.append(np.vstack([cocycle_value(rho,f,mu_word,n),cocycle_value(rho,f,lam_word,n)]))
        resmat=np.hstack(cols+[d0T]) if cols else d0T; rres=rank(resmat)-rank(d0T)
        out[tag]=dict(h1=hv,h1T=hT,h0T=h0T,rres=rres)
    N=out['V']['h1']-out['V*']['h1']; ok=(N==out['V']['rres']-out['V']['h0T'])
    print(f"  {label:46s} h1(V)={out['V']['h1']} h1(V*)={out['V*']['h1']} N={N:+d} | h0(dM;V)={out['V']['h0T']} h0(dM;V*)={out['V*']['h0T']} h1(dM;V)={out['V']['h1T']} | res rank V={out['V']['rres']} V*={out['V*']['rres']} | lemma {'OK' if ok else 'VIOLATED'}")
    return N

print("=== (3) pi_1(4_1) ->> PSL(2,7), the two 3-dim irreps (mutually dual, non-self-dual) ===")
z=np.exp(2j*np.pi/7)
T=np.array([[0,1,0],[0,0,1],[1,0,0]],dtype=complex)
M0=np.array([[z-z**6,z**2-z**5,z**4-z**3],[z**2-z**5,z**4-z**3,z-z**6],[z**4-z**3,z-z**6,z**2-z**5]])
c=(M0@M0)[0,0]; assert np.allclose(M0@M0,c*np.eye(3)); R=M0/np.sqrt(c)
if not np.isclose(np.linalg.det(R),1): R=-R
assert np.isclose(np.linalg.det(R),1) and np.allclose(R@R,np.eye(3))
def key(M): return tuple(np.round(M.flatten(),6))
def closure(gens,cap=600):
    G={key(np.eye(3)):np.eye(3,dtype=complex)}; fr=[np.eye(3,dtype=complex)]
    while fr and len(G)<cap:
        new=[]
        for g in fr:
            for h in gens:
                x=g@h; k=key(x)
                if k not in G: G[k]=x; new.append(x)
        fr=new
    return G
G=None
for perm in itertools.permutations([z,z**2,z**4]):
    S=np.diag(perm); Gp=closure((S,T,R))
    print(f"  diagonal {tuple(int(round(np.angle(w)/(2*np.pi/7)))%7 for w in perm)} -> |<S,T,R>| = {len(Gp)}")
    if len(Gp)==168 and G is None: G=Gp
elems=list(G.values()); print("  |<S,T,R>| =",len(elems),"(168 = PSL(2,7))"); assert len(elems)==168
def order(M):
    P=np.eye(3)
    for k in range(1,15):
        P=P@M
        if np.allclose(P,np.eye(3),atol=1e-9): return k
def wm(x,y,wd):
    d={'a':x,'b':y,'A':np.linalg.inv(x),'B':np.linalg.inv(y)}; M=np.eye(3,dtype=complex)
    for ch in wd: M=M@d[ch]
    return M
invs={k:np.linalg.inv(v) for k,v in G.items()}
sols=[]
for kx,x in G.items():
    for ky,y in G.items():
        w=y@invs[kx]@invs[ky]@x
        if np.allclose(x@w,w@y,atol=1e-9): sols.append((x,y))
print("  homomorphism pairs (x,y):",len(sols))
def gen_size(x,y):
    H={key(np.eye(3))}; fr=[np.eye(3,dtype=complex)]
    while fr:
        new=[]
        for g in fr:
            for h in (x,y):
                m=g@h; k=key(m)
                if k not in H: H.add(k); new.append(m)
        fr=new
    return len(H)
seen=set(); n_surj=0
for x,y in sols:
    if np.allclose(x,np.eye(3)): continue
    sig=(order(x),order(y),order(x@y),order(x@np.linalg.inv(y)),gen_size(x,y),round(np.trace(x).real,4),round(np.trace(x).imag,4),round(np.trace(x@y).real,4),round(np.trace(x@y).imag,4))
    if sig in seen: continue
    seen.add(sig)
    lam=wm(x,y,LAM)
    print(f"   class: ord(a)={sig[0]} ord(b)={sig[1]} ord(ab)={sig[2]} |image|={sig[4]} tr a={np.trace(x):.3f} tr ab={np.trace(x@y):.3f} eig(a)={np.round(np.linalg.eigvals(x),3)} eig(lambda)={np.round(np.linalg.eigvals(lam),3)}")
    if sig[4]==168: n_surj+=1
    report(x,y,f"      PSL(2,7) 3-dim, |image|={sig[4]}")
print("  surjective classes:",n_surj)

print("\n=== (4) a NON-semisimple, non-self-dual rep: 0 -> rho_geom -> V -> chi_t -> 0 (cusp-fixed vectors present) ===")
u=sp.Rational(1,2)+sp.sqrt(3)*sp.I/2; s=sp.symbols('s')
a2=sp.Matrix([[1,1],[0,1]]); b2=sp.Matrix([[1,0],[u,1]])
rho_s={'a':s*a2,'b':s*b2,'A':(s*a2).inv(),'B':(s*b2).inv()}
def fox_sym(word,x,rho):
    M=sp.zeros(2,2); pref=sp.eye(2)
    for c in word:
        if c==x: M+=pref
        elif c==x.upper(): M-=pref*rho[c]
        pref=pref*rho[c]
    return M
Da=sp.simplify(fox_sym(REL,'a',rho_s)); det_a=sp.factor(sp.simplify(Da.det()))
print("  det Phi_s(dr/da) =",det_a)
roots=[r for r in sp.solve(sp.numer(sp.together(det_a)),s)]
print("  roots:",[sp.nsimplify(r) for r in roots])
u_n=complex(u); A2=np.array([[1,1],[0,1]],dtype=complex); B2=np.array([[1,0],[u_n,1]],dtype=complex)
for r in roots:
    s0=complex(r)
    if abs(s0-1)<1e-9: continue
    rhoW=full(s0*A2,s0*B2)                      # W = rho (x) chi_{s0}
    d0W,d1W=cochain(rhoW,GENS,[REL],2); Z=kernel_basis(d1W)
    zv=next((zz for zz in Z if rank(np.hstack([d0W,zz]))>rank(d0W)),None)
    if zv is None: print(f"  s0={s0:.4f}: h^1(rho x chi_s0)=0, no extension"); continue
    t=1/s0                                       # quotient character chi_t, t = 1/s0 so that Hom(chi_t, rho) = rho (x) chi_{s0}
    def ext(g,cvec):
        M=np.zeros((3,3),dtype=complex); M[:2,:2]=g; M[:2,2]=(t*cvec).ravel(); M[2,2]=t; return M
    Ea,Eb=ext(A2,zv[0:2]),ext(B2,zv[2:4])
    rhoE=full(Ea,Eb); relE=mat_word(rhoE,REL)
    print(f"  s0={s0:.4f} (t={t:.4f}): extension satisfies the relator: {np.max(np.abs(relE-np.eye(3))):.1e};  h^1(rho x chi_s0)={h1(rhoW,GENS,[REL],2)}")
    report(Ea,Eb,f"     extension of chi_t by rho_geom, t={t:.3f}")
