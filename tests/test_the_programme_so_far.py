"""P-514 (the owner, 2026-10-30): THE PROGRAMME SO FAR, the plain-words account of the programme. Every arc it cites has a
folder, every register row it cites exists, it states the count of derived parameters as the goal does, and it carries
no audit-room path. (Its GENESIS item IDs are checked by the genesis-cited gate.) A planted control shows the arc check
can fail."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs" / "THE_PROGRAMME_SO_FAR.md"


def _arcs(text):
    return sorted({int(m) for m in re.findall(r"(?<![A-Za-z:_/])B(\d{1,4})\b", text)})


def _missing(nums):
    have = {int(m.group(1)) for m in (re.match(r"B(\d+)", p.name) for p in (ROOT / "frontier").iterdir()) if m}
    return [n for n in nums if n not in have]


def test_every_cited_arc_has_a_folder():
    assert _missing(_arcs(PAGE.read_text(encoding="utf-8"))) == []


def test_the_arc_check_can_fail():
    assert _arcs("see B1812, sm:B1516 and B99999") == [1812] and _missing([1812, 9876]) == [9876]


def test_every_cited_register_row_exists():
    reg = {m for m in re.findall(r"^\| (P-\d{3}) \|", (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8"), re.M)}
    cited = set(re.findall(r"\bP-\d{3}\b", PAGE.read_text(encoding="utf-8")))
    assert cited and cited <= reg, sorted(cited - reg)


def test_it_states_the_goal_as_the_goal_does():
    goal = re.search(r"Its state is \*\*(\d+) of 19\*\*", (ROOT / "docs" / "MAIN_GOAL.md").read_text(encoding="utf-8")).group(1)
    t = PAGE.read_text(encoding="utf-8")
    assert "%s of 19" % goal in t and "audit/" not in t
