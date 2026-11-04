"""S301-A check c36b (value-free; main's frame code; first-principles theta series).
c36 found T a symmetry of every output with DR but not with main's F_10 direction (cm_zero_line.direction), which builds
theta_2 through mpmath's jtheta(2, 0, q) with q = e^{i pi tau}: q^{1/4} is then the principal root, so at Re tau > 1 the
evaluated theta_2^10 differs from the analytic continuation by a sign.  Here: (a) main's F_10 against the analytic
F_10 = (eps th2^10, eps th4^10, i th3^10), eps = i^{(a+2)/2}, inside the census strip and one period out; (b) T on the outputs
with the analytic F_10 (FR-FIB, FR-COV at a0 = 0; and a singlet with F_10's own multiplier, sigma = r eta^6).
Prints deviations only."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(v, "1")
import cmath, math, sys
import numpy as np
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import c36_generators as G
Z, B = G.Z, G.B


def thetas(tau, N=40):
    n = np.arange(N)
    t2 = 2 * np.sum(np.exp(1j * math.pi * tau * (n + 0.5) ** 2))
    m = np.arange(1, N)
    t3 = 1 + 2 * np.sum(np.exp(1j * math.pi * tau * m * m))
    t4 = 1 + 2 * np.sum((-1.0) ** m * np.exp(1j * math.pi * tau * m * m))
    return t2, t3, t4


def F_analytic(a, tau):
    t2, t3, t4 = thetas(tau)
    eps = 1j ** ((a + 2) // 2)
    return np.array([eps * t2 ** a, eps * t4 ** a, 1j * t3 ** a])


def outputs_h(tau, p1, p2, L, h, a0, reading):
    S = G.S_of(a0, h)
    rd = {"FR-FIB": (G.tilde(S), S, S), "FR-COV": (-G.adj(S), S, S)}[reading]
    M = G.Ms(tau, B.line_w(p1, p2, tau), L)
    Y = {sn: B.coupling(Sx, M[sn][0]) for (sn, _, _), Sx in zip(G.SECT, rd)}
    out, U = [], {}
    for sn in ("up", "down", "lepton"):
        u_, s_, _ = np.linalg.svd(Y[sn]); out += [s_[1] / s_[0], s_[2] / s_[0]]; U[sn] = u_[:, ::-1]
    V = U["up"].conj().T @ U["down"]
    return np.array(out), np.abs(V), float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))


if __name__ == "__main__":
    print("c36b: main's F_10 evaluator vs the analytic F_10, and T with the analytic one")
    for t in (complex(0.37, 3.05), complex(0.21, 2.3), complex(1.37, 3.05), complex(1.21, 2.3)):
        hm = np.array(Z.direction("F_10", t)); ha = F_analytic(10, t)
        print("  tau = %s: |main - analytic| / |F| per component (I, J, K): %s" % (t, " ".join("%.1e" % (abs(hm[i] - ha[i]) / np.abs(ha).max()) for i in range(3))))
    ws = 0.0
    for t in (complex(0.37, 3.05), complex(0.21, 2.3)):
        f0, f1 = F_analytic(10, t), F_analytic(10, t + 1)
        ws = max(ws, np.abs(f1 - 1j * np.array([f0[0], f0[2], -f0[1]])).max() / np.abs(f0).max())
    print("  analytic F_10(tau+1) vs i (h_I, h_K, -h_J): %.1e  (and eta^6(tau+1) = i eta^6)" % ws)
    for reading in ("FR-FIB", "FR-COV"):
        for r in (0.0, 0.3, 1.1):
            worst = 0.0
            for t in (complex(0.21, 2.3), complex(0.37, 3.05)):
                L = Z.radii(t)[0]
                for (p1, p2) in ((0.4, 0.1), (0.4, 0.5), (0.4, 0.2), (1 / 3, 1 / 7)):
                    o0, v0, j0 = outputs_h(t, p1, p2, L, F_analytic(10, t), r * G.eta(t) ** 6, reading)
                    o1, v1, j1 = outputs_h(t + 1, p1, p2 + p1, L, F_analytic(10, t + 1), r * G.eta(t + 1) ** 6, reading)
                    worst = max(worst, np.abs(o1 - o0).max() / np.abs(o0).max(), np.abs(v1 - v0).max(), abs(j1 - j0) / max(abs(j0), 1e-12))
            print("  analytic F_10, %s, a0 = %.1f eta^6: T (tau+1, p2+p1) worst relative output deviation %.1e" % (reading, r, worst), flush=True)
