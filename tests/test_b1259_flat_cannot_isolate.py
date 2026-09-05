"""B1259 — no flat G2 orbifold can supply Acharya–Witten isolation."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1259_flat_orbifolds_cannot_isolate" / "verification" / "flat_cannot_isolate.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import flat_cannot_isolate as F
    return F


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_every_SO7_element_fixes_a_line():
    import numpy as np
    F = _mod()
    rng = np.random.default_rng(5)
    assert all(F.has_eigenvalue_one(F.random_SO(7, rng)) for _ in range(500))


def test_the_statement_is_dimension_specific_not_trivial():
    """MB12: SO(6) generically avoids eigenvalue +1, so the SO(7) result has content."""
    import numpy as np
    F = _mod()
    rng = np.random.default_rng(7)
    misses = sum(0 if F.has_eigenvalue_one(F.random_SO(6, rng)) else 1 for _ in range(300))
    assert misses > 0
