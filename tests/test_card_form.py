"""2026-11-26 (the framework's thin path, patch T2; main's M54; register row P-885): the claim card's form check,
scripts/queue/card_form.py. A card whose form holds passes and each rule, planted once, fails it; the template in
docs/CLAIM_CARD.md holds exactly the fields the check reads, so the page and the check cannot drift apart; the command
runs by hand."""
import importlib.util
import json
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
- scope: frame: F-HE; object: m004; reach: single; hypotheses: none
- identifications: none
- definitions: a class is an orbit of the group on the level's states
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
        ("- kind: computation", "- kind: none", "may not be none"),
        ("- touches: P-885", "- touches: none", "so its effect is not none"),
        ("- effect: supports — P-885", "- effect: none", "'effect' may not be none"),
        ("- scope: frame: F-HE; object: m004; reach: single; hypotheses: none\n", "", "'scope' is missing"),
        ("- scope: frame: F-HE; object: m004; reach: single; hypotheses: none", "- scope: none", "may not be none"),
        ("object: m004; reach", "reach", "scope is not"),
        ("reach: single", "reach: every", "reach 'every' is not one of"),
        ("frame: F-HE;", "frame: ;", "scope is not"),
        ("- identifications: none\n", "", "'identifications' is missing"),
        ("- definitions: a class is an orbit of the group on the level's states\n", "", "'definitions' is missing"),
        ("- definitions: a class is an orbit of the group on the level's states", "- definitions:", "is empty"),
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


def test_definitions_may_be_none_m60():
    assert CF.form_problems(TWIN.replace("- definitions: a class is an orbit of the group on the level's states",
                                         "- definitions: none")) == []


def test_a_card_that_touches_nothing_and_a_card_declared_heavy():
    none = TWIN.replace("- touches: P-885", "- touches: none").replace("- effect: supports — P-885", "- effect: none")
    assert CF.form_problems(none) == []
    heavy = TWIN.replace("output SHA-256 fedcba9876543210", "output SHA-256 fedcba9876543210, heavy")
    assert CF.form_problems(heavy) == [] and CF.declared_heavy(CF.read(heavy)[1])
    assert not CF.declared_heavy(CF.read(TWIN)[1])
    assert CF.form_problems(TWIN.replace("fedcba9876543210", "fedcba9876543210, light")), "only ', heavy' may follow"


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


def test_review_88s_rules_on_the_form_t7b():
    """main's M64, items 14, 18, 26 and 28 (Review 88's A3, A12, A14, A21, B10), each planted once"""
    plants = [
        # 14: the effect's codes are codes the card touches
        ("- effect: supports — P-885", "- effect: removes — A03", "the effect names what the card does not touch: A03"),
        ("- effect: supports — P-885", "- effect: supports — the Higgs mass", "the 19: mass"),
        # 18: the script's path stays in the commit; "run as" runs the declared script; the control compared as a command
        ("frontier/B2011_x/verification/count.py, SHA-256", "/etc/count.py, SHA-256", "leaves the commit"),
        ("frontier/B2011_x/verification/count.py, SHA-256", "../count.py, SHA-256", "leaves the commit"),
        ("run as python3 frontier/B2011_x/verification/count.py,", "run as python3 other.py,",
         "'run as' does not run the declared script"),
        ("- failing control: python3 frontier/B2011_x/verification/count.py --plant",
         "- failing control: python3  frontier/B2011_x/verification/count.py",
         "the failing control is the decisive command itself"),
        # 28: a line outside any field is said
        ("- second computation: none\n", "- second computation: none\n\nan orphan line\n", "outside any field"),
    ]
    for old, new, words in plants:
        bad = _plant(old, new)
        assert bad and any(words in b for b in bad), (words, bad)
    # 28: the hypotheses may hold ";"; a code the card touches may stand in the effect, in any case
    assert CF.form_problems(TWIN.replace("hypotheses: none", "hypotheses: the frame's cusp; its field")) == []
    assert CF.form_problems(TWIN.replace("- touches: P-885", "- touches: P-885, a03").replace(
        "- effect: supports — P-885", "- effect: supports — A03")) == []
    # 26: the allowed list is the rerun's own, from ALLOWED_PACKAGES.json
    pins = json.loads((ROOT / "scripts/queue/ALLOWED_PACKAGES.json").read_text(encoding="utf-8"))
    assert set(CF.ALLOWED) == {"the standard library"} | set(pins["packages"]) | set(pins["heavy"])


def test_mains_own_trial_cards_hold_the_form():
    for card in sorted((ROOT / "relays" / "claims").glob("CLAIM_*_main_trial.md")):
        assert CF.form_problems(card.read_text(encoding="utf-8")) == [], card.name
