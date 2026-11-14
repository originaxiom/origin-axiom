"""B1930's lock: the foundation at version 1.68, its six paths into the moved folders under docs/archive/."""
import importlib.util
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PAGE = ROOT / "GENESIS.md"


def _script():
    spec = importlib.util.spec_from_file_location("b1930_write_version_1_68", HERE / "write_version_1_68.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


W = _script()


def _taken_back(text):
    """the page with this version taken back: the paths at their old places, the entry out, the line at 1.67"""
    i = text.index(W.LOG_HEAD)
    living, log = text[:i], text[i:]
    for p in W.PATHS:
        living = living.replace("`" + W.ARCHIVE + p, "`" + p)
    return (living + log.replace(W.ENTRY, "", 1)).replace(W.HEADER_IS, W.HEADER_WAS)


def _at_1_68(text):
    """MENDED 2026-11-14 (the building session's card C21, version 1.69): the page as it stood at this version, each later
    version taken back by its own lock, newest first, so this lock holds 1.68 and not the page's being at 1.68"""
    for later in sorted(ROOT.glob("frontier/B*_the_foundation_at_version_1_*/verification/test_b*_the_foundation_at_version_1_*.py"),
                        key=lambda q: -int(q.name.rsplit("_1_", 1)[1].split(".")[0])):
        minor = int(later.name.rsplit("_1_", 1)[1].split(".")[0])
        if minor <= 68 or "**Version 1.%d " % minor not in text:
            continue
        spec = importlib.util.spec_from_file_location("later_version_lock_%d" % minor, later)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        text = m._taken_back(text)
    return text


def test_the_page_is_at_1_68_and_its_paths_name_the_archive():
    text = _at_1_68(PAGE.read_text(encoding="utf-8"))
    assert W.HEADER_IS in text and W.HEADER_WAS not in text
    living = text[:text.index(W.LOG_HEAD)]
    for p in W.PATHS:
        assert living.count("`" + W.ARCHIVE + p) == 1, p
        assert (ROOT / W.ARCHIVE / p).is_file(), p
        assert not (ROOT / p).exists(), p
    log = text[text.index(W.LOG_HEAD):]
    assert log.index(W.ENTRY) < log.index("\n- **v1.67 ")


def test_the_script_gives_the_page_again():
    text = _at_1_68(PAGE.read_text(encoding="utf-8"))
    assert W.version_1_68(_taken_back(text)) == text


def test_a_path_left_at_its_old_place_is_refused():
    text = _taken_back(_at_1_68(PAGE.read_text(encoding="utf-8")))
    import pytest
    # a seventh path into a moved folder, added to section 1
    k = text.index("## 1. The principle")
    planted = text[:k] + "See `philosophy/P000_what_is_not_nothing.md`.\n\n" + text[k:]
    with pytest.raises(AssertionError):
        W.version_1_68(planted)
    # one of the six already taken (the script finds it not once)
    half = text.replace("`" + W.PATHS[0], "`" + W.ARCHIVE + W.PATHS[0], 1)
    with pytest.raises(AssertionError):
        W.version_1_68(half)
