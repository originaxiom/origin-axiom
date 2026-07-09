"""B484 — "SM = braiding of Fibonacci anyons" refuted (10th kill): recompute the
verified numbers + lock the density-theorem verdict.

Recompute tier (braid_verify.py, exact/1e-12): the dim-2 Fibonacci braid rep is a
genuine braid rep (F^2 = I, sigma1 sigma2 sigma1 = sigma2 sigma1 sigma2), the
figure-eight braid word (sigma1^{-1} sigma2)^2 has trace -3/phi with golden
eigenphases (about 157.98 deg — nowhere near Cabibbo/Weinberg angles), the fusion
space dims are Fibonacci numbers 2, 3, 5, 8, 13 (so the ladder after "SU(3)" is
SU(5) — the cherry-pick point), and the commutant of the N=3 braid action is
1-dimensional (irreducible: NO multiplicity symmetry channel).

Doc-integrity tier (not a recompute): the NULL verdict and the three-channel
addendum (multiplicity ABSENT / interaction gives CFT c=7/10 / nothing to gauge).
"""
import pathlib

import numpy as np

FINDINGS = (pathlib.Path(__file__).resolve().parents[1] / "frontier"
            / "B484_braiding_sm_verdict" / "FINDINGS.md").read_text(encoding="utf-8")

PHI = (1 + np.sqrt(5)) / 2


def _rep():
    s1 = np.diag([np.exp(-4j * np.pi / 5), np.exp(3j * np.pi / 5)])
    F = np.array([[1 / PHI, 1 / np.sqrt(PHI)], [1 / np.sqrt(PHI), -1 / PHI]])
    return s1, F @ s1 @ F, F


def test_braid_representation_is_valid():
    """F is an involution and the braid (Yang-Baxter) relation holds to 1e-12."""
    s1, s2, F = _rep()
    assert np.allclose(F @ F, np.eye(2), atol=1e-12)
    assert np.allclose(s1 @ s2 @ s1, s2 @ s1 @ s2, atol=1e-12)


def test_figure_eight_braid_trace_is_minus3_over_phi():
    """tr((sigma1^{-1} sigma2)^2) = -3/phi = -1.8541..., eigenphases +-157.98 deg
    (2 cos theta = -3/phi): golden-field phases, not SM mixing angles."""
    s1, s2, _ = _rep()
    B = np.linalg.inv(s1) @ s2 @ np.linalg.inv(s1) @ s2
    tr = np.trace(B)
    assert abs(tr.real + 3 / PHI) < 1e-12 and abs(tr.imag) < 1e-12
    ev = np.linalg.eigvals(B)
    assert np.allclose(np.abs(ev), 1, atol=1e-10)          # unitary
    theta = np.degrees(np.arccos(-3 / (2 * PHI)))
    assert abs(theta - 157.98) < 0.01
    for sm_angle in (13.0, 28.7, 0.2):                     # Cabibbo/Weinberg/theta13
        assert abs(theta - sm_angle) > 100                 # not remotely SM


def test_fusion_space_dims_are_fibonacci_and_ladder_continues_past_su3():
    """dim(N tau-anyons) = 2, 3, 5, 8, 13 for N = 3..7 (path count via the fusion
    matrix [[0,1],[1,1]]): after the 'SU(2), SU(3)' rungs comes SU(5) — the ladder
    has no principled SM stop."""
    def dim(n):
        A = [[0, 1], [1, 1]]
        R = [[1, 0], [0, 1]]
        for _ in range(n):
            R = [[sum(R[i][k] * A[k][j] for k in range(2)) for j in range(2)]
                 for i in range(2)]
        return R[0][1]
    dims = [dim(n) for n in (3, 4, 5, 6, 7)]
    assert dims == [2, 3, 5, 8, 13]
    assert all(dims[i] + dims[i + 1] == dims[i + 2] for i in range(3))  # Fibonacci
    assert dims[2] == 5                                    # next rung: SU(5), not SM


def test_commutant_is_scalar_no_multiplicity_channel():
    """The N=3 braid action is irreducible: the joint commutant of {sigma1, sigma2}
    is 1-dimensional (Schur => scalar), so there is no internal multiplicity
    symmetry to extract as a gauge group."""
    s1, s2, _ = _rep()
    rows = []
    for X in (s1, s2):
        rows.append(np.kron(np.eye(2), X) - np.kron(X.T, np.eye(2)))
    sv = np.linalg.svd(np.vstack(rows), compute_uv=False)
    assert np.sum(sv < 1e-10) == 1                         # nullity 1 = scalars only


def test_density_verdict_locked():
    """Documentation-integrity lock (not a recompute): the banked refutation — the
    density theorem forbids the frame; all three symmetry channels are non-gauge."""
    assert "the density theorem FORBIDS the frame (10th kill)" in FINDINGS
    assert "## Verdict: NULL (10th SM kill). Firewall holds." in FINDINGS
    assert "SU(5), SU(8), SU(13)" in FINDINGS              # the ladder, no SM stop
    assert "Multiplicity — ABSENT" in FINDINGS
    assert "Interaction — gives emergent CFT, not gauge" in FINDINGS
    assert "Gauging — nothing to gauge" in FINDINGS
    assert "tricritical Ising c = 7/10" in FINDINGS
