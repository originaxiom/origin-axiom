"""B1854 (P-739): the tube's Im tau as the limit d -> 0 of the levels s0 + d, under the covariant root
tau_cov = Re tau + i Im tau sqrt(det E) (row 1614; basis-invariant, checked by the control below), reduced.
Calibration: B1847's committed k = 1 runs (gamma_runs/, 120 grid), against the web seat's sealed 6.14916(41).
Fits: (a) two points, Im(d) = I0 - a d^2 on d = 0.0005 and the mirror mean at 0.001; (b) three points, I0 - a d^2 - b d^4
on 0.0005, 0.001, 0.002 (mirror means where both signs exist)."""
import re, math, glob, sys, os
sys.path.insert(0, "../../B1847_the_level_surfaces_own_modulus/verification"); sys.path.insert(0, "../../B1846_the_metrics_read_out/verification")
from stage_b_modulus import reduce_tau
import numpy as np
def parse(path):
    t = open(path).read()
    m = re.search(r"tau ([+-][0-9.]+)([+-][0-9.]+)i\s+reduced\s+([+-][0-9.]+)([+-][0-9.]+)i\s+detE-1 ([+-][0-9.e-]+)", t)
    if not m: return None
    tau = complex(float(m.group(1)), float(m.group(2))); dE = float(m.group(5))
    return reduce_tau(complex(tau.real, tau.imag * math.sqrt(1 + dE))), reduce_tau(tau), dE
def table(files):
    rows = {}
    for d, f in files:
        r = parse(f)
        if r: rows[d] = r
    return rows
def fits(rows):
    I = lambda d: np.mean([rows[x][0].imag for x in (d, -d) if x in rows])
    a2 = I(0.0005) + (I(0.0005) - I(0.001)) / 3
    x = np.array([0.25, 1.0, 4.0]); y = np.array([I(0.0005), I(0.001), I(0.002)])
    A = np.c_[np.ones(3), -x, -x ** 2]; I0, a, b = np.linalg.solve(A, y)
    return a2, I0
B = "../../B1847_the_level_surfaces_own_modulus/verification/gamma_runs/"
k1 = table([(0.0005, B + "gamma_lim2_s0.0005.txt"), (0.001, B + "gamma_lim2_s0.001.txt"), (-0.001, B + "gamma_lim2_s-0.001.txt"),
            (0.002, B + "gamma_lim2_s0.002.txt"), (0.003, B + "gamma_lim2_s0.003.txt")])
k2 = table([(d, "runs/k2_s%.6f_N120.txt" % round(0.534940 + d, 6)) for d in (0.0005, 0.001, -0.001, 0.002, -0.002, 0.005)])
for name, rows, seat in (("k = 1 (B1847's runs)", k1, 6.14916), ("k = 2 (this arc's runs)", k2, 6.08186)):
    print(name)
    for d in sorted(rows):
        cov, old, dE = rows[d]
        print("   d = %+.4f: covariant %+.6f%+.6fi   (old formula %+.6f%+.6fi; det E - 1 %+.2e)" % (d, cov.real, cov.imag, old.real, old.imag, dE))
    a2, a3 = fits(rows)
    print("   limit d -> 0: two-point %.4f, three-point %.4f; the web seat's sealed value %.5f" % (a2, a3, seat))
