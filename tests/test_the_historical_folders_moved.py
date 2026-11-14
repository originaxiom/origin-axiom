"""The third move under GOVERNANCE section 12 (docs/REORGANIZATIONS.md, its third entry; card C18 of the building session,
approved by main in M28): the historical folders stand under docs/archive/, the ten copies of notes are out of the tree,
and no living page names a moved file at its old place. Planted: a living page that names one at its old place; a file
of a moved folder back at its old place; a copy of a note back in the tree."""
import importlib.util
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def _move():
    spec = importlib.util.spec_from_file_location("history_2026_11_13", ROOT / "scripts" / "reorganize" / "history_2026_11_13.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


M = _move()


def test_the_tree_is_as_the_move_leaves_it():
    assert M.check() == []
    for old, new in M.MOVES:
        assert not (ROOT / old).exists() and (ROOT / new).is_dir(), old


def test_a_living_page_that_names_a_moved_file_at_its_old_place_is_found():
    found, again = M.references("See `philosophy/P000_what_is_not_nothing.md` and `docs/archive/legacy/README.md`.")
    assert found == ["philosophy/P000_what_is_not_nothing.md"]
    assert "`docs/archive/philosophy/P000_what_is_not_nothing.md`" in again and "docs/archive/docs/archive" not in again
    # the twin: a path that names no moved file is left as it is
    assert M.references("the paths/ of a walk, and `outside_bench/README.md`")[0] == []


def test_a_file_back_at_its_old_place_or_a_note_back_in_the_tree_is_reported(monkeypatch):
    real = M.tracked

    def planted(prefix, rev=None):
        out = real(prefix, rev)
        if rev is None and prefix == "story/":
            out = out + ["story/README.md"]
        if rev is None and prefix == M.REMOVE[0]:
            out = out + [M.REMOVE[0]]
        return out
    monkeypatch.setattr(M, "tracked", planted)
    bad = M.check()
    assert "still at its old place: story/" in bad and ("still in the tree: " + M.REMOVE[0]) in bad
