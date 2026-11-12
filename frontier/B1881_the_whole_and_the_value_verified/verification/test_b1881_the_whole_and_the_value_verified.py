"""B1881 lock -- the web seat's two relays of 2026-11-11, verified on main.

What could fail here: a check of the sealed run not holding; the run not being what the script gives today (three facts are
recomputed from scratch, by other code than the script's); the arc claiming more than a criterion for what it calls main's reading.

ADDED 2026-11-12, after a second reading of Review 79's mends by a session that did not write them.  That reading found that this
lock held two of the nine mends and that the other seven could be undone with every test passing.  The five tests at the end hold
them: what the second convention is, computed on all 120 matrices with a mark for which the statement fails; that no check of the
script is passed a constant, with two planted lines the scan must report; the three counts of run sequences by a second method;
the short-gap figure in exact arithmetic; and that each correction stands in the paragraph of the sentence it corrects.

ADDED 2026-11-12, a second time, after the same session planted 23 errors against the lock as it then stood: 17 were caught and
six passed.  The four tests at the end hold the six: the committed run is what the script gives today, by running it; the
conditions of the mended checks, word for word; that the script computes the counts it prints; and where the withdrawn word
stands.  One thing they cannot hold is said in the last of them.

ADDED 2026-11-12, a third time (Review 80), after a reader weakened the script five ways with its output unchanged and every
test passing; main made each again by a plant of its own.  The lock had read the script's text in places: two conditions,
the beginning of two expressions, the shape of one kind of `or`.  A weakening anywhere else passed.  The test after those
holds the script whole, by the digest of its bytes, so that any change to it is a change in two places."""
import ast
import hashlib
import importlib.util
import itertools
import json
import math
import os
import pathlib
import re
import subprocess
import sys
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
        # a table, a list, a tuple or a set written out counts as a constant when every entry of it is one (added 2026-11-12,
        # a second time: a plant typed three counts as a table of numbers, and the scan saw no constant)
        if isinstance(e, ast.Dict):
            return bool(e.values) and all(is_constant(v) for v in e.values)
        if isinstance(e, (ast.List, ast.Tuple, ast.Set)):
            return bool(e.elts) and all(is_constant(v) for v in e.elts)
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


# ---------------------------------------------------------------------------------------------- added 2026-11-12, a second time
# A session that did not write this lock planted 23 errors against it as it stood after B1895: 17 were caught and six passed.
# The four tests below hold the six.  What they cannot hold is said in the last of them.

def _run_the_script_in_a_copy(tmp_path, seed):
    """the arc's script, copied alone into an empty folder and run there: (its run file, its json), as bytes"""
    work = tmp_path / ("run_%s" % seed)
    work.mkdir()
    (work / "whole_and_value_on_main.py").write_bytes((HERE / "whole_and_value_on_main.py").read_bytes())
    env = {k: v for k, v in os.environ.items() if not k.startswith("OA_")}
    env["PYTHONHASHSEED"] = str(seed)
    r = subprocess.run([sys.executable, "-B", str(work / "whole_and_value_on_main.py")], cwd=str(work), env=env, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-600:]
    return (work / "whole_and_value_on_main_run.txt").read_bytes(), (work / "whole_and_value_on_main.json").read_bytes()


def _made_with():
    import mpmath
    return {"python": "%d.%d" % sys.version_info[:2], "mpmath": mpmath.__version__, "sympy": sp.__version__}


def _to_eight_digits(text):
    """a transcript with every decimal number given to eight significant digits: what must be the same under any version"""
    return [re.sub(r"\d+\.\d+(?:[eE][-+]?\d+)?", lambda m: "%.8g" % float(m.group(0)), line) for line in text.split("\n")]


