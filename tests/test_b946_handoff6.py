"""B946 locks — solo handoff 6 verified against this bench's own B941 data.

The point of these locks is that the convergence is INDEPENDENT: B941's
symmetric functions were computed here, before the handoff arrived.
"""
import json
import pathlib

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B946_solo_handoff6"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_all_four_solo_claims_verify():
    r = _res()
    assert r["RL2_line1_matches"] is True
    assert r["RL2_line2_matches"] is True
    assert r["RL2_line3_matches"] is True
    assert r["RL4_matches"] is True
    assert r["ALL_SOLO_CLAIMS_VERIFY"] is True


def test_the_norm_line_is_exactly_27():
    assert sp.Rational(_res()["e3_over_l4"]) == 27


def test_lambda_is_FORCED_not_assumed():
    """Solving e3/27 for lambda returns the tau-gauge value 2304/953."""
    r = _res()
    assert r["lambda_forced"] == "2304/953"
    assert r["lambda_is_2304_over_953"] is True


def test_the_thinning_law():
    """Residual primes thin with degree and vanish at the norm."""
    r = _res()
    assert r["residual_primes_degree1"] == [13, 421493]
    assert r["residual_primes_degree2"] == [17, 1129]
    assert r["residual_primes_degree3"] == []
    assert r["primes_thin_with_degree"] is True


def test_the_discriminant_is_honestly_NOT_953_free():
    """Solo flagged their own non-clean case; it must stay non-clean."""
    r = _res()
    assert r["RL4_is_953_free"] is False
    assert r["RL4_den_factors"].get("953") == 4


def test_the_convergence_with_b941_is_the_same_number():
    r = _res()
    assert r["b941_headline_numerator"] == 2**32 * 3**11 == 760840571584512
    assert r["equals_2p32_3p11"] is True
    assert r["e3_equals_27_lambda4"] is True


def test_the_adjudications_are_recorded():
    txt = " ".join((CELL / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "WITHDRAW. Concur." in txt                 # (a)
    assert "A new gate does not fix a skipping problem" in txt   # (b)
    assert "B892 stands" in txt                       # (c)
    # and the honest non-discharge
    assert "not verified here" in txt and "recorded as owed" in txt.lower()
