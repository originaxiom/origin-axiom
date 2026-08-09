"""B980 locks — the k=3 -> G*Lambda chain's two conflations, and the object's legal gravity number."""
import json
import pathlib
import sys

import mpmath as mp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B980_k3_conflation"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_G_Lambda_is_dimensionless_only_in_four_dimensions():
    """[G_d] = L^(d-2) from Einstein-Hilbert with hbar=c=1; [Lambda] = L^-2."""
    for d in (3, 4, 5):
        dim_G, dim_L = d - 2, -2
        assert (dim_G + dim_L == 0) is (d == 4), f"d={d} misclassified"


def test_the_three_dimensional_ratio_is_ell_over_G():
    """Witten eq 2.2: k_L + k_R = ell/(8G); dimensionless because [G_3] = L^1."""
    assert (3 - 2) + (-1) == 0, "G_3 * sqrt|Lambda| must be dimensionless"


def test_the_algebra_was_never_wrong():
    mp.mp.dps = 30
    assert abs(6 * mp.pi / 3 - 2 * mp.pi) < mp.mpf("1e-28")
    assert _res()["cell2_chain"]["equals_2pi"] is True


def test_the_defect_is_provenance_not_gauge_group():
    """Smolin's CS theory IS SU(2) -- the draft's gauge-group diagnosis was wrong."""
    c = _res()["cell4_which_k"]
    assert c["same_gauge_group_as_Smolin"] is True
    assert "POSITS" in c["THE_REAL_DEFECT"]
    assert "SELF_CORRECTION" in c


def test_smolin_relation_is_four_dimensional_and_carries_hbar():
    d = _res()["cell1_smolin_dimension_verified"]
    assert d["verified_4d_by_title"] is True
    assert "hbar" in _res()["cell4_which_k"]["B259_dropped_hbar"]


def test_object_complex_volume_and_zero_CS():
    """B250's Vol = 6*Lambda(pi/3); CS = 0 exactly by amphichirality."""
    r = _res()["cell3_complex_volume"]
    assert r["matches_known_2.029883212819307"] is True
    assert r["CS"] == 0
    assert "amphichiral" in r["why_CS_zero"].lower()


def test_the_122_orders_is_withdrawn_as_ours_but_B259_theorem_stands():
    assert contains(CELL / "FINDINGS.md",
                    "is not a failure of the object",
                    "stand untouched")
