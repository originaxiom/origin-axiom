"""Main's own check of the odd L-value (owed since B1917, which did not recompute it), by the Siegel function, written
without reading the seats' code. Expectation, written before the run: for every one of the SM seat's 601 characters
(M, c = (i, j)/N), the winding Delta = log g_a(gamma z0) - log g_a(z0) of the Siegel function g_a, a = Jc = (-c2, c1)
reduced to [0, 1)^2 and gamma = M^T acting as z -> (a z + c)/(b z + d) (B1917's convention), satisfies:
(1) Re Delta = 0 (g_a(gamma z) = root of unity times g_a(z), since gamma fixes a mod Z^2);
(2) L_odd(1, chi_c) = kappa * (pi i) Delta with ONE universal constant kappa over all 601 characters, where L_odd(1) is
    the seat's step-2 value (SM-C7, verified nowhere on main until now). agy-exp's proof gives kappa = -2.
Kubert-Lang's product: g_a(z) = -q^{B2(a1)/2} e^{2 pi i a2 (a1 - 1)/2} (1 - q_a) prod_{n>=1} (1 - q^n q_a)(1 - q^n / q_a),
q = e^{2 pi i z}, q_a = e^{2 pi i (a1 z + a2)}, B2(x) = x^2 - x + 1/6. The winding is summed along the straight path from
z0 to gamma z0 (g has no zeros in H) with steps small enough for each ratio's argument to stay below pi/4."""
import cmath, json, math, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent


def logg(a1, a2, z, K=None):
    q = cmath.exp(2j * math.pi * z); qa = cmath.exp(2j * math.pi * (a1 * z + a2))
    if K is None:
        K = int(40 / (2 * math.pi * z.imag)) + 5
    n = np.arange(1, K + 1)
    qn = np.exp(2j * math.pi * n * z)
    s = np.sum(np.log(1 - qn * qa)) + np.sum(np.log(1 - qn / qa))
    B2 = a1 * a1 - a1 + 1 / 6
    return cmath.log(-1) + 2j * math.pi * z * B2 / 2 + 2j * math.pi * a2 * (a1 - 1) / 2 + cmath.log(1 - qa) + s


def winding_arc(a1, a2, zs, s0, s1, depth=0):
    """the continuous change of log g along the arc z(s), s from s0 to s1, by adaptive bisection (each piece's argument
    change below 1/2 radian)"""
    d = logg(a1, a2, zs(s1)) - logg(a1, a2, zs(s0))
    d = complex(d.real, (d.imag + math.pi) % (2 * math.pi) - math.pi)
    if abs(d.imag) < 0.5 or depth > 40:
        assert depth <= 40, "bisection did not settle"
        return d
    m = 0.5 * (s0 + s1)
    return winding_arc(a1, a2, zs, s0, m, depth + 1) + winding_arc(a1, a2, zs, m, s1, depth + 1)


if __name__ == "__main__":
    pop = json.loads((HERE / "received_sm" / "population.json").read_text())
    rows = {(json.dumps(r["level"]), r["i"], r["j"]): r for r in json.loads((HERE / "received_sm" / "sm_c7_results.json").read_text())["rows"]}
    kap, re_max, out = [], 0.0, []
    for o in pop:
        (a, b), (c, d) = o["M"]; N = o["N"]; c1, c2 = o["i"] / N, o["j"] / N
        A1, A2 = (-c2) % 1.0, c1 % 1.0
        tr = a + d; D = tr * tr - 4
        r1 = ((a - d) + math.sqrt(D)) / (2 * b); r2 = ((a - d) - math.sqrt(D)) / (2 * b)   # fixed points of gamma = M^T
        cen, R = (r1 + r2) / 2, abs(r1 - r2) / 2
        zs = lambda s: complex(cen + R * math.tanh(s), R / math.cosh(s))  # the geodesic by hyperbolic arclength
        ell = 2 * math.log((abs(tr) + math.sqrt(D)) / 2)
        g = lambda z: (a * z + c) / (b * z + d)
        s0 = -ell / 2
        s1 = s0 + ell if abs(g(zs(s0)) - zs(s0 + ell)) < 1e-7 * (1 + abs(zs(s0))) else s0 - ell
        assert abs(g(zs(s0)) - zs(s1)) < 1e-7 * (1 + abs(zs(s0))), "gamma does not move the arc by one period"
        Dl = winding_arc(A1, A2, zs, s0, s1)
        L = rows[(json.dumps(o["level"]), o["i"], o["j"])]["step2"]["c_odd"]["Lodd1"]
        Lv = complex(L[0], L[1])
        re_max = max(re_max, abs(Dl.real))
        if abs(Dl) > 1e-9:
            kap.append(Lv / (math.pi * 1j * Dl))
        out.append({"level": o["level"], "i": o["i"], "j": o["j"], "Delta": [Dl.real, Dl.imag]})
    kap = np.array(kap)
    print("601 characters: largest |Re Delta| %.1e; kappa = L_odd / (pi i Delta) over the %d characters with Delta != 0: "
          "real part from %.10f to %.10f, largest |imaginary part| %.1e" % (re_max, len(kap), kap.real.min(), kap.real.max(), np.abs(kap.imag).max()), flush=True)
    (HERE / "main_siegel.json").write_text(json.dumps(out))
