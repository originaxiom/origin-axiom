"""B1388 lock -- THE CUTOFF TEST (sealed 68c1b809; outcome UNSTABLE) and its post-seal anatomy.

One K_n = 10 solve of B1387's instrument reproduces, at the heights that decide them:
- the sealed finding: at both Eisenstein cusps the relative index's chi(d+) is +2 at tau = 0.15 and -1 at 0.25 (the transition sits at
  0.1867, cusp 3 fitted independently: the swap, unimposed); cusp 1 stays annular;
- the anatomy: at tau = 0.183 Morse's boundary count Phi (the signed Higgs zeros, exact) is already -1 while the relative index is still
  +2 -- the two counts part between the Higgs zeros at 0.1791 and the tangency at 0.1867;
- the orbit of three Higgs zeros sits at the height where the neighbourhoods of cusps 0 and 3, grown together, first touch
  (SnapPy: volume 9 sqrt3 each, tau_joint = 0.1790950).
The run records carry K_n = 14 and 20, the bisected transitions, the zero census and the touching-point offsets."""
import importlib.util
import math
import warnings
from pathlib import Path

import pytest

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1388_the_cutoff_test" / "verification"


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, VER / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def solved():
    HZ = _load("b1388_higgs_zeros", "higgs_zeros.py")          # loads cutoff_test.py (the sealed test) as HZ.CT
    M = HZ.HF.member()
    S, x, st = HZ.HF.solve(M, 10, 0.10, 1, 1)
    assert st["full rank"] and st["fit residual rms"] < 1e-3
    return HZ, M, S, x


def test_the_count_depends_on_the_cutoff(solved):
    HZ, M, S, x = solved
    CT = HZ.CT
    for c in (0, 3):                                     # the Eisenstein cusps: +2 below the transition, -1 above it
        assert CT.chi_at(S, x, c, 0.15)[0] == 2
        assert CT.chi_at(S, x, c, 0.25)[0] == -1
    assert CT.chi_at(S, x, 1, 0.20)[0] == 0 and CT.chi_at(S, x, 1, 0.60)[0] == 0
    emb = CT.embedded_heights(M, S)
    assert abs(emb[0]["tau_emb"] - 0.08955) < 1e-4 and abs(emb[3]["tau_emb"] - 0.08955) < 1e-4    # the cut at 0.15 is admissible


def test_the_two_counts_part_between_the_zeros_and_the_tangency(solved):
    HZ, M, S, x = solved
    for c in (0, 3):
        phi, complete, _ = HZ.phi(S, x, c, 0.183)
        assert complete and phi == -1                    # the orbit zeros (0.1791) are below the cut: counted
        assert HZ.CT.chi_at(S, x, c, 0.183)[0] == 2      # the relative index has not yet made its tangency transition (0.1867)
        assert HZ.phi(S, x, c, 0.15)[0] == 2             # below the orbit zeros both counts read +2


def test_the_orbit_zeros_sit_where_the_eisenstein_cusps_touch(solved):
    HZ, M, S, x = solved
    tj0, tj3, V0, V3, _, _ = HZ.joint_height(M)
    assert abs(V0 - 9 * math.sqrt(3)) < 1e-6 and abs(V3 - 9 * math.sqrt(3)) < 1e-6
    assert abs(tj0 - 0.1790950) < 1e-6
    zs = HZ.zeros(S, x, 0, 0.17, 0.19, ns=8, nh=6)
    assert len(zs) == 3 and all(z[1] == -1 for z in zs)                  # an R-orbit of three, index -1
    assert all(abs(z[0][2] - tj0) < 5e-4 for z in zs)                     # at the joint touching height (K_n 20: 6e-8)
    assert all(abs(z[3]) < 1e-10 for z in zs)                             # harmonic: the Euclidean Hessian is traceless
