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
