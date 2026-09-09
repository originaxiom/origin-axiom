#!/usr/bin/env python3
"""B1236 -- the A1 landing at EXACT multiplet grade (codex R035, re-implemented here, not copied).

Setting. B1098 opened the non-abelian hatch: of the twenty sl2 classes of e6, the minimal A1 has
centralizer su(6) (rank 5) and was recorded "SM-compatible with ONE extra u(1)" -- an embedding
note, no matter content. B280 banked the textbook branching e6 > su(6)+su(2): 27 = (15,1)+(6bar,2).
This cell evaluates the A1 landing's matter content EXACTLY: read the unbroken algebra as the
centralizer su(6), embed su(3)+su(2)+u(1) in it by 6 = (3,1)_a + (1,2)_b + (1,1)_c, and ask
whether 27 = Lambda^2(6) + 2*conj(6) reproduces the SM-shaped 27 as a MULTISET of irreps.

Answer: yes, exactly, and the u(1) direction is UNIQUE within the support constraint. Three
controls type the result. All arithmetic is exact (fractions), no floats anywhere.

Gate 5: nothing here is a measured value. The target is the standard SM-shaped E6 27 (labels,
not numbers); its status is the same as B1100's "banked 6Y multiset".
"""
from collections import Counter
from fractions import Fraction as F

DIM = {"3": 3, "3b": 3, "1": 1, "2": 2}   # colour and weak dimensions


def content_internal(a, b, c):
    """27 restricted to su(3)+su(2)+u(1) INSIDE su(6); 6 = (3,1)_a+(1,2)_b+(1,1)_c; 2_E forgotten."""
    assert 3*a + 2*b + c == 0, "Y must be traceless on the 6"
    out = Counter()
    out[("3b", "1", 2*a)] += 1      # Lambda^2(3) = 3bar
    out[("3", "2", a+b)] += 1       # 3 x 2
    out[("3", "1", a+c)] += 1       # 3 x 1
    out[("1", "1", 2*b)] += 1       # Lambda^2(2) = 1
    out[("1", "2", b+c)] += 1       # 2 x 1
    out[("3b", "1", -a)] += 2       # conj(6) x 2_E, the doublet forgotten -> two copies
    out[("1", "2", -b)] += 2
    out[("1", "1", -c)] += 2
    return out


def content_external(a, b, c, d):
    """The OTHER reading: 2_E itself called weak (the su(6)+su(2)_L embedding); 6 = 3bar_a+1_b+1_c+1_d."""
    assert 3*a + b + c + d == 0
    out = Counter()
    out[("3", "1", 2*a)] += 1                                  # Lambda^2(3bar) = 3
    for v in (b, c, d):
        out[("3b", "1", a+v)] += 1
    for u, v in ((b, c), (b, d), (c, d)):
        out[("1", "1", u+v)] += 1
    out[("3", "2", -a)] += 1                                   # conj(6) x 2_E with 2_E = weak
    for v in (b, c, d):
        out[("1", "2", -v)] += 1
    return out


def dim(cnt):
    return sum(DIM[cc]*DIM[w]*m for (cc, w, _), m in cnt.items())


def histogram(cnt):
    h = Counter()
    for (cc, w, y), m in cnt.items():
        h[y] += DIM[cc]*DIM[w]*m
    return h


TARGET = Counter({("3", "2", F(1, 6)): 1,     # Q
                  ("3b", "1", F(-2, 3)): 1,   # u^c
                  ("3b", "1", F(1, 3)): 2,    # d^c, D^c
                  ("3", "1", F(-1, 3)): 1,    # D
                  ("1", "2", F(-1, 2)): 2,    # L, H_d
                  ("1", "2", F(1, 2)): 1,     # H_u
                  ("1", "1", F(1)): 1,        # e^c
                  ("1", "1", F(0)): 2})       # nu^c, S


