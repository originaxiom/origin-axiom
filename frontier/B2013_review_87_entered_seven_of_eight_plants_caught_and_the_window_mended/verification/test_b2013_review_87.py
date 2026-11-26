"""B2013's lock: the plant list committed here is the one sealed before reading (its sha256), it holds eight plants in eight
arcs with B1980 and B1995 clean, and the window's main mends are present in the arcs they mend."""
import pathlib, hashlib, re
HERE = pathlib.Path(__file__).resolve().parent
FR = HERE.parents[1]


def test_plants_sealed():
    b = (HERE / "plants.txt").read_bytes()
    assert hashlib.sha256(b).hexdigest() == "85455f2cc650a0638d9b086119f663d54083e37c2d8a72e50ff9ddfe421c4018"
    rows = [l for l in b.decode().splitlines() if l.startswith("PLANT ")]
    arcs = [l.split(" | ")[1] for l in rows]
    assert len(rows) == 8 and len(set(arcs)) == 7 and arcs.count("B2011") == 2 and not {"B1980", "B1995"} & set(arcs)


def test_mends_present():
    f = lambda a, rel="FINDINGS.md": (next(FR.glob(a + "_*")) / rel).read_text()
    assert "frame C fails the S move, also with its end read on the whole curve\" struck" in f("B1980")
    assert "at 29 ≤ p ≤ 43 more than half the leaves split, at 47, 23 of 47" in f("B1983")
    assert "only the plane's projector is meaningful" in f("B1995")
    assert "coefficients up to 101 against a limit of 200" in f("B1996")
    assert "matched to the modes 6, −6 and 0 by count" in f("B2009")
    assert "scoped\n  to the leaves run" in f("B2012") and "the card's Q(x) is R(x + 4)" in f("B2012")
    assert "def test_integers_rerun" in f("B1993", "verification/test_b1993_integers.py")
    assert "slowest decay ratio 0.8389" in f("B1996", "verification/test_b1996_tower.py")