def test_the_committed_run_is_what_the_script_gives_today(tmp_path):
    """The lock read three things of the committed run file: its last line, that no check fails, and that one old label is gone.
    A plant edited the file elsewhere and passed.  Here the script is run, twice, with two seeds of the hash, in a folder of its
    own.  About twenty seconds.

    WHERE THE LIBRARIES ARE THE ONES THE COMMITTED RUN WAS MADE WITH (a file beside the run records them), both outputs must be
    the committed files byte for byte.  The script's numbers are printed by arithmetic at a fixed number of digits and by exact
    algebra, not by the machine's floats, so the bytes do not depend on the machine; they can depend on the version of a
    library.  WHERE A VERSION DIFFERS the test does not skip and holds less: the same lines in the same order with every
    decimal number to eight digits, and the same checks, each holding, with the same counts.  A lock that compares as text
    what a process printed passes where it was written and can fail elsewhere: that is the class the enforcement package's
    fourth series names, and this test was of it for two hours."""
    made = json.loads((HERE / "whole_and_value_on_main_made_with.json").read_text(encoding="utf-8"))
    # ADDED 2026-11-12 (Review 80; a reader's finding F5, made again by main's plant).  The file that says which versions made
    # the run decides which of the two comparisons below is made, and nothing held it: given another version, it sent the run
    # to the weaker comparison on the very machine that made it.  It is held to what it says, so that a change is in two places.
    assert made == _MADE_WITH_AS_HELD, "the file that says which versions made the run is not the one this lock holds"
    same = made == _made_with()
    run0 = (HERE / "whole_and_value_on_main_run.txt").read_bytes()
    data0 = (HERE / "whole_and_value_on_main.json").read_bytes()
    for seed in (1, 2):
        run, data = _run_the_script_in_a_copy(tmp_path, seed)
        if same:
            assert run == run0, "the run file is not what the script gives (seed %d)" % seed
            assert data == data0, "the json is not what the script gives (seed %d)" % seed
        else:
            _held_under_another_version(run, data, run0, data0, seed)


_MADE_WITH_AS_HELD = {"python": "3.12", "mpmath": "1.3.0", "sympy": "1.14.0"}      # whole_and_value_on_main_made_with.json, as committed


def _values_to_eight_digits(v):
    """a value of the json with every decimal number in it given to eight significant digits; whole numbers and words as they are"""
    if isinstance(v, bool) or isinstance(v, int) or v is None:
        return v
    if isinstance(v, float):
        return "%.8g" % v
    if isinstance(v, str):
        return _to_eight_digits(v)[0] if "\n" not in v else _to_eight_digits(v)
    if isinstance(v, (list, tuple)):
        return [_values_to_eight_digits(x) for x in v]
    if isinstance(v, dict):
        return {k: _values_to_eight_digits(x) for k, x in v.items()}
    return v


def _held_under_another_version(run, data, run0, data0, seed):
    assert _to_eight_digits(run.decode("utf-8")) == _to_eight_digits(run0.decode("utf-8")), "the run differs by more than a last digit (seed %d)" % seed
    new, old = json.loads(data), json.loads(data0)
    assert list(new) == list(old), "the checks are not the same, or not in the same order (seed %d)" % seed
    assert all(new[k] == old[k] for k in old if isinstance(old[k], bool)) and new["B_counts"] == old["B_counts"]
    # ADDED 2026-11-12 (Review 80; a reader's finding F5).  The line above compared the checks and one table of counts.  The
    # numbers of part A and of part B that the json keeps beside them were not compared: one of them changed in the script
    # passed here.  Every value that is not a check is compared, whole numbers and words exactly, decimals to eight digits.
    for k in old:
        if not isinstance(old[k], bool):
            assert _values_to_eight_digits(new[k]) == _values_to_eight_digits(old[k]), "%s is not what the committed json holds (seed %d)" % (k, seed)


