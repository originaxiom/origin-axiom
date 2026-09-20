"""F09 exact failable controls; global analytic steps are in PROOF.md."""
import importlib.util
from pathlib import Path
import sympy as s
import pytest

spec = importlib.util.spec_from_file_location('f09_verify', Path(__file__).with_name('verify.py'))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def zero(m):
    return v.clean(m) == s.zeros(*m.shape)


def test_exterior_full_lie_invariance_and_leibniz():
    a = s.Matrix(s.symbols('a0:4'))
    b = s.Matrix(s.symbols('b0:4'))
    k = v.volume_pairing()
    for x in v.lie_basis():
        l = v.f05.exterior_lie(x)
        assert zero(l.T*k+k*l)
        assert zero(l*v.exterior(a,b)-v.exterior(x*a,b)-v.exterior(a,x*b))


def test_induced_flatness_and_moment():
    c = v.six_connection()
    z = v.f08.z
    coords = v.f08.COORDS
    for i in range(3):
        for j in range(i+1,3):
            assert zero(c[j].diff(coords[i])-c[i].diff(coords[j])+c[i]*c[j]-c[j]*c[i])
    residual = sum((z**3*((c[i]+c[i].H)/z).diff(coords[i])
                    +z*z*(c[i]*c[i].H-c[i].H*c[i]) for i in range(3)), s.zeros(6))
    assert zero(residual)


def test_parallel_induced_higgs():
    a, psi = v.f08.split()
    a = tuple(v.f05.exterior_lie(x) for x in a)
    psi = tuple(v.f05.exterior_lie(x) for x in psi)
    for i in range(3):
        for j in range(3):
            r = psi[j].diff(v.f08.COORDS[i])+a[i]*psi[j]-psi[j]*a[i]
            r -= sum((v.f05.gamma()[k][i][j]*psi[k] for k in range(3)), s.zeros(6))
            assert zero(r)


@pytest.mark.parametrize('p', range(4))
def test_full_six_hodge_algebra(p):
    h = v.bochner(p)
    expected = {2:6} if p in (0,3) else {1:10,3:6,4:2}
    assert h == h.H
    assert h.eigenvals() == expected
    assert min(expected) >= 1
    if p in (1,2):
        # Independent block identity from commutators, not the same wedge sum.
        bs = v.six_boosts()
        n = h.rows//6
        alt = s.kronecker_product(s.eye(n), sum((b*b for b in bs), s.zeros(6)))
        for i in range(3):
            for j in range(3):
                alt += s.kronecker_product(v.f05.wedge(i,p-1)*v.f05.wedge(j,p-1).T,
                                           bs[i]*bs[j]-bs[j]*bs[i])
        assert zero(h-alt)


def test_volume_and_lorentz_exterior_maps():
    k, l, a = v.volume_pairing(), v.induced_j(), v.internal_s()
    assert k == k.T and k*k == s.eye(6)
    assert l.T*k*l == -k
    assert a.conjugate() == a and a.H*a == s.eye(6)
    assert a*a == -s.eye(6)
    for c in v.six_connection():
        assert zero(a*c-c*a)
        assert zero(l*c+c.T*l)


