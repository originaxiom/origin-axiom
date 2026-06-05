"""B75 (Path F1, V57) -- locking test: the m-axis of the degree=rank law.

Locks the solid finding: at rank n=3, the ODD metallic bundles m=1 AND m=3 give the SAME clean
degree=rank relation M^3=L (convention-independent eigenvalue test eig[A,B]=eig(t)^3), so degree=rank
persists across the metallic family (not special to the figure-eight m=1); and the eigenvalue test is
the right convention-independent criterion (it gives k=3, not k=2 or 4). Kept small (n=3, few reps)."""
import numpy as np
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b75_mdr", _ROOT / "frontier" / "B75_metallic_degree_rank" / "probe.py")
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)

SPEC = [1, 1j, -1j]  # the n=3 figure-eight Dehn-filling spectrum (tr A = 1)


def _clean_degree(spec, m, n_reps=3, seed=3):
    """Return the median eigenvalue-test dev for k=2,3,4 over a few metallic-m bundle reps."""
    out = {}
    for k in (2, 3, 4):
        med, nrep = P.degree_over_family(spec, m, k, n_reps=n_reps, seed=seed, budget=120)
        out[k] = (med, nrep)
    return out


def test_odd_metallic_bundles_give_degree_rank_M3():
    """m=1 and m=3 metallic bundles both give M^3=L (degree=rank=3) at n=3 -- the m-axis."""
    for m in (1, 3):
        out = _clean_degree(SPEC, m)
        assert out[3][1] >= 2, (m, "need >=2 reps")
        assert out[3][0] < 1e-9, (m, "M^3=L must be clean", out)
        # and k=2,4 are NOT clean (the degree is specifically 3)
        assert out[2][0] > 1e-4 and out[4][0] > 1e-4, (m, "only k=3 clean", out)


def test_eigenvalue_test_is_convention_independent_anchor():
    """The eigenvalue test eig[A,B]=eig(t)^3 reproduces M^3=L for the figure-eight (m=1) -- the anchor
    that the cross-family test is sound (B73's scalar mu=A^-1 t is convention-specific; this is not)."""
    out = _clean_degree(SPEC, 1)
    assert out[3][0] < 1e-9 and out[3][1] >= 2, out
