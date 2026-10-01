"""B1440 lock -- the rank bound |I(V)| <= min(r, n - r) on once-punctured-torus bundles.

Live: random triangular modules of rank 2..6, their sums and exterior squares, each inequality of the proof checked
separately; the two-step formula against the index code; the bound attained; and the bite (a false bound fails).
"""
import json
import pathlib
import random
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
V = ROOT / "frontier" / "B1440_the_rank_bound" / "verification"
sys.path.insert(0, str(V))


def test_the_bound_holds_live_and_is_attained():
    import rank_bound as rb
    tab, two = rb.run(seed=11, per_rank=12, quiet=True)
    assert not any("FAILS" in k for k in list(tab) + list(two))
    assert sum(v for k, v in tab.items() if k.endswith("holds")) > 200
    assert two["two-step formula holds"] > 50
    for n, m in ((2, 1), (3, 1), (4, 2), (5, 2)):
        assert tab["triangular rank %d: max |I|" % n] <= m


def test_the_record():
    r = json.loads((V / "rank_bound.json").read_text())
    assert r["holds"] is True
    t = r["table"]
    assert [t["triangular rank %d: max |I|" % n] for n in (2, 3, 4, 5, 6)] == [1, 1, 2, 2, 3]
    assert all(t["triangular rank %d: bound attained" % n] > 0 for n in (2, 3, 4, 5, 6))
    assert not any("FAILS" in k for k in t)


def test_rank_five_never_reaches_three_and_rank_six_does():
    """the sentence the arc is for"""
    r = json.loads((V / "rank_bound.json").read_text())["table"]
    assert r["triangular rank 5: max |I|"] == 2 and r["direct sum rank 5: max |I|"] == 2
    assert r["triangular rank 6: max |I|"] == 3


def test_the_bite_a_tighter_bound_is_false():
    """|I| <= min(r, n - r) - 1 fails on modules that attain the bound: the check can fail"""
    import rank_bound as rb
    from modules import Level, build, index
    random.seed(3)
    L = Level(1, "LR", 2)
    nt = [c for c in L.chars if c != (0, 0, 0)]
    attained = 0
    for _ in range(200):
        chars = [random.choice(nt) for _ in range(2)]
        Vm = build(L, chars, {(0, 1): 1})
        if Vm is None:
            continue
        I, d1, d2 = index(Vm, L.Lr, L.Lmu, L.Llam)
        r = rb.rk_lambda(Vm, L)
        if d1[0] == 0 and d2[0] == 0 and I != 0:
            assert abs(I) == min(r, 2 - r) == 1
            attained += 1
    assert attained > 0


def test_the_sealed_instrument_it_builds_on_is_unchanged():
    import hashlib
    arc = ROOT / "frontier" / "B1435_the_interaction_census"
    h = (arc / "ARTIFACT_HASHES.txt").read_text()
    assert hashlib.sha256((arc / "verification" / "relcup.py").read_bytes()).hexdigest() in h
