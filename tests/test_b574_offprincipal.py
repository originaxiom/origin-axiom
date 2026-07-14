"""B574 — the off-principal proposal: the two locks.

  (1) the minimal nilpotent orbit of E6 (= the A1 orbit, highest-root sl2) has
      reductive centralizer of dimension 35 = A5 = su(6) — NOT 45 = D5 = so(10);
      adjoint grading under the highest-root coweight = (1, 20, 30, 20, 1);
  (2) the 27 under the minimal sl2 = 6 V1 + 15 V0 (gradings {+-1: 6, 0: 15}) —
      every summand self-dual: the fifth wall applies verbatim at the minimal
      embedding; the obstruction is rank-1-ness, not the choice of orbit.
See frontier/B574_offprincipal/FINDINGS.md.
"""
from collections import Counter

from helpers_e6 import cartan_ip, fundamental_coweight_orbit, highest_root, root_system, sl2_grading


def test_minimal_orbit_centralizer_is_a5_not_d5():
    roots = root_system()
    assert len(roots) == 72
    theta = highest_root(roots)
    assert list(theta) == [1, 2, 2, 3, 2, 1]                 # the highest root
    grading = Counter(int(cartan_ip(r, theta)) for r in roots)
    assert dict(grading) == {-2: 1, -1: 20, 0: 30, 1: 20, 2: 1}
    z_triple = (grading[0] + 6) - 1                          # ker(ad e_theta: g0 -> g2)
    assert z_triple == 35                                    # = dim A5 = su(6)
    assert z_triple != 45                                    # != dim D5 = so(10)


def test_27_at_minimal_embedding_self_dual():
    theta = highest_root(root_system())
    orbit = fundamental_coweight_orbit()          # the 27-weight orbit (shared BFS)
    g27 = sl2_grading(orbit, theta)
    assert dict(g27) == {-1: 6, 0: 15, 1: 6}                 # 6 V1 + 15 V0: all self-dual
