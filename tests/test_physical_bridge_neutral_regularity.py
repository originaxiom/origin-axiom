"""R49 exact algebra controls; not a numerical or independent global PDE proof."""
import importlib.util
from pathlib import Path

import pytest
import sympy as s

PATH = Path(__file__).resolve().parents[1]/"reports/physical_bridge_2026_09_05/neutral_regularity.py"
SPEC = importlib.util.spec_from_file_location("neutral_regularity_r49", PATH)
r = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(r)


def test_actual_positive_metrics_and_shear():
    h, ambient, pulled = r.geometry()
    assert r.zero(ambient-r.H_INF)
    assert r.zero(pulled-s.diag(s.Rational(3,4),s.Rational(3,8),s.Rational(3,4)))
    assert h[0,1] != 0
    assert r.H_INF[0,0] != r.H_INF[1,1]
    assert r.zero(2*r.J-r.D/4-r.H0)


def test_basis_reconstruction_and_positive_gram():
    g = r.gram()
    for i,b in enumerate(r.basis()):
        assert r.coordinates(b)==s.eye(15)[:,i]
    for i in range(1,16):
        assert g[:i,:i].det()>0
    assert not r.zero(g-s.eye(15))


def test_commutator_action_against_literal_matrices():
    g,aa,bb,ll,bs,_ = r.operators()
    for j,b in enumerate(r.basis()):
        assert aa[:,j]==r.coordinates(r.H0*b-b*r.H0)
        assert bb[:,j]==r.coordinates(r.N*b-b*r.N)
        assert ll[:,j]==r.coordinates((r.D*b-b*r.D)/2)
    assert r.zero(bs-r.ad(r.N.T))
    assert r.zero(r.adj(aa,g)-aa)
    assert r.zero(r.adj(ll,g)-ll)


def test_exterior_chain_and_omitted_structure_control():
    d0,d1,d2 = [r.differential(p) for p in range(3)]
    assert r.zero(d1*d0)
    assert r.zero(d2*d1)
    assert not r.zero(r.differential(1,True)*r.differential(0,True))


@pytest.mark.parametrize("degree", [0,1,2,3])
def test_all_degree_indicial_laplacians(degree):
    assert r.zero(r.laplacian(degree)-r.expected(degree))


def test_direct_component_expansion_is_independent():
    assert r.zero(r.independent_degree_one()-r.laplacian(1))
    for lam,nu in ((0,0),(s.Rational(1,2),0),(-2,3)):
        assert r.zero((r.independent_degree_one()-r.expected(1)).subs({r.LAM:lam,r.NU:nu}))


def test_full_and_zero_weight_potential_not_particle_count():
    g,_,_,_,_,tt = r.operators()
    assert r.zero(r.adj(tt,g)-tt)
    assert r.zero(tt.charpoly(r.Z).as_expr()-r.Z*(r.Z-2)**3*(r.Z-6)**11)
    assert r.zero(tt*(tt-2*s.eye(15))*(tt-6*s.eye(15)))
    inc,small,residue = r.zero_weight_restriction()
    assert inc.cols==9
    assert r.zero(residue)
    assert r.zero(small.charpoly(r.Z).as_expr()-r.Z*(r.Z-2)**3*(r.Z-6)**5)
    assert tt.rows-small.rows==6


def test_wrong_volume_metric_and_unsheared_radial_fail():
    assert not r.zero(r.laplacian(1,volume_weight=0)-r.expected(1))
    assert not r.zero(r.laplacian(1,wrong_metric=True)-r.expected(1))
    assert not r.zero(r.laplacian(1,unsheared=True)-r.expected(1))


def test_indicial_roots_and_threshold_exact():
    for potential,roots in ((0,(0,1)),(2,(-1,2)),(6,(-2,3))):
        poly=-r.LAM*r.LAM+r.LAM+potential
        assert set(s.solve(poly,r.LAM))==set(roots)
        assert all(root<=0 or root>=1 for root in roots)
    conjugated=s.expand((-r.LAM**2+r.LAM).subs(r.LAM,s.Rational(1,2)+s.I*r.NU))
    assert r.zero(conjugated-r.NU**2-s.Rational(1,4))
    assert s.Rational(1,4)/r.A_SCALE==s.Rational(1,3)
    # Positive nonzero longitudinal frequency shifts the coefficient upward.
    assert r.zero(r.expected(0).subs(r.NU,2)-r.expected(0).subs(r.NU,0)-s.Rational(16,3)*s.eye(15))


def test_nonzero_meridian_inverse_both_sides_and_zero_control():
    b=r.operators()[2]
    assert r.zero(b**5)
    assert not r.zero(b**4)
    m,inv=r.meridian_inverse()
    assert r.zero(m*inv-s.eye(15))
    assert r.zero(inv*m-s.eye(15))
    assert b.det()==0
    # A deliberately shortened inverse cannot recover the actual last term.
    bad=inv-(-r.Y)**4/(s.I*r.OM)**5*b**4
    assert not r.zero(m*bad-s.eye(15))


def test_integrability_and_collapse_factor_controls():
    assert r.power_integrable(s.Rational(3,8),2)
    assert not r.power_integrable(s.Rational(3,8),4)
    assert not r.power_integrable(s.Rational(1,4),4)
    assert r.power_integrable(0,4)
    for p in (2,4,8,20):
        eps=s.Rational(1,2)-1/s.Integer(2*p)
        assert eps< s.Rational(1,2)
        assert eps> s.Rational(1,2)-1/s.Integer(p)
        assert r.power_integrable(s.Rational(1,2)-eps,p)
