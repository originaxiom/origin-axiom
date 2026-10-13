import sympy as s
import pytest
import verify as v


def test_exact_guard_set():
    result = v.run()
    assert result['all_passed'], [k for k, passed in result['checks'].items() if not passed]


def test_noncoordinate_rejected():
    z = s.Symbol('z')
    for f in (z*z, z+1):
        with pytest.raises(ValueError):
            v.trace_ratio_squared(f, z)


def test_nontrivial_coordinate_correction_is_not_erased():
    z = s.Symbol('z')
    ratio = v.trace_ratio_squared(4*z+z*z, z)
    assert s.cancel(ratio-1) != 0
    assert ratio.subs(z, 0) == 1
    assert v.trace_ratio_squared(4*z+z*z, z, False).subs(z, 0) != 1


def test_fixed_index_allows_rank_jump():
    first = s.Matrix([[1, 0], [0, 1], [0, 0]])
    second = s.Matrix([[1, 0], [0, 0], [0, 0]])
    assert v.cohomology_dimensions(first) == (0, 1)
    assert v.cohomology_dimensions(second) == (1, 2)


def test_noninvariant_plane_detected():
    _, _, ms, mt, _, _ = v.data()
    p = s.diag(1, 0, 0, 0, 0, 0)
    assert not (v.zero(ms*p-p*ms) and v.zero(mt*p-p*mt))


def test_green_partner_cannot_be_copied_from_plus():
    _, _, _, _, p, _ = v.data()
    g = s.Matrix.vstack(s.Matrix.hstack(s.zeros(6), s.eye(6)),
                        s.Matrix.hstack(s.eye(6), s.zeros(6)))
    wrong = s.diag(p, p)
    assert not v.zero(wrong.H*g*wrong)


def test_selfadjointness_alone_does_not_force_grading():
    eye = s.eye(6)
    graph = s.Matrix.vstack(eye, s.I*eye)
    g = s.Matrix.vstack(s.Matrix.hstack(s.zeros(6), eye), s.Matrix.hstack(eye, s.zeros(6)))
    gamma = s.diag(eye, -eye)
    assert v.zero(graph.H*g*graph)
    assert s.Matrix.hstack(graph, gamma*graph).rank() == 12
