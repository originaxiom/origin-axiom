"""P9 — figure-eight knot complement (4_1) verified data.

The constants are hard-coded SnapPy / literature values so the suite runs
without SnapPy; an optional live cross-check runs only if SnapPy is installed.
"""

import pytest

from origin_axiom.constants import CS_FIG8, CS_SISTER, VOL_FIG8


def test_figure_eight_constants():
    assert abs(VOL_FIG8 - 2.0298832128) < 1e-9   # minimal hyperbolic volume
    assert CS_FIG8 == 0.0                        # Chern-Simons invariant
    assert CS_SISTER == 0.25                     # sister m003 differs in CS


def test_snappy_volume_crosscheck_if_available():
    snappy = pytest.importorskip("snappy")
    M = snappy.Manifold("4_1")
    assert abs(M.volume() - VOL_FIG8) < 1e-6
