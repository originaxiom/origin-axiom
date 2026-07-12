"""Locks for B536 — measurement-architecture verification (level 15, theta lift)."""
import numpy as np

N = 15
z = np.exp(2j*np.pi/N)
n_ = np.arange(N)
W1 = np.diag(z**((n_*(n_-1)//2) % N))
F = z**np.outer(n_, n_) / np.sqrt(N)
W2 = F @ np.conj(W1) @ np.conj(F).T
Par = np.zeros((N, N)); Par[n_, (-n_) % N] = 1


def _commutant_dim(mats):
    rows = [np.kron(np.eye(N), M) - np.kron(M.T, np.eye(N)) for M in mats]
    s = np.linalg.svd(np.vstack(rows), compute_uv=False)
    return int(np.sum(s < 1e-10 * s[0]))


def test_w1w2_commutant_is_4():
    assert _commutant_dim([W1, W2]) == 4


def test_irreducible_with_par():
    assert _commutant_dim([W1, W2, Par]) == 1


def test_U_crt_tensor_factorizes():
    U = W1 @ W2
    P = np.zeros((N, N))
    for n in range(N):
        P[5*(n % 3) + (n % 5), n] = 1
    Uc = (P @ U @ P.T).reshape(3, 5, 3, 5)
    i0 = np.unravel_index(np.argmax(np.abs(Uc)), Uc.shape)
    U5 = Uc[i0[0], :, i0[2], :]
    U3 = Uc[:, i0[1], :, i0[3]] / Uc[i0]
    assert np.abs(np.einsum('ik,jl->ijkl', U3, U5) - Uc).max() < 1e-12


def test_commutator_golden_eigenvalue_level15():
    C = W1 @ W2 - W2 @ W1
    eg = np.linalg.eigvals(C)
    phi = (1 + np.sqrt(5)) / 2
    hits = [e for e in eg if abs(abs(e) - phi) < 1e-9 and abs(e.real) < 1e-9]
    assert len(hits) == 2  # +i phi and -i phi


def test_commutator_level5_no_iphi_but_sqrtphi():
    lvl = 5
    zz = np.exp(2j*np.pi/lvl); m = np.arange(lvl)
    w1 = np.diag(zz**((m*(m-1)//2) % lvl))
    f = zz**np.outer(m, m) / np.sqrt(lvl)
    w2 = f @ np.conj(w1) @ np.conj(f).T
    eg = np.linalg.eigvals(w1 @ w2 - w2 @ w1)
    phi = (1 + np.sqrt(5)) / 2
    assert not any(abs(abs(e) - phi) < 1e-9 for e in eg)
    mags = sorted(np.abs(eg))[::-1]
    assert abs(mags[0] - np.sqrt(phi)) < 1e-9


def test_par_split_8_7():
    assert int(round((N + np.trace(Par).real) / 2)) == 8


def test_natural_lift_period_is_20_not_6():
    """Under U = W1 W2, the Par-projected most-uncertain eigenvector has
    state-period 20 up to phase (the order of A1 in SL(2,Z/15)), not 6."""
    U = W1 @ W2
    ev, evec = np.linalg.eig(U)
    par_exp = [float(np.real(np.conj(v) @ Par @ v)) for v in evec.T]
    psi0 = evec[:, int(np.argmin(np.abs(par_exp)))]
    psi = psi0 + Par @ psi0
    psi = psi / np.linalg.norm(psi)
    def period(state):
        for k in range(1, 61):
            if abs(abs(np.conj(np.linalg.matrix_power(U, k) @ state) @ state) - 1) < 1e-9:
                return k
        return None
    assert period(psi) == 20


def test_dark_free_is_generic():
    """Basis state and a fixed random state both have 0 dark points."""
    rng = np.random.RandomState(1)
    states = [np.eye(N)[0], rng.randn(N) + 1j*rng.randn(N)]
    W1p = [np.linalg.matrix_power(W1, j) for j in range(N)]
    W2p = [np.linalg.matrix_power(W2, l) for l in range(N)]
    for st in states:
        st = st / np.linalg.norm(st)
        dark = sum(1 for j in range(N) for l in range(N)
                   if abs(np.conj(st) @ (Par @ W1p[j] @ W2p[l]) @ st) < 1e-10)
        assert dark == 0
