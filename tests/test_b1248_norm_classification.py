"""B1248 -- eps is the Fricke invariant read modulo squares.

Locks the law  det X * (cq-br)^2 = 2 - kappa  and its integral trichotomy
    det X0 = squarefree part of (2 - kappa),
which closes B1192's named-open refinement cell ("the general norm-classification").

These are INVARIANT locks, not snapshot pins: no count is hard-coded, and each control is
identified by the mathematical property that makes it a control.
"""
import importlib.util
import pathlib

import pytest
import sympy as sp

_SRC = (pathlib.Path(__file__).resolve().parents[1]
        / "frontier" / "B1248_norm_classification" / "verification" / "norm_classification.py")
_spec = importlib.util.spec_from_file_location("b1248_norm_classification", _SRC)
nc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(nc)


def test_selftest_passes():
    assert nc.selftest(verbose=False) == []


def test_law_is_an_identity_not_a_fit():
    """The Groebner residue must be exactly zero and the denominator a perfect square."""
    residue, denom = nc.law_symbolic()
    assert residue == 0
    assert denom.is_Pow and denom.exp == 2


def test_kappa_is_the_fricke_vogt_invariant():
    """kappa = tr[A,M] must equal K001's x^2+y^2+z^2-xyz-2 (B167's first integral)."""
    A = sp.Matrix([[2, 1], [1, 1]])
    for M in (sp.Matrix([[2, 3], [1, 2]]), sp.Matrix([[5, 2], [2, 1]]), sp.Matrix([[8, 21], [3, 8]])):
        x, y, z = sp.trace(A), sp.trace(M), sp.trace(A * M)
        assert nc.kappa(A, M) == sp.expand(x**2 + y**2 + z**2 - x * y * z - 2)


def test_b1192_crown_positive_reproduced_exactly():
    """B1192 banked det X0 = -1 for the sqrt3 partner. The law must GIVE that number."""
    k, D, pred, obs = nc.classify(sp.Matrix([[2, 3], [1, 2]]))
    assert k == 3 and 2 - k == -1
    assert D == -1 and pred == "DIRECT-1" == obs


def test_b1189_kill_is_the_reducibility_locus():
    """(A,A) has no bit because kappa = 2 -- Fricke reducibility -- not as a separate fact."""
    k, D, pred, obs = nc.classify(nc.A_OBJ)
    assert k == 2 and D == 0
    assert pred == "DEGENERATE" and obs == "rank 2"


def test_object_alone_carries_no_bit_and_the_cusp_is_the_reason():
    """m004's once-punctured-torus fibre has parabolic commutator kappa = -2, so D = +1."""
    w = sp.Rational(-1, 2) + sp.sqrt(-3) / 2
    a = sp.Matrix([[1, 1], [0, 1]])
    b = sp.Matrix([[1, 0], [-w, 1]])
    k = sp.simplify(nc.kappa(a * nc.inv(b), nc.inv(b) * a))
    assert k == -2                       # parabolic: the cusp
    assert nc.squarefree(2 - k) == 1     # trivial class -> no bit


def test_eps_minus_one_iff_2_minus_kappa_equals_minus_g_squared():
    """CORRECTED criterion (a peer seat's formula, verified here).

    The old form 'eps = -1 iff kappa - 2 is a perfect square' is FALSE: at 2 - kappa = -121
    with entry-gcd 1 the true det X0 is -121 (torsor), not -1 (bit).
    """
    A = nc.A_OBJ
    for M in list(nc.EXTRA.values()) + [m for m, _ in nc.BANKED.values()]:
        k = int(nc.kappa(A, M))
        if k == 2:
            continue
        D, g = nc.additive_commutator_det(M, A)
        assert (D == -1) == (2 - k == -g * g)


def test_the_additive_commutator_formula_beats_squarefree():
    """The counterexample that overturned this arc's first integral refinement.

    2 - kappa = -121 = -(11^2), entry-gcd 1: the ACTUAL integral realizer has det -121
    (TORSOR), while squarefree(-121) = -1 would have called it THE BIT.
    """
    A = nc.A_OBJ
    M = sp.Matrix([[-7, -9], [4, 5]])
    k = int(nc.kappa(A, M))
    assert 2 - k == -121
    D, g = nc.additive_commutator_det(M, A)
    real = int(sp.det(nc.realizer_module(A, M)[0]))
    assert real == -121                       # the truth
    assert D == real                          # the peer formula gets it
    assert nc.squarefree(2 - k) == -1         # the old formula does not
    assert nc.squarefree(2 - k) != real


