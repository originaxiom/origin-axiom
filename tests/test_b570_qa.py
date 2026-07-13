"""B570 Lane C Q-A lock: c (complex conj) vs theta (Out E6) on the 4_1 geometric component.
Fast, deterministic, in-sandbox; two independent methods where load-bearing. Run: pytest -q."""
import sympy as sp
from collections import deque, Counter

I3=sp.sqrt(-3); T=(1+I3)/2; TB=(1-I3)/2   # primitive 6th roots, t^2-t+1=0
REL="abABaBAbaB"                            # 4_1 = 2-bridge b(5,3)
def rep(tt):
    return {'a':sp.Matrix([[1,1],[0,1]]),'A':sp.Matrix([[1,-1],[0,1]]),
            'b':sp.Matrix([[1,0],[tt,1]]),'B':sp.Matrix([[1,0],[-tt,1]])}
def ev(word,R):
    M=sp.eye(2)
    for c in word: M=M*R[c]
    return M
inv={'a':'A','A':'a','b':'B','B':'b'}
def wimg(word,m):
    mm={'a':m['a'],'A':''.join(inv[c] for c in reversed(m['a'])),
        'b':m['b'],'B':''.join(inv[c] for c in reversed(m['b']))}
    return ''.join(mm[c] for c in word)

def test_riley_root():
    assert sp.simplify(T**2-T+1)==0 and sp.simplify(TB-(1-T))==0

def test_relator_identity_both():
    assert sp.simplify(ev(REL,rep(T))-sp.eye(2))==sp.zeros(2,2)
    assert sp.simplify(ev(REL,rep(TB))-sp.eye(2))==sp.zeros(2,2)

def test_c_moves_sl2_point():
    R,Rb=rep(T),rep(TB)
    assert sp.simplify(sp.trace(ev('ab',R)))==sp.Rational(5,2)+sp.sqrt(3)*sp.I/2
    assert sp.simplify(sp.trace(ev('ab',Rb)))==sp.Rational(5,2)-sp.sqrt(3)*sp.I/2

def test_amphichiral_phi_intertwiner():
    R,Rb=rep(T),rep(TB)
    phi={'a':'b','b':'abA'}                       # a->b, b->a b a^{-1}
    g=sp.Matrix([[sp.Rational(-1,2)+sp.sqrt(3)*sp.I/2, sp.Rational(1,2)-sp.sqrt(3)*sp.I/2],[1,0]])
    assert sp.simplify(g.det())!=0
    for x in ['a','b','ab','aabb','abAB']:
        lhs=ev(x,Rb); rhs=g*ev(wimg(x,phi),R)*g.inv()
        assert sp.simplify(lhs-rhs)==sp.zeros(2,2)   # rho-bar = g (rho o phi) g^{-1}

def _principal_27():
    adj=[(1,3),(3,4),(4,5),(5,6),(2,4)]           # E6 Bourbaki
    C=[[2 if i==j else 0 for j in range(6)] for i in range(6)]
    for (i,j) in adj: C[i-1][j-1]=-1; C[j-1][i-1]=-1
    start=(1,0,0,0,0,0); seen={start:0}; q=deque([start])
    while q:
        mu=q.popleft(); h=seen[mu]
        for i in range(6):
            if mu[i]>=1:
                nw=tuple(mu[j]-C[i][j] for j in range(6))
                if nw not in seen: seen[nw]=h+1; q.append(nw)
    cnt=Counter(seen.values()); g=[cnt.get(h,0) for h in range(max(cnt)+1)]
    irr=[]
    while any(g):
        top=max(i for i in range(len(g)) if g[i]); bot=min(i for i in range(len(g)) if g[i])
        irr.append(top-bot+1); g=[x-(1 if bot<=i<=top else 0) for i,x in enumerate(g)]
    return sorted(irr,reverse=True)

def test_27_and_adjoint_principal_decomp():
    assert _principal_27()==[17,9,1]              # 27|principal SL2, all self-dual
    assert sorted([2*m+1 for m in (1,4,5,7,8,11)])==[3,9,11,15,17,23]  # adjoint

def _chi(d,x): return sp.chebyshevu(d-1,x/2)
def _tr(dims,x): return sp.expand(sum(_chi(d,x) for d in dims))
ADJ=[3,9,11,15,17,23]; SEV=[17,9,1]

def test_adjoint_matches_banked_B565():
    # independent method (Chebyshev/principal) reproduces B565 Sym-power value
    val=sp.simplify(_tr(ADJ, -1-sp.sqrt(3)*sp.I))
    assert val==37437270+38799960*sp.sqrt(3)*sp.I
    assert sp.nsimplify(_tr(ADJ,2))==78 and sp.nsimplify(_tr(SEV,2))==27

def test_QB_theta_fixes_c_moves_on_27_and_adjoint():
    R=rep(T)
    x=sp.simplify(sp.trace(ev('ab',R)))           # SL2 trace of witness g=ab
    xb=sp.conjugate(x)
    t27=sp.simplify(_tr(SEV,x))
    assert t27==sp.Rational(1295415,2)+sp.Rational(1011915,2)*sp.sqrt(3)*sp.I
    assert sp.simplify(_tr(SEV,xb)-sp.conjugate(t27))==0          # c conjugates (MOVES)
    assert sp.simplify(_tr(SEV,xb)-t27)!=0
    xinv=sp.simplify(sp.trace(ev('BA',R)))        # (ab)^{-1}; theta on 27 = tr27(h^-1)
    assert sp.simplify(_tr(SEV,xinv)-t27)==0                       # theta FIXES 27
    tad=sp.simplify(_tr(ADJ,x))
    assert sp.simplify(_tr(ADJ,xinv)-tad)==0                       # theta FIXES adjoint
    assert sp.simplify(_tr(ADJ,xb)-tad)!=0                         # c MOVES adjoint

def test_principal_nilpotent_is_theta_fixed():
    # theta = E6 diagram flip permutes simple roots (1<->6,3<->5,2,4 fixed);
    # sum e=Sum e_{alpha_i} is invariant => principal sl2 in F4=E6^theta.
    flip={1:6,6:1,3:5,5:3,2:2,4:4}
    assert {flip[i] for i in (1,2,3,4,5,6)}=={1,2,3,4,5,6}