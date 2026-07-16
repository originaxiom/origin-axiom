"""B649 locks — the exact silver holonomy over L (mathematical, snappy-free)."""
import json
import os
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
B649 = os.path.join(HERE, "..", "frontier", "B649_silver_holonomy")

MOD = [Fr(16), Fr(0), Fr(8), Fr(0)]  # s^4 = 16 + 8 s^2


def _pmulred(p, q):
    out = [Fr(0)] * 7
    for i, a in enumerate(p):
        if a == 0:
            continue
        for j, b in enumerate(q):
            out[i + j] += a * b
    for k in range(6, 3, -1):
        c = out[k]
        if c != 0:
            out[k] = Fr(0)
            for t, m in enumerate(MOD):
                out[k - 4 + t] += c * m
    return out[:4]


class L:
    def __init__(self, re=None, im=None):
        self.re = re or [Fr(0)] * 4
        self.im = im or [Fr(0)] * 4
    def __add__(self, o):
        return L([a + b for a, b in zip(self.re, o.re)],
                 [a + b for a, b in zip(self.im, o.im)])
    def __sub__(self, o):
        return L([a - b for a, b in zip(self.re, o.re)],
                 [a - b for a, b in zip(self.im, o.im)])
    def __mul__(self, o):
        rr, ii = _pmulred(self.re, o.re), _pmulred(self.im, o.im)
        ri, ir = _pmulred(self.re, o.im), _pmulred(self.im, o.re)
        return L([a - b for a, b in zip(rr, ii)],
                 [a + b for a, b in zip(ri, ir)])
    def is_zero(self):
        return all(c == 0 for c in self.re + self.im)


def _lc(q):
    return L([Fr(q), Fr(0), Fr(0), Fr(0)], None)


def _load():
    d = json.load(open(os.path.join(B649, "entries_L.json")))
    mats = {}
    for nm in "abc":
        mats[nm] = [[L([Fr(x) for x in d[f"{nm}{i}{j}"][0]],
                       [Fr(x) for x in d[f"{nm}{i}{j}"][1]])
                     for j in range(2)] for i in range(2)]
    return mats


def _mm(X, Y):
    return [[X[i][0] * Y[0][j] + X[i][1] * Y[1][j] for j in range(2)]
            for i in range(2)]


def _inv(M):
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    assert (det - _lc(1)).is_zero()
    return [[M[1][1], _lc(0) - M[0][1]], [_lc(0) - M[1][0], M[0][0]]]


def test_silver_holonomy_exact():
    mats = _load()
    lets = dict(mats)
    for nm in "abc":
        lets[nm.upper()] = _inv(mats[nm])

    def word(w):
        m = None
        for ch in w:
            m = lets[ch] if m is None else _mm(m, lets[ch])
        return m

    for rel in ("aBAbcc", "aaCbcB"):
        R = word(rel)
        assert R[0][1].is_zero() and R[1][0].is_zero()
        assert (R[0][0] - _lc(1)).is_zero() and (R[1][1] - _lc(1)).is_zero()
    # peripheral traces: mu = CCB tr = 2; lam = caCA tr = -2
    for w, t in (("CCB", 2), ("caCA", -2)):
        W = word(w)
        assert ((W[0][0] + W[1][1]) - _lc(t)).is_zero(), w
    # tr(ac) = -sqrt2 - sqrt2 i with sqrt2 = (s^2-4)/4
    s2 = L([Fr(-1), Fr(0), Fr(1, 4), Fr(0)], None)
    iL = L(None, [Fr(1), Fr(0), Fr(0), Fr(0)])
    W = word("ac")
    assert ((W[0][0] + W[1][1]) + s2 + s2 * iL).is_zero()
    W = word("abc")
    assert ((W[0][0] + W[1][1]) + _lc(2) * s2 * iL).is_zero()


def test_silver_27_letters_exact():
    """Stage 2b lock: reload the lifted letters and re-verify one
    relator + the mu trace exactly over L (pure Fractions)."""
    import json
    d = json.load(open(os.path.join(B649, "letters27_L.json")))

    def mat(nm):
        return [[L([Fr(x) for x in d[nm][i][j][:4]],
                   [Fr(x) for x in d[nm][i][j][4:]])
                 for j in range(27)] for i in range(27)]

    lets = {nm: mat(nm) for nm in "abcABC"}

    def mm27(A, B):
        n = 27
        Bt = list(zip(*B))
        out = [[None] * n for _ in range(n)]
        for i in range(n):
            nz = [(k, A[i][k]) for k in range(n) if not A[i][k].is_zero()]
            for j in range(n):
                acc = L()
                for k, a in nz:
                    b = Bt[j][k]
                    if not b.is_zero():
                        acc = acc + a * b
                out[i][j] = acc
        return out

    W = None
    for ch in "aBAbcc":
        W = lets[ch] if W is None else mm27(W, lets[ch])
    one = L([Fr(1), Fr(0), Fr(0), Fr(0)], None)
    for i in range(27):
        for j in range(27):
            tgt = one if i == j else L()
            assert (W[i][j] - tgt).is_zero(), (i, j)
    MU = None
    for ch in "CCB":
        MU = lets[ch] if MU is None else mm27(MU, lets[ch])
    tr = L()
    for i in range(27):
        tr = tr + MU[i][i]
    assert (tr - L([Fr(27), Fr(0), Fr(0), Fr(0)], None)).is_zero()


def test_stage3a_dimensions_banked():
    out = open(os.path.join(B649, "b649_stage3a_output.txt")).read()
    assert "invertible weld intertwiner FOUND" in out
    assert "dEDeff: = I27 exactly: True" in out
    assert "ddFefE: = I27 exactly: True" in out
    assert "rank B1 = 26; h0(D) = 1; h1(D) = 5" in out
    assert "h0 = 1; h1 = 3" in out
    fnd = open(os.path.join(B649, "FINDINGS.md")).read()
    assert "OBJECT-INDEPENDENT" in fnd


def test_stage3bi_sigma_matrix():
    """The silver sigma*-matrix: C conj(C) = I exactly and s-free (pure
    fractions from the banked JSON)."""
    import json
    rows = json.load(open(os.path.join(B649, "sigma_matrix_L.json")))
    C = [[L([Fr(x) for x in ent[:4]], [Fr(x) for x in ent[4:]])
          for ent in row] for row in rows]
    one = L([Fr(1), Fr(0), Fr(0), Fr(0)], None)
    for i in range(5):
        for j in range(5):
            acc = L()
            for k in range(5):
                ck = C[k][j]
                acc = acc + C[i][k] * L(ck.re[:], [-x for x in ck.im])
            tgt = one if i == j else L()
            assert (acc - tgt).is_zero(), (i, j)
    for row in C:
        for x in row:
            assert all(x.re[k] == 0 and x.im[k] == 0 for k in (1, 2, 3))
    out = open(os.path.join(B649, "b649_stage3b_swap_output.txt")).read()
    assert "c^2 = 1: True" in out
    assert "cocycle: [True, True, True, True, True]" in out
