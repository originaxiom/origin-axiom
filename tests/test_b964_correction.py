"""B964 locks — the two VEV corrections, and the terminological rule that prevents them."""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B964_vev_correction"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_the_adjoint_contains_a_24_so_the_route_does_not_stop_short():
    r = _res()["error_1"]
    assert "78" in r["what_was_wrong"] and "24" in r["what_was_wrong"]
    assert "scope error" in r["severity"]


def test_adjoint_VEV_and_centralizer_are_the_same_operation():
    """The substantive correction."""
    r = _res()["error_2"]
    assert "SAME OPERATION" in r["what_was_wrong"]
    assert "substantive" in r["severity"]
    p = _res()["the_corrected_picture"]
    assert "rank-PRESERVING" in p["object_supplies"]
    assert "rank-REDUCING" in p["object_lacks"]


def test_the_rank_obstruction_is_untouched():
    p = _res()["the_corrected_picture"]
    assert "UNCHANGED" in p["why_B952_still_stands"]


def test_what_is_withdrawn_is_listed_explicitly():
    r = _res()
    assert len(r["what_is_withdrawn"]) == 2
    assert any("does not supply a VEV" in w for w in r["what_is_withdrawn"])
    assert len(r["what_survives_of_B962"]) >= 5


def test_the_terminological_rule_is_stated():
    # NB: keep probes SHORT and punctuation-free -- long phrases break on quotes,
    # periods inside quotes, and em-dashes. Fifth such slip on 2026-08-08.
    assert contains(CELL / "FINDINGS.md",
                    "as meaning",
                    "27 vev",
                    "say which",
                    "every time",
                    "adjoint higgs mechanism")
