#!/usr/bin/env python3
"""Independent exact checks for the reproducible core of B1199/GC-31.

The certificate deliberately reads only the already banked B879 packet shipped
in this checkout.  It does not trust B1199's prose or scratch-only verifier.
All arithmetic is integer arithmetic over SL(2,F_5); no optional dependency is
required.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "frontier" / "B879_selection_cochain" / "packet"
W0A = PACKET / "w0a_criteria" / "w0a_table.json"
W2B = PACKET / "w2b_landscape" / "w2b_table.json"
P = 5

Matrix = tuple[int, int, int, int]
I: Matrix = (1, 0, 0, 1)
R: Matrix = (1, 1, 0, 1)
L: Matrix = (1, 0, 1, 1)


def mul(a: Matrix, b: Matrix) -> Matrix:
    return (
        (a[0] * b[0] + a[1] * b[2]) % P,
        (a[0] * b[1] + a[1] * b[3]) % P,
        (a[2] * b[0] + a[3] * b[2]) % P,
        (a[2] * b[1] + a[3] * b[3]) % P,
    )


def inv(a: Matrix) -> Matrix:
    assert (a[0] * a[3] - a[1] * a[2]) % P == 1
    return (a[3] % P, -a[1] % P, -a[2] % P, a[0] % P)


def word_matrix(word: str) -> Matrix:
    out = I
    for letter in word:
        out = mul(out, R if letter == "R" else L)
    return out


def sl2() -> list[Matrix]:
    return [
        (a, b, c, d)
        for a in range(P)
        for b in range(P)
        for c in range(P)
        for d in range(P)
        if (a * d - b * c) % P == 1
    ]


def conjugacy_classes(group: list[Matrix]) -> tuple[list[frozenset[Matrix]], dict[Matrix, Matrix]]:
    remaining = set(group)
    classes: list[frozenset[Matrix]] = []
    representative: dict[Matrix, Matrix] = {}
    while remaining:
        x = min(remaining)
        cls = frozenset(mul(mul(g, x), inv(g)) for g in group)
        rep = min(cls)
        classes.append(cls)
        for y in cls:
            representative[y] = rep
        remaining -= cls
    return classes, representative


def main() -> None:
    w0a = json.loads(W0A.read_text(encoding="utf-8"))
    w2b = json.loads(W2B.read_text(encoding="utf-8"))
    rows0 = w0a["hyperbolic_classes"]
    rows2 = w2b["classes"]

    expected_by_length = {
        2: 1,
        3: 2,
        4: 3,
        5: 6,
        6: 9,
        7: 18,
        8: 30,
        9: 56,
        10: 99,
        11: 186,
        12: 335,
    }
    count_by_length = Counter(row["length"] for row in rows0)
    assert len(rows0) == len(rows2) == 745
    assert dict(sorted(count_by_length.items())) == expected_by_length
    words0 = {row["word"] for row in rows0}
    words2 = {row["word"] for row in rows2}
    assert words0 == words2

    unit = {row["word"] for row in rows0 if row["unit_det"]}
    prime = {row["word"] for row in rows0 if row["prime_conductor"]}
    trace3 = {row["word"] for row in rows0 if row["trace"] == 3}
    assert unit == prime == trace3 == {"LR"}

    group = sl2()
    assert len(group) == 120
    classes, class_of = conjugacy_classes(group)
    assert len(classes) == 9
    assert sorted(map(len, classes)) == [1, 1, 12, 12, 12, 12, 20, 20, 30]

    values_by_class: dict[Matrix, set[str]] = defaultdict(set)
    values_by_trace: dict[int, set[str]] = defaultdict(set)
    value_counts: Counter[str] = Counter()
    for row in rows2:
        matrix = word_matrix(row["word"])
        label = row["abs_tr_odd_sq_closed_form"]
        values_by_class[class_of[matrix]].add(label)
        values_by_trace[(matrix[0] + matrix[3]) % P].add(label)
        value_counts[label] += 1

    assert len(values_by_class) == 9
    assert all(len(values) == 1 for values in values_by_class.values())
    assert len(values_by_trace[2]) > 1 and len(values_by_trace[3]) > 1
    assert value_counts == Counter(
        {
            "0": 188,
            "(3-sqrt5)/2 = 1/phi^2": 153,
            "1": 249,
            "(3+sqrt5)/2 = phi^2": 147,
            "4": 8,
        }
    )

    print(f"primitive_classes={len(rows0)}")
    print(f"classes_by_length={list(expected_by_length.values())}")
    print(f"word_sets_byte_level_equal={words0 == words2}")
    print(f"unit_prime_trace3_selector={sorted(unit)}")
    print(f"sl2_f5_order={len(group)}")
    print(f"sl2_f5_conjugacy_class_sizes={sorted(map(len, classes))}")
    print(f"shadow_classes_represented={len(values_by_class)}")
    print("multivalued_shadow_classes=0")
    print(f"trace2_value_count={len(values_by_trace[2])}")
    print(f"trace3_value_count={len(values_by_trace[3])}")
    print("R023 B1199 SELECTION RECHECK: PASS")


if __name__ == "__main__":
    main()
