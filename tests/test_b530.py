"""B530 locks — the full object's own grammar (Movement I of the natural history).

Everything the object 'said' when left alone, pinned: the golden breath (beta), the golden-section
decider/courier split (deciders weigh beta, ratio phi), the 7-of-16 grammar, the single symmetry
break (A->A), deterministic couriers, and the always-re-begin-from-a rule.
"""
import sympy as sp
from collections import Counter

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def _grow(n, seed='a'):
    w = seed
    for _ in range(n):
        w = ''.join(SUB[c] for c in w)
    return w


def test_golden_breath_and_split_exact():
    phi = (1 + sp.sqrt(5)) / 2
    sq = sp.sqrt(phi)
    beta = phi * (1 + sq)
    wa, wA, wb, wB = phi, phi * sq, sp.Integer(1), sq        # Perron weights of a, A, b, B
    deciders = sp.simplify(wa + wA)                          # a, A (they branch)
    couriers = sp.simplify(wb + wB)                          # b, B (they don't)
    assert sp.simplify(deciders - beta) == 0                 # deciders weigh EXACTLY the growth rate
    assert sp.simplify(deciders / couriers - phi) == 0       # deciders : couriers = phi (golden section)
    assert sp.simplify(deciders / (deciders + couriers) - 1 / phi) == 0   # decider fraction = 1/phi


def test_grammar_is_7_of_16():
    w = _grow(7)
    pairs = set(zip(w, w[1:]))
    assert len(pairs) == 7
    forbidden = {(x, y) for x in 'abAB' for y in 'abAB'} - pairs
    assert len(forbidden) == 9
    assert ('a', 'a') in forbidden and ('a', 'a') not in pairs   # no a-repeat


def test_single_symmetry_break_is_the_A_selfloop():
    allowed = {('a', 'b'), ('a', 'A'), ('b', 'A'), ('A', 'a'), ('A', 'A'), ('A', 'B'), ('B', 'a')}
    swap = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
    img = {(swap[x], swap[y]) for (x, y) in allowed}
    # the swap fixes the grammar EXCEPT for exactly one transition: the self-loop A->A
    assert allowed - img == {('A', 'A')}
    assert img - allowed == {('a', 'a')}


def test_couriers_deterministic_and_always_rebegin_from_a():
    w = _grow(7)
    succ = {}
    for x, y in zip(w, w[1:]):
        succ.setdefault(x, set()).add(y)
    assert succ['b'] == {'A'} and succ['B'] == {'a'}        # couriers never branch
    assert all(img[0] == 'a' for img in SUB.values())        # every image re-begins from a


def test_the_crack_is_the_symplectic_form():
    # Movement II: the growth M = swap-symmetric S + antisymmetric D; D is the standard symplectic 2-form.
    letters = 'abAB'
    M = sp.Matrix([[SUB[j].count(i) for j in letters] for i in letters])
    P = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])   # swap a<->A, b<->B
    D = sp.simplify(M - P * M * P)
    S = sp.simplify((M + P * M * P) / 2)
    assert D.T == -D                                         # antisymmetric
    assert sp.simplify(P * S * P) == S                       # S swap-symmetric
    assert sp.simplify(M - (S + D / 2)) == sp.zeros(4)       # M = S + D/2
    # in basis (a,A,b,B): D = J (+) J, the standard symplectic form, nondegenerate
    R = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])   # (a,b,A,B)->(a,A,b,B)
    Dr = R * D * R.T
    J = sp.Matrix([[0, -1], [1, 0]])
    assert Dr == sp.Matrix(sp.BlockDiagMatrix(J, J))
    assert D.det() == 1                                      # nondegenerate symplectic 2-form


