"""Main's rough independent check of SM-C7's step 2 at s = 1: Z_tot(1, chi) against -4 * integral over one period of
log|g_Jc(z)| ds, with g_a the Siegel function q^(B2(a1)/2) (1 - q^a1 e(a2)) prod_n (1 - q^(n + a1) e(a2)) (1 - q^(n - a1) e(-a2)),
a = Jc reduced to 0 <= a1 < 1 (|g| does not see the reduction), B2(x) = x^2 - x + 1/6. Main's code. The direct sum at s = 1
converges slowly (orbit representatives to |Q| <= X); it is shown at four cutoffs."""
import math, numpy as np, io, contextlib, sys
import hecke_s2 as H

def log_abs_g(a1, a2, z, nmax=60):
    a1 = a1 % 1.0
    q = np.exp(2j * np.pi * z)
    B2 = a1 * a1 - a1 + 1 / 6
    out = np.real(B2 / 2 * 2j * np.pi * z)                     # log|q^(B2/2)| = Re(B2/2 * 2 pi i z)
    out = out + np.log(np.abs(1 - np.exp(2j * np.pi * a1 * z) * np.exp(2j * np.pi * a2)))
    for n in range(1, nmax):
        out = out + np.log(np.abs(1 - q ** n * np.exp(2j * np.pi * a1 * z) * np.exp(2j * np.pi * a2)))
        out = out + np.log(np.abs(1 - q ** n * np.exp(-2j * np.pi * a1 * z) * np.exp(-2j * np.pi * a2)))
    return out

def geo_integral(M, a, nodes=400):
    beta, betap, ell, _ = H.geodesic(M)
    x, w = np.polynomial.legendre.leggauss(nodes)
    t = ell / 2 * x
    z = (beta * 1j * np.exp(t) + betap) / (1j * np.exp(t) + 1)
    return ell / 2 * np.sum(w * log_abs_g(a[0], a[1], z))

SL = H.B._sl()
for st, k in [("+LR", 2), ("+LR", 3)]:
    eps = 1 if st[0] == "+" else -1
    with contextlib.redirect_stdout(io.StringIO()):
        N, F, S = SL.exact_slopes(eps, st[1:], k)
    M = H.B.abel_M(SL, eps, st[1:], k)
    for (i, j, _) in list(S)[:4]:
        if (i, j) == (0, 0):
            continue
        c = (i / N, j / N); Jc = (-c[1], c[0])
        K = -4 * geo_integral(M, Jc)
        sums = [H.rhs(M, i, j, N, s=1.0, X=X)[0].real for X in (2000.0, 8000.0, 32000.0, 128000.0)]
        print(st, k, (i, j), "-4 int log|g| = %.6f" % K, "| Z_tot(1) at X = 2e3, 8e3, 3.2e4, 1.28e5:", ["%.5f" % v for v in sums], flush=True)
