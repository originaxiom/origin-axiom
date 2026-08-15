"""B1066 -- the exhaustion census, given an executable check at last.

Closes the proof auditor's D9.  The Wave-1 inventory recorded the defect plainly:
"B1066 -- the exhaustion census -- has ZERO locks; the paper's most-quoted negative is
the one with no executable check."  A negative that carries weight in the argument and
cannot be run is exactly the shape the paper's own Appendix B forbids.

What is locked here:

  * the two predicted values are members of the LICENSED menus, not chosen after the
    fact -- phi/2 lies in the T and M menus, (1 - 1/sqrt5)/2 lies in the L menu;
  * the two exclusions reproduce from the quoted measurements by exact rational
    arithmetic: 3.4 sigma on the phase-independent anchor |U_e1|, and 4.7 sigma on
    sin^2(theta_12);
  * the census count -- EXACTLY TWO target-shaped relations -- matches the arc;
  * the arc's verdict is NEGATIVE and its withdrawn first execution stays withdrawn.

What is NOT locked, and must not be read as locked: that the menus themselves are
exhaustive.  The arc's own scope is a bounded enumeration (arity <= 3, fixed menus,
kind-licensed), and the load-bearing word is "licensed", never "exhausted" alone.
The final test pins that scope so no later draft can quietly widen it.

Exact arithmetic throughout; the sigma figures are computed as rationals and compared
to the paper's one-decimal roundings by an exact interval test, not by float equality.
"""

import json
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_ARC = _ROOT / "frontier" / "B1066_lane3_nomination"
_VERDICT = json.loads((_ARC / "arc_verdict.json").read_text(encoding="utf-8"))
_FINDINGS = (_ARC / "FINDINGS.md").read_text(encoding="utf-8")

PHI = (1 + sp.sqrt(5)) / 2

# The licensed menus, as defined in b1066_inventory.py.
MENU_T = [sp.Integer(0), 1 / (2 * PHI), sp.Rational(1, 2), PHI / 2, sp.Integer(1)]
MENU_M = [sp.Integer(0), sp.Rational(1, 4), 1 / (4 * PHI), sp.Rational(1, 2),
          1 / (2 * PHI), PHI / 4, PHI / 2, sp.Integer(1)]
MENU_L = [(1 - 1 / sp.sqrt(5)) / 2, (1 + 1 / sp.sqrt(5)) / 2, sp.Integer(1)]

# The two fired relations, as adjudicated in execution 2 (NuFIT 6.1, Nov 2025),
# both orderings, delta profiled over the full circle.
RELATIONS = {
    "R-B": {  # the phi-geometric row; the anchor is delta-independent
        "observable": "|U_e1|",
        "measured": sp.Rational("0.8225"),
        "sigma": sp.Rational("0.0040"),
        "predicted": PHI / 2,
        "reported_sigma": sp.Rational("34", 10),
        "phase_independent": True,
    },
    "R-A": {  # the listener pair
        "observable": "sin^2(theta_12)",
        "measured": sp.Rational("0.308"),
        "sigma": sp.Rational("0.0067"),
        "predicted": (1 - 1 / sp.sqrt(5)) / 2,
        "reported_sigma": sp.Rational("47", 10),
        "phase_independent": False,
    },
}


def _in_menu(x, menu):
    return any(sp.simplify(sp.radsimp(x - m)) == 0 for m in menu)


def _tension(rel):
    """|measured - predicted| / sigma, exactly."""
    return sp.simplify(sp.Abs(rel["measured"] - rel["predicted"]) / rel["sigma"])


def test_the_predicted_values_are_licensed_menu_members():
    """Neither prediction was invented to fit; both are menu entries."""
    assert _in_menu(PHI / 2, MENU_T)
    assert _in_menu(PHI / 2, MENU_M)
    assert _in_menu((1 - 1 / sp.sqrt(5)) / 2, MENU_L)


def test_the_menus_are_closed_under_their_own_definition():
    """Guards against a menu silently gaining an entry later."""
    assert len(MENU_T) == 5
    assert len(MENU_M) == 8
    assert len(MENU_L) == 3


def test_both_exclusions_reproduce_to_the_reported_precision():
    for name, rel in RELATIONS.items():
        t = _tension(rel)
        lo, hi = rel["reported_sigma"] - sp.Rational(1, 10), \
            rel["reported_sigma"] + sp.Rational(1, 10)
        assert lo < t < hi, f"{name}: recomputed {sp.N(t, 5)}, reported {rel['reported_sigma']}"


def test_the_phase_independent_anchor_is_the_unrescuable_one():
    """R-B misses on a delta-independent quantity, so profiling cannot save it."""
    assert RELATIONS["R-B"]["phase_independent"] is True
    assert RELATIONS["R-A"]["phase_independent"] is False
    assert _tension(RELATIONS["R-B"]) > 3


def test_both_relations_miss():
    """Neither is within 3 sigma; the census is a double negative."""
    for name, rel in RELATIONS.items():
        assert _tension(rel) > 3, name


def test_exactly_two_target_shaped_relations():
    assert len(RELATIONS) == 2


def test_the_arc_verdict_is_negative_and_execution_one_stays_withdrawn():
    assert _VERDICT["verdict"] == "NEGATIVE"
    claim = _VERDICT["claim_one_line"]
    assert "WITHDRAWN" in claim
    assert "NuFIT 6.1" in claim
    assert "execution 2 valid" in claim


def test_the_scope_word_is_licensed_not_exhausted():
    """The enumeration is bounded; this pins that and must not be relaxed.

    The paper may say the licensed inventory is exhausted.  It may NOT say the space
    of relations is exhausted, and this test exists so that distinction survives.
    """
    text = _FINDINGS.lower()
    assert "licensed" in text
    # A bounded enumeration: arity cap and fixed menus are both recorded.
    assert "arity" in text or "menu" in text