def test_what_is_held_under_another_version_can_fail_and_lets_a_last_digit_be():
    """The weaker comparison is not run on this machine by the test above, where the versions are the run's own.  Here it is run
    on the committed files themselves and on three changed copies: a last digit, which it lets be; a label, and a set printed
    where a list was, which it refuses."""
    run0 = (HERE / "whole_and_value_on_main_run.txt").read_bytes()
    data0 = (HERE / "whole_and_value_on_main.json").read_bytes()
    _held_under_another_version(run0, data0, run0, data0, 0)
    text = run0.decode("utf-8")
    assert "1.118033989" in text and "(16275 sequences as written; 2815 up to rotation;" in text and "['-11 + 2*I', '-11 - 2*I']" in text
    _held_under_another_version(text.replace("1.118033989", "1.118033988").encode("utf-8"), data0, run0, data0, 0)       # a last digit
    for old, new in (("(16275 sequences as written; 2815 up to rotation;", "(16275 sequences; 2815 up to rotation;"),
                     ("['-11 + 2*I', '-11 - 2*I']", "{'-11 - 2*I', '-11 + 2*I'}"), ("1.118033989", "1.118133989")):
        changed = text.replace(old, new).encode("utf-8")
        assert changed != run0
        try:
            _held_under_another_version(changed, data0, run0, data0, 0)
        except AssertionError:
            continue
        raise AssertionError("the weaker comparison let this through: %s" % new)
    flipped = json.loads(data0)
    first = next(k for k, v in flipped.items() if isinstance(v, bool))
    flipped[first] = not flipped[first]
    try:
        _held_under_another_version(run0, json.dumps(flipped).encode("utf-8"), run0, data0, 0)
    except AssertionError:
        pass
    else:
        raise AssertionError("the weaker comparison let a failing check through")
    # ADDED 2026-11-12 (Review 80; a reader's finding F5): the numbers the json keeps beside its checks.  A whole number of part
    # A changed, and a decimal of part B changed in its third digit, are refused; the same decimal changed past its eighth is let be.
    # Each of the three passed the comparison as it was, which read the checks and one table of counts.
    def as_it_was(run, data):
        new, old = json.loads(data), json.loads(data0)
        return (_to_eight_digits(run.decode("utf-8")) == _to_eight_digits(run0.decode("utf-8")) and list(new) == list(old)
                and all(new[k] == old[k] for k in old if isinstance(old[k], bool)) and new["B_counts"] == old["B_counts"])
    whole = json.loads(data0)
    assert whole["A_numbers"]["W"] == [-3, -14, 1, 3] and whole["B_numbers"]["own"]["(6)"] == "3.61803398875"
    for where, value, refused in ((("A_numbers", "W"), [-3, -14, 1, 4], True), (("B_numbers", "own", "(6)"), "3.62803398875", True),
                                  (("B_numbers", "own", "(6)"), "3.61803398876", False)):
        changed = json.loads(data0)
        at = changed
        for key in where[:-1]:
            at = at[key]
        at[where[-1]] = value
        changed = json.dumps(changed).encode("utf-8")
        assert as_it_was(run0, changed), where                                  # the comparison as it was lets all three through
        try:
            _held_under_another_version(run0, changed, run0, data0, 0)
        except AssertionError:
            assert refused, where
        else:
            assert not refused, "the weaker comparison let a changed number through: %s" % (where,)
    # and the file that says which versions made the run is the script's own, written at every run
    made = json.loads((HERE / "whole_and_value_on_main_made_with.json").read_text(encoding="utf-8"))
    assert made == _MADE_WITH_AS_HELD and dict(made, python="0.0") != _MADE_WITH_AS_HELD      # main's plant on that file
    assert set(made) == {"python", "mpmath", "sympy"} and "whole_and_value_on_main_made_with.json" in (HERE / "whole_and_value_on_main.py").read_text(encoding="utf-8")


_PINNED_CONDITIONS = {      # the label a check begins with -> its condition, and what it prints beside it, as the script has them
    "E3 (Q5) the mirror normalises the group": ("mirror_ok and len(box) >= 200 and sum(1 for x in box if x[2] != 0) >= 200", None),
    "the own values of the allowed single runs increase without bound": ("single_ok", None),
    "E5 W fixes the two twins over one of t = +-5 sqrt5": (None, "{k: sorted(v) for k, v in over.items()}"),
}


def test_the_conditions_of_the_mended_checks_are_the_ones_that_were_mended():
    """Two plants: a clause that is not a literal and is always true, joined by `or` to the two conditions that were once the
    literal True; and the sorting of a printed set undone.  The scan for constants sees neither.  The conditions and the printed
    detail of the mended checks are held here word for word, so that a change to one is a change in two places; and what the
    two conditions rest on is held as well: each is a conjunction over something computed.

    CHANGED 2026-11-12 (Review 80): the body is the function below, word for word, so that it can be given a planted text.
    It returns how many checks of the script it read."""
    assert _the_mended_conditions_are_held((HERE / "whole_and_value_on_main.py").read_text(encoding="utf-8")) >= 60


