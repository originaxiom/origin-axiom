"""B1881 lock -- the web seat's two relays of 2026-11-11, verified on main.

What could fail here: a check of the sealed run not holding; the run not being what the script gives today (three facts are
recomputed from scratch, by other code than the script's); the arc claiming more than a criterion for what it calls main's reading.

ADDED 2026-11-12, after a second reading of Review 79's mends by a session that did not write them.  That reading found that this
lock held two of the nine mends and that the other seven could be undone with every test passing.  The five tests at the end hold
them: what the second convention is, computed on all 120 matrices with a mark for which the statement fails; that no check of the
script is passed a constant, with two planted lines the scan must report; the three counts of run sequences by a second method;
the short-gap figure in exact arithmetic; and that each correction stands in the paragraph of the sentence it corrects."""
import ast
import importlib.util
import itertools
import json
import math
import pathlib
import re
from fractions import Fraction as Fr

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
ARC = HERE.parent
RES = json.loads((HERE / "whole_and_value_on_main.json").read_text(encoding="utf-8"))
RUN = (HERE / "whole_and_value_on_main_run.txt").read_text(encoding="utf-8")


def test_every_check_of_the_sealed_run_holds():
    checks = {k: v for k, v in RES.items() if isinstance(v, bool)}
    assert len(checks) == 65 and all(checks.values()), [k for k, v in checks.items() if not v]
    assert "CHECKS: 65, FAILING: 0" in RUN and "[FAILS]" not in RUN
    for e in range(1, 13):
        assert any(k.startswith("E%d " % e) for k in checks), e           # each of the twelve expectations has a check


def test_the_ten_points_recomputed():
    """j(tau) = j(5 tau) in the coordinate t: the factorisation, and that every root has |t|^2 = 125"""
    t = sp.symbols("t")
    poly = sp.expand((t ** 2 + 250 * t + 3125) ** 3 - t ** 4 * (t ** 2 + 10 * t + 5) ** 3)
    want = -(t ** 2 - 125) * (t ** 2 + 22 * t + 125) * (t ** 2 + 4 * t + 125) * (t ** 2 + 18 * t + 125) * (t ** 2 - 14 * t + 125)
    assert sp.expand(poly - want) == 0 and sp.degree(poly, t) == 10
    for b in (22, 4, 18, -14):
        assert b * b < 500                                    # complex roots, with product 125: on the circle
    assert RES["A_numbers"]["j_at_the_ten_points"]["t**2 + 22*t + 125"] == ["1728"]
    assert sorted(int(v[0]) for k, v in RES["A_numbers"]["j_at_the_ten_points"].items() if len(v) == 1) == [-884736, -32768, 1728, 287496]


