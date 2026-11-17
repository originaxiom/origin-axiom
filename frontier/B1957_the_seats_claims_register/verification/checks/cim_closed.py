"""B1957: the closed-fibre triple overlap in closed form, derived by main and checked against main's quadrature
(cim_overlap.py).  Data-free.
With zeta_H = (zeta_L + zeta_R)/2 and xi = (zeta_L - zeta_R)/2 the product of two zero modes of flux 3 is, by the
addition formula theta[a1](x, 3 tau) theta[a2](y, 3 tau) = sum over m in {0, 1} of
theta[(a1 + a2 + m)/2](x + y, 6 tau) theta[(a1 - a2 + m)/2](x - y, 6 tau), a combination of the zero modes of flux 6:
    Y_ijk(tau, xi) = (3 Im tau)^(1/4) exp(6 pi i xi Im xi / Im tau) exp(2 pi i k / 6) theta[(i - j + 3m)/6, 0](6 xi, 6 tau)
for k = i + j + 1 + 3m mod 6, m in {0, 1}, and zero otherwise.  It depends on the Wilson lines through xi alone.
Consequences used later: for one Higgs mode k the matrix Y_ij is monomial (one entry in each row and column), with
moduli |theta[c/6](6 xi, 6 tau)|, c = 1, 3, 5 up to order."""
import numpy as np, mpmath as mp


def theta(a, z, tau, nw=40):
    n = np.arange(-nw, nw + 1) + a - np.round(a + z.imag / tau.imag)            # centred on the largest term
    return np.exp(1j * np.pi * n ** 2 * tau + 2j * np.pi * n * z)


def Y(tau, xi):
    """the 3 x 3 x 6 tensor at Wilson-line difference 2 xi (double precision; the Gaussian factor is kept inside the sum)"""
    out = np.zeros((3, 3, 6), complex); y = tau.imag; pre = (3 * y) ** 0.25
    for i in range(3):
        for j in range(3):
            for m in (0, 1):
                k = (i + j + 1 + 3 * m) % 6; a = ((i - j + 3 * m) % 6) / 6
                n = np.arange(-40, 41) + a - np.round(a + xi.imag / y)
                e = 6j * np.pi * xi * xi.imag / y + 6j * np.pi * n ** 2 * tau + 12j * np.pi * n * xi
                out[i, j, k] = pre * np.exp(2j * np.pi * k / 6) * np.exp(e).sum()
    return out


def Y_mp(tau, xi, dps=40):
    """the same at extended precision (for points high in the cusp)"""
    mp.mp.dps = dps; tau = mp.mpc(tau); xi = mp.mpc(xi); y = mp.im(tau); out = {}
    for i in range(3):
        for j in range(3):
            for m in (0, 1):
                k = (i + j + 1 + 3 * m) % 6; a = mp.mpf((i - j + 3 * m) % 6) / 6; c = mp.nint(a + mp.im(xi) / y)
                s = mp.mpc(0)
                for nn in range(-12, 13):
                    n = nn + a - c; s += mp.exp(6j * mp.pi * xi * mp.im(xi) / y + 6j * mp.pi * n ** 2 * tau + 12j * mp.pi * n * xi)
                out[i, j, k] = (3 * y) ** mp.mpf("0.25") * mp.exp(2j * mp.pi * k / 6) * s
    return out


if __name__ == "__main__":
    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import cim_overlap as C
    worst = wmp = 0.0
    for tau, (a, b) in C.POINTS:
        w = a * tau + b
        for name, qL, qR in C.SECTORS:
            zL, zR = qL * w, qR * w; Yq = C.overlap(tau, zL, zR, (zL + zR) / 2); Yc = Y(tau, (zL - zR) / 2)
            worst = max(worst, np.abs(Yq - Yc).max())
            Ym = Y_mp(tau, (zL - zR) / 2); wmp = max(wmp, max(abs(complex(v) - Yc[key]) for key, v in Ym.items()))
    print("the closed form against the quadrature at 12 cases (four moduli, points of orders 5, 10, 15, three sectors): %.1e; double against extended precision: %.1e" % (worst, wmp))
    tau = 0.13 + 1.1j; xi = 0.37 * tau - 0.21; Y0 = Y(tau, xi)
    mono = all(sum(abs(Y0[i, j, k]) > 1e-12 for j in range(3)) == 1 for i in range(3) for k in range(6))
    print("for each Higgs mode the matrix has one entry in each row: %s; so with one Higgs mode the mixing matrix is a permutation matrix" % mono)
