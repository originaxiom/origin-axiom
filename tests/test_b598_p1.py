"""B598-P1 — the cusp table (OA_SLOW lock: the exact B575 build ~9 min).

Self-contained recomputation of the m=1 block's Fox H1 and peripheral values
against the banked table. See frontier/B598_l85_campaign/FINDINGS.md (P1).
"""
import importlib.util
import os
import sys
from fractions import Fraction as Fr

import pytest

if not os.environ.get("OA_SLOW"):
    pytest.skip("B598-P1 lock requires OA_SLOW=1 (the exact B575 build)",
                allow_module_level=True)

_ROOT = os.path.join(os.path.dirname(__file__), "..")
_L51 = os.path.join(_ROOT, "frontier", "B575_bridge_obstruction", "l51_obstruction.py")
_spec = importlib.util.spec_from_file_location("l51lockmod", _L51)
m5 = importlib.util.module_from_spec(_spec)
_argv = sys.argv
sys.argv = [_L51]
try:
    _spec.loader.exec_module(m5)
finally:
    sys.argv = _argv

K0, K1 = m5.K0, m5.K1
REL = m5.REL


def _mat_vec(M, v):
    return [sum((M[i][j] * v[j] for j in range(len(v)) if not v[j].is_zero()), K0)
            for i in range(len(M))]


def _mat_mul(X, Y):
    n, m, p = len(X), len(Y), len(Y[0])
    out = [[K0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            x = X[i][k]
            if x.is_zero():
                continue
            for j in range(p):
                y = Y[k][j]
                if not y.is_zero():
                    out[i][j] = out[i][j] + x * y
    return out


def _fox_pair(acts, d):
    I = [[K1 if i == j else K0 for j in range(d)] for i in range(d)]
    Da = [[K0] * d for _ in range(d)]
    Db = [[K0] * d for _ in range(d)]
    P = I
    for ch in REL:
        if ch == 'a':
            for i in range(d):
                for j in range(d):
                    Da[i][j] = Da[i][j] + P[i][j]
        elif ch == 'A':
            PA = _mat_mul(P, acts['A'])
            for i in range(d):
                for j in range(d):
                    Da[i][j] = Da[i][j] - PA[i][j]
        elif ch == 'b':
            for i in range(d):
                for j in range(d):
                    Db[i][j] = Db[i][j] + P[i][j]
        else:
            PB = _mat_mul(P, acts['B'])
            for i in range(d):
                for j in range(d):
                    Db[i][j] = Db[i][j] - PB[i][j]
        P = _mat_mul(P, acts[ch])
    return Da, Db


def _rank(rows):
    if not rows:
        return 0
    _, piv = m5.rref([list(r) for r in rows])
    return len(piv)


def _cocycle_eval(acts, xa, xb, word):
    d = len(xa)
    val = [K0] * d
    P = [[K1 if i == j else K0 for j in range(d)] for i in range(d)]
    for ch in word:
        if ch == 'a':
            inc = xa
        elif ch == 'b':
            inc = xb
        elif ch == 'A':
            inc = [K0 - v for v in _mat_vec(acts['A'], xa)]
        else:
            inc = [K0 - v for v in _mat_vec(acts['B'], xb)]
        val = [val[i] + v for i, v in enumerate(_mat_vec(P, inc))]
        P = _mat_mul(P, acts[ch])
    return val


def test_m1_cusp_row():
    D = m5.BLOCK_DATA[1]
    d, acts = D['d'], D['acts']
    Da, Db = _fox_pair(acts, d)
    big = [[Da[i][j] for j in range(d)] + [Db[i][j] for j in range(d)]
           for i in range(d)]
    sols = m5.nullspace(big)
    cobs = []
    for j in range(d):
        e = [K1 if i == j else K0 for i in range(d)]
        ca = [e[i] - v for i, v in enumerate(_mat_vec(acts['a'], e))]
        cb = [e[i] - v for i, v in enumerate(_mat_vec(acts['b'], e))]
        cobs.append(ca + cb)
    rank_cob = _rank(cobs)
    assert len(sols) - rank_cob == 1                     # dim H1 = 1
    rep = next(s for s in sols if _rank(cobs + [list(s)]) > rank_cob)
    xa, xb = list(rep[:d]), list(rep[d:])
    piv = next(i for i, v in enumerate(xa) if not v.is_zero())
    sc = xa[piv].inv()
    xa = [sc * v for v in xa]
    xb = [sc * v for v in xb]
    lam = _cocycle_eval(acts, xa, xb, "baBA")
    # banked m=1 row: xi(mu) = [1, 0, 3/8 - w/8]; xi(lam) = [3/4+3w/4, 1/4+w/4, -w/2]
    assert xa[0].a == 1 and xa[0].b == 0 and xa[1].is_zero()
    assert xa[2].a == Fr(3, 8) and xa[2].b == Fr(-1, 8)
    assert lam[0].a == Fr(3, 4) and lam[0].b == Fr(3, 4)
    assert lam[1].a == Fr(1, 4) and lam[1].b == Fr(1, 4)
    assert lam[2].a == 0 and lam[2].b == Fr(-1, 2)
