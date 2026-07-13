"""B576 / L59 — the deformed closure: the lock.

Executes l59_closure.py, which transitively re-runs the entire B575 exact build
(all gates as asserts) and then computes the channel table. Locks:
  - all six forcing channels NONZERO ([V8,V8]->V10,V14; [V8,V10]->V16;
    [V8,V16]->V22; [V16,V16]->V10; [V16,V10]->V8);
  - the theta-parity gate ([V10,V14] has no odd components — asserted in-module);
  - both forcing flags True: theta-odd activation forces full e6.
Runtime ~6.5 min (the decisive locks of the arc; cost accepted deliberately).
See frontier/B576_deformed_closure/FINDINGS.md.
"""
import importlib.util
import os
import sys

import pytest


@pytest.mark.skipif(os.environ.get('OA_SLOW') != '1',
                    reason='full exact e6 build ~6 min; run with OA_SLOW=1 (the B352 house pattern; reviews run slow-tier on)')
def test_theta_odd_motion_forces_full_e6():
    path = os.path.join(os.path.dirname(__file__), "..",
                        "frontier", "B576_deformed_closure", "l59_closure.py")
    spec = importlib.util.spec_from_file_location("l59mod", path)
    mod = importlib.util.module_from_spec(spec)
    argv = sys.argv
    sys.argv = [path]
    try:
        spec.loader.exec_module(mod)       # B575 gates + the parity assert fire in-module
    finally:
        sys.argv = argv
    assert mod.CH == {(4, 4, 5): True, (4, 4, 7): True, (4, 5, 8): True,
                      (4, 8, 11): True, (8, 8, 5): True, (8, 5, 4): True}
    assert mod.force4 and mod.force8
