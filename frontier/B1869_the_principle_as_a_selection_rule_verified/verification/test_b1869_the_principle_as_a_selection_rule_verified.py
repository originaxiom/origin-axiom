"""B1869 -- the enumeration's decisive rows are recomputed here at smaller bounds, with the arc's own functions and with this
file's own independent count; the sealed run says what the findings quote."""
import importlib.util
import itertools
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("b1869_nc_on_main", HERE / "nc_on_main.py")
nc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nc)
RUN = (HERE / "nc_on_main_run.txt").read_text(encoding="utf-8")


def _least(rows, key=0):
    v = min(r[key] for r in rows)
    return v, sorted(r[2] for r in rows if r[key] == v)


def test_the_golden_background_at_its_own_level():
    hits, count = nc.run(1, {"5": [5]}, 12)
    assert count == 2 ** 10                                              # every departure of at most 12 letters
    assert _least(hits[("whole level, sign +", "5")]) == (6, [(6,)])
    plus = hits[("whole level, sign +", "5")]
    anysign = hits[("whole level, any sign by level", "5")]
    minus = [r for r in anysign if r not in plus]
    assert _least(minus) == (10, [(2, 2, 1, 5), (3, 4, 3), (5, 1, 2, 2)])
    assert _least(hits[("the line", "5")]) == (6, [(2, 2, 2), (6,)])
    assert (len(plus), len(minus), len(hits[("the line", "5")]) - len(anysign)) == (8, 9, 77)
    assert _least(plus, key=1)[0] == 5                                   # by extra letters the run of 6 is not alone
    assert len(_least(plus, key=1)[1]) > 1


def test_the_rule_is_empty_in_the_level():
    """at any single level N the least is the single run of N + 1: the pick is the level that was put in"""
    for N in (2, 3, 4, 5, 7, 11):
        hits, _ = nc.run(1, {"N": [N]}, N + 2)
        assert _least(hits[("whole level, sign +", "N")]) == (N + 1, [(N + 1,)]), N
    # the control: at level 5 the run of 5 and the run of 7 are detected
    hits, _ = nc.run(1, {"5": [5]}, 7)
    seen = {r[2] for r in hits[("whole level, any sign by level", "5")]}
    assert (5,) not in seen and (7,) not in seen and (6,) in seen


def test_the_other_backgrounds_give_no_single_run():
    hs, _ = nc.run(2, {"own": [8]}, 10)
    assert _least(hs[("whole level, sign +", "own")]) == (10, [(1, 2, 1, 2, 1, 2, 1), (10,)])
    assert _least(hs[("the line", "own")]) == (4, [(1, 2, 1)])
    hb, _ = nc.run(3, {"own": [13]}, 13)
    v, best = _least(hb[("whole level, sign +", "own")])
    assert v == 13 and len(best) == 4 and (16,) not in best
    assert all((b * b + 4) % own == 0 for b, own in ((1, 5), (2, 8), (3, 13)))


def test_an_independent_count_of_the_allowed_set():
    """this file's own enumeration, by brute force over compositions with numpy-free 2x2 integer products: the same counts to 10 letters"""
    def mul(X, Y): return (X[0] * Y[0] + X[1] * Y[2], X[0] * Y[1] + X[1] * Y[3], X[2] * Y[0] + X[3] * Y[2], X[2] * Y[1] + X[3] * Y[3])
    def D(runs):
        M = (1, 0, 0, 1)
        for i, r in enumerate(runs):
            M = mul(M, (1, r, 0, 1) if i % 2 == 0 else (1, 0, r, 1))
        return M
    def comps(n):
        for cuts in itertools.product((0, 1), repeat=n - 1):
            out, run = [], 1
            for c in cuts:
                if c:
                    out.append(run)
                    run = 1
                else:
                    run += 1
            out.append(run)
            yield tuple(out)
    plus = minus = 0
    for n in range(2, 11):
        for S in comps(n):
            if S[0] == 1 or S[-1] == 1:
                continue
            g = D((1,) * len(S))
            E = mul(D(S), (g[3], -g[1], -g[2], g[0]))
            if all((a - b) % 5 == 0 for a, b in zip(E, (1, 0, 0, 1))): plus += 1
            if all((a + b) % 5 == 0 for a, b in zip(E, (1, 0, 0, 1))): minus += 1
    hits, _ = nc.run(1, {"5": [5]}, 10)
    p = hits[("whole level, sign +", "5")]
    a = hits[("whole level, any sign by level", "5")]
    assert (plus, minus) == (len(p), len(a) - len(p)) and plus >= 1 and minus == 3


def test_the_sealed_run_says_what_the_findings_quote():
    for s in ("GOLDEN: 262144 departures with at most 20 letters", "whole level, sign +              6: 1 departure (6,); next 11",
              "the line                         6: 2 departures (2,2,2) (6,); next 7",
              "whole level, sign +              18: 2 departures (2,2,2,2,1,1,4,4) (4,4,1,1,2,2,2,2)",
              "to 12 letters at level 5: 8 with E = +1, 9 with E = -1, 77 more that fix the line only",
              "whole level, sign +              10: 2 departures (1,2,1,2,1,2,1) (10,); next 12",
              "the single run (16,) has 16 letters and is +1 at level 13: True"):
        assert s in RUN, s
    f = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("The repo sweep:", "Main read the seat's result before enumerating", "the run\n  of 6 comes out because 5 goes in"):
        assert s in f, s
