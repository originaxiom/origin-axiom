# calibration C18: the unshifted F_0 (Kronecker's first limit formula) against a shifted F_u by a lattice difference
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import numpy as np, sm_c7_lib as L
z = complex(0.17, 1.05); Rm = 1500
for u in [(0.2, 0.3), (0.5, 0.5)]:
    tot = 0.0
    for mm in range(-Rm, Rm + 1):
        lam = mm * z + np.arange(-Rm, Rm + 1)
        a0 = np.abs(lam); a0 = np.where(a0 > 0, a0, np.inf)
        tot += np.sum(1 / np.abs(lam + (u[0] * z + u[1])) ** 2 - 1 / a0 ** 2)
    print("F_u - F_0 = %.7f   lattice %.7f" % (L.F_shift(u, z) - L.F_shift((0, 0), z), z.imag * tot))