def test_golden_at_three_levels():
    # Movement III: growth beta, split phi, inner decider ratio sqrt(phi).
    phi = (1 + sp.sqrt(5)) / 2
    sq = sp.sqrt(phi)
    # (1) decider-content: every letter emits 'aA'; only a emits an extra A
    proj = lambda s: ''.join(c for c in s if c in 'aA')
    assert proj(SUB['a']) == 'aAA'
    assert all(proj(SUB[L]) == 'aA' for L in 'bAB')
    # (2) inside the decider stream a:A = 1:sqrt(phi), empirically
    w = _grow(9)
    dec = proj(w)
    A, a = dec.count('A'), dec.count('a')
    assert abs(A / a - float(sq)) < 1e-3
    # (3) freq(a) = sqrt(phi) - 1 exactly (Perron weight phi / sum)
    wa, wb, wA, wB = phi, sp.Integer(1), phi * sq, sq
    S = sp.simplify(wa + wb + wA + wB)
    assert sp.simplify(wa / S - (sq - 1)) == 0


def test_pulse_is_the_object():
    # Movement IV: a marks image-boundaries exactly; return-words = images; derived seq = the object.
    for im in SUB.values():
        assert [i for i, c in enumerate(im) if c == 'a'] == [0]   # a only at position 0, never interior
    w = _grow(8)
    pos = [i for i, c in enumerate(w) if c == 'a']
    retwords = [w[pos[i]:pos[i + 1]] for i in range(len(pos) - 1)]
    assert set(retwords) == set(SUB.values())                     # return-words = the four images
    inv = {im: L for L, im in SUB.items()}
    derived = ''.join(inv[rw] for rw in retwords)
    assert derived == w[:len(derived)]                            # the pulse IS the object


def test_kappa_web_bB_is_the_unspoken_swap_fixed_pair():
    # Movement V: conversation graph = K4 minus bB; swap-fixed kappas = {aA, bB} = the symplectic pairs.
    from itertools import combinations
    w = _grow(8)
    adj = {frozenset((x, y)) for x, y in zip(w, w[1:]) if x != y}
    pairs = [frozenset(p) for p in combinations('abAB', 2)]
    absent = [p for p in pairs if p not in adj]
    assert absent == [frozenset(('b', 'B'))]                      # only bB never adjacent
    swap = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
    fixed = [p for p in pairs if {swap[x] for x in p} == set(p)]
    assert set(map(frozenset, fixed)) == {frozenset(('a', 'A')), frozenset(('b', 'B'))}  # swap-fixed kappas
    assert frozenset(('b', 'B')) in absent                        # the unspoken pair is swap-fixed (symplectic)


def test_four_letters_are_the_bootstrap_and_growth_is_dissipative():
    # Movement VI: copy-grouping {a,b},{A,B} gives M = [[F,F],[F^2,F]] = the B517 bootstrap; not symplectic.
    letters = 'abAB'
    M = sp.Matrix([[SUB[j].count(i) for j in letters] for i in letters])
    F = sp.Matrix([[1, 1], [1, 0]])
    assert M[0:2, 0:2] == F and M[0:2, 2:4] == F and M[2:4, 2:4] == F   # three blocks = F
    assert M[2:4, 0:2] == F * F                                          # bottom-left = F^2
    # => M = [[F,F],[F^2,F]] = M*
    assert M == sp.Matrix(sp.BlockMatrix([[F, F], [F * F, F]]))
    # growth is NOT symplectic w.r.t. its own 2-form D (static orientation, dissipative dynamics)
    D = sp.Matrix([[0, 0, -1, 0], [0, 0, 0, -1], [1, 0, 0, 0], [0, 1, 0, 0]])
    MtDM = M.T * D * M
    assert all(sp.simplify(MtDM - c * D) != sp.zeros(4) for c in (1, -1))   # not +/- D
    assert M.det() == -1                                                     # unimodular, dissipative


def test_breath_is_born_from_the_copy_inequality():
    # Movement VII: the complex mode exists ONLY for the unequal coupling F vs F^2.
    F = sp.Matrix([[1, 1], [1, 0]])
    blk = lambda tl, tr, bl, br: sp.Matrix(sp.BlockMatrix([[tl, tr], [bl, br]]))
    has_complex = lambda X: any(sp.im(e) != 0 for e in X.eigenvals())
    assert has_complex(blk(F, F, F * F, F))                 # the object M*: rotates
    assert not has_complex(blk(F, F, F, F))                 # symmetric coupling: no rotation
    assert not has_complex(blk(F, sp.zeros(2), sp.zeros(2), F))   # uncoupled: no rotation
    # the copies stand in ratio 1:sqrt(phi)
    phi = (1 + sp.sqrt(5)) / 2
    sq = sp.sqrt(phi)
    c1 = sp.simplify(phi + 1)               # copy1 {a,b}
    c2 = sp.simplify(phi * sq + sq)         # copy2 {A,B}
    assert sp.simplify(c2 / c1 - sq) == 0


