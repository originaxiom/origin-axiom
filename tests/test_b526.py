"""B526 locks — the crossing package's verified structure (independently recomputed).

Every fact here was re-derived from scratch (numerical eigenvalues), not by re-running the
package's own symbolic script. The package is firewall-consistent (structure-only, no crossing);
these locks pin the tetrahedral metric, the isotropy-Stein no-go, and the RG exponents.
"""
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
SQ = PHI ** 0.5
M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]], float)
R = np.array([PHI, 1, PHI * SQ, SQ])
BETA = PHI * (1 + SQ)


def _ell():
    w, V = np.linalg.eig(M.T)
    v = V[:, int(np.argmax(w.real))].real
    return v / (v @ R)


def _sig(A):
    ev = np.linalg.eigvalsh((A + A.T) / 2)
    return (int((ev > 1e-9).sum()), int((ev < -1e-9).sum()), int((abs(ev) <= 1e-9).sum()))


def test_perron_and_tetrahedral_metric():
    assert np.allclose(M @ R, BETA * R)
    D = np.diag(R)
    C = np.eye(4) - np.ones((4, 4)) / 4
    S = np.linalg.inv(D) @ C @ np.linalg.inv(D)
    assert np.linalg.matrix_rank(S) == 3
    assert np.allclose(S @ R, 0)                       # kernel = time-line r
    d = [R[i] * np.eye(4)[:, i] for i in range(4)]
    G = np.array([[d[a] @ S @ d[b] for b in range(4)] for a in range(4)])
    assert np.allclose(G, C)                           # weighted Gram = regular tetrahedron (3/4, -1/4)


def test_isotropy_stein_no_go():
    ell = _ell()
    D = np.diag(R)
    S = np.linalg.inv(D) @ (np.eye(4) - np.ones((4, 4)) / 4) @ np.linalg.inv(D)
    Giso = S - np.outer(ell, ell)
    assert _sig(Giso) == (3, 1, 0)                     # Lorentzian, r timelike
    assert round(R @ Giso @ R, 6) == -1.0
    Wiso = Giso - M.T @ Giso @ M
    assert _sig(Wiso)[1] >= 1                          # NOT positive definite -> the no-go
    B = np.column_stack([ell[i] * np.eye(4)[:, 0] - ell[0] * np.eye(4)[:, i] for i in (1, 2, 3)])
    Wst = B.T @ (S - M.T @ S @ M) @ B
    assert _sig(Wst) == (2, 1, 0) and np.linalg.det(Wst) < 0    # obstruction on the spatial hyperplane


def test_no_go_is_non_normality_not_beta_gt_1():
    ell = _ell()
    D = np.diag(R)
    S = np.linalg.inv(D) @ (np.eye(4) - np.ones((4, 4)) / 4) @ np.linalg.inv(D)
    Wiso = (S - np.outer(ell, ell)) - M.T @ (S - np.outer(ell, ell)) @ M
    assert R @ Wiso @ R > 0                            # expanding dir is FINE -> not "beta>1"
    B = np.column_stack([ell[i] * np.eye(4)[:, 0] - ell[0] * np.eye(4)[:, i] for i in (1, 2, 3)])
    ev = np.linalg.eigvals(np.linalg.pinv(B) @ M @ B)
    assert all(abs(e) < 1 for e in ev)                 # M|E_s spectrally contracting, yet W_stable indefinite


def test_rg_exponents_exact():
    h = PHI * (1 - SQ)
    gam = -1 / PHI + 1j * (5 ** 0.5 - 2) ** 0.5
    assert abs(-np.log(abs(h)) / np.log(BETA) - 0.6303718738431496) < 1e-12
    assert abs(-np.log(abs(gam)) / np.log(BETA) - 0.1848140630784252) < 1e-12
    Om = np.angle(gam) / np.log(BETA)
    assert abs(np.exp(2 * np.pi / Om) - 27.23662275649545) < 1e-9
