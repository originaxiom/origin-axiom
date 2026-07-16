"""B644 locks — the ear = the mod-5 congruence shadow (L94)."""
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
B644 = os.path.join(HERE, "..", "frontier", "B644_mckay_comparison")


def _m5mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % 5
                       for j in range(2)) for i in range(2))


def test_mod5_group_is_sl25():
    R5, L5, I5 = ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((1, 0), (0, 1))
    g5 = {I5}
    fr = [I5]
    while fr:
        new = []
        for M in fr:
            for G in (R5, L5):
                M2 = _m5mul(M, G)
                if M2 not in g5:
                    g5.add(M2)
                    new.append(M2)
        fr = new
    assert len(g5) == 120
    # the cat map RL mod 5 has order 10 (the pentagon's arithmetic source)
    RL = _m5mul(R5, L5)
    P, o = ((1, 0), (0, 1)), 0
    for k in range(1, 61):
        P = _m5mul(P, RL)
        if P == ((1, 0), (0, 1)):
            o = k
            break
    assert o == 10


def test_observed_table_is_golden_irreducible_character():
    phi = (1 + sp.sqrt(5)) / 2
    obs = {(1, None): (1, sp.Integer(2)), (2, None): (1, sp.Integer(-2)),
           (4, None): (30, sp.Integer(0)), (3, None): (20, sp.Integer(-1)),
           (6, None): (20, sp.Integer(1)), (5, True): (12, 1 / phi),
           (5, False): (12, -phi), (10, True): (12, -1 / phi),
           (10, False): (12, phi)}
    assert sum(sz for sz, _ in obs.values()) == 120
    for q in (True, False):
        assert sp.simplify(obs[(10, q)][1] + obs[(5, q)][1]) == 0
    assert sp.simplify(
        sum(sz * ch ** 2 for sz, ch in obs.values()) / 120) == 1


def test_b644_banked_run():
    out = open(os.path.join(B644, "b644_output.txt")).read()
    assert "kernel mismatches: 0/560" in out
    assert "class-function well-defined: True" in out
    assert "class (10, True)" in out and "-0.6180339887498948" in out
    fnd = open(os.path.join(B644, "FINDINGS.md")).read()
    assert "sealing error, disclosed" in fnd  # the M3 adjudication is in
    assert "NEEDS-SPECIALIST" in fnd


def test_b644_artifact_hashes_live():
    import hashlib
    d = B644
    for line in open(os.path.join(d, "ARTIFACT_HASHES.txt")):
        parts = line.split()
        if len(parts) == 2 and len(parts[0]) == 64:
            h, fn = parts
            got = hashlib.sha256(
                open(os.path.join(d, fn), "rb").read()).hexdigest()
            assert got == h, fn
