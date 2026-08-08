"""Locks MASTERPLAN v3 — the post-SM-verdict plan, registered before the handoff."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
MP = ROOT / "docs" / "STRUCTURE_TO_NATURE_MASTERPLAN.md"


def test_the_three_phases_are_registered():
    assert contains(MP, "phase a", "close out the sm surface",
                    "phase b", "the one live opening",
                    "phase c", "the new frontier")


def test_phase_A_leads_are_named():
    t = MP.read_text(encoding="utf-8")
    for lead in ("L134", "L132", "L137", "L135"):
        assert lead in t


def test_phase_C_opens_with_a_ledger_not_a_probe():
    """The B950 lesson, carried forward."""
    assert contains(MP, "opens with a specification ledger, not a probe",
                    "target it had never written down")


def test_the_handoff_clause_prevents_drift():
    assert contains(MP, "verified first", "folded in as a dated amendment",
                    "does not redirect it")


def test_scale_and_order_are_left_to_the_owner():
    assert contains(MP, "not launched without explicit authorization",
                    "open for the owner")
