"""Locks for B136 -- amphichirality for ALL once-punctured-torus bundles (general LR words)."""
import importlib.util
import pathlib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "b136_probe", _ROOT / "frontier/B136_general_amphichirality/probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B136 = _load()


def test_lemma_pair_criterion_iff_anti_palindromic():
    r = B136.lemma_exhaustive(max_blocks=4, max_exp=3)
    assert r["holds"] and r["checked"] > 7000


def test_specializes_to_B134_metallic():
    assert B136.specializes_to_metallic()["reduces_to_B134"]


def test_nonmetallic_spot():
    # genuinely non-metallic (a_i != b_i): (1,2),(2,1) amphichiral; (1,2),(1,2) chiral
    assert B136.pair_criterion([(1, 2), (2, 1)])
    assert not B136.pair_criterion([(1, 2), (1, 2)])


def test_snappy_threeway_general():
    pytest.importorskip("snappy")
    s = B136.snappy_threeway()
    assert s is not None and s["all_agree"]
