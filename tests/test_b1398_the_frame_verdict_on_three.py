"""B1398 lock -- THE FRAME'S VERDICT ON THREE.

In the seat's frame (7d E6 super-Yang-Mills, the geometric SL(2)_beta twist, an abelian Higgs field of any rank) the 78's 10s are all
SL(2)_beta doublets, the frame's spin-0 count is anomaly-free only if zero, caps give 10s in pairs, and every exotic-free anomaly-free
combination has an even number of generations (zero for a bulk flux).  With 27 matter the frame's rule admits exactly one anomaly-free
family, three generations at N = (3, 0, -3, 0, 3, -6) on six direction classes -- two absolute values, so no rank-one Higgs gives it."""
import importlib.util
from fractions import Fraction as Fr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VER = ROOT / "frontier" / "B1398_the_frame_verdict_on_three" / "verification"


def _load():
    spec = importlib.util.spec_from_file_location("b1398_frame_verdict", VER / "frame_verdict.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_verdict_and_the_escape():
    V = _load()
    out = V.main()                                             # every assertion of V1-V7 runs inside
    assert out["V1 78 10-type weights by SL(2)_beta spin"] == {1: 40}
    assert out["V2 F78 anomaly matrix rank"] == (3, 3)
    assert out["V4 F78 combination solutions"] == [{"c": "0", "d": "g/2", "n0": "0", "n1": "0", "n2": "0"}]
    assert out["V5 F27+78 anomaly matrix rank"] == (5, 6)
    assert out["V5 the anomaly-free family at g = 3: N per class"] == {
        "(1, -4)": 3, "(1, 0)": 0, "(1, 1)": -3, "(1, 6)": 0, "(3, -2)": 3, "(3, 8)": -6}
    assert out["V6 absolute values of the pattern"] == [3, 6]


def test_linear_content_matches_integer_content():
    """the truncation bug caught while building the instrument: at integral counts the linear content equals FS.content's"""
    V = _load()
    FS = V.FS
    for d in (3, 6):
        st = V.cap_states(0, d, V.ALL78 + list(FS.W27))
        lin = {r: k for r, k in V.net_linear(st).items()}
        integer = {r: Fr(k) for r, k in V.net_content(st).items()}
        assert lin == integer
    lin1 = V.net_linear(V.cap_states(0, 1, V.ALL78 + list(FS.W27)))
    assert all(k == Fr(4, 3) for k in lin1.values())            # 4/3 of a generation per unit gamma-flux, exactly
