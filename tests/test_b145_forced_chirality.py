"""B145 -- can chirality be forced? Combinatorial (self-mirror) core unconditional; catalog SnapPy/Sage-gated."""
import pytest

from frontier.B145_forced_chirality.probe import (
    analyze,
    catalog,
    enumerate_words,
    metallic_all_self_mirror,
    simplest_substitution_self_mirror,
)


def test_metallic_family_is_self_mirror():
    """The canonical metallic family R^mL^m is entirely self-mirror (amphichiral); genuinely chiral words are not."""
    mm = metallic_all_self_mirror()
    assert mm["all_metallic_self_mirror"] is True
    assert mm["none_chiral_self_mirror"] is True


def test_simplest_substitution_self_mirror():
    """The simplest/forced substitution (Fibonacci -> monodromy RL) is self-mirror."""
    assert simplest_substitution_self_mirror()["RL_self_mirror"] is True


def test_enumeration_sane():
    """The o-p-t word enumerator returns cyclic-primitive two-letter words (figure-eight RL present as 'LR')."""
    ws = enumerate_words(5)
    assert "LR" in ws                                  # cyclic rep of RL (the figure-eight)
    assert all(("R" in w and "L" in w) for w in ws)


def test_catalog_canonicity_is_self_mirror():
    """Decisive: GHH==SnapPy on the catalog; minimal-volume bundle amphichiral; all quadratic-trace-field bundles amphichiral."""
    pytest.importorskip("snappy")
    a = analyze(catalog(maxlen=6))
    if "skipped" in a:
        pytest.skip("snappy unavailable")
    assert a["ghh_vs_snappy_match"] is True
    assert a["min_volume_is_amphichiral"] is True
    assert a["quadratic_bundles_all_amphichiral"] is True
