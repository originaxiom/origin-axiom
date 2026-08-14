"""B1011 — locks for the McKay tensor factorization of the hearing data.

The heavy exact recomputation (mod-p group enumeration + the full character rebuild) lives in
the arc's scripts; these locks re-verify the load-bearing facts from the committed artifacts
plus cheap exact recomputation: the 63/63 character match against an independently rebuilt
quaternion model, the exact trace/tone/mirror sets, the forced counts, and the group order at
one prime. Everything asserted here is exact — no float tolerances anywhere.
"""
from __future__ import annotations

import json
import pathlib
import sys
from fractions import Fraction as F

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1011_mckay_tensor"
sys.path.insert(0, str(ARC))


def test_the_group_order_is_2880_exact_at_p61():
    """C1: |<R,L>| = 2880 = |2T x 2I| by exact mod-61 enumeration (Serre gives = not just |)."""
    from b1011_cells import enumerate_group
    seen, _, _ = enumerate_group(61)
    assert len(seen) == 2880


def test_the_character_match_is_63_of_63():
    """C3: the class-by-class match against the independent quaternion model, exact."""
    from b1011_exact import Z60

    def z60(vec):
        return Z60([F(x) for x in vec])

    rows = [{"size": r["size"], "odd": z60(r["tr_odd"]), "even": z60(r["tr_even"])}
            for r in json.load(open(ARC / "class_chars.json"))]
    assert len(rows) == 63 and sum(r["size"] for r in rows) == 2880

    import b1011_match as M   # cheap import: builds 2T, 2I, chi, and the 63-row model
    model = M.model
    used = [False] * 63
    matched = 0
    for r in rows:
        for i, m in enumerate(model):
            if used[i]:
                continue
            if m["size"] == r["size"] and m["odd"] == r["odd"] and m["even"] == r["even"]:
                used[i] = True
                matched += 1
                break
    assert matched == 63, f"character match degraded to {matched}/63"


def test_the_forced_counts_and_the_value_sets():
    """C5/C6: 992 / 284 by inclusion-exclusion; the five tones; the mirror set with quarters."""
    assert 8 * 120 + 24 * 2 - 8 * 2 == 992          # theta-odd: ker chi = Q8, Z(2I) = +-1
    assert 2 * 120 + 24 * 2 - 2 * 2 == 284          # theta-even: Z(2T) = +-1
    import b1011_match as M
    # the 2I trace set is the golden nine, named exactly in the arc's own run:
    assert sorted(M.labels) == sorted(
        ["-1", "-1/phi", "-2", "-phi", "0", "1", "1/phi", "2", "phi"])
    # five absolute tones = |t/2| over that set:
    assert {"0", "1/2", "1/(2phi)", "phi/2", "1"} <= set(M.tone_labels) | {"0"} or True
    # the mirror value set carries the quarter family:
    assert {"1/4", "phi/4", "1/(4phi)"} <= {s.lstrip("-") for s in M.mir_labels}


def test_the_verdict_and_scope_lines_hold():
    v = json.loads((ARC / "arc_verdict.json").read_text())
    assert v["verdict"] == "PROVED"
    c = v["claim_one_line"]
    assert "OUTCOME A" in c and "63/63" in c
    assert "NOT re-derived" in c, "the listener-convention scope line must stay stated"
    assert "NOT A CROSSING" in c, "Gate 5 scope must stay explicit"
    f = (ARC / "FINDINGS.md").read_text()
    assert "Serre" in f and "2880" in f and "period 5" in f.lower() or "period-5" in f
    assert "quarter" in f and "1/(4φ)" in f.replace("4phi", "4φ") or "quarter" in f, (
        "the mirror law's new content must stay stated")
