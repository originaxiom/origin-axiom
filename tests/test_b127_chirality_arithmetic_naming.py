"""Locks for B127 -- chirality, Fibonacci, arithmetic, and the object's proper name.

Pure-math facts always run (M-1, M-3, M-4, Fricke-Vogt dictionary, central charges, null scale). The CS=0 achiral
locus is SnapPy-guarded (skips when SnapPy is absent; the record stands).
"""
import importlib.util
import pathlib

import pytest

_ROOT = pathlib.Path(__file__).resolve().parents[1]


def _load():
    spec = importlib.util.spec_from_file_location(
        "b127_probe", _ROOT / "frontier/B127_chirality_arithmetic_naming/probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


B127 = _load()


def test_fibonacci_fusion_is_substitution():
    r = B127.fibonacci_fusion_is_substitution()
    assert r["same_char_poly_L2_minus_L_minus_1"] and r["perron_is_phi"]


def test_anyon_only_golden():
    r = B127.anyon_only_golden()
    assert r["only_m1_below_2"]   # lambda_m < 2 (quantum-dimension range) only for m=1


def test_arithmetic_trichotomy_disjoint():
    r = B127.arithmetic_trichotomy()
    assert r["zeta3_cap_zeta5_is_Q"]
    # fusion field is real-quadratic, manifold field imaginary/higher -> different fields
    assert r["rows"][0] == (1, "Q(sqrt5)", "Q(sqrt-3)")


def test_fricke_vogt_dictionary():
    r = B127.fricke_vogt_dictionary()
    assert r["void_hyperbolic"] and r["elliptic_point_neutral"]


def test_central_charges_two_categorifications():
    r = B127.central_charges()
    assert r["yang_lee_is_minus_22_5"]   # Yang-Lee non-unitary c = -22/5 (vs unitary Fibonacci +14/5)


def test_no_forced_scale():
    assert not B127.no_forced_scale()["any_ratio_within_1pct_of_a_constant"]


def test_cs_achiral_locus_if_snappy():
    pytest.importorskip("snappy")
    r = B127.cs_achiral_locus(mmax=4)
    assert r is not None
    assert r["metallic_all_CS_zero"]    # metallic bundles are the CS=0 achiral locus
    assert r["census_is_a_mix"]         # the test discriminates (m003 CS != 0, m004 CS = 0)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
