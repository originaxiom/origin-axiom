"""B960 locks — the adjoint hatch closes itself."""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B960_l136_adjoint"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_the_27_is_not_a_rep_of_the_adjoint_form():
    r = _res()
    assert r["cartan_det"] == 3
    assert r["the_27_highest_weight_in_root_lattice"] is False
    assert r["centre_acts_nontrivially_on_27"] is True
    assert r["adjoint_form_has_a_27"] is False


def test_the_adjoint_type_weights_are_the_integral_ones():
    w = _res()["fundamental_weights_in_root_lattice"]
    assert w["omega_2"] is True and w["omega_4"] is True
    assert w["omega_1"] is False and w["omega_6"] is False


def test_the_hatch_closes_itself():
    r = _res()
    assert "closes itself" in r["verdict"]
    assert "costs the 27" in r["reason"]
    assert "complete" in r["consequence"]


def test_the_scope_is_not_overstated():
    """It must not be read as 'the object cannot reach the SM'."""
    assert contains(CELL / "FINDINGS.md",
                    "does not say the object cannot reach the SM",
                    "remains unexcluded",
                    "the class is",
                    "open-and-shut reading")
