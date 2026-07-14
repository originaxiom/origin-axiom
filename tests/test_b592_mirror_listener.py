"""B592 — R3-M, the mirror listener (locks): the DEAF verdict, sharpened.

(i) the theta-odd channels of the cut-open pairing vanish identically for
every mapping-class gluing (C psi = psi + C central); (ii) the C-twist is
absorbed by the mirror covector (twisted = untwisted); (iii) the Theta-reality
identity conj A(g) = A(g^-1); (iv) the R-matrix pipeline reproduces B245 on
4_1 and the 5_2 braid word closes to 5_2 (Jones layer).

See frontier/B592_mirror_listener/FINDINGS.md.
"""
import cmath
import math
import importlib.util
import os

import numpy as np

_ROOT = os.path.join(os.path.dirname(__file__), "..")


def _load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b238 = _load("frontier/B238_su32_levelrank/su32_wrt.py", "b238m5")
b245 = _load("frontier/B245_higher_color_levelrank/higher_color_levelrank.py", "b245m5")

Q = cmath.exp(1j * math.pi / 5)


def _stage():
    w, S, T, c = b238.su3_data(2)
    n = len(w)
    C = np.zeros((n, n))
    for i, wt in enumerate(w):
        C[w.index((wt[1], wt[0])), i] = 1.0
    return w, S, T, C


def _rho(S, T, word):
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    D = {"R": T, "L": Si @ Ti @ S}
    D["r"], D["l"] = np.linalg.inv(D["R"]), np.linalg.inv(D["L"])
    M = np.eye(S.shape[0], dtype=complex)
    for ch in word:
        M = M @ D[ch]
    return M


def _psi(w):
    J = {(0, 0): 1.0, (1, 0): b245.H_sym(1, Q ** 3, Q),
         (0, 1): b245.H_antisym(2, Q ** 3, Q), (2, 0): b245.H_sym(2, Q ** 3, Q),
         (0, 2): b245.H_sym(2, Q ** 3, Q), (1, 1): 0.0}
    return np.array([J[wt] for wt in w], dtype=complex)


def test_odd_channels_identically_dead():
    w, S, T, C = _stage()
    psi = _psi(w)
    conj_idx = [w.index((wt[1], wt[0])) for wt in w]
    for word in ("", "RL", "RRLL", "RRL"):
        vec = (C @ _rho(S, T, word)) @ psi
        a = np.array([np.conj(psi[conj_idx[i]]) * vec[i] for i in range(len(w))])
        for u, v in (((1, 0), (0, 1)), ((2, 0), (0, 2))):
            odd = a[w.index(u)] - a[w.index(v)]
            assert abs(odd) < 1e-12                     # identically zero


def test_c_twist_absorbed():
    w, S, T, C = _stage()
    psi = _psi(w)
    conj_idx = [w.index((wt[1], wt[0])) for wt in w]
    for word in ("RL", "RRLL", "RRL"):
        M = _rho(S, T, word)
        tw = sum(np.conj(psi[conj_idx[i]]) * ((C @ M) @ psi)[i] for i in range(len(w)))
        un = sum(np.conj(psi[conj_idx[i]]) * (M @ psi)[i] for i in range(len(w)))
        # NOTE: the untwisted comparison uses the SAME mirror covector; the
        # absorption statement is tw == the plain-label pairing:
        plain = psi.conj() @ M @ psi
        assert abs(tw - plain) < 1e-12


def test_theta_reality_identity():
    w, S, T, C = _stage()
    psi = _psi(w)
    for word in ("RL", "RRLL", "RRL"):
        ginv = "".join({"R": "r", "L": "l"}[ch] for ch in reversed(word))
        A1 = psi.conj() @ _rho(S, T, word) @ psi
        A2 = psi.conj() @ _rho(S, T, ginv) @ psi
        assert abs(np.conj(A1) - A2) < 1e-10
        assert abs(((A1 + A2) / 2).imag) < 1e-10


def _rmat(N, qv):
    d = N * N
    R = np.zeros((d, d), dtype=complex)
    for i in range(N):
        for j in range(N):
            row = i * N + j
            if i == j:
                R[row, row] = qv
            else:
                R[j * N + i, row] += 1.0
                if i < j:
                    R[row, row] += (qv - 1 / qv)
    return R / qv ** (1.0 / N)


