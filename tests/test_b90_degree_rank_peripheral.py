"""B90 (Task 1b) -- locking tests: the uniform peripheral identity (Lemma 1) lambda = mu X^-1 mu Y^-1
and X mu X^-1 = mu A holds on the bundle reps (n=3,4), with the collapse lambda = (-1)^(n-1) mu^n; and
L1b holds EXACTLY over Q(w) on the B89 symbolic family."""
import importlib.util
import pathlib

import numpy as np
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B90 = _load("b90", "frontier/B90_degree_rank_peripheral/probe.py")


def test_lemma1_and_collapse_n4():
    """n=4: the uniform peripheral identity (L1a, L1b) and the collapse lambda=c*mu^4, c=-1."""
    out = B90._build_n4()
    assert out is not None
    A, B, t = out
    l1a, l1b = B90.lemma1_residuals(A, B, t)
    assert l1a < 1e-7 and l1b < 1e-7
    dev, c = B90.collapse_dev(A, B, t, 4)
    assert dev < 1e-7 and abs(c - (-1.0)) < 1e-4


def test_lemma1_and_collapse_n3():
    """n=3: same identity, collapse lambda=c*mu^3 with c=+1 = (-1)^(3-1) (the sign law)."""
    out = B90._build_n3()
    assert out is not None
    A, B, t = out
    l1a, l1b = B90.lemma1_residuals(A, B, t)
    assert l1a < 1e-7 and l1b < 1e-7
    dev, c = B90.collapse_dev(A, B, t, 3)
    assert dev < 1e-7 and abs(c - 1.0) < 1e-4


def test_L1b_exact_over_Qw_on_b89_family():
    """L1b: X mu X^-1 = mu A holds EXACTLY over Q(w) on the B89 symbolic family (X = A mu A^-1)."""
    B89 = _load("b89", "frontier/B89_sl4_symbolic_M4L/probe.py")
    A, A2, t, _ = B89.family()
    red, redM = B89.red, B89.redM
    mu = redM(A2 * t)
    X = redM(A * mu * A2)                          # X = A mu A^-1 (A^-1 = A^2)
    Xi = X.adjugate() / sp.cancel(X.det())
    lhs = redM(X * mu * Xi)
    rhs = redM(mu * A)
    assert all(sp.expand(red(sp.numer(sp.together(lhs[i, j] - rhs[i, j])))) == 0
               for i in range(4) for j in range(4))
