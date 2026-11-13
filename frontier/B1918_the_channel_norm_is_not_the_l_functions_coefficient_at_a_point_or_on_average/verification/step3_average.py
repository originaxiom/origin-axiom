"""SM-C7 step 3, the average: is the geodesic average of B1656's channel norm N(c, tau) over one period of the golden
geodesic an affine function of the geodesic average of log|g_(c+1/2)| (the placement that fits best pointwise)? If not,
the norm is neither the L-function's Kronecker coefficient at a point nor as an average. Main's code."""
import math, json, pathlib
import numpy as np
import step3_norm as S
HERE = pathlib.Path(__file__).resolve().parent


def log_abs_g(a1, a2, z, nmax=60):
    a1 = a1 % 1.0; q = np.exp(2j * np.pi * z); B2 = a1 * a1 - a1 + 1 / 6
    out = np.real(B2 / 2 * 2j * np.pi * z) + np.log(np.abs(1 - np.exp(2j * np.pi * a1 * z) * np.exp(2j * np.pi * a2)))
    for n in range(1, nmax):
        out += np.log(np.abs(1 - q ** n * np.exp(2j * np.pi * a1 * z) * np.exp(2j * np.pi * a2)))
        out += np.log(np.abs(1 - q ** n * np.exp(-2j * np.pi * a1 * z) * np.exp(-2j * np.pi * a2)))
    return float(out)


phi = (1 + 5 ** 0.5) / 2
beta, betap, ell = phi, -1 / phi, 2 * math.log(phi ** 2)      # gamma = [[2,1],[1,1]] acting z -> (2z+1)/(z+1); lambda = phi^2
x, w = np.polynomial.legendre.leggauss(8)
ts = ell / 2 * x
zs = [complex((beta * 1j * math.exp(s) + betap) / (1j * math.exp(s) + 1)) for s in ts]
chars = [(i / 10, j / 10) for i in range(1, 10) for j in range(0, 10) if (i, j) != (5, 5)][::3]
avgN, avgG = [], []
for c in chars:
    avgN.append(ell / 2 * sum(wi * S.norm(c, z) for wi, z in zip(w, zs)))
    avgG.append(ell / 2 * sum(wi * log_abs_g(c[0] + .5, c[1] + .5, z) for wi, z in zip(w, zs)))
    print(c, "avg N %.6f" % avgN[-1], "avg log|g| %.6f" % avgG[-1], flush=True)
A = np.c_[avgG, np.ones(len(chars))]; co, *_ = np.linalg.lstsq(A, np.array(avgN), rcond=None)
r = np.array(avgN) - A @ co
print("fit avg N = %.6f avg log|g| %+.6f" % tuple(co), "| max residual %.3e of a spread %.3f" % (abs(r).max(), max(avgN) - min(avgN)))
(HERE / "step3_average.json").write_text(json.dumps({"chars": chars, "avgN": avgN, "avgG": avgG, "coef": co.tolist(),
                                                     "max_residual": float(abs(r).max())}, indent=1))
