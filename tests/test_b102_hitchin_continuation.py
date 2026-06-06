"""B102 -- locking tests for the W1/W2 dichotomy + the R4 (boundary-controlled cubic) continuation.

D1  the dichotomy: the two CH conditions hold on B71's V0/W1/W2; the census has 0 "neither".
D2/D3  ellipticity obstruction + cross-check: realized W1->A, W2->B has eigenvalues {1,i,-i}; the geometric
       V0 point is self-dual with tr(AB) a root of t^2-t+7 (Q(sqrt-3)).
D4  Task-M link: the elliptic spectrum is {1,i,-i} = Task M's forced n=3 spectrum.
D5  the relative cubic family is 9-dim and keeps the cusp real ONLY to first order -- generically it
    complexifies at second order (honest finding: the handoff's t*~3.775 geodesic boundary does NOT reproduce).
"""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b102", _ROOT / "frontier" / "B102_hitchin_continuation" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


# --- D1 -----------------------------------------------------------------
def test_dichotomy_conditions_on_b71_components():
    """The two Cayley-Hamilton conditions hold (a factor vanishes) on B71's exact V0/W1/W2 families."""
    conds = B.conditions_on_components()
    for name in ("V0", "W1", "W2"):
        assert conds[name] == (True, True)


def test_dichotomy_census_no_exceptions():
    """Every irreducible Fix(T_1^2) character is Case I or the trB=trB^-1=1 branch -- 0 'neither'."""
    n_I, n_J, n_neither = B.dichotomy_census(n=30, seed=20)
    assert n_neither == 0
    assert n_I > 0 and n_J > 0                              # both cases are populated


# --- D2 / D3 ------------------------------------------------------------
def test_w1_w2_elliptic_generator():
    """Route (b) cross-check on B71's realized components: W1 -> A elliptic {1,i,-i}; W2 -> B elliptic."""
    w1 = B.realize_and_classify("W1")
    assert w1["A_elliptic_1ii"] is True and w1["B_elliptic_1ii"] is False
    w2 = B.realize_and_classify("W2")
    assert w2["B_elliptic_1ii"] is True and w2["A_elliptic_1ii"] is False


def test_geometric_v0_trace_field():
    """The geometric V0 point is self-dual; tr(AB) is a root of t^2-t+7 (Q(sqrt-3))."""
    self_dual, dev = B.geometric_trace_field()
    assert self_dual is True
    assert dev < 1e-10


# --- D4 -----------------------------------------------------------------
def test_task_m_spectrum_link():
    """The W1/W2 elliptic spectrum {1,i,-i} = Task M's forced n=3 spectrum (B95)."""
    spec = set(complex(round(z.real), round(z.imag)) for z in B.task_m_spectrum_link())
    assert spec == {1 + 0j, 1j, -1j}


# --- D5 -----------------------------------------------------------------
def test_relative_cubic_family_dim():
    """The boundary conditions tr(dC)=0, tr(C dC)=0 cut the 10-dim cubic directions to a 9-dim family."""
    assert B.relative_cubic_family() == 9


def test_cusp_complexifies_at_second_order():
    """HONEST FINDING: boundary control is first-order only -- a generic relative-family ray complexifies
    the cusp at second order (the handoff's real (lambda,1,1/lambda) trajectory does NOT reproduce)."""
    frac = B.cusp_second_order_complexifies(n=30, seed=7)
    assert frac > 0.5                                       # the majority of rays leave the real cusp class
