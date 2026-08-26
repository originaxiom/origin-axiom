#!/usr/bin/env python3
"""Exact hostile reproduction of outside memo 70, with its scope made explicit.

This certificate reuses the byte-identical, branch-local E6/27 construction already
shipped in R006.  It checks all three choices of color A2 (the source checked two),
all three weak roots in the derived weak A2, and every SM-shaped 15-state assignment
formed by the declared multiplet rules.  It also proves separately that the anomaly
ratio theorem is universal once the SM multiplet multiplicities are assumed.
"""

from collections import Counter, defaultdict
import itertools
from pathlib import Path


HERE = Path(__file__).resolve().parent
STACK = HERE.parent / "r006_e6_invariants" / "twisted_double.py"
source = STACK.read_text(encoding="utf-8")
cut = source.index("# ---------------- stage 4")

# The imported stack locates its vendored charge-bracket file relative to __file__.
this_file = __file__
__file__ = str(STACK)
exec(compile(source[:cut], str(STACK), "exec"), globals())
__file__ = this_file


R6 = [tuple(int(x) for x in root) for root in ROOTS]
R6_SET = set(R6)
W = [tuple(sp.Rational(x) for x in weight) for weight in weights]


def inner(a, b):
    return ipr(tuple(sp.Rational(x) for x in a),
               tuple(sp.Rational(x) for x in b))


def a2_span(r1, r2):
    found = set()
    for c1 in (-1, 0, 1):
        for c2 in (-1, 0, 1):
            candidate = tuple(c1 * a + c2 * b for a, b in zip(r1, r2))
            if candidate in R6_SET:
                found.add(candidate)
    return found


slots = []
for r1 in R6:
    if slots and any(inner(r1, old) != 0 for slot in slots for old in slot):
        continue
    for r2 in R6:
        if r2 == r1 or inner(r1, r2) != -1:
            continue
        if tuple(a + b for a, b in zip(r1, r2)) not in R6_SET:
            continue
        if slots and any(inner(r2, old) != 0 for slot in slots for old in slot):
            continue
        slot = a2_span(r1, r2)
        assert len(slot) == 6
        slots.append(sorted(slot))
        break
    if len(slots) == 3:
        break

assert len(slots) == 3
assert len(R6_SET - set().union(*(set(slot) for slot in slots))) == 54


def simple_pair(slot):
    for r1 in slot:
        for r2 in slot:
            if r1 != r2 and inner(r1, r2) == -1:
                if tuple(a + b for a, b in zip(r1, r2)) in slot:
                    return r1, r2
    raise AssertionError("A2 simple pair not found")


pairs = [simple_pair(slot) for slot in slots]
triplet = {(1, 0), (-1, 1), (0, -1)}
antitriplet = {(-1, 0), (1, -1), (0, 1)}


def slot_weight(weight, slot_index):
    return (ipr(weight, tuple(sp.Rational(x) for x in pairs[slot_index][0])),
            ipr(weight, tuple(sp.Rational(x) for x in pairs[slot_index][1])))


def rep_type(weight, slot_index):
    value = slot_weight(weight, slot_index)
    if value in triplet:
        return "3"
    if value in antitriplet:
        return "3b"
    assert value == (0, 0)
    return "1"


blocks = Counter(tuple(rep_type(weight, k) for k in range(3)) for weight in W)
assert len(blocks) == 3 and set(blocks.values()) == {9}
print("ANCHOR A2^3: 6+6+6 roots, 54 crossing roots, blocks", dict(blocks))


def null_basis(constraints):
    unit = [tuple(sp.Rational(1 if i == j else 0) for i in range(6))
            for j in range(6)]
    matrix = sp.Matrix([[ipr(e, tuple(sp.Rational(x) for x in constraint))
                         for e in unit]
                        for constraint in constraints])
    basis = [tuple(sp.Rational(x) for x in vector)
             for vector in matrix.nullspace()]
    assert len(basis) == 3
    return basis


SM = {
    (sp.Rational(-4), sp.Rational(2), sp.Rational(-3), sp.Rational(6)),
    (sp.Rational(2), sp.Rational(-4), sp.Rational(-3), sp.Rational(6)),
}


