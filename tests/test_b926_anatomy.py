"""B926 locks: the anatomy's structural completeness."""
import os

ARC = os.path.join(os.path.dirname(__file__), "..", "frontier", "B926_crossing_anatomy")


def _t(name):
    with open(os.path.join(ARC, name)) as f:
        return f.read()


def test_the_wall_list_and_menu_present():
    a = _t("ANATOMY.md")
    for tok in ("B915", "B925", "B429", "B916", "B923", "B905",
                "HEMISPHERE", "null"):
        assert tok in a


def test_executive_twelve_lines_and_the_default():
    e = _t("EXECUTIVE.md")
    assert "M0" in e and "standing default" in e.lower()
    assert "HEMISPHERE CHECK" in e


def test_no_status_upgrades_claimed():
    a = _t("ANATOMY.md").lower()
    assert "nothing here upgrades" in a or "no status" in a
