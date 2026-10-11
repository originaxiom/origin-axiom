"""Focused mathematical locks for the authored conditional phase extension."""
import importlib.util
from pathlib import Path
import sympy as S

PACKET=Path(__file__).resolve().parents[1]/"reports/physical_bridge_2026_09_05/silver_framed_coupled_domains_2026_10_11"


def load(name):
    spec=importlib.util.spec_from_file_location("framed_coupled_"+name,PACKET/(name+".py"))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_nonparallel_green_needs_actual_normal_complement():
    native=load("probe")
    c,O,good,bad=native.green_data(S.Integer(5))
    assert O*c != S.zeros(2,1)
    assert (O*c).dot(good)==0
    assert (O*c).dot(bad)!=0
    assert c.dot(O*bad)==-(O*c).dot(bad)


def test_symmetric_Weyl_mass_has_actual_singular_values():
    native=load("probe")
    U,d0,d1,d2,R=native.model(S.Integer(7))
    assert native.zero(R-R.T)
    assert not native.zero(R-R.adjoint())
    assert native.zero(R.adjoint()*R-49*S.eye(3))


def test_real_exact_and_imaginary_exact_not_same_gauge():
    native=load("probe")
    U,d0,d1,d2,R=native.model(S.Integer(3))
    e=U[:,0]
    assert native.zero(d1*e)
    assert (d0.adjoint()*e)[0].simplify()==3
    assert S.im((d0.adjoint()*(S.I*e))[0]).simplify()==3


def test_antilinear_not_linear_mass_square():
    native=load("probe")
    U,d0,d1,d2,R=native.model(S.Integer(2))
    K=d1.conjugate(); u=U[:,1]
    assert native.zero(K*K.conjugate()*u-4*u)
    assert not native.zero(K*K*u-4*u)


def test_twisted_slab_breaks_old_constant_without_reset():
    ref=load("reference")
    r,x,y,n,q,O,c,der,grad,div,curl,lap0=ref.slab()
    assert ref.zero(lap0(c)-q*q*c)
    assert not ref.zero(grad(c)[2])
    assert ref.zero(grad(c)[2].subs(q,0))


def test_twisted_slab_exact_and_coclosed_maps():
    ref=load("reference")
    r,x,y,n,q,O,c,der,grad,div,curl,lap0=ref.slab()
    f=S.cos(n*r)*c; g=[S.zeros(2,1),S.sin(n*r)*c,S.zeros(2,1)]
    assert ref.zero(lap0(f)-(n*n+q*q)*f)
    assert all(ref.zero(z) for z in curl(grad(f)))
    assert ref.zero(div(g))
    assert all(ref.zero(a-(n*n+q*q)*b) for a,b in zip(curl(curl(g)),g))


def test_higher_normal_response_not_whole_squared_domain():
    r=S.symbols("r",real=True); f=r*(S.pi-r)
    assert f.subs(r,0)==f.subs(r,S.pi)==0
    assert f.diff(r,2).subs(r,0)==-2
    n=S.symbols("n",integer=True,positive=True); eigen=S.sin(n*r)
    assert eigen.diff(r,2).subs(r,0)==eigen.diff(r,2).subs(r,S.pi)==0


def test_Gauss_longitudinal_frequency_all_momenta():
    m=S.symbols("m",positive=True); p,E,v=S.symbols("p E v",real=True)
    red=((1+p*p/(m*m))*E*E+m*m*v*v)/2
    assert S.simplify(S.diff(red,E,2)*S.diff(red,v,2)-p*p-m*m)==0
    assert S.diff(red,v,2)==m*m
