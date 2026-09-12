"""B1339 - the chain status is adopted, current, and joined to the queue.

Four consolidations answered "what don't we have on the chain" and none was on main; each was
ADDED, never ADOPTED, which is the mechanism B1338 identified behind the rediscovery loop. These
assert the adoption holds: the status lives on main, it carries the currency correction that its
own source lacked, and the gates the record says are where values could cross are in the queue.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATUS = ROOT / "docs" / "THE_CHAIN_STATUS.md"
QUEUE = ROOT / "docs" / "SPECIALIST_SEND_QUEUE.md"


def test_status_of_record_exists_on_main():
    assert STATUS.exists(), "the chain status of record is not on main -- adoption undone"


def test_it_supersedes_rather_than_joins():
    t = STATUS.read_text(encoding="utf-8")
    assert "supersedes" in t.lower(), "a consolidation that does not supersede is a fifth taxonomy"
    for src in ("THE_CHAIN_GAP", "THE_TOE_GAP", "THE_FULL_ACCOUNTING", "THE_GRAND_TABLE"):
        assert src in t, f"{src} is not demoted to a source"


def test_it_carries_the_currency_correction_its_source_lacked():
    """memo 152 recommends gate C as the door for generations; gate C closed the same day it was
    banked. An adopted status that repeats that is not adopted, it is copied."""
    t = STATUS.read_text(encoding="utf-8")
    assert "CLOSED 2026-08-30" in t, "gate C's closure is not carried"
    assert "OA-C0009" in t, "the relocated address of the generation question is not carried"


def test_the_gates_reached_the_queue():
    """memo 152's measured defect: four gates plus a hatch, none in the queue. Gate C is
    excluded on purpose -- it is closed."""
    q = QUEUE.read_text(encoding="utf-8")
    assert "Gate B" in q, "the CRUX is still not in the specialist queue"
    assert "Gate D" in q, "the non-Hermitian gate is still not in the specialist queue"
    assert "Route A" in q, "the hatch is still not in the specialist queue"
    assert "DRAFTED, NOT SENT" in q, "the send fence must stay explicit"
