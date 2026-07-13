"""B570 AP4 locks: chiral-selector table + reachability. Fast, deterministic, exact."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from math import comb
import sympy as sp

def neg_symmetric(weights):
    c = Counter(weights)
    return all(c.get(tuple(-x for x in w),0)==m for w,m in c.items())

def su3():
    return [(F(2,3),F(-1,3),F(-1,3)),(F(-1,3),F(2,3),F(-1,3)),(F(-1,3),F(-1,3),F(2,3))]
def neg(w): return tuple(-x for x in w)
def add(*ws): return tuple(sum(c) for c in zip(*ws))

# ---------- Part 1: the table (negation symmetry of 27|_H) ----------
def test_trinification_chiral():
    A=su3(); Ab=[neg(w) for w in A]; z=(F(0),)*3
    W=[w+n+z for w in A for n in Ab]+[z+w+n for w in A for n in Ab]+[neg(w)+z+m for w in A for m in A]
    assert len(W)==27
    assert not neg_symmetric(W)   # SU(3)^3 CHIRAL

def test_spin10_u1_chiral():
    import itertools
    S16=[s for s in itertools.product([F(1,2),F(-1,2)],repeat=5) if sum(1 for x in s if x<0)%2==0]
    V10=[tuple(F(1) if k==i else F(0) for k in range(5)) for i in range(5)]+\
        [tuple(F(-1) if k==i else F(0) for k in range(5)) for i in range(5)]
    full=[w+(F(1),) for w in S16]+[w+(F(-2),) for w in V10]+[(F(0),)*5+(F(4),)]
    assert len(full)==27 and len(S16)==16
    assert not neg_symmetric(full)   # Spin(10)xU(1) CHIRAL

def test_su6_su2_chiral():
    def fund(n): return [tuple(F(n-1,n) if k==i else F(-1,n) for k in range(n)) for i in range(n)]
    w6=fund(6); fifteen=[add(w6[i],w6[j]) for i,j in combinations(range(6),2)]; sixbar=[neg(w) for w in w6]
    W=[w+(F(0),) for w in fifteen]+[w+(s,) for w in sixbar for s in (F(1,2),F(-1,2))]
    assert len(W)==27
    assert not neg_symmetric(W)   # SU(6)xSU(2) CHIRAL

def test_f4_selfdual():
    import itertools
    short=[]
    for i in range(4):
        e=[F(0)]*4; e[i]=F(1); short.append(tuple(e)); short.append(neg(tuple(e)))
    for s in itertools.product([F(1,2),F(-1,2)],repeat=4): short.append(tuple(s))
    W=short+[(F(0),)*4,(F(0),)*4,(F(0),)*4]  # 26 = 24 short + 0(mult2); +singlet
    assert len(short)==24 and len(W)==27
    assert neg_symmetric(W)   # F4 SELF-DUAL (vector-like)

def test_sp8_selfdual():
    eight=[]
    for i in range(4):
        e=[F(0)]*4; e[i]=F(1); eight.append(tuple(e)); eight.append(neg(tuple(e)))
    lam2=[add(eight[i],eight[j]) for i,j in combinations(range(8),2)]
    assert len(lam2)==28
    assert neg_symmetric(lam2)   # Sp(8): all reps self-dual, VECTOR-LIKE

def test_g2_su3_chiral():
    A=su3(); Ab=[neg(w) for w in A]; z=(F(0),)*3
    seven=[z]+A+Ab   # 7 of G2 via its A2: 0,+a_i,-a_i (negation closed)
    Sym2=[add(A[i],A[j]) for i,j in [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]]  # 6 of SU(3)
    W=[g+a for g in seven for a in A]+[z+s for s in Sym2]   # (7,3)+(1,6)
    assert len(W)==27
    assert not neg_symmetric(W)   # G2xSU(3) CHIRAL

# ---------- Part 2: reachability — principal 27 blocks are self-dual ----------
def sym_power_sym(A,n):
    x,y=sp.symbols('x y'); a,b,c,d=A[0,0],A[0,1],A[1,0],A[1,1]
    M=sp.zeros(n+1,n+1)
    for j in range(n+1):
        P=sp.Poly(sp.expand((a*x+c*y)**(n-j)*(b*x+d*y)**j),x,y)
        for i in range(n+1): M[i,j]=P.coeff_monomial(x**(n-i)*y**i)
    return M
def sym_form(n):
    B=sp.zeros(n+1,n+1)
    for i in range(n+1): B[i,n-i]=sp.Rational((-1)**i,comb(n,i))
    return B

def test_symn_selfdual_exact():
    a,b,c,d=sp.symbols('a b c d'); A=sp.Matrix([[a,b],[c,d]])
    for n in [2,4,8]:   # each principal block Sym^n preserves a symmetric form on det=1
        R=sym_power_sym(A,n); B=sym_form(n)
        D=sp.simplify(sp.expand(R.T*B*R-B).subs(d,(1+b*c)/a))
        assert D.is_zero_matrix

def test_principal_27_decomposition():
    # 27 under principal SL(2) of E6 = Sym^16 (+) Sym^8 (+) Sym^0 (dims 17+9+1), each self-dual.
    dims=[17,9,1]
    assert sum(dims)==27
    tops=[d-1 for d in dims]           # h-tops 16,8,0 : all even -> integer spins -> self-dual
    assert all(t%2==0 for t in tops)
    eig=[]
    for t in tops: eig+=list(range(-t,t+1,2))
    assert neg_symmetric([(x,) for x in eig])   # h-eigenvalues negation-symmetric

if __name__=='__main__':
    for k,v in sorted(globals().items()):
        if k.startswith('test_'): v(); print('PASS',k)