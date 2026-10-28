"""L251 (b): the off-diagonal overlaps against B1636's matrix across tau.  For each off-diagonal pair the overlap with its
own sector's two flux-two modes is c_{pq,k}(tau); test (i) whether c_{pq,1}/c_{pq,0} is tau-independent (one Higgs
combination per sector), and (ii) whether the ratios Y_32/theta4^2 : Y_24/theta3^2 : Y_34/theta2^2 are tau-independent
(B1636's matrix from a fixed Higgs), against the alternative pattern c_pq ~ theta_r(tau)^p for other powers; within-sector
orthonormality of the flux-two modes checked."""
import math, numpy as np
import overlaps as O
taus = [complex(a, b) for a, b in ((0.37, 1.2), (0.11, 0.9), (0.0, 1.0), (0.25, 1.5), (-0.3, 1.1), (0.45, 2.0), (0.2, 0.8))]
def thc(a, b, t): return complex(O.theta(a, b, np.array([0j]), t)[0])
rows = []
for t in taus:
    per, ip, ortho, Y = O.run(t, n=96)
    # within-sector orthonormality
    x, y = np.meshgrid(np.arange(96) / 96, np.arange(96) / 96, indexing="ij"); z = (x + t * y).ravel(); dA = t.imag / 96**2
    wo = 0.0
    for (a, b) in O.SECT:
        f = [O.mode(2, (k + a) / 2, b, z, t) for k in (0, 1)]
        f = [g / math.sqrt(np.sum(np.abs(g)**2) * dA) for g in f]
        wo = max(wo, abs(np.sum(f[0] * np.conj(f[1])) * dA))
    th2, th3, th4 = thc(0.5, 0, t), thc(0, 0, t), thc(0, 0.5, t)
    c32 = (Y[("3", "2", 0.5, 0.0, 0)], Y[("3", "2", 0.5, 0.0, 1)])
    c24 = (Y[("2", "4", 0.5, 0.5, 0)], Y[("2", "4", 0.5, 0.5, 1)])
    c34 = (Y[("3", "4", 0.0, 0.5, 0)], Y[("3", "4", 0.0, 0.5, 1)])
    rows.append((t, wo, c32, c24, c34, th2, th3, th4))
    print("tau %s | within-sector cross-overlap %.1e | k1/k0: 32 %s, 24 %s, 34 %s" % (t, wo, np.round(c32[1] / c32[0], 6), np.round(c24[1] / c24[0], 6), "k1 %.1e" % abs(c34[1])))
print()
print("B1636's pattern (Y_pq / theta_r(tau)^2, r the third parity; ratios to the 34 entry):")
for (t, wo, c32, c24, c34, th2, th3, th4) in rows:
    a, b, c = c32[0] / th4**2, c24[0] / th3**2, c34[0] / th2**2
    print("  tau %-18s |32/th4^2 : 34/th2^2| %.6f   |24/th3^2 : 34/th2^2| %.6f" % (t, abs(a / c), abs(b / c)))
print("the overlaps' own pattern, |c_pq| against |theta_p theta_q| and |theta_r|^2 (Im-tau normalised by the 34 entry):")
for (t, wo, c32, c24, c34, th2, th3, th4) in rows:
    print("  tau %-18s |c32|/|c34| %.6f  |c24|/|c34| %.6f  || |th2|/|th4| %.6f  |th2|/|th3| %.6f  || |th2^2/th4^2| %.6f" % (
        t, abs(c32[0]) / abs(c34[0]), abs(c24[0]) / abs(c34[0]), abs(th2 / th4), abs(th2 / th3), abs(th2**2 / th4**2)))
print("compare exit 0")