def test_the_two_quotients_recomputed():
    """index, cusp widths and elliptic points, by a count written apart from the script's: orbits of matrices mod 5"""
    def mul(A, B):
        return ((A[0] * B[0] + A[1] * B[2]) % 5, (A[0] * B[1] + A[1] * B[3]) % 5, (A[2] * B[0] + A[3] * B[2]) % 5, (A[2] * B[1] + A[3] * B[3]) % 5)
    S, T, I = (0, 4, 1, 0), (1, 1, 0, 1), (1, 0, 0, 1)
    grp, todo = {I}, [I]
    while todo:
        g = todo.pop()
        for h in (mul(g, S), mul(g, T)):
            if h not in grp:
                grp.add(h); todo.append(h)
    assert len(grp) == 120                                    # SL2 mod 5
    v = (1, 3)
    img = lambda g: ((v[0] * g[0] + v[1] * g[2]) % 5, (v[0] * g[1] + v[1] * g[3]) % 5)
    pm = [g for g in grp if img(g) in ((1, 3), (4, 2))]
    ln = [g for g in grp if img(g) in ((1, 3), (2, 1), (3, 4), (4, 2))]
    assert (len(pm), len(ln)) == (10, 20)                     # index 12 and 6 in the 120 (B1872's 10 and 20 of 120)
    assert 120 // len(pm) == 12 == RES["A_numbers"]["quotient_one_twin"][0] and 120 // len(ln) == 6 == RES["A_numbers"]["quotient_line"][0]
    assert RES["A_numbers"]["quotient_one_twin"][1:] == [[1, 1, 5, 5], 0, 0, "0"] and RES["A_numbers"]["quotient_line"][1:] == [[1, 5], 2, 0, "0"]
    # REMOVED 2026-11-12 (Review 79; found by a second reading): a line stood here that added typed fractions to zero and called
    # it the genus.  It could not fail.  The genus is computed below from the cusps and elliptic points that are counted.
    # ADDED 2026-11-12 (Review 79).  The docstring promised the cusp widths and the elliptic points "by a count written apart", and
    # the lines above compare them with the committed file and do arithmetic on typed numbers.  Here they are counted: the cosets of
    # each group are the 12 vectors up to sign and the 6 lines; a cusp is a cycle of T on them, its width the cycle's length; an
    # elliptic point of order 2 or 3 is a coset fixed by S or by ST.  The genus is then computed from what was counted.
    def act(g, w):
        return ((w[0] * g[0] + w[1] * g[2]) % 5, (w[0] * g[1] + w[1] * g[3]) % 5)
    vecs = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]
    up_to_sign = sorted({min(w, ((-w[0]) % 5, (-w[1]) % 5)) for w in vecs})
    line_of = lambda w: min(((w[0] * u) % 5, (w[1] * u) % 5) for u in range(1, 5))
    lines = sorted({line_of(w) for w in vecs})
    assert (len(up_to_sign), len(lines)) == (12, 6)
    ST = mul(S, T)

    def census(points, canon):
        seen, widths = set(), []
        for p0 in points:
            if p0 in seen:
                continue
            n, q = 0, p0
            while True:
                seen.add(q); n += 1; q = canon(act(T, q))
                if q == p0:
                    break
            widths.append(n)
        e2 = sum(1 for p0 in points if canon(act(S, p0)) == p0)
        e3 = sum(1 for p0 in points if canon(act(ST, p0)) == p0)
        genus = Fr(1) + Fr(len(points), 12) - Fr(e2, 4) - Fr(e3, 3) - Fr(len(widths), 2)
        return sorted(widths), e2, e3, genus
    sign = lambda w: min(w, ((-w[0]) % 5, (-w[1]) % 5))
    assert census(up_to_sign, sign) == ([1, 1, 5, 5], 0, 0, 0) and census(lines, line_of) == ([1, 5], 2, 0, 0)
    assert list(census(up_to_sign, sign)[:3]) == RES["A_numbers"]["quotient_one_twin"][1:4] and list(census(lines, line_of)[:3]) == RES["A_numbers"]["quotient_line"][1:4]


def test_a_run_keeps_the_line_exactly_when_it_is_one_mod_five_recomputed():
    def keeps(n, g):
        W = (1, 0, 0, 1)
        runs = [n] + [1] * (2 * g + 1)
        for k, r in enumerate(runs):
            M = (1, 0, r % 5, 1) if k % 2 == 0 else (1, r % 5, 0, 1)
            W = ((W[0] * M[0] + W[1] * M[2]) % 5, (W[0] * M[1] + W[1] * M[3]) % 5, (W[2] * M[0] + W[3] * M[2]) % 5, (W[2] * M[1] + W[3] * M[3]) % 5)
        u = ((1 * W[0] + 3 * W[2]) % 5, (1 * W[1] + 3 * W[3]) % 5)
        return u in ((1, 3), (2, 1), (3, 4), (4, 2))
    for n, g in itertools.product(range(1, 31), range(0, 4)):
        assert keeps(n, g) == (n % 5 == 1), (n, g)
    b = RES["B_numbers"]
    assert b["own"] == {"(6)": "3.61803398875", "(11)": "6.11803398875", "(2,1,2,1,2)": "1.72360679775"}
    assert b["rate"][:8] == b["four_ln_phi"][:8] == "1.924847" and b["phi4"].startswith("6.854101")
    assert b["conventions"] == {"agree": 47988, "differ": 0, "differ_against_reversed": 0, "differ_against_rotated": 8366, "first_difference": None}
    assert b["A_then_B_apex_by_gap"]["1"] == "A" and all(b["A_then_B_apex_by_gap"][str(g)] == "B" for g in range(2, 13))


