"""B976 locks — the cascade recovery. These pin the corrections so they cannot silently revert."""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B976_cascade_recovery"
VERDICT = ROOT / "docs" / "THE_SM_VERDICT.md"
LEDGER = ROOT / "docs" / "SM_SPECIFICATION_LEDGER.md"


def _res():
    return json.loads((CELL / "results.json").read_text(encoding="utf-8"))


def test_the_loss_was_quantified_not_asserted():
    r = _res()
    assert r["arcs_in_range"] == 60
    assert r["uncited_on_any_surface"] >= 35
    assert r["cascade_arcs_cited_on_any_surface"] <= 2


def test_hypercharge_is_now_recorded_as_DERIVED():
    """B864 derived it on 2026-08-03; the ledger called it OPEN today."""
    t = LEDGER.read_text(encoding="utf-8")
    assert "DERIVED (B864" in t
    assert "forcing b = c = 0 exactly" in t
    assert "OPEN — the sharpest available target" not in t


def test_the_normalisation_limit_is_kept():
    """The direction is derived; the normalisation is not and cannot be."""
    assert contains(LEDGER, "the direction is derived", "normalisation is not")


def test_the_verdict_carries_the_cascade_rows():
    t = VERDICT.read_text(encoding="utf-8")
    for arc in ("B862", "B863", "B864", "B873"):
        assert arc in t, f"{arc} missing from the SM verdict"
    assert "TERMINATION THEOREM" in t


def test_the_verdict_declares_its_own_amendment():
    assert contains(VERDICT, "amended 2026-08-08", "written without the b860s",
                    "the synthesis layer", "forgot them")


def test_causation_is_not_claimed():
    r = _res()
    c = r["ON_CAUSATION"].lower()
    assert "cannot verify that the model switch caused this" in c
    assert "correlation is not causation and is not claimed" in c


def test_the_repo_lost_nothing_is_stated():
    r = _res()
    assert "lost NOTHING" in r["WHAT_WAS_NOT_LOST"]
