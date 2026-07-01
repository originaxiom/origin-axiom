"""B338 -- the bridge flow (Attack C). Recorded SnapPy CS values; pure-python."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B338_the_bridge_flow'))
from the_bridge_flow import flow_from_symmetric_to_broken, law_holds, PARAMETER_IS_EXTERNAL


def test_flow_connects_symmetric_and_broken():
    assert flow_from_symmetric_to_broken()       # CS=0 at cusp (symmetric), !=0 for finite n (broken)


def test_chiral_order_parameter_law():
    assert law_holds()                           # CS(1,n) ~ -1/(2n)


def test_flow_parameter_is_external():
    assert PARAMETER_IS_EXTERNAL                  # the slope = the vacuum choice = physics (firewall)
