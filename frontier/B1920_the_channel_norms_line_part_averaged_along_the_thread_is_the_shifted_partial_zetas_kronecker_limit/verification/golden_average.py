"""The line part of B1656's channel norm, F_u, averaged over one period of the golden thread +LR 2 (M = [[5,3],[3,2]]),
for channel 1 (u = Jc) of the twins (1,2)/5 and (2,4)/5, in the window centred at the geodesic's top, where main's F_u
series is converged; and the convergence of that series at the lowest node of a lower window (Im z = 0.08), where it is
not at the default length. Main's code (seat_formula.F)."""
import math, numpy as np, mpmath as mp
import seat_formula as SF
a, b, c, d = 5, 3, 3, 2; D = (a + d) ** 2 - 4
r1 = ((a - d) + math.sqrt(D)) / (2 * b); r2 = ((a - d) - math.sqrt(D)) / (2 * b); beta, betap = max(r1, r2), min(r1, r2)
ell = 2 * math.log(((a + d) + math.sqrt(D)) / 2)
def zt(t): return (beta * 1j * math.exp(t) + betap) / (1j * math.exp(t) + 1)
def average(u, start, nodes=16):
    x, w = np.polynomial.legendre.leggauss(nodes); ts = start + ell / 2 * (x + 1)
    return float(sum(wi * SF.F(u[0], u[1], mp.mpc(zt(t).real, zt(t).imag)) for wi, t in zip(w, ts)) / 2)
if __name__ == "__main__":
    for (i, j) in [(1, 2), (2, 4)]:
        u = ((-j / 5) % 1, i / 5)
        print((i, j), "u = Jc =", tuple(round(v, 3) for v in u), "<F_u> over the centred period: %.6f" % average(u, -ell / 2), flush=True)
    x, w = np.polynomial.legendre.leggauss(16); ts = -ell / 2 + 0.37 * ell + ell / 2 * (x + 1)
    z = min((zt(t) for t in ts), key=lambda q: q.imag)
    for R, Mk in ((30, 40), (60, 80), (120, 160)):
        f = (SF.E_shift(.2, .4, mp.mpc(z.real, z.imag), 1 + mp.mpf("1e-6"), R=R, Mk=Mk) + SF.E_shift(.2, .4, mp.mpc(z.real, z.imag), 1 - mp.mpf("1e-6"), R=R, Mk=Mk)) / 2
        print("lowest node of a lower window, Im z = %.4f: F_u at R %d, Mk %d = %.6f (not converged at the default)" % (z.imag, R, Mk, float(f)), flush=True)
