"""B106 -- locking tests: the trace map at the Dehn-filling fixed points.
D1: the Jacobian stability signatures (SL(3) 1-1-6, SL(4) 4-4-7) + the honest negative (stability does not
encode the exponent). D4: per-eigenvector L_i = c*M_i^k on all four components. D3: the SL(4) census
(M^4=L principal, M^3=L secondary; conjugates absent)."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b106", _ROOT / "frontier" / "B106_dehn_filling_anatomy" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


# --- D1 -----------------------------------------------------------------
def test_sl3_dehn_jacobian_partially_elliptic():
    """SL(3) W1/W2 Dehn-filling Jacobian is 1 stable, 1 unstable, 6 neutral (partially elliptic) -- distinct
    from the trivial-rep hyperbolic tower and the geometric saddle."""
    for comp in ("W1", "W2"):
        _, st = B.sl3_dehn_jacobian(comp)
        assert st == (1, 1, 6)


def test_sl4_jacobian_stability_does_not_encode_exponent():
    """Both SL(4) Dehn-filling components are 4-4-7 (same), yet principal exponent=4, secondary=3 -- the
    exponent is NOT read off the Jacobian (the hinge test is not met by stability)."""
    sp, se, same = B.jacobian_stability_does_not_encode_exponent()
    assert sp == (4, 4, 7) and se == (4, 4, 7)
    assert same is True


# --- D4 -----------------------------------------------------------------
def test_eigenvalue_anatomy_per_eigenvector_relation():
    """L_i = c*M_i^k holds PER EIGENVECTOR on all four Dehn-filling components, c a root of unity."""
    import numpy as np
    expect = {"W1": (3, 1), "W2": (-3, 1), "principal": (4, -1), "secondary": (3, 1j)}
    for comp, (k, c) in expect.items():
        r = B.eigenvalue_anatomy(comp)
        assert r["k"] == k
        assert r["commute_offdiag"] < 1e-6                 # mu and [A,B] commute
        assert r["per_eigenvector_dev"] < 1e-6             # L_i = c M_i^k per eigenvector
        assert abs(r["c"] - c) < 1e-3                       # the scalar c (root of unity)
        assert abs(abs(r["c_to_k"]) - 1) < 1e-3            # |c^k| = 1


# --- D3 -----------------------------------------------------------------
def test_sl4_census_conjugates_absent():
    """SL(4): M^4=L (principal) and M^3=L (secondary) hold; the conjugates M^4*L=1 and M^3*L=1 are ABSENT."""
    pr = B.census_relations("principal")
    assert pr["M^4=L"][0] < 1e-6 and pr["M^4L=1"][0] > 0.1 and pr["M^3L=1"][0] > 0.1
    se = B.census_relations("secondary")
    assert se["M^3=L"][0] < 1e-6 and pr["M^4L=1"][0] > 0.1 and se["M^4L=1"][0] > 0.1
