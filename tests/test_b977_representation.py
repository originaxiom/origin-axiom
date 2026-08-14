"""B977 locks — the representation sweep: the gate for rows never written."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts" / "checks"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import representation_sweep as rsw  # noqa: E402
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
TRIAGE = ROOT / "docs" / "REPRESENTATION_TRIAGE.md"


def test_the_corpus_is_fully_triaged():
    assert rsw.sweep() == []


def test_substantiality_is_claim_length_not_file_size():
    """File size would have caught 1 of 11; claim length catches 11 of 11."""
    assert rsw.CLAIM_FLOOR == 500
    assert contains(TRIAGE, "claim length, not file size", "1 of 11", "11 of 11")


def test_the_lost_cascade_block_would_now_be_caught():
    """Every arc B976 found missing is either cited or triaged."""
    subs = {i for i, _, _ in rsw.substantial_arcs()}
    for a in ("B861", "B869", "B870", "B872"):
        assert a in subs, f"{a} must be substantial by the claim-length test"
    assert rsw.sweep() == []


def test_the_pending_debt_is_itemised_not_hidden():
    t = TRIAGE.read_text(encoding="utf-8")
    assert t.count("| PENDING |") >= 12
    assert contains(TRIAGE, "13 arcs marked pending", "does not discharge it")


def test_the_three_dispositions_exist():
    t = TRIAGE.read_text(encoding="utf-8")
    for d in ("PENDING", "PROCESS", "SURFACE"):
        assert f"| {d} |" in t
