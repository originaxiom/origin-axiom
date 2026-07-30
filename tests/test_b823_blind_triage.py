"""B823 — locks the triage registry and, critically, that the gate CAN FAIL.

A gate that cannot fail is the defect `test-vacuity` exists to catch. These locks perturb the
registry three ways and require a failure each time.
"""
import importlib.util
import re
import shutil
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "docs" / "atlas" / "BLIND_ARCS.md"
_SPEC = importlib.util.spec_from_file_location("gates", ROOT / "scripts" / "gates" / "gates.py")
g = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(g)


@pytest.fixture
def registry(tmp_path):
    backup = tmp_path / "BLIND_ARCS.md"
    shutil.copy(REG, backup)
    yield REG
    shutil.copy(backup, REG)


def test_there_is_no_ceiling_any_more():
    """B822's threshold was self-referential; B823 removes it rather than tuning it."""
    assert not hasattr(g, "LEXICON_BLIND_CEILING"), (
        "the ceiling must be gone -- a threshold's only available response is to move it")


def test_the_gate_passes_and_names_the_open_gaps():
    ok, msg = g.gate_atlas_lexicon_current()
    assert ok, msg
    assert "all triaged" in msg
    assert "open GAP" in msg, "the gate must surface real gaps, not just report a clean pass"


def test_every_row_carries_a_reason():
    """A disposition with no reason is a label, not a judgement."""
    rows = re.findall(r"^\| `(B\d+)` \| \*?\*?(GAP|INSTRUMENT)\*?\*? \| (.+?) \|$",
                      REG.read_text(encoding="utf-8"), re.M)
    assert rows, "registry has no dispositioned rows"
    thin = [(a, why) for a, _, why in rows if len(why.strip()) < 30]
    assert not thin, f"rows with no substantive reason: {thin}"


def test_gate_FAILS_on_an_untriaged_arc(registry):
    s = registry.read_text(encoding="utf-8")
    registry.write_text(re.sub(r"^\| `B\d+` \| \*?\*?GAP.*$", "", s, count=1, flags=re.M),
                        encoding="utf-8")
    ok, msg = g.gate_atlas_lexicon_current()
    assert not ok and "NOT triaged" in msg


def test_gate_FAILS_on_a_stale_row(registry):
    """A registry that outlives its arcs stops being readable."""
    registry.write_text(registry.read_text(encoding="utf-8")
                        + "\n| `B999` | INSTRUMENT | a row for an arc that is not blind |\n",
                        encoding="utf-8")
    ok, msg = g.gate_atlas_lexicon_current()
    assert not ok and "no longer substantial-and-blind" in msg


def test_gate_FAILS_when_the_registry_is_missing(registry):
    registry.unlink()
    ok, msg = g.gate_atlas_lexicon_current()
    assert not ok and "MISSING" in msg