def test_movement_VIII_convergence_and_chirality():
    x = sp.symbols('x')
    proj = lambda s, keep: ''.join(c for c in s if c in keep)
    # (chat1) letter-restricted = exact Fibonacci on each copy
    assert {L: proj(SUB[L], 'ab') for L in 'ab'} == {'a': 'ab', 'b': 'a'}
    assert {L: proj(SUB[L], 'AB') for L in 'AB'} == {'A': 'AB', 'B': 'A'}
    w = _grow(9)
    # (chat1) constant return number 4 for every letter
    for L in 'abAB':
        pos = [i for i, c in enumerate(w) if c == L]
        assert len({w[pos[i]:pos[i + 1]] for i in range(len(pos) - 1)}) == 4
    # (chat1) the derived substitution through 'a' reproduces the object (char poly); tail block included
    pos = [i for i, c in enumerate(w) if c == 'a']
    RW = sorted({w[pos[i]:pos[i + 1]] for i in range(len(pos) - 1)}, key=len)
    idx = {r: i for i, r in enumerate(RW)}
    M = sp.zeros(4, 4)
    for j, r in enumerate(RW):
        sr = ''.join(SUB[c] for c in r)
        p = [i for i, c in enumerate(sr) if c == 'a']
        blocks = [sr[p[k]:p[k + 1]] for k in range(len(p) - 1)] + [sr[p[-1]:]]
        for b in blocks:
            if b in idx:
                M[idx[b], j] += 1
    assert sp.expand(M.charpoly(x).as_expr() - (x**4 - 2*x**3 - 5*x**2 - 4*x - 1)) == 0
    # the SILVER is the incidence of tunnel-erasure -- but the ACTUAL decider frequency is GOLDEN sqrt(phi)
    eff = {L: proj(SUB[L], 'aA') for L in 'aA'}          # a->aAA, A->aA
    Meff = sp.Matrix([[eff[j].count(i) for j in 'aA'] for i in 'aA'])
    assert sp.factor(Meff.charpoly(x).as_expr()) == x**2 - 2*x - 1     # Perron 1+sqrt2 (silver incidence)
    dec = proj(w, 'aA')
    assert abs(dec.count('A') / dec.count('a') - float(sp.sqrt((1 + sp.sqrt(5)) / 2))) < 1e-2  # golden sqrt(phi)


def test_movement_IX_firewall_in_the_arithmetic():
    # the object's growth field: D4 quartic, disc -400; carries sqrt5 (golden end) but NOT sqrt-3/-15/-7.
    x = sp.symbols('x')
    p = x**4 - 2*x**3 - 5*x**2 - 4*x - 1
    assert sp.Poly(p, x).is_irreducible
    assert sp.discriminant(sp.Poly(p, x)) == -400
    reducible_over = lambda d: len(sp.factor_list(p, extension=sp.sqrt(d))[1]) > 1
    assert reducible_over(5)          # golden / E8 end IS inside
    assert not reducible_over(-3)     # Eisenstein / E6 end ABSENT
    assert not reducible_over(-15)    # the seam ABSENT
    assert not reducible_over(-7)     # chirality field ABSENT
    # disc -400 = -(20^2) => Q(sqrt(disc)) = Q(i): the Gaussian imaginary subfield (the breath), not Eisenstein
    assert sp.sqrt(sp.Integer(-400)) == 20 * sp.I


