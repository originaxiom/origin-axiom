#!/usr/bin/env python3
"""B1895 -- what the second convention of B1881 is, and the least apex over every run sequence.

Data-free: integers modulo 5, and the record's flat-fibre instrument on run sequences at 50 digits.  No value of tau on record is
read and nothing is compared with a measured number.  B1881's script is imported for its own functions (the two tests of 'keeps the
line', the heights); nothing of any other session's code is run.

Computed once.  Main had computed each of these numbers at the keyboard before this script was written, so nothing here was
predicted before it was seen, and the script says so.

PART A.  The seat's convention: rows, the letters L = [[1,0],[1,1]] and R = [[1,1],[0,1]], the mark v = (1,3).  B1881's second
convention: columns, the letters [[1,1],[0,1]] and [[1,0],[1,1]], the mark (1,2).  A mend of Review 79 called the second the
transpose of the first.  What is computed here:
  A1  every word of the second is the seat's word conjugated by the swap J of the two coordinates, the order of the letters kept;
  A2  it is not the transpose: the seat's ground is symmetric, and the swapped word differs from the transposed word;
  A3  the row v annihilates one line of columns, the line of v itself, and the second mark is J applied to it;
  A4  a row is kept by a matrix exactly when the column it annihilates is kept: all 120 matrices of SL2 mod 5, each of the six lines;
  A5  so the row test on W is the column test on J W J, on all 120;
  A6  a control: for a mark that does not annihilate its own line, 'the swapped mark on the swapped matrix' is another test;
  A7  the reversed sequence: the second word on it is the transpose of the seat's word conjugated by J, and a row is kept by W
      exactly when the same vector as a column is kept by the transpose of W, for every line.
PART B.  The least apex.  B1881 found the least over 16,275 sequences to be the ground's own, sqrt5/2.  A reading of that arc added
a bound that makes it the least over every sequence.  By hand: x = 1/[a; ...] lies strictly between 1/(a + 1) and 1/a, a being the
next run.  A sequence with a run of 3 or more reads above 3/2 at that run.  A sequence of ones and twos with a two reads above
(2 + 1/3 + 1/3)/2 = 4/3 at a two.  And sqrt5/2 < 4/3.  So every sequence that is not all ones reads above 4/3, and the ground's
sqrt5/2 is the least and is reached only by the ground.  Computed here:
  B1  the ingredient, at every run of every sequence tried;
  B2  the all-ones sequences read sqrt5/2; every other reads above 4/3, and above 3/2 if it has a run of 3 or more;
  B3  the least among the others in the range tried, and where.
"""
import importlib.util
import itertools
import json
import pathlib

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location("b1881_script", ROOT / "frontier" / "B1881_the_whole_and_the_value_verified" / "verification" / "whole_and_value_on_main.py")
S = importlib.util.module_from_spec(spec)
spec.loader.exec_module(S)
OUT, RES, FAILS = [], {}, []


def P(*a):
    s = " ".join(str(x) for x in a)
    OUT.append(s)
    print(s)


def check(name, ok, detail=""):
    RES[name] = bool(ok)
    if not ok:
        FAILS.append(name)
    P("   [%s] %s%s" % ("ok" if ok else "FAILS", name, (" -- " + str(detail)) if detail else ""))


def mul5(A, B):
    return ((A[0] * B[0] + A[1] * B[2]) % 5, (A[0] * B[1] + A[1] * B[3]) % 5, (A[2] * B[0] + A[3] * B[2]) % 5, (A[2] * B[1] + A[3] * B[3]) % 5)


