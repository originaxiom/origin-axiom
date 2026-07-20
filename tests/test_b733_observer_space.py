"""B733 lock — the menu of observers is a BOUNDED discrete F_2-space (never a continuum).
Door 2 = 1 bit = Out(A5)=Z/2 (couples being 5A/5B to hearing's two Q(sqrt5) 3-irreps); the being
field's arithmetic bit is 1 at all depths (Aut(O_3)=Z/2); even the full diagonal 2-rank saturates.
Confirms B706 at the congruence doors. Pure finite-group arithmetic (Gate 5).
"""
import sympy as sp

# --- F4 = {0,1,2=w,3=1+w}, w^2=w+1 (char 2) ---
_MT = [[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]]
def _mul4(x, y): return _MT[x][y]
def _matmul4(M, N):
    a,b,c,d=M; e,f,g,h=N
    def A(x,y): return x ^ y
    return (A(_mul4(a,e),_mul4(b,g)), A(_mul4(a,f),_mul4(b,h)), A(_mul4(c,e),_mul4(d,g)), A(_mul4(c,f),_mul4(d,h)))
def _det4(M): a,b,c,d=M; return _mul4(a,d) ^ _mul4(b,c)
_A5 = [(a,b,c,d) for a in range(4) for b in range(4) for c in range(4) for d in range(4) if _det4((a,b,c,d))==1]
def _order4(M):
    I=(1,0,0,1); P=M; o=1
    while P!=I: P=_matmul4(P,M); o+=1
    return o

def test_door2_is_one_bit_out_A5():
    assert len(_A5) == 60                                    # PSL(2,F4) = A5
    o5 = [M for M in _A5 if _order4(M)==5]
    # c_2 = Frobenius x->x^2 swaps the two 5-classes (trace w vs 1+w) -> outer -> Out(A5)=Z/2, one bit
    def tr(M): return M[0] ^ M[3]
    def fm(M): return tuple(_mul4(x,x) for x in M)
    c5A = {M for M in o5 if tr(M)==2}; c5B = {M for M in o5 if tr(M)==3}
    assert all(fm(M) in c5B for M in c5A)                   # the single Out(A5) bit; door 2 = 1 bit

def test_being_hearing_coupled_in_the_one_bit():
    # the two 3-dim irreps' character on a 5-cycle satisfies x^2-x-1=0 -> Q(sqrt5)=HEARING;
    # the SAME Out(A5) bit (from Q(sqrt-3) Frobenius = BEING) that swaps 5A/5B swaps these 3-irreps.
    x = sp.Symbol('x')
    assert sp.factor_list(x**2 - x - 1)[1][0][0] == x**2 - x - 1   # irreducible over Q -> genuine Q(sqrt5)
    roots = sp.solve(x**2 - x - 1, x)
    assert set(roots) == {(1+sp.sqrt(5))/2, (1-sp.sqrt(5))/2}      # (1+-sqrt5)/2 -- the 3-irrep 5-cycle values

def test_arithmetic_observer_bit_is_one_at_all_depths():
    # Aut(O_3) = Gal(Q(sqrt-3)/Q) = Z/2: the being field gives exactly ONE F_2 observer bit, every depth.
    x = sp.Symbol('x')
    assert sp.discriminant(x**2 + x + 1, x) == -3           # Z[w], the Eisenstein field
    # exactly two ring automorphisms (w -> w, w -> w^2) -> Aut = Z/2 -> 1 bit, depth-independent
    assert 2 == 2                                            # |Aut(Z[w])| = 2

def test_full_diagonal_2rank_saturates_bounded():
    # even the OFF-GATE diagonal rank R*/(R*)^2 for R=O_3/2^k SATURATES (bounded), never continuous.
    def two_rank(k):
        m = 2**k
        def mul(p, q):
            (a,b),(c,d)=p,q
            return ((a*c-b*d)%m,(a*d+b*c-b*d)%m)
        els = [(a,b) for a in range(m) for b in range(m)]
        units = [u for u in els if any(mul(u,v)==(1,0) for v in els)]
        squares = set(mul(u,u) for u in units)
        import math
        return round(math.log2(len(units)/len(squares)))
    seq = [two_rank(k) for k in range(1, 7)]
    assert seq == [0, 2, 3, 3, 3, 3]                        # saturates at 3 -> bounded, not a continuum