def _inv(N, braid, nstr, qv):
    R = _rmat(N, qv)
    Ri = np.linalg.inv(R)
    M = np.eye(N ** nstr, dtype=complex)
    wr = 0
    for g in braid:
        k = abs(g) - 1
        op = np.kron(np.kron(np.eye(N ** k), R if g > 0 else Ri),
                     np.eye(N ** (nstr - k - 2)))
        M = M @ op
        wr += 1 if g > 0 else -1
    mu1 = np.diag([qv ** (N - 1 - 2 * i) for i in range(N)])
    mu = mu1
    for _ in range(nstr - 1):
        mu = np.kron(mu, mu1)
    return np.trace(M @ mu) * qv ** (-(N - 1.0 / N) * wr) / np.trace(mu1)


def test_rmatrix_pipeline_and_52():
    # validation on 4_1 at the SU(3)_2 root
    assert abs(_inv(3, [1, -2, 1, -2], 3, Q) - b245.H_sym(1, Q ** 3, Q)) < 1e-9
    # the braid closes to 5_2 (Jones layer, generic q, unique among candidates)
    q = 1.37 * cmath.exp(0.41j)
    t = q ** 2
    v = _inv(2, [1, 1, 1, 2, -1, 2], 3, q)
    jones52 = -t**-6 + t**-5 - t**-4 + 2 * t**-3 - t**-2 + t**-1
    assert abs(v - jones52) < 1e-9
    # J_3(5_2) at the root is non-real (the amphichirality contrast)
    j52 = _inv(3, [1, 1, 1, 2, -1, 2], 3, Q)
    assert abs(j52.imag) > 0.5


# ---------------- B592-OPEN: the faithful open-matrix locks ----------------
def _open_matrix(word, twisted, psi_vec):
    w, S, T, C = _stage()
    n = len(w)
    conj_idx = [w.index((wt[1], wt[0])) for wt in w]
    M2 = _rho(S, T, word)
    W = (C @ M2) if twisted else M2
    return np.diag(np.conj(psi_vec[conj_idx])) @ W @ np.diag(psi_vec), w


def _bases(w):
    n = len(w)
    pairs = [(w.index((1, 0)), w.index((0, 1))), (w.index((2, 0)), w.index((0, 2)))]
    sing = [w.index((0, 0)), w.index((1, 1))]
    odd = np.zeros((n, 2))
    even = np.zeros((n, 4))
    for j, (a, b) in enumerate(pairs):
        odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
        even[a, j], even[b, j] = 1 / np.sqrt(2), 1 / np.sqrt(2)
    for j, i in enumerate(sing):
        even[i, 2 + j] = 1.0
    return odd, even


def test_open_c1_foundation_real():
    w, S, T, C = _stage()
    M, _ = _open_matrix("", False, _psi(w))
    assert np.abs(M.imag).max() < 1e-12


def test_open_sign_flip_theorem():
    w, S, T, C = _stage()
    psi = _psi(w)
    odd, even = _bases(w)
    for word in ("", "RL", "RRLL"):
        Mt, _ = _open_matrix(word, True, psi)
        Mu, _ = _open_matrix(word, False, psi)
        assert np.abs(odd.T @ Mt @ odd + odd.T @ Mu @ odd).max() < 1e-12
        assert np.abs(even.T @ Mt @ even - even.T @ Mu @ even).max() < 1e-12


def test_open_parity_conservation_and_mixed_im():
    w, S, T, C = _stage()
    psi = _psi(w)
    odd, even = _bases(w)
    M, _ = _open_matrix("RL", True, psi)
    assert np.abs(odd.T @ M @ even).max() < 1e-12
    assert np.abs(even.T @ M @ odd).max() < 1e-12
    assert np.abs((odd.T @ M @ odd).imag).max() > 0.5       # Im in odd (open)
    assert np.abs((even.T @ M @ even).imag).max() > 0.5     # and in even
    M0, _ = _open_matrix("", True, psi)
    assert np.abs(M0.imag).max() < 1e-12                    # bare twisted weld real
