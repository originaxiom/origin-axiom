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


def test_movement_XII_eigenvector_geometry_of_the_growth():
    import numpy as np
    phi = (1 + np.sqrt(5)) / 2
    M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]], float)
    vals = np.linalg.eigvals(M)
    mags = sorted([abs(v) for v in vals], reverse=True)
    assert mags[0] > 1 and all(m < 1 for m in mags[1:])          # expand in 1, contract in 3
    gamma = [v for v in vals if abs(v.imag) > 1e-9][0]
    theta = np.angle(gamma)
    assert abs(abs(gamma) - 1 / np.sqrt(phi)) < 1e-9             # breath radius = 1/sqrt(phi)
    assert abs(gamma.real + 1 / phi) < 1e-9                      # Re(gamma) = -1/phi
    assert abs(np.cos(theta) + 1 / np.sqrt(phi)) < 1e-9          # cos(angle) = -1/sqrt(phi)
    # anti-anticipation: the breath angle is NOT the golden angle
    assert abs(np.degrees(theta) - np.degrees(2 * np.pi / phi**2)) > 3
    assert np.linalg.norm(M @ M.T - M.T @ M) > 1e-6             # non-normal (the breath needs it)


def test_movement_XIII_pisot_with_strong_coincidence():
    import numpy as np
    # irreducible unimodular primitive Pisot
    cp = sp.Poly(sp.symbols('x')**4 - 2 * sp.symbols('x')**3 - 5 * sp.symbols('x')**2
                 - 4 * sp.symbols('x') - 1, sp.symbols('x'))
    assert cp.is_irreducible
    roots = np.roots([1, -2, -5, -4, -1])
    beta = max(roots, key=lambda z: z.real).real
    assert all(abs(r) < 1 for r in roots if abs(r - beta) > 1e-6)          # Pisot
    M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]], float)
    assert abs(round(np.linalg.det(M))) == 1                               # unimodular

    def coincidence(sub, alph, maxn=14):
        def exp(s, n):
            for _ in range(n):
                s = ''.join(sub[c] for c in s)
            return s
        for a, i in enumerate(alph):
            for j in alph[a + 1:]:
                ok = False
                for n in range(1, maxn):
                    wi, wj = exp(i, n), exp(j, n)
                    for p in range(min(len(wi), len(wj))):
                        if wi[p] == wj[p] and tuple(wi[:p].count(c) for c in alph) == tuple(wj[:p].count(c) for c in alph):
                            ok = True
                            break
                    if ok:
                        break
                if not ok:
                    return False
        return True
    # code validated on controls, then applied to the object
    assert coincidence({'a': 'ab', 'b': 'ba'}, 'ab') is False              # Thue-Morse: singular spectrum
    assert coincidence({'a': 'ab', 'b': 'a'}, 'ab') is True                # Fibonacci: discrete spectrum
    assert coincidence(SUB, 'abAB') is True                                # OBJECT: strong coincidence
    assert all(SUB[c][0] == 'a' for c in 'abAB')                           # ...trivially (all images start with a)


def test_movement_XIV_rauzy_fractal_subtile_volumes_are_golden_tensor():
    import numpy as np
    idx = {c: i for i, c in enumerate('abAB')}
    u = _grow(11)[:120000]
    steps = np.zeros((len(u), 4))
    for k, c in enumerate(u):
        steps[k, idx[c]] = 1
    P = np.cumsum(steps, axis=0)
    M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]], float)
    vals, V = np.linalg.eig(M)
    W = np.linalg.inv(V)
    i_perr = int(np.argmax(vals.real))
    i_real = [i for i in range(4) if abs(vals[i].imag) < 1e-9 and i != i_perr][0]
    i_cplx = [i for i in range(4) if vals[i].imag > 1e-9][0]
    z = np.vstack([(W[i_real] @ P.T).real, (W[i_cplx] @ P.T).real, (W[i_cplx] @ P.T).imag]).T
    assert np.abs(z).max() < 5                                             # bounded compact fractal
    lab = np.array([idx[c] for c in u])
    phi = (1 + np.sqrt(5)) / 2
    sq = np.sqrt(phi)
    w = np.array([phi, 1, phi * sq, sq])
    w = w / w.sum()                                                        # golden-tensor freqs
    freq = np.array([(lab == i).mean() for i in range(4)])
    assert np.allclose(freq, w, atol=3e-3)                                 # subtile volumes = golden tensor


