"""B1710 -- W121's index law on main (P-255). Stored: the exponents and sums; the law -15 chi, -18 chi with the genus
cancelling; K3's degrees and indices; never +-3. Live: the Riemann-Roch arithmetic from the stored exponents."""
import json, pathlib
from fractions import Fraction as Fr
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1710_w121s_index_law_on_main" / "verification"


def test_stored():
    d = json.loads((A / "the_index_law.json").read_text(encoding="utf-8"))
    assert d["exponents_rho_T"] == ["1/8", "3/8", "7/8"] and d["exponents_conj"] == ["1/8", "5/8", "7/8"]
    assert d["law_is_-15chi_and_-18chi"] and d["never_pm3"] and all(v["genus_cancels"] for v in d["law"].values())
    assert d["K3"] == {"canonical_extension_degree_rho_T": "-33", "canonical_extension_degree_conj": "-39", "index_rho_T": "-30", "index_conj": "-36"}


def test_live_arithmetic():
    d = json.loads((A / "the_index_law.json").read_text(encoding="utf-8"))
    for key, slope in (("exponents_rho_T", -15), ("exponents_conj", -18)):
        smu = sum(Fr(x) for x in d[key])
        for chi in range(1, 7):
            for g in range(4):
                assert 3 * Fr(2 * g - 2 + chi, 2) - 12 * chi * smu + 3 * (1 - g) == slope * chi
