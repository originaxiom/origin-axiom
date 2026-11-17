"""B1957: the web seat's W-Z1, lines 76 to 82 (its referee's figures, computed once there): Hecke's period of the
Eisenstein series along a closed geodesic at discriminants 12 and 40, recomputed by main.  Data-free.
The full lattice sum G(z, s) = sum over (c, d) != 0 of y^s/|c z + d|^(2s) = 2 zeta(2s) E(z, s), integrated over one
period of the geodesic of a form [a, b, c] of discriminant D (length 2 log eps, eps = (t + u sqrt D)/2 the least
solution of t^2 - D u^2 = 4), by Gauss-Legendre nodes, each point first reduced to the fundamental domain, at two
cut-offs with the 1/N^(2s-2) tail removed.  The seat's statements, in this normalisation:
  D = 5  (main's earlier check, B1955):  integral of G = 2 * 5^(s/2) * C(s) * zeta(s) L(s, chi_5)
  D = 12 (class number 1, unit of norm +1): integral of G = 12^(s/2) * C(s) * zeta(s) L(s, chi_12)   [the half]
  D = 40 (class number 2, unit of norm -1): integral of G = 40^(s/2) * C(s) * (zeta(s) L(s, chi_40) +- L(s, chi_5) L(s, chi_8)),
          + for the principal class, - for the other,  with C(s) = Gamma(s/2)^2/Gamma(s)."""
import math, functools
import numpy as np, mpmath as mp
print = functools.partial(print, flush=True)
mp.mp.dps = 25
kron = {5: lambda n: (0, 1, -1, -1, 1)[n % 5], 8: lambda n: {1: 1, 7: 1, 3: -1, 5: -1}.get(n % 8, 0), 12: lambda n: {1: 1, 11: 1, 5: -1, 7: -1}.get(n % 12, 0)}
kron[40] = lambda n: kron[5](n) * kron[8](n)
Lf = lambda s, q: sum(mp.mpf(kron[q](r)) * mp.zeta(s, mp.mpf(r) / q) for r in range(1, q) if kron[q](r)) / mp.mpf(q) ** s


def reduce(z):
    for _ in range(200):
        z = complex(z.real - round(z.real), z.imag)
        if abs(z) < 1 - 1e-13: z = -1 / z
        else: return z
    raise RuntimeError


def G(z, s, N):
    z = reduce(z); c = np.arange(-N, N + 1)[:, None].astype(float); d = np.arange(-N, N + 1)[None, :].astype(float)
    den = (c * z.real + d) ** 2 + (c * z.imag) ** 2; den[N, N] = np.inf; return float((z.imag ** s / den ** s).sum())


def period(form, D, s, nodes=96, N=(250, 500)):
    a, b, c = form; assert b * b - 4 * a * c == D; t, u = next((t, u) for u in range(1, 2000) for t in [math.isqrt(D * u * u + 4)] if t * t == D * u * u + 4)
    ell = 2 * math.log((t + u * math.sqrt(D)) / 2); cen, R = -b / (2 * a), math.sqrt(D) / (2 * abs(a)); xs, ws = np.polynomial.legendre.leggauss(nodes); ts = ell / 2 * xs; ws = ws * ell / 2
    vals = []
    for Nc in N: vals.append(sum(w * G(complex(cen + R * math.tanh(x), R / math.cosh(x)), s, Nc) for x, w in zip(ts, ws)))
    k = 2 ** (2 * s - 2); return (k * vals[1] - vals[0]) / (k - 1), ell, (t, u)


if __name__ == "__main__":
    for s in (2, 3):
        C = mp.gamma(mp.mpf(s) / 2) ** 2 / mp.gamma(s); z = mp.zeta(s)
        I, ell, tu = period((1, 1, -1), 5, s); rhs = 2 * mp.mpf(5) ** (mp.mpf(s) / 2) * C * z * Lf(s, 5)
        print("s = %d, D = 5, form [1, 1, -1] (length %.6f): integral %.8f; 2 * 5^(s/2) C zeta L(chi_5) = %.8f; relative difference %.1e" % (s, ell, I, float(rhs), abs(I / float(rhs) - 1)))
        for form in ((1, 2, -2), (3, 0, -1)):
            I, ell, tu = period(form, 12, s); full = mp.mpf(12) ** (mp.mpf(s) / 2) * C * z * Lf(s, 12)
            print("s = %d, D = 12, form %s (length %.6f, unit (%d + %d sqrt 12)/2): integral %.8f; 12^(s/2) C zeta L(chi_12) = %.8f, relative difference %.1e; against twice that (no half): %.1e" % (s, list(form), ell, *tu, I, float(full), abs(I / float(full) - 1), abs(I / float(2 * full) - 1)))
        for form, sign, name in (((1, 6, -1), 1, "principal"), ((2, 4, -3), -1, "the other class")):
            I, ell, tu = period(form, 40, s, nodes=220); a, b = z * Lf(s, 40), Lf(s, 5) * Lf(s, 8); pre = mp.mpf(40) ** (mp.mpf(s) / 2) * C
            print("s = %d, D = 40, form %s, %s (length %.6f): integral %.8f; 40^(s/2) C (zeta L(chi_40) %s L(chi_5) L(chi_8)) = %.8f, relative difference %.1e; with the other sign: %.1e; against the full Dedekind zeta alone: %.1e" % (
                s, list(form), name, ell, I, "+" if sign > 0 else "-", float(pre * (a + sign * b)), abs(I / float(pre * (a + sign * b)) - 1), abs(I / float(pre * (a - sign * b)) - 1), abs(I / float(pre * a) - 1)))