J, I2 = (0, 1, 1, 0), (1, 0, 0, 1)
swap = lambda g: mul5(mul5(J, g), J)
tr = lambda g: (g[0], g[2], g[1], g[3])
row = lambda v, g: ((v[0] * g[0] + v[1] * g[2]) % 5, (v[0] * g[1] + v[1] * g[3]) % 5)
col = lambda g, v: ((g[0] * v[0] + g[1] * v[1]) % 5, (g[2] * v[0] + g[3] * v[1]) % 5)
line = lambda w: min(((k * w[0]) % 5, (k * w[1]) % 5) for k in (1, 2, 3, 4))
kept_row = lambda v, g: line(row(v, g)) == line(v)
kept_col = lambda g, u: line(col(g, u)) == line(u)
VECS = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]
LINES = sorted({line(w) for w in VECS})
annihilated = lambda v: sorted({line(u) for u in VECS if (v[0] * u[0] + v[1] * u[1]) % 5 == 0})


def group():
    grp, todo = {I2}, [I2]
    while todo:
        g = todo.pop()
        for h in (mul5(g, (0, 4, 1, 0)), mul5(g, (1, 1, 0, 1))):
            if h not in grp:
                grp.add(h); todo.append(h)
    return grp


def part_a():
    P("PART A. THE SECOND CONVENTION")
    G = group()
    V = S.V
    second = line(col(J, annihilated(V)[0]))
    seqs = [seq for n in (2, 4) for seq in itertools.product(range(1, 7), repeat=n)]
    words = {}
    for seq in seqs:
        W = I2
        for k, r in enumerate(seq):
            W = mul5(W, (1, 0, r % 5, 1) if k % 2 == 0 else (1, r % 5, 0, 1))
        words[seq] = W
    check("the group has 120 matrices and the %d run sequences of length 2 and 4 with runs to 6 reach all of them" % len(seqs), len(G) == 120 and set(words.values()) == G, len(set(words.values())))
    check("A1 B1881's first test is 'the row v is kept by the seat's word W', on every sequence", all(S.keeps_line_seat(list(q)) == kept_row(V, W) for q, W in words.items()))
    check("A1 B1881's second test is 'the column (1,2) is kept by J W J', the same word conjugated by the swap, on every sequence",
          all(S.keeps_line_main(list(q)) == kept_col(swap(W), second) for q, W in words.items()), "the second mark, computed: %s" % (second,))
    ground = mul5((1, 0, 1, 1), (1, 1, 0, 1))
    d_word = sum(swap(W) != tr(W) for W in words.values())
    d_test = sum(kept_col(swap(W), second) != kept_col(tr(W), second) for W in words.values())
    check("A2 the seat's ground is symmetric: its transpose is itself, and the second ground is its conjugate by the swap and another matrix",
          row(V, ground) == ((-V[0]) % 5, (-V[1]) % 5) and tr(ground) == ground and swap(ground) == (2, 1, 1, 1) and swap(ground) != ground, (ground, swap(ground)))
    check("A2 the swapped word is not the transposed word: they differ on %d of the %d sequences, and the two tests they give differ on %d" % (d_word, len(seqs), d_test), d_word > 0 and d_test > 0)
    check("A3 the row v = %s annihilates one line of columns, and it is the line of v itself" % (V,), annihilated(V) == [line(V)], annihilated(V))
    check("A3 the second mark is the swap of that column: J (2,1) = (1,2), and it is another line than the mark's", col(J, (2, 1)) == (1, 2) and line((2, 1)) == line(V) and second == (1, 2) != line(V))
    a4 = {v: sum(kept_row(v, g) == kept_col(g, annihilated(v)[0]) for g in G) for v in LINES}
    check("A4 a row is kept by a matrix exactly when the column it annihilates is kept: 120 of 120 for each of the six lines", len(LINES) == 6 and all(len(annihilated(v)) == 1 for v in LINES) and set(a4.values()) == {120}, a4)
    a5 = sum(kept_row(V, g) == kept_col(swap(g), second) for g in G)
    check("A5 so the row test on W is the column test on J W J: 120 of 120", a5 == 120, a5)
    controls = {}
    for c in LINES:
        if annihilated(c) != [c]:
            controls[c] = sum(kept_row(c, g) == kept_col(swap(g), line(col(J, c))) for g in G)
    own = [c for c in LINES if annihilated(c) == [c]]
    check("A6 the lines that annihilate themselves are two, the mark's and the second mark's; for each of the other four the same recipe gives another test",
          sorted(own) == sorted([line(V), second]) and len(controls) == 4 and all(n < 120 for n in controls.values()), controls)
    a7 = all(S.keeps_line_main(list(q)[::-1]) == kept_col(swap(tr(W)), second) for q, W in words.items())
    a7b = all(kept_row(v, g) == kept_col(tr(g), v) for v in LINES for g in G)
    check("A7 on the reversed sequence the second word is the transpose of W conjugated by the swap; a row is kept by W exactly when the same column is kept by its transpose, for every line", a7 and a7b)
    RES["A_numbers"] = {"sequences": len(seqs), "matrices": len(G), "swapped_word_differs_from_transposed": d_word, "tests_differ": d_test, "row_and_annihilated_column": {str(k): v for k, v in a4.items()},
                        "row_test_equals_column_test_on_swapped": a5, "controls": {str(k): v for k, v in controls.items()}, "lines_that_annihilate_themselves": [list(x) for x in own]}