def test_movement_XV_discrete_spectrum_certificate():
    import importlib.util
    import os
    p = os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B530_natural_history',
                     'listen_17_discrete_spectrum_certificate.py')
    spec = importlib.util.spec_from_file_location('l17', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # the balanced pair algorithm must classify all five controls correctly...
    for name, sub, alph, want in mod.CONTROLS:
        assert mod.pure_discrete(sub, alph, wordlen=8000, maxlen=40)[0] is want, name
    # ...before we trust its verdict on the object: pure discrete spectrum, 0 bad pairs
    r = mod.pure_discrete(mod.SUB, 'abAB', wordlen=30000, maxlen=130)
    assert r[0] is True and r[2] == 0                                       # discrete, no bad pair
    assert r[3] < 130                                                       # no truncation (max word << bound)


def test_movement_XVI_entropy_and_golden_branching():
    import numpy as np
    from collections import Counter
    phi = (1 + np.sqrt(5)) / 2
    sq = np.sqrt(phi)
    u = _grow(11)[:500000]
    dig = Counter(u[i:i + 2] for i in range(len(u) - 1))
    uni = Counter(u[:-1])
    P = lambda x, y: dig[x + y] / uni[x]
    # topological entropy = log beta
    beta = phi * (1 + sq)
    assert abs(np.log(beta) - 1.3019) < 1e-3
    # exact golden branching
    assert abs(P('a', 'b') - 1 / phi) < 2e-3 and abs(P('A', 'B') - 1 / phi) < 2e-3
    # tunnels deterministic
    assert abs(P('b', 'A') - 1) < 1e-9 and abs(P('B', 'a') - 1) < 1e-9
    # after A, the remaining 1/phi^2 mass splits a:A in the breath ratio 1/sqrt(phi)
    assert abs(P('A', 'a') / P('A', 'A') - 1 / sq) < 3e-3
    # decider/courier is an ENTROPY split too: deciders carry bits, couriers zero
    Hb = -sum(p * np.log2(p) for p in [P('b', 'A')])
    assert Hb < 1e-9                                                        # tunnel b: zero entropy
    Ha = -sum(P('a', y) * np.log2(P('a', y)) for y in 'bA')
    assert Ha > 0.9                                                         # decider a: ~0.96 bits
    # Path A caught correction: lifted keep-verb eigenvalues are phi,phi,-1/phi,-1/phi (NOT +1/phi)
    F = np.kron(np.eye(2), np.array([[1, 1], [1, 0]]))
    assert sorted(np.round(np.linalg.eigvals(F).real, 3).tolist()) == [-0.618, -0.618, 1.618, 1.618]


def test_movement_XVII_phi_is_non_geometric():
    # Path B: sigma* conserves NO genus-2 boundary trace -> phi non-geometric -> Goldman inapplicable.
    import importlib.util
    import os
    p = os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B530_natural_history',
                     'listen_19_no_conserved_symplectic.py')
    spec = importlib.util.spec_from_file_location('l19', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    diffs = mod.boundary_not_conserved(seed=0)
    assert len(diffs) == 4
    for name, d in diffs.items():
        assert d > 1.0, name          # every candidate boundary changes -> none conserved


def test_movement_XVIII_rauzy_boundary_is_fractal():
    import importlib.util
    import os
    p = os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B530_natural_history',
                     'listen_20_rauzy_boundary_dimension.py')
    spec = importlib.util.spec_from_file_location('l20', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # calibrate: the method recovers Tribonacci's known boundary dimension ~1.0933
    tri = mod.rauzy(mod.TRIB, 'abc', 400000)
    tb = mod.boundary_dim(tri, [0.06, 0.045, 0.033, 0.025])
    assert 0.9 < tb < 1.3, tb
    # the object's Rauzy tile has a fractal boundary: dimension strictly between 2 and 3
    obj = mod.rauzy(mod.OBJ, 'abAB', 600000)
    ob = mod.boundary_dim(obj, [0.11, 0.085, 0.066, 0.051])
    assert 2.0 < ob < 3.0, ob


def test_movement_XIX_golden_ladder_at_trace_zero_point():
    import importlib.util
    import os
    import numpy as np
    p = os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B530_natural_history',
                     'listen_21_golden_ladder_point.py')
    spec = importlib.util.spec_from_file_location('l21', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    T, Ms = mod.trace_zero_point()
    # the special point is the trace-zero representation (every generator order 4)
    assert all(abs(np.trace(Ms[g])) < 1e-4 for g in 'abAB')
    assert all(np.allclose(Ms[g] @ Ms[g], -np.eye(2), atol=1e-4) for g in 'abAB')
    # its twist is a primitive 6th root of unity
    assert abs(T[0, 0] ** 6 - 1) < 1e-6 and abs(T[0, 0] ** 3 + 1) < 1e-6
    # and Dsigma* is exactly {phi,1,-1/phi} (x) {1,omega,omega^2}
    assert mod.ladder_matches(mod.dsigma_spectrum(T, Ms)) == 9
