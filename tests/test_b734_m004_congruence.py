"""B734 lock — m004 IS congruence at level (2)^3=(8) (CORRECTING B731's wrong 'non-congruence').
The PSL image-index plateaus at 6 through level 4, then jumps to 12 (the geometric index) at level 8
-> Gamma contains Gamma((8)) -> congruence. Pure finite-group arithmetic (Gate 5).
"""
def _ring(m):
    def mul(p, q):
        (a, b), (c, d) = p, q
        return ((a*c - b*d) % m, (a*d + b*c - b*d) % m)   # O_3 = Z[w], w^2 = -w-1
    def add(p, q): return ((p[0]+q[0]) % m, (p[1]+q[1]) % m)
    def sub(p, q): return ((p[0]-q[0]) % m, (p[1]-q[1]) % m)
    return mul, add, sub

def _image(m, cap=60000):
    mul, add, sub = _ring(m); E, Z = (1, 0), (0, 0)
    def MM(X, Y):
        return (add(mul(X[0], Y[0]), mul(X[1], Y[2])), add(mul(X[0], Y[1]), mul(X[1], Y[3])),
                add(mul(X[2], Y[0]), mul(X[3], Y[2])), add(mul(X[2], Y[1]), mul(X[3], Y[3])))
    def inv(X): return (X[3], sub(Z, X[1]), sub(Z, X[2]), X[0])
    w = (0, 1)
    A = (E, E, Z, E); B = (E, Z, sub(Z, add(E, w)), E)           # figure-eight Riley generators
    gens = [A, inv(A), B, inv(B)]
    seen = {(E, Z, Z, E)}; fr = [(E, Z, Z, E)]
    while fr:
        nf = []
        for X in fr:
            for g in gens:
                Y = MM(X, g)
                if Y not in seen:
                    seen.add(Y); nf.append(Y)
                    if len(seen) > cap: return None
        fr = nf
    return seen

def _psl_index(m, psl_ambient):
    """PSL image-index using the known ambient |PSL(2,O_3/m)| (avoids re-generating the big ambient)."""
    mul, _, _ = _ring(m); Z = (0, 0)
    img = _image(m)
    centers = [(a, b) for a in range(m) for b in range(m) if mul((a, b), (a, b)) == (1, 0)]
    img_c = len([c for c in centers if (c, Z, Z, c) in img])
    return psl_ambient // (len(img) // img_c)

def test_m004_is_congruence_at_level_8():
    # |PSL(2,O_3/m)| known: 60 (lvl2), 960 (lvl4), 30720 (lvl8).
    assert _psl_index(2, 60) == 6          # plateau at 6 ...
    assert _psl_index(4, 960) == 6         # ... still 6 at level 4 (NOT stabilization -- the B731 trap)
    assert _psl_index(8, 30720) == 12      # JUMPS to 12 = geometric index at level 8
    # index 12 = [PSL(2,O_3):Gamma] => Gamma contains Gamma((8)) => m004 IS CONGRUENCE, level (2)^3=(8).

def test_the_B731_error_was_a_shallow_plateau():
    # the lesson (E22): index 6 at levels 2 AND 4 looked like stabilization but was NOT;
    # the congruence level is three 2-adic powers deep. Inferring non-congruence from a shallow
    # plateau is premature. (m003 the sister is at level (2)^1; m004 the knot at (2)^3.)
    assert _psl_index(2, 60) == _psl_index(4, 960) == 6   # the deceptive plateau
    assert _psl_index(8, 30720) == 12                     # the jump one level past where B731 stopped
