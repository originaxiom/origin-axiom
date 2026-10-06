"""B1480 -- the index against the sign: the stored tabulation re-read, the amendment reproduced, and the elliptic
involution's word checked live."""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "frontier", "B1480_the_index_against_the_sign")


def test_the_tabulation():
    d = json.load(open(os.path.join(A, "verification", "index_by_sign.json"))); s = d["summary"]; rows = d["rows"]
    assert s["own_level_states"] == 758 and s["by_sign"] == {"+": 379, "-": 379} and s["unknown_amphichirality"] == 0
    assert s["firing_by_sign"] == {"+": 375, "-": 379} and s["generation_by_sign"] == {"+": 49, "-": 46}
    am = [r for r in rows if r["amphichiral"]]; assert len(am) == 68
    assert sum(1 for r in am if r["sign"] == "+" and r["firing"] > 0) == 32 and sum(1 for r in am if r["sign"] == "-" and r["firing"] > 0) == 34
    assert len(s["amphichiral_generation"]["+"]) == 8 and s["amphichiral_generation"]["-"] == ["-LLLRLRLRRR"]
    # Q1 fails on both readings; the criterion could have passed (a planted split passes it)
    ratio = lambda a, b: max(a, b) / max(1, min(a, b))
    assert ratio(375 / 379, 379 / 379) < 1.5 and ratio(49, 46) < 1.5 and ratio(90, 30) > 1.5


def test_genesis_v1_13_is_what_the_amendment_produces():
    assert subprocess.run([sys.executable, os.path.join(A, "adoption", "amend.py"), "--check"]).returncode == 0
    g = open(os.path.join(ROOT, "GENESIS.md"), encoding="utf-8").read()
    assert "RULED BY THE PRINCIPLE" in g and "does the principle generate the sign?" in g and int(g.split("**Version 1.")[1].split()[0]) >= 13


def test_the_elliptic_involution_needs_an_inverse_letter():
    mul = lambda X, Y: [[X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]], [X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]]]
    L, R, Ri = [[1, 1], [0, 1]], [[1, 0], [1, 1]], [[1, 0], [-1, 1]]
    S = mul(mul(L, Ri), L); assert mul(S, S) == [[-1, 0], [0, -1]]
    # no positive word in L, R of length <= 8 equals -I (entries of a positive word are non-negative)
    import itertools
    for n in range(1, 9):
        for w in itertools.product((L, R), repeat=n):
            M = [[1, 0], [0, 1]]
            for X in w: M = mul(M, X)
            assert min(M[0] + M[1]) >= 0
