"""Path B (re-examination): j=1728 of y^2=M^4-aM^2+1 is forced+isolated (a in {0,+-6}); CONFIRMS V34."""
import importlib.util, pathlib
import sympy as sp
_r=pathlib.Path(__file__).resolve().parents[1]
_s=importlib.util.spec_from_file_location("scc", _r/"frontier"/"physics_probes"/"spectral_curve_coulomb_test.py")
m=importlib.util.module_from_spec(_s); _s.loader.exec_module(m)

def test_j_invariant_family_and_forced_isolation():
    a=sp.symbols("a")
    I,J,j=m.j_of_a()
    assert sp.expand(I-(a**2+12))==0
    assert sp.expand(J-2*a*(a-6)*(a+6))==0
    # j=1728 <=> a in {0,+-6}
    assert set(sp.solve(sp.Eq(J,0),a))=={sp.Integer(0),sp.Integer(6),sp.Integer(-6)}
    assert sp.simplify(j.subs(a,6))==1728 and sp.simplify(j.subs(a,0))==1728
    # j varies (not constant) -> a is the only modulus, j=1728 isolated
    assert sp.simplify(sp.diff(j,a))!=0
    assert sp.simplify(j.subs(a,3))!=1728
