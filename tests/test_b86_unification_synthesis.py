"""B86 (Phase E, V69) -- locking test: the unification synthesis is internally consistent and the paper
skeleton exists with honest novelty labels. A documentation-integrity test (the underlying results are
locked by the V1-V68 tests this synthesis references)."""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b86_syn", _ROOT / "frontier" / "B86_unification_synthesis" / "probe.py")
B86 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B86)


def test_three_threads_present():
    assert len(B86.THREADS) == 3
    keys = " ".join(B86.THREADS)
    assert "tower" in keys and "A-polynomial" in keys and "degree=rank" in keys


def test_novelty_labels_honest():
    """SL(2)/SL(3) KNOWN; the A_n family / SL(4) and the methods APPARENTLY_NEW pending external check."""
    assert "KNOWN" in B86.NOVELTY["SL(2) Cooper-Long"]
    assert "KNOWN" in B86.NOVELTY["SL(3) Falbel M^3=L"]
    assert "APPARENTLY_NEW" in B86.NOVELTY["A_n family / SL(4) L=-M^4"]
    # no item is over-claimed as PROVED-novel
    assert all("PROVED_NEW" not in v for v in B86.NOVELTY.values())


def test_paper_skeleton_exists():
    skel = _ROOT / "papers" / "SLN_FIGURE_EIGHT_SKELETON.md"
    assert skel.exists()
    text = skel.read_text()
    # the skeleton carries proof-status and the physics-closed statement
    assert "PROVED from first principles" in text and "physics chapter is closed" in text
    assert "APPARENTLY_NEW" in text
