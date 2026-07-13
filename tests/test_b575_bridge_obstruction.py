"""B575 / L51 — the bridge obstruction: the lock.

Re-runs the ENTIRE exact build (e6 in gl(27) from the minuscule model, the
principal holonomy, per-block Fox cohomology, the cup product with the true e6
bracket). Every stage gate is a module-level assert — executing the module IS
the verification chain (G1 closure=78, G2 blocks, G3 relator=identity,
G4 H1=H2=1 x6, G5 the m=1 control). This test then locks the verdict:

    Q == 0 identically on H^1 — all 6 diagonal and all 15 cross components.

Runtime ~6 min (exact Q(sqrt(-3)) arithmetic end to end). This is the decisive
lock of the arc; the cost is accepted deliberately.
See frontier/B575_bridge_obstruction/FINDINGS.md.
"""
import importlib.util
import os
import sys


def test_bridge_obstruction_vanishes_identically():
    path = os.path.join(os.path.dirname(__file__), "..",
                        "frontier", "B575_bridge_obstruction", "l51_obstruction.py")
    spec = importlib.util.spec_from_file_location("l51mod", path)
    mod = importlib.util.module_from_spec(spec)
    argv = sys.argv
    sys.argv = [path]                      # run WITHOUT the verify pass (locks the core)
    try:
        spec.loader.exec_module(mod)       # gates G1-G5 are module-level asserts
    finally:
        sys.argv = argv
    # the verdict: Q identically zero — every diagonal and cross component
    assert set(mod.QDIAG.keys()) == {1, 4, 5, 7, 8, 11}
    for m, comps in mod.QDIAG.items():
        assert all(v.is_zero() for v in comps.values()), f"Q(u_{m}) != 0"
    assert len(mod.CROSS) == 15
    for pair, comps in mod.CROSS.items():
        assert all(v.is_zero() for v in comps.values()), f"B{pair} != 0"
