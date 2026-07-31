"""B838 — locks the tested-and-declined re-grounding, and the diagnostic that decided it."""
import glob
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = glob.glob(str(ROOT / "frontier" / "*" / "FINDINGS.md"))


def _share(pattern):
    n = sum(1 for f in FILES
            if re.search(pattern, open(f, encoding="utf-8", errors="replace").read(), re.I))
    return n / len(FILES)


def test_the_forcing_vocabulary_is_AMBIENT():
    """41.9% -- worse than 'character variety' (13.8%), which failed B824's ceiling."""
    s = _share(r"\bforc(e|ed|es|ing)\b")
    assert s > 0.25, f"'forcing/forced' now at {s:.1%}; B838's ambient finding assumed >25%"


def test_the_K025_coinages_are_ABSENT_from_the_corpus():
    """A motif built from these would match nothing."""
    for pat in (r"\bheld[- ]?(open )?slot\b", r"\btwo ingredients\b"):
        s = _share(pat)
        assert s < 0.03, f"{pat} now at {s:.1%} -- if a coinage has spread, re-open R35-7"


def test_the_lexicon_was_NOT_regrounded_on_K023_K025():
    src = (ROOT / "scripts" / "atlas" / "atlas.py").read_text(encoding="utf-8")
    assert "K001..K022" in src, "the grounding note must still state what it is grounded in"
    for absent in ("held_slot", "forcing_map", "one_root"):
        assert absent not in src, f"a K023-K025 motif ({absent}) was added; B838 declined that"


def test_the_finding_states_the_reason_not_just_the_refusal():
    f = " ".join((ROOT / "frontier" / "B838_lexicon_regrounding"
                  / "FINDINGS.md").read_text(encoding="utf-8").split())
    assert "syntheses, not new topics" in f.lower() or "SYNTHESES, not new topics" in f
    assert "A synthesis does not add a topic" in f
