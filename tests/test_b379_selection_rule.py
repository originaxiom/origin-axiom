"""Locks for B379 — the reduction + closed form (fast: banked-data + the two traces)."""

import json
import os
import sys
from fractions import Fraction as Fr

BASE = os.path.join(os.path.dirname(__file__), "..", "frontier")
BANKED = json.load(open(os.path.join(BASE, "B367_value_map", "step0_tables.json")))["1,2"]


def test_row16_sqrt5_dark():
    assert BANKED["16,0"] == ["1/24", "1/120", "0", "0"]
    assert BANKED["16,4"] == ["5/48", "-1/240", "0", "0"]
    assert BANKED["16,8"] == ["5/48", "-1/240", "0", "0"]


def test_rigid_rank1_sign_pattern():
    s = {c: Fr(BANKED[c][3]) for c in ("6,2", "6,10", "14,2", "14,10")}
    assert abs(s["6,2"]) == Fr(1, 48)
    assert s["6,2"] == -s["6,10"] == -s["14,2"] == s["14,10"]


def test_t2_traces_exact():
    """The two closed-form traces, recomputed exactly (the load-bearing lock)."""
    sys.path.insert(0, os.path.join(BASE, "B367_value_map"))
    sys.path.insert(0, os.path.join(BASE, "B358_seam_certification"))
    import cyclo_engine as E
    import seam_certification as SC
    from step0_exact_matrices import build_theta_W, matrix_order
    N = 15
    W1, W2 = build_theta_W(1), build_theta_W(2)
    o1, pow1 = matrix_order(W1)
    o2, pow2 = matrix_order(W2)

    def proj(powers, o, zstep, a):
        M = [[E.ZERO] * N for _ in range(N)]
        for j in range(o):
            c = E.scal(Fr(1, o), E.zeta((-zstep * j * a) % 60))
            for i in range(N):
                for k in range(N):
                    if powers[j][i][k] != E.ZERO:
                        M[i][k] = E.add(M[i][k], E.mul(c, powers[j][i][k]))
        return M

    Par = [[E.ONE if i == (-j) % N else E.ZERO for j in range(N)] for i in range(N)]

    def msub(A, B):
        return [[E.sub(A[i][j], B[i][j]) for j in range(N)] for i in range(N)]

    def tr(M):
        t = E.ZERO
        for i in range(N):
            t = E.add(t, M[i][i])
        return t

    H1 = msub(proj(pow1, o1, 3, 6), proj(pow1, o1, 3, 14))
    H2 = msub(proj(pow2, o2, 5, 2), proj(pow2, o2, 5, 10))
    slot = SC.solve_H(SC.H_avg(tr(E.mmul(E.mmul(Par, H1), H2))))
    assert tuple(slot) == (Fr(0), Fr(0), Fr(-1, 12), Fr(-1, 12))
    H1t = msub(proj(pow1, o1, 3, 0), proj(pow1, o1, 3, 4))
    H2t = msub(proj(pow2, o2, 5, 4), proj(pow2, o2, 5, 8))
    blk = SC.solve_H(SC.H_avg(tr(E.mmul(E.mmul(Par, H1t), H2t))))
    assert tuple(blk) == (Fr(0), Fr(0), Fr(-1, 12), Fr(1, 12))


def test_gram_spectrum_exact():
    """The seam form's Gram spectrum: {1/576 x2, 1/768, 23/19200} exactly."""
    S = [[Fr(0)] * 12 for _ in range(20)]
    for k, v in BANKED.items():
        a, b = (int(x) for x in k.split(","))
        S[a][b] = Fr(v[3])
    G = [[sum(S[i][a] * S[i][b] for i in range(20)) for b in range(12)] for a in range(12)]
    n = 12
    I = [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    def mm(X, Y):
        return [[sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    Bk, cs = I, [Fr(1)]
    for k in range(1, n + 1):
        AB = mm(G, Bk)
        ck = -Fr(sum(AB[i][i] for i in range(n)), k)
        cs.append(ck)
        Bk = [[AB[i][j] + (ck if i == j else 0) for j in range(n)] for i in range(n)]
    lam = Fr(1, 576)
    p = lambda x: x**4 + cs[1]*x**3 + cs[2]*x**2 + cs[3]*x + cs[4]
    dp = lambda x: 4*x**3 + 3*cs[1]*x**2 + 2*cs[2]*x + cs[3]
    assert p(lam) == 0 and dp(lam) == 0                      # the exact doublet
    assert p(Fr(1, 768)) == 0 and p(Fr(23, 19200)) == 0      # the rational pair
