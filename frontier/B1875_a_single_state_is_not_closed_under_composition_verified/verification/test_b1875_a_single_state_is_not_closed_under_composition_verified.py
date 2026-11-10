"""B1875 -- the card's split and the triples' table recomputed with this file's own code; the sealed run says what the findings quote."""
import itertools
import math
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
RUN = (HERE / "closure_on_main_run.txt").read_text(encoding="utf-8")
FINDINGS = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")


def _c(runs):
    """for each run the lower-left entry of the word started there, that run's letter taken as the translation"""
    out = []
    for i in range(len(runs)):
        a, b, c, d = 1, 0, 0, 1
        for j, r in enumerate(runs[i:] + runs[:i]):
            if j % 2 == 0:
                b, d = b + r * a, d + r * c            # times L^r = [[1, r], [0, 1]]
            else:
                a, c = a + r * b, c + r * d            # times R^r = [[1, 0], [r, 1]]
        out.append(c)
    return out


def _places(runs):
    c = _c(runs)
    return sum(1 for x in c if x == min(c))


def _d6(k): return (6,) + (1,) * (2 * k + 1)
def _d2(k): return (2, 1, 2, 1, 2) + (1,) * (2 * k + 1)
SIX = [("6", _d6(k)) for k in (1, 2, 3)] + [("2", _d2(k)) for k in (1, 2, 3)]


def test_the_six_are_single_and_half_of_their_composites_are_not():
    assert all(_places(r) == 1 for _, r in SIX)
    same = [a + b for (ka, a), (kb, b) in itertools.product(SIX, SIX) if ka == kb]
    diff = [a + b for (ka, a), (kb, b) in itertools.product(SIX, SIX) if ka != kb]
    assert len(same) == 18 and all(_places(r) == 2 for r in same)
    assert len(diff) == 18 and all(_places(r) == 1 for r in diff)
    for r in diff:                                           # the apex is the run of 6, more than 1 above the next height
        c = _c(r)
        t = 0
        a, b, cc, d = 1, 0, 0, 1
        for j, x in enumerate(r):
            if j % 2 == 0: b, d = b + x * a, d + x * cc
            else: a, cc = a + x * b, cc + x * d
        disc = math.sqrt((a + d) ** 2 - 4)
        hs = sorted({disc / (2 * x) for x in c}, reverse=True)
        assert r[c.index(min(c))] == 6 and hs[0] - hs[1] > 1
    assert _places((1, 1)) == 2                              # LR itself is not single


def test_the_integer_form_is_the_continued_fraction():
    runs = _d2(2) + _d6(1)
    c = _c(runs)
    a, b, cc, d = 1, 0, 0, 1
    for j, x in enumerate(runs):
        if j % 2 == 0: b, d = b + x * a, d + x * cc
        else: a, cc = a + x * b, cc + x * d
    disc = math.sqrt((a + d) ** 2 - 4)
    n = len(runs)
    for i in range(n):
        x = y = 0.0
        for k in range(60, 0, -1):
            x = 1 / (runs[(i + k) % n] + x)
            y = 1 / (runs[(i - k) % n] + y)
        assert abs((runs[i] + x + y) / 2 - disc / (2 * c[i])) < 1e-9


def test_three_factors_and_the_ties_with_no_symmetry():
    table = {}
    for (ka, a), (kb, b), (kc, c) in itertools.product(SIX, SIX, SIX):
        key = (ka, kb, kc).count("6")
        table.setdefault(key, [0, 0, 0, 0])
        table[key][0] += 1
        table[key][_places(a + b + c)] += 1
    assert table == {1: [81, 81, 0, 0], 2: [81, 54, 27, 0], 3: [27, 15, 9, 3], 0: [27, 15, 9, 3]}
    assert [_places(_d6(1) + _d6(2) + _d2(k)) for k in (1, 2, 3)] == [1, 2, 1]
    for runs, want in (((1, 3, 1, 3, 4, 3), 72), ((2, 2, 1, 3, 3, 1, 1, 3), 196)):
        c = _c(runs)
        assert min(c) == want and c.count(want) == 2
    r = (2, 2, 1, 3, 3, 1, 1, 3)                             # no rotation and no reflection of the cyclic run sequence fixes it
    n = len(r)
    assert not any(all(r[(i + s) % n] == r[i] for i in range(n)) for s in range(1, n))
    assert not any(all(r[(s - i) % n] == r[i] for i in range(n)) for s in range(n))


def test_the_sealed_run_and_the_findings():
    for s in ("ALL CHECKS PASS", "15641 cyclic run sequences to 18 letters; in 16 the apex", "the 216 ordered triples: 165 single, 45 with the apex twice, 6 three times",
              "all 18 have twice as many isometries as the word has symmetries", "12 have 2 isometries, 6 have 4 isometries",
              "every other class is below 1", "180 of the 324 are single"):
        assert s in RUN, s
    for s in ("The repo sweep:", "**The seat's card holds in every cell.**", "It is a thread's property.", "| **all** | **216** | **165** | **45** | **6** |",
              "16 of the 15 641 cyclic run sequences to 18 letters", "Nothing is\n  computed on the hyperbolic metric."):
        assert s in FINDINGS, s
