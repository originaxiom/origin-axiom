"""Locks for B492 (the Verlinde / Affleck-Ludwig boundary-entropy lens).

Two parts. (1) Recompute: the node's inline reproducer (Fibonacci S-matrix + Verlinde +
AL g-factors) is cheap exact algebra — re-executed here in sympy: D = sqrt(2+phi),
tau x tau = 1 + tau, g_tau/g_1 = phi exactly, and the banked decimals. (2) Documentation-
integrity lock, not a recompute: the verdict that this is classical RCFT data (the same
golden phi, dressed as a boundary g-factor), firewalled with nothing to CLAIMS.md, and
that both lens probes (QCA=B480, Verlinde=B492) are closed.
"""
import math
import pathlib

import sympy as sp

_FIND = (pathlib.Path(__file__).resolve().parents[1]
         / "frontier" / "B492_verlinde_boundary_lens" / "FINDINGS.md").read_text(encoding="utf-8")

_PHI = (1 + sp.sqrt(5)) / 2
_D = sp.sqrt(2 + _PHI)
_S = sp.Matrix([[1, _PHI], [_PHI, -1]]) / _D          # Fibonacci modular S-matrix


def test_total_quantum_dimension_exact():
    assert sp.simplify(1 + _PHI**2 - (2 + _PHI)) == 0          # sqrt(1+phi^2) = sqrt(2+phi)
    assert abs(float(_D) - 1.902113) < 1e-6
    assert sp.simplify(_S * _S.T - sp.eye(2)) == sp.zeros(2)   # S unitary (real symmetric)


def _fusion(a, b, c):
    # Verlinde: N_{ab}^c = sum_x S_ax S_bx S_cx / S_0x  (S real symmetric here)
    return sp.simplify(sum(_S[a, x] * _S[b, x] * _S[c, x] / _S[0, x] for x in range(2)))


def test_verlinde_reproduces_golden_fusion_rule():
    # tau x tau = 1 + tau, exactly
    assert _fusion(1, 1, 0) == 1 and _fusion(1, 1, 1) == 1
    assert _fusion(0, 0, 0) == 1 and _fusion(0, 0, 1) == 0     # 1 x 1 = 1


def test_affleck_ludwig_g_factors():
    g1 = _S[0, 0] / sp.sqrt(_S[0, 0])
    gt = _S[0, 1] / sp.sqrt(_S[0, 0])
    assert sp.simplify(gt / g1 - _PHI) == 0                    # boundary entropy ratio IS phi
    assert abs(float(g1) - 0.72507) < 1e-5
    assert abs(float(gt) - 1.17319) < 1e-5
    assert abs(math.log(float(g1)) - (-0.32148)) < 1e-5
    assert abs(math.log(float(gt)) - 0.15973) < 1e-5


def test_verdict_classical_and_firewalled():
    assert "**g_τ/g₁ = φ** exactly" in _FIND
    assert "D = √(1+φ²) = √(2+φ) = 1.902113" in _FIND
    assert "**classical RCFT / Affleck–Ludwig modular data**" in _FIND
    assert "**Firewalled — nothing to CLAIMS.md.**" in _FIND
    assert "(QCA=B480, Verlinde=B492) are closed" in _FIND
