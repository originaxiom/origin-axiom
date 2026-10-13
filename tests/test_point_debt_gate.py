"""The point-debt gate (2026-10-13, the owner: "we clarify the picture, but fail to address all the points we made").
Pins: FLOOR equals the register's row count (adding points raises it in the same commit); STALE_DAYS = 21; the real
register passes today; and the failure paths -- a deleted point, a row without a disposition, a DONE row naming nothing
that exists, an undefined slot, a stale QUEUED row, and its escalation -- each fire on a planted copy."""
import datetime
import importlib.util
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "checks" / "point_debt.py"
REGISTER = ROOT / "docs" / "POINT_REGISTER.md"


def _mod():
    spec = importlib.util.spec_from_file_location("point_debt", CHECKER)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _run(text, tmp_path, today=None):
    f = tmp_path / "POINT_REGISTER.md"
    f.write_text(text, encoding="utf-8")
    env = dict(os.environ, OA_POINT_REGISTER=str(f))
    if today:
        env["OA_POINT_TODAY"] = today
    return subprocess.run([sys.executable, str(CHECKER)], capture_output=True, text=True, env=env)


def test_floor_and_stale_days():
    m = _mod()
    rows, _ = m.parse(REGISTER.read_text(encoding="utf-8"))
    assert m.FLOOR == len(rows), "a point was added or removed: set FLOOR to the register's row count"
    assert m.STALE_DAYS == 21


def test_the_real_register_passes_and_the_gate_is_registered():
    sys.path.insert(0, str(ROOT / "scripts" / "gates"))
    import gates
    assert "point-debt" in gates.GATES
    r = subprocess.run([sys.executable, str(CHECKER)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout


def test_the_gate_fails_on_a_deleted_point(tmp_path):
    text = REGISTER.read_text(encoding="utf-8")
    lines = [l for l in text.splitlines() if not l.startswith("| P-002 |")]
    r = _run("\n".join(lines) + "\n", tmp_path)
    assert r.returncode == 1 and "deleted" in r.stdout


def test_planted_defects_each_fire(tmp_path):
    text = REGISTER.read_text(encoding="utf-8")
    first_done = next(l for l in text.splitlines() if l.startswith("| P-001 |"))
    first_q = next(l for l in text.splitlines() if l.startswith("| P-") and "| QUEUED |" in l)
    cases = {
        "disposition": text.replace(first_done, first_done.replace("| DONE |", "| MAYBE |")),
        "does not exist": text.replace(first_done, first_done.replace("| DONE |", "| DONE |").replace("B1640 cell A;", "docs/NO_SUCH_FILE.md;")),
        "not defined": text.replace(first_q, first_q.replace("| QUEUED | Q", "| QUEUED | Q99 Q")),
    }
    for needle, planted in cases.items():
        r = _run(planted, tmp_path)
        assert r.returncode == 1 and needle in r.stdout, (needle, r.stdout)


def test_a_stale_queued_point_fails_and_escalation_clears_it(tmp_path):
    text = REGISTER.read_text(encoding="utf-8")
    far = (datetime.date(2026, 10, 13) + datetime.timedelta(days=60)).isoformat()
    r = _run(text, tmp_path, today=far)
    assert r.returncode == 1 and "without ESCALATED" in r.stdout
    q = next(l for l in text.splitlines() if l.startswith("| P-") and "| QUEUED |" in l)
    pid = q.split("|")[1].strip()
    escalated = text.replace(q, q.replace("| QUEUED | ", f"| QUEUED | ESCALATED({far}: next action named) "))
    r2 = _run(escalated, tmp_path, today=far)
    assert pid + ":" not in r2.stdout and pid + ":" in r.stdout
