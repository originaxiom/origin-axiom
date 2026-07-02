"""B358 -- the seam certification: theta lift carries sqrt(-15) exactly; canonical lift exactly not."""
import os
import sys
from fractions import Fraction as Fr

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B358_seam_certification'))
from seam_certification import double_one, singles_clean, numeric_spot_check, run_all, FLAGSHIP


def test_flagship_exact():
    # the cross-session claim, certified coefficient-for-coefficient at its label
    assert double_one("C_theta.json", 0, 4) == FLAGSHIP
    # its Galois partner flips the imaginary coefficients
    p, q, r, s = double_one("C_theta.json", 0, 8)
    assert (p, q) == (Fr(-1, 48), Fr(-1, 80)) and (r, s) == (Fr(1, 48), Fr(-1, 48))


def test_canonical_lift_is_seam_free_samples():
    for (a, b) in ((0, 4), (1, 3), (5, 2), (6, 2), (9, 1)):
        sol = double_one("C_canonical.json", a, b)
        assert sol[3] == 0, ((a, b), sol)            # s = 0 exactly


def test_controls_exactly_clean():
    assert singles_clean("C_theta.json")             # r = s = 0 on every single-seed trace
    assert singles_clean("C_canonical.json")


def test_committed_tables_numeric_guard():
    assert numeric_spot_check("C_theta.json")        # exact tables match fresh dps-40 numerics
    assert numeric_spot_check("C_canonical.json")


@pytest.mark.skipif(os.environ.get("OA_SLOW") != "1",
                    reason="full 240-double readout x2 ~minutes; banked counts under OA_SLOW=1")
def test_full_counts_slow():
    r = run_all()
    assert r["theta_nonzero"] == 49 and r["theta_seam"] == 44
    assert r["canonical_nonzero"] == 49 and r["canonical_seam"] == 0
    assert r["flagship"] and r["controls"]
