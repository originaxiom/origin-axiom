"""B222 / Act I -- emergent SUSY confirmed via the finite-size operator content. Nothing to CLAIMS.md.

Load-bearing locks:
  (1) the momentum-ED CORRECTNESS GATE: union of all sector spectra == the full spectrum (machine precision)
      -- proves the momentum decomposition is exact (must pass before any dimension claim).
  (2) the NS-sector (even N) spinless dimensions reproduce the tricritical-Ising primaries {0,1/10,3/5,3/2},
      INCLUDING the h=3/2 SUPERCURRENT at x=3.0 (the emergent-SUSY generator).
  (3) the R-sector (odd N) 2nd spinless level -> 2(7/16-3/80)=0.8 (the R primaries 3/80, 7/16).
Small N for test speed; the reproducer goes larger.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B222_golden_chain_operator_content"))
from momentum_ed import correctness_gate, scaling_dimensions, r_sector_gap  # noqa: E402


def test_momentum_decomposition_is_exact():
    # the gate: sum of momentum-sector spectra == full spectrum, to machine precision
    for N in (10, 12, 14):
        assert correctness_gate(N)


def test_ns_sector_tricritical_ising_primaries():
    # even-N NS sector: spinless dims -> {0, 1/10, 3/5, 3/2} (x = 0, 0.2, 1.2, 3.0)
    v, x = scaling_dimensions(18, nlev=6)
    assert abs(x[0]) < 1e-6                       # identity
    assert abs(x[1] - 0.2) < 0.05                 # h=1/10
    assert abs(x[2] - 1.2) < 0.06                 # h=3/5
    # the SUPERCURRENT: h=3/2 primary at x=3.0 (the SUSY generator), essentially exact
    assert abs(x[4] - 3.0) < 0.05
    assert abs(x[4] - 3.0) < abs(x[4] - 2.0) and abs(x[4] - 3.0) < abs(x[4] - 4.0)


def test_r_sector_ramond_primaries():
    # odd-N realizes the Ramond sector: a low spinless level near 0.8 = 2(7/16 - 3/80) -- the R primaries
    # {3/80, 7/16}. [consistent] tier: at small N it sits ~0.84, trending to 0.8 with N; it is clearly NOT
    # the NS first excitation (0.2), proving odd-N is a DIFFERENT (R) topological sector.
    g17 = r_sector_gap(17)
    assert 0.78 < g17 < 0.90               # consistent with 0.8 = 2(7/16-3/80) (noisy at small N)
    assert g17 > 0.5                        # distinct from the NS first excitation x=0.2
    g21 = r_sector_gap(21)                  # larger N sharpens the trend toward 0.8
    assert g21 < g17 and abs(g21 - 0.8) < abs(g21 - 0.875)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
