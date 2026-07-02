"""B359 -- the seam form: pair-specific and parity-selective (exact artifact locks)."""
import os
import sys
from fractions import Fraction as Fr

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B359_seam_form'))
from seam_form import load_banked


def test_pair_13_is_seam_dark():
    t13, _ = load_banked()
    assert len(t13) == 39
    assert all(v[3] == 0 for v in t13.values())          # golden x bronze: NO sqrt(-15), exactly


def test_pair_23_is_seam_bright_with_its_own_values():
    _, t23 = load_banked()
    assert len(t23) == 39
    seam = {k: v for k, v in t23.items() if v[3] != 0}
    assert len(seam) == 18
    svals = {v[3] for v in seam.values()}
    assert svals == {Fr(1, 144), Fr(-1, 144), Fr(1, 288), Fr(-1, 288)}
    # disjoint from the (1,2) s-set (B358): denominators 48..2880, none of {144, 288}
    assert seam[(0, 2)] == (Fr(1, 144), Fr(1, 144), Fr(5, 144), Fr(1, 144))
    assert seam[(1, 0)] == (Fr(1, 288), Fr(1, 288), Fr(5, 288), Fr(1, 288))


def test_h_membership_structure():
    t13, t23 = load_banked()
    for table in (t13, t23):
        for v in table.values():
            assert len(v) == 4                            # exact (p, q, r, s) in H


@pytest.mark.skipif(os.environ.get("OA_SLOW") != "1",
                    reason="full exact regeneration ~8 min; run under OA_SLOW=1")
def test_full_regeneration_slow():
    from seam_form import regenerate_matches_banked
    assert regenerate_matches_banked()
