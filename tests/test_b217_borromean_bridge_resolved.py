"""B217 -- L40 resolved: closed period (B204) vs cusped volume (L31/Borromean). Nothing to CLAIMS.md.

Load-bearing locks:
 - B204's Z_k is the CLOSED torus-bundle invariant: Z_k(identity)=Z(T^3)=k+1.
 - the CUSPED figure-eight carries the hyperbolic VOLUME (Kashaev volume conjecture, Ohtsuki-corrected).
 - => period (closed/algebraic) and volume (cusped/geometric) are different invariants of different
   manifolds sharing gamma; the Borromean parent governs the volume, not the period.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B217_borromean_bridge_resolved"))
from closed_vs_cusped import Z_closed, vol_estimate, VOL_FIG8  # noqa: E402


def test_B204_is_closed_torus_bundle():
    # Z_k(identity monodromy) = Z(T^3) = dim rho_k = k+1  (the closed-bundle signature)
    for k in [1, 2, 3, 4, 5]:
        assert abs(Z_closed(0, 0, k) - (k + 1)) < 1e-6, k
    # the figure-eight CLOSED bundle is the period-5 1/phi object (B204), not the cusped one
    phi = (1 + 5 ** 0.5) / 2
    assert abs(abs(Z_closed(1, 1, 3)) - 1 / phi) < 1e-4


def test_cusped_figure_eight_carries_volume():
    # the Borromean/cusped side: Kashaev volume conjecture -> Vol(4_1), converging with N
    e200, e400, e700 = vol_estimate(200), vol_estimate(400), vol_estimate(700)
    assert abs(e700 - VOL_FIG8) < abs(e200 - VOL_FIG8)          # monotone convergence
    assert abs(e700 - VOL_FIG8) < 0.01                          # close to the hyperbolic volume
    # and the volume (~2.03) is a different order of object than the closed period (|Z|~O(1))
    assert VOL_FIG8 > 2.0 and abs(Z_closed(1, 1, 3)) < 1.0


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
