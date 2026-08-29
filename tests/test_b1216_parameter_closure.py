"""B1216 — the parameter-closure loop, run 1. These locks pin the two corrections and the caveat."""
import json
from itertools import combinations_with_replacement
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1216_parameter_closure_run1"


def _res():
    return json.loads((ARC / "b1216_results.json").read_text(encoding="utf-8"))


def test_the_eigenline_clause_cannot_fail():
    """The vacuity, re-derived. Every anti-conjugator swaps the eigenlines -- including a det +1 one,
    which is the mirror-EVEN type the record calls dead. A clause with no failing branch supports
    nothing, and must never again be cited as evidence that the class restricts to c."""
    def swaps(P, X):
        P, X = sp.Matrix(P), sp.Matrix(X)
        if sp.simplify(X * P * X.inv() - P.inv()) != sp.zeros(2, 2):
            return None
        (l1, _, v1), (l2, _, v2) = P.eigenvects()[0], P.eigenvects()[1]
        w = sp.simplify(X * v1[0])
        return sp.simplify(w[0] * v2[0][1] - w[1] * v2[0][0]) == 0
    assert swaps([[2, 1], [1, 1]], [[-1, 0], [1, 1]]) is True      # det X = -1, the live case
    dead = swaps([[5, 2], [2, 1]], [[0, -1], [1, 0]])              # det X = +1, the dead type
    assert dead is True, "if a det +1 anti-conjugator ever FAILED to swap, the clause would bite"


def test_the_sign_result_is_untouched_and_still_discriminates():
    """The vacuity removes a supporting leg, not the headline. The control is what keeps the sign
    result real: the norm-(-1) sqrt(2) control never yields DIRECT(-1)."""
    r = _res()
    c1 = next(c for c in r["cells"] if c["cell"].startswith("C1"))
    assert "never DIRECT(-1)" in c1["finding"] or "never  DIRECT(-1)" in c1["finding"]
    corr = next(c for c in r["corrections_to_our_own_record"] if "GC-16" in c["target"])
    assert "det = -1 sign result" in corr["untouched"]


def test_the_tail_enumeration_is_complete():
    """B1215 missed (8,8). The corrected enumeration must stay complete."""
    pairs = [(a, b) for a, b in combinations_with_replacement([0, 2, 4, 6, 8], 2)
             if (a + b) % 12 == 4]
    assert pairs == [(0, 4), (2, 2), (8, 8)], pairs
    surviving = [p for p in pairs if p[0] != p[1]]
    assert len(surviving) == 1, "one surviving lepton pure-tail pair"
    down = [(a, b) for a, b in combinations_with_replacement([0, 2, 4, 6, 8], 2)
            if (a + b) % 12 == 8]
    assert len([p for p in down if p[0] != p[1]]) == 2, "two surviving down pairs"


def test_the_advance_caveat_on_a_future_P3_closure_is_recorded():
    """The single most quotable-out-of-context thing this run produced. dim 0 is a FINITE POINT SET;
    closing the P^3 converts the row from continuous to finite label, it does NOT yield a unique
    prediction. Recorded before any closure, so it cannot be added afterwards."""
    c = _res()["advance_caveat"]
    assert "FINITE POINT SET" in c and "does" in c and "NOT become a unique prediction" in c


def test_the_score_is_recorded_honestly():
    """An adjudication reporting four successes would not be credible. The run's own score, and the
    fact that the pre-registration was wrong, must stay in the record."""
    r = _res()
    assert "zero rows deleted" in r["score"]
    p = r["prereg_vs_actual"]
    assert p["actual"]["C2"].startswith("failed")
    assert "did not close" in p["actual"]["C3"]
    assert "least likely" in p["lesson"]
    assert r["goal_test"]["met"] is False
    assert set(r["goal_test"]["blocks"]) == {"lambda", "the P^3"}
