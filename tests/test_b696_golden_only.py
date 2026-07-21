"""B696 — the golden-only sum-rule locking: silver solo classes rank 3."""
import json
import os
import re

import sympy as sp

_SRC = ("~/oa-seat-cc2/origin-axiom/frontier/B673_loop4_integration/"
        "packet/loop4/d3_silvercup/d3_results.json")


def test_silver_solo_classes_rank_3_golden_only():
    if not os.path.exists(_SRC):
        return  # source is on the cc2 clone; skip if unavailable
    s, I = sp.symbols("s I")
    bc = json.load(open(_SRC))["banked_classes"]

    def parse(e):
        return sp.sympify(e.replace("^", "**").replace("i*", "I*"),
                          locals={"s": s, "I": I, "i": I})

    def red(expr):
        expr = sp.expand(sp.expand(expr).subs(I**2, -1))
        return sp.Poly(expr, s).rem(sp.Poly(s**4 - 8*s**2 - 16, s)).as_expr()

    M = sp.Matrix([[parse(c) for c in bc[p]["obstruction_coords"]]
                   for p in ["23", "24", "34"]])
    assert red(M[:, [0, 1, 4]].det()) != 0    # a nonzero 3x3 minor => rank 3
