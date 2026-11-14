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


# --- 2026-11-13 (main's M25, answer 3; C14, patch 8): the short living page, a draft for one cold reading ---

SHORT = ROOT / "docs" / "THE_PROGRAMME_IN_SHORT.md"


def _short_problems(text, full):
    """what is wrong with the short page: a path it names that does not exist; a section of the full account it names
    that the full account does not have; a line of a list with no source in brackets; the goal's count not as the goal
    states it"""
    bad = []
    for p in re.findall(r"`([\w./-]+\.md)`", text):
        if not ((ROOT / p).exists() or (ROOT / "docs" / p).exists()):
            bad.append("no such page: " + p)
    for s in set(re.findall(r"§ (\d+(?:\.\d+)?)", text)):
        if not re.search(r"^#{2,3} %s[ .]" % re.escape(s), full, re.M):
            bad.append("no such section: § " + s)
    for item in re.split(r"\n(?=- )", text):
        item = item.split("\n\n")[0]
        if item.startswith("- ") and not re.search(r"\((?:[^()]*?)(?:§ \d|`[^`]+`)[^()]*\)\.?\s*$", " ".join(item.split())):
            bad.append("a line with no source: " + item[:60])
    goal = re.search(r"Its state is \*\*(\d+) of 19\*\*", (ROOT / "docs" / "MAIN_GOAL.md").read_text(encoding="utf-8")).group(1)
    if "**%s of 19**" % goal not in text:
        bad.append("the goal's count is not stated as the goal states it")
    return bad


def test_the_short_page_names_a_source_for_every_line_and_uses_no_inner_word():
    import importlib.util, sys
    spec = importlib.util.spec_from_file_location("gates_for_the_short_page", ROOT / "scripts" / "gates" / "gates.py")
    g = importlib.util.module_from_spec(spec); sys.dont_write_bytecode = True; spec.loader.exec_module(g)
    text, full = SHORT.read_text(encoding="utf-8"), PAGE.read_text(encoding="utf-8")
    assert _short_problems(text, full) == []
    assert dict(g.public_face_words(text)) == {}
    # planted: a line with its source taken out, a section the full account lacks, a page that does not exist
    assert len(_short_problems(text.replace(" (§ 6).", ".", 1), full)) == 1
    assert len(_short_problems(text.replace("(§ 7)", "(§ 17)", 1), full)) == 1
    assert len(_short_problems(text.replace("`docs/THE_WEAVE.md`", "`docs/THE_WEAVES.md`", 1), full)) == 1
