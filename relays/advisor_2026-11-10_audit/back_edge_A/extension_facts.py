#!/usr/bin/env python3
"""Exact facts used by the design note for back-edge A (data-free; integers only; SnapPy optional for the H_1 check).
For a history W (a word in L, R) acting on the fibre's H_1 = Z^2:
  - a fibre character chi extends over the mapping torus as a flat line bundle iff W* chi = chi:   |det(W - I)| of them
  - it extends as the rank-2 bundle chi + chi^-1 (the pair, with the swap) iff W* chi = chi^-1:      |det(W + I)| of them
At level N the question is the action of W on (Z/N)^2.
    python3 relays/advisor_2026-11-10_audit/back_edge_A/extension_facts.py"""
from itertools import product
L = ((1, 1), (0, 1)); R = ((1, 0), (1, 1)); I2 = ((1, 0), (0, 1))
mul = lambda A, B: tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def word(w):
    M = I2
    for ch in w: M = mul(M, L if ch == "L" else R)
    return M
def runs_to_word(runs):                      # (6) -> the departure L^6 in place of one L, inside the golden word
    return "".join(("L" if i % 2 == 0 else "R") * r for i, r in enumerate(runs))
det = lambda M: M[0][0] * M[1][1] - M[0][1] * M[1][0]
tr = lambda M: M[0][0] + M[1][1]
def fixed_lines(M, N, sign):
    """vectors v in (Z/N)^2 of exact order N with M v = sign * v, counted as +-pairs (lines)."""
    out = set()
    for a, b in product(range(N), repeat=2):
        from math import gcd
        if gcd(gcd(a, b), N) != 1: continue
        w = ((M[0][0] * a + M[0][1] * b) % N, (M[1][0] * a + M[1][1] * b) % N)
        if w == ((sign * a) % N, (sign * b) % N): out.add(min((a, b), ((-a) % N, (-b) % N)))
    return sorted(out)
print("the golden background LR:", word("LR"), "tr", tr(word("LR")))
print("  |det(LR - I)| =", abs(det(tuple(tuple(word('LR')[i][j] - I2[i][j] for j in range(2)) for i in range(2)))),
      "  |det(LR + I)| =", abs(det(tuple(tuple(word('LR')[i][j] + I2[i][j] for j in range(2)) for i in range(2)))))
print("  lines of order 5 with LR v = +v:", fixed_lines(word("LR"), 5, 1), " with LR v = -v:", fixed_lines(word("LR"), 5, -1))
v = fixed_lines(word("LR"), 5, -1)
print("\nhistories: the golden word with one departure (runs of the departure), closed with k golden periods")
print("%-26s %-5s %-9s %-9s %-10s %s" % ("history", "tr", "|det W-I|", "|det W+I|", "W mod 5", "order-5 points v (as +-pairs) with W v = +v | with W v = -v"))
cases = {"(6)": "LLLLLLR", "(2,1,2,1,2)": "LLRLLRLLR", "(2,1,1,1,2)": "LLRLRLLR", "golden LR": "LR"}
for name, dep in cases.items():
    for k in (1, 2, 3):
        W = word(dep + "LR" * k) if name != "golden LR" else word("LR" * (k + 1))
        Wm = tuple(tuple(W[i][j] - I2[i][j] for j in range(2)) for i in range(2))
        Wp = tuple(tuple(W[i][j] + I2[i][j] for j in range(2)) for i in range(2))
        W5 = tuple(tuple(x % 5 for x in row) for row in W)
        tag = "+I" if W5 == ((1, 0), (0, 1)) else "-I" if W5 == ((4, 0), (0, 4)) else "other"
        fp, fm = fixed_lines(W, 5, 1), fixed_lines(W, 5, -1)
        short = lambda f: "all 12" if len(f) == 12 else str(f)
        print("%-26s %-5d %-9d %-9d %-10s %s | %s" % ("%s + (LR)^%d" % (name, k), tr(W), abs(det(Wm)), abs(det(Wp)), tag, short(fp), short(fm)))
try:
    import snappy
    for w in ("LR", "LLLLLLRLR"):
        M = snappy.Manifold("b++" + w)
        print("\nSnapPy b++%s: H_1 = %s (torsion order should be |det(W - I)| = %d)" % (w, M.homology(), abs(det(tuple(tuple(word(w)[i][j] - I2[i][j] for j in range(2)) for i in range(2))))))
except Exception as exc:
    print("\nSnapPy check skipped:", repr(exc)[:80])
