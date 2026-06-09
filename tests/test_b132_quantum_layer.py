"""Locks for B132 -- the quantum layer (SU(2)_k field content, quantum selection criteria; CORRECTED by B133).

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


def test_field_content_not_chirality():
    # [CORRECTED B133] the field is word-composition (quantum-group), NOT chirality: ACHIRAL words alone span
    # all three fields, and achiral words vanish at k=4 -> neither field nor vanishing tracks chirality.
    c = B132.chirality_control()
    assert set(c["achiral_words_span_fields"]) == {"Q (rational)", "Q(sqrt-3)", "Q(zeta12)"}
    assert c["chirality_determines_field"] is False     # headline withdrawn
    assert c["achiral_words_vanishing_at_k4"]           # achiral words vanish at k=4 too
    assert c["vanishing_tracks_chirality"] is False


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


def test_vanishing_is_composition_not_chirality():
    # [CORRECTED B133] the S5 chiral-fragility reading is withdrawn: ACHIRAL words vanish at k=4 too.
    r = B132.vanishing_is_composition_not_chirality()
    assert r["achiral_words_vanishing_at_k4"]
    assert r["chirality_explains_vanishing"] is False


def test_lee_yang_galois():
    r = B132.lee_yang()
    assert r["is_phi"] and r["is_minus_inv_phi"]   # sigma_1 -> +phi (Fibonacci), sigma_3 -> -1/phi (Lee-Yang)
