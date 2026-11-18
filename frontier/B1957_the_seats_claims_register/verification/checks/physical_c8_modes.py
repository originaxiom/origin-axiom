"""B1957: the physical lane's package PHYSICAL-C8, its kinematic derivations, tested on main's own mode functions
(cim_overlap.psi: the magnetic zero modes main rebuilt for agy-002's gate 2).  Data-free; nothing of the lane's is run.
Everything is by quadrature over the cell (x, u) in [0,1)^2, z = x + tau u, and central differences in the parameters.
 D1  zero Wilson line, flux N, spin (0, 0): <psi_j, d_X psi_k> = i delta/(4y); <psi_j, d_y psi_k> = 0; the part of d psi
     orthogonal to the modes has squared norm |d tau|^2/(8 y^2)                     (its COVARIANT note, (7) and (8)).
 D2  the frame's matrices: under tau -> tau + 1 the modes change by T6; under S by sqrt(tau/|tau|) S6     (its (9)'s inputs).
 D3  the retwisted modes chi = exp(i pi N (xi u - eta x)) psi(z + zeta), zeta = xi + tau eta: their boundary transitions
     do not depend on (xi, eta)                                                       (its WILSON note, (2)).
 D4  <chi_j, d chi_k> = i delta [dX/(4y) + pi N (xi d eta - eta d xi)]                 (its (5)).
 D5  a move of xi by 1/N and of eta by 1/N: the clock and the shift, with the gauge factors it states   (its (7)).
 D6  the orthogonal part of d chi: |d tau|^2/(8y^2) + (pi N/y)|d xi + tau d eta|^2     (its (9)).
 D7  the three-mode product: the retwisting phases cancel under 3 zeta_L + 3 zeta_R = 6 zeta_H           (its section 4)."""
import sys, pathlib, functools
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE)); import cim_overlap as CO
print = functools.partial(print, flush=True); nrm = lambda A: float(np.abs(np.asarray(A)).max()); N = 6; n = 96
g = np.arange(n) / n; X, Ug = np.meshgrid(g, g, indexing="ij"); ip = lambda a, b: np.einsum("axy,bxy->ab", a.conj(), b) / n ** 2
def chi(tau, xi, eta, x=X, u=Ug, M=N): return np.exp(1j * np.pi * M * (xi * u - eta * x)) * CO.psi(M, 0.0, 0.0, x + tau * u, tau, xi + tau * eta)
def d(f, h=1e-5): return lambda *a: (f(*[a_ + h * e for a_, e in zip(a, d.e)]) - f(*[a_ - h * e for a_, e in zip(a, d.e)])) / (2 * h)
def deriv(f, args, i, h=1e-5):
    ap = list(args); am = list(args); ap[i] += h; am[i] -= h; return (f(*ap) - f(*am)) / (2 * h)
def modes(Xr, y, xi, eta): return chi(complex(Xr, y), xi, eta)
rng = np.random.default_rng(5)
# ---- D1, D4, D6 together: the full first-order data at several points
w1 = w4 = w6 = wo = 0
for trial in range(4):
    Xr, y = rng.uniform(-0.4, 0.4), rng.uniform(0.8, 1.4); xi, eta = (0.0, 0.0) if trial == 0 else (rng.uniform(-0.3, 0.3), rng.uniform(-0.3, 0.3)); a = (Xr, y, xi, eta); tau = complex(Xr, y)
    c0 = modes(*a); G0 = ip(c0, c0); wo = max(wo, nrm(G0 - np.eye(N)))
    D = [deriv(modes, a, i) for i in range(4)]; Gam = [ip(c0, Di) for Di in D]
    exp_ = [1j / (4 * y), 0.0, -1j * np.pi * N * eta, 1j * np.pi * N * xi]
    err = max(nrm(Gam[i] - exp_[i] * np.eye(N)) for i in range(4))
    if trial == 0: w1 = max(w1, max(nrm(Gam[i] - exp_[i] * np.eye(N)) for i in range(2)))
    w4 = max(w4, err)
    perp = [Di - np.einsum("ab,bxy->axy", ip(c0, Di).T, c0) for Di in D]         # remove the components along the modes
    Q = np.array([[ip(perp[i], perp[j])[0, 0] for j in range(4)] for i in range(4)])   # the form on (dX, dy, dxi, deta), mode 0
    Qfull_err = max(nrm(ip(perp[i], perp[j]) - ip(perp[i], perp[j])[0, 0] * np.eye(N)) for i in range(4) for j in range(4))
    E = np.zeros((4, 4), complex); E[0, 0] = E[1, 1] = 1 / (8 * y * y)
    v = [0, 0, 1, tau]                                                             # d xi + tau d eta
    for i in (2, 3):
        for j in (2, 3): E[i, j] = (np.pi * N / y) * np.conj(v[i]) * v[j]
    w6 = max(w6, nrm(Q.real - E.real), Qfull_err); w6i = max(globals().get('w6i', 0), nrm(Q.imag - Q.imag.T * -1))   # for real displacements only the symmetric real part enters