def run_frame(color, weak_slot, weak_root):
    basis = null_basis([pairs[color][0], pairs[color][1], weak_root])

    def y_functional(weight):
        return tuple(ipr(weight, vector) for vector in basis)

    states = range(27)
    color_type = {i: rep_type(W[i], color) for i in states}
    weak_weight = {
        i: ipr(W[i], tuple(sp.Rational(x) for x in weak_root)) for i in states
    }

    q_states = [i for i in states
                if color_type[i] == "3" and weak_weight[i] in (1, -1)]
    q_keys = {y_functional(W[i]) for i in q_states}
    assert len(q_keys) == 1
    yq = next(iter(q_keys))

    anti_groups = defaultdict(list)
    lepton_groups = defaultdict(list)
    singlets = []
    for i in states:
        key = y_functional(W[i])
        if color_type[i] == "3b" and weak_weight[i] == 0:
            anti_groups[key].append(i)
        if color_type[i] == "1" and weak_weight[i] in (1, -1):
            lepton_groups[key].append(i)
        if color_type[i] == "1" and weak_weight[i] == 0:
            singlets.append(i)

    anti_multiplets = [group for group in anti_groups.values() if len(group) == 3]
    lepton_multiplets = [group for group in lepton_groups.values() if len(group) == 2]
    counts = Counter()
    ratios = set()

    for first, second in itertools.combinations(anti_multiplets, 2):
        yu = y_functional(W[first[0]])
        yd = y_functional(W[second[0]])
        for lepton in lepton_multiplets:
            yl = y_functional(W[lepton[0]])
            for singlet in singlets:
                ye = y_functional(W[singlet])
                rows = [
                    [2 * yq[k] + yu[k] + yd[k] for k in range(3)],
                    [3 * yq[k] + yl[k] for k in range(3)],
                    [6 * yq[k] + 3 * yu[k] + 3 * yd[k] + 2 * yl[k] + ye[k]
                     for k in range(3)],
                ]
                kernel = sp.Matrix(rows).nullspace()
                if len(kernel) != 1:
                    if len(kernel) > 1:
                        counts["multidimensional"] += 1
                    continue
                direction = kernel[0]

                def charge(functional):
                    return sp.simplify(sum(functional[k] * direction[k]
                                           for k in range(3)))

                values = [charge(item) for item in (yq, yu, yd, yl, ye)]
                if values[0] == 0:
                    continue
                cubic = (6 * values[0] ** 3 + 3 * values[1] ** 3
                         + 3 * values[2] ** 3 + 2 * values[3] ** 3
                         + values[4] ** 3)
                if sp.simplify(cubic) != 0:
                    continue
                ratio = tuple(sp.Rational(value / values[0]) for value in values[1:])
                ratios.add(ratio)
                counts["solutions"] += 1
                counts["SM"] += int(ratio in SM)
                counts["non_SM"] += int(ratio not in SM)
    return counts, ratios


frame_results = []
for color in range(3):
    color_states = [i for i in range(27) if rep_type(W[i], color) == "3"]
    weak_slot = next(k for k in range(3)
                     if k != color and rep_type(W[color_states[0]], k) != "1")
    weak_roots = [pairs[weak_slot][0], pairs[weak_slot][1],
                  tuple(a + b for a, b in zip(*pairs[weak_slot]))]
    aggregate = Counter()
    ratios = set()
    for weak_root in weak_roots:
        counts, found = run_frame(color, weak_slot, weak_root)
        aggregate.update(counts)
        ratios.update(found)
    assert aggregate["solutions"] == 36
    assert aggregate["SM"] == 36
    assert aggregate["non_SM"] == 0
    assert aggregate["multidimensional"] == 0
    assert ratios == SM
    frame_results.append((aggregate, ratios))
    print(f"FRAME color={color} weak_slot={weak_slot}: {dict(aggregate)} ratios={sorted(ratios)}")

assert all(result == frame_results[0] for result in frame_results)
print("THREE-COLOR-FRAME COVARIANCE: PASS")

# The key hostile fence: after assuming one left-handed SM-shaped 15-plet, the
# anomaly equations alone force the ratios.  E6 is not used in this derivation.
u = sp.symbols("u")
d = -2 - u               # SU(3)^2 U(1), after Yq=1
lepton = -3              # SU(2)^2 U(1)
electron = 6             # gravitational U(1)
cubic = sp.factor(6 + 3 * u**3 + 3 * d**3 + 2 * lepton**3 + electron**3)
assert sp.expand(cubic + 18 * (u - 2) * (u + 4)) == 0
print("UNIVERSAL ANOMALY REDUCTION:")
print("  Yl/Yq=-3, Ye/Yq=6, (Yu+Yd)/Yq=-2")
print("  cubic=-18*(Yu/Yq-2)*(Yu/Yq+4)")
print("  ratios are SM up to u<->d, independently of E6: PASS")
print("SCOPE VERDICT: selected trinification frames realize the universal ratio theorem;")
print("the frame, physical 15-plet, gauging and overall normalization are not selected.")
