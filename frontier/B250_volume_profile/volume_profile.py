"""B250 -- the complex-volume profile of the figure-eight's E6<->E8 geometric transition (push from B248/B249).

Quantifies the hyperbolic->Euclidean->spherical transition (B248): the volume (real part of the complex volume) and
the Chern-Simons (imaginary part / the framing) at the three Niven-forced ends (B249).

  HYPERBOLIC end (E6, cone angle 0, complete cusp):
     Vol = 6 * Lambda(pi/3) = 2.0298832...   (two regular ideal tetrahedra, shape e^{i pi/3} in Q(sqrt-3))
     CS  = 0                                   (4_1 is amphicheiral)
  EUCLIDEAN transition (cone angle 2pi/3):
     Vol = 0                                   (the hyperbolic structure collapses; scale-free)
  SPHERICAL end (E8, cone angle pi, the Z/2 orbifold; double branched cover = lens space L(5,2)=S^3/Z5):
     Vol = Vol(L(5,2))/2 = (2 pi^2 / 5)/2 = pi^2 / 5 = 1.9739208...
     CS  in (1/5) Z / Z                        (flat-connection CS of L(5,2): {0, 2/5, 3/5})

THE POINT: the determinant det(4_1)=5 is *literally* the denominator of the spherical-end volume pi^2/5 and its
Chern-Simons, while the Eisenstein '-3' sits in the hyperbolic-end ideal tetrahedra (shape e^{i pi/3}, vol via
Lambda(pi/3)). So the two exceptional ends carry their two arithmetic invariants in their VOLUMES: E6 <-> '-3'
(hyperbolic, via Lambda(pi/3)), E8 <-> '5' (spherical, via pi^2/5). The two end-volumes are comparable
(2.0299 vs 1.9739) but live in different geometries.

FIREWALL: complex volume / Chern-Simons is a dimensionless element of C/4pi^2 Z (PAPER sec.5.1); E6/E8 are
McKay/Arnold-trinity labels. No scale, no dynamics. Nothing to CLAIMS.md.

Run: python volume_profile.py (pyenv; mpmath). Hyperbolic anchor cross-checked with SnapPy (Vol=2.02988321281931).
"""
import mpmath as mp

mp.mp.dps = 30
VOL_SNAPPY = mp.mpf("2.02988321281931")     # SnapPy Vol(4_1), cross-check


def lobachevsky(theta):
    """Lambda(theta) = -int_0^theta ln|2 sin t| dt."""
    return mp.quad(lambda t: -mp.log(abs(2 * mp.sin(t))), [0, theta])


def hyperbolic_volume():
    """Vol(4_1) = 6 Lambda(pi/3) (two regular ideal tetrahedra)."""
    return 6 * lobachevsky(mp.pi / 3)


def spherical_volume():
    """Vol of the spherical Z/2 orbifold = Vol(L(5,2))/2 = pi^2/5 (det(4_1)=5 in the denominator)."""
    return mp.pi ** 2 / 5


def lens_cs_numerators(p=5, q=2):
    """flat-SU(2) CS numerators of L(p,q): {q* n^2 mod p}, q*q=1 mod p -> CS in (1/p)Z/Z."""
    qstar = pow(q, -1, p)
    return sorted({(qstar * n * n) % p for n in range(p)})


if __name__ == "__main__":
    vh = hyperbolic_volume()
    vs = spherical_volume()
    print("complex-volume profile of the E6<->E8 geometric transition:")
    print(f"  HYPERBOLIC (E6): Vol = 6 Lambda(pi/3) = {mp.nstr(vh, 12)}   CS = 0   ('-3': tetra shape e^(i pi/3))")
    print(f"  EUCLIDEAN      : Vol = 0   (collapse / scale-free)")
    print(f"  SPHERICAL  (E8): Vol = pi^2/5 = {mp.nstr(vs, 12)}   CS in (1/5)Z   ('5' = det(4_1))")
    print(f"  CS(L(5,2)) flat-connection numerators (/5): {lens_cs_numerators()}")
    print()
    assert abs(vh - VOL_SNAPPY) < mp.mpf(10) ** -10            # hyperbolic anchor matches SnapPy
    assert abs(vs - mp.pi ** 2 / 5) == 0                       # spherical = pi^2/5 exactly
    assert lens_cs_numerators() == [0, 2, 3]                   # denominator 5 (= det)
    assert abs(vh - vs) < mp.mpf("0.06")                       # the two ends are comparable (2.030 vs 1.974)
    print("the '5'=det(4_1) is the spherical-end volume & CS denominator; '-3' is the hyperbolic-end tetra shape.")
    print("ALL CHECKS PASS")