def _the_mended_conditions_are_held(src):
    tree = ast.parse(src)
    calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "check" and isinstance(n.args[0], ast.Constant)]
    for start, (cond, detail) in _PINNED_CONDITIONS.items():
        hit = [n for n in calls if str(n.args[0].value).startswith(start)]
        assert len(hit) == 1, start
        if cond is not None:
            assert ast.get_source_segment(src, hit[0].args[1]) == cond, start
        if detail is not None:
            assert ast.get_source_segment(src, hit[0].args[2]) == detail, start
    # no condition of any check is an `or` with a comparison of a length or a count to zero in it: the shape of the plant
    for n in calls:
        for b in ast.walk(n.args[1]):
            if isinstance(b, ast.BoolOp) and isinstance(b.op, ast.Or):
                seg = ast.get_source_segment(src, b)
                assert not re.search(r"len\([^)]*\)\s*(>=\s*0|>\s*-1|>\s*0)\b", seg), seg[:120]
    # the two flags are computed: each is bound once, to all(...) over the things multiplied out or evaluated
    for name in ("mirror_ok", "single_ok"):
        binds = [n for n in ast.walk(tree) if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) and n.targets[0].id == name]
        assert len(binds) == 1 and "all(" in ast.get_source_segment(src, binds[0].value), name
    return len(calls)


def test_the_script_computes_what_it_says_it_computes():
    """A plant typed the three counts of run sequences in place of the comprehensions that compute them; the lock read the
    committed file, where the numbers are the same, and its scan saw a constant and not a table of constants.  The scan now
    sees a table, a list or a tuple whose every entry is a constant, and the three counts are held to what they are built from.

    CHANGED 2026-11-12 (Review 80): the reading of the script's text is the function below, word for word."""
    planted = 'RES["counts"] = {"a": 16275, "b": 2815}\nn = 5\nRES["more"] = [1, n]\nRES["fine"] = {"a": len(xs)}\n'
    assert _constant_checks(planted)[0] == [1, 3]
    assert _the_counts_are_built((HERE / "whole_and_value_on_main.py").read_text(encoding="utf-8")) == ["len(lows)", "by_all", "by_even"]


def _the_counts_are_built(src):
    found, calls = _constant_checks(src)
    assert found == [] and calls >= 60
    tree = ast.parse(src)
    counts = [n for n in ast.walk(tree) if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Subscript) and isinstance(n.targets[0].slice, ast.Constant) and n.targets[0].slice.value == "B_counts"]
    assert len(counts) == 1 and isinstance(counts[0].value, ast.Dict)
    names = [ast.get_source_segment(src, v) for v in counts[0].value.values]
    assert names == ["len(lows)", "by_all", "by_even"]
    for name in ("by_all", "by_even"):
        binds = [n for n in ast.walk(tree) if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) and n.targets[0].id == name]
        assert len(binds) == 1 and ast.get_source_segment(src, binds[0].value).startswith("len({min(seq[i:] + seq[:i] for i in range("), name
    return names


# ---- Review 80 (2026-11-12): a reader's findings F1, F3 and F4, each made again by main with a plant of its own (the arc B1898
# keeps them, verification/checks/plants_b1881_third.py).  Each weakens the script so that a check cannot fail, or so that
# nothing is read, and leaves what the script prints as it was.  The run compared with the committed files is then the same,
# and the second methods agree with it.  Only a reading of the script's text can see such a change, and the lock read it in
# places.  It is now held whole.
_THE_SCRIPT_AS_HELD = "b0210f3eb312cabf130dc84b33f23ecf5a4b4e10a53abded3173c6630386c4ca"      # sha256 of whole_and_value_on_main.py


def _as_the_lock_read_the_scripts_text_before(src):
    """every reading of the script's text that this lock made before it held the script whole: True where each passes"""
    try:
        found, calls = _constant_checks(src)
        assert found == [] and calls >= 60 and src.count("this check was passed the literal True") == 2
        _the_mended_conditions_are_held(src)
        _the_counts_are_built(src)
    except AssertionError:
        return False
    return True


