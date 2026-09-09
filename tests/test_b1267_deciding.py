"""B1267 — the deciding computation: index zero, W1/W2 rigid, with the Sym homomorphism control."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1267_the_deciding_computation" / "verification" / "deciding.py"


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-4000:] + r.stderr[-4000:]
    assert "SELFTEST: PASS" in r.stdout


def test_sym_is_a_homomorphism():
    """The bug that failed attempt 1: a transposed Sym is an ANTI-homomorphism."""
    import numpy as np
    sys.path.insert(0, str(SCRIPT.parent))
    import deciding as D
    rng = np.random.default_rng(3)
    X = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2)); X /= np.linalg.det(X) ** 0.5
    Y = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2)); Y /= np.linalg.det(Y) ** 0.5
    for n in (1, 2, 3, 4, 6):
        assert np.max(np.abs(D.sym(X @ Y, n) - D.sym(X, n) @ D.sym(Y, n))) < 1e-9, n
