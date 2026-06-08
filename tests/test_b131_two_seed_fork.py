"""Locks for B131 -- two-seed gluing creates an internal discrete fork (S032-B).

The exact (1,2) fork, the same-seed continuum, and irreducibility run unconditionally (sympy). The matrix
re-derivation of the A-poly relations is numpy-guarded.
"""
import importlib.util
import pathlib

import pytest
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "b131_probe", _ROOT / "frontier/B131_two_seed_fork/probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B131 = _load()


def test_same_seed_is_continuum():
    # gluing a seed to itself = same A-poly curve -> kappa free (no fork)
    assert B131.fork(1, 1) == "CONTINUUM"
    assert B131.fork(2, 2) == "CONTINUUM"


def test_distinct_seeds_make_discrete_fork():
    f = B131.fork(1, 2)
    assert f != "CONTINUUM"
    assert set(f) == {-4, -2}            # exact (1,2) fork


def test_fork_points_irreducible():
    # all matched kappa != 2 -> all irreducible reps (reducible <=> tr[A,B]=2)
    assert B131.fork_is_irreducible(B131.fork(1, 2))


def test_apoly_relations_validated_values():
    t = sp.Symbol("t")
    assert sp.expand(B131.apoly_relation(1) - (t**4 - 5*t**2 + 2)) == 0   # B67
    assert sp.expand(B131.apoly_relation(2) - (t**2 - 6)) == 0            # B69/V33


def test_apoly_from_matrices_matches():
    pytest.importorskip("numpy")
    for m in (1, 2):
        r = B131.verify_apoly_from_matrices(m, samples=40)
        assert r is not None and r["matches_exact_relation"]   # rederived kappa=P_m(trT) from SL(2,C) matrices
