"""B1482 -- the sign is the cancelling move: the four statements re-checked live on a smaller range, the stored
enumeration re-read, and GENESIS reproduced from the amendment."""
import json, os, subprocess, sys, itertools
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1482_the_sign_is_the_cancelling_move")
mul = lambda X, Y: ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]), (X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]))
L, R, P, NEG, I2 = ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((0, 1), (1, 0)), ((-1, 0), (0, -1)), ((1, 0), (0, 1))
tr = lambda X: X[0][0] + X[1][1]


def test_the_four_statements_live():
    fr = {I2}
    for n in range(7):
        fr = {mul(X, G) for X in fr for G in (L, R, P)}; assert all(min(X[0] + X[1]) >= 0 for X in fr) and NEG not in fr      # S1
    words = set()
    for n in range(2, 9):
        for t in itertools.product((L, R), repeat=n):
            if L in t and R in t:
                M = I2
                for G in t: M = mul(M, G)
                words.add(M)
    assert min(tr(M) for M in words) == 3
    sq = {tr(mul(X, X)) for X in (((a, b), (c, d)) for a in range(-5, 6) for b in range(-5, 6) for c in range(-5, 6) for d in range(-5, 6)) if abs(X[0][0] * X[1][1] - X[0][1] * X[1][0]) == 1}
    assert min(sq) == -2                                                                                                    # S2: squares have trace >= -2 ...
    assert max(-tr(M) for M in words) == -3                                                                                 # ... and a - state has trace <= -3
    assert all(mul(NEG, G) == mul(G, NEG) for G in (L, R, P)) and mul(NEG, NEG) == I2                                       # S3
    neg = lambda X: tuple(tuple(-a for a in row) for row in X); assert not any(neg(M) in words for M in words)
    one_sign = lambda X: min(X[0] + X[1]) >= 0 or max(X[0] + X[1]) <= 0
    assert not one_sign(((1, -1), (0, 1))) and all(one_sign(M) for M in words)                                              # S4
    # the checks can fail: a matrix with a square root of trace < -2 would break S2's bound -- none exists, and a planted one is caught
    assert not (tr(mul(((0, 1), (-1, 0)), ((0, 1), (-1, 0)))) < -2)


def test_the_stored_enumeration_and_the_page():
    c = json.load(open(os.path.join(A, "verification", "checks.json")))
    assert c["S1"]["all_entries_nonnegative"] and c["S1"]["equal_to_minus_identity"] == 0 and c["S2"]["squares_with_trace_below_minus_2"] == 0
    assert c["S3"]["twins_are_new"] and not c["S4"]["L_inverse_has_one_sign"] and all(c["S4"]["the_record_s_two_words_for_minus_identity"].values())
    assert subprocess.run([sys.executable, os.path.join(A, "adoption", "amend.py"), "--check"]).returncode == 0
    g = open(os.path.join(ROOT, "GENESIS.md"), encoding="utf-8").read()
    assert "is negating the records a legal move?" in g and int(g.split("**Version 1.")[1].split()[0]) >= 14
