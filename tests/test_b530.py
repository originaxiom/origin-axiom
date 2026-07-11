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
