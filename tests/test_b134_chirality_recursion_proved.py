"""Locks for B134 -- the chirality recursion PROVED (corollary of GHH 2008) + the reconciliations.

The elementary lemma (anti-palindromic word <=> block-seq cyclic palindrome) and the gluing-map reconciliation run
unconditionally; the SnapPy three-way agreement is guarded.
"""
import importlib.util
import pathlib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "b134_probe", _ROOT / "frontier/B134_chirality_recursion_proved/probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B134 = _load()


def test_lemma_anti_palindromic_iff_cyclic_palindrome():
    # the proof's combinatorial heart: holds for ALL block sequences (exhaustive) -> the string identity
    r = B134.lemma_exhaustive(max_len=6, max_entry=4)
    assert r["holds"] and r["checked"] > 5000


def test_word_criteria_spot():
    # GHH anti-palindromic vs B128 cyclic-palindrome agree on representative seqs
    assert B134.anti_palindromic(B134.seq_word((1, 2, 1))) and B134.seq_cyclic_palindrome((1, 2, 1))
    assert not B134.anti_palindromic(B134.seq_word((1, 2, 3))) and not B134.seq_cyclic_palindrome((1, 2, 3))


def test_gluing_map_dependence():
    # R2 reconciliation: swap (splice) gluing discretizes even a same-seed glue (Kitano-Nozaki)
    r = B134.gluing_map_dependence()
    assert r["identity_gluing_same_seed"] == "CONTINUUM"
    assert r["swap_discretizes_same_seed"] and r["swap_gluing_same_seed_finite_count"] == 16


def test_snappy_threeway_agreement():
    pytest.importorskip("snappy")
    s = B134.snappy_threeway()
    assert s is not None and s["all_agree"]   # GHH anti-pal == B128 cyc-pal == is_amphicheiral
