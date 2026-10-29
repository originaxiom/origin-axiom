"""THE CRITICAL LINE, POST HOC (labelled; written after the run's output was read, where P(-1/2) = 1.0986122887 was seen to
equal log 3): an exact check of the computed line at beta = -k/2, k = 0, 1, 2, 4, 8, 16.

Why it should hold.  For a hyperbolic M in SL(2, Z) with eigenvalues lam > 1 and 1/lam, the geodesic length is
l = 2 log lam, so e^(k l / 2) = lam^k, and tr Sym^k(M) = lam^k + lam^(k-2) + ... + lam^-k lies between lam^k and
lam^k / (1 - lam^-2); for parabolic words (lam = 1) the ratio is k + 1.  Summing over the 2^n words of length n,
sum_w tr Sym^k(M_w) = tr((Sym^k L + Sym^k R)^n), so the growth rate of sum_w e^(k l(w)/2), which is e^(P(-k/2)), is the
spectral radius of Sym^k L + Sym^k R (counting words instead of primitive classes does not change a growth rate).
Data-free.  The web seat, 2026-10-29.  0 of 19.
"""
import json, math, pathlib
import numpy as np
from math import comb

HERE = pathlib.Path(__file__).resolve().parent


def sym(M, k):
    """the matrix of Sym^k(M) on the basis x^(k-j) y^j, j = 0..k, for (x, y) -> (x, y) M (row action)"""
    (a, b), (c, d) = M
    S = np.zeros((k + 1, k + 1))
    for j in range(k + 1):            # image of x^(k-j) y^j: (a x + c y)^(k-j) (b x + d y)^j  [row vector (x, y) M]
        poly = np.zeros(k + 1)
        for i1 in range(k - j + 1):
            for i2 in range(j + 1):
                # x-power: (k-j-i1) from the first factor's x terms and (j - i2) from the second's
                coef = comb(k - j, i1) * comb(j, i2) * (a ** (k - j - i1)) * (c ** i1) * (b ** (j - i2)) * (d ** i2)
                poly[i1 + i2] += coef        # y-power i1 + i2
        S[j] = poly
    return S


run = json.loads((HERE / "critical_line.json").read_text())
P = {e["beta"]: e["P"] for e in run["line"]}
L, R = ((1, 1), (0, 1)), ((1, 0), (1, 1))
print("THE CRITICAL LINE, POST HOC: e^P(-k/2) against the spectral radius of Sym^k L + Sym^k R\n")
out = {}
for k in (0, 1, 2, 4, 8, 16):
    rho = max(abs(np.linalg.eigvals(sym(L, k) + sym(R, k))))
    b = -k / 2
    p = P.get(float(b), P.get(b))
    print("k = %2d (beta = %5.1f): log rho = %.10f   P(beta) = %.10f   difference %.1e" % (k, b, math.log(rho), p, math.log(rho) - p))
    out[k] = {"log_rho": math.log(rho), "P": p}
print("\nexact forms: k = 1: rho = 3; k = 2: rho = %.10f = (5 + sqrt 17)/2 = %.10f" % (
    max(abs(np.linalg.eigvals(sym(L, 2) + sym(R, 2)))), (5 + 17 ** 0.5) / 2))
(HERE / "sym_check.json").write_text(json.dumps(out, indent=1))
