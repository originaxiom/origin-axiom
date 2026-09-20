"""Finite exact controls of F02; the universal proof is in PROOF.md."""
import importlib.util
from pathlib import Path

import pytest
import sympy as s

spec = importlib.util.spec_from_file_location('complete_domain_controls', Path(__file__).with_name('verify.py'))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


@pytest.mark.parametrize('n', [1, 2, 3])
def test_creation_contraction_clifford_and_parity(n):
    es, ins, cs, hs = v.clifford(n)
    eye = s.eye(2**n)
    zero = s.zeros(2**n)
    grading = s.diag(*[(-1)**i.bit_count() for i in range(2**n)])
    for i in range(n):
        assert cs[i].H == -cs[i]
        assert hs[i].H == hs[i]
        assert grading*hs[i]+hs[i]*grading == zero
        for j in range(n):
            delta = int(i == j)
            assert es[i]*ins[j]+ins[j]*es[i] == delta*eye
            assert cs[i]*cs[j]+cs[j]*cs[i] == -2*delta*eye
            assert hs[i]*hs[j]+hs[j]*hs[i] == 2*delta*eye
            assert cs[i]*hs[j]+hs[j]*cs[i] == zero


def test_symbol_norm():
    _, _, cs, _ = v.clifford(3)
    a = s.symbols('a:3', real=True)
    C = sum((a[i]*cs[i] for i in range(3)), s.zeros(8))
    assert s.simplify(C.H*C-sum(t*t for t in a)*s.eye(8)) == s.zeros(8)


def test_noncommuting_hermitian_potential():
    _, _, _, hs = v.clifford(3)
    ps = [s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
    assert ps[0]*ps[1]-ps[1]*ps[0] != s.zeros(2)
    P = sum((s.kronecker_product(hs[i], ps[i]) for i in range(3)), s.zeros(16))
    assert P.H == P


def test_cutoff_commutator_with_growing_potential():
    _, _, cs, hs = v.clifford(3)
    xs = s.symbols('x:3', real=True)
    chi = xs[0]*xs[1]+xs[2]**2
    vec = s.Matrix([xs[0]**k+xs[1]*xs[2] for k in range(8)])
    P = sum((hs[i]*xs[i]**3 for i in range(3)), s.zeros(8))
    def Q(w):
        return sum((cs[i]*w.diff(xs[i]) for i in range(3)), s.zeros(8, 1))+P*w
    expected = sum((cs[i]*s.diff(chi, xs[i])*vec for i in range(3)), s.zeros(8, 1))
    assert s.simplify(Q(chi*vec)-chi*Q(vec)-expected) == s.zeros(8, 1)


def test_hermiticity_mutant_is_rejected():
    _, _, _, hs = v.clifford(1)
    bad = hs[0]+s.I*s.eye(2)
    assert bad-bad.H == 2*s.I*s.eye(2)


def test_cusp_zero_residual_but_nonzero_norm():
    d = v.cusp_data()
    r, R, S, area, c = d['symbols']
    assert d['residual'] == 0
    assert s.simplify(d['norm']-2*area*c*c*(s.exp(2*R)-s.exp(2*S))) == 0
    assert s.limit(d['norm'].subs({area: 1, c: 1, S: 1}), R, s.oo) == s.oo


def test_zero_cusp_control():
    d = v.cusp_data()
    c = d['symbols'][-1]
    assert d['norm'].subs(c, 0) == 0


def test_two_cusp_signed_flux_balance():
    A, B = s.symbols('A B', positive=True)
    c1, c2 = B, -A
    assert s.simplify(2*A*c1+2*B*c2) == 0
    assert c1 != 0 and c2 != 0
    c = s.symbols('c', real=True)
    assert s.solve(2*A*c, c) == [0]


def test_complete_gaussian_even_kernel():
    x = s.symbols('x', real=True)
    f = s.exp(-x*x/2)
    assert v.q_line(s.Matrix([f, 0]), x, x) == s.zeros(2, 1)
    assert v.norm_integral(f, x) == s.sqrt(s.pi)


def test_odd_formal_solution_is_not_l2():
    x = s.symbols('x', real=True)
    g = s.exp(x*x/2)
    assert v.q_line(s.Matrix([0, g]), x, x) == s.zeros(2, 1)
    assert v.norm_integral(g, x) == s.oo


def test_oscillator_square_signs():
    x = s.symbols('x', real=True)
    f, g = s.Function('f')(x), s.Function('g')(x)
    w = s.Matrix([f, g])
    squared = v.q_line(v.q_line(w, x, x), x, x)
    expected = s.Matrix([-s.diff(f, x, 2)+(x*x-1)*f, -s.diff(g, x, 2)+(x*x+1)*g])
    assert s.simplify(squared-expected) == s.zeros(2, 1)


def test_free_complete_operator_not_bounded_below():
    x = s.symbols('x', real=True)
    R = s.symbols('R', positive=True)
    f = s.pi**(-s.Rational(1, 4))*R**(-s.Rational(1, 2))*s.exp(-x*x/(2*R*R))
    assert v.norm_integral(f, x) == 1
    norm_sq = v.norm_integral(s.diff(f, x), x)
    assert s.simplify(norm_sq-1/(2*R*R)) == 0
    assert s.limit(norm_sq, R, s.oo) == 0


@pytest.mark.parametrize('sign', [-1, 1])
def test_incomplete_half_line_has_deficiency_vectors(sign):
    x = s.symbols('x', real=True)
    w = s.exp(-x)*s.Matrix([1, sign*s.I])
    assert s.simplify(v.q_line(w, x, 0)-sign*s.I*w) == s.zeros(2, 1)
    assert sum(v.norm_integral(a, x, 0, s.oo) for a in w) == 1