print("D1: zero Wilson line, flux %d: |<psi_j, d_X psi_k> - i delta/(4y)| and |<psi_j, d_y psi_k>| at most %.1e (orthonormality of the modes to %.1e)" % (N, w1, wo))
print("D4: the retwisted modes at four (tau, xi, eta): |<chi, d chi> - i [dX/(4y) + pi N (xi d eta - eta d xi)]| at most %.1e in all four directions" % w4)
print("D6: the part of d chi orthogonal to the modes: for real displacements (dX, dy, dxi, deta) its squared norm is |d tau|^2/(8y^2) + (pi N/y)|d xi + tau d eta|^2, the same for every mode and with no cross term between tau and the Wilson line: worst difference of the real symmetric forms %.1e" % w6)
# ---- D2
k = np.arange(6); T6 = np.diag(np.exp(1j * np.pi * k ** 2 / 6)); S6 = np.exp(-1j * np.pi / 4) * np.exp(-2j * np.pi * np.outer(k, k) / 6) / np.sqrt(6); wT = wS = 0
for tau in (0.3 + 1.1j, -0.2 + 0.9j):
    WT = CO.transport(6, 0.0, 0.0, tau, 0.0, "T", n=64); WS = CO.transport(6, 0.0, 0.0, tau, 0.0, "S", n=64)
    wT = max(wT, min(nrm(WT - T6), nrm(WT - T6.conj()))); wS = max(wS, nrm(WS - np.sqrt(tau / abs(tau)) * S6)); which = "T6" if nrm(WT - T6) < 1e-8 else "conj(T6)"
print("D2: main's transport matrices of the flux-6 modes: under tau -> tau + 1 it is %s (%.1e); under S it is sqrt(tau/|tau|) S6 (%.1e)" % (which, wT, wS))
# ---- D3, D5
w3 = w5a = w5b = 0
for trial in range(3):
    tau = complex(rng.uniform(-0.4, 0.4), rng.uniform(0.8, 1.4)); xi, eta = rng.uniform(-0.3, 0.3), rng.uniform(-0.3, 0.3); x = rng.uniform(0, 1, size=7); u = rng.uniform(0, 1, size=7)
    c = chi(tau, xi, eta, x, u)
    w3 = max(w3, nrm(chi(tau, xi, eta, x + 1, u) - np.exp(1j * np.pi * N * u) * c), nrm(chi(tau, xi, eta, x, u + 1) - np.exp(-1j * np.pi * N * x) * c))
    a_ = chi(tau, xi + 1 / N, eta, x, u); w5a = max(w5a, nrm(a_ - np.exp(1j * (2 * np.pi * u + np.pi * eta)) * np.exp(2j * np.pi * k / N)[:, None] * c))
    b_ = chi(tau, xi, eta + 1 / N, x, u); w5b = max(w5b, nrm(b_ - np.exp(-1j * (2 * np.pi * x + np.pi * xi)) * c[(k + 1) % N]))
print("D3: chi(x + 1, u) = e^(i pi N u) chi and chi(x, u + 1) = e^(-i pi N x) chi at three (tau, xi, eta), seven points each: worst %.1e (the transitions do not depend on the Wilson line)" % w3)
print("D5: chi_j(xi + 1/N, eta) = e^(i(2 pi u + pi eta)) e^(2 pi i j/N) chi_j: worst %.1e; chi_j(xi, eta + 1/N) = e^(-i(2 pi x + pi xi)) chi_(j+1): worst %.1e" % (w5a, w5b))
# ---- D7
w7 = 0
for trial in range(3):
    tau = complex(rng.uniform(-0.4, 0.4), rng.uniform(0.8, 1.4)); zL = complex(rng.uniform(-0.3, 0.3), rng.uniform(-0.3, 0.3)); zR = complex(rng.uniform(-0.3, 0.3), rng.uniform(-0.3, 0.3)); zH = (zL + zR) / 2
    def split(z_): eta_ = z_.imag / tau.imag; return (z_ - tau * eta_).real, eta_
    (xL, eL), (xR, eR), (xH, eH) = split(zL), split(zR), split(zH); x = rng.uniform(0, 1, size=5); u = rng.uniform(0, 1, size=5)
    ph = np.exp(1j * np.pi * 3 * (xL * u - eL * x)) * np.exp(1j * np.pi * 3 * (xR * u - eR * x)) * np.conj(np.exp(1j * np.pi * 6 * (xH * u - eH * x))); w7 = max(w7, nrm(ph - 1))
print("D7: with 3 zeta_L + 3 zeta_R = 6 zeta_H the three retwisting phases multiply to 1 in chi_L chi_R conj(chi_H): worst %.1e" % w7)
