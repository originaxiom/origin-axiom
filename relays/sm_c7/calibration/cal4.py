import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
# calibration C8: the value coefficient. B1737's Z(0, chi) against the declared family of weight-2 periods
import math, numpy as np, sm_c7_lib as L
from fractions import Fraction as Fr
def fixed_chars(M, N):
    (a, b), (c, d) = M
    return [(i, j) for i in range(N) for j in range(N) if (i, j) != (0, 0) and ((i*a + j*c - i) % N, (i*b + j*d - j) % N) == (0, 0)]
rows = []
for M in ([[-3, -1], [-2, -1]], [[7, 4], [5, 3]], [[3, 1], [2, 1]]):
    geo = L.Geodesic(M)
    for N in (5, 6, 7, 8, 9, 10, 11, 12, 13):
        for (i, j) in fixed_chars(M, N)[:4]:
            c = (Fr(i, N), Fr(j, N)); Jc = (-c[1], c[0])
            z0 = L.Z0_b1737(geo, i, j, N)
            P = {"v c": L.period(geo, c, "v"), "v Jc": L.period(geo, Jc, "v"), "u c": L.period(geo, c, "u"), "u Jc": L.period(geo, Jc, "u")}
            lo = L.L_odd1(geo, i, j, N)
            rows.append((M, N, i, j, z0, P, lo))
            print(M, N, (i, j), "Z0 %.10f" % z0.real, " ".join("%s %.6f%+.6fj" % (k, v.real, v.imag) for k, v in P.items()), " Lodd1 %.8f%+.1ej" % (lo.real, lo.imag))
print()
for key in ("v c", "v Jc", "u c", "u Jc"):
    r = [ (z0.real / P[key]) * 4 * math.pi**2 if abs(P[key]) > 1e-9 else None for (_, _, _, _, z0, P, _) in rows]
    print(key, "4 pi^2 Z0/P:", ["%.6f%+.6fj" % (x.real, x.imag) if x is not None else None for x in r][:24])
print("Lodd1 vs v c period:", [("%.6f" % (P["v c"] / lo).real) if abs(lo) > 1e-9 else None for (_, _, _, _, z0, P, lo) in rows][:20])
