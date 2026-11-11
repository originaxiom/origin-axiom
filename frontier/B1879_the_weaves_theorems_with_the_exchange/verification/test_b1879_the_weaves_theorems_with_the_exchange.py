"""B1879 -- the tick's fixed characters and the walk's law recomputed with this file's own code; the sealed run says what the
findings quote."""
import fractions
import itertools
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
RUN = (HERE / "weave_with_the_exchange_run.txt").read_text(encoding="utf-8")
FINDINGS = (HERE.parent / "FINDINGS.md").read_text(encoding="utf-8")


def test_the_tick_alone_fixes_exactly_two_characters():
    """a fixed character of (x, y, z) -> (z, x, xz - y) has z = x and x = y, so all three are one number t with t*t - t = t.
    Checked here over a grid of integers and half-integers, and the two solutions verified; the algebra is the proof."""
    tick = lambda v: (v[2], v[0], v[0] * v[2] - v[1])
    grid = [fractions.Fraction(k, 2) for k in range(-12, 13)]
    fixed = [v for v in itertools.product(grid, repeat=3) if tick(v) == v]
    assert fixed == [(0, 0, 0), (2, 2, 2)]
    # the two moves, each alone, fix a curve: many grid points
    m1 = lambda v: (v[2], v[1], v[2] * v[1] - v[0])
    m2 = lambda v: (v[0], v[2], v[0] * v[2] - v[1])
    assert len([v for v in itertools.product(grid, repeat=3) if m1(v) == v]) > 10
    both = [v for v in itertools.product(grid, repeat=3) if m1(v) == v and m2(v) == v]
    assert both == [(0, 0, 0), (2, 2, 2)]
    # the tick done twice fixes more than those two (the root's curve)
    twice = [v for v in itertools.product(grid, repeat=3) if tick(tick(v)) == v]
    assert len(twice) > 2 and (0, 0, 0) in twice
    # every one of these maps keeps the commutator's trace
    kappa = lambda v: v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2] - 2
    assert all(kappa(tick(v)) == kappa(v) for v in itertools.product(grid[::4], repeat=3))


def test_the_runs_have_the_same_law_in_both_grammars():
    n = 10
    def runs_lr(w):
        out, k = [], 1
        for a, b in zip(w, w[1:]):
            if a == b: k += 1
            else: out.append(k); k = 1
        return tuple(out[:2])
    def runs_lf(w):
        out, k = [], 1
        for ch in w:
            if ch == "F": out.append(k); k = 1
            else: k += 1
        return tuple(out[:2])
    def law(alphabet, runs):
        cnt = {}
        for t in itertools.product(alphabet, repeat=n):
            r = runs("".join(t))
            if len(r) == 2: cnt[r] = cnt.get(r, 0) + 1
        return {k: fractions.Fraction(v, 2 ** n) for k, v in cnt.items()}
    a, b = law("LR", runs_lr), law("LF", runs_lf)
    fit = [k for k in a if sum(k) <= n - 1]
    assert len(fit) == 36 and all(a[k] == b[k] == fractions.Fraction(1, 2 ** sum(k)) for k in fit)


def test_the_sealed_run_and_the_findings():
    for s in ("ALL CHECKS PASS", "the tick alone fixes exactly [(0, 0, 0), (2, 2, 2)]", "the two acts: 96 elements, two pieces", "with the exchange: 192 elements, one piece",
              "E4 IS NOT WELL POSED", "indicator twisted by the exchange is +1.000", "on all 165 triples that fit", "number of ends [1]",
              "the tick fixes no point of the upper half-plane"):
        assert s in RUN, s
    for s in ("The repo sweep:", "**What changes is one thing: the hand.**", "It decides nothing; it says what each decision costs.",
              "and it is main's suggestion, not a result", "the index itself is not recomputed here",
              '> "A condition to derive (Recommended)"', "it supplies no hand"):
        assert s in FINDINGS, s