def test_the_arc_says_what_it_is_and_what_it_is_not():
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for s in ("## Seen first", "## Disclosed", "## Reproduce", "0 of 19", "main's reading; a criterion, not a result", "Nothing is selected",
              "Three of main's own checks failed on the first run, and none of the seat's facts", "main's safeguard, which is main's wording and not the owner's"):
        assert s in f, s
    v = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["id"] == "B1881" and v["verdict"] == "PROVED" and "main's reading and not a result" in v["claim_one_line"] and v["claim_one_line"].endswith("0 of 19.")
    # no value of the modulus on record is named in the arc: the script reads no other arc's output
    src = (HERE / "whole_and_value_on_main.py").read_text(encoding="utf-8")
    assert "frontier/" not in src and "open(" not in src.replace("write_text", "")
    led = (ROOT / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8")
    assert "WHAT_SYMMETRY_ALLOWS_A_STATE_OF_THE_WHOLE" in led and "THE_READ_OUT_AS_A_VALUE" in led and "`8ff3f7e5`" in led


# ---------------------------------------------------------------------------------------------- added 2026-11-12
def _mul5(A, B):
    return ((A[0] * B[0] + A[1] * B[2]) % 5, (A[0] * B[1] + A[1] * B[3]) % 5, (A[2] * B[0] + A[3] * B[2]) % 5, (A[2] * B[1] + A[3] * B[3]) % 5)


def _sl2_mod_5():
    S, T, I = (0, 4, 1, 0), (1, 1, 0, 1), (1, 0, 0, 1)
    grp, todo = {I}, [I]
    while todo:
        g = todo.pop()
        for h in (_mul5(g, S), _mul5(g, T)):
            if h not in grp:
                grp.add(h); todo.append(h)
    return grp


_J = (0, 1, 1, 0)                                                              # the swap of the two coordinates


def _swap(g):
    return _mul5(_mul5(_J, g), _J)


def _tr(g):
    return (g[0], g[2], g[1], g[3])


def _row(v, g):
    return ((v[0] * g[0] + v[1] * g[2]) % 5, (v[0] * g[1] + v[1] * g[3]) % 5)


def _col(g, v):
    return ((g[0] * v[0] + g[1] * v[1]) % 5, (g[2] * v[0] + g[3] * v[1]) % 5)


def _line(w):
    return min(((k * w[0]) % 5, (k * w[1]) % 5) for k in (1, 2, 3, 4))


_VECS = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]


def _annihilated(v):
    """the lines of columns u with v . u = 0 modulo 5"""
    return {_line(u) for u in _VECS if (v[0] * u[0] + v[1] * u[1]) % 5 == 0}


