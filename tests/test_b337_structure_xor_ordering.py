"""B337 -- structure (XOR) ordering (Chat-2 insight, probed). sympy-only."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B337_structure_xor_ordering'))
from structure_xor_ordering import (single_object_spectrum, multiplicity_spectrum, is_ordered,
                                    multiplicity_overlap, metallic_disc, seeds_not_forced,
                                    distinct_hyperbolic_fields)


def test_single_object_is_degenerate():
    assert single_object_spectrum() == [52, 1, 1]        # one heavy, two equal light -> democratic


def test_multiplicity_orders():
    M = multiplicity_overlap()
    assert M.tolist() == [[2, 3, 6], [3, 2, 3], [6, 3, 2]]   # the genuine overlap (Chat-2)
    assert is_ordered(multiplicity_spectrum())               # three distinct magnitudes


def test_seeds_not_forced_and_structure_lost():
    assert seeds_not_forced()                            # arithmeticity selects {1,2}, not {1,2,3}
    assert len(set(distinct_hyperbolic_fields())) == 3   # distinct fields -> no shared E6
    assert [metallic_disc(m) for m in (1, 2, 3)] == [5, 32, 117]
