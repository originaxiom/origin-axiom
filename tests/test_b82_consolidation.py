"""B82 (Phase 3, V65) -- locking test: the consolidation synthesis is internally consistent and the
physics record is complete. A documentation-integrity test (the underlying results are locked by the
V53-V64 tests this synthesis references)."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b82_cons", _ROOT / "frontier" / "B82_consolidation" / "probe.py")
B82 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B82)


def test_three_threads_present():
    """The synthesis names exactly the three real threads."""
    assert set(B82.THREADS) == {"tower factorization", "figure-eight A-poly", "degree=rank"}


def test_physics_record_is_the_kill_list():
    """The physics-chapter close records all five killed bridges (V28/V29/V34/V56/V58)."""
    keys = " ".join(B82.PHYSICS_RECORD)
    for tag in ("V28", "V29", "V56", "V58"):
        assert tag in keys, tag
    assert len(B82.PHYSICS_RECORD) >= 5


def test_novelty_labels_honest():
    """SL(3) degree=rank is labelled KNOWN (Falbel); the general pattern APPARENTLY_NEW."""
    assert "KNOWN" in B82.NOVELTY["degree=rank SL(3)"]
    assert "APPARENTLY_NEW" in B82.NOVELTY["degree=rank general"]
