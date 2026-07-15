"""B611 lock: the two-law test — both registered predictions FAILED as
sealed, with the diagnoses pinned.

Pins: RL and RRLL (amphichiral) conjugation-closed at all 15 levels; RRL
closed nowhere; RRRL closed ONLY at the dim-1 level kappa=4 (the P1
degenerate edge); NO object departs the unit circle anywhere (B_odd is
unitary by construction — the P2 vacuity diagnosis); the golden kappa=5
eigenvalues are exactly e^{+-2 pi i/5}.
"""
import importlib.util
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(__file__)
_SCRIPT = os.path.join(HERE, "..", "frontier", "B611_two_laws",
                       "two_laws_test.py")


def test_b611_scan():
    r = subprocess.run([sys.executable, _SCRIPT], capture_output=True,
                       text=True, timeout=3600)
    assert r.returncode == 0, r.stdout[-2000:] + r.stderr[-2000:]
    out = r.stdout
    assert out.count("departs the unit circle at kappa = []") == 4
    assert "RRL (m136, chiral): conj-closed at kappa = []" in out
    assert "RRRL (chiral): conj-closed at kappa = [4]" in out
    assert "P1 VERDICT: FAIL" in out
    assert "P2 (fig-8 golden-exclusivity in-scan): departures = [] " in out


def test_golden_eigenvalues_are_fifth_roots():
    spec = importlib.util.spec_from_file_location(
        "b238", os.path.join(HERE, "..", "frontier",
                             "B238_su32_levelrank", "su32_wrt.py"))
    b238 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(b238)
    w, S, T, cc = b238.su3_data(2)
    n = len(w)
    WRL = T @ (np.linalg.inv(S) @ np.linalg.inv(T) @ S)
    prs = sorted({(min(a, b), max(a, b)) for (a, b) in w if a != b})
    U = np.zeros((n, len(prs)))
    for j, (a, b) in enumerate(prs):
        U[w.index((a, b)), j] = 1 / np.sqrt(2)
        U[w.index((b, a)), j] = -1 / np.sqrt(2)
    lams = np.linalg.eigvals(-(U.T @ WRL @ U))
    targets = [np.exp(2j * np.pi / 5), np.exp(-2j * np.pi / 5)]
    assert all(min(abs(l - t) for t in targets) < 1e-9 for l in lams)
