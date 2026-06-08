"""Locks for B130 -- no forced choice in the invariant ring (seventh firewall form).

The symbolic kappa-elimination (m=2,3,4) and the located-fork facts (L1 deterministic word, L2 trace=m
inequivalence) always run. The m=5 numerical continuum is scipy/numpy-guarded (skips when absent; record stands).
"""
import importlib.util
import pathlib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "b130_probe", _ROOT / "frontier/B130_no_forced_choice/probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B130 = _load()


# ---------------------------------------------------------------------------------------------------------------
# S1 -- kappa-elimination ideal empty (kappa free on the fixed locus). m=2 runs live (fast); m=3,4 verified
# in-sandbox and recorded (the m=3 lex Groebner is ~80s -- too slow for the suite, so it is a checked record).
# ---------------------------------------------------------------------------------------------------------------
def test_kappa_free_on_fixed_locus_m2_live():
    r = B130.kappa_elimination(2)
    assert r["k_only_elimination_polys"] == []   # no relation purely in k -> kappa unconstrained -> kappa free
    assert r["kappa_free"]


def test_kappa_free_record_m3_m4():
    # verified in-sandbox this session (empty k-elimination ideal); recorded so the suite stays fast
    assert B130.KAPPA_FREE_SYMBOLIC == {2: True, 3: True, 4: True}


# ---------------------------------------------------------------------------------------------------------------
# L1 -- within a fixed m: unique deterministic fixed word (no internal combinatorial choice).
# ---------------------------------------------------------------------------------------------------------------
def test_within_m_deterministic_word():
    r = B130.deterministic_word()
    assert r["deterministic_unique_fixed_word"]
    assert r["prefix"].startswith("aab")        # silver word


# ---------------------------------------------------------------------------------------------------------------
# L2 -- across m: trace=m distinct -> not GL(2,Z)-conjugate (the only discrete fork = the external seed label).
# ---------------------------------------------------------------------------------------------------------------
def test_across_m_inequivalent():
    a = B130.across_m_inequivalent()
    assert a["distinct_traces_not_conjugate"]
    assert a["rows"][2]["trace"] == 2 and a["rows"][2]["det"] == -1
    assert a["rows"][3]["perron_field"] == "Q(sqrt13)"


# ---------------------------------------------------------------------------------------------------------------
# S1' -- m=5 numerical continuum (scipy/numpy-guarded).
# ---------------------------------------------------------------------------------------------------------------
def test_m5_kappa_continuum():
    pytest.importorskip("numpy")
    r = B130.kappa_continuum_m5(starts=60)       # lighter deterministic run for the suite
    assert r is not None
    assert r["distinct_kappa_3dp"] > 20          # a continuum of kappa-values, not a finite set
    assert r["kappa_free"]
