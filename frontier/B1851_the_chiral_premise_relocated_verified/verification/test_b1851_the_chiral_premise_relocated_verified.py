"""B1851 -- the web seat's relays' checkable facts reproduce on main's code, and the rulings are on the record."""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def test_relay_facts_reproduce():
    out = subprocess.run([sys.executable, "-B", str(HERE / "relay_facts.py")], capture_output=True, text=True, check=True,
                         timeout=600).stdout
    lines = [l for l in out.splitlines() if l.strip()]
    want = [l for l in (HERE / "relay_facts_run.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
    assert lines == want
    assert sum("ALL HOLD" in l or "HOLDS" in l for l in lines) == 3 and "4_1 isometric to b++LR: True" in out


def test_the_rulings_and_notes_are_on_the_record():
    card = (ROOT / "docs" / "THE_SCALE_CARD_DESIGN_P722.md").read_text(encoding="utf-8")
    assert "So the card is not sealable." in card and "the itemized count, priced in bits" in card
    for arc, phrase in (("B1012_branch_verifications", "The display's form."), ("B287_distinguished_closing", "two standard closings"),
                        ("B1034_l154_sigma", "V3 (a) records the gravity reading as non-chiral")):
        assert phrase in (ROOT / "frontier" / arc / "FINDINGS.md").read_text(encoding="utf-8"), arc
    reg = (ROOT / "docs" / "POINT_REGISTER.md").read_text(encoding="utf-8")
    assert "| P-732 | 2026-11-07 |" in reg and "NOT SEALABLE" in reg
