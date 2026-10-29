"""P-436 (decided 2026-10-29): the input-completeness ledger ('an unfilled row is a design defect') went unfilled in six
sealed six-fits (B1726, B1741, B1749, B1753, B1755, B1786); sealed preregistrations are not edited, so the gap is recorded
by dated notes, and the rule is gated from B1811 on, the first seal that filled it: every arc numbered 1811 or later with a
PREREGISTRATION.md carries the ledger's section, unless its preregistration declares itself data-free near the top.
A planted control shows the check can fail."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
HEAD = "## The input-completeness ledger"


def offenders(preregs):
    bad = []
    for arc, text in preregs:
        n = int(re.match(r"B(\d+)_", arc).group(1))
        if n < 1811: continue
        top = "\n".join(text.splitlines()[:25]).lower()
        if "data-free" in top or "no measured" in top: continue
        if HEAD not in text: bad.append(arc)
    return bad


def test_every_new_seal_fills_the_ledger():
    pre = [(p.parent.name, p.read_text(encoding="utf-8")) for p in (ROOT / "frontier").glob("B*/PREREGISTRATION.md") if re.match(r"B\d+_", p.parent.name)]
    assert offenders(pre) == []


def test_the_check_can_fail():
    assert offenders([("B1900_x", "# a seal\nagainst the measured six\n"), ("B1901_y", "# a seal\n" + HEAD + "\n"),
                      ("B1902_z", "# a seal (data-free)\n"), ("B1700_old", "# old\n")]) == ["B1900_x"]
