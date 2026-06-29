"""B285 lock -- the figure-eight meridian-commutator trace kappa = u^2+2 = sqrt(3) e^{+-i pi/6}; |arg|=pi/6 forced by
Q(sqrt-3) (verifying chat-2's pi/6). The physics ("CP-violating phase") is FIREWALLED; nothing to CLAIMS.md."""
import importlib.util
import pathlib
import sympy as sp

_DIR = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B285_commutator_phase"
def _load(n):
    spec = importlib.util.spec_from_file_location(n, _DIR / f"{n}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
_cp = _load("commutator_phase")
_v = _load("verdict")


def test_commutator_trace_is_u2_plus_2():
    expr, u = _cp.commutator_trace()
    assert sp.simplify(expr - (u**2 + 2)) == 0


def test_phase_magnitude_pi_over_6_forced():
    for s in (+1, -1):
        arg, mod = _cp.phase_and_modulus(s)
        assert sp.Abs(arg) == sp.pi/6
        assert sp.simplify(mod - sp.sqrt(3)) == 0
    # the sign flips between the two conjugate Riley roots (the tau/amphichirality swap)
    assert _cp.phase_and_modulus(+1)[0] == -_cp.phase_and_modulus(-1)[0]


def test_physics_firewalled():
    assert _v.verdict()
    assert _v.PHYSICS_CP_CLAIM_ESTABLISHED is False and _v.MATH_PHASE_FORCED is True
