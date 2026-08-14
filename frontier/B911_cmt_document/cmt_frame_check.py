#!/usr/bin/env python3
"""B911 -- frame check: the Killing geometry of the four superselection charges
(ledger LI KF1-KF3), recomputed exactly on the banked B854 build.

Checks: (a) the 4x4 Killing Gram K(g_a, g_b) is DIAGONAL (Killing-orthogonal
frame); (b) the signs are (+,-,+,-) on (g8,g14,g16,g22) -- the noncompact pair
{g8,g16} positive, the compact pair {g14,g22} negative (the (2,2) signature and
the compact/noncompact split); (c) det of the Gram is minus... i.e. sign
(+)(-)(+)(-) = +, and modulo squares det is a perfect square (KF3's all-even
exponent claim is normalization-invariant: rescaling charges multiplies det by
a square). Norm VALUES are normalization-bound (solo norms differ by squares);
the squarefree kernels of the norms are the invariant content per charge.

Exact throughout (integer Killing Gram on the Chevalley basis, sparse trace).
"""
import json
import os
import time
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))
T0 = time.time()


def log(m):
    print(f"[{time.time()-T0:7.1f}s] {m}", flush=True)


log("exec of the banked B854 build ...")
src = open(B854, encoding="utf-8").read()
g = {"__file__": os.path.join(HERE, "b854_rerun_frame.py"), "__name__": "b854f"}
exec(compile(src, B854, "exec"), g)
DIM, N = g["DIM"], g["N"]
ROOTS, BB, INV, C = g["ROOTS"], g["BB"], g["INV"], g["C"]
if os.path.exists(os.path.join(HERE, "results.json")):
    os.remove(os.path.join(HERE, "results.json"))   # b854's rerun artifact; the
    # main cell already archived an identical copy as b854_rerun_results.json

log("exact Killing Gram on the Chevalley basis (sparse trace) ...")
K = [[0] * DIM for _ in range(DIM)]
for i in range(N):
    for j in range(N):
        K[i][j] = sum((sum(r[k] * C[i][k] for k in range(N)))
                      * (sum(r[k] * C[j][k] for k in range(N)))
                      for r in ROOTS)
for ri, r in enumerate(ROOTS):
    mr = tuple(-x for x in r)
    mi = ROOTS.index(mr)
    tr = Fr(0)
    for k in range(DIM):
        w = BB[N + mi][k]
        acc = Fr(0)
        for pdx, wp in enumerate(w):
            if wp:
                acc += wp * BB[N + ri][pdx][k]
        tr += acc
    assert tr.denominator == 1
    K[N + ri][N + mi] = int(tr)

# sanity: Killing rank must be 78 (nondegenerate) -- check mod two primes
for p in (40739, 40751):
    rows = [[K[i][j] % p for j in range(DIM)] for i in range(DIM)]
    rk, rr, m = 0, rows, DIM
    R = [row[:] for row in rows]
    rank = 0
    for col in range(DIM):
        piv = next((i for i in range(rank, DIM) if R[i][col] % p), None)
        if piv is None:
            continue
        R[rank], R[piv] = R[piv], R[rank]
        inv = pow(R[rank][col], p - 2, p)
        R[rank] = [x * inv % p for x in R[rank]]
        for i in range(DIM):
            if i != rank and R[i][col]:
                f = R[i][col]
                R[i] = [(a - f * b) % p for a, b in zip(R[i], R[rank])]
        rank += 1
    log(f"  Killing rank mod {p}: {rank} (must be 78)")
    assert rank == DIM

CH = {n: INV[n] for n in (8, 14, 16, 22)}
names = [8, 14, 16, 22]
G = sp.zeros(4, 4)
for a in range(4):
    for b in range(4):
        va, vb = CH[names[a]], CH[names[b]]
        acc = Fr(0)
        for i, vi in enumerate(va):
            if not vi:
                continue
            for j, vj in enumerate(vb):
                if vj and K[i][j]:
                    acc += vi * vj * K[i][j]
        G[a, b] = sp.Rational(acc.numerator, acc.denominator)

log("charge Gram K(g_a, g_b):")
for a in range(4):
    log("  " + "  ".join(str(G[a, b]) for b in range(4)))
diag = all(G[a, b] == 0 for a in range(4) for b in range(4) if a != b)
signs = [sp.sign(G[a, a]) for a in range(4)]
det = (G[0, 0] * G[1, 1] * G[2, 2] * G[3, 3]) if diag else G.det()
det_num = sp.Rational(det)
sq = sp.sqrt(det_num)
kernels = {}
for a in range(4):
    v = sp.Rational(G[a, a])
    fac = sp.factorint(v.p) | {k: -e for k, e in sp.factorint(v.q).items()}
    kernels[names[a]] = sorted(int(k) for k, e in fac.items()
                               if k > 0 and e % 2 == 1)
res = dict(
    gram_diagonal=bool(diag),
    diag_signs=[int(x) for x in signs],
    signature_2_2_noncompact_g8_g16_positive=(signs == [1, -1, 1, -1]),
    det=str(det_num),
    det_is_rational_square=bool((sq).is_rational),
    norm_squarefree_kernels={str(k): v for k, v in kernels.items()},
    diag_norms={str(names[a]): str(G[a, a]) for a in range(4)})
log(f"diagonal: {diag}; signs (g8,g14,g16,g22) = {signs} (expect +,-,+,-)")
log(f"det = {det_num}; det is a rational square: {res['det_is_rational_square']}")
log(f"norm squarefree kernels: {res['norm_squarefree_kernels']}")
json.dump(res, open(os.path.join(HERE, "cmt_frame_results.json"), "w"),
          indent=1, sort_keys=True)
log("DONE.")