def test_det_of_additive_commutator_is_2_minus_kappa():
    """det(AM - MA) = 2 - kappa exactly -- the identity behind the corrected formula."""
    A = nc.A_OBJ
    for M in list(nc.EXTRA.values()) + [m for m, _ in nc.BANKED.values()]:
        assert sp.det(A * M - M * A) == 2 - nc.kappa(A, M)


def test_one_pair_does_not_license_a_field_conclusion():
    """A peer seat's catch: B1192's sqrt2 control fixed ONE matrix and spoke of the field.

    Both determinant signs occur inside the SAME trace field Q(sqrt2).
    """
    A = nc.A_OBJ
    minus = sp.Matrix([[-35, -36], [1, 1]])
    plus = sp.Matrix([[-29, -12], [-12, -5]])
    for M in (minus, plus):
        t = int(sp.trace(M))
        assert nc.squarefree(t * t - 4) == 2          # trace field is exactly Q(sqrt2)
    assert nc.additive_commutator_det(minus, A)[0] == -1
    assert nc.additive_commutator_det(plus, A)[0] == 1


def test_det_minus_one_partner_admits_no_realizer():
    """det M = -1 forces tr M = 0, so a partner with det -1 and nonzero trace has no realizer."""
    M = sp.Matrix([[1, 2], [1, 1]])
    assert sp.det(M) == -1 and sp.trace(M) != 0
    assert nc.realizer_module(nc.A_OBJ, M) == []


def test_trichotomy_is_non_vacuous_in_every_branch():
    """MB12: the criterion must be able to return each verdict, or it discriminates nothing."""
    seen = {nc.classify(M)[2] for M in list(nc.EXTRA.values()) + [m for m, _ in nc.BANKED.values()]}
    assert {"DIRECT+1", "DIRECT-1", "TORSOR", "DEGENERATE"} <= seen


def test_maclachlan_reid_second_slot():
    """eps is the second Hilbert-symbol slot: B1^2 = (2 - kappa)/(tr^2 A - 4)."""
    I2 = sp.eye(2)
    A = nc.A_OBJ
    for M in (sp.Matrix([[2, 3], [1, 2]]), sp.Matrix([[5, 2], [2, 1]]), sp.Matrix([[8, 21], [3, 8]])):
        trA = sp.trace(A)
        A0 = A - trA / 2 * I2
        B0 = M - sp.trace(M) / 2 * I2
        B1 = sp.expand(B0 - (sp.trace(A0 * B0) / sp.trace(A0 * A0)) * A0)
        assert sp.simplify(A0 * B1 + B1 * A0) == sp.zeros(2)
        sq = sp.simplify((B1 * B1)[0, 0])
        assert sp.simplify(sq - (2 - nc.kappa(A, M)) / (trA**2 - 4)) == 0


def test_2T_gives_the_hurwitz_quaternions():
    """The control that refuted the draft claim 'eps IS the second slot'.

    2T is the chain's own door (48 surjections pi_1(m004) -> 2T). Its quaternion algebra is
    known to be the Hurwitz quaternions (-1,-1). The wrong form (tr^2 A - 4, 2 - kappa) gives
    (-1,+1), split -- so this test would have caught the error at creation.
    """
    order, spectrum, algebra = nc.twoT_algebra()
    assert order == 24
    assert set(spectrum) == {-2, 0, 2}          # 2T's kappa spectrum is exactly three values
    assert algebra == (-1, -1)                  # Hurwitz, NOT the wrong form's (-1, +1)


def test_2T_carries_no_bit():
    """No pair in 2T has class -1: kappa - 2 in {-4, -2, 0} is never a positive perfect square."""
    _, spectrum, _ = nc.twoT_algebra()
    assert all(nc.squarefree(2 - k) != -1 for k in spectrum)
