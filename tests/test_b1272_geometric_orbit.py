"""B1272 — the two 2T orbits are separated arithmetically; one is the geometric reduction."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1272_the_binary_is_geometric" / "verification" / "geometric_orbit.py"


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import geometric_orbit as G
    return G


def test_selftest_passes():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout


def test_the_invariant_triples_are_3_6_4_and_6_6_4():
    G = _mod()
    S, lab, k = G.orbits()
    assert k == 2
    tri = sorted({G.triple(*p) for p in S})
    assert tri == [(3, 6, 4), (6, 6, 4)], tri


def test_the_geometric_reduction_lands_in_the_order_3_orbit():
    G = _mod()
    S, lab, k = G.orbits()
    A, B = (1, 1, 0, 1), (1, 0, 2, 1)          # holonomy mod (1-omega) over F_3
    assert G.T.generated([A, B]).__len__() == 24
    assert G.triple(A, B) == (3, 6, 4)


def test_the_longitude_does_not_separate():
    """Control: the third slot is the commutator, not the longitude."""
    G = _mod()
    S, _, _ = G.orbits()
    assert {G.order(G.ev(G.LONGITUDE, *p)) for p in S} == {2}
