"""B364 -- both lift classes arise as theta families; the T-side identities at 1e-15."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B364_theta_polarization'))
from theta_geometric import T_side_check, f_theta
import cmath


def test_triangular_family_carries_the_theta_lift_multiplier():
    assert T_side_check() < 1e-10


def test_square_family_carries_the_canonical_multiplier():
    tau = 0.31 + 1.13j
    z = 0.17 + 0.05j
    def e(x): return cmath.exp(2j * cmath.pi * x)
    def fam(j, zz, tt, K=40):
        s = 0
        for m in range(-K, K + 1):
            n = 15 * m + j
            s += e((n * n / 15) * tt + n * zz)
        return s
    worst = 0
    for j in range(15):
        lhs = fam(j, z, tau + 1)
        rhs = e(j * j / 15) * fam(j, z, tau)
        worst = max(worst, abs(lhs - rhs) / abs(rhs))
    assert worst < 1e-10
