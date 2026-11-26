"""2026-11-26 (the framework's thin path, patch T2; main's M54; register row P-885): the claim card's form check,
scripts/queue/card_form.py. A card whose form holds passes and each rule, planted once, fails it; the template in
docs/CLAIM_CARD.md holds exactly the fields the check reads, so the page and the check cannot drift apart; the command
runs by hand."""
import importlib.util
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("card_form_under_test", ROOT / "scripts/queue/card_form.py")
CF = importlib.util.module_from_spec(_spec)
sys.dont_write_bytecode = True
_spec.loader.exec_module(CF)

TWIN = """# CLAIM CARD — a count of the classes at level 5, reproduced

```
- card id: new
- seat code: fam2-v5.5-high-01
- seat, branch, commit: fam2-v5.5-high-01, seat/frontier-2026-11-26, 0123456789abcdef0123456789abcdef01234567
- kind: computation
- touches: P-885
- effect: supports — P-885
- imports: none
- premises on main: B2011
- decisive script: frontier/B2011_x/verification/count.py, SHA-256 0123456789abcdef, depends on the standard library
  and python-flint, run as python3 frontier/B2011_x/verification/count.py, output SHA-256 fedcba9876543210
- decisive lines: 3 lines marked "DECISIVE:", SHA-256 00112233445566ff
- failing control: python3 frontier/B2011_x/verification/count.py --plant
- second computation: none
- already on main?: python3 scripts/checks/topic_sweep.py count; the closest arc B2011
- what would make it fail: the planted level must change the count
```
"""


def _plant(old, new):
    assert TWIN.count(old) == 1, old
    return CF.form_problems(TWIN.replace(old, new))


def test_a_card_whose_form_holds_passes_and_each_rule_planted_fails():
    assert CF.form_problems(TWIN) == []
    plants = [
        ("# CLAIM CARD — a count", "# CLAIM — a count", "first line"),
        ("- card id: new\n", "", "'card id' is missing"),
        ("- card id: new", "- card id: Q0007", "card id is not"),
        ("- seat code: fam2-v5.5-high-01", "- seat code: a seat", "seat code:"),
        ("- seat code: fam2-v5.5-high-01", "- seat code: F1", "seat code:"),
        ("fam2-v5.5-high-01, seat/", "fam3-v5.5-high-01, seat/", "is not the card's seat code"),
        ("0123456789abcdef0123456789abcdef01234567", "0123456", "full 40-hex commit"),
        ("- kind: computation", "- kind: a guess", "kind is not"),
        ("- effect: supports — P-885", "- effect: supports P-885", "effect does not"),
        ("- premises on main: B2011", "- premises on main:", "is empty"),
        ("- touches: P-885", "- touches: none", "may not be none"),
        ("the standard library\n  and python-flint", "the standard library\n  and pandas", "not allowed: pandas"),
        ("output SHA-256 fedcba9876543210", "output fedcba9876543210", "decisive script is not"),
        ("3 lines marked", "0 lines marked", "decisive lines is not"),
        ("SHA-256 00112233445566ff", "SHA-256 0011", "decisive lines is not"),
        ("count.py --plant", "count.py", "the decisive command itself"),
        ("- failing control: python3 frontier/B2011_x/verification/count.py --plant", "- failing control: fails",
         "not a command"),
        ("- second computation: none", "- second computation: none\n- score: 3", "not a field of the card"),
        ("- kind: computation", "- kind: computation\n- kind: theorem", "stands twice"),
    ]
    for old, new, words in plants:
        bad = _plant(old, new)
        assert bad and any(words in b for b in bad), (words, bad)


def test_a_field_runs_over_lines_and_a_refile_names_its_card():
    _, f, bad = CF.read(TWIN)
    assert bad == [] and f["decisive script"].endswith("output SHA-256 fedcba9876543210")
    assert CF.form_problems(TWIN.replace("- card id: new", "- card id: refiles Q0007")) == []


def test_the_template_holds_exactly_the_fields_the_check_reads():
    page = (ROOT / "docs" / "CLAIM_CARD.md").read_text(encoding="utf-8")
    block = re.search(r"```\n(# CLAIM CARD.*?)```", page, re.S).group(1)
    names = [m.group(1) for m in re.finditer(r"^- ([a-z ,?]+):", block, re.M)]
    assert tuple(names) == CF.FIELDS
    for pkg in CF.ALLOWED[1:]:
        assert pkg in block, pkg


def test_the_command_runs_by_hand(tmp_path):
    good, bad = tmp_path / "CLAIM_good.md", tmp_path / "CLAIM_bad.md"
    good.write_text(TWIN, encoding="utf-8")
    bad.write_text(TWIN.replace("- kind: computation", "- kind: a guess"), encoding="utf-8")
    run = lambda *a: subprocess.run([sys.executable, "-B", str(ROOT / "scripts/queue/card_form.py"), *map(str, a)],
                                    capture_output=True, text=True)
    assert run(good).returncode == 0
    r = run(good, bad)
    assert r.returncode == 1 and "kind is not" in r.stdout and "the form holds" in r.stdout