_PLANTS_OF_REVIEW_80 = {      # main's plants, as main wrote them: (the text that stands in the script, what the plant puts there)
    "F1: the two mended conditions taken over empty lists": [
        ("mirror_ok = all(_conj_by_mirror(a, b, c5, d) == [[a, -b], [-c5, d]] and (-c5) % 5 == 0 and a * d - (-b) * (-c5) == 1 for a, b, c5, d in box)", "mirror_ok = all([])"),
        ("single_ok = all(abs(v - (mp.mpf(5 * m) / 2 + mp.sqrt(5) / 2)) < mp.mpf(10) ** -40 for m, v in zip(range(1, 6), single)) and all(x < y for x, y in zip(single, single[1:]))", "single_ok = all([])")],
    "F2: check() made to ignore what it is passed": [
        ('def check(name, ok, detail=""):', 'def check(name, _ignored_ok, detail="", ok=True):')],
    "F3: an unpinned check made unable to fail by an 'or' on a length that is never 0": [
        ("          len(seqs) == len(lows) and abs(floor - mp.sqrt(5) / 2) < mp.mpf(10) ** -100, mp.nstr(floor, 10))",
         "          (False and (len(seqs) == len(lows) and abs(floor - mp.sqrt(5) / 2) < mp.mpf(10) ** -100)) or len(OUT) >= 1, mp.nstr(floor, 10))")],
    "F4: no sequence read: the least typed, the two counts typed behind the pinned beginning": [
        ("                lows.append(max(heights(list(seq))))", "                lows.append(mp.sqrt(5) / 2)"),
        ("    by_all = len({min(seq[i:] + seq[:i] for i in range(len(seq))) for seq in seqs})", "    by_all = len({min(seq[i:] + seq[:i] for i in range(len(seq))) for seq in []}) or %d" % RES["B_counts"]["up_to_every_rotation"]),
        ("    by_even = len({min(seq[i:] + seq[:i] for i in range(0, len(seq), 2)) for seq in seqs})", "    by_even = len({min(seq[i:] + seq[:i] for i in range(0, len(seq), 2)) for seq in []}) or %d" % RES["B_counts"]["up_to_rotations_that_keep_the_letters"])],
    "F5, its half in the script: a number of part A changed": [
        ('"W": list(W),', '"W": [[100 + len(OUT), 101], [102, 103]],')],
}


def _planted(src, pairs):
    for old, new in pairs:
        assert src.count(old) == 1, old[:60]
        src = src.replace(old, new)
    return src


def test_the_script_is_the_one_this_lock_was_written_against():
    """The script is held by the digest of its bytes.  A change to it, a comment included, fails here until the digest above is
    changed as well: say in this lock's docstring what changed and why.

    What could fail: any of main's five plants, or any other change to the script.  Each plant is put to the readings of the
    script's text that the lock made before: every one passes them, which is the finding; and every one changes the digest.
    WHAT THIS CANNOT HOLD: a change made to the script and to the digest together.  That is two places, and a reader of the
    difference sees both."""
    raw = (HERE / "whole_and_value_on_main.py").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == _THE_SCRIPT_AS_HELD, "the script is not the one this lock was written against"
    src = raw.decode("utf-8")
    assert _as_the_lock_read_the_scripts_text_before(src)
    for what, pairs in _PLANTS_OF_REVIEW_80.items():
        planted = _planted(src, pairs)
        assert _as_the_lock_read_the_scripts_text_before(planted), what           # the readings of before pass: the finding
        assert hashlib.sha256(planted.encode("utf-8")).hexdigest() != _THE_SCRIPT_AS_HELD, what
    # the readings of before are not blind to everything: a plant that B1895's lock holds is refused by them
    assert not _as_the_lock_read_the_scripts_text_before(_planted(src, [('for the run of 5m + 1", single_ok,', 'for the run of 5m + 1", True,')]))


