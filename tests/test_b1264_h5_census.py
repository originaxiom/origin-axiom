"""B1264 — the H5 census and I-14's recomputed status."""
import re
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1264_h5_census" / "verification" / "h5_census.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import h5_census as H
    return H


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_trinification_gradings_measured():
    H = _mod()
    lab, col = H.trinification_gradings()
    assert lab == 170 and len(col) == 85


def test_the_census_has_eight_instances_and_marks_what_is_measured():
    H = _mod()
    assert len(H.CENSUS) == 8
    measured = [c for c in H.CENSUS if c[2] is not None]
    assert len(measured) == 5, "measured vs banked-unmeasured must stay distinguished"


def test_the_census_headline_matches_what_the_census_actually_measures():
    """B1410 repair, second form. The two assertions above are BOTH-LITERAL
    (check_test_vacuity's own class): they pin hand-written numbers and could never catch the
    defect that actually happened -- this arc's HEADLINE said 'EIGHT MEASURED INSTANCES' for nine
    days while this file asserted five, the wrong headline sat in arc_verdict.json, and eleven
    live uses spread across seven files.

    The FIRST version of this lock read three hand-listed surfaces and passed an injected use in
    an eighth file -- the enforcement narrower than its rule (E66). It now sweeps every tracked
    .md/.py/.json outside the GENERATED views, so its population is the defect's population.

    A MENTION inside a correction must pass: a record OF an error has to be able to quote it.
    That is the same use/mention split scripts/checks/retraction_sweep.py makes."""
    H = _mod()
    measured = len([c for c in H.CENSUS if c[2] is not None])
    banked = len(H.CENSUS)
    assert measured < banked, "the census no longer distinguishes measured from banked"

    root = Path(__file__).resolve().parents[1]
    cue = re.compile(r"corrected|B1410|banked-unmeasured|this row said|HEADLINE said", re.I)
    # \b before the digit: "B1008 measured the atlas" is not a claim about eight instances.
    bad = re.compile(rf"\b(eight|{banked})\s+measured\b", re.I)
    # A QUOTED occurrence is a MENTION, not a use: writing a correction requires quoting the
    # wording being corrected. Same principle as retraction_sweep.py allowing a retracted phrase
    # inside a retraction record. Quoted = wrapped in "..." / “...” / `...` on that line.
    quoted = re.compile(
        rf"""["\u201c`][^"\u201d`]*\b(eight|{banked})\s+measured\b[^"\u201d`]*["\u201d`]""", re.I)
    offenders = []
    for path in root.rglob("*"):
        if path.suffix not in (".md", ".py", ".json") or not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        # docs/views/ is GENERATED from arc_verdict.json -- fixing the source fixes it, and the
        # views-generated gate proves it. .git and legacy are not the corpus.
        if rel.startswith(("docs/views/", ".git/", "legacy/", "audit/", "docs/progress/")):
            continue
        # The append-only record is EXEMPT, exactly as scripts/checks/retraction_sweep.py exempts
        # CHANGELOG.md / PROGRESS_LOG.md / docs/progress/REVIEWS.md: those files record what was
        # written AT THE TIME and are never rewritten -- corrections are appended. Rewriting them
        # to hide a corrected claim would destroy the evidence that the correction happened.
        if rel in ("CHANGELOG.md", "PROGRESS_LOG.md"):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for line in text.splitlines():
            if cue.search(line):
                continue
            if bad.search(line) and not quoted.search(line):
                offenders.append(f"{rel}: {line.strip()[:100]}")
    assert not offenders, (
        f"{len(offenders)} surface(s) USE the banked count ({banked}) as the measured count, "
        f"but only {measured} are measured:\n  " + "\n  ".join(offenders[:6]))
