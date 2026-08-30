"""B1202 lock -- the already-banked check must stay two-sided."""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "scripts" / "checks" / "already_banked.py"


def _run(terms):
    return subprocess.run([sys.executable, str(CHECK), "--exclude=B1202"] + terms,
                          capture_output=True, text=True, cwd=str(ROOT)).returncode


def test_flags_the_four_historical_misses():
    for terms in (["quine", "self-naming", "census"],
                  ["stabilization", "depth-closure", "WALL-7", "TOMB-L34"],
                  ["genesis", "fork", "locks", "F2", "F8"],
                  ["dark", "hyperbola", "prime-power", "symbolic", "proof"]):
        assert _run(terms) == 1, f"must flag: {terms}"


def test_stays_silent_on_genuine_blind_regions():
    for terms in (["inflation", "reheating", "e-folds", "primordial"],
                  ["dark", "matter", "relic", "abundance", "freeze-out"]):
        assert _run(terms) == 0, f"false alarm: {terms}"
