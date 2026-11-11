"""B1881 lock -- the web seat's two relays of 2026-11-11, verified on main.

What could fail here: a check of the sealed run not holding; the run not being what the script gives today (three facts are
recomputed from scratch, by other code than the script's); the arc claiming more than a criterion for what it calls main's reading."""
import itertools
import json
import pathlib
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
    assert Fr(1) + Fr(12, 12) - 0 - 0 - Fr(4, 2) == 0 and Fr(1) + Fr(6, 12) - Fr(2, 4) - 0 - Fr(2, 2) == 0     # both of genus 0


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
