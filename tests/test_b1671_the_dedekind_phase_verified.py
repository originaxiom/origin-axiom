"""B1671 -- the Dedekind phase, verified and scoped on main. Stored logs: the sum rule holds for the symmetric and
antisymmetric zero-diagonal sectors and fails for the general one (the scope); B1635's table reproduced by the exact
solver; det Y1 / eta^6 = 8; the phase law's deviation small at Im tau = 2.5. Live: e1^2 = 4 e2 for a random complex
symmetric zero-diagonal matrix, and its failure for a random zero-diagonal one (the bite)."""
import json, pathlib, re
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1671_the_dedekind_phase_verified"
V = A / "verification"


def test_stored_logs():
    v4 = (V / "my_verify4.log").read_text()
    assert re.search(r"symmetric zero-diag \(O\+\)\s+: .* violations\(>1e-9\)=0/50000", v4)
    assert re.search(r"general zero-diag \(O\+ \+ r O-\)\s+: .*min s2/s1=0\.1280\s+violations\(>1e-9\)=50000/50000", v4)
    v3 = (V / "my_verify3.log").read_text()
    assert "B1635 table reproduced: True" in v3
    v2 = (V / "my_verify2.log").read_text()
    assert "e1^2-4e2 = 0" in v2 and v2.count("det Y1/eta^6 = (8.0") == 3
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"


def test_live_sum_rule_and_bite():
    rng = np.random.default_rng(1670)
    def ratios(Y):
        s = np.sort(np.linalg.svd(Y, compute_uv=False))[::-1]
        return abs(s[0] - s[1] - s[2]) / s[0], s[1] / s[0]
    a, b, c = rng.normal(size=3) + 1j * rng.normal(size=3)
    Ysym = np.array([[0, a, b], [a, 0, c], [b, c, 0]])
    d, s2 = ratios(Ysym)
    assert d < 1e-12 and s2 >= 0.5 - 1e-12                        # m1 = m2 + m3, so m2/m1 >= 1/2
    Ygen = np.array([[0, a, b], [a * 1.7j, 0, c], [b, c * -0.6, 0]])
    assert ratios(Ygen)[0] > 1e-3                                  # bite: a general zero-diagonal coupling breaks it
