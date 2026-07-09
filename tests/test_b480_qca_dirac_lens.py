"""B480 — the QCA/Dirac lens NULL: recompute the dispersion cells + lock the verdict.

Recompute tier (qca_dispersion.py, ~1 s): the reproduce-gate (split-step walk mass =
coin angle — the Dirac emergence is GENERIC, not object-supplied) and the alignment
law for the object's order-4 coin diag(i,-i) (mass = alignment angle: 0 -> massless
Weyl, pi/4 -> pi/2, pi/2 -> massless again — the mass is a free embedding parameter,
not an object invariant).

Doc-integrity tier (not a recompute): the banked NULL/type-mismatch verdict lines,
including the heavy arithmetic-degeneracy measurement (level-ratio 0.16 at N=181,301).
"""
import pathlib

import numpy as np

FINDINGS = (pathlib.Path(__file__).resolve().parents[1] / "frontier"
            / "B480_qca_dirac_lens" / "FINDINGS.md").read_text(encoding="utf-8")

SY = np.array([[0, -1j], [1j, 0]])


def _massgap(C, npts=4001):
    g = 1e9
    for k in np.linspace(-np.pi, np.pi, npts):
        U = np.diag([np.exp(-1j * k), np.exp(1j * k)]) @ C
        w = np.sort(np.angle(np.linalg.eigvals(U)))
        g = min(g, abs(w[1] - w[0]) / 2)
    return g


def test_reproduce_gate_mass_equals_coin_angle():
    """The gate: a generic rotation coin C(theta) gives emergent mass = theta exactly
    (the universality result the probe reproduces) — Dirac emergence is generic."""
    for th in (0.0, 0.3, 0.8):
        C = np.cos(th) * np.eye(2) - 1j * np.sin(th) * SY
        assert abs(_massgap(C) - th) < 5e-3, th


def test_object_coin_is_order4_and_mass_is_alignment_not_object():
    """The object's doublet coin has eigenvalues +-i (order 4, maximally chiral) for
    every member; its mass is ENTIRELY the alignment angle: alpha=0 -> massless Weyl,
    alpha=pi/4 -> pi/2, alpha=pi/2 -> massless, alpha=0.3 -> 0.6 (tunable)."""
    coin = np.diag([1j, -1j])
    assert np.allclose(np.linalg.matrix_power(coin, 4), np.eye(2))       # order 4
    assert not np.allclose(np.linalg.matrix_power(coin, 2), np.eye(2))
    expected = {0.0: 0.0, 0.3: 0.6, np.pi / 4: np.pi / 2, np.pi / 2: 0.0}
    for a, want in expected.items():
        R = np.cos(a) * np.eye(2) - 1j * np.sin(a) * SY
        assert abs(_massgap(R @ coin @ R.conj().T) - want) < 5e-3, a


def test_findings_null_verdict_locked():
    """Documentation-integrity lock (not a recompute): the banked NULL verdict and
    the type-mismatch reason, incl. the heavy spectral measurement (r=0.16)."""
    assert ("# B480 — the QCA/Dirac lens: NULL, and the reason is a structural "
            "type-mismatch (not a gap)") in FINDINGS
    assert "**Mass:** NULL/TUNABLE" in FINDINGS
    assert "**Chirality:** STRUCTURAL-BUT-KNOWN" in FINDINGS
    assert "level-ratio ⟨r⟩ = 0.16 at N = 181, 301" in FINDINGS
    assert "No B398 escalation: the probe does not fire." in FINDINGS