def part_b():
    P("")
    P("PART B. THE LEAST APEX")
    mp.mp.dps = 50
    s5 = mp.sqrt(5) / 2
    seqs = [seq for n, top in ((2, 6), (4, 6), (6, 3)) for seq in itertools.product(range(1, top + 1), repeat=n)]
    ingredient, apex = True, {}
    for seq in seqs:
        q, n = list(seq), len(seq)
        for i in range(n):
            fwd = [q[(i + 1 + k) % n] for k in range(n)]
            x = 1 / S.cf_value(fwd)
            ingredient = ingredient and (mp.mpf(1) / (fwd[0] + 1) < x < mp.mpf(1) / fwd[0])
        apex[seq] = max(S.heights(q))
    check("B1 at every run of the %d sequences tried (length 2 and 4 with runs to 6, length 6 with runs to 3), 1/(a + 1) < x < 1/a for the next run a" % len(seqs), ingredient)
    ones = [q for q in seqs if set(q) == {1}]
    others = sorted((a, q) for q, a in apex.items() if set(q) != {1})
    check("B2 the %d all-ones sequences read sqrt5/2, to 1e-45" % len(ones), len(ones) == 3 and all(abs(apex[q] - s5) < mp.mpf(10) ** -45 for q in ones))
    check("B2 every other sequence reads above 4/3, and sqrt5/2 is below 4/3", all(a > mp.mpf(4) / 3 for a, q in others) and s5 < mp.mpf(4) / 3, "%d others" % len(others))
    big = [a for a, q in others if max(q) >= 3]
    check("B2 every sequence with a run of 3 or more reads above 3/2", len(big) > 0 and min(big) > mp.mpf(3) / 2, "%d of them; the least %s" % (len(big), mp.nstr(min(big), 10)))
    least = others[0]
    check("B3 the least among the others, in the range tried, is sqrt2, at the sequences of twos", abs(least[0] - mp.sqrt(2)) < mp.mpf(10) ** -45 and set(least[1]) == {2}
          and all(set(q) == {2} for a, q in others if abs(a - least[0]) < mp.mpf(10) ** -45), "%s at %s" % (mp.nstr(least[0], 12), least[1]))
    RES["B_numbers"] = {"sequences": len(seqs), "all_ones": len(ones), "others": len(others), "least_among_the_others": mp.nstr(least[0], 12), "at": list(least[1]),
                        "with_a_run_of_three_or_more": len(big), "least_of_those": mp.nstr(min(big), 12)}


if __name__ == "__main__":
    part_a()
    part_b()
    P("")
    n = sum(1 for v in RES.values() if isinstance(v, bool))
    P("CHECKS: %d, FAILING: %d%s" % (n, len(FAILS), (" -- " + "; ".join(FAILS)) if FAILS else ""))
    (HERE / "second_convention_and_least_apex.json").write_text(json.dumps(RES, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    (HERE / "second_convention_and_least_apex_run.txt").write_text("\n".join(OUT) + "\n", encoding="utf-8")
