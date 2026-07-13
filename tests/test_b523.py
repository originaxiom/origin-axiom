"""B523 locks — the wrong-leap re-examination.

Cell 1 (C3/Malament): the four banked verbs carry four DIFFERENT causal types, so the Level-1
monoid preserves no single cone (only evolution gives a proper (3,1) Lorentzian cone).
Plus the incoming Level-1 handoff check: the stated free-product substitution is NOT an
automorphism (non-injective; det of the abelianization = 0, not -1), and |gamma| = 1/sqrt(phi).
"""
import numpy as np
import sympy as sp


def _boot(v):
    v = np.array(v, float)
    return np.block([[v, v], [v @ v, v]])


def _causal_type(M):
    """(#|eig|>1, #|eig|<1, #|eig|=1-or-0-degenerate) with det=0 flagged degenerate."""
    w = np.linalg.eigvals(M)
    aw = np.abs(w)
    n_exp = int(np.sum(aw > 1 + 1e-9))
    n_con = int(np.sum((aw < 1 - 1e-9) & (aw > 1e-9)))
    degenerate = bool(np.any(aw < 1e-9)) or abs(np.linalg.det(M)) < 1e-9
    return n_exp, n_con, degenerate


def test_C3_four_verbs_have_different_causal_types():
    F = [[1, 1], [1, 0]]      # evolution, det -1
    D = [[2, 0], [0, 2]]      # decimation, det 4
    Dpd = [[1, 2], [1, 0]]    # decimation pd, det -2
    T = [[1, 1], [1, 1]]      # TM/erasure, det 0
    # evolution: exactly one expanding direction (proper (3,1)), invertible
    ne, nc, deg = _causal_type(_boot(F))
    assert (ne, nc, deg) == (1, 3, False)
    # decimation 2I: TWO expanding directions -> (2,2), not a single-time cone
    ne, nc, deg = _causal_type(_boot(D))
    assert ne == 2 and not deg
    # decimation pd: THREE expanding -> inverted, multiple time directions
    ne, nc, deg = _causal_type(_boot(Dpd))
    assert ne == 3 and not deg
    # TM/erasure: det 0 -> degenerate (non-invertible), not a causal automorphism
    assert abs(np.linalg.det(_boot(T))) < 1e-9
    ne, nc, deg = _causal_type(_boot(T))
    assert deg
    # => four different causal types; only evolution (det +-1) gives a proper (3,1) cone


def test_C3_only_evolution_bootstrap_is_unimodular():
    assert abs(round(np.linalg.det(_boot([[1, 1], [1, 0]])))) == 1   # evolution
    assert abs(np.linalg.det(_boot([[2, 0], [0, 2]]))) > 1           # decimation dissipative
    assert abs(np.linalg.det(_boot([[1, 1], [1, 1]]))) < 1e-9        # TM/erasure degenerate


def test_handoff_substitution_is_not_an_automorphism():
    # phi: a->abAB, b->aA, A->abaAB, B->aA  (rows a,b,A,B ; cols = images)
    M = sp.Matrix([[1, 1, 2, 1],
                   [1, 0, 1, 0],
                   [1, 1, 1, 1],
                   [1, 0, 1, 0]])
    assert M.det() == 0                       # NOT -1 as the handoff claims
    assert M[:, 1] == M[:, 3]                 # phi(b) == phi(B) == aA : non-injective


def test_handoff_gamma_modulus_is_golden_sqrt():
    phi = (1 + sp.sqrt(5)) / 2
    mod2 = sp.simplify((-1 / phi) ** 2 + (sp.sqrt(5) - 2))   # |gamma|^2 = 1/phi^2 + (sqrt5-2)
    assert sp.simplify(mod2 - 1 / phi) == 0                   # = 1/phi  =>  |gamma| = 1/sqrt(phi)


def test_corrected_substitution_is_injective_and_abelianizes_to_bootstrap():
    # corrected phi: a->abAAB, b->aAB, A->abAB, B->aA  (the fix for the broken handoff)
    imgs = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
    gens = ['a', 'b', 'A', 'B']
    assert imgs['b'] != imgs['B'] and len(set(imgs.values())) == 4     # injective (no collapse)
    x = sp.symbols('x')
    M = sp.Matrix([[imgs[g].count(gi) for g in gens] for gi in gens])
    # abelianizes to the bootstrap matrix M* = [[F,F],[F^2,F]] (same charpoly => conjugate over Q)
    F = sp.Matrix([[1, 1], [1, 0]])
    Mstar = sp.Matrix(sp.BlockMatrix([[F, F], [F * F, F]]))
    assert M.charpoly(x) == Mstar.charpoly(x)
    assert sp.expand(M.charpoly(x).as_expr()) == x**4 - 2*x**3 - 5*x**2 - 4*x - 1  # bootstrap beta minpoly
    assert M.det() == -1                                              # necessary for automorphism
    # primitive (Perron-Frobenius): (I+M)^3 entrywise > 0  -- necessary, NOT sufficient, for iwip
    P = ((sp.eye(4) + M) ** 3)
    assert all(P[i, j] > 0 for i in range(4) for j in range(4))
    # NOTE: iwip is NOT certified by these (needs Bestvina-Handel). Aut(F4) IS -- see below.


