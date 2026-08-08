"""B967 locks — the retraction sweep, and the instance it found at its source."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts" / "checks"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import retraction_sweep as rs  # noqa: E402
from _prose import contains  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
CELL = ROOT / "frontier" / "B967_retraction_sweep"


def test_the_registry_has_entries_and_the_corpus_is_clean():
    assert len(rs._phrases()) >= 5
    assert len(rs._tracked_md()) > 2000
    assert rs.sweep() == []


def test_B962_now_carries_its_correction_at_the_source():
    """The instance the sweep found: the retraction had never reached B962."""
    t = (ROOT / "frontier" / "B962_vev_scout" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "PARTIALLY RETRACTED BY B964" in t
    assert "Original title asserted two claims" in t
    # and the body is marked inline, not only at the top
    assert t.count("⚠") >= 3


def test_the_registry_records_what_is_deliberately_NOT_registered():
    t = (ROOT / "docs" / "RETRACTED_PHRASES.md").read_text(encoding="utf-8")
    assert "Deliberately NOT registered" in t
    assert "correction banner" in t or "banner" in t


def test_the_limits_are_stated_not_hidden():
    assert contains(CELL / "FINDINGS.md",
                    "phrase-exact", "paraphrase", "registration is manual",
                    "neither removes the need to read")
