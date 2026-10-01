"""B1442 lock -- no generation-shaped background of count two on the seventeen several-cusped carriers.

Sealed before any background was assembled on several cusps. Recorded: the seventeen, the five predictions as read by
the sealed reader. Live: the order-two lemma (the dual of the Q sector is the L sector), one carrier re-assembled, and
the one-cusp control with its bite (backgrounds do exist where they should).
"""
import hashlib
import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1442_the_two_generation_backgrounds"
V = ARC / "verification"
sys.path.insert(0, str(V))
snappy = pytest.importorskip("snappy")


def _rows():
    out = []
    for i in range(6):
        out += json.loads((V / f"backgrounds_{i}.json").read_text())
    return out


def test_the_seal_is_the_file_that_was_sealed():
    hashes = (ARC / "ARTIFACT_HASHES.txt").read_text()
    assert hashlib.sha256((ARC / "PREREGISTRATION.md").read_bytes()).hexdigest() in hashes
    for name in ("backgrounds_mc.py", "read_backgrounds.py"):
        assert hashlib.sha256((V / name).read_bytes()).hexdigest() in hashes, f"{name} changed after the seal"


def test_the_seventeen_and_the_reading():
    import read_backgrounds
    r = _rows()
    assert len(r) == 17 and len({o["tag"] for o in r}) == 17
    assert all(o["max_abs_I"] == 2 for o in r)                    # they are B1441's carriers: a module does count two
    s = read_backgrounds.read(str(V))
    assert s["predictions"] == dict(G1=False, G2=False, G3=False, G4=False, G5=True)
    assert s["backgrounds"] == 32 and s["carriers_with_count_two"] == []
    assert json.loads(json.dumps(s)) == json.loads((ARC / "backgrounds_summary.json").read_text())
    assert read_backgrounds.read(str(V)) == s


def test_only_one_carrier_has_any_background():
    with_bg = [o for o in _rows() if o["backgrounds"]]
    assert [o["tag"] for o in with_bg] == ["m009 deg 6 #25"]
    assert with_bg[0]["by_count"] == {"-1": 16, "1": 16} and with_bg[0]["N"] == 8
    assert sum(1 for o in _rows() if o["N"] == 2) == 9


def test_the_order_two_lemma():
    """for exponent two: alpha_Q + alpha_L = l (additively), so the dual of the Q sector is the L sector"""
    import itertools
    SECT = [("Q", 1, 3), ("uc", -4, 3), ("ec", 6, 3), ("dc", 2, 1), ("L", -3, 1), ("nuc", 0, -5)]
    for th, pY, W in itertools.product(range(2), repeat=3):       # one coordinate of a character of order two
        l = (2 * th - W) % 2
        al = {lab: (th + pY * sy + W * ((sg - 1) // 2)) % 2 for lab, sy, sg in SECT}
        assert (al["Q"] + al["L"]) % 2 == l
    # and it is special to exponent two: at exponent four the identity fails for some data
    bad = 0
    for th, pY, W in itertools.product(range(4), repeat=3):
        l = (2 * th - W) % 4
        if ((th + pY + W) + (th - 3 * pY)) % 4 != l: bad += 1
    assert bad > 0


def test_one_carrier_live_and_the_control_bites():
    import backgrounds_mc as bm
    import several_cusps as sc
    r = bm.backgrounds(sc.get("m009", 6, 21))                     # three cusps, sign characters
    assert r["cusps"] == 3 and r["max_abs_I"] == 2 and r["backgrounds"] == 0
    c = bm.backgrounds(snappy.Manifold("m004").covers(3, cover_type="cyclic")[0])
    assert c["backgrounds"] == 48 and c["by_count"] == {"-1": 24, "1": 24}      # the instrument does find backgrounds
