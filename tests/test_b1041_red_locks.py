"""B1041 locks — the three red locks and the reason none was seen.

Reads the banked results.json (verify.py re-runs B616's script and a 240-step matrix walk) and
independently re-checks the two cheap structural facts.
"""
import json
import os
import pathlib
import re
import subprocess

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_R = json.loads((_ROOT / "frontier" / "B1041_the_red_locks" / "results.json")
                .read_text(encoding="utf-8"))


def test_every_check_passes():
    failed = [k for k, c in _R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_manifest_gap_is_measured_and_single_caused():
    """366 entries over nine harvest arcs; the missing ones are exactly what git refuses."""
    SHA = re.compile(r"^([0-9a-f]{64})\s\s(.+)$")
    entries, missing = 0, []
    for man in sorted(_ROOT.glob("frontier/B*/**/ORIGINALS_MANIFEST.txt")):
        base = man.parent
        for line in man.read_text(errors="ignore").splitlines():
            m = SHA.match(line.rstrip())
            if not m:
                continue
            rel = m.group(2).lstrip("./")
            entries += 1
            if not any((c / rel).exists() for c in (base, base / "packet")):
                missing.append(base / rel)
    assert entries > 300, entries
    assert 55 <= len(missing) <= 75, len(missing)
    rels = [str(p.relative_to(_ROOT)) for p in missing]
    r = subprocess.run(["git", "check-ignore", "--stdin"], input="\n".join(rels),
                       capture_output=True, text=True, cwd=_ROOT)
    ignored = set(r.stdout.split("\n")) - {""}
    assert len(ignored) >= 55, (len(ignored), len(rels))
    assert all(pathlib.Path(p).suffix in (".log", ".pyc") for p in ignored)


def test_the_gitignore_rule_that_causes_it_is_still_there():
    """If `*.log` is ever removed the gap can be closed and B1041's disposition revisited."""
    gi = (_ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
    assert "*.log" in [l.strip() for l in gi]


def test_B511s_known_arcsine_bug_is_documented_but_unrepaired():
    """The correction lives in prose; the script and the banked artifact still carry the error.
    Not this arc's discovery — D3_PARTIAL.md caught it in 2026-07. Locked so it is not re-raised
    as new, and so a repair is detectable."""
    d = _ROOT / "frontier" / "B511_physics_verdict"
    assert "is a\nBUG" in (d / "D3_PARTIAL.md").read_text(encoding="utf-8").replace("**", "")
    assert "U-SHAPED (arcsine-consistent)" in (d / "d3_measure.py").read_text(encoding="utf-8")
    assert "U-SHAPED (arcsine-consistent)" in (d / "d3_results.txt").read_text(encoding="utf-8")


def test_the_three_locks_are_no_longer_red():
    """The point of the arc: all three run green (one an explicit, reasoned skip)."""
    r = subprocess.run(["python3", "-m", "pytest", "-q",
                        "tests/test_b511_d5.py", "tests/test_b616_heldout.py",
                        "tests/test_b646_wave2.py"],
                       capture_output=True, text=True, cwd=_ROOT, timeout=1800)
    assert r.returncode == 0, r.stdout[-3000:]
    assert "failed" not in r.stdout.split("\n")[-3][:60], r.stdout[-500:]


def test_the_mechanism_is_credited_to_Review_42_not_claimed_as_new():
    """The arc's headline is a RECURRENCE, not a discovery. If this text ever moves, the arc's
    framing must move with it."""
    rev = (_ROOT / "docs" / "progress" / "REVIEWS.md").read_text(encoding="utf-8")
    assert "two locks were red at HEAD, and nobody knew" in rev
    assert "gates do not cover what" in rev
    assert "a partial run is not a run" in rev
    lawmap = (_ROOT / "docs" / "LAW_MAP.md").read_text(encoding="utf-8")
    assert "Review 42" in lawmap and "RECURRED" in lawmap
    assert "Not a new mechanism" in lawmap