def test_antiunitary_hodge_blocks():
    for p in range(4):
        h = v.bochner(p)
        a = s.kronecker_product(s.eye(h.rows//6), v.internal_s())
        assert zero(a*h.conjugate()-h*a)
        assert a*a.conjugate() == -s.eye(h.rows)


def test_actual_twisted_global_descent_and_outside_control():
    for g in v.f05.geometric_matrices():
        r = v.f08.balanced_group(g)
        for phase in (1,-1,s.I,-s.I):
            m = v.f08.clean(v.f05.exterior_group(phase*r))
            assert zero(v.internal_s()*m.conjugate()-m*v.internal_s())
        phase = (1+s.I*s.sqrt(3))/2
        bad = v.f08.clean(v.f05.exterior_group(phase*r))
        assert not zero(v.internal_s()*bad.conjugate()-bad*v.internal_s())
        assert s.simplify(phase**4-1) != 0  # outside the same SL4 scalar class


def test_current_symmetry_and_antilinear_functor():
    u = s.Matrix(3,4,s.symbols('u0:12'))
    w = s.Matrix(3,4,s.symbols('v0:12'))
    for a,b,c in zip(v.current(u,w), v.current(w,u), v.current(v.anti4(u),v.anti4(w))):
        assert zero(a-b)
        assert zero(c-v.induced_j()*a.conjugate())


def test_full_vertex_mirror_relation():
    u = s.Matrix(3,4,s.symbols('u0:12'))
    w = s.Matrix(3,6,s.symbols('w0:18'))
    b = s.Matrix([[1+s.I,2,0,1],[0,-s.I,3,2],[1,0,1-s.I,4]])
    original = v.vertex(u,b,w)
    mirrored = v.vertex(v.anti4(u),v.anti4(b),v.anti6_dual(w))
    assert s.expand(mirrored+s.conjugate(original)) == 0


def test_cofactor_dictionary_for_general_tensor():
    b = s.Matrix(3,3,s.symbols('b0:9'))
    q = v.cross_rows(v.current(v.codazzi_profile(b),v.codazzi_profile(b)))
    assert zero(q-b.cofactor_matrix())


def test_tracefree_cofactor_and_real_norm():
    b = v.symmetric_tracefree(real=True)
    q = v.cross_rows(v.current(v.codazzi_profile(b),v.codazzi_profile(b)))
    assert zero(q-b*b+s.trace(b*b)*s.eye(3)/2)
    assert s.expand(s.trace(q.T*q)-s.trace(b*b)**2/4) == 0


def test_complex_rank_one_null_control():
    a = s.Matrix([1,s.I,0])
    b = a*a.T
    assert b != s.zeros(3) and b.T == b and s.trace(b) == 0
    assert b.rank() == 1 and b*b == s.zeros(3)
    assert all(zero(q) for q in v.current(v.codazzi_profile(b),v.codazzi_profile(b)))


def test_nonzero_repeated_profile_and_decomposable_zero():
    u = v.codazzi_profile(s.diag(1,-1,0))
    w = s.zeros(3,6)
    w[2,2] = 1  # e3-form times e0 wedge e3 coefficient
    assert v.vertex(u,u,w) == -1
    decomposable = s.Matrix([1,2,3])*s.Matrix([[2,1,4,3]])
    assert all(zero(q) for q in v.current(decomposable,decomposable))


def test_actual_wedge_statistics_and_profile_factor():
    w = s.zeros(3,6)
    w[2,2] = 1
    m = v.trilinear_matrix(w)
    assert m == m.T and m != s.zeros(12)
    spin = s.Matrix([[0,1],[-1,0]])
    grassmann = s.kronecker_product(spin,m)
    assert grassmann.T == -grassmann and grassmann != s.zeros(24)
    u = v.codazzi_profile(s.diag(1,-1,0))
    flat = s.Matrix(list(u))
    assert (flat.T*m*flat)[0] == 2*v.vertex(u,u,w)


def test_whole_space_response_equal_and_broken_positive_control():
    a = v.internal_s()
    j = s.Matrix([1+s.I,2-s.I,3,4+s.I,5,6-2*s.I])
    paired = a*j.conjugate()
    k = s.diag(2,3,4,4,3,2)
    assert k.is_positive_definite and a*k == k*a
    assert v.response(k,j) == v.response(k,paired)
    changed = s.diag(2,3,4,5,6,7)
    assert changed.is_positive_definite and a*changed != changed*a
    assert v.response(changed,j) != v.response(changed,paired)


def test_selected_mediator_is_not_whole_space():
    j = s.eye(6)[:,5]
    paired = v.internal_s()*j
    chosen = s.eye(6)[:,0]
    assert (chosen.T*j)[0] == 0
    assert abs((chosen.T*paired)[0]) == 1
    assert (j.H*j)[0] == (paired.H*paired)[0] == 1
