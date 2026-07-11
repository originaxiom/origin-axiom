"""B527 locks — the complete Stein-compatible metric cone (independently recomputed).

Discriminating facts: M|E_s is stable; the Lyapunov operator is invertible (=> 6-dim cone);
the AFFINE metric S_aff is Stein-compatible (interior) while B526's PERRON-WEIGHTED S_tet is NOT
(driver signature (2,1)) -- the reconciliation that narrows B526; alpha is a unit choice; the four
letters are not equivalent null rays.
"""
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
SQ = PHI ** 0.5
BETA = PHI * (1 + SQ)
M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]], float)
R = np.array([PHI, 1, PHI * SQ, SQ])


def _setup():
    w, V = np.linalg.eig(M.T)
    ell = V[:, int(np.argmax(w.real))].real
    ell = ell / (ell @ R)
    raw = np.column_stack([ell[i] * np.eye(4)[:, 0] - ell[0] * np.eye(4)[:, i] for i in (1, 2, 3)])
    B, _ = np.linalg.qr(raw)                       # my own ON basis of ker ell^T
    return ell, B, B.T @ M @ B


def _vec(S):
    return np.array([S[0, 0], S[1, 1], S[2, 2], S[0, 1], S[0, 2], S[1, 2]])


def _mat(x):
    return np.array([[x[0], x[3], x[4]], [x[3], x[1], x[5]], [x[4], x[5], x[2]]])


def test_stable_and_lyapunov_invertible_6dim_cone():
    ell, B, Abar = _setup()
    assert np.all(np.abs(np.linalg.eigvals(Abar)) < 1 - 1e-9)      # M|E_s contracting
    L6 = np.column_stack([_vec(_mat(e) - Abar.T @ _mat(e) @ Abar) for e in np.eye(6)])
    assert abs(np.linalg.det(L6)) > 1e-9                            # invertible => full 6-dim cone
    series = sum(np.linalg.matrix_power(Abar.T, n) @ np.eye(3) @ np.linalg.matrix_power(Abar, n)
                 for n in range(200))
    assert np.allclose(_mat(np.linalg.solve(L6, _vec(np.eye(3)))), series)   # L^{-1}(I) = series


def test_affine_metric_interior_but_perron_tetra_not():
    ell, B, _ = _setup()
    A = np.eye(4) - np.outer(R, np.ones(4)) / (np.ones(4) @ R)
    Saff = 0.5 * A.T @ A
    Qaff = B.T @ (Saff - M.T @ Saff @ M) @ B
    assert np.min(np.linalg.eigvalsh(Qaff)) > 1e-9                  # S_aff Stein-compatible (interior)
    # B526 reconciliation: the Perron-weighted S_tet is NOT in the cone (driver indefinite)
    D = np.diag(R)
    Stet = np.linalg.inv(D) @ (np.eye(4) - np.ones((4, 4)) / 4) @ np.linalg.inv(D)
    ev = np.linalg.eigvalsh(B.T @ (Stet - M.T @ Stet @ M) @ B)
    assert (int((ev > 1e-9).sum()), int((ev < -1e-9).sum())) == (2, 1)


def test_lorentzian_completion_and_alpha_is_units():
    ell, B, _ = _setup()
    A = np.eye(4) - np.outer(R, np.ones(4)) / (np.ones(4) @ R)
    Saff = 0.5 * A.T @ A
    Pt = np.outer(R, ell); Ps = np.eye(4) - Pt
    G = lambda al: Saff - al * np.outer(ell, ell)
    Tc = lambda c: Ps + c * Pt
    e = np.linalg.eigvalsh((G(1) + G(1).T) / 2)
    assert (int((e > 1e-9).sum()), int((e < -1e-9).sum())) == (3, 1)          # Lorentzian
    assert np.min(np.linalg.eigvalsh(G(1) - M.T @ G(1) @ M)) > 1e-9           # Stein-positive
    assert np.linalg.norm(Tc(1.7).T @ G(1) @ Tc(1.7) - G(1.7 ** 2)) < 1e-9    # alpha = unit rescale
    alpha_null = np.diag(Saff) / ell ** 2
    assert len({round(a, 6) for a in alpha_null}) == 4                        # 4 distinct null directions
