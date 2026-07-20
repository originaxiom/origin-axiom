"""B732 lock — B701's conjugation is the OUTER automorphism of A5 = PSL(2,F4) = PSL(2,O_3)/Gamma((2)).
Complex conjugation on O_3 (w->w^2) reduces mod 2 to the F4-Frobenius, which swaps the two 5-cycle
classes of A5 -> outer. Pure finite-group arithmetic (Gate 5).
"""
# F4 = {0,1,2=w,3=1+w}, w^2=w+1, char 2. add=XOR, mult table:
_MT = [[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]]
def _add(x, y): return x ^ y
def _mul(x, y): return _MT[x][y]
def _frob(x): return _mul(x, x)          # Frobenius x -> x^2
def _matmul(M, N):
    a,b,c,d = M; e,f,g,h = N
    return (_add(_mul(a,e),_mul(b,g)), _add(_mul(a,f),_mul(b,h)),
            _add(_mul(c,e),_mul(d,g)), _add(_mul(c,f),_mul(d,h)))
def _det(M): a,b,c,d = M; return _add(_mul(a,d),_mul(b,c))
_SL = [(a,b,c,d) for a in range(4) for b in range(4) for c in range(4) for d in range(4) if _det((a,b,c,d))==1]
def _order(M):
    I=(1,0,0,1); P=M; o=1
    while P!=I: P=_matmul(P,M); o+=1
    return o

def test_conjugation_is_frobenius_mod2():
    # complex conjugation w->w^2 on O_3 reduces mod 2 to the F4-Frobenius, swapping w(=2) and 1+w(=3).
    assert {x:_frob(x) for x in range(4)} == {0:0, 1:1, 2:3, 3:2}

def test_A5_and_two_5classes():
    assert len(_SL) == 60                                  # SL(2,F4) = A5
    o5 = [M for M in _SL if _order(M)==5]
    assert len(o5) == 24                                   # 24 order-5 elements
    traces = {}
    for M in o5:
        t = _add(M[0], M[3]); traces[t] = traces.get(t,0)+1
    assert traces == {2:12, 3:12}                          # two 5-classes by trace w / 1+w

def test_frobenius_swaps_the_5classes_hence_outer():
    o5 = [M for M in _SL if _order(M)==5]
    def tr(M): return _add(M[0], M[3])
    def fm(M): return tuple(_frob(x) for x in M)
    # Frobenius sends trace t -> t^2, swapping the two classes -> NOT inner (inner preserves classes)
    assert all(tr(fm(M)) == _frob(tr(M)) for M in o5)
    c5A = {M for M in o5 if tr(M)==2}; c5B = {M for M in o5 if tr(M)==3}
    assert all(fm(M) in c5B for M in c5A)                  # frob(5A) subset 5B -> swap -> OUTER automorphism