def test_corrected_substitution_is_an_automorphism_surjective_hopfian():
    """phi in Aut(F4) via surjectivity + Hopficity: all 4 generators are words in the images."""
    def inv(w):
        return [c[:-1] if c.endswith('~') else c + '~' for c in reversed(w)]

    def red(w):
        st = []
        for c in w:
            if st and ((st[-1].endswith('~') and st[-1][:-1] == c) or
                       (c.endswith('~') and c[:-1] == st[-1])):
                st.pop()
            else:
                st.append(c)
        return st

    img = {'a': ['a', 'b', 'A', 'A', 'B'], 'b': ['a', 'A', 'B'],
           'A': ['a', 'b', 'A', 'B'], 'B': ['a', 'A']}
    al, be, ga, de = img['a'], img['b'], img['A'], img['B']
    a = red(be + inv(al) + ga + inv(be) + de)          # a = beta alpha^-1 gamma beta^-1 delta
    B = red(inv(de) + be)                               # B = delta^-1 beta
    A = red(inv(a) + de)                               # A = a^-1 delta
    b = red(inv(a) + red(ga + inv(be)) + a)            # b = a^-1 (gamma beta^-1) a
    assert a == ['a'] and b == ['b'] and A == ['A'] and B == ['B']  # all gens in im(phi)
    # => phi surjective => (F4 Hopfian) phi in Aut(F4).  Only iwip stays open (Bestvina-Handel).


def test_amphichiral_involution():
    """Door 2 / chat-1 C2 correction: J=[[0,1],[1,0]] does NOT commute with
    A1=[[2,1],[1,1]] (nor conjugate it to A1^-1); the correct orientation-
    reversing involution is C=[[1,0],[-1,-1]] with C A1 C^-1 = A1^-1."""
    A1 = np.array([[2, 1], [1, 1]])
    assert np.array_equal(A1, A1.T)                      # A1 symmetric (chat-1 right)
    J = np.array([[0, 1], [1, 0]])
    assert not np.array_equal(J @ A1, A1 @ J)            # J does NOT commute (chat-1 wrong)
    A1inv = np.array([[1, -1], [-1, 2]])                 # det A1 = 1
    assert np.array_equal(A1 @ A1inv, np.eye(2, dtype=int))
    assert not np.array_equal(J @ A1 @ J, A1inv)         # J does not give A1^-1 either
    C = np.array([[1, 0], [-1, -1]])
    assert round(np.linalg.det(C)) == -1                 # orientation-reversing
    assert np.array_equal(C @ A1 @ np.linalg.inv(C).round().astype(int), A1inv)  # correct involution


def test_amphichiral_signature_split():
    """Door 2 sharpened: Ad(C) on sl(2,R) for C=[[1,0],[-1,-1]] has eigenvalues
    +1,-1,-1; the -1 eigenspace is 2-dim with an INDEFINITE Killing form
    (signature (1,1)) -> amphichirality allows (3,1) OR (2,2), not a forced (3,1)."""
    import sympy as sp
    H = sp.Matrix([[1, 0], [0, -1]]); E = sp.Matrix([[0, 1], [0, 0]]); Fm = sp.Matrix([[0, 0], [1, 0]])
    basis = [H, E, Fm]
    C = sp.Matrix([[1, 0], [-1, -1]])
    assert C.trace() == 0 and C * C == sp.eye(2)          # C in sl(2,R), involution
    Cinv = C.inv()

    def coords(X):
        return [X[0, 0], X[0, 1], X[1, 0]]
    Ad = sp.Matrix([coords(C * X * Cinv) for X in basis]).T
    assert Ad.eigenvals() == {sp.Integer(1): 1, sp.Integer(-1): 2}   # +1, -1, -1

    def Bk(X, Y):
        return 4 * (X * Y).trace()
    ev = Ad.eigenvects()
    minus = [v for val, m, vecs in ev if val == -1 for v in vecs]
    w = [v[0] * H + v[1] * E + v[2] * Fm for v in minus]
    Gr = sp.Matrix(len(w), len(w), lambda i, j: Bk(w[i], w[j]))
    assert Gr.det() < 0                                    # indefinite -> signature (1,1)
    plus = [v for val, m, vecs in ev if val == 1 for v in vecs][0]
    Xp = plus[0] * H + plus[1] * E + plus[2] * Fm
    assert Bk(Xp, Xp) > 0                                  # +1 direction (C) is spacelike
