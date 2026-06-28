"""B248 locks -- the figure-eight cone-manifold geometric transition realizes the dual McKay E6+E8: hyperbolic
end (x=2) -> Q(sqrt-3), Euclidean (x=1) -> Q (u=-2), spherical end (x=0) -> Q(sqrt5), tr(ab)=phi. FIREWALLED math
(McKay/Arnold trinity, not gauge groups); nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_PATH = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B248_e6_e8_geometric_transition" / "geometric_transition.py"
_spec = importlib.util.spec_from_file_location("b248", _PATH)
b248 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b248)

_S, _U, _PHI = b248.character_variety()


def _roots(sval):
    return sp.solve(sp.Eq(_PHI.subs(_S, sval), 0), _U)


def test_hyperbolic_end_eisenstein():
    # x=2 (alpha=0): u^2+u+1=0 -> e^{+-2 i pi/3}, field Q(sqrt-3)
    assert sp.simplify(_PHI.subs(_S, 1) - (_U ** 2 + _U + 1)) == 0
    for r in _roots(1):
        assert sp.simplify(sp.expand_complex(r).as_real_imag()[1]) != 0     # complex -> Q(sqrt-3), hyperbolic


def test_euclidean_transition_degenerate():
    # x=1 (alpha=2pi/3): u = -2 (double, rational) -- evaluate numerically (sympy leaves (-1)^(1/3) form)
    for r in _roots(sp.exp(sp.I * sp.pi / 3)):
        assert abs(complex(sp.N(sp.expand_complex(r))) + 2) < 1e-9


def test_spherical_end_golden():
    # x=0 (alpha=pi): u in Q(sqrt5); tr(ab) = -2-u is the golden ratio; rep is SU(2) (real tr in [-2,2])
    phi_gold = (1 + sp.sqrt(5)) / 2
    r0 = _roots(sp.I)
    tabs = [sp.simplify(-2 - r) for r in r0]
    assert any(sp.simplify(t - phi_gold) == 0 for t in tabs)                # golden ratio appears
    for t in tabs:                                                          # both real, in [-2,2] => SU(2)
        assert sp.simplify(sp.im(t)) == 0 and -2 <= float(t) <= 2


def test_determinant_five_lens_space():
    # det(4_1) = 5 = |H1| of the double branched cover L(5,2) (the spherical/E8 end's "5")
    import sympy as sp2
    t = sp2.symbols('t')
    alex = t**2 - 3 * t + 1          # Alexander polynomial of 4_1 (normalized)
    assert abs(alex.subs(t, -1)) == 5
