"""B474 — lock: the commutator-trace multiset on the torus + law 1 (fast part)."""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "frontier", "B474_tier_commutator_law"))


def test_commutator_trace_multiset():
    from cross_table import commutator_traces
    ctr = commutator_traces()
    assert dict(sorted(Counter(ctr.values()).items())) == {-5: 28, -1: 32, 3: 96, 15: 84}