def test_movement_X_neutral_census_flat_and_all():
    # the flat invariants, banked with the same care (the anti-anticipation discipline).
    from sympy.matrices.normalforms import smith_normal_form
    M = sp.Matrix([[SUB[j].count(i) for j in 'abAB'] for i in 'abAB'])
    S = smith_normal_form(M, domain=sp.ZZ)
    assert [abs(S[i, i]) for i in range(4)] == [1, 1, 1, 1]        # trivial ZZ-module (unimodular, no torsion)
    assert M.det() == -1
    # special factors: max out-degree 2 for length >= 2 (minimal branching above Sturmian); p(n) increments 3/4
    w = _grow(8)
    p = []
    for k in (1, 2, 3, 4, 5, 6):
        facs = {w[i:i + k] for i in range(len(w) - k)}
        p.append(len(facs))
        maxdeg = max(len({w[i + k] for i in range(len(w) - k) if w[i:i + k] == f}) for f in facs)
        assert maxdeg == (3 if k == 1 else 2)
    assert p == [4, 7, 10, 13, 17, 20]                             # p(n): increments 3,3,3,4,3 ~ 3n+1


def test_movement_XI_third_witness_and_silver_artifact():
    x = sp.symbols('x')
    obj = x**4 - 2 * x**3 - 5 * x**2 - 4 * x - 1
    # (a) the old/new block PAIRS reproduce the object's polynomial -- a THIRD witness
    pairsub = {0: '23', 1: '230', 2: '21330', 3: '2130'}
    M = sp.zeros(4, 4)
    for j, im in pairsub.items():
        for ch in im:
            M[int(ch), j] += 1
    assert sp.expand(M.charpoly(x).as_expr() - obj) == 0
    # (b) the naive erase-tunnels skeleton is SILVER (1+sqrt2) -- the artifact, not the object
    MDD = sp.Matrix([[SUB[j].count(i) for j in 'aA'] for i in 'aA'])   # deciders a,A
    naive_perron = max(MDD.eigenvals(), key=lambda e: sp.re(sp.N(e)))
    assert sp.simplify(sp.nsimplify(naive_perron) - (1 + sp.sqrt(2))) == 0
    # the proper effective decider dynamics is the derived substitution -> the object (golden), banked in mvt VIII


def test_movement_XI_level1_floor_is_a_variety():
    # irreducible SL2(C) reps of the mapping torus F4 x|_phi Z = irreducible fixed points of the trace map.
    import numpy as np
    from scipy.optimize import least_squares
    np.random.seed(1)
    GENS = ['a', 'b', 'A', 'B']

    def unpack(z):
        z = z[:len(z) // 2] + 1j * z[len(z) // 2:]
        T = np.diag([z[0], 1 / z[0]])
        Ms = {g: np.array([[z[1 + 4 * i], z[2 + 4 * i]], [z[3 + 4 * i], z[4 + 4 * i]]], complex)
              for i, g in enumerate(GENS)}
        return T, Ms

    def wordmat(w, Ms, inv):
        P = np.eye(2, dtype=complex)
        for ch in w:
            P = P @ (Ms[ch] if ch in Ms else inv[ch.lower()])
        return P

    def resid(z):
        T, Ms = unpack(z)
        Ti = np.linalg.inv(T)
        inv = {g: np.linalg.inv(Ms[g]) for g in GENS}
        r = [T @ Ms[g] @ Ti - wordmat(SUB[g], Ms, inv) for g in GENS]
        d = np.array([np.linalg.det(Ms[g]) - 1 for g in GENS])
        flat = np.concatenate([m.ravel() for m in r] + [d])
        return np.concatenate([flat.real, flat.imag])

    sigs = set()
    for _ in range(60):                                              # small deterministic budget for CI
        s = least_squares(resid, np.random.randn(34) * 0.9, method='lm', max_nfev=1200)
        if s.cost < 1e-16:
            _, Ms = unpack(s.x)
            C = Ms['a'] @ Ms['b'] @ np.linalg.inv(Ms['a']) @ np.linalg.inv(Ms['b'])
            if abs(np.trace(C) - 2) > 1e-4:                          # irreducible
                sigs.add(tuple(round(np.trace(Ms[g]).real, 1) for g in GENS))
    assert len(sigs) >= 2       # the Level-1 quantum floor exists and is not a single point
