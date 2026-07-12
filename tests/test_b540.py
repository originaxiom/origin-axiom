"""Locks for B540 — the observer flow."""
import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier',
                                'B530_natural_history'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier',
                                'B540_observer_flow'))
from listen_39_induction_engine import canonical_codes
from flow import SYSTEMS, derive_prefix


@pytest.fixture(scope='module')
def flow_map():
    canon = {canonical_codes(v): k for k, v in SYSTEMS.items()}
    flow, frontier = {}, []
    for name, codes in SYSTEMS.items():
        out = derive_prefix(canonical_codes(codes))
        if out not in canon:
            lbl = f"NEW_{len(frontier)}"
            canon[out] = lbl
            frontier.append((lbl, out))
        flow[name] = canon[out]
    while frontier:
        lbl, codes = frontier.pop()
        out = derive_prefix(codes)
        if out not in canon:
            nl = f"NEW_{len(canon)}"
            canon[out] = nl
            frontier.append((nl, out))
        flow[lbl] = canon[out]
    return flow


def test_sigma_is_fixed_point(flow_map):
    assert flow_map['S_a'] == 'S_a'


def test_flow_closes_on_12_nodes(flow_map):
    assert len(flow_map) == 12


def test_unique_2cycle(flow_map):
    """Exactly three fixed points and one 2-cycle; nothing longer."""
    fixed = {k for k, v in flow_map.items() if v == k}
    assert len(fixed) == 3 and 'S_a' in fixed
    two = {k for k in flow_map
           if k not in fixed and flow_map[flow_map[k]] == k}
    assert len(two) == 2
