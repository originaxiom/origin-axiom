"""B90 (Task 1b) -- locking tests, POST-AUDIT (CC-web, 2026-06-05).

What survives: L1b (X mu X^-1 = mu A) is genuine (fails off the bundle constraint) and the collapse
lambda = (-1)^(n-1) mu^n holds at n=3,4. What was corrected: L1a is a TAUTOLOGY (holds on random
non-bundle (A,t)); and 'exponent = CH degree = rank' is REFUTED by the HINGE TEST -- both SL(4)
Dehn-filling components satisfy L1b but give different exponents (4 vs 3)."""
import importlib.util
import pathlib

import numpy as np

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B90 = _load("b90", "frontier/B90_degree_rank_peripheral/probe.py")


def test_L1a_is_a_tautology():
    """L1a (lambda = mu X^-1 mu Y^-1) holds even on RANDOM non-bundle (A,t) -> a rewriting, not content."""
    assert B90.l1a_is_tautology() < 1e-6


def test_L1b_is_genuine_and_collapse_holds_n4():
    """L1b is genuine (holds on a real bundle rep) and the collapse lambda=c*mu^4, c=-1, holds at n=4."""
    out = B90.hinge_test()
    l1b, k = out["principal {1,1,w,w2}"]
    assert l1b is not None and l1b < 1e-7 and k == 4


def test_hinge_refutes_exponent_equals_CH_degree():
    """THE HINGE TEST: both SL(4) components satisfy L1b (4x4 A, CH degree 4) but give DIFFERENT exponents
    (principal M^4, secondary M^3) -> 'exponent = CH degree = rank' is REFUTED."""
    out = B90.hinge_test()
    l1b_p, k_p = out["principal {1,1,w,w2}"]
    l1b_s, k_s = out["secondary {prim 8th, z^4+1}"]
    assert l1b_p is not None and l1b_s is not None
    assert l1b_p < 1e-7 and l1b_s < 1e-7        # BOTH satisfy L1b
    assert k_p == 4 and k_s == 3                 # but exponents DIFFER -> CH-degree mechanism refuted
