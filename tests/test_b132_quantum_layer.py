"""Locks for B132 -- the quantum layer (eigenvalue field-fusion, chirality-arithmetic, quantum selection criteria).

All checks use the validated SU(2)_k modular rep (framing=False, R=T, L=STS^-1); the eigenvalue-order method is exact
and precision-independent, so these run unconditionally (numpy only).
"""
import importlib.util
import pathlib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "b132_probe", _ROOT / "frontier/B132_quantum_layer/probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B132 = _load()


def test_field_fusion_m_mod_4():
    r = B132.field_fusion()
    # m=2,6 (m ≡ 2 mod 4) carry Q(i) content -> fused; others pure Q(sqrt-3)
    assert r[1]["field"] == "Q(sqrt-3)" and not r[1]["fused"]
    assert r[2]["fused"] and r[6]["fused"]
    assert all(not r[m]["fused"] for m in (1, 3, 4, 5, 7))


def test_chirality_arithmetic_connection():
    rows = {x["label"]: x for x in B132.chirality_arithmetic()}
    # same-seed / achiral -> Q(sqrt-3); cross-seed / chiral -> Q(zeta12) and vanish
    assert rows["fig8xfig8 (same)"]["field"] == "Q(sqrt-3)"
    assert rows["silverxsilver (same)"]["field"] == "Q(sqrt-3)"   # DEFUSED
    assert rows["(1,2,1) achiral"]["field"] == "Q(sqrt-3)"
    assert rows["fig8xsilver (cross)"]["field"] == "Q(zeta12)" and rows["fig8xsilver (cross)"]["absZ"] == 0.0
    assert rows["(1,2,3) chiral"]["field"] == "Q(zeta12)" and rows["(1,2,3) chiral"]["absZ"] == 0.0


def test_self_referential_loop_Z_eq_omega():
    assert B132.self_referential_loop()["equals_omega"]


def test_pure_phase_m1_unique():
    r = B132.pure_phase()
    assert r[1]["all_unit_modulus"]
    assert not any(r[m]["all_unit_modulus"] for m in (2, 3, 4))


def test_vanishing_period_unit_group():
    v = B132.vanishing_period()
    assert v["m1_period3_eq_6over2"]    # Q(sqrt-3): |O^x|/2 = 6/2 = 3
    assert v["m2_period2_eq_4over2"]    # Q(i):      |O^x|/2 = 4/2 = 2
    assert v["nonarith_irregular"]      # m=3,4 aperiodic


def test_two_scales_by_m_mod_4():
    assert B132.two_scales()["two_scales_by_m_mod_4"]


def test_chiral_fragility():
    r = B132.chiral_fragility()
    assert r["chiral_vanishes_at_k4"]
    assert r["chiral_more_fragile"]


def test_lee_yang_galois():
    r = B132.lee_yang()
    assert r["is_phi"] and r["is_minus_inv_phi"]   # sigma_1 -> +phi (Fibonacci), sigma_3 -> -1/phi (Lee-Yang)
