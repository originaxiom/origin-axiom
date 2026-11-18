"""B1957: the physical lane's package 'all seats, main preparation' (2026-11-16): the mathematics inside its
findings F01 to F17 on other seats' sources, on main's own ground.  The custody of the quotations the findings rest on
is physical_evidence_custody.py; main's own verdicts on the same sources are in its records of those lanes.
 A1  F01: the least valuation over the permutations bounds a determinant's valuation from below and need not equal
     it: for the 2 x 2 matrix of ones the bound is 0 and the determinant vanishes.
 A2  F05: on functions on Z/N the normalised Fourier transform squares to the parity C; the normalised Gauss scalars
     gamma_N(r) = N^(-1/2) sum_x exp(2 pi i r x^2 / (2 N)) (with 1/2 the inverse of 2 modulo N) are i, 1, i at
     (N, r) = (15, 1), (5, 3), (3, 2), and gamma_15(1) = gamma_5(3) gamma_3(2); with S = F / gamma and
     T = diag(exp(2 pi i r x^2 / (2 N))) the relation (S T)^3 = S^2 holds, and S^2 = gamma^-2 C is -C, +C, -C:
     so '(ST)^3 = S^2 = C' is wrong by that scalar in two of the three.
 A3  F12: the two conventions for the quartic.  With V = (lambda'/2)|H|^4 the running in ln mu has 12 lambda'^2,
     -78 lambda'^3 and -24 lambda'^2 Y2 (main's own code, from the primary source); with lambda' = 2 lambda these are
     24 lambda^2, -312 lambda^3 and -48 lambda^2 Y2.  A routine that carries 24 and -312 must carry -48, not -24.
 A4  F13: two quantities of one mass dimension have a dimension matrix of rank 1 and still one free ratio.
 A6  the source-vector point: for a positive matrix G every F = G^(-1/2) U with U unitary has F^dagger G F = 1, so
     that condition does not fix F times the vector of ones.
 A5  F17: for a real symmetric mass matrix with eigenvalues m_i, the rescaling (1 + eps E) M (1 + eps E)^T changes
     M^2 off the diagonal by eps E_ij (m_i + m_j)^2 in the eigenbasis, so the rotation is eps E_ij (m_i + m_j) /
     (m_j - m_i): it grows without bound as the two masses approach each other."""
import functools, itertools, cmath, math
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
print = functools.partial(print, flush=True)

if __name__ == "__main__":
    val = [[0, 0], [0, 0]]; bound = min(val[0][0] + val[1][1], val[0][1] + val[1][0]); det = 1 * 1 - 1 * 1
    print("A1: the matrix of ones: least valuation over the permutations %d; its determinant: %d" % (bound, det))
    rows = []; gam = {}
    for N, r in ((15, 1), (5, 3), (3, 2)):
        h = pow(2, -1, N); w = np.exp(2j * np.pi / N); x = np.arange(N)
        g = sum(w ** ((r * h * k * k) % N) for k in range(N)) / np.sqrt(N); gam[(N, r)] = g
        T = np.diag(w ** ((r * h * x * x) % N)); C = np.zeros((N, N)); C[(-x) % N, x] = 1
        ok = {}
        for sgn in (1, -1):
            F = w ** ((sgn * r * np.outer(x, x)) % N) / np.sqrt(N); S = F / g
            ok[sgn] = (bool(np.allclose(F @ F, C)), bool(np.allclose(np.linalg.matrix_power(S @ T, 3), S @ S)), bool(np.allclose(S @ S, C)), bool(np.allclose(S @ S, -C)))
        rows.append((N, r, complex(np.round(g, 12)), ok))
    print("A2: (N, r, gamma, for the two signs of the Fourier kernel: (F^2 = C, (ST)^3 = S^2, S^2 = C, S^2 = -C)): %s; gamma_15(1) - gamma_5(3) gamma_3(2) = %.1e" % (rows, abs(gam[(15, 1)] - gam[(5, 3)] * gam[(3, 2)])))
    lam, lp, Y2 = sp.symbols("lambda lambda_prime Y2"); beta_p = 12 * lp ** 2 - 78 * lp ** 3 - 24 * lp ** 2 * Y2          # the three terms, loop factors dropped
    beta = sp.expand(beta_p.subs(lp, 2 * lam) / 2)
    print("A3: with lambda' = 2 lambda the three terms 12 lambda'^2, -78 lambda'^3, -24 lambda'^2 Y2 become %s" % beta)
    Dm = sp.Matrix([[1, 1]]); print("A4: the dimension matrix of two masses has rank %d for %d quantities: %d free ratio" % (Dm.rank(), 2, 2 - Dm.rank()))
    rng = np.random.default_rng(47); out = []
    for gap in (0.5, 0.05, 0.005):
        m = np.array([1.0, 1.0 + gap, 3.0]); O = np.linalg.qr(rng.normal(size=(3, 3)))[0]; M = O @ np.diag(m) @ O.T; Ef = np.diag(rng.normal(size=3)); eps = 1e-6
        Mp = (np.eye(3) + eps * Ef) @ M @ (np.eye(3) + eps * Ef).T; E = O.T @ Ef @ O
        d2 = O.T @ (Mp @ Mp.T - M @ M.T) @ O / eps; pred = E[0, 1] * (m[0] + m[1]) ** 2
        vals, vecs = np.linalg.eigh(Mp @ Mp.T); rot = abs((O.T @ vecs)[1, 0]) / eps
        out.append((gap, round(float(d2[0, 1] / pred), 6), round(float(rot / abs(E[0, 1] * (m[0] + m[1]) / (m[1] - m[0]))), 4), round(float(rot), 3)))
    print("A5: (gap, the off-diagonal change over E_12 (m_1 + m_2)^2, the rotation over E_12 (m_1 + m_2)/(m_2 - m_1), the rotation per unit eps): %s" % out)
    G0 = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); G = G0 @ G0.conj().T + np.eye(3); wv, Uv = np.linalg.eigh(G); Gm = Uv @ np.diag(wv ** -0.5) @ Uv.conj().T; ones = np.ones(3); vecs = []
    for _ in range(3):
        Uq = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))[0]; F = Gm @ Uq; assert np.allclose(F.conj().T @ G @ F, np.eye(3)); vecs.append(np.round(np.abs(F @ ones), 3).tolist())
    print("A6: three matrices F with F^dagger G F = 1; the moduli of F times the vector of ones: %s" % vecs)
