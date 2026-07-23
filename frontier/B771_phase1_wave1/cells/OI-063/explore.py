"""OI-063 exploration -- general-gamma sector decomposition of the WRT trace.

Chain (generalizing B204 r=2 -> all words):
  tr rho_n(gamma) = (const)*(2/n)^{r/2} * Ztil(n),
  Ztil(n) = sum_{p in [1..n-1]^r} prod_i e^{i pi q_i p_i^2/(2n)} * prod_i sin(pi p_i p_{i+1}/n)
  (cyclic word gamma ~ prod_i T^{q_i} S, r letters).
  Full-period extension (each var, sin-form invariant under p -> 2n-p, vanishes at 0,n):
  Ztil = (1/2^r) sum_{p in (Z/2n)^r} ... ;  sin-expansion into 2^r sign patterns eps,
  orbits under vertex flips = 2 classes by prod(eps), sizes 2^{r-1}:
  Ztil = (2^{r-1}/(2i)^r) [ s_+ G(Q_+;2n) + s_- G(Q_-;2n) ],  s_cls = prod(eps).
  det Q_cls = +-(t-2) / +-(t+2)  [to verify].
  Reciprocity (Krazer/Turaev, N=2n even):
  G(Q;2n) = (2n)^{r/2} e^{i pi sig(Q)/4}/sqrt|det Q| * sum_{y in Z^r/QZ^r} e^{-2 pi i n q(y)},
  q(y) = y^T adj(Q) y / det(Q) mod 1  -> frequency counts (m mod t-+2) -> exact period analysis.
"""
import numpy as np
from math import gcd
from fractions import Fraction
from functools import reduce
import itertools, cmath, sys