def _the_script():
    spec = importlib.util.spec_from_file_location("b1881_whole_and_value_on_main", HERE / "whole_and_value_on_main.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)                                               # definitions only: the run is under __main__
    return mod


def test_the_second_convention_is_the_first_conjugated_by_the_swap_and_the_two_tests_are_one_test():
    """A mend of Review 79 called the arc's second convention the transpose of the seat's.  What it is, computed.  How this could
    fail: the script's second function being another test than 'the column J u on J W J'; the identity failing on some matrix;
    the control, a mark that does not annihilate its own line, agreeing everywhere."""
    mod = _the_script()
    grp = _sl2_mod_5()
    assert len(grp) == 120
    kept_row = lambda v, g: _line(_row(v, g)) == _line(v)
    kept_col = lambda g, u: _line(_col(g, u)) == _line(u)
    V = mod.V                                                                  # the mark, read from the script
    # the mark annihilates one line of columns, and it is the mark's own line; the swap of it is the second mark
    assert _annihilated(V) == {_line(V)}
    second = _line(_col(_J, _line(V)))
    assert second == (1, 2) and second != _line(V)
    # the ground: symmetric, so its transpose is itself, and the second ground is another matrix
    G = _mul5((1, 0, 1, 1), (1, 1, 0, 1))
    assert _row(V, G) == ((-V[0]) % 5, (-V[1]) % 5)                            # it is the ground: it sends the mark to minus itself
    assert _tr(G) == G and _swap(G) == (2, 1, 1, 1) and _swap(G) != _tr(G)
    assert _col(_swap(G), second) == ((-second[0]) % 5, (-second[1]) % 5)
    # the script's two functions are these two tests, on every run sequence of length 2 and 4 with runs to 6
    reached, differ_from_transpose, tests_differ_from_transpose = set(), 0, 0
    for n in (2, 4):
        for seq in itertools.product(range(1, 7), repeat=n):
            W = (1, 0, 0, 1)
            for k, r in enumerate(seq):
                W = _mul5(W, (1, 0, r % 5, 1) if k % 2 == 0 else (1, r % 5, 0, 1))
            reached.add(W)
            assert mod.keeps_line_seat(list(seq)) == kept_row(V, W), seq
            assert mod.keeps_line_main(list(seq)) == kept_col(_swap(W), second), seq                 # the swap, the order of the letters kept
            assert mod.keeps_line_main(list(seq)[::-1]) == kept_col(_swap(_tr(W)), second), seq      # reversed: the transpose, then the swap
            differ_from_transpose += _swap(W) != _tr(W)
            tests_differ_from_transpose += kept_col(_swap(W), second) != kept_col(_tr(W), second)
    assert reached == grp                                                      # the words reach the whole group, so nothing above is on a part of it
    assert differ_from_transpose > 0 and tests_differ_from_transpose > 0       # and 'the transpose' would have been another word and another test
    # why the two agree: a row is kept by a matrix exactly when the column it annihilates is kept.  All 120, each of the six lines.
    lines = sorted({_line(w) for w in _VECS})
    assert len(lines) == 6
    for v in lines:
        (u,) = _annihilated(v)
        assert all(kept_row(v, g) == kept_col(g, u) for g in grp), v
        assert all(kept_row(v, g) == kept_col(_tr(g), v) for g in grp), v     # the transpose proper, for any mark
    assert sum(kept_row(V, g) == kept_col(_swap(g), second) for g in grp) == 120
    # the control: (1, 1) does not annihilate its own line, and the same recipe, the swapped mark on the swapped matrix, is another test
    c = (1, 1)
    assert _annihilated(c) != {_line(c)}
    assert sum(kept_row(c, g) == kept_col(_swap(g), _line(_col(_J, c))) for g in grp) == 88
    # the page's numbers
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "on all 120 matrices of determinant 1 modulo 5, for each of the six lines" in f and "for (1, 1) the two agree on 88 of the 120" in f


def _constant_checks(src):
    """lines of a script where check() is passed a constant, or a name bound once to a constant, or RES[...] is assigned one"""
    tree = ast.parse(src)
    bound = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            bound.setdefault(node.targets[0].id, []).append(node.value)
    constant_names = {k for k, vals in bound.items() if len(vals) == 1 and isinstance(vals[0], ast.Constant)}

    def is_constant(e):
        return isinstance(e, ast.Constant) or (isinstance(e, ast.Name) and e.id in constant_names)
    out, calls = [], 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "check":
            calls += 1
            if len(node.args) < 2 or is_constant(node.args[1]):
                out.append(node.lineno)
        if isinstance(node, ast.Assign) and any(isinstance(t_, ast.Subscript) and isinstance(t_.value, ast.Name) and t_.value.id == "RES" for t_ in node.targets):
            if is_constant(node.value):
                out.append(node.lineno)
    return sorted(out), calls


def test_no_check_of_the_script_is_passed_a_constant():
    """Review 79 found two checks that were passed the literal True and counted among the 65.  Both are computed now, and until
    this test nothing held that.  The scan is shown to report two planted lines."""
    src = (HERE / "whole_and_value_on_main.py").read_text(encoding="utf-8")
    found, calls = _constant_checks(src)
    assert found == [], found
    assert calls >= 60, calls                                                  # the scan saw the script's checks (the 65 include some set in loops)
    planted = 'ok = True\ncheck("the mirror normalises the group", True, "by hand")\ncheck("increase without bound", ok)\nRES["a third"] = True\nx = f()\ncheck("computed", x)\n'
    assert _constant_checks(planted) == ([2, 3, 4], 3)
    # the two that were constants: each is computed from something that could come out otherwise
    assert "this check was passed the literal True" in src and src.count("this check was passed the literal True") == 2
    assert RES["the own values of the allowed single runs increase without bound: 5m/2 + sqrt5/2 for the run of 5m + 1"] is True


def test_the_three_counts_of_run_sequences_by_a_second_method():
    """The page corrected '16,275 cyclic run sequences' at Review 79 and the script's label kept it.  The script now counts by
    canonical forms; here the same three numbers by the orbit-counting formula, and the page and the run held to them."""
    as_written = sum(5 ** n for n in (2, 4, 6))
    every_rotation = sum(sum(5 ** math.gcd(n, j) for j in range(n)) // n for n in (2, 4, 6))
    even_rotations = sum(sum(5 ** math.gcd(n, j) for j in range(0, n, 2)) // (n // 2) for n in (2, 4, 6))
    assert all(sum(5 ** math.gcd(n, j) for j in range(n)) % n == 0 for n in (2, 4, 6))
    assert RES["B_counts"] == {"sequences_as_written": as_written, "up_to_every_rotation": every_rotation, "up_to_rotations_that_keep_the_letters": even_rotations}
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    for n in (as_written, every_rotation, even_rotations):
        assert format(n, ",") in f, n
    label = [k for k in RES if k.startswith("the least apex over every run sequence")]
    assert len(label) == 1 and all(str(n) in label[0] for n in (as_written, every_rotation, even_rotations)) and RES[label[0]] is True
    assert not any("every cyclic run sequence" in k for k in RES) and "every cyclic run sequence" not in RUN


def test_the_short_gap_figure_in_exact_arithmetic():
    """Review 79 found that a mended check, said to ask what the relay says, asked for a figure main had typed.  It asks for both
    now.  Here the figure itself, from integer matrices and exact square roots: the run of 6 closed by one golden period."""
    def apex(runs):
        best = None
        for i in range(len(runs)):
            W = (1, 0, 0, 1)
            for k in range(len(runs)):
                r = runs[(i + k) % len(runs)]
                M = (1, r, 0, 1) if k % 2 == 0 else (1, 0, r, 1)
                W = (W[0] * M[0] + W[1] * M[2], W[0] * M[1] + W[1] * M[3], W[2] * M[0] + W[3] * M[2], W[2] * M[1] + W[3] * M[3])
            h = sp.sqrt((W[0] + W[3]) ** 2 - 4) / (2 * abs(W[2]))
            best = h if best is None or sp.N(h - best, 30) > 0 else best
        return best
    own = lambda n: sp.Rational(n - 1, 2) + sp.sqrt(5) / 2
    for n, percent, shown in ((6, "0.92", "3.6515"), (11, "0.65", None)):
        a = apex([n, 1, 1, 1])
        off = sp.N((a - own(n)) / own(n) * 100, 30)
        assert "%.2f" % float(off) == percent, (n, off)
        if shown:
            assert str(sp.N(a, 5)) == shown and sp.Rational(9, 10) < off < 1       # what the relay calls nearly one percent
            assert sp.simplify(a - 2 * sp.sqrt(30) / 3) == 0
    assert str(sp.N(own(6), 12)) == RES["B_numbers"]["own"]["(6)"] and str(sp.N(own(11), 12)) == RES["B_numbers"]["own"]["(11)"]
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    assert "reads 3.6515, 0.92 percent above its own value; (11) is 0.65 percent off" in f
    assert any(k.startswith("E11 (6) with one period on both sides reads 3.6515 against 3.6180, nearly one percent (0.92); (11) is 0.65 percent off") and v is True for k, v in RES.items())
    # and the script's own check asks for both: main's figure, and that it lies where the relay puts it.  Its condition is read here.
    src = (HERE / "whole_and_value_on_main.py").read_text(encoding="utf-8")
    calls = [n for n in ast.walk(ast.parse(src)) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "check"
             and isinstance(n.args[0], ast.Constant) and str(n.args[0].value).startswith("E11 (6) with one period on both sides")]
    assert len(calls) == 1
    cond = ast.get_source_segment(src, calls[0].args[1])
    assert '== "0.92"' in cond and 'mp.mpf("0.9") < (one6 - own["(6)"]) / own["(6)"] * 100 < 1' in cond and '== "0.65"' in cond


def _paragraphs(text):
    return [b for b in re.split(r"\n\s*\n", text) if b.strip()]


def test_each_correction_stands_with_the_sentence_it_corrects():
    """The nine mends of Review 79 and the four of its second reading, on the page, in the verdict line and in the script.  A
    correction is looked for in the paragraph of the old sentence, or in the paragraph after it where it is a note of its own."""
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    paras = _paragraphs(f)
    pairs = (
        ("B1872 writes columns, the mark (1, 2)", "that is not B1872's convention", 0),                                 # SM-11
        ("is its transpose and is this arc's own", "It is not the transpose", 1),                                        # the second reading
        ("Main read both relays about ten hours after the first was pushed", "is about a re-audit that sat unread for eight hours", 0),   # SM-12
        ("The expectations were written before the run", "By the protocol's labels this arc is computed once", 0),      # SM-16
        ("this read \"cyclic run sequences\"", "up to rotation\n  they are 2,815", 0),                                 # SM-17
        ("this read \"is reproduced\"", "None of the seat's code was run", 0),                                          # the second reading
    )
    for old, correction, after in pairs:
        at = [i for i, b in enumerate(paras) if old in b]
        assert len(at) == 1, old
        assert correction in paras[at[0] + after], old
    for s in ("Three checks did not check what they said", "Two were passed the literal value true", "it now asks for both", "it\n  recomputes all three now",
              "Those mends were read on 2026-11-12 by a session that did not write them, and four things were found", "Main found two more while mending those"):
        assert s in f, s
    assert "is reproduced by main's own code" not in f
    c = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    for s in ("every printed number recomputed [CORRECTED 2026-11-12: this read 'reproduced'", "B1872's convention is the seat's, rows",
              "CORRECTED AGAIN the same day, found by a second reading of that note: it is not the transpose", "conjugated by the swap of the two coordinates",
              "an instance of an identity"):
        assert s in c, s
    assert "every printed number reproduced" not in c
    src = (HERE / "whole_and_value_on_main.py").read_text(encoding="utf-8")
    assert '"""B1872\'s convention' not in src and "this arc's second convention" in src and "[CORRECTED 2026-11-12, twice." in src
    assert "it is not the transpose either" in src and "things to be recomputed" in src and "is recomputed to its printed digits" in src
    # the check on the two conventions asks for both readings the page states, and not for any one of three
    tree = ast.parse(src)
    e12 = [n for n in ast.walk(tree) if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Subscript) and isinstance(n.value, ast.BoolOp)
           and any(isinstance(x, ast.Name) and x.id == "disagree" for x in ast.walk(n.value))]
    assert len(e12) == 1 and isinstance(e12[0].value.op, ast.And)
    assert RES["E12 the two conventions name one allowed set: no sequence differs as written, and none on the reversed sequence"] is True

