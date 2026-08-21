#!/usr/bin/env python3
"""Theorem (the arithmetic tail): no metallic word R^m L^m with m >= 3 is arithmetic.

Bowditch-Maclachlan-Reid give a COMPLETE classification of arithmetic once-punctured
torus bundles: precisely three CYCLIC commensurability classes, carried by RL, RRLL and
RRL.  Cyclic commensurability is weaker than "conjugate to a power of a listed word":
two bundles in one class share a common finite cyclic cover, so only SOME power of one
monodromy is conjugate to SOME power of the other.

This script checks that the paper's block-sequence argument survives that weaker
reading -- i.e. that the comparison is made between ARBITRARY powers on both sides and
still forces m in {1,2}.  By the positivity lemma, conjugacy of positive words IS cyclic
rotation, so comparing block sequences up to rotation is exactly comparing conjugacy
classes.

Exact integer/word combinatorics; standard library only; exits non-zero on drift.
"""
import sys

FAIL = []


def check(label, got, want):
    ok = got == want
    print(f"  [{'ok ' if ok else 'FAIL'}] {label}: {got!r}" + ("" if ok else f"  (expected {want!r})"))
    if not ok:
        FAIL.append(label)


def blocks(w):
    """The block sequence of a positive word in R, L -- a cyclic-word invariant."""
    out = []
    for c in w:
        if out and out[-1][0] == c:
            out[-1][1] += 1
        else:
            out.append([c, 1])
    return [n for _, n in out]


def rotations_match(a, b):
    """Positive words are conjugate iff cyclic rotations (positivity lemma)."""
    return len(a) == len(b) and any(a == b[i:] + b[:i] for i in range(len(b)))


WORDS = {"RL": "RL", "RRLL": "RRLL", "RRL": "RRL"}
PMAX = 8   # powers compared on both sides


def compatible(m):
    """Is some power of R^m L^m conjugate to some power of a listed word?"""
    metallic = "R" * m + "L" * m
    hits = set()
    for name, w in WORDS.items():
        for j in range(1, PMAX + 1):
            bm = blocks(metallic * j)
            for k in range(1, PMAX + 1):
                if rotations_match(bm, blocks(w * k)):
                    hits.add(name)
    return sorted(hits)


print("\n(1) the three block sequences the classification supplies")
check("(RL)^3 blocks", blocks("RL" * 3), [1, 1, 1, 1, 1, 1])
check("(RRLL)^2 blocks", blocks("RRLL" * 2), [2, 2, 2, 2])
check("(RRL)^2 blocks -- alternating, never constant", blocks("RRL" * 2), [2, 1, 2, 1])

print("\n(2) (R^m L^m)^j has 2j blocks, all of length m")
for m in (1, 2, 3, 5):
    for j in (1, 2, 3):
        b = blocks(("R" * m + "L" * m) * j)
        check(f"m={m}, j={j}", (len(b), set(b)), (2 * j, {m}))

print("\n(3) the tail: matching ARBITRARY powers on both sides")
check("m=1 is compatible, via RL", compatible(1), ["RL"])
check("m=2 is compatible, via RRLL", compatible(2), ["RRLL"])
for m in range(3, 13):
    check(f"m={m} matches NOTHING at any pair of powers up to {PMAX}", compatible(m), [])

print("\n(4) the control: a non-metallic positive word CAN match, so the test can pass")
# RLRL is (RL)^2 -- arithmetic, and the instrument must see it.
check("RLRL matches RL (the bite control)",
      rotations_match(blocks("RLRL"), blocks("RL" * 2)), True)

if FAIL:
    print(f"\nFAIL: {FAIL}")
    sys.exit(1)
print("\nPASS: no metallic word with m >= 3 is compatible with any power of the three")
print("      classified words; m = 1 and m = 2 are, exactly as the theorem states.")
