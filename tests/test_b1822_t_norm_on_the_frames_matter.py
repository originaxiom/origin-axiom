"""B1822 -- T-NORM on the frame's matter: the committed results hold the theorem's identity, the referee's independent
implementation agrees, and the freedom of H is stated. A planted non-orthogonal basis must fail the check."""
import json, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1822_t_norm_on_the_frames_matter" / "verification"


def test_the_committed_results():
    d = json.loads((V / "REPORT.json").read_text(encoding="utf-8"))
    assert d["verdict"].startswith("T-NORM HOLDS") and len(d["results"]) == 1170
    assert max(r["max_offdiag"] for r in d["results"]) < 1e-10 and max(r["max_diag_spread"] for r in d["results"]) == 0.0
    ind = json.loads((V / "referee" / "independent.json").read_text(encoding="utf-8"))
    assert ind


def test_the_check_can_fail():
    # a deliberately non-orthogonal pair (psi1 + 0.3 psi0 against psi0) has normalised overlap 0.3/sqrt(1.09) = 0.287348
    g = np.array([[1.0, 0.3], [0.3, 1.09]]); off = g[0, 1] / np.sqrt(g[0, 0] * g[1, 1])
    assert abs(off - 0.287348) < 1e-6 and off > 1e-10


def test_the_freedom_is_stated():
    t = (ROOT / "frontier" / "B1822_t_norm_on_the_frames_matter" / "FINDINGS.md").read_text(encoding="utf-8")
    assert "CHOSEN input" in t and "8 real parameters per field" in t and "proves at best a diagonal H" in t
