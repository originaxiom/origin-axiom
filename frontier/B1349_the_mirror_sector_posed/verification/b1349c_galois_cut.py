"""THE GALOIS CUT. A direction with RATIONAL coordinates in the weight basis is fixed by every
sigma in Gal(Q(zeta_60)/Q) automatically. So the question 'does Galois cut the orbit' becomes:
HOW MANY of the distinguished directions are rational? That number replaces the orbit size in
R7's look-elsewhere ledger and in R11's anchor debit."""
import numpy as np, itertools, math
from fractions import Fraction

def su3(k=2):
    kap = k+3
    W=[(a,b) for a in range(k+1) for b in range(k+1-a)]
    Lv=lambda w:np.array([w[0]+w[1]+2.,w[1]+1.,0.])
    ip=lambda u,v: float(np.dot(u,v)-u.sum()*v.sum()/3)
    P=list(itertools.permutations(range(3)))
    sg=lambda p:(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    S=np.zeros((6,6),dtype=complex)
    for i,wl in enumerate(W):
        for j,wm in enumerate(W):
            S[i,j]=sum(sg(p)*np.exp(-2j*np.pi*ip(Lv(wl)[list(p)],Lv(wm))/kap) for p in P)
    S*=-1j/(kap*np.sqrt(3.))
    C2=lambda w:(2/3)*(w[0]**2+w[0]*w[1]+w[1]**2)+2*(w[0]+w[1])
    T=np.diag([np.exp(2j*np.pi*(C2(w)/(2*kap)-(8*k/(k+3))/24)) for w in W])
    return W,S,T
W,S,T=su3(); C=S@S; R=T; L=np.linalg.inv(S)@np.linalg.inv(T)@S
ix={w:i for i,w in enumerate(W)}

def group(Bas, root):
    rest=lambda M: np.linalg.lstsq(Bas,M@Bas,rcond=None)[0]
    Ro,Lo=rest(R),rest(L); d=Bas.shape[1]
    def pk(M,q=6):
        Mn=M/(np.linalg.det(M)**(1.0/d)); best=None
        for r in range(d):
            A=Mn*np.exp(2j*np.pi*r/d)
            kk=tuple((round(float(x.real),q),round(float(x.imag),q)) for x in A.flatten())
            best=kk if best is None else min(best,kk)
        return best
    seen,fr,mats={pk(np.eye(d))},[np.eye(d,dtype=complex)],[np.eye(d,dtype=complex)]
    gens=[Ro,Lo,np.linalg.inv(Ro),np.linalg.inv(Lo)]
    while fr:
        nx=[]
        for M in fr:
            for g in gens:
                Pm=M@g; kk=pk(Pm)
                if kk not in seen: seen.add(kk); nx.append(Pm); mats.append(Pm)
        fr=nx
    return mats

par=lambda a,b,tol=1e-6: np.linalg.norm(b/np.linalg.norm(b)-np.vdot(a/np.linalg.norm(a),b/np.linalg.norm(b))*a/np.linalg.norm(a))<tol
def is_rational(v, tol=1e-11, maxden=1000):
    """is the projective direction v representable with RATIONAL coordinates?

    TRAP, hit on the first pass and recorded: with tol=1e-8 and maxden=10^4 this ACCEPTED 1/phi,
    because the Fibonacci ratio 4181/6765 approximates it to ~1e-8. Golden values are exactly what
    this instrument is full of, so the test must reject them. With maxden=1000 the best rational
    approximation to 1/phi is 610/987, off by 4.5e-7 >> 1e-11, so 1/phi is now correctly rejected."""
    v = v/v[int(np.argmax(np.abs(v)))]
    for x in v:
        if abs(x.imag) > tol: return False
        if abs(float(Fraction(float(x.real)).limit_denominator(maxden)) - x.real) > tol: return False
    return True

# the control the first pass lacked: the test must REJECT the golden values
_phi_inv = (5 ** 0.5 - 1) / 2
assert not is_rational(np.array([1.0 + 0j, _phi_inv + 0j])), "is_rational must reject 1/phi"
assert is_rational(np.array([1.0 + 0j, -0.5 + 0j])), "is_rational must accept -1/2"

for name, Bas, d in (("theta-ODD plane (B1348, freedom 12)",
                      np.array([[0,0],[1,0],[0,1],[-1,0],[0,0],[0,-1]],dtype=complex), 2),
                     ("theta-EVEN sector (B1349, freedom 48; THE CROSSING TARGET)",
                      np.array([[1,0,0,0],[0,0,1,0],[0,0,0,1],[0,0,1,0],[0,1,0,0],[0,0,0,1]],dtype=complex), 4)):
    mats = group(Bas, d)
    G = len(mats)
    stab = lambda v: sum(1 for M in mats if par(v, M@v))
    cand={}
    for M in mats:
        if np.allclose(M-(np.trace(M)/d)*np.eye(d),0,atol=1e-8): continue
        for col in np.linalg.eig(M)[1].T:
            cand[tuple(np.round(col/np.linalg.norm(col),5))]=col
    smax = max(stab(v) for v in cand.values())
    top = [v for v in cand.values() if stab(v)==smax]
    # dedupe projectively
    uniq=[]
    for v in top:
        if not any(par(v,u) for u in uniq): uniq.append(v)
    rat = [v for v in uniq if is_rational(v)]
    print(f"\n{name}")
    print(f"   |group| = {G},  maximal |Stab| = {smax},  orbit size = {G//smax}")
    print(f"   distinct maximal-stabiliser directions found: {len(uniq)}")
    print(f"   of them RATIONAL (hence fixed by every sigma in Gal(Q(zeta_60)/Q)): {len(rat)}")
    for v in rat:
        vv = v/v[int(np.argmax(np.abs(v)))]
        print(f"      {np.round(vv.real,6)}   |Stab| = {stab(v)}")
