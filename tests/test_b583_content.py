"""B583 — the content campaign: the locks.

  (1) X1 witness = the banked B572 value (the non-reality of the coupled character):
      (1295415 + 1011915*sqrt(-3))/2 == 647707.5 + 876344.096...i exactly;
  (2) X3 mechanism at level 1: C = S^2 commutes with S and T, e0 is C-fixed
      => every filling covector is theta-even (the unhearability mechanism).
See frontier/B583_chiral_content/FINDINGS.md.
"""
import numpy as np
import sympy as sp


def test_x1_witness_is_banked_b572_value():
    w = (sp.Integer(1295415) + sp.Integer(1011915) * sp.sqrt(-3)) / 2
    t = (5 + sp.sqrt(-3)) / 2
    z = sp.Symbol('z')
    zv = sp.solve(z + 1 / z - t, z)[0]
    chi27 = sum(sum(zv**(k - 2 * j) for j in range(k + 1)) for k in (16, 8, 0))
    assert sp.simplify(sp.expand(chi27) - w) == 0        # the X1 witness IS tr_27(rho(ab))
    assert sp.im(w) != 0                                  # non-real => no real form (D10)


def test_x3_mechanism_level1():
    w = np.exp(2j * np.pi / 3)
    S = np.array([[w**(-a * b) for b in range(3)] for a in range(3)]) / np.sqrt(3)
    T = np.diag([np.exp(2j * np.pi * (h - 0.25)) for h in (0.0, 2 / 3, 2 / 3)])
    C = S @ S
    assert np.linalg.norm(C @ S - S @ C) < 1e-12          # [C, S] = 0
    assert np.linalg.norm(C @ T - T @ C) < 1e-12          # [C, T] = 0
    e0 = np.array([1, 0, 0], dtype=complex)
    assert np.linalg.norm(e0 @ C - e0) < 1e-12            # the vacuum is C-fixed
    # => every row-0 covector e0 . rho(g) is C-fixed = theta-even: the fillings
    #    can never hear the theta-odd (chiral) sector, at any level (the mechanism).
    odd = np.array([0, 1, -1]) / np.sqrt(2)
    for word in [S, T, S @ T, T @ S @ T, S @ T @ S]:
        assert abs((e0 @ word) @ odd) < 1e-12
