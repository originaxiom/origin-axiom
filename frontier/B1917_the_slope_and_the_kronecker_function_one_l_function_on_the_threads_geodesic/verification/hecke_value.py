"""Main's own check, behind the SM seat, of SM-C7's step 1 (the seat's sealed convention at ae5f6d7d1):

    Z(0, chi_c) = (1 / 4 pi^2) * integral from z0 to gamma z0, along the geodesic of gamma = M^T, of G^(Jc)*(z) dz,

with chi_c(v) = e((i v0 + j v1)/N) fixed by M, c = (i, j)/N, Jc = (-c2, c1), gamma: z -> (a z + c)/(b z + d) for
M = [[a, b], [c, d]], and G^(u)*(z) = sum over (m, n) in u + Z^2 of (m z + n)^(-2), minus pi/y (inner sum over n).
Z(0, chi) is B1737's own (its cone-parallelogram code), not recomputed here.

Main's code, written without reading the seat's library: the inner sum over n is pi^2 / sin^2(pi (m z + u2)) in closed
form; the sum over m is truncated where |m| y > 7; the integral is Gauss-Legendre over a window of one period centred
at the geodesic's top, at two node counts. No data; nothing of the frame (B1656) is read."""
import sys, io, json, math, cmath, contextlib, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1737_the_slope_is_a_zeta_value" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import the_slope_is_a_zeta_value as B


def Gstar(u1, u2, z):
    z = np.asarray(z, dtype=complex); y = z.imag
    K = int(7.0 / y.min()) + 3
    k = np.arange(-K, K + 1)
    m = u1 + k
    a = m[None, :] * z[:, None] + u2
    # pi^2 / sin^2(pi a) = -4 pi^2 q / (1 - q)^2 with q = e^(2 pi i a) when Im a > 0, and with q = e^(-2 pi i a) when
    # Im a < 0: |q| < 1 in both, so no overflow (the first version used sin directly and gave NaN far up the lattice)
    up = a.imag >= 0
    q = np.where(up, np.exp(2j * np.pi * np.where(up, a, 0)), np.exp(-2j * np.pi * np.where(up, 0, a)))
    terms = -4 * np.pi ** 2 * q / (1 - q) ** 2
    real_row = np.abs(m) <= 1e-12                                  # m = 0: the sum over n alone, pi^2 / sin^2(pi u2)
    if real_row.any():
        terms[:, real_row] = (np.pi ** 2 / np.sin(np.pi * u2) ** 2) if abs(u2 - round(u2)) > 1e-12 else 0
    out = terms.sum(1) - np.pi / y
    assert np.all(np.isfinite(out)), "a non-finite value of G*"
    return out


def period(M, u, nodes=200):
    a, b, c, d = int(M[0][0]), int(M[0][1]), int(M[1][0]), int(M[1][1])
    g = lambda z: (a * z + c) / (b * z + d)                       # gamma = M^T
    D = (a + d) ** 2 - 4
    r1 = ((a - d) + math.sqrt(D)) / (2 * b); r2 = ((a - d) - math.sqrt(D)) / (2 * b)
    beta, betap = max(r1, r2), min(r1, r2)
    lam = max(abs(((a + d) + math.sqrt(D)) / 2), abs(((a + d) - math.sqrt(D)) / 2))
    ell = 2 * math.log(lam)
    zt = lambda t: (beta * 1j * np.exp(t) + betap) / (1j * np.exp(t) + 1)
    dz = lambda t: 1j * np.exp(t) * (beta - betap) / (1j * np.exp(t) + 1) ** 2
    t0 = -ell / 2
    if abs(g(zt(t0)) - zt(t0 + ell)) < 1e-8 * (1 + abs(zt(t0))):
        lo, hi = t0, t0 + ell
    elif abs(g(zt(t0)) - zt(t0 - ell)) < 1e-8 * (1 + abs(zt(t0))):
        lo, hi = t0, t0 - ell
    else:
        raise RuntimeError("gamma does not move the geodesic by one period")
    x, w = np.polynomial.legendre.leggauss(nodes)
    t = 0.5 * (hi - lo) * x + 0.5 * (hi + lo)
    return 0.5 * (hi - lo) * np.sum(w * Gstar(u[0], u[1], zt(t)) * dz(t))


def run(levels=None, nodes=(160, 240)):
    SL = B._sl(); rows = []
    for st, k in (levels or B.LEVELS):
        eps = 1 if st[0] == "+" else -1; word = st[1:]
        with contextlib.redirect_stdout(io.StringIO()):
            N, F, S = SL.exact_slopes(eps, word, k)
        M = B.abel_M(SL, eps, word, k)
        for (i, j, _) in S:
            if (i, j) == (0, 0):
                continue
            Z = B.Z0(M, i, j, N)
            u = (-j / N, i / N)                                   # Jc = (-c2, c1)
            P = [period(M, u, n) / (4 * math.pi ** 2) for n in nodes]
            rows.append({"level": [st, k], "N": N, "ij": [i, j], "Z0": [Z.real, Z.imag],
                         "P/4pi^2": [P[-1].real, P[-1].imag], "diff": abs(P[-1] - Z), "nodes_gap": abs(P[-1] - P[0])})
    return rows


if __name__ == "__main__":
    lv = None
    if len(sys.argv) > 1 and sys.argv[1] == "one":
        lv = [("+LR", 2)]
    rows = run(lv)
    assert all(r["diff"] == r["diff"] and r["nodes_gap"] == r["nodes_gap"] for r in rows), "a NaN among the rows"
    print("characters:", len(rows), "| max |P/4pi^2 - Z0|:", max(r["diff"] for r in rows),
          "| max node gap:", max(r["nodes_gap"] for r in rows))
    for r in rows[:6]:
        print(r["level"], r["ij"], "Z0", [round(x, 10) for x in r["Z0"]], "P", [round(x, 10) for x in r["P/4pi^2"]])
    (HERE / ("hecke_value_one.json" if lv else "hecke_value.json")).write_text(json.dumps(rows, indent=1))
