"""B822 — locks the size-floored lexicon gate and the removal of its unsupported verdict."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location("gates", ROOT / "scripts" / "gates" / "gates.py")
g = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(g)


def test_the_metric_is_size_floored():
    assert g.LEXICON_MIN_BYTES == 2000
    # 9, not 8: writing B822's own findings file broke the ceiling it had just set, because the
    # arc documenting the gate is itself a substantial instrument arc. The self-reference is the
    # point -- see B823, which removes the threshold entirely.
    assert g.LEXICON_BLIND_CEILING == 9


def test_the_gate_passes_and_reports_the_split():
    ok, msg = g.gate_atlas_lexicon_current()
    assert ok, msg
    assert "thin arcs excluded" in msg, "the gate must report what it excluded, not hide it"


def test_the_gate_no_longer_asserts_ROTTING():
    """B821 showed count-plus-rate cannot support that inference. The gate must not print it."""
    src = (ROOT / "scripts" / "gates" / "gates.py").read_text(encoding="utf-8")
    fn = src[src.index("def gate_atlas_lexicon_current"):src.index("GATES = {")]
    assert "ROTTING" not in fn, "the gate must report composition, not conclude a diagnosis"
    assert "OBJECT lexicon should" in fn, "it should hand the judgement to the reader explicitly"


def test_instrument_arcs_are_still_counted():
    """Excluding by topic would let the number be tuned by relabelling. Size is objective."""
    fn = (ROOT / "scripts" / "gates" / "gates.py").read_text(encoding="utf-8")
    assert "Instrument arcs are deliberately still COUNTED" in fn