# ---------------- SL(2,Z) word machinery ----------------
def matmul2(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

T = [[1, 1], [0, 1]]
S = [[0, -1], [1, 0]]

def Tpow(q):
    return [[1, q], [0, 1]]

def factor_ST(M):
    """B216 factorization: gamma = prod T^{q_i} S * T^m * (S^2 if e==-1). Returns ops,(e,m)."""
    M = [[int(M[0][0]), int(M[0][1])], [int(M[1][0]), int(M[1][1])]]
    ops = []
    while M[1][0] != 0:
        a, c = M[0][0], M[1][0]
        q = int(round(a / c))
        M = [[a - q * M[1][0], M[0][1] - q * M[1][1]], [M[1][0], M[1][1]]]
        M = [[M[1][0], M[1][1]], [-M[0][0], -M[0][1]]]
        ops.append(q)
    return ops, (M[0][0], M[0][1])

def cyclic_word(M):
    """cyclic q-word: gamma == +- prod_i T^{q_i} S  (absorb the final T^m by cyclicity).
    Returns (qs, sign) with prod T^{q_i}S == sign * gamma."""
    ops, (e, m) = factor_ST(M)
    # rho = prod T^{q_i}S then T^m (e=1) or S^2 T^{-m} (e=-1); S^2=-I in SL2
    qs = list(ops)
    mm = m if e == 1 else -m
    if not qs:
        raise ValueError("no S letters (parabolic/triangular?)")
    qs[0] += mm
    W = [[1, 0], [0, 1]]
    for q in qs:
        W = matmul2(W, matmul2(Tpow(q), S))
    sign = None
    if W == M:
        sign = 1
    else:
        Mm = [[-M[0][0], -M[0][1]], [-M[1][0], -M[1][1]]]
        if W == Mm:
            sign = -1
    return qs, sign

def content(M):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    return reduce(gcd, [abs(b), abs(c), abs(a - d)])

def lcm(a, b):
    return a * b // gcd(a, b)

def law_period(M):
    t = abs(M[0][0] + M[1][1])
    return lcm(t - 2, t + 2) // content(M)

# ---------------- ground truth: B216 rho_mat trace ----------------
def rho_trace_abs(M, k):
    n = k + 2
    j = np.arange(k + 1)
    Smat = np.sqrt(2.0 / n) * np.sin(np.pi * np.outer(j + 1, j + 1) / n)
    Td = np.exp(1j * np.pi * ((j + 1) ** 2 / (2.0 * n)))
    ops, (e, m) = factor_ST(M)
    rho = np.eye(k + 1, dtype=complex)
    for q in ops:
        rho = rho @ np.diag(Td ** q) @ Smat
    rho = rho @ np.diag(Td ** m) if e == 1 else rho @ (Smat @ Smat) @ np.diag(Td ** (-m))
    return abs(np.trace(rho))

# ---------------- sector forms ----------------
def build_Q(qs, eps):
    """cyclic form: diag q_i, edge couplings eps_i on (i,i+1 mod r); r=1,2 degenerate handled."""
    r = len(qs)
    Q = [[0] * r for _ in range(r)]
    for i in range(r):
        Q[i][i] = qs[i]
    for i in range(r):
        j = (i + 1) % r
        if i == j:
            Q[i][i] += 2 * eps[i]
        else:
            Q[i][j] += eps[i]
            Q[j][i] += eps[i]
    return Q

def det_int(Q):
    import copy
    A = [row[:] for row in Q]
    n = len(A)
    # fraction-free Bareiss
    sign = 1
    prev = 1
    for i in range(n - 1):
        if A[i][i] == 0:
            for kk in range(i + 1, n):
                if A[kk][i] != 0:
                    A[i], A[kk] = A[kk], A[i]
                    sign = -sign
                    break
            else:
                return 0
        for j in range(i + 1, n):
            for kk in range(i + 1, n):
                A[j][kk] = (A[j][kk] * A[i][i] - A[j][i] * A[i][kk]) // prev
            A[j][i] = 0
        prev = A[i][i]
    return sign * A[n - 1][n - 1]

def smith_with_left(Q):
    """SNF: returns (diag s, Ainv) with A Q B = diag(s), Ainv = A^{-1} integer;
    quotient Z^r/QZ^r = {A^{-1} w : w_i mod s_i}."""
    import sympy as sp
    M = sp.Matrix(Q)
    r = M.shape[0]
    A = sp.eye(r); B = sp.eye(r)
    Mw = M[:, :]
    def minpos(Mw):
        best = None
        for i in range(r):
            for j in range(r):
                v = Mw[i, j]
                if v != 0 and (best is None or abs(v) < abs(Mw[best[0], best[1]])):
                    best = (i, j)
        return best
    t0 = 0
    while t0 < r:
        sub = Mw[t0:, t0:]
        if all(sub[i, j] == 0 for i in range(r - t0) for j in range(r - t0)):
            break
        while True:
            piv = None
            bestabs = None
            for i in range(t0, r):
                for j in range(t0, r):
                    v = Mw[i, j]
                    if v != 0 and (bestabs is None or abs(v) < bestabs):
                        bestabs = abs(v); piv = (i, j)
            i0, j0 = piv
            if i0 != t0:
                Mw = Mw.elementary_row_op('n<->m', row1=t0, row2=i0)
                A = sp.Matrix(sp.eye(r)).elementary_row_op('n<->m', row1=t0, row2=i0) * A
            if j0 != t0:
                Mw = Mw.elementary_col_op('n<->m', col1=t0, col2=j0)
                B = B * sp.Matrix(sp.eye(r)).elementary_col_op('n<->m', col1=t0, col2=j0)
            done = True
            for i in range(t0 + 1, r):
                q = Mw[i, t0] // Mw[t0, t0]
                if q != 0 or Mw[i, t0] != 0:
                    Mw = Mw.elementary_row_op('n->n+km', row=i, k=-q, row2=t0)
                    A = sp.Matrix(sp.eye(r)).elementary_row_op('n->n+km', row=i, k=-q, row2=t0) * A
                    if Mw[i, t0] != 0:
                        done = False
            for j in range(t0 + 1, r):
                q = Mw[t0, j] // Mw[t0, t0]
                if q != 0 or Mw[t0, j] != 0:
                    Mw = Mw.elementary_col_op('n->n+km', col=j, k=-q, col2=t0)
                    B = B * sp.Matrix(sp.eye(r)).elementary_col_op('n->n+km', col=j, k=-q, col2=t0)
                    if Mw[t0, j] != 0:
                        done = False
            if done:
                offdiag = any(Mw[i, t0] != 0 for i in range(t0 + 1, r)) or \
                          any(Mw[t0, j] != 0 for j in range(t0 + 1, r))
                if not offdiag:
                    break
        t0 += 1
    s = [int(Mw[i, i]) for i in range(r)]
    Ainv = A.inv()
    assert all(x == int(x) for x in Ainv), "Ainv not integer"
    return s, [[int(Ainv[i, j]) for j in range(r)] for i in range(r)]

def sector_freqs(Q):
    """frequency counts of the dual sum: dict {Fraction f mod 1: count}, f = y^T Q^{-1} y mod 1."""
    import sympy as sp
    r = len(Q)
    D = det_int(Q)
    Qs = sp.Matrix(Q)
    adj = Qs.adjugate()
    s, Ainv = smith_with_left(Q)
    ranges = [range(abs(x)) if x != 0 else [0] for x in s]
    counts = {}
    for w in itertools.product(*ranges):
        y = [sum(Ainv[i][j] * w[j] for j in range(r)) for i in range(r)]
        num = 0
        for i in range(r):
            for j in range(r):
                num += y[i] * int(adj[i, j]) * y[j]
        f = Fraction(num, D) % 1
        counts[f] = counts.get(f, 0) + 1
    return counts

def signature(Q):
    ev = np.linalg.eigvalsh(np.array(Q, dtype=float))
    return int(np.sum(ev > 0) - np.sum(ev < 0))

# ---------------- per-gamma analysis ----------------
def analyze(M, nwin=None, verbose=True):
    t = M[0][0] + M[1][1]
    assert t > 2
    qs, sgn = cyclic_word(M)
    r = len(qs)
    # sector reps: all eps=-1 (prod=(-1)^r) and one flip (prod=(-1)^{r-1})
    epsA = [-1] * r
    epsB = [-1] * (r - 1) + [1]
    QA, QB = build_Q(qs, epsA), build_Q(qs, epsB)
    dA, dB = det_int(QA), det_int(QB)
    dets = sorted([abs(dA), abs(dB)])
    ok_det = (dets == sorted([t - 2, t + 2]))
    # untwisted = |det| = t-2
    if abs(dA) == t - 2:
        Qm, sm, Qp, sp_ = QA, np.prod(epsA), QB, np.prod(epsB)
    else:
        Qm, sm, Qp, sp_ = QB, np.prod(epsB), QA, np.prod(epsA)
    Um = sector_freqs(Qm)   # untwisted, denom t-2
    Vp = sector_freqs(Qp)   # twisted, denom t+2
    sigm, sigp = signature(Qm), signature(Qp)
    # reconstruction check: |Z(n)| = C * |P-(n) + zeta8^delta * P+(n)| for some delta in 0..7
    if nwin is None:
        nwin = list(range(8, 40))
    zvals = np.array([rho_trace_abs(M, n - 2) for n in nwin])
    Pm = np.array([sum(c * cmath.exp(-2j * cmath.pi * n * float(f)) for f, c in Um.items())
                   for n in nwin]) / np.sqrt(t - 2)
    Pp = np.array([sum(c * cmath.exp(-2j * cmath.pi * n * float(f)) for f, c in Vp.items())
                   for n in nwin]) / np.sqrt(t + 2)
    best = None
    for delta in range(8):
        Fv = np.abs(Pm + np.exp(1j * np.pi * delta / 4) * Pp)
        mask = Fv > 1e-9
        if mask.sum() == 0:
            continue
        C = np.sum(zvals[mask] * Fv[mask]) / np.sum(Fv[mask] ** 2)
        err = np.max(np.abs(zvals - C * Fv))
        if best is None or err < best[1]:
            best = (delta, err, C)
    delta, err, C = best
    return dict(M=M, t=t, r=r, qs=qs, sgn=sgn, ok_det=ok_det, detm=dA if abs(dA)==t-2 else dB,
                detp=dA if abs(dA)==t+2 else dB, Um=Um, Vp=Vp, sigm=sigm, sigp=sigp,
                delta=delta, err=err, C=C, content=content(M), law=law_period(M))

def show(res):
    Um = {str(f): c for f, c in sorted(res['Um'].items())}
    Vp = {str(f): c for f, c in sorted(res['Vp'].items())}
    print(f"gamma={res['M']} t={res['t']} content={res['content']} law={res['law']}")
    print(f"  word r={res['r']} qs={res['qs']} sign={res['sgn']} ok_det={res['ok_det']} "
          f"det-={res['detm']} det+={res['detp']} sig-={res['sigm']} sig+={res['sigp']}")
    print(f"  U-(freqs mod 1, x(t-2)): {Um}")
    print(f"  V+(freqs mod 1, x(t+2)): {Vp}")
    print(f"  reconstruction: delta={res['delta']} C={res['C']:.6f} maxerr={res['err']:.2e}")

if __name__ == "__main__":
    tests = [
        [[2, 1], [1, 1]],            # t=3, content 1
        [[3, 1], [2, 1]],            # t=4? det=1: 3*1-2=1 ok t=4 content gcd(1,2,2)=1
        [[5, 2], [2, 1]],            # R^2L^2 t=6 content 2
        [[7, 3], [2, 1]],            # t=8 content 1
        [[13, -8], [-8, 5]],         # GAMMA_A t=18 content 8
        [[17, -4], [-4, 1]],         # GAMMA_B t=18 content 4
        [[10, 3], [3, 1]],           # R^3L^3 t=11 content 3
        [[7, 5], [4, 3]],            # t=10 content 1
    ]
    for M in tests:
        try:
            res = analyze(M)
            show(res)
        except Exception as ex:
            print(f"gamma={M} FAILED: {ex}")
        print()
