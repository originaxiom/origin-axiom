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


def test_the_single_tick_is_the_only_short_history_that_fixes_exactly_the_two():
    """the advisor seat's sharper fact (2026-11-11), reproduced by main: recomputed here for the words to three letters, and
    read from the sealed run for all thirteen"""
    import importlib.util
    spec = importlib.util.spec_from_file_location("only_the_tick_b1879", HERE / "only_the_tick.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    assert len(m.classes(5)) == 13 and m.classes(3) == ["F", "FL", "FLL", "FFL"]
    assert m.fixed("F") == ("finite", {(2, 2, 2), (0, 0, 0)})
    kind, pts = m.fixed("FL")
    assert kind == "finite" and pts == {(2, 2, 2), (0, 0, 0), (-2, 2, -2)}
    assert m.fixed("FF")[0] == "positive dimension" and m.fixed("FLL")[0] == "positive dimension"
    run = (HERE / "only_the_tick_run.txt").read_text(encoding="utf-8")
    assert "exactly the two: F\n" in run and "a set of positive dimension: 11 of 13" in run
    assert "the tick alone is the only history of at most five letters that fixes exactly the two: True" in run


def test_the_script_is_run_again_and_says_the_same():
    """Added 2026-11-12 (Review 79).  The test above looks for the group's orders, the indicator, the number of ends and the tick's
    fixed set as lines of the committed run; only the walk's law and the short histories were recomputed in this lock.  A reader
    planted a wrong group count in the script: the script failed and this lock passed.  Here the script itself is run, its own
    assertions with it, and the lines are looked for in what it prints now."""
    import subprocess
    import sys
    args = [sys.executable, "-B", str(HERE / "weave_with_the_exchange.py")]
    try:
        import snappy                                                         # noqa: F401
        want_ends = True
    except ImportError:
        args.append("--no-snappy"); want_ends = False
    r = subprocess.run(args, capture_output=True, text=True, timeout=1800)
    assert r.returncode == 0, (r.stdout[-600:], r.stderr[-600:])
    fresh = r.stdout
    for s in ("ALL CHECKS PASS", "the tick alone fixes exactly [(0, 0, 0), (2, 2, 2)]", "the two acts: 96 elements, two pieces", "with the exchange: 192 elements, one piece",
              "indicator twisted by the exchange is +1.000", "on all 165 triples that fit", "the tick fixes no point of the upper half-plane",
              "the sixth root of unity 1/2 + i sqrt(3)/2 at their corners"):
        assert s in fresh and s in RUN, s
    assert (not want_ends) or "number of ends [1]" in fresh
    # and the corrections of that date stand on the page, each with what it replaced
    for s in ("Corrections of 2026-11-12 (Review 79)", "the walk's law of run lengths", "The measure itself is not shown unchanged", "this holds by construction",
              "is not among the\n  thirteen", "this read \"The square of the tick, which is the root, is one of the eleven.\"", "By the protocol's labels this arc is computed once",
              "main has neither read nor run them"):
        assert s in FINDINGS, s

