"""The freshness sweep as a suite test (ported from the consolidation branch's
B1054, commit 6be907ec; adopted on main 2026-08-13 after the B946 species was
confirmed here — the corpus's oldest E40 instance).

E40 (cached verification): a lock that passes when it should not, because it
asserts over a committed results.json cache instead of the instrument's fresh
output. E38 is a lock that fails when it should not; E40 is its silent twin.
This test re-runs every cache-shape instrument (non-mutating: snapshot and
restore) and fails on STALE-GREEN, RED, CRASH, or KEY-LOSS.

Cost: proportionate inside the full suite (main has 2 cache-shape
instruments today; the sweep discovers them, so growth is covered). The
per-push gate version stays registered-not-pretended (their R1-12).
Environment note (the audit's finding): instruments that measure platform
numerics or working-tree state certify container-relatively — a deviation
here must be dissected before it is called a corpus error.
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SWEEP = ROOT / "scripts" / "checks" / "instrument_freshness.py"


def test_every_cache_shape_instrument_reruns_green():
    r = subprocess.run([sys.executable, str(SWEEP)], capture_output=True,
                       text=True, cwd=ROOT, timeout=1800)
    assert r.returncode == 0, (
        "instrument freshness failed -- a lock is passing over a cache its "
        "instrument cannot reproduce (E40):\n" + r.stdout + r.stderr)


def test_the_sweep_is_not_vacuous():
    """The audit hit vacuous-green twice while porting (wrong ROOT scanned
    zero instruments). MB12 at the sweep level: the sweep must SEE at least
    the two known cache-shape instruments."""
    r = subprocess.run([sys.executable, str(SWEEP)], capture_output=True,
                       text=True, cwd=ROOT, timeout=1800)
    out = r.stdout + r.stderr
    assert "0 instruments" not in out, "the sweep scanned nothing -- ROOT is wrong"
