"""SM-C7's step 3, run by main on its own code: is B1656's channel norm the Kronecker function plus a tau-only term?

The channel norm (B1656, as main's b1656_funcs.cA defines it): N(c, tau) = the regularised flat L^2 norm over the fibre's
parallelogram of K_c(u) = th1'(0) vartheta(c; u) / (vartheta(c; 0) th1(u)), i.e. int over P minus the eps-disc of |K_c|^2
d^2u - 2 pi log(1/eps) + pi eps^2 |a0|^2. Written before the run: at fixed tau, if N(c, tau) = alpha * log|vartheta(c; 0)|
+ beta * (Im of the characteristic)^2 * Im tau + gamma(tau) exactly over many c, the norm is a Kronecker function of c
plus a tau-only term, and its geodesic average is B1917's coefficient up to that term's average. A fit with a large
residual says it is not. Main's code (B1716's copy of B1656's functions for theta, th1 and the polar quadrature); no
measured value is read; no frame output (masses, mixings) is formed."""
import sys, math, pathlib, json
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1716_the_zeros_derived" / "verification"))
import b1656_funcs as F
from numpy.polynomial.legendre import leggauss


def th1p0(t, h=1e-6):
    return (F.th1(h, t) - F.th1(-h, t)) / (2 * h)


def K(c, u, t):
    a, b = c
    return th1p0(t) * F.thc(a, b, u, t) / (F.thc(a, b, 0.0, t) * F.th1(u, t))


def a0(c, t, rad=0.05, N=256):
    u = rad * np.exp(2j * np.pi * np.arange(N) / N)
    return complex(np.mean(K(c, u, t) - 1 / u))


def norm(c, t, eps=1e-5, nth=128, ns=96):
    br = F.vangles(t); xg, wg = leggauss(nth); xs, ws = leggauss(ns); tot = 0.0
    for lo_a, hi_a in zip(br[:-1], br[1:]):
        th = 0.5 * (hi_a - lo_a) * xg + 0.5 * (hi_a + lo_a); wt = 0.5 * (hi_a - lo_a) * wg
        hi = np.log(F.rmax_np(th, t)); lo = math.log(eps)
        sg = 0.5 * (hi - lo)[:, None] * xs[None, :] + 0.5 * (hi + lo)[:, None]; w2 = 0.5 * (hi - lo)[:, None] * ws[None, :]
        rr = np.exp(sg); z = rr * np.exp(1j * th)[:, None]
        tot += np.sum(wt[:, None] * w2 * np.abs(K(c, z, t)) ** 2 * rr ** 2)
    return float(tot - 2 * np.pi * math.log(1 / eps) + np.pi * eps ** 2 * abs(a0(c, t)) ** 2)


def features(c, t):
    a, b = c
    return [math.log(abs(complex(F.thc(a, b, 0.0, t)))), a * a * t.imag, 1.0]


if __name__ == "__main__":
    phi = (1 + 5 ** 0.5) / 2
    beta, betap = (3 + 5 ** 0.5) / 2 - 0.5, (3 - 5 ** 0.5) / 2 - 0.5        # a placeholder pair, replaced below
    # the golden ground's geodesic for gamma = M^T with M = [[2,1],[1,1]] (gamma: z -> (2z + 1)/(z + 1)): fixed points phi, -1/phi
    beta, betap = phi, -1 / phi
    pts = [(beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1) for s in (-0.6, 0.0, 0.6)]
    chars = [(i / 10, j / 10) for i in range(1, 10) for j in range(0, 10) if (i, j) != (5, 5)][::3]
    out = []
    for t in pts:
        t = complex(t)
        rows = [(c, norm(c, t)) for c in chars]
        A = np.array([features(c, t) for c, _ in rows]); y = np.array([n for _, n in rows])
        coef, *_ = np.linalg.lstsq(A, y, rcond=None)
        res = y - A @ coef
        out.append({"tau": [t.real, t.imag], "alpha, beta, gamma": coef.tolist(), "max |residual|": float(np.abs(res).max()),
                    "spread of N": float(y.max() - y.min()), "characters": len(rows)})
        print("tau %.4f%+.4fi" % (t.real, t.imag), "fit N = %.6f log|theta[c](0)| %+.6f a^2 Im tau %+.6f" % tuple(coef),
              "| max residual %.2e of a spread %.3f over %d characters" % (np.abs(res).max(), y.max() - y.min(), len(rows)), flush=True)
    (HERE / "step3_norm.json").write_text(json.dumps(out, indent=1))
