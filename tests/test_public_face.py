"""The gate `public-face` (main's card C14): the pages a reader outside the project opens use none of the record's inner words.

Held here: the words the reader counts and those it does not; "main" in a phrase of plain English; the count held by page and
by word, so that a new word fails even where another left the page; the working record and the working indices not read;
a missing page fails; and the gate on this repository, with today's counts."""
import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _gates():
    sys.dont_write_bytecode, was = True, sys.dont_write_bytecode
    try:
        spec = importlib.util.spec_from_file_location("gates_for_the_public_face", ROOT / "scripts" / "gates" / "gates.py")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
    finally:
        sys.dont_write_bytecode = was
    return m


g = _gates()
words = g.public_face_words


def test_the_words_it_counts_and_the_words_it_does_not():
    assert words("The owner's ruling, relayed by the SM seat to main, was ruled on a card.") == {
        "owner": 1, "ruling": 1, "relay": 1, "seat": 1, "main": 1, "ruled": 1, "card": 1}
    assert words("cc3 and cc read agy-002's lane, and codex and cld-advisor read the lanes") == {"cc": 2, "a session's name": 3, "lane": 2}
    # not counted: the words inside other words, and the plain-English "main"
    assert words("ownership, seated, planes, relayer, cardinal, domain, mainly, remains, pruled") == {}
    assert words("The main goal is stated; the main result is open; MAIN_GOAL.md is a file.") == {}
    assert words("main reads the main goal") == {"main": 1}
    # the atlas query's subcommand is a command; the word elsewhere is counted
    assert words("`python3 scripts/atlas/query.py card B1812`") == {} and words("the seat's card") == {"seat": 1, "card": 1}


def test_a_new_word_fails_even_where_another_left_the_page():
    held = {"README.md": {"owner": 2}}
    assert g.public_face_problems({"README.md": {"owner": 2}}, held) == []
    assert g.public_face_problems({"README.md": {"owner": 1}}, held) == []
    assert g.public_face_problems({"README.md": {"owner": 1, "seat": 1}}, held) == ["README.md: 'seat' 1 times, held at 0"]
    assert g.public_face_problems({"README.md": {"owner": 3}}, held) == ["README.md: 'owner' 3 times, held at 2"]
    assert g.public_face_problems({"README.md": None}, held) == ["README.md: the page is not there"]


def test_the_working_record_and_the_working_indices_are_not_read():
    assert "PROGRESS_LOG.md" not in g.PUBLIC_FACE and "docs/POINT_REGISTER.md" not in g.PUBLIC_FACE
    assert not set(g.WORKING_INDICES) & set(g.PUBLIC_FACE)
    # the README points to each working index it names as one
    readme = " ".join((ROOT / "README.md").read_text(encoding="utf-8").split())
    for rel in g.WORKING_INDICES:
        if rel in readme:
            i = readme.index(rel)
            near = readme[max(0, i - 200):i + 300]                         # the label stands before the link or after it
            assert "working index" in near or "working indices" in near, rel
    assert not [p for p in g.PUBLIC_FACE if p.startswith(("docs/seats/", "docs/progress/", "docs/handoffs/", "frontier/", "relays/"))]


def test_on_this_repository_the_gate_passes_and_every_page_is_held_as_found():
    ok, detail = g.GATES["public-face"]()
    assert ok is True, detail
    counts = g.public_face_counts()
    assert all(c is not None for c in counts.values())
    assert {k: v for k, v in counts.items() if v} == {k: v for k, v in g.PUBLIC_FACE_HELD.items() if v}
    assert set(g.PUBLIC_FACE_HELD) <= set(g.PUBLIC_FACE)


def test_the_readme_block_gives_no_words_of_a_changelog_heading(tmp_path, monkeypatch):
    """C14, patch 5 (main's M24): the generated block of the README is read by the gate with the rest of the page; its
    line on the last landing gives the day and where the entry stands, so a heading in the working record's words does
    not reach the front page. Planted: a heading full of inner words."""
    g = _gates()
    spec = importlib.util.spec_from_file_location("views_generate", ROOT / "scripts" / "views" / "generate.py")
    gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen)
    heading = "S999 THE OWNER'S SEAT RULED THAT THE LANE'S RELAY BE CARDED BY MAIN (P-1) (2026-11-14)"
    assert sum(g.public_face_words(heading).values()) >= 6           # the plant carries the words
    (tmp_path / "CHANGELOG.md").write_text("# Changelog\n\n## %s\n\n- a line\n" % heading, encoding="utf-8")
    monkeypatch.setattr(gen, "ROOT", str(tmp_path))
    block = gen.view_readme_state([])
    line = [l for l in block.split("\n") if l.startswith("| the last landing |")]
    assert line == ["| the last landing | 2026-11-14; its entry heads `CHANGELOG.md` (the working record) |"], line
    assert dict(g.public_face_words(block)) == {}
    # the twin: the line as it stood printed the heading, and the gate would have counted its words
    assert sum(g.public_face_words("| the last landing | %s |" % heading[:150]).values()) >= 6
