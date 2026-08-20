"""B1102 locks — the exact hypercharge solve at the A2 landing.

Recomputes the verdict-bearing claims from the arc's stored exact JSONs with
independent arithmetic (the banking seat's own checks, made permanent):
  1. all 18 stored directions reproduce the banked 6Y 27-multiset EXACTLY,
     against an independent transcription of B950's banked target;
  2. the completeness premise of the 625-assignment search (exactly four
     +-standard-basis weight classes, all of size 3; five admissible values);
  3. the sharpener is forced at Cartan level: NO stored direction is pure on
     either ideal's Cartan pair (so no solution can commute with full color);
  4. the recorded su(2) compatibility and search-bookkeeping fields.
"""
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1102_exact_hypercharge_solve"

# The banked target, transcribed independently from B950's ledger via
# frontier/B1100_landing_content/b1100_hypercharge.py (line: target=...).
TARGET = Counter(
    [F(1, 6)] * 6 + [F(-2, 3)] * 3 + [F(1, 3)] * 3 + [F(-1, 2)] * 2
    + [F(1)] + [F(0)] + [F(-1, 3)] * 3 + [F(1, 3)] * 3 + [F(1, 2)] * 2
    + [F(-1, 2)] * 2 + [F(0)]
)


def _load():
    inter = json.load(open(ARC / "b1102_intermediate.json"))
    res = json.load(open(ARC / "b1102_results.json"))
    cls = [(tuple(F(x) for x in w), int(sz)) for w, sz in inter["classes"]]
    sols = [[F(x) for x in t] for t in res["all_solving_directions"]]
    return cls, sols, res


def test_banked_target_shape():
    assert sum(TARGET.values()) == 27
    assert sorted(TARGET.values(), reverse=True) == [6, 6, 4, 3, 3, 2, 2, 1]


def test_all_18_directions_match_exactly():
    cls, sols, _ = _load()
    assert len(sols) == 18, "the solution set must be exactly the 18 banked"
    assert sum(sz for _, sz in cls) == 27
    for t in sols:
        vals = Counter()
        for w, sz in cls:
            vals[sum(ti * wi for ti, wi in zip(t, w))] += sz
        assert vals == TARGET, f"direction {t} fails the banked multiset"


def test_completeness_premise():
    cls, _, res = _load()
    basis_cls = [(w, sz) for w, sz in cls
                 if sorted(map(abs, w)) == [0, 0, 0, 1]]
    assert len(basis_cls) == 4, "exactly four +-basis-vector classes"
    assert all(sz == 3 for _, sz in basis_cls), "all four have size 3"
    m3 = [v for v, c in TARGET.items() if c >= 3]
    assert len(m3) == 5, "five admissible target values for size-3 classes"
    assert res["assignments_tried"] == 5 ** 4 == 625


def test_no_color_commuting_solution():
    _, sols, res = _load()
    pure = [t for t in sols
            if (t[0] == 0 and t[1] == 0) or (t[2] == 0 and t[3] == 0)]
    assert pure == [], ("a direction pure on one ideal would be a "
                        "color-commuting candidate; the sharpener says none exist")
    su2 = res["su2_compat"]
    assert su2["commutes"] is True
    assert su2["any_solution_has_full_color_commuting_with_Y"] is False
    assert su2["neutral_root_count_all_solutions"] == [2] * 18
    dec = su2["decomposition"]
    n_doub = sum(entry[-1] for entry in dec["doublets"])
    n_sing = sum(entry[-1] for entry in dec["singlets"])
    assert n_doub == 6 and n_sing == 15, (n_doub, n_sing)
    assert 2 * n_doub + n_sing == 27


def test_weight_class_sizes_match_banked():
    cls, _, res = _load()
    sizes = sorted((sz for _, sz in cls), reverse=True)
    assert sizes == [3] * 6 + [1] * 9
    assert res["weight_class_sizes"] == [3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert res["cartan_certified"] is True and res["exact_match"] is True
    assert res["solving_direction"] == ["1/6", "1/6", "2/3", "-1/3"]