# ---- Review 80 (2026-11-12): a reader's finding F2, made again by main's plant.  The script's own function for a check was
# given a signature under which it ignores what it is passed: every check then reads as holding, and the 65 are 65 holding.
# The digest above sees the change.  This sees what the change does: the function is called, and must record a failure.
def _check_records_what_it_is_passed(mod):
    """True where the script's check() records a false thing as failing and a true thing as holding, in all three places"""
    mod.OUT.clear(); mod.RES.clear(); mod.FAILS.clear()
    a = mod.check("planted by the lock: a false thing", False, "the detail")
    b = mod.check("planted by the lock: a true thing", 1 == 1)
    return (a is False and b is True and mod.RES == {"planted by the lock: a false thing": False, "planted by the lock: a true thing": True}
            and mod.FAILS == ["planted by the lock: a false thing"] and len(mod.OUT) == 2
            and mod.OUT[0].startswith("   [FAILS] planted by the lock: a false thing -- the detail") and mod.OUT[1].startswith("   [ok] planted by the lock: a true thing"))


def _a_module_of(src, name):
    import types
    mod = types.ModuleType(name)
    mod.__file__ = str(HERE / "whole_and_value_on_main.py")
    exec(compile(src, mod.__file__, "exec"), mod.__dict__)                     # definitions only: the run is under __main__
    return mod


def test_a_check_of_the_script_fails_when_it_is_passed_a_false_thing(capsys):
    src = (HERE / "whole_and_value_on_main.py").read_text(encoding="utf-8")
    assert _check_records_what_it_is_passed(_a_module_of(src, "b1881_script_as_it_is"))
    # main's plant, and two more ways to the same end: the function then records a false thing as holding, or not at all
    for old, new in _PLANTS_OF_REVIEW_80["F2: check() made to ignore what it is passed"] + [
            ("    RES[name] = bool(ok)\n    if not ok:\n        FAILS.append(name)", "    RES[name] = True\n    if not ok and False:\n        FAILS.append(name)"),
            ('"ok" if ok else "FAILS"', '"ok"')]:
        assert src.count(old) == 1, old
        assert not _check_records_what_it_is_passed(_a_module_of(src.replace(old, new), "b1881_script_planted")), new
    capsys.readouterr()                                                        # what the planted checks printed is not this test's output
    # and the committed run was made by 65 calls that could fail: its json holds no check under a planted name
    assert not any(k.startswith("planted by the lock") for k in RES)


def test_the_withdrawn_word_stands_only_where_it_is_taken_back():
    """Two plants: the docstring of the script's second function given the withdrawn word, where the lock read the header; and
    a new paragraph on the page that states the withdrawn claim in other words than the old sentence.  Held here: the function's
    own docstring; every line of the script and every paragraph of the page that holds the word; and how many paragraphs do.
    WHAT THIS CANNOT HOLD: the claim restated without the word.  A list of spellings is not complete (register row P-817); the
    computation in the test above is what says that the claim is false."""
    mod = _the_script()
    doc = mod.keeps_line_main.__doc__
    assert "conjugated by the swap of the two coordinates" in doc and "transpos" not in doc and "B1872 writes the seat's, rows" in doc
    src = (HERE / "whole_and_value_on_main.py").read_text(encoding="utf-8")
    lines = [l for l in src.split("\n") if "transpos" in l.lower()]
    assert len(lines) == 2 and "it is not the transpose either" in lines[0] and "so its transpose is itself" in lines[1], lines
    f = (ARC / "FINDINGS.md").read_text(encoding="utf-8")
    paras = _paragraphs(f)
    with_word = [i for i, p in enumerate(paras) if "transpos" in p.lower()]
    assert len(with_word) == 3, len(with_word)                       # the old sentence, its second correction, the line of what was found
    old, second, found = (paras[i] for i in with_word)
    assert "is its transpose and is this arc's own" in old and with_word[1] == with_word[0] + 1 and second.startswith("> **CORRECTED 2026-11-12, a second time,**")
    assert "It is not the transpose." in second and "where a transpose does enter" in second and "word transpose (§ 5)" in found.replace("\n  ", " ")
    c = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    assert c.lower().count("transpos") == 2 and "it is not the transpose" in c
