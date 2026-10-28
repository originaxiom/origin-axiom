"""L251 (P-403's geometry-first step; data-free): the couplings as overlaps of zero modes on the fibre E_tau.
Matter: flux-one modes psi_p(z) = N e^{i pi z Im z / Im tau} theta[a_p, b_p](z, tau), p over the three even
characteristics [0,0] (theta3), [1/2,0] (theta2), [0,1/2] (theta4).  Higgs: flux-two modes
chi_{(a,b),k}(z) = N e^{2 i pi z Im z / Im tau} theta[(k + a)/2, b](2z, 2tau), k = 0, 1, in each Wilson-line sector (a, b).
Overlaps Y_{pq,(s,k)} = int psi_p psi_q conj(chi_{s,k}) dA by spectrally accurate quadrature on the periodic integrand,
after checking the integrand's double periodicity and the modes' orthonormality.
    python3 -B overlaps.py"""
import itertools, math
import numpy as np
NT = 40


def theta(a, b, nu, T):
    n = np.arange(-NT, NT + 1)[:, None] + a
    return np.sum(np.exp(1j * np.pi * n * n * T + 2j * np.pi * n * (nu[None, :] + b)), 0)


def mode(M, a, b, z, t):
    return np.exp(1j * np.pi * M * z * z.imag / t.imag) * theta(a, b, M * z, M * t)


CH = {"3": (0.0, 0.0), "2": (0.5, 0.0), "4": (0.0, 0.5)}           # theta3, theta2, theta4 as flux-one characteristics
SECT = [(0.0, 0.0), (0.5, 0.0), (0.0, 0.5), (0.5, 0.5)]           # Wilson-line sectors of the flux-two Higgs (a, b)


def run(t, n=96):
    x, y = np.meshgrid(np.arange(n) / n, np.arange(n) / n, indexing="ij")
    z = (x + t * y).ravel(); dA = t.imag / n**2
    psi = {p: mode(1, a, b, z, t) for p, (a, b) in CH.items()}
    for p in psi: psi[p] = psi[p] / math.sqrt(np.sum(np.abs(psi[p])**2) * dA)
    chi = {}
    for (a, b) in SECT:
        for k in (0, 1):
            f = mode(2, (k + a) / 2, b, z, t); chi[(a, b, k)] = f / math.sqrt(np.sum(np.abs(f)**2) * dA)
    # periodicity of |psi|^2 and of the integrands (z -> z + 1, z -> z + tau) on a few random points
    rng = np.random.default_rng(1); zz = rng.random(6) + t * rng.random(6)
    per = 0.0
    for p, (a, b) in CH.items():
        for sh in (1, t):
            per = max(per, np.max(np.abs(np.abs(mode(1, a, b, zz + sh, t))**2 - np.abs(mode(1, a, b, zz, t))**2) / np.abs(mode(1, a, b, zz, t))**2))
    integrand_per = {}
    for p, q in itertools.combinations_with_replacement(CH, 2):
        best = None
        for (a, b, k) in chi:
            def f(w): return mode(1, *CH[p], w, t) * mode(1, *CH[q], w, t) * np.conj(mode(2, (k + a) / 2, b, w, t))
            d = max(np.max(np.abs(f(zz + sh) - f(zz)) / np.abs(f(zz))) for sh in (1, t))
            integrand_per[(p, q, a, b, k)] = d
    # orthonormality of the Higgs modes within each sector (modes of different sectors are sections of different
    # bundles: no common inner product)
    keys = list(chi); ortho = 0.0
    for (a, b) in SECT:
        ks = [(a, b, 0), (a, b, 1)]
        G = np.array([[np.sum(chi[i] * np.conj(chi[j])) * dA for j in ks] for i in ks]); ortho = max(ortho, np.max(np.abs(G - np.eye(2))))
    Y = {}
    for p, q in itertools.combinations_with_replacement(CH, 2):
        for key in keys:
            Y[(p, q) + key] = complex(np.sum(psi[p] * psi[q] * np.conj(chi[key])) * dA)
    return per, integrand_per, ortho, Y


if __name__ == "__main__":
    for t in (complex(0.37, 1.2), complex(0.11, 0.9)):
        per, ip, ortho, Y = run(t)
        print("tau", t, "| |psi|^2 periodicity %.1e | Higgs modes orthonormal within each sector to %.1e" % (per, ortho))
        okper = {k: v for k, v in ip.items() if v < 1e-8}
        print("  periodic integrands (pair, sector, k):", sorted((k[0] + k[1], (k[2], k[3]), k[4]) for k in okper))
        for k, v in sorted(Y.items()):
            if ip[k] < 1e-8: print("  Y[%s%s; sector (%.1f,%.1f) k=%d] = %+.6f %+.6fi   |.| %.6f" % (k[0], k[1], k[2], k[3], k[4], v.real, v.imag, abs(v)))
    print("overlaps exit 0")
