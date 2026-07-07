"""Lock for B452 — the Ethogram E0: the typed gates validate (fire AND fail)."""
import os
import sys

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B452_ethogram_dictionary")
sys.path.insert(0, HERE)


def test_ez_gates_validate():
    import ez_dryrun
    assert ez_dryrun.run()


def test_registry_frozen_shape():
    import registry
    assert len(registry.NUMERIC_TARGETS) == 20
    assert registry.P_BINDING == 0.01
    assert registry.NULL_DRAWS == 2000
    s = registry.structural_joint([], [])
    assert s["can_fire_alone"] is False