def main():
    assert dim(TARGET) == 27
    assert sorted(histogram(TARGET).values(), reverse=True) == [6, 6, 4, 3, 3, 2, 2, 1]  # B1100's pattern

    # (1) the exact hit
    y6 = (F(-1, 3), F(1, 2), F(0))
    hit = content_internal(*y6)
    assert dim(hit) == 27 and hit == TARGET
    print("[1] internal reading, Y6 = diag(-1/3,-1/3,-1/3, 1/2,1/2, 0): 27 -> the SM-shaped 27 EXACTLY (multiset of irreps)")

    # (2) uniqueness within the support constraint: conj(6) x 2_E forces -a, -b, -c into the target's
    #     (3bar,1), (1,2), (1,1) charge sets; tracelessness then leaves TWO triples; ONE gives the target.
    A = {-y for (cc, w, y) in TARGET if cc == "3b" and w == "1"}
    B = {-y for (cc, w, y) in TARGET if cc == "1" and w == "2"}
    C = {-y for (cc, w, y) in TARGET if cc == "1" and w == "1"}
    triples = sorted((a, b, c) for a in A for b in B for c in C if 3*a + 2*b + c == 0)
    hits = [t for t in triples if content_internal(*t) == TARGET]
    assert triples == [(F(-1, 3), F(1, 2), F(0)), (F(2, 3), F(-1, 2), F(-1))]
    assert hits == [y6]
    print("[2] support constraint + tracelessness leave 2 triples; exactly 1 reproduces the target:", hits)

    # (3) control -- charge histogram is NOT the multiplet content: (-1/6, 1/2, -1/2) matches every
    #     charge count and fails at multiplet level (the B1100 "collapse form" is weaker than this cell).
    ctrl = content_internal(F(-1, 6), F(1, 2), F(-1, 2))
    assert histogram(ctrl) == histogram(TARGET) and ctrl != TARGET
    print("[3] control: (-1/6,1/2,-1/2) reproduces the CHARGE HISTOGRAM but not the multiplets -- histogram-level tests are weaker")

    # (4) control -- the external reading (2_E as weak, the su(6)+su(2)_L embedding) ALSO hits the target
    #     abstractly. It is excluded by TYPE, not by content: the A1 is the holonomy's own sl2 and the
    #     unbroken algebra is its CENTRALIZER; a non-abelian factor does not commute with itself.
    ext = content_external(F(-1, 6), F(1, 2), F(1, 2), F(-1, 2))
    assert ext == TARGET
    print("[4] control: the EXTERNAL reading (2_E = weak) also matches abstractly -- excluded by type (2_E is not in its own centralizer), not by content")

    # (5) control -- a diagonal weak su(2) (weak = diag of su(2)_W and 2_E) cannot rescue the external
    #     reading: the internal branch's 2(1,2)_{-1/2} is one (2_W, 2_E), which restricts as 2x2 = 1+3.
    assert hit[("1", "2", F(-1, 2))] == 2
    assert {DIM[w] for (_, w, _) in TARGET} == {1, 2}          # no weak triplet in the target
    print("[5] control: a diagonal weak su(2) turns (2_W,2_E) into 1+3 -- a triplet the target lacks")

    # (6) the extra u(1): the commutant of su(3)+su(2) in su(6) is the block-scalars (x,x,x,y,y,z),
    #     3x+2y+z=0 -> rank 2. Y6 is one direction; X = (1/3, 0, -1) is an independent second.
    X = (F(1, 3), F(0), F(-1))
    assert 3*X[0] + 2*X[1] + X[2] == 0 and y6[0]*X[1] - y6[1]*X[0] != 0
    print("[6] commutant rank 2: hypercharge plus ONE extra u(1) (B1098's note, now with the direction exhibited)")

    print("VERDICT: the A1 landing reproduces the SM-shaped 27 EXACTLY at multiplet grade; Y6 unique within support; "
          "compatibility theorem -- A1 selection, extra-u(1) breaking, chirality, generations, spin, values all OPEN")


if __name__ == "__main__":
    main()
