"""B142 -- Item A Klein-4 (unconditional); Item B cartography (snappy-gated; trace fields sage-gated)."""
import pytest

from frontier.B142_klein4_and_magic_cartography.probe import (
    factual_correction,
    klein4_lemma_symbolic,
    klein4_numeric,
    sl3_ptolemy_object,
    thurston_dimension,
    trace_fields_sage,
)


def test_klein4_lemma_symbolic():
    """Item A: the principal stratum is rigorously reducible (involution => Klein-4 => reducible)."""
    s = klein4_lemma_symbolic()
    assert s["all_ok"] is True
    assert s["checks"]["(AB)^2=I"] and s["checks"]["AB=BA (commute)"]


def test_klein4_numeric_all_commute():
    """Item A reconfirm: every converged phi-fixed solution at A=diag(1,-1,-1) has B^2=I, (AB)^2=I, AB=BA."""
    n = klein4_numeric(starts=20, seed=20260609)
    assert n["converged"] > 0
    assert n["all_klein4"] is True


def test_factual_correction_s776_not_borromean():
    """Item B.1: s776 (magic manifold) is NOT the Borromean rings (L6a4)."""
    pytest.importorskip("snappy")
    fc = factual_correction()
    assert fc["is_isometric"] is False
    assert fc["s776"]["cusps"] == 3 and fc["L6a4_borromean"]["cusps"] == 3
    assert abs(fc["s776"]["vol"] - 5.33349) < 1e-3
    assert abs(fc["L6a4_borromean"]["vol"] - 7.32772) < 1e-3
    assert any("6^3_1" in x for x in fc["s776"]["identify"])


def test_thurston_dim_is_cusps_generic():
    """Item B.2 (MB8 null control): every 3-cusped M has SL(2,C) geometric dim = #cusps = 3, regardless of symmetry."""
    pytest.importorskip("snappy")
    td = thurston_dimension()
    for name in ("s776", "L6a4", "L8a19", "L8a20"):
        assert td[name]["cusps"] == 3
        assert td[name]["sl2c_geom_dim_=_cusps_(Thurston)"] == 3


def test_sl3_ptolemy_is_the_right_object():
    """Item B: the SU(3) venue is SL(3,C) (T_3[M]); s776's SL(3,C) geometric component is dim 6, not 'dim 2'."""
    pytest.importorskip("snappy")
    r = sl3_ptolemy_object()
    if "skipped" in r:
        pytest.skip(r["skipped"])
    assert r["sl3_geom_component_dim_expected"] == 6
    assert r["sl3_ptolemy_obstruction_classes"] > 0


def test_trace_fields_sage():
    """Item B (sage-gated): s776 -> Q(sqrt-7), L6a4 -> Q(i), 4_1 -> Q(sqrt-3) (s776 outside the forced chain)."""
    pytest.importorskip("sage.all")
    tf = trace_fields_sage()
    assert tf["s776"] == "x^2 - x + 2"      # disc -7 -> Q(sqrt-7)
    assert tf["L6a4"] == "x^2 + 1"          # Q(i)
    assert tf["4_1"] == "x^2 - x + 1"       # Q(sqrt-3) -- the forced field
