"""B570 Lane C, C2 — the gap-chirality duality theorem, verified on 4_1 at SL(2,C).
THEOREM (irreducible rho: Gamma -> SL(2,C)): (A) all traces real <=> (B) rho-bar ~ rho
<=> (C) rho conjugates into a real form (SL(2,R) or SU(2)).  On the figure-eight geometric
rep all three FAIL on the single fact tr(ab) not in R (trace field Q(sqrt-3)) = the
compactness gap = c-chirality.  Amphichirality gives only the TWISTED rho-bar ~ rho o phi
with phi OUTER.  Fast + deterministic."""
import numpy as np, sympy as sp

# ---------- exact symbolic geometric rep (Riley two-bridge, y=omega) ----------
I=sp.I; s3=sp.sqrt(3); w=sp.Rational(-1,2)+s3*I/2
A=sp.Matrix([[1,1],[0,1]]); B=sp.Matrix([[1,0],[-w,1]])
gen={'a':A,'A':A.inv(),'b':B,'B':B.inv()}
def wd(s):
    R=sp.eye(2)
    for c in s: R=R*gen[c]
    return R

def test_relator_holds():
    # figure-eight relator a W b^-1 W^-1, W='bABa'  (a W = W b)
    assert sp.simplify(wd('abABaBAbaB'))==sp.eye(2)

def test_irreducible():
    # reducible iff tr[a,b]=2
    assert sp.simplify(sp.trace(wd('abAB')))==sp.Rational(3,2)-s3*I/2
    assert sp.simplify(sp.trace(wd('abAB')))!=2

def test_A_trace_field_nonreal():
    # (A) FALSE: tr(ab) exactly 5/2 - sqrt(3)/2 i, non-real => trace field Q(sqrt-3)
    t=sp.simplify(sp.trace(wd('ab')))
    assert t==sp.Rational(5,2)-s3*I/2
    assert sp.im(t)!=0

# ---------- numeric intertwiner machinery (complex null space: use .conj()) ----------
def _block(R,T):
    M=np.zeros((4,4),complex)
    for i in range(2):
        for j in range(2):
            r=2*i+j
            for k in range(2):
                M[r,2*i+k]+=R[k,j]; M[r,2*k+j]-=T[i,k]
    return M
def solve_g(Rl,Tl,tol=1e-9):
    S=np.vstack([_block(R,T) for R,T in zip(Rl,Tl)])
    u,s,vh=np.linalg.svd(S)
    if s[-1]<tol:
        g=vh[-1].conj().reshape(2,2)
        if abs(np.linalg.det(g))>1e-6: return g/np.sqrt(np.linalg.det(g)),s[-1]
    return None,s[-1]
wn=-0.5+np.sqrt(3)/2*1j
An=np.array([[1,1],[0,1]],complex); Bn=np.array([[1,0],[-wn,1]],complex)
gn={'a':An,'A':np.linalg.inv(An),'b':Bn,'B':np.linalg.inv(Bn)}
def wnum(s):
    R=np.eye(2,dtype=complex)
    for c in s: R=R@gn[c]
    return R

def test_B_untwisted_FALSE():
    # (B) FALSE: no g with g rho = rho-bar g
    g,res=solve_g([An,Bn],[np.conj(An),np.conj(Bn)])
    assert g is None and res>0.5      # residual ~1.0, no intertwiner

def test_amphichiral_twisted_TRUE_and_phi_OUTER():
    # phi: a->a, b->bAbaB ; rho-bar ~ rho o phi
    Ra,Rb=wnum('a'),wnum('bAbaB')
    g,res=solve_g([Ra,Rb],[np.conj(An),np.conj(Bn)])
    assert g is not None and res<1e-9
    assert np.linalg.norm(g@Ra@np.linalg.inv(g)-np.conj(An))<1e-9
    assert np.linalg.norm(g@Rb@np.linalg.inv(g)-np.conj(Bn))<1e-9
    # phi preserves relator (is an automorphism at the faithful rep level)
    inv=lambda word: word[::-1].swapcase()
    phi={'a':'a','b':'bAbaB'}; phi['A']=inv(phi['a']); phi['B']=inv(phi['b'])
    rel=''.join(phi[c] for c in 'abABaBAbaB')
    assert np.linalg.norm(wnum(rel)-np.eye(2))<1e-9
    # phi is OUTER: no single inner conjugator realises a->a, b->bAbaB
    h,resi=solve_g([An,Bn],[wnum('a'),wnum('bAbaB')])
    assert h is None and resi>0.1

def test_C_controls_both_real_forms():
    # (B)<=>(C): both FS signs land in a real form (no obstruction at SL(2))
    # SL(2,R): real rep, FS +1
    A1=np.array([[2,1],[1,1]],complex); B1=np.array([[1,1],[1,2]],complex)
    g,res=solve_g([A1,B1],[np.conj(A1),np.conj(B1)])
    assert res<1e-9 and abs((np.conj(g)@g)[0,0]-1)<1e-6      # FS = +1 (real)
    # SU(2): quaternionic, FS -1
    th,ph=0.7,1.1
    U1=np.array([[np.cos(th),np.sin(th)],[-np.sin(th),np.cos(th)]],complex)
    U2=np.array([[np.exp(1j*ph),0],[0,np.exp(-1j*ph)]],complex)
    g,res=solve_g([U1,U2],[np.conj(U1),np.conj(U2)])
    lam=np.conj(g)@g
    assert res<1e-9 and abs(lam[0,0]+1)<1e-6                 # FS = -1 (quaternionic)
    assert np.linalg.norm(lam-lam[0,0]*np.eye(2))<1e-9       # scalar => clean sign

def test_C_object_no_real_form():
    # (C) FALSE by the SAME fact as (A): a real form has ALL traces real; tr(ab) is not.
    t=complex(np.trace(wnum('ab')))
    assert abs(t.imag)>0.5    # -sqrt(3)/2 ~ -0.866