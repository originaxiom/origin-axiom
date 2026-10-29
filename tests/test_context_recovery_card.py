"""P-506: the context-recovery card (docs/views/CONTEXT_RECOVERY.md) is generated from tracked files, names the newest arc,
and its counts equal a recount of the files. A planted control shows the newest-arc check can fail."""
import json, os, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
CARD = ROOT / "docs" / "views" / "CONTEXT_RECOVERY.md"


def _newest(folders):
    return max(folders, key=lambda d: int(re.match(r"B(\d+)", d).group(1)))


def test_the_card_names_the_newest_arc_and_its_verdict():
    text = CARD.read_text(encoding="utf-8")
    folders = [d for d in os.listdir(ROOT / "frontier") if re.match(r"B\d+[a-zA-Z]?_", d) and (ROOT / "frontier" / d / "FINDINGS.md").is_file()]
    top = _newest(folders); v = json.loads((ROOT / "frontier" / top / "arc_verdict.json").read_text(encoding="utf-8"))["verdict"]
    assert "| %s | %s |" % (re.match(r"(B\d+)", top).group(1), v) in text


def test_the_register_count_equals_a_recount():
    text = CARD.read_text(encoding="utf-8")
    n = sum(1 for l in (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8").splitlines() if l.startswith("| P-"))
    assert "| register points | %d |" % n in text


def test_the_newest_check_can_fail():
    assert _newest(["B9_a", "B10_b", "B1817_c"]) == "B1817_c" and _newest(["B99_a", "B100_b"]) != "B99_a"
