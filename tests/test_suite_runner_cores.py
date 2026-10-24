"""R69-3 (Review 69, 2026-10-24): the suite runner's parallel default respects the owner's 8-core rule; `--changed` falls
back to the runner itself, so one default covers both paths.  The check is shown to fail on a planted default."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]


def workers(text):
    m = re.search(r'^MODE="-n (\d+)"', text, re.M)
    return int(m.group(1)) if m else None


def test_default_at_most_eight():
    assert (workers((ROOT / "scripts" / "run_suite.sh").read_text(encoding="utf-8")) or 0) <= 8


def test_changed_falls_back_to_the_runner():
    assert 'subprocess.run(["scripts/run_suite.sh"])' in (ROOT / "scripts" / "affected_tests.py").read_text(encoding="utf-8")


def test_the_check_can_fail():
    assert workers('MODE="-n 12"; MARK=()') == 12 and workers('MODE="-n 8"; MARK=()') == 8
