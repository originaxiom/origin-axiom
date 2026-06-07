"""Phase 3 -- locking test: the figure-eight Kashaev invariant is a cheap finite sum whose asymptotic recovers the
hyperbolic volume (the SL(2)/4_1 complex-CS partition function) -- the feasibility witness for the HEAVY fork S027.
FIREWALLED; low-dim topology, NOT fundamental physics; nothing to CLAIMS.md; P1-P16 untouched."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "kashaev_feasibility", _ROOT / "frontier" / "physics_probes" / "kashaev_feasibility.py")
K = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(K)


def test_volume_conjecture_feasible():
    vc = K.volume_conjecture()
    assert vc["feasible"] is True               # the error shrinks with N
    assert vc["monotone_toward_vol"] is True      # monotone (from above) toward vol(4_1)
    assert vc["rows"][-1]["err"] < 0.1            # at N=800 within 0.08 of vol=2.0299 (slow log convergence)


def test_kashaev_is_finite_and_positive():
    for N in (10, 30, 60):
        J = K.kashaev_fig8(N)
        assert J > 0 and J < float("inf")         # a well-defined finite sum -- the computation is in-house
