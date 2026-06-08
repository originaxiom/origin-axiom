"""Locks for B128 -- the symmetry-breaking landscape: chirality recursion, order parameter, torsion firewall.

Pure-combinatorics facts (the recursion rule, the balanced-count M-B, the torsion records, K-F) always run. The live
SnapPy recomputations (method bug, 15/15 recursion, CS mirror negation, torsion table) are SnapPy-guarded and skip
when SnapPy is absent (the records stand).
"""
import importlib.util
import pathlib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "b128_probe", _ROOT / "frontier/B128_symmetry_breaking_chirality/probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B128 = _load()


# ---------------------------------------------------------------------------------------------------------------
# Pure-combinatorics (no SnapPy) -- always run.
# ---------------------------------------------------------------------------------------------------------------
def test_recursion_rule_matches_15_labels():
    r = B128.recursion_combinatorics()
    assert r["rule_matches_15_labels"]
    assert r["every_double_is_achiral"]


def test_recursion_rule_is_reversal_equals_cyclic_rotation():
    # spot-checks of the rule itself: doubles & palindromes achiral, distinct-block triples chiral
    assert B128.seq_is_amphichiral((1, 2))            # double
    assert B128.seq_is_amphichiral((2, 1, 3, 1))      # reversal (1,3,1,2) is a rotation
    assert B128.seq_is_amphichiral((1, 1, 2, 2))      # reversal (2,2,1,1) is a rotation
    assert not B128.seq_is_amphichiral((1, 2, 3))     # reversal (3,2,1) not a rotation
    assert not B128.seq_is_amphichiral((1, 2, 2, 3))  # reversal (3,2,2,1) not a rotation


def test_order_parameter_is_ordering_not_count():
    r = B128.order_parameter_counts()
    assert r["all_balanced_imbalance_zero"]   # the three chiral triples are #R=#L balanced
    assert r["balanced_yet_chiral"]           # ... yet chiral -> the count is not the order parameter


def test_torsion_does_not_track_chirality():
    r = B128.torsion_does_not_track_chirality()
    # single torsion appears in BOTH an achiral double and the chiral (1,2,3) -> torsion != chirality
    assert r["single_torsion_is_both_achiral_and_chiral"]


def test_kf_records_single_vs_doubled():
    # K-F empirical spine: achiral doubles single-torsion, periodic doubled, chiral (1,2,3) single
    t = B128.TORSION_TABLE
    assert t["RLRRLL"][0].count("Z/") == 1 and t["RLRRLL"][1] is True       # single, achiral
    assert t["RLRLRL"][0].count("Z/") == 2 and t["RLRLRL"][1] is True       # doubled, periodic achiral
    assert t["RLRRLLRRRLLL"][0].count("Z/") == 1 and t["RLRRLLRRRLLL"][1] is False  # single, CHIRAL


# ---------------------------------------------------------------------------------------------------------------
# Live SnapPy recomputations -- skip cleanly when SnapPy is absent.
# ---------------------------------------------------------------------------------------------------------------
def test_method_bug_live():
    pytest.importorskip("snappy")
    r = B128.method_bug_live()
    assert r["is_amphicheiral_correct"]        # is_amphicheiral matches all controls
    assert r["naive_gives_false_positives"]    # naive isometry false-positives on the chiral controls


def test_recursion_15_of_15_live():
    pytest.importorskip("snappy")
    r = B128.recursion_live()
    assert r["all_match"] and r["matched"] == 15


def test_cs_mirror_negation_live():
    pytest.importorskip("snappy")
    r = B128.cs_mirror_live()
    assert r["all_negate_to_machine_zero"]


def test_torsion_table_live():
    pytest.importorskip("snappy")
    r = B128.torsion_live()
    assert r["matches_record"]
