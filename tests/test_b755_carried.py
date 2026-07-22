"""Locks for B755 -- the five carried recomputes (B140/B332/B685/B720/S019)."""
import os
from itertools import permutations

import sympy as sp

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ARC = os.path.join(ROOT, "frontier", "B755_carried_recomputes")


def _read(name):
    with open(os.path.join(ARC, name), encoding="utf-8") as fh:
        return fh.read()


def test_cell1_b140_genus2_witness():
    out = _read("cell1_out.txt")
    assert "CHECK: WITNESSED -- genus-2 chiral bundle 'abcDef'" in out
    assert "=> chiral True; isometry-orientation route => True" in out
    assert "CS+CSm = +0.00e+00" in out


def test_cell2_b332_quarter_not_distinguished():
    out = _read("cells245_out.txt")
    assert "window 2%: 1/4 hits 0: []" in out
    assert "window 5%: 1/4 hits 0: []" in out
    assert "CELL 2 VERDICT: 1/4 NOT DISTINGUISHED" in out


def test_cell4_b720_object_side_halves_exact():
    # (i) Q(zeta3) and Q(i) linearly disjoint
    x, y = sp.symbols("x y")
    comp = sp.Poly(sp.resultant(sp.expand((x - y) ** 2 + (x - y) + 1),
                                sp.expand(y**2 + 1), y), x)
    assert comp.degree() == 4
    # (ii) the Markov quiver's mutation class has size 1 and is not ADE (+-2 entries)
    def mutate(B, k):
        n = len(B)
        return [[-B[i][j] if (i == k or j == k)
                 else B[i][j] + (abs(B[i][k]) * B[k][j] + B[i][k] * abs(B[k][j])) // 2
                 for j in range(n)] for i in range(n)]

    def canon(B):
        n = len(B)
        return min(tuple(tuple(B[p[i]][p[j]] for j in range(n)) for i in range(n))
                   for p in permutations(range(n)))

    markov = [[0, 2, -2], [-2, 0, 2], [2, -2, 0]]
    seen, front = {canon(markov)}, [markov]
    while front:
        B = front.pop()
        for k in range(3):
            c = canon(mutate(B, k))
            if c not in seen:
                seen.add(c)
                front.append(mutate(B, k))
    assert len(seen) == 1
    assert all(v == 0 or abs(v) == 2 for row in markov for v in row)


def test_cell5_s019_fisher_positive_and_tombstone_repaired():
    m, t = sp.symbols("m t", positive=True)
    M2 = sp.Matrix([[m, 1], [1, 0]]) ** 2
    cp = t**2 - sp.trace(M2) * t + M2.det()
    disc2 = sp.discriminant(cp, t)
    assert sp.simplify(16 / disc2 - 16 / (m**2 * (m**2 + 4))) == 0
    tomb = open(os.path.join(ROOT, "speculations", "TOMBSTONES.md"), encoding="utf-8").read()
    assert "citation repaired 2026-07-22, B755 cell 5" in tomb
    assert "holds by dimension" in tomb


def test_cell3_b685_gswz_gates_and_pure3():
    out = _read("cell3_out.txt")
    assert "r_1 = 11/24" in out and "r_2 = 697/1152" in out
    assert "r_4 = 278392949/39813120" in out
    assert "r_5 = 244284791741/6688604160" in out
    assert "GATES: r1 = 11/24 exact, r2 = 697/1152 exact" in out
    for frag in ("[eq(2): -1/27 -> MATCH]", "[eq(2): 1/27 -> MATCH]",
                 "[eq(2): -4/243 -> MATCH]", "[eq(2): -1/243 -> MATCH]"):
        assert frag in out
    assert "CHECK2: all denominators through u^5 are pure powers of 3: True" in out
    assert "CELL 3 FINAL VERDICT: PURE-3 CONFIRMED to order u^5" in out


def test_verification_addendum_independent_algebra():
    from fractions import Fraction as F
    rs = [F(11, 24), F(697, 1152), F(724351, 414720), F(278392949, 39813120),
          F(244284791741, 6688604160)]
    n = 6
    prod = [F(0)] * n
    for j in range(6):
        for k in range(6):
            if j + k >= n or (j + k) % 2 == 1:
                continue
            aj = rs[j - 1] if j else F(1)
            ak = rs[k - 1] if k else F(1)
            prod[j + k] += aj * ak * ((-1) ** k) * (F(-1, 27) ** ((j + k) // 2))
    logc = [F(0)] + [F((-1) ** (i + 1), i) for i in range(1, n)]
    powers = {0: [F(1)] + [F(0)] * (n - 1)}
    for m in range(1, n):
        prev = powers[m - 1]
        cur = [F(0)] * n
        for i in range(n):
            for j2 in range(n - i):
                cur[i + j2] += prev[i] * logc[j2]
        powers[m] = cur
    out = [F(0)] * n
    for m in range(n):
        if prod[m] == 0:
            continue
        for i in range(n):
            out[i] += prod[m] * powers[m][i]
    assert [str(c) for c in out] == ["1", "0", "-1/27", "1/27", "-4/243", "-1/243"]
