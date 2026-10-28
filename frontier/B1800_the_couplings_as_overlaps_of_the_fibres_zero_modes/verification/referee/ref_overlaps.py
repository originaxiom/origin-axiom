"""Referee B1800: independent recomputation (own theta series, Gauss-Legendre quadrature on the cell, not the trapezoid
grid; explicit covariant-holomorphy and boundary-condition checks; CIM normalisation predicted, not fitted).
    python3 -B ref_overlaps.py"""
import itertools, math, cmath
import numpy as np

def th(a, b, nu, T, N=30):
    """theta[a,b](nu, T) = sum_n exp(i pi (n+a)^2 T + 2 pi i (n+a)(nu+b)), vectorised in nu."""
    nu = np.atleast_1d(np.asarray(nu, dtype=complex))
    n = np.arange(-N, N + 1)[:, None] + a
    return np.exp(1j*np.pi*n*n*T + 2j*np.pi*n*(nu[None, :] + b)).sum(0)

def mode(M, j, a, b, z, t):
    """flux-M mode with boundary phases (a, b): e^{i pi M z Im z/Im t} theta[(j+a)/M, b](M z, M t)."""
    return np.exp(1j*np.pi*M*z*z.imag/t.imag) * th((j + a)/M, b, M*z, M*t)

def gl_grid(t, n=72):
    x, w = np.polynomial.legendre.leggauss(n); x = (x + 1)/2; w = w/2
    X, Y = np.meshgrid(x, x, indexing="ij"); W = np.outer(w, w)
    z = (X + t*Y).ravel(); dA = (W*t.imag).ravel()
    return z, dA

def inner(f, g, dA): return complex(np.sum(f*np.conj(g)*dA))

def checks(t):
    out = {}
    rng = np.random.default_rng(7)
    zz = rng.random(5) + t*rng.random(5)
    # covariant holomorphy (d/dzbar + pi M z/(2 Im t)) psi = 0, central differences
    h = 1e-5; worst = 0.0
    for M, (a, b) in [(1, (0.0, 0.0)), (1, (0.3, 0.17)), (2, (0.5, 0.5)), (2, (0.21, 0.4))]:
        f = lambda w: mode(M, 0, a, b, w, t)
        dx = (f(zz + h) - f(zz - h))/(2*h); dy = (f(zz + 1j*h) - f(zz - 1j*h))/(2*h)
        dzbar = 0.5*(dx + 1j*dy)
        r = np.abs(dzbar + np.pi*M*zz/(2*t.imag)*f(zz))/np.abs(f(zz))
        worst = max(worst, r.max())
    out["covariant_holomorphy"] = worst
    # boundary conditions: psi(z+1) = e^{2 pi i a} e^{i pi M Im z/Im t} psi(z); psi(z+t) = e^{-2 pi i b} e^{i pi M Im(conj(t) z)/Im t} psi(z)
    worst = 0.0
    for M, j, (a, b) in [(1, 0, (0.3, 0.17)), (2, 1, (0.21, 0.4)), (2, 0, (0.5, 0.0))]:
        f = mode(M, j, a, b, zz, t)
        r1 = mode(M, j, a, b, zz + 1, t)/(np.exp(2j*np.pi*a)*np.exp(1j*np.pi*M*zz.imag/t.imag)*f)
        r2 = mode(M, j, a, b, zz + t, t)/(np.exp(-2j*np.pi*b)*np.exp(1j*np.pi*M*(np.conj(t)*zz).imag/t.imag)*f)
        worst = max(worst, np.abs(r1 - 1).max(), np.abs(r2 - 1).max())
    out["boundary_conditions"] = worst
    return out

CH = {"3": (0.0, 0.0), "2": (0.5, 0.0), "4": (0.0, 0.5), "1": (0.5, 0.5)}
SECT = [(0.0, 0.0), (0.5, 0.0), (0.0, 0.5), (0.5, 0.5)]

def overlaps(t, n=72, chars=("3", "2", "4")):
    z, dA = gl_grid(t, n)
    psi = {}
    for p in chars:
        f = mode(1, 0, *CH[p], z, t); psi[p] = f/math.sqrt(inner(f, f, dA).real)
    chi = {}
    for s in SECT:
        for k in (0, 1):
            f = mode(2, k, *s, z, t); chi[(s, k)] = f/math.sqrt(inner(f, f, dA).real)
    Y = {}
    for p, q in itertools.combinations_with_replacement(chars, 2):
        s = ((CH[p][0] + CH[q][0]) % 1, (CH[p][1] + CH[q][1]) % 1)
        for k in (0, 1):
            Y[(p, q, k)] = inner(psi[p]*psi[q], chi[(s, k)], dA)
    # norms of raw modes against the CIM normalisation: int |theta-mode|^2 = sqrt(Im t / (2 M))
    raw = {M: inner(mode(M, 0, 0.13, 0.29, z, t), mode(M, 0, 0.13, 0.29, z, t), dA).real for M in (1, 2)}
    return Y, raw, psi, chi, z, dA

if __name__ == "__main__":
    for t in (complex(0.37, 1.2), complex(-0.21, 0.83), complex(0.05, 1.7)):
        c = checks(t)
        Y, raw, psi, chi, z, dA = overlaps(t)
        print("tau", t, "| covariant holomorphy %.1e | boundary conditions %.1e" % (c["covariant_holomorphy"], c["boundary_conditions"]))
        print("  raw norms: M=1 %.12f vs sqrt(Im/2) %.12f; M=2 %.12f vs sqrt(Im/4) %.12f" % (raw[1], math.sqrt(t.imag/2), raw[2], math.sqrt(t.imag/4)))
        # orthonormality within sector, and quadrature convergence n=72 vs n=96
        Y2 = overlaps(t, n=96)[0]
        print("  GL n=72 vs n=96 max diff %.1e" % max(abs(Y[k] - Y2[k]) for k in Y))
        G = max(abs(inner(chi[(s, 0)], chi[(s, 1)], dA)) for s in SECT)
        print("  within-sector cross-overlap %.1e" % G)
        K = t.imag**-0.25
        for (p, q, k), v in sorted(Y.items()):
            (a1, b1), (a2, b2) = CH[p], CH[q]
            # the CIM / Mumford closed form with the Higgs at characteristic ((k + s_a)/2, s_b), s = (a1+a2, b1+b2) mod 1
            sa, sb = (a1 + a2) % 1, (b1 + b2) % 1
            pred = 0j
            for m in (0, 1):
                ca, cb = (a1 + a2 + m)/2, b1 + b2
                tgt_a, tgt_b = (k + sa)/2, sb
                da, db = ca - tgt_a, cb - tgt_b
                if abs(da - round(da)) < 1e-12 and abs(db - round(db)) < 1e-12:
                    pred += th((a1 - a2 + m)/2, b1 - b2, 0j, 2*t)[0]*cmath.exp(2j*math.pi*ca*round(db))
            pred *= K
            print("  Y[%s%s;k=%d] = %+.10f%+.10fi  closed form K*theta: %+.10f%+.10fi  |diff| %.1e" % (p, q, k, v.real, v.imag, pred.real, pred.imag, abs(v - pred)))
    print("ref_overlaps exit 0")
