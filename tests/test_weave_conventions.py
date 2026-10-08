"""The weave dossier's conventions, enforced (docs/dossiers/the_weave_2026-10-07/CONVENTIONS.md).

Step 2 of the assurance plan the owner approved on 2026-10-08. Each test pins one convention the dossier's scripts rely
on, so that a script that silently changes one fails here rather than in a result.
"""
import itertools
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "docs" / "dossiers" / "the_weave_2026-10-07"
sys.path.insert(0, str(HERE))

import the_common_point as CP  # noqa: E402
import the_chiral_triplet as CT  # noqa: E402
import the_mixing_patterns_verified as MV  # noqa: E402


def h1(phi):
    cols = []
    for g in (1, 2):
        v = [0, 0]
        for x in phi[g]:
            v[abs(x) - 1] += 1 if x > 0 else -1
        cols.append(v)
    return np.array(cols).T


def up_to_phase(A, B, phases=(1, -1, 1j, -1j)):
    return min(float(np.max(abs(A - s * B))) for s in phases) < 1e-9


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)


def test_section1_words_and_matrices():
    assert CP.AUT["L"] == {1: [1], 2: [1, 2]} and CP.AUT["R"] == {1: [1, 2], 2: [2]}
    assert CP.AUT["P"] == {1: [2], 2: [1]} and CP.AUT["-I"] == {1: [-1], 2: [-2]}
    for m in ("L", "R", "P", "-I"):
        assert h1(CP.AUT[m]).tolist() == [list(r) for r in CP.MAT[m]], m
    lr = CP.word_aut("LR", 1)
    assert lr == CP.compose(CP.AUT["L"], CP.AUT["R"])                       # word_aut("LR") = L o R
    assert h1(lr).tolist() == [[2, 1], [1, 1]]
    for w in ("LR", "RRL", "LRLRR", "LLRLRR"):                               # h1 is a homomorphism
        M = np.eye(2, dtype=int)
        for c in w:
            M = M @ np.array(CP.MAT[c])
        assert h1(CP.word_aut(w, 1)).tolist() == M.tolist(), w


def test_section2_lifts_and_the_right_action():
    gL, gR = CP.extend(CP.AUT["L"]), CP.extend(CP.AUT["R"])
    assert len(gL) == 2 and len(gR) == 2
    assert np.allclose(np.array(gL[0]), -np.array(gL[1]))
    lr = CP.word_aut("LR", 1)
    glr = CP.extend(lr)
    prod = qmul(gL[0], gR[0])                                                # the lift of L o R is g_L g_R
    assert any(np.allclose(np.array(prod), s * np.array(g)) for g in glr for s in (1, -1))
    A, B = CT.on_V(CP.AUT["L"], gL[0]), CT.on_V(CP.AUT["R"], gR[0])
    C = CT.on_V(lr, glr[0])
    assert up_to_phase(C, B @ A) and not up_to_phase(C, A @ B)               # a right action
    # MV.word reads its string the other way: word("LR") = on_V(L) on_V(R) = the action of R o L = word_aut("RL")
    W = MV.word({"L": A, "R": B}, "LR")
    rl = CP.word_aut("RL", 1)
    assert np.allclose(W, A @ B)
    assert any(up_to_phase(W, CT.on_V(rl, g)) for g in CP.extend(rl))


def test_section2_reversal_is_a_rotation_only_for_short_words():
    """the reverse of a word names the same thread exactly when it is a cyclic rotation of the word"""
    def rotations(w):
        return {w[i:] + w[:i] for i in range(len(w))}
    for w in ("L", "R", "RL", "RRL", "RRLL"):
        assert w[::-1] in rotations(w), w
    assert "LLRLRR"[::-1] not in rotations("LLRLRR")                         # a reversal pair: the conventions differ


def test_section3_the_modulus():
    """the geometric action on W21's period ratio is the period rule tau -> (delta tau + beta)/(gamma tau + alpha); the
    standard Moebius rule used before the correction equals the period rule on the reversed word"""
    w = np.exp(2j * np.pi / 3)
    U = h1({1: [2], 2: [-1, 2]})
    assert U.tolist() == [[0, -1], [1, 1]]
    std = lambda M, t: (M[0][0] * t + M[0][1]) / (M[1][0] * t + M[1][1])
    per = lambda M, t: (M[1][1] * t + M[0][1]) / (M[1][0] * t + M[0][0])
    assert abs(std(U, w) - w) < 1e-12 and abs(per(U, w) - w) > 1e-3        # the two rules disagree on U ...
    assert abs(per(U, w + 1) - (w + 1)) < 1e-12                             # ... U fixes omega + 1 under the period rule
    Lm, Rm = np.array(CP.MAT["L"]), np.array(CP.MAT["R"])
    LUL = (Lm @ U @ np.linalg.inv(Lm)).round().astype(int)
    assert LUL.tolist() == [[1, -1], [1, 0]] and abs(per(LUL, w) - w) < 1e-12
    t = 0.3 + 1.1j
    for word in ("LR", "RRL", "LRLRR"):
        M, Mrev = np.eye(2, dtype=int), np.eye(2, dtype=int)
        for c in word:
            M = M @ np.array(CP.MAT[c])
        for c in word[::-1]:
            Mrev = Mrev @ np.array(CP.MAT[c])
        assert abs(std(M, t) - per(Mrev, t)) < 1e-12, word
    for n in range(2, 9):                                                    # positive words with both letters: trace >= 3
        for t in itertools.product("LR", repeat=n):
            if "L" in t and "R" in t:
                M = np.eye(2, dtype=int)
                for c in t:
                    M = M @ np.array(CP.MAT[c])
                assert int(np.trace(M)) >= 3


def test_section4_theta_branches():
    import mpmath as mp
    import the_zero_modes_weight as ZW
    z, t = complex(0.13, 0.07), complex(0.23, 1.07)
    q = mp.exp(1j * mp.pi * t)
    assert abs(ZW.th(1, z, t) - mp.jtheta(1, mp.pi * z, q)) < 1e-15        # inside the strip they agree
    t1 = t + 1                                                               # |Re t1| > 1: mpmath's principal q^(1/4) slips
    q1 = mp.exp(1j * mp.pi * t1)
    assert abs(ZW.th(1, z, t1) - mp.exp(1j * mp.pi / 4) * ZW.th(1, z, t)) < 1e-12
    assert abs(mp.jtheta(1, mp.pi * z, q1) - ZW.th(1, z, t1)) > 1e-3


def test_section5_the_normal_form_values():
    d = json.loads((HERE / "the_couplings_exact.json").read_text(encoding="utf-8"))
    ks = {w: v["c = exp(2 pi i k/24), k"] for w, v in d["the residual elements"].items()}
    assert ks == {"L": 21, "R": 3, "RL": 0, "RRL": 3}


def test_section6_hypercharge():
    Y = np.diag([-1 / 3, -1 / 3, -1 / 3, 1 / 2, 1 / 2])
    Z = np.diag([-2, -2, -2, 3, 3])
    assert np.allclose(Z, 6 * Y)
    assert np.isclose(np.trace(Y), 0)


def test_section7_no_stringified_booleans_in_the_dossier_json():
    bad = []
    for f in sorted(HERE.glob("*.json")):
        def walk(x):
            if isinstance(x, dict):
                return any(walk(v) for v in x.values())
            if isinstance(x, list):
                return any(walk(v) for v in x)
            return x in ("True", "False")
        if walk(json.loads(f.read_text(encoding="utf-8"))):
            bad.append(f.name)
    assert not bad, bad
