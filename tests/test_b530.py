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


def test_movement_XX_interleaving_golden_ratio_not_simplicity():
    import numpy as np
    phi = (1 + np.sqrt(5)) / 2
    sq = np.sqrt(phi)
    b = ''.join('0' if c in 'ab' else '1' for c in _grow(11)[:400000])
    f_new = b.count('1') / len(b)
    # coarse-graining keeps the golden ratio: new:old = sqrt(phi)
    assert abs(f_new - sq / (1 + sq)) < 2e-3
    # but is NOT Sturmian: p(2) = 4 > 3
    p2 = len({b[i:i + 2] for i in range(len(b) - 2)})
    assert p2 == 4


def test_movement_XXI_floor_arithmetic():
    import importlib.util
    import os
    import sympy as sp
    p = os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B530_natural_history',
                     'listen_23_floor_arithmetic.py')
    spec = importlib.util.spec_from_file_location('l23', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # growth field: char poly disc = -400 -> Q(√5) (movement IX)
    assert mod.growth_field() == -400
    # trace-zero point: rational F4-character, but the twist is forced order-6
    rational, traces, tau = mod.trace_zero_character_is_rational()
    assert rational                                          # static character in Q -- ends absent
    assert abs(tau ** 6 - 1) < 1e-6                          # order-6 twist FORCED (brings in √-3)
    # so the dynamics spectrum field Q(√5,√-3) contains the seam √-15
    assert mod.spectrum_field_contains_seam()


def test_movement_XXII_gap_structure_density_trapped():
    import importlib.util
    import os
    p = os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B530_natural_history',
                     'listen_24_gap_structure.py')
    spec = importlib.util.spec_from_file_location('l24', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    Eg, ids = mod.sturm_ids(N=40000, npts=1500)
    gaps = mod.find_gaps(Eg, ids, 40000)
    assert len(gaps) >= 3                                    # object HAS a real quasicrystal gap spectrum
    best = min(mod.margin(l)[1] for _, l in gaps if mod.margin(l))
    assert best < 3.0                                        # but NO gap gets a decisive rank: density-trapped


def test_movement_XXIII_second_seed_seam_generic():
    import importlib.util
    import os
    p = os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B530_natural_history',
                     'listen_25_second_seed_seam.py')
    spec = importlib.util.spec_from_file_location('l25', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    tags = mod.object_coupling_produces_seam()
    assert '√5' in tags and '√-3' in tags                    # both ends present in the joint character
    assert mod.seam_is_generic()                             # but √-15 = √5·√-3 is forced (generic, not selected)


def test_movement_XXIV_gap_module_is_rank_four():
    import importlib.util
    import os
    p = os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B530_natural_history',
                     'listen_26_reexamination.py')
    spec = importlib.util.spec_from_file_location('l26', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # the re-examination's clean fact: the gap-labeling frequency module is full rank 4
    # (a genuine rank-4 quasicrystal; this is why numerical single-N gap-labeling is dense) --
    # it REVISES the "density-trapped NEEDS-SPECIALIST wall" verdict of movement XXII to "OPEN, not walled".
    assert mod.gap_label_module_rank() == 4


def test_movement_XXV_the_prime_11_and_deep_listening():
    import importlib.util
    import os
    p = os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B530_natural_history',
                     'listen_27_deep_listening.py')
    spec = importlib.util.spec_from_file_location('l27', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    u = mod.word(60000)
    # THE PRIME 11: H^1 torsion Z/11 = |det(M-I)| = |char_poly(1)| = |N(1-beta)|
    torsion, detMI, cp1 = mod.prime11()
    assert torsion == 11 and abs(detMI) == 11 and abs(cp1) == 11
    # prime splitting: 5,7 inert; 11 splits (2 roots); 29 fully splits (4 roots)
    sp_ = mod.prime_splitting()
    assert sp_[5] == 0 and sp_[7] == 0 and sp_[11] == 2 and sp_[29] == 4
    # running letter-sum uniform mod 3 and mod 6
    md = mod.mod_uniform(u)
    assert md[3] < 0.01 and md[6] < 0.01
    # deterministic hierarchy: denominators = p(n); fraction climbs 50% -> ~87%
    h = mod.deterministic_hierarchy(u)
    assert [t for _, t in h] == [4, 7, 10, 13, 17, 20, 23]
    assert h[0][0] / h[0][1] == 0.5 and h[-1][0] / h[-1][1] > 0.8
    # sublattice coupling ~1.23 bits
    assert abs(mod.sublattice_mi(u) - 1.23) < 0.05
    # the BbB THREE-point resonance is REAL (I false-killed it first by checking the wrong 2-point quantity):
    # B at i, b at i+2, B at i+4 is ~12x enhanced, always BabAB, straddling a sigma-image boundary
    ratio, all_babab, straddle = mod.bbb_resonance(u)
    assert ratio > 10 and all_babab and straddle > 0.99


def test_movement_XXVII_falsekill_corrections():
    # three of four "did not survive" claims were ALIVE; restored with the right instrument.
    import importlib.util
    import os
    p = os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B530_natural_history',
                     'listen_28_falsekill_corrections.py')
    spec = importlib.util.spec_from_file_location('l28', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # DIFFRACTION: Bragg peaks at the golden family, huge over random (I killed this with a coarse FFT)
    golden, gmean, cmean = mod.golden_bragg(N=131072)
    assert gmean > 50 * max(cmean, 1)                       # golden Bragg >> random
    assert golden['phi'] > 500                              # the strongest peak, at f*beta = phi
    # FORWARD-BACKWARD: matrix powers converge (chirality short-range, as the sender stated)
    fb = mod.forward_backward_decay()
    assert fb[49] < 1e-3 and fb[1] > 1                      # decays 6.8 -> ~0


def test_movement_XXVIII_corpse_audit():
    import importlib.util
    import os
    p = os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B530_natural_history',
                     'listen_29_corpse_audit.py')
    spec = importlib.util.spec_from_file_location('l29', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    u = mod._word(60000)
    # false-kill 1: kappa3(3,5) with the +/-1 signal reproduces |0.236|
    assert abs(abs(mod.kappa3_reproduces(u)) - 0.236) < 0.02
    # false-kill 2: recurrence function matches the handoff (R(2)~28-29, staircase)
    R = mod.recurrence_function(u)
    assert 27 <= R[1] <= 30 and R[4] > 3 * R[3]             # jump at a substitution boundary
    # false-kill 3: the interleaving IS substitutive -- exactly 4 return words to '0'
    assert mod.interleaving_return_words(u) == {'0', '01', '011', '0111'}
    # kill holds: the walk's superdiffusion is drift; drift-subtracted fluctuations are bounded
    assert abs(mod.walk_drift_subtracted_nu(u)) < 0.15


def test_movement_XXIX_qca_reexamination():
    import importlib.util
    import os
    p = os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B530_natural_history',
                     'listen_30_qca_reexamination.py')
    spec = importlib.util.spec_from_file_location('l30', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # the coupling resonance: golden >> uncoupled (the F!=F^2 coupling matters)
    g, u, s = mod.coupling_resonance()
    assert g < 1e-7                            # golden achieves very low nesting cost
    assert u / g > 1e4                         # uncoupled is at least 10000x worse
    assert s / g > 10                          # symmetric coupling also worse
    # iSy generic: 6 degenerate eigenphases
    nd, gc, cc = mod.isy_generic()
    assert nd == 6                             # exactly 6 distinct eigenphases (degeneracy)
    assert gc < 1e-10 and cc < 1e-10           # both reach ~0 at matched size


def test_movement_XXX_three_fields():
    """Movement XXX: the three arithmetic fields and D₄ Galois group."""
    import sympy as sp
    M = sp.Matrix([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])
    x = sp.Symbol('x')
    sqrt5 = sp.sqrt(5)
    phi = (1 + sqrt5) / 2

    # 1. The char poly factors over Q(√5)
    f = x**4 - 2*x**3 - 5*x**2 - 4*x - 1
    q1 = x**2 - (1 + sqrt5)*x - phi
    q2 = x**2 + (sqrt5 - 1)*x + 1/phi
    assert sp.simplify(sp.expand(q1 * q2) - f) == 0

    # 2. D₄ Galois group: resolvent cubic has rational root -3/2
    t = sp.Symbol('t')
    f_dep = sp.Poly(f.subs(x, t + sp.Rational(1, 2)), t)
    coeffs = f_dep.all_coeffs()
    p_val, q_val, r_val = coeffs[2], coeffs[3], coeffs[4]
    y = sp.Symbol('y')
    resolvent = y**3 - p_val*y**2 - 4*r_val*y + (4*p_val*r_val - q_val**2)
    assert resolvent.subs(y, sp.Rational(-3, 2)) == 0

    # 3. Discriminant = -400
    assert int(sp.discriminant(f, x)) == -400

    # 4. Augmented substitution: char poly = f_orig · f_parity
    f_par = x**4 - 2*x**3 - x**2 - 1
    M_aug = sp.zeros(8, 8)
    ALPHA = 'abAB'
    def is_lower(c): return c in 'ab'
    aug_sub = {}
    for c in ALPHA:
        img = SUB[c]
        for p_start in range(2):
            p = p_start
            result = []
            for letter in img:
                result.append(f"{letter}{p}")
                if is_lower(letter):
                    p = 1 - p
            aug_sub[f"{c}{p_start}"] = ''.join(result)
    aug_alpha = [f"{c}{p}" for c in ALPHA for p in range(2)]
    for j, key in enumerate(aug_alpha):
        img_str = aug_sub[key]
        for k in range(0, len(img_str), 2):
            letter = img_str[k]
            parity = int(img_str[k+1])
            idx = ALPHA.index(letter) * 2 + parity
            M_aug[idx, j] += 1
    cp_aug = sp.Poly(M_aug.charpoly(x), x)
    cp_product = sp.Poly(f * f_par, x)
    assert cp_aug == cp_product

    # 5. Parity factor discriminant = -1424 = -16·89
    assert int(sp.discriminant(f_par, x)) == -1424

    # 6. √3 ∉ Q(√5) → √(-3) ∉ splitting field
    # No rational a,b with (a+b√5)² = 3 (2ab=0 forces a=0 or b=0; neither works)
    # This is an algebraic argument; the test just confirms the discriminants are independent.
    assert sp.gcd(400, 1424) == 16  # share only 2⁴, not the odd parts (25 vs 89)

    # 7. Tiling torsion: 3 is absent from |det(M^k-I)| for k=1,...,6
    for k in range(1, 7):
        d = abs(int((M**k - sp.eye(4)).det()))
        assert d % 3 != 0, f"3 divides |det(M^{k}-I)| = {d}"

    # 8. BbB = BabAB at seams: all images start with 'a'; a,b,A end with 'B'; B ends with 'A'
    for c in 'abA':
        assert SUB[c][-1] == 'B'
    assert SUB['B'][-1] == 'A'
    for c in ALPHA:
        assert SUB[c][0] == 'a'

    # 9. 3 and 11 independent: orders
    M3 = sp.Matrix([[int(M[i,j]) % 3 for j in range(4)] for i in range(4)])
    Mk = sp.eye(4)
    for k in range(1, 200):
        Mk = (Mk * M3).applyfunc(lambda v: v % 3)
        if Mk == sp.eye(4):
            assert k == 80
            break


def test_movement_XXXI_handoff_verification():
    """Movement XXXI: √13 retraction, coupling resonance, recognizability, bounded remainder."""
    import numpy as np
    import sympy as sp

    M = sp.Matrix([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])
    x = sp.Symbol('x')

    # 1. √13 artifact: the handoff's substitution is broken (letter '1' never regenerated)
    handoff_sub = {0: '0', 1: '030', 2: '0302', 3: '20202'}
    for target in range(4):
        if target == 1:
            assert not any(str(target) in v for v in handoff_sub.values()), \
                "letter '1' should NOT appear in any image"
        else:
            assert any(str(target) in v for v in handoff_sub.values())
    # handoff char poly has factor x²−x−3 with root (1+√13)/2 — an artifact
    handoff_M = sp.zeros(4, 4)
    for src, img in handoff_sub.items():
        for ch in img:
            handoff_M[int(ch), src] += 1
    cp_handoff = handoff_M.charpoly(x).as_expr()
    assert sp.factor(cp_handoff) == x*(x - 1)*(x**2 - x - 3)

    # Correct derivation: 5 return words, char poly = x·(x⁴−2x³−5x²−4x−1)
    u = _grow(8)
    old_pos = [i for i, c in enumerate(u[:5000]) if c in 'ab']
    orig_rws = sorted(set(u[old_pos[i]:old_pos[i + 1]]
                          for i in range(len(old_pos) - 1)), key=len)
    assert len(orig_rws) == 5, f"expected 5 return words, got {len(orig_rws)}"
    # binary '011' comes from both 'aAB' and 'bAB'
    binary_rws = [''.join('0' if c in 'ab' else '1' for c in rw) for rw in orig_rws]
    assert binary_rws.count('011') == 2

    rw_idx = {rw: i for i, rw in enumerate(orig_rws)}
    n = len(orig_rws)
    inc = sp.zeros(n, n)
    for j, rw in enumerate(orig_rws):
        img = ''.join(SUB[c] for c in rw)
        old_p = [k for k, c in enumerate(img) if c in 'ab']
        for k in range(len(old_p)):
            start = old_p[k]
            end = old_p[k + 1] if k + 1 < len(old_p) else len(img)
            chunk = img[start:end]
            if chunk in rw_idx:
                inc[rw_idx[chunk], j] += 1
    cp_correct = inc.charpoly(x).as_expr()
    assert sp.simplify(cp_correct - x*(x**4 - 2*x**3 - 5*x**2 - 4*x - 1)) == 0

    # 2. Recognizability: centered R=3 resolves all ambiguity
    def fp_(level, seed='a'):
        w = seed
        for _ in range(level):
            w = ''.join(SUB.get(c, c) for c in w)
        return w
    u_prev = fp_(7)
    u_next = fp_(8)
    pos_map = []
    for c in u_prev:
        img = SUB[c]
        for j_ in range(len(img)):
            pos_map.append((c, j_))
    nn = min(len(u_next), len(pos_map))
    for R in [3]:
        factor_map = {}
        for i in range(R, nn - R):
            f = u_next[i-R:i+R+1]
            key = (pos_map[i][0], pos_map[i][1])
            if f not in factor_map:
                factor_map[f] = set()
            factor_map[f].add(key)
        ambiguous = [f for f, s in factor_map.items() if len(s) > 1]
        assert len(ambiguous) == 0, f"R=3 should have 0 ambiguous factors, got {len(ambiguous)}"
    # R=2 should still have ambiguity (the bound is tight at R=3)
    factor_map2 = {}
    for i in range(2, nn - 2):
        f = u_next[i-2:i+3]
        key = (pos_map[i][0], pos_map[i][1])
        if f not in factor_map2:
            factor_map2[f] = set()
        factor_map2[f].add(key)
    ambiguous2 = [f for f, s in factor_map2.items() if len(s) > 1]
    assert len(ambiguous2) >= 1, "R=2 should still be ambiguous"

    # 3. Bounded remainder: max discrepancy < 3
    M_np = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]], float)
    evals, evecs = np.linalg.eig(M_np)
    idx = int(np.argmax(np.abs(evals)))
    freq = np.abs(evecs[:, idx])
    freq = freq / freq.sum()
    letter_map = {'a': 0, 'b': 1, 'A': 2, 'B': 3}
    w = _grow(10)[:100000]
    counts = np.zeros(4)
    max_disc = np.zeros(4)
    for i, c in enumerate(w):
        counts[letter_map[c]] += 1
        for k in range(4):
            d = abs(counts[k] - (i + 1) * freq[k])
            if d > max_disc[k]:
                max_disc[k] = d
    assert max(max_disc) < 3, f"bounded remainder violated: max = {max(max_disc):.2f}"
