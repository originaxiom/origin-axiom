"""Locks B872 -- the coset leg: 32 = 16 + 16bar on two legs."""
import json
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
_D = _ROOT / "frontier" / "B872_coset_leg"
RES = json.loads((_D / "results.json").read_text(encoding="utf-8"))
_F = " ".join((_D / "FINDINGS.md").read_text(encoding="utf-8").split()).lower().replace("*", "")


def test_overall_verdict():
    assert RES["coset_is_16_16bar"] is True
    assert RES["galois_consistent"] is True


def test_leg_a_exact_over_Z():
    a = RES["leg_a"]
    assert a["ok"] is True
    assert (a["d5_count"], a["plus_count"], a["minus_count"]) == (40, 16, 16)
    assert a["single_orbit_plus"] and a["single_orbit_minus"]
    assert a["spinor_fundamental_split"] is True


def test_leg_b_at_all_three_roots():
    assert len(RES["leg_b"]) == 3
    for r in RES["leg_b"]:
        assert r["verdict_16_16bar"] is True
        assert (r["kernel_dim"], r["center_dim"]) == (46, 1)
        assert (r["plus_dim"], r["minus_dim"]) == (16, 16)
        assert (r["commutant_plus"], r["commutant_minus"]) == (1, 1)
        assert r["Bpm_rank"] == 16


def test_the_charge_splits_real_and_the_correction_is_recorded():
    """q^2 > 0 at every root: a split-torus direction, as the split form e6(6)
    requires. The earlier compact-u(1) draft claim was a wrong-stratum artifact;
    the lock that caught it is this one's ancestor."""
    assert all(r["q2_sign"] == 1 for r in RES["leg_b"])
    assert "split real form e6(6)" in _F.replace("**", "")
    assert "layer-8" in _F and "not probed by this arc" in _F


def test_findings_scope_and_the_two_readings():
    assert "the labels are a charge-sign convention" in _F
    assert "the deciding computation" in _F
    assert "two compatible readings" in _F


def test_normalization_certificate_is_in_the_arc():
    src = (_D / "cubic_modp_check.py").read_text(encoding="utf-8")
    assert "banked(t/13)" in src and "13 x banked roots" in src.replace("×", "x")
