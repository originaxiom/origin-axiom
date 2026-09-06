"""B1260 — where net chirality can live: closed walled generally, abelian walled, rank-3 branch named."""
import subprocess, sys
from pathlib import Path
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1260_where_chirality_can_live" / "verification" / "where_chirality_can_live.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import where_chirality_can_live as W
    return W


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_alexander_is_reciprocal_with_golden_roots():
    W = _mod()
    t = W.t
    assert sp.simplify(sp.expand(t**2 * W.ALEX.subs(t, 1/t)) - W.ALEX) == 0
    roots = sp.solve(W.ALEX, t)
    assert sp.simplify(roots[0] * roots[1]) == 1


def test_abelian_sector_never_carries_net_chirality_including_at_a_jump():
    W = _mod()
    roots = sp.solve(W.ALEX, W.t)
    jump = False
    for v in (sp.Integer(2), sp.Rational(1, 2), sp.Integer(-1), roots[0]):
        a, b = W.h1_abelian(v), W.h1_abelian(sp.simplify(1 / v))
        assert a == b, (v, a, b)
        jump = jump or a > 0
    assert jump, "the control requires exercising a value where h1 jumps"


def test_every_symmetric_power_is_self_dual():
    t = sp.Symbol("t")
    for n in (0, 2, 4, 8, 12, 16):
        f = sum(t**(n - 2*k) for k in range(n + 1))
        g = sum((1/t)**(n - 2*k) for k in range(n + 1))
        assert sp.simplify(f - g) == 0
